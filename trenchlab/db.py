"""SQLite storage. Every observation and decision is kept, passes AND kills,
so the Lab can test 'what if this rule were different' later."""
import json
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS pools (
    pool_address    TEXT PRIMARY KEY,
    network         TEXT,
    token_mint      TEXT,
    symbol          TEXT,
    name            TEXT,
    dex             TEXT,
    pool_created_ts REAL,
    first_seen_ts   REAL,
    first_price     REAL,
    first_liq       REAL,
    first_kills     TEXT,
    first_pass_ts   REAL,
    first_pass_price REAL,
    first_pass_score REAL,
    audit_passed    INTEGER,
    audit_kills     TEXT,
    audit_notes     TEXT,
    track_until_ts  REAL
);
CREATE TABLE IF NOT EXISTS observations (
    ts              REAL,
    pool_address    TEXT,
    source          TEXT,
    scout_pass      INTEGER,
    kills           TEXT,
    flags           TEXT,
    score           REAL,
    score_parts     TEXT,
    final_pass      INTEGER,
    metrics         TEXT
);
CREATE INDEX IF NOT EXISTS obs_pool ON observations(pool_address, ts);
CREATE TABLE IF NOT EXISTS samples (
    pool_address    TEXT,
    ts              REAL,
    price_usd       REAL,
    liquidity_usd   REAL,
    PRIMARY KEY (pool_address, ts)
);
CREATE TABLE IF NOT EXISTS clusters (
    token_mint      TEXT,
    ts              REAL,
    research        INTEGER,
    kills           TEXT,
    metrics         TEXT
);
CREATE INDEX IF NOT EXISTS clusters_mint ON clusters(token_mint, ts);
CREATE TABLE IF NOT EXISTS helius_usage (
    day             TEXT PRIMARY KEY,
    credits         INTEGER
);
CREATE TABLE IF NOT EXISTS meta (
    key             TEXT PRIMARY KEY,
    value           TEXT
);
CREATE TABLE IF NOT EXISTS paper_bank (
    id              INTEGER PRIMARY KEY CHECK (id = 1),
    start_usd       REAL,
    cash            REAL,
    created_ts      REAL
);
CREATE TABLE IF NOT EXISTS paper_positions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    pool_address    TEXT,
    token_mint      TEXT,
    symbol          TEXT,
    mode            TEXT,
    entry_ts        REAL,
    cost_usd        REAL,
    tokens          REAL,
    score           REAL,
    entry_info      TEXT,
    last_value      REAL,
    peak_value      REAL,
    misses          INTEGER DEFAULT 0,
    exit_ts         REAL,
    exit_value      REAL,
    exit_reason     TEXT
);
CREATE TABLE IF NOT EXISTS paper_skips (
    ts              REAL,
    pool_address    TEXT,
    symbol          TEXT,
    reason          TEXT
);
CREATE TABLE IF NOT EXISTS paper_equity (
    ts              REAL,
    equity          REAL,
    cash            REAL,
    n_open          INTEGER
);
CREATE TABLE IF NOT EXISTS alerts (
    pool_address    TEXT PRIMARY KEY,
    ts              REAL
);
"""


class DB:
    def __init__(self, path="trenchlab.db"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self._migrate()

    DEX_SWITCH_TS = 1793910600  # 2026-11-05 20:30 UTC: DexScreener became the tracking source

    def _migrate(self):
        done = self.conn.execute("SELECT 1 FROM meta WHERE key='cleanup_dex_v1'").fetchone()
        if not done:
            # Remove impossible readings recorded after the DexScreener switch (data errors, not rugs):
            #  (a) liquidity ~gone while price has not crashed
            #  (b) price up >3x while liquidity grew far less than sqrt(price) (wrong pair orientation)
            rows = self.conn.execute(
                """SELECT s.rowid, s.price_usd, s.liquidity_usd, p.first_price, p.first_liq
                   FROM samples s JOIN pools p ON p.pool_address = s.pool_address
                   WHERE s.ts >= ?""", (self.DEX_SWITCH_TS,)).fetchall()
            bad = [r[0] for r in rows if not self._dex_reading_ok(r[1], r[2], r[3], r[4])]
            for i in range(0, len(bad), 500):
                chunk = bad[i:i + 500]
                self.conn.execute(f"DELETE FROM samples WHERE rowid IN ({','.join('?' * len(chunk))})", chunk)
            self.conn.execute("INSERT INTO meta VALUES ('cleanup_dex_v1', ?)", (str(len(bad)),))
            self.conn.commit()
        if not self.conn.execute("SELECT 1 FROM meta WHERE key='prune_obs_v1'").fetchone():
            n = self.conn.execute(
                """UPDATE observations SET metrics = NULL
                   WHERE scout_pass = 0 AND metrics IS NOT NULL AND pool_address IN
                     (SELECT pool_address FROM pools WHERE COALESCE(first_liq, 0) < 10000)""").rowcount
            self.conn.execute("INSERT INTO meta VALUES ('prune_obs_v1', ?)", (str(n),))
            self.conn.commit()
            self.conn.execute("VACUUM")

    @staticmethod
    def _dex_reading_ok(price, liq, first_price, first_liq):
        if price is None:
            return False
        if not first_price:
            return True
        r = price / first_price
        if liq is not None and liq < 100 and r >= 0.5:
            return False
        if r > 3 and first_liq and liq is not None and (liq / first_liq) < (r ** 0.5) / 4:
            return False
        return True

    def commit(self):
        self.conn.commit()

    def get_pool(self, addr):
        return self.conn.execute("SELECT * FROM pools WHERE pool_address=?", (addr,)).fetchone()

    def upsert_first_seen(self, pool, ts, kills, track_until):
        if self.get_pool(pool.address):
            return False
        self.conn.execute(
            """INSERT INTO pools (pool_address, network, token_mint, symbol, name, dex, pool_created_ts,
               first_seen_ts, first_price, first_liq, first_kills, track_until_ts)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (pool.address, pool.network, pool.token_mint, pool.symbol, pool.name, pool.dex,
             pool.created_ts, ts, pool.price_usd, pool.liquidity_usd, json.dumps(kills), track_until),
        )
        return True

    def mark_first_pass(self, addr, ts, price, score):
        self.conn.execute(
            """UPDATE pools SET first_pass_ts=?, first_pass_price=?, first_pass_score=?
               WHERE pool_address=? AND first_pass_ts IS NULL""",
            (ts, price, score, addr),
        )

    def set_audit(self, addr, passed, kills, notes):
        self.conn.execute(
            "UPDATE pools SET audit_passed=?, audit_kills=?, audit_notes=? WHERE pool_address=?",
            (1 if passed else 0, json.dumps(kills), json.dumps(notes), addr),
        )

    def extend_tracking(self, addr, until):
        self.conn.execute(
            "UPDATE pools SET track_until_ts=MAX(COALESCE(track_until_ts,0), ?) WHERE pool_address=?",
            (until, addr))

    def add_observation(self, ts, pool, scout_pass, kills, flags, score, parts, final_pass, keep_metrics=True):
        """Full market metrics are kept only for pools worth studying (trackable or scout-passing);
        for the thousands of tiny pools a day, the decision and kill reasons are enough."""
        metrics = None
        if keep_metrics:
            metrics = json.dumps({k: v for k, v in pool.to_dict().items() if v not in (None, "", {})},
                                 separators=(",", ":"))
        self.conn.execute(
            "INSERT INTO observations VALUES (?,?,?,?,?,?,?,?,?,?)",
            (ts, pool.address, pool.source, int(scout_pass), json.dumps(kills), json.dumps(flags),
             score, json.dumps(parts) if parts else None, int(final_pass), metrics),
        )

    def add_sample(self, addr, ts, price, liq):
        if price is None:
            return
        self.conn.execute("INSERT OR IGNORE INTO samples VALUES (?,?,?,?)", (addr, ts, price, liq))

    def last_obs_state(self, addr):
        r = self.conn.execute(
            "SELECT scout_pass, final_pass FROM observations WHERE pool_address=? ORDER BY ts DESC LIMIT 1",
            (addr,)).fetchone()
        return None if r is None else (r[0], r[1])

    # ---- paper trader ----
    def ensure_paper_bank(self, start_usd, now=None):
        if self.paper_bank() is None:
            import time as _t
            self.conn.execute("INSERT INTO paper_bank VALUES (1, ?, ?, ?)", (start_usd, start_usd, now or _t.time()))
            self.conn.commit()

    def paper_bank(self):
        return self.conn.execute("SELECT * FROM paper_bank WHERE id=1").fetchone()

    def paper_cash(self):
        r = self.paper_bank()
        return r["cash"] if r else 0.0

    def open_positions(self):
        return self.conn.execute("SELECT * FROM paper_positions WHERE exit_ts IS NULL ORDER BY entry_ts").fetchall()

    def closed_positions(self):
        return self.conn.execute("SELECT * FROM paper_positions WHERE exit_ts IS NOT NULL ORDER BY exit_ts").fetchall()

    def has_open_position(self, pool_address):
        return self.conn.execute("SELECT 1 FROM paper_positions WHERE pool_address=? AND exit_ts IS NULL",
                                 (pool_address,)).fetchone() is not None

    def paper_traded_token(self, mint):
        return self.conn.execute("SELECT 1 FROM paper_positions WHERE token_mint=?", (mint,)).fetchone() is not None

    def paper_realized_today(self, now):
        day = self._day(now)
        rows = self.conn.execute("SELECT exit_ts, exit_value, cost_usd FROM paper_positions WHERE exit_ts IS NOT NULL").fetchall()
        return sum(r["exit_value"] - r["cost_usd"] for r in rows if self._day(r["exit_ts"]) == day)

    def paper_last_loss_ts(self):
        r = self.conn.execute("SELECT MAX(exit_ts) FROM paper_positions WHERE exit_ts IS NOT NULL AND exit_value < cost_usd").fetchone()
        return r[0] if r else None

    def paper_open(self, now, pool, cost, tokens, score, mode, info):
        self.conn.execute("UPDATE paper_bank SET cash = cash - ? WHERE id=1", (cost,))
        cur = self.conn.execute(
            """INSERT INTO paper_positions (pool_address, token_mint, symbol, mode, entry_ts, cost_usd, tokens,
               score, entry_info, last_value, peak_value) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (pool.address, pool.token_mint, pool.symbol, mode, now, cost, tokens, score, json.dumps(info), None, cost))
        self.conn.commit()
        return cur.lastrowid

    def paper_mark(self, pid, value, peak):
        self.conn.execute("UPDATE paper_positions SET last_value=?, peak_value=? WHERE id=?", (value, peak, pid))

    def paper_miss(self, pid):
        self.conn.execute("UPDATE paper_positions SET misses = misses + 1 WHERE id=?", (pid,))
        return self.conn.execute("SELECT misses FROM paper_positions WHERE id=?", (pid,)).fetchone()[0]

    def paper_reset_miss(self, pid):
        self.conn.execute("UPDATE paper_positions SET misses = 0 WHERE id=?", (pid,))

    def paper_close(self, pid, now, value, reason):
        self.conn.execute("UPDATE paper_positions SET exit_ts=?, exit_value=?, exit_reason=?, last_value=? WHERE id=?",
                          (now, value, reason, value, pid))
        self.conn.execute("UPDATE paper_bank SET cash = cash + ? WHERE id=1", (value,))

    def paper_skip(self, now, pool, reason):
        self.conn.execute("INSERT INTO paper_skips VALUES (?,?,?,?)", (now, pool.address, pool.symbol, reason))

    def paper_skip_counts(self):
        rows = self.conn.execute("SELECT reason, COUNT(*) n FROM paper_skips GROUP BY reason ORDER BY n DESC").fetchall()
        return [(r[0].split("(")[0], r[1]) for r in rows]

    def paper_snapshot(self, now, equity, cash, n_open):
        self.conn.execute("INSERT INTO paper_equity VALUES (?,?,?,?)", (now, equity, cash, n_open))

    def paper_snapshots(self):
        return self.conn.execute("SELECT * FROM paper_equity ORDER BY ts").fetchall()

    def latest_sample(self, addr, since):
        return self.conn.execute(
            "SELECT * FROM samples WHERE pool_address=? AND ts>=? ORDER BY ts DESC LIMIT 1", (addr, since)).fetchone()

    def sample_due(self, addr, now, dense_hours=3.0, sparse_minutes=30):
        """Dense sampling (every cycle) for `dense_hours` after first sighting or first pass,
        then one sample per `sparse_minutes`. Keeps the database small enough for 24/7 runs."""
        p = self.get_pool(addr)
        if p is None:
            return True
        if self.has_open_position(addr):
            return True  # open paper positions are priced every cycle
        ref = max(p["first_seen_ts"] or 0, p["first_pass_ts"] or 0)
        if now - ref <= dense_hours * 3600:
            return True
        last = self.conn.execute("SELECT MAX(ts) FROM samples WHERE pool_address=?", (addr,)).fetchone()[0]
        return last is None or now - last >= sparse_minutes * 60 - 30

    def mints_for(self, addrs):
        out = {}
        for i in range(0, len(addrs), 500):
            chunk = addrs[i:i + 500]
            q = ",".join("?" * len(chunk))
            for r in self.conn.execute(f"SELECT pool_address, token_mint FROM pools WHERE pool_address IN ({q})", chunk):
                out[r[0]] = r[1]
        return out

    def sample_is_sane(self, addr, price, liq):
        """Sanity check for DexScreener readings (GeckoTerminal readings are trusted, so genuine
        liquidity pulls still show up). An AMM pool can't lose its liquidity while the price holds,
        and a big price rise must come with liquidity growth (~sqrt of the price move)."""
        p = self.get_pool(addr)
        if p is None:
            return price is not None
        return self._dex_reading_ok(price, liq, p["first_price"], p["first_liq"])

    def tracked_addresses(self, now):
        rows = self.conn.execute(
            "SELECT pool_address FROM pools WHERE track_until_ts >= ?", (now,)).fetchall()
        return [r[0] for r in rows]

    def samples_for(self, addr):
        return self.conn.execute(
            "SELECT ts, price_usd, liquidity_usd FROM samples WHERE pool_address=? ORDER BY ts",
            (addr,)).fetchall()

    def all_pools(self):
        return self.conn.execute("SELECT * FROM pools").fetchall()

    # ---- cabal finder ----
    @staticmethod
    def _day(ts):
        import datetime as _dt
        return _dt.datetime.fromtimestamp(ts, _dt.timezone.utc).strftime("%Y-%m-%d")

    def credits_used(self, now):
        r = self.conn.execute("SELECT credits FROM helius_usage WHERE day=?", (self._day(now),)).fetchone()
        return r[0] if r else 0

    def add_credits(self, now, n):
        self.conn.execute(
            "INSERT INTO helius_usage VALUES (?,?) ON CONFLICT(day) DO UPDATE SET credits=credits+excluded.credits",
            (self._day(now), int(n)))

    def get_cluster(self, mint, now=None, max_age_hours=None):
        r = self.conn.execute(
            "SELECT * FROM clusters WHERE token_mint=? ORDER BY ts DESC LIMIT 1", (mint,)).fetchone()
        if r is None:
            return None
        if now is not None and max_age_hours is not None and now - r["ts"] > max_age_hours * 3600:
            return None
        return r

    def save_cluster(self, mint, ts, metrics, kills, research):
        self.conn.execute("INSERT INTO clusters VALUES (?,?,?,?,?)",
                          (mint, ts, int(bool(research)), json.dumps(kills), json.dumps(metrics)))

    def was_alerted(self, addr):
        return self.conn.execute("SELECT 1 FROM alerts WHERE pool_address=?", (addr,)).fetchone() is not None

    def mark_alerted(self, addr, ts):
        self.conn.execute("INSERT OR IGNORE INTO alerts VALUES (?,?)", (addr, ts))
