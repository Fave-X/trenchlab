"""ALIVE CHECK: which CoreSight winners are still alive and thriving right now?

CoreSight's own tip: take tokens from the 7d / 1m leaderboard that are "still alive and thriving",
research them, and buy for "another leg up". This module does the research part, the same way
for every token on the list:

  market (GeckoTerminal, the token's deepest pool):
    market cap now vs CoreSight's call market cap and vs the peak (call mcap x ATH multiple),
    liquidity, 24h volume, 1h/24h price change, 1h buyers vs sellers, pool age
  safety (same as the scanner): RugCheck/GoPlus audit + cabal finder (bundled / fresh / linked)

Status (rules written down before looking at the results):
  dead     liquidity < $5k, or 24h volume < $2k, or mcap below 30% of the call
  fading   down > 70% from peak, or 24h change < -40%, or more sellers than buyers in the last hour
  thriving mcap >= 1.5x the call, within 50% of the peak, 24h volume >= 50% of liquidity,
           >= 100 buyers in the last hour, buyers >= sellers
  alive    everything else
A safety problem (audit kill, bundled buys > 20%, fresh wallets > 40%) is shown as a warning.

Whether "alive and thriving" tokens really give "another leg up" is a separate, untested claim;
this report is a snapshot, not a signal.
"""
import json
import time

from .gecko import BASE, parse_pool_list


def classify(m, call_mcap, ath_x):
    mcap = m.get("mcap")
    liq, vol = m.get("liq") or 0, m.get("vol24") or 0
    peak = call_mcap * ath_x if call_mcap and ath_x else None
    if mcap is None:
        return "dead", "no market data"
    if liq < 5000 or vol < 2000 or (call_mcap and mcap < 0.3 * call_mcap):
        return "dead", "no liquidity/volume or far below the call"
    from_peak = mcap / peak - 1 if peak else None
    buyers, sellers = m.get("buyers1h") or 0, m.get("sellers1h") or 0
    if (from_peak is not None and from_peak < -0.7) or (m.get("chg24") or 0) < -40 or sellers > buyers:
        return "fading", "far off the peak, dumping, or sellers dominate"
    if (call_mcap and mcap >= 1.5 * call_mcap and from_peak is not None and from_peak >= -0.5
            and vol >= 0.5 * liq and buyers >= 100 and buyers >= sellers):
        return "thriving", "above the call, near the peak, active buyers"
    return "alive", "trading, but not strong on every measure"


def run(winners, gecko, auditor=None, cabal=None, now=None, log=print):
    now = now or time.time()
    rows = []
    for t in winners:
        mint = t["address"]
        m = {}
        try:
            data = gecko.raw(f"/networks/solana/tokens/{mint}/pools?page=1&include=base_token")
            pools = [p for p in parse_pool_list(data, "solana", "alive") if p.token_mint == mint]
            pools.sort(key=lambda p: -(p.liquidity_usd or 0))
            if pools:
                p = pools[0]
                m = {"pool": p.address, "dex": p.dex, "mcap": p.market_cap_usd or p.fdv_usd,
                     "liq": p.liquidity_usd, "vol24": p.vol_h24, "chg1h": p.chg_h1, "chg24": None,
                     "buyers1h": p.buyers_h1, "sellers1h": p.sellers_h1,
                     "age_d": round(p.age_hours(now) / 24, 1) if p.age_hours(now) is not None else None}
                raw = next((it for it in (data or {}).get("data", []) if (it.get("attributes") or {}).get("address") == p.address), {})
                m["chg24"] = float(((raw.get("attributes") or {}).get("price_change_percentage") or {}).get("h24") or 0)
        except Exception as e:
            log(f"[alive] {t['symbol']} market data failed: {e}")
        status, why = classify(m, t.get("called_mcap"), t.get("ath_x"))
        warn = []
        if status != "dead":
            if auditor is not None:
                ok, kills, _ = auditor.audit(mint)
                if not ok:
                    warn.append("audit:" + kills[0].split("(")[0])
            if cabal is not None and cabal.enabled:
                res = cabal.check(mint, now, auditor.known_accounts.get(mint) if auditor else None)
                if res and res[1]:
                    cm = res[1]
                    if cm.get("same_slot_pct", 0) > 20:
                        warn.append(f"bundled {cm['same_slot_pct']:.0f}%")
                    if cm.get("fresh_pct", 0) > 40:
                        warn.append(f"fresh {cm['fresh_pct']:.0f}%")
                    if cm.get("largest_cluster_pct", 0) > 15:
                        warn.append(f"linked group {cm['largest_cluster_pct']:.0f}%")
        call = t.get("called_mcap")
        peak = call * t["ath_x"] if call and t.get("ath_x") else None
        rows.append({**t, **m, "status": status, "why": why, "warnings": ", ".join(warn),
                     "x_vs_call": round(m["mcap"] / call, 2) if m.get("mcap") and call else None,
                     "from_peak_pct": round((m["mcap"] / peak - 1) * 100) if m.get("mcap") and peak else None})
        log(f"[alive] {t['symbol']}: {status}")
    order = {"thriving": 0, "alive": 1, "fading": 2, "dead": 3}
    rows.sort(key=lambda r: (order[r["status"]], -(r.get("x_vs_call") or 0)))
    return rows


def _usd(x):
    if x is None:
        return "-"
    return f"${x / 1e6:.2f}M" if x >= 1e6 else f"${x / 1e3:.0f}k"


def markdown(rows, captured_at):
    counts = {s: sum(r["status"] == s for r in rows) for s in ("thriving", "alive", "fading", "dead")}
    L = ["# Alive check: CoreSight winners today", "",
         f"Checked: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}  |  leaderboard captured: {captured_at}", "",
         f"**{counts['thriving']} thriving, {counts['alive']} alive, {counts['fading']} fading, {counts['dead']} dead** "
         f"out of {len(rows)} tokens.", "",
         "x vs call = market cap now / CoreSight's call market cap. From peak = now vs the call x ATH multiple.",
         "Status rules are in `trenchlab/alive.py`. A snapshot, not a buy signal.", "",
         "| status | token | mcap now | x vs call | from peak | liquidity | 24h vol | 24h | 1h buyers/sellers | age (d) | warnings | chart |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        chg24 = f"{r['chg24']:+.0f}%" if r.get("chg24") is not None else "-"
        chart = f"[chart](https://www.geckoterminal.com/solana/pools/{r['pool']})" if r.get("pool") else "-"
        L.append(f"| **{r['status']}** | {r['symbol']} | {_usd(r.get('mcap'))} | "
                 f"{(str(r['x_vs_call']) + 'x') if r.get('x_vs_call') else '-'} | "
                 f"{(str(r['from_peak_pct']) + '%') if r.get('from_peak_pct') is not None else '-'} | "
                 f"{_usd(r.get('liq'))} | {_usd(r.get('vol24'))} | "
                 f"{chg24} | "
                 f"{r.get('buyers1h', '-')}/{r.get('sellers1h', '-')} | {r.get('age_d', '-')} | {r['warnings'] or '-'} | {chart} |")
    L += ["", "Token addresses: `research/coresight_winners.json`. Full data: `research/alive.json`."]
    return "\n".join(L) + "\n"
