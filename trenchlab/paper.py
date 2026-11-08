"""PAPER TRADER (v0.3): turns FINAL PASS signals into simulated trades with realistic costs.

Never signs anything, never touches a wallet. It answers one question: if we had followed
the rules, with real position sizing and real trading costs, what would the account look like?

Pricing (two modes):
  - "jupiter": real Jupiter swap quotes (needs a free JUPITER_API_KEY from portal.jup.ag).
               Buy = quote SOL->token; mark/sell = quote token->SOL for the exact amount held.
  - "model":   no key needed. Constant-product price impact from the pool's own liquidity:
               impact ~= trade_usd / (liquidity_usd / 2), plus pool fee and network fee.

Rules (config "paper"):
  size = min(risk_per_trade / |stop|, max_position) * equity     (confidence never changes size)
  max open positions, max total exposure, one entry per token (no averaging),
  cooldown after a loss, daily loss limit -> no new entries that UTC day.
  Exits are checked every scan on the NET value you would get by selling now:
  hard stop, trailing stop after activation, time stop, and dead-pool handling.
  The stop never moves down.

Ledger: every entry/exit is a row; cash + cost of open positions == start + realized P&L
(checked in the report).
"""
import json
import math
import os
import time
import urllib.parse

from .http import get_json, HttpError

SOL_MINT = "So11111111111111111111111111111111111111112"
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
JUP_QUOTE = "https://api.jup.ag/swap/v1/quote?"


# ---------------------------------------------------------------- pricing
class ModelQuoter:
    mode = "model"

    def __init__(self, cfg):
        self.fee = cfg["paper"]["model_pool_fee_pct"] / 100
        self.net_fee_usd = cfg["paper"]["network_fee_usd"]

    def _impact(self, usd, liq):
        if not liq or liq <= 0:
            return None
        return usd / (liq / 2.0)

    def buy(self, pool_state, usd):
        """Return (tokens_received, info) for spending `usd`. tokens are in UI units."""
        price, liq = pool_state["price"], pool_state["liq"]
        imp = self._impact(usd, liq)
        if not price or imp is None:
            return None, {"error": "no price/liquidity"}
        spend = usd - self.net_fee_usd
        eff_price = price * (1 + imp) / (1 - self.fee)
        return spend / eff_price, {"impact_pct": round(imp * 100, 3), "eff_price": eff_price}

    def sell_value(self, pool_state, tokens):
        """USD you would receive now for `tokens`."""
        price, liq = pool_state["price"], pool_state["liq"]
        if not price or not liq:
            return None, {"error": "no price/liquidity"}
        gross = tokens * price
        imp = self._impact(gross, liq)
        out = gross / (1 + imp) * (1 - self.fee) - self.net_fee_usd
        return max(out, 0.0), {"impact_pct": round(imp * 100, 3)}


class JupiterQuoter:
    mode = "jupiter"

    def __init__(self, cfg, api_key, fetch=get_json):
        self.key = api_key
        self.fetch = fetch
        self.slip = cfg["paper"]["jupiter_slippage_bps"]
        self.net_fee_usd = cfg["paper"]["network_fee_usd"]
        self._sol_usd = None

    def _quote(self, inp, out, amount):
        qs = urllib.parse.urlencode({"inputMint": inp, "outputMint": out, "amount": int(amount),
                                     "slippageBps": self.slip, "restrictIntermediateTokens": "true"})
        return self.fetch(JUP_QUOTE + qs, min_interval=1.1, headers={"x-api-key": self.key})

    def sol_usd(self):
        if self._sol_usd is None:
            q = self._quote(SOL_MINT, USDC_MINT, 10**9)
            self._sol_usd = int(q["outAmount"]) / 1e6
        return self._sol_usd

    def buy(self, pool_state, usd, mint):
        lamports = (usd - self.net_fee_usd) / self.sol_usd() * 1e9
        try:
            q = self._quote(SOL_MINT, mint, lamports)
        except HttpError as e:
            return None, {"error": str(e)[:100]}
        if not q or "outAmount" not in q:
            return None, {"error": (q or {}).get("error", "no route")}
        # worst case fill within slippage = otherAmountThreshold (conservative)
        raw = int(q.get("otherAmountThreshold") or q["outAmount"])
        return raw, {"impact_pct": round(float(q.get("priceImpactPct") or 0) * 100, 3), "raw": True}

    def sell_value(self, pool_state, raw_tokens, mint):
        try:
            q = self._quote(mint, SOL_MINT, raw_tokens)
        except HttpError as e:
            return None, {"error": str(e)[:100]}
        if not q or "outAmount" not in q:
            return None, {"error": (q or {}).get("error", "no route")}
        lam = int(q.get("otherAmountThreshold") or q["outAmount"])
        return max(lam / 1e9 * self.sol_usd() - self.net_fee_usd, 0.0), {
            "impact_pct": round(float(q.get("priceImpactPct") or 0) * 100, 3)}


def make_quoter(cfg, api_key=None, fetch=get_json):
    key = api_key if api_key is not None else os.environ.get("JUPITER_API_KEY", "")
    return JupiterQuoter(cfg, key, fetch) if key else ModelQuoter(cfg)


# ---------------------------------------------------------------- trader
class PaperTrader:
    def __init__(self, cfg, db, quoter=None, log=print, notify=None, book="A"):
        self.cfg = cfg
        self.c = cfg["paper"]
        self.db = db
        self.book = book
        self.q = quoter or make_quoter(cfg)
        self.log = log
        self.notify = notify or (lambda msg: None)
        db.ensure_paper_bank(self.c["start_usd"], book=book)

    # -- helpers
    def _state(self, pool_address, now):
        """Latest reliable price/liquidity for a pool from this scan cycle (or the last 15 min)."""
        r = self.db.latest_sample(pool_address, since=now - 900)
        if not r:
            return None
        return {"price": r["price_usd"], "liq": r["liquidity_usd"], "ts": r["ts"]}

    def _value(self, pos, state):
        if self.q.mode == "jupiter":
            return self.q.sell_value(state, int(pos["tokens"]), pos["token_mint"])
        return self.q.sell_value(state, pos["tokens"])

    def equity(self, now, marks=None):
        cash = self.db.paper_cash(self.book)
        open_val = 0.0
        for p in self.db.open_positions(self.book):
            v = (marks or {}).get(p["id"])
            open_val += v if v is not None else (p["last_value"] if p["last_value"] is not None else p["cost_usd"])
        return cash + open_val

    # -- entries
    def on_signal(self, pool, score, now, extra=None):
        c = self.c
        if self.db.paper_traded_token(pool.token_mint, self.book):
            return self._skip(pool, now, "already_traded_token")
        opens = self.db.open_positions(self.book)
        if len(opens) >= c["max_open_positions"]:
            return self._skip(pool, now, "max_open_positions")
        eq = self.equity(now)
        if self.db.paper_realized_today(now, self.book) <= -c["daily_loss_limit_pct"] / 100 * c["start_usd"]:
            return self._skip(pool, now, "daily_loss_limit")
        last_loss = self.db.paper_last_loss_ts(self.book)
        if last_loss and now - last_loss < c["cooldown_after_loss_min"] * 60:
            return self._skip(pool, now, "cooldown_after_loss")
        frac = min(c["risk_per_trade_pct"] / abs(c["stop_pct"]), c["max_position_pct"] / 100)
        size = round(eq * frac, 2)
        exposure = sum(p["cost_usd"] for p in opens)
        if exposure + size > eq * c["max_exposure_pct"] / 100:
            return self._skip(pool, now, "max_exposure")
        if size > self.db.paper_cash(self.book):
            return self._skip(pool, now, "insufficient_cash")
        if size < c["min_trade_usd"]:
            return self._skip(pool, now, "below_min_trade")
        state = {"price": pool.price_usd, "liq": pool.liquidity_usd}
        if self.q.mode == "jupiter":
            tokens, info = self.q.buy(state, size, pool.token_mint)
        else:
            tokens, info = self.q.buy(state, size)
        if not tokens:
            return self._skip(pool, now, "no_quote:" + str(info.get("error", "?"))[:40])
        if info.get("impact_pct", 0) > c["max_entry_impact_pct"]:
            return self._skip(pool, now, f"impact_too_high({info['impact_pct']:.1f}%)")
        if extra:
            info = {**info, **extra}
        pid = self.db.paper_open(now, pool, size, tokens, score, self.q.mode, info, book=self.book)
        self.log(f"[paper {self.book}] BUY {pool.symbol} ${size:.2f} (impact {info.get('impact_pct')}%, {self.q.mode})")
        self.notify(f"PAPER {self.book} BUY ${pool.symbol}  ${size:.2f}  score {score}\nimpact {info.get('impact_pct')}% "
                    f"({self.q.mode})\n{pool.gecko_url()}\nPaper only. NFA.")
        return pid

    def _skip(self, pool, now, reason):
        self.db.paper_skip(now, pool, reason, self.book)
        self.log(f"[paper {self.book}] skip {pool.symbol}: {reason}")
        return None

    # -- exits
    def manage(self, now):
        c = self.c
        marks = {}
        for pos in self.db.open_positions(self.book):
            if pos["entry_ts"] >= now:
                # entered this cycle: the stored sample may come from a different price source than the
                # entry quote (book B enters on fresh GeckoTerminal data), so start checking next cycle
                continue
            state = self._state(pos["pool_address"], now)
            value, info = (None, {"error": "no fresh price"})
            if state:
                value, info = self._value(pos, state)
            if value is None:
                misses = self.db.paper_miss(pos["id"])
                if misses >= c["dead_after_missed_cycles"]:
                    # can't price or route for a long time: assume the exit is worthless (conservative)
                    self._close(pos, now, 0.0, "dead_no_route")
                continue
            self.db.paper_reset_miss(pos["id"])
            marks[pos["id"]] = value
            ret = value / pos["cost_usd"] - 1
            peak = max(pos["peak_value"] or pos["cost_usd"], value)
            self.db.paper_mark(pos["id"], value, peak)
            peak_ret = peak / pos["cost_usd"] - 1
            if ret <= c["stop_pct"] / 100:
                self._close(pos, now, value, "stop")
            elif peak_ret >= c["trail_activate_pct"] / 100 and value <= peak * (1 - c["trail_distance_pct"] / 100):
                self._close(pos, now, value, "trail")
            elif now - pos["entry_ts"] >= c["max_hold_hours"] * 3600:
                self._close(pos, now, value, "time")
        self.db.paper_snapshot(now, self.equity(now, marks), self.db.paper_cash(self.book),
                               len(self.db.open_positions(self.book)), self.book)
        self.db.commit()

    def _close(self, pos, now, value, reason):
        self.db.paper_close(pos["id"], now, value, reason)
        pnl = value - pos["cost_usd"]
        self.log(f"[paper {self.book}] SELL {pos['symbol']} {reason} ${value:.2f} ({pnl:+.2f})")
        self.notify(f"PAPER {self.book} SELL ${pos['symbol']} ({reason})\nP&L {pnl:+.2f} USD "
                    f"({value / pos['cost_usd'] - 1:+.1%})\nPaper only. NFA.")


# ---------------------------------------------------------------- report
BOOK_LABELS = {"A": "A: momentum (thread filters)", "B": "B: pullback (safety-first, buy the dip)"}


def book_stats(db, book):
    bank = db.paper_bank(book)
    if not bank:
        return None
    cash = db.paper_cash(book)
    opens = db.open_positions(book)
    closed = db.closed_positions(book)
    realized = sum(p["exit_value"] - p["cost_usd"] for p in closed)
    open_cost = sum(p["cost_usd"] for p in opens)
    open_mark = sum((p["last_value"] if p["last_value"] is not None else p["cost_usd"]) for p in opens)
    peak, mdd = -math.inf, 0.0
    for s_ in db.paper_snapshots(book):
        peak = max(peak, s_["equity"])
        if peak > 0:
            mdd = min(mdd, s_["equity"] / peak - 1)
    rets = [p["exit_value"] / p["cost_usd"] - 1 for p in closed]
    return {
        "bank": bank, "cash": cash, "opens": opens, "closed": closed, "realized": realized,
        "equity": cash + open_mark, "mdd": mdd, "rets": rets,
        "reconciles": abs((cash + open_cost) - (bank["start_usd"] + realized)) < 0.01,
        "mode": opens[0]["mode"] if opens else (closed[-1]["mode"] if closed else "-"),
    }


def paper_report(db, cfg, book="A"):
    st = book_stats(db, book)
    if not st:
        return ""
    lines = []
    w = lines.append
    bank, closed, opens = st["bank"], st["closed"], st["opens"]
    started = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(bank["created_ts"]))
    w("")
    w("=" * 64)
    w(f"PAPER BOOK {BOOK_LABELS.get(book, book)}")
    w(f"  pricing: {st['mode']} | start ${bank['start_usd']:.2f} on {started}")
    w("=" * 64)
    w(f"equity ${st['equity']:.2f} ({st['equity'] / bank['start_usd'] - 1:+.1%}) | cash ${st['cash']:.2f} | "
      f"open {len(opens)} | max drawdown {st['mdd']:.1%}")
    w(f"ledger reconciles: {'YES' if st['reconciles'] else 'NO - investigate'} "
      f"(cash + open cost = start + realized P&L)")
    if closed:
        rets = st["rets"]
        wins = sum(1 for r in rets if r > 0)
        w(f"closed {len(closed)} | win {wins}/{len(closed)} ({wins / len(closed):.0%}) | "
          f"avg net {sum(rets) / len(rets):+.1%} | realized ${st['realized']:+.2f} | "
          f"expectancy ${st['realized'] / len(closed):+.2f}/trade")
        reasons = {}
        for p in closed:
            reasons[p["exit_reason"]] = reasons.get(p["exit_reason"], 0) + 1
        w("exits: " + ", ".join(f"{k} {v}" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1])))
        if len(closed) < 100:
            w(f"  (n={len(closed)} < 100: noise, not evidence)")
    if opens:
        w("open:")
        for p in opens:
            mk = p["last_value"] if p["last_value"] is not None else p["cost_usd"]
            w(f"  {p['symbol'][:12]:<13}cost ${p['cost_usd']:.2f}  now ${mk:.2f} ({mk / p['cost_usd'] - 1:+.1%})"
              f"  held {(time.time() - p['entry_ts']) / 3600:.1f}h")
    if closed:
        w("last trades:")
        for p in closed[-8:]:
            w(f"  {p['symbol'][:12]:<13}${p['cost_usd']:.2f} -> ${p['exit_value']:.2f} "
              f"({p['exit_value'] / p['cost_usd'] - 1:+.1%})  {p['exit_reason']}  "
              f"{(p['exit_ts'] - p['entry_ts']) / 3600:.1f}h")
    skips = db.paper_skip_counts(book)
    if skips:
        w("signals skipped by the sizer/risk rules: " + ", ".join(f"{k} {v}" for k, v in skips))
    return "\n".join(lines)


def comparison_report(db):
    """Side-by-side A vs B. Same sizing, same exits, same costs: only the ENTRY rule differs."""
    books = db.paper_books()
    if len(books) < 2:
        return ""
    stats = {b: book_stats(db, b) for b in books}
    lines = ["", "=" * 64, "A vs B (same sizing, exits and costs; only the entry rule differs)", "=" * 64]
    hdr = f"{'':<22}" + "".join(f"{b:>14}" for b in books)
    lines.append(hdr)

    def row(label, fn):
        lines.append(f"{label:<22}" + "".join(f"{fn(stats[b]):>14}" for b in books))

    row("started", lambda s: time.strftime("%m-%d %H:%M", time.gmtime(s["bank"]["created_ts"])))
    row("equity", lambda s: f"${s['equity']:.2f}")
    row("return", lambda s: f"{s['equity'] / s['bank']['start_usd'] - 1:+.1%}")
    row("closed trades", lambda s: str(len(s["closed"])))
    row("win rate", lambda s: f"{sum(1 for r in s['rets'] if r > 0) / len(s['rets']):.0%}" if s["rets"] else "-")
    row("avg net / trade", lambda s: f"{sum(s['rets']) / len(s['rets']):+.1%}" if s["rets"] else "-")
    row("expectancy $/trade", lambda s: f"${s['realized'] / len(s['closed']):+.2f}" if s["closed"] else "-")
    row("max drawdown", lambda s: f"{s['mdd']:.1%}")
    row("open now", lambda s: str(len(s["opens"])))
    lines.append("Judge on expectancy after >=100 trades each, not on win rate or a few days.")
    return "\n".join(lines)
