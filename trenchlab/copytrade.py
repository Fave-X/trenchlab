"""BOOK C: paper copy-trading of watched wallets (thesis C, started 2026-11-24).

Thesis: some wallets that were early AND profitable on CoreSight's winners - and are not bots,
snipers or overall losers - have a repeatable edge that survives a realistic copy delay.

How it works (every scan cycle, read-only, never signs anything):
  1. Watched wallets come from research/watch_wallets.txt (one address per line, optional
     "  # label"). Editing that file is how wallets are added or removed.
  2. For each wallet: new transactions since the last check (Helius getSignaturesForAddress
     with `until`). On the very first check a wallet is only bookmarked: we never copy the past.
  3. Each new transaction is parsed for token buys/sells by that wallet (SOL/stablecoins ignored).
  4. BUY  -> book C buys the same token at the market price `delay_s` seconds AFTER the wallet's
            transaction, from GeckoTerminal 1-minute candles (conservative: between high and close),
            plus the same impact/fee model as books A and B.
     SELL -> if book C holds that token from this wallet, it sells at the price `delay_s` seconds
            after the wallet's sell (between low and close). This is the "mirror exit".
  5. Safety exits (wide stop, time stop) and dead-pool handling come from the paper trader.
Per-wallet results are reported so wallets that don't copy well can be dropped.
"""
import os
import time

from .cluster import Rpc, RpcError, RPC_URL, TX_VERSION
from .gecko import BASE as GECKO_BASE, parse_pool_list
from .http import get_json

IGNORE_MINTS = {
    "So11111111111111111111111111111111111111112",   # wSOL
    "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
    "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",  # USDT
}


def load_watchlist(path):
    wallets = {}
    if not os.path.exists(path):
        return wallets
    with open(path) as f:
        for line in f:
            addr, _, label = line.partition("#")
            addr = addr.strip()
            if 32 <= len(addr) <= 44:
                wallets[addr] = label.strip()
    return wallets


def _key(k):
    return k.get("pubkey") if isinstance(k, dict) else k


def wallet_trades(tx, wallet):
    """All token buys/sells by `wallet` in one transaction: [(mint, side, tokens, sol_delta)]."""
    if not tx or (tx.get("meta") or {}).get("err") is not None:
        return []
    meta = tx.get("meta") or {}
    keys = [_key(k) for k in ((tx.get("transaction") or {}).get("message") or {}).get("accountKeys") or []]
    if wallet not in keys:
        return []
    i = keys.index(wallet)
    pb, qb = meta.get("preBalances") or [], meta.get("postBalances") or []
    sol = (qb[i] - pb[i]) / 1e9 if i < len(pb) and i < len(qb) else 0.0

    def bal(rows):
        out = {}
        for b in rows or []:
            if b.get("owner") != wallet or b.get("mint") in IGNORE_MINTS:
                continue
            out[b["mint"]] = out.get(b["mint"], 0.0) + float(((b.get("uiTokenAmount") or {}).get("uiAmount")) or 0)
        return out

    pre, post = bal(meta.get("preTokenBalances")), bal(meta.get("postTokenBalances"))
    trades = []
    for mint in set(pre) | set(post):
        d = post.get(mint, 0.0) - pre.get(mint, 0.0)
        if d > 0 and sol < 0:
            trades.append((mint, "buy", d, sol))
        elif d < 0 and sol > 0:
            trades.append((mint, "sell", -d, sol))
    return trades


class CandlePricer:
    """Price of a token at a past moment, from GeckoTerminal 1-minute candles of its top pool."""

    def __init__(self, network="solana", fetch=get_json, min_interval=2.5):
        self.net = network
        self.fetch = fetch
        self.mi = min_interval
        self._pool = {}

    def top_pool(self, mint):
        if mint not in self._pool:
            data = self.fetch(f"{GECKO_BASE}/networks/{self.net}/tokens/{mint}/pools?page=1&include=base_token",
                              min_interval=self.mi)
            pools = [p for p in parse_pool_list(data, self.net, "copy") if p.token_mint == mint]
            pools.sort(key=lambda p: -(p.liquidity_usd or 0))
            self._pool[mint] = pools[0] if pools else None
        return self._pool[mint]

    def price_at(self, pool_address, ts, side):
        """Conservative fill price for a trade at unix time `ts`: buys between high and close,
        sells between low and close, of the 1-minute candle containing ts (else the previous one)."""
        data = self.fetch(f"{GECKO_BASE}/networks/{self.net}/pools/{pool_address}/ohlcv/minute"
                          f"?aggregate=1&before_timestamp={int(ts) + 60}&limit=5&currency=usd&token=base",
                          min_interval=self.mi)
        rows = ((((data or {}).get("data") or {}).get("attributes") or {}).get("ohlcv_list")) or []
        rows = sorted((r for r in rows if r and r[0] <= ts), key=lambda r: -r[0])
        if not rows:
            return None
        t, o, h, l, c = rows[0][:5]
        if ts - t > 600:          # no trade within 10 minutes before: too stale to price
            return None
        return (h + c) / 2 if side == "buy" else (l + c) / 2


def run(db, trader, cfg, now, rpc=None, pricer=None, log=print, watch_path="research/watch_wallets.txt"):
    """One copy-trading cycle. Returns (entries, exits)."""
    c = cfg["copytrade"]
    watch = load_watchlist(watch_path)
    if not watch:
        return 0, 0
    if rpc is None:
        key = os.environ.get("HELIUS_API_KEY", "")
        if not key:
            log("[C] HELIUS_API_KEY not set - copy-trading off")
            return 0, 0
        rpc = Rpc(RPC_URL.format(key=key), min_interval=0.13)
    pricer = pricer or CandlePricer(cfg["network"])
    entries = exits = 0
    for wallet, label in watch.items():
        state = db.copy_wallet(wallet)
        if state is None:
            # first sight: bookmark the newest transaction, never copy history
            try:
                newest = rpc.call("getSignaturesForAddress", [wallet, {"limit": 1}]) or []
            except RpcError as e:
                log(f"[C] {wallet[:6]} bookmark failed: {e}")
                continue
            db.copy_wallet_set(wallet, label, newest[0]["signature"] if newest else None, now)
            continue
        opts = {"limit": c["max_new_txs_per_wallet"]}
        if state["last_sig"]:
            opts["until"] = state["last_sig"]
        try:
            sigs = rpc.call("getSignaturesForAddress", [wallet, opts]) or []
        except RpcError as e:
            log(f"[C] {wallet[:6]} check failed: {e}")
            continue
        db.copy_wallet_set(wallet, label, sigs[0]["signature"] if sigs else None, now)
        if not sigs:
            continue
        for s in reversed(sigs):                       # oldest first
            if s.get("err") is not None or not s.get("blockTime"):
                continue
            if now - s["blockTime"] > c["max_signal_age_min"] * 60:
                continue                               # too old to copy honestly
            try:
                tx = rpc.call("getTransaction", [s["signature"], {"encoding": "jsonParsed",
                                                                  "maxSupportedTransactionVersion": TX_VERSION}])
            except RpcError:
                continue
            for mint, side, tokens, sol in wallet_trades(tx, wallet):
                db.copy_event(now, wallet, s["signature"], mint, side, tokens, sol, s["blockTime"])
                if side == "buy" and -sol >= c["min_wallet_buy_sol"]:
                    entries += _copy_buy(db, trader, pricer, cfg, wallet, label, mint, s, sol, now, log)
                elif side == "sell":
                    exits += _copy_sell(db, trader, pricer, cfg, wallet, mint, s, now, log)
    db.commit()
    return entries, exits


def _copy_buy(db, trader, pricer, cfg, wallet, label, mint, sig, sol, now, log):
    c = cfg["copytrade"]
    try:
        pool = pricer.top_pool(mint)
        if pool is None:
            db.paper_skip(now, _Stub(mint), "copy:no_pool", "C")
            return 0
        if (pool.liquidity_usd or 0) < c["min_liquidity_usd"]:   # cheap check first: no candle call
            db.paper_skip(now, pool, "copy:liquidity_too_low", "C")
            return 0
        if db.paper_traded_token(mint, "C"):
            return 0
        px = pricer.price_at(pool.address, sig["blockTime"] + c["delay_s"], "buy")
    except Exception as e:
        log(f"[C] pricing {mint[:6]} failed: {e}")
        return 0
    if not px:
        db.paper_skip(now, pool, "copy:no_price_at_delay", "C")
        return 0
    pool.price_usd = px
    db.upsert_first_seen(pool, now, ["copy_trade"], now + 72 * 3600)
    db.add_sample(pool.address, now, pool.price_usd, pool.liquidity_usd)
    info = {"copied_wallet": wallet, "wallet_label": label, "wallet_sig": sig["signature"],
            "wallet_sol": round(-sol, 4), "lag_s": int(now - sig["blockTime"]), "delay_s": c["delay_s"]}
    return 1 if trader.on_signal(pool, None, now, extra=info) else 0


def _copy_sell(db, trader, pricer, cfg, wallet, mint, sig, now, log):
    c = cfg["copytrade"]
    import json as _json
    for pos in db.open_positions("C"):
        if pos["token_mint"] != mint:
            continue
        info = _json.loads(pos["entry_info"] or "{}")
        if info.get("copied_wallet") != wallet:
            continue
        try:
            px = pricer.price_at(pos["pool_address"], sig["blockTime"] + c["delay_s"], "sell")
        except Exception as e:
            log(f"[C] exit pricing failed: {e}")
            px = None
        if not px:
            return 0                                     # safety exits will handle it later
        latest = db.latest_sample(pos["pool_address"], since=0)
        liq = latest["liquidity_usd"] if latest else None
        if trader.close_at(pos, now, {"price": px, "liq": liq}, "mirror_sell") is not None:
            return 1
    return 0


class _Stub:
    def __init__(self, mint):
        self.address = mint
        self.symbol = mint[:6]


def wallet_report(db):
    """Per-wallet results of book C."""
    import json as _json
    rows = {}
    for p in db.conn.execute("SELECT * FROM paper_positions WHERE book='C'"):
        info = _json.loads(p["entry_info"] or "{}")
        w = info.get("copied_wallet", "?")
        r = rows.setdefault(w, {"label": info.get("wallet_label", ""), "open": 0, "closed": 0, "pnl": 0.0, "wins": 0,
                                "rets": []})
        if p["exit_ts"] is None:
            r["open"] += 1
        else:
            r["closed"] += 1
            r["pnl"] += p["exit_value"] - p["cost_usd"]
            ret = p["exit_value"] / p["cost_usd"] - 1
            r["rets"].append(ret)
            r["wins"] += ret > 0
    watched = db.conn.execute("SELECT COUNT(*) FROM copy_wallets WHERE last_check_ts >= "
                              "(SELECT MAX(last_check_ts) FROM copy_wallets) - 3600").fetchone()[0]
    events = db.conn.execute("SELECT COUNT(*) FROM copy_events").fetchone()[0]
    lines = ["", f"BOOK C per wallet  (watching {watched} wallets, {events} wallet trades seen)"]
    if not rows:
        lines.append("  no copied trades yet")
        return "\n".join(lines)
    lines.append(f"{'wallet':<14}{'label':<14}{'closed':>7}{'open':>6}{'win%':>6}{'avg net':>9}{'P&L $':>9}")
    for w, r in sorted(rows.items(), key=lambda kv: -kv[1]["pnl"]):
        avg = sum(r["rets"]) / len(r["rets"]) if r["rets"] else None
        win = f"{r['wins'] / r['closed']:.0%}" if r["closed"] else "-"
        lines.append(f"{w[:6] + '…' + w[-4:]:<14}{r['label'][:13]:<14}{r['closed']:>7}{r['open']:>6}{win:>6}"
                     f"{(f'{avg:+.1%}' if avg is not None else '-'):>9}{r['pnl']:>+9.2f}")
    lines.append("Drop wallets with negative expectancy after ~20 copied trades each.")
    return "\n".join(lines)
