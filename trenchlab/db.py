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

    def add_observation(self, ts, pool, scout_pass, kills, flags, score, parts, final_pass):
        self.conn.execute(
            "INSERT INTO observations VALUES (?,?,?,?,?,?,?,?,?,?)",
            (ts, pool.address, pool.source, int(scout_pass), json.dumps(kills), json.dumps(flags),
             score, json.dumps(parts), int(final_pass), json.dumps(pool.to_dict())),
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

    def sample_due(self, addr, now, dense_hours=3.0, sparse_minutes=30):
        """Dense sampling (every cycle) for `dense_hours` after first sighting or first pass,
        then one sample per `sparse_minutes`. Keeps the database small enough for 24/7 runs."""
        p = self.get_pool(addr)
        if p is None:
            return True
        ref = max(p["first_seen_ts"] or 0, p["first_pass_ts"] or 0)
        if now - ref <= dense_hours * 3600:
            return True
        last = self.conn.execute("SELECT MAX(ts) FROM samples WHERE pool_address=?", (addr,)).fetchone()[0]
        return last is None or now - last >= sparse_minutes * 60 - 30

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
