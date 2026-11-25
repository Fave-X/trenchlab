"""WALLET FINDER: who bought CoreSight's winning tokens early - and are they copyable humans or bots?

Stage 1 - early buyers (per token, Helius free RPC, 1 credit per call):
  page getSignaturesForAddress(mint) back to the token's first transaction, then read the first
  `early_txs` successful transactions. A trade's trader = the fee payer; buy = payer's token
  balance went up, sell = it went down; SOL in/out from the payer's lamport change.

Control group (the important part): the same is done for tokens that DIED (from TrenchLab's own
database). Sniper bots buy every launch, so they show up early on winners AND losers. A wallet that
is early on dead tokens too is not "smart", just indiscriminate.

Stage 2 - candidates (early on >= min_winners winners) get checked:
  - activity: transactions per day (hundreds/day = bot)
  - behaviour on the winners: launch-block sniping, same-transaction bundles, average hold time
  - realized SOL P&L on each winner from the wallet's own trades in that token
Output: research/watchlist.csv + WALLETS.md, ranked, with every flag shown.

Hindsight warning: wallets are picked BECAUSE they were early on tokens we already know won.
That proves nothing about their next trade. The only honest test is to track their NEXT trades
forward (paper copy-trading with a delay), which is the step after this one.
"""
import csv
import json
import os
import time
from collections import defaultdict

from .cluster import Rpc, RpcError, RPC_URL, TX_VERSION

SOL_DECIMALS = 1e9


def _key(k):
    return k.get("pubkey") if isinstance(k, dict) else k


def parse_trade(tx, mint):
    """Return dict(trader, side, tokens, sol, token_account, slot, ts) for one transaction, or None."""
    if not tx or (tx.get("meta") or {}).get("err") is not None:
        return None
    meta = tx.get("meta") or {}
    keys = [_key(k) for k in ((tx.get("transaction") or {}).get("message") or {}).get("accountKeys") or []]
    if not keys:
        return None
    payer = keys[0]

    def bal(rows):
        out, accts = {}, {}
        for b in rows or []:
            if b.get("mint") != mint:
                continue
            o = b.get("owner")
            amt = float(((b.get("uiTokenAmount") or {}).get("uiAmount")) or 0)
            out[o] = out.get(o, 0.0) + amt
            idx = b.get("accountIndex")
            if idx is not None and idx < len(keys):
                accts[o] = keys[idx]
        return out, accts

    pre, _ = bal(meta.get("preTokenBalances"))
    post, accts = bal(meta.get("postTokenBalances"))
    d_tok = post.get(payer, 0.0) - pre.get(payer, 0.0)
    if d_tok == 0:
        return None
    pb, qb = meta.get("preBalances") or [], meta.get("postBalances") or []
    d_sol = ((qb[0] - pb[0]) / SOL_DECIMALS) if pb and qb else 0.0
    return {"trader": payer, "side": "buy" if d_tok > 0 else "sell", "tokens": abs(d_tok),
            "sol": d_sol, "token_account": accts.get(payer), "slot": tx.get("slot"),
            "ts": tx.get("blockTime")}


def first_signatures(rpc, address, max_pages):
    """Page back to the oldest signatures of `address`. Returns (oldest_first_list, complete)."""
    before, last_page = None, []
    for _ in range(max_pages):
        opts = {"limit": 1000}
        if before:
            opts["before"] = before
        page = rpc.call("getSignaturesForAddress", [address, opts]) or []
        if not page:
            break
        last_page = page
        if len(page) < 1000:
            return list(reversed(page)), True
        before = page[-1]["signature"]
    return list(reversed(last_page)), False


def early_buyers(rpc, mint, cfg):
    """Stage 1 for one token. Returns dict with creation info and first buy per wallet."""
    c = cfg["walletfinder"]
    sigs, complete = first_signatures(rpc, mint, c["max_sig_pages"])
    if not complete:
        return {"mint": mint, "complete": False, "buyers": {}}
    sigs = [s for s in sigs if s.get("err") is None][: c["early_txs"]]
    if not sigs:
        return {"mint": mint, "complete": True, "buyers": {}}
    create_slot = sigs[0].get("slot")
    create_ts = sigs[0].get("blockTime")
    buyers, by_sig = {}, defaultdict(list)
    for s in sigs:
        try:
            tx = rpc.call("getTransaction", [s["signature"], {"encoding": "jsonParsed",
                                                              "maxSupportedTransactionVersion": TX_VERSION}])
        except RpcError:
            continue
        t = parse_trade(tx, mint)
        if not t or t["side"] != "buy":
            continue
        by_sig[s["signature"]].append(t["trader"])
        if t["trader"] not in buyers:
            buyers[t["trader"]] = {"slot_offset": (t["slot"] or 0) - (create_slot or 0),
                                   "sec_offset": (t["ts"] or 0) - (create_ts or 0),
                                   "sol_in": -t["sol"], "token_account": t["token_account"],
                                   "sig": s["signature"]}
    # same-transaction multi-buyer bundles (rare when trader = fee payer, but recorded)
    for sig, ws in by_sig.items():
        if len(set(ws)) > 1:
            for w in ws:
                buyers[w]["bundle"] = True
    return {"mint": mint, "complete": True, "create_slot": create_slot, "create_ts": create_ts,
            "buyers": buyers}


def wallet_activity(rpc, wallet):
    """Transactions per day over the wallet's last <=1000 transactions."""
    sigs = rpc.call("getSignaturesForAddress", [wallet, {"limit": 1000}]) or []
    if len(sigs) < 2:
        return {"txs": len(sigs), "per_day": 0.0}
    t0, t1 = sigs[-1].get("blockTime") or 0, sigs[0].get("blockTime") or 0
    days = max((t1 - t0) / 86400, 1 / 24)
    return {"txs": len(sigs), "per_day": round(len(sigs) / days, 1), "saturated": len(sigs) >= 1000}


def token_pnl(rpc, wallet, token_account, mint, max_txs):
    """Realized SOL P&L of `wallet` in `mint`, from its token account's history."""
    if not token_account:
        return None
    sigs = rpc.call("getSignaturesForAddress", [token_account, {"limit": max_txs}]) or []
    bought = sold = sol_in = sol_out = 0.0
    first_buy = last_sell = None
    for s in reversed(sigs):
        if s.get("err") is not None:
            continue
        try:
            tx = rpc.call("getTransaction", [s["signature"], {"encoding": "jsonParsed",
                                                              "maxSupportedTransactionVersion": TX_VERSION}])
        except RpcError:
            continue
        t = parse_trade(tx, mint)
        if not t or t["trader"] != wallet:
            continue
        if t["side"] == "buy":
            bought += t["tokens"]
            sol_in += -t["sol"]
            first_buy = first_buy or t["ts"]
        else:
            sold += t["tokens"]
            sol_out += t["sol"]
            last_sell = t["ts"]
    if bought == 0:
        return None
    return {"sol_in": round(sol_in, 4), "sol_out": round(sol_out, 4),
            "realized_sol": round(sol_out - sol_in * min(1.0, sold / bought), 4),
            "sold_frac": round(min(1.0, sold / bought), 3),
            "hold_min": round((last_sell - first_buy) / 60, 1) if first_buy and last_sell else None,
            "n_trades": len(sigs)}


def run(cfg, winners, dead_mints, out_dir="research", api_key=None, post=None, log=print):
    c = cfg["walletfinder"]
    key = api_key if api_key is not None else os.environ.get("HELIUS_API_KEY", "")
    if not key and post is None:
        raise SystemExit("HELIUS_API_KEY not set")
    rpc = Rpc(RPC_URL.format(key=key), min_interval=c["min_interval"], post=post)
    os.makedirs(out_dir, exist_ok=True)
    cache_path = os.path.join(out_dir, "early_buyers_cache.json")
    cache = {}
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            cache = json.load(f)

    def stage1(mint):
        if mint in cache:
            return cache[mint]
        if rpc.calls >= c["credit_budget"]:
            return None
        try:
            r = early_buyers(rpc, mint, cfg)
        except RpcError as e:
            log(f"[wallets] {mint[:8]} failed: {e}")
            return None
        cache[mint] = r
        with open(cache_path, "w") as f:
            json.dump(cache, f)
        return r

    win_hits, dead_hits = defaultdict(list), defaultdict(int)
    for t in winners:
        r = stage1(t["address"])
        if not r:
            continue
        log(f"[wallets] {t['symbol']}: {len(r['buyers'])} early buyers (complete={r['complete']})")
        for w, info in r["buyers"].items():
            win_hits[w].append({**info, "mint": t["address"], "symbol": t["symbol"]})
    for m in dead_mints:
        r = stage1(m)
        if not r:
            continue
        for w in r["buyers"]:
            dead_hits[w] += 1

    n_dead = sum(1 for m in dead_mints if m in cache and cache[m].get("complete"))
    cands = [w for w, hits in win_hits.items() if len({h["mint"] for h in hits}) >= c["min_winners"]]
    cands.sort(key=lambda w: (-len(win_hits[w]), dead_hits.get(w, 0)))
    log(f"[wallets] {len(win_hits)} distinct early buyers; {len(cands)} early on >= {c['min_winners']} winners")

    rows = []
    for w in cands[: c["max_candidates"]]:
        if rpc.calls >= c["credit_budget"]:
            log("[wallets] credit budget reached; remaining candidates not profiled")
            break
        try:
            act = wallet_activity(rpc, w)
        except RpcError:
            act = {"txs": None, "per_day": None}
        hits = win_hits[w]
        pnls = []
        for h in hits[: c["max_tokens_per_wallet"]]:
            try:
                p = token_pnl(rpc, w, h.get("token_account"), h["mint"], c["max_pnl_txs"])
            except RpcError:
                p = None
            if p:
                pnls.append(p)
        snipes = sum(1 for h in hits if h["slot_offset"] <= c["sniper_max_slot_offset"])
        bundles = sum(1 for h in hits if h.get("bundle"))
        holds = [p["hold_min"] for p in pnls if p["hold_min"] is not None]
        realized = sum(p["realized_sol"] for p in pnls)
        flags = []
        if act.get("per_day") and act["per_day"] > c["bot_txs_per_day"]:
            flags.append("high_frequency")
        if snipes >= max(1, len(hits) * 0.5):
            flags.append("launch_sniper")
        if bundles:
            flags.append("bundled")
        if dead_hits.get(w, 0) >= max(1, n_dead * c["max_dead_frac"]):
            flags.append("buys_dead_tokens_too")
        if holds and sorted(holds)[len(holds) // 2] < c["min_median_hold_min"]:
            flags.append("flipper")
        rows.append({
            "wallet": w, "winners_early": len({h["mint"] for h in hits}),
            "dead_early": dead_hits.get(w, 0), "dead_checked": n_dead,
            "symbols": " ".join(sorted({h["symbol"] for h in hits})),
            "median_entry_sec": sorted(h["sec_offset"] for h in hits)[len(hits) // 2],
            "snipes": snipes, "tx_per_day": act.get("per_day"),
            "realized_sol": round(realized, 3), "profitable_tokens": sum(1 for p in pnls if p["realized_sol"] > 0),
            "pnl_checked": len(pnls),
            "median_hold_min": sorted(holds)[len(holds) // 2] if holds else None,
            "flags": ",".join(flags), "copy_candidate": "YES" if not flags and realized > 0 else "no",
            "solscan": f"https://solscan.io/account/{w}",
        })
    rows.sort(key=lambda r: (r["copy_candidate"] != "YES", -r["realized_sol"]))

    with open(os.path.join(out_dir, "watchlist.csv"), "w", newline="") as f:
        if rows:
            wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            wr.writeheader()
            wr.writerows(rows)
    write_markdown(rows, winners, cache, n_dead, len(win_hits), rpc.calls, os.path.join(out_dir, "..", "WALLETS.md"), cfg)
    return rows


def write_markdown(rows, winners, cache, n_dead, n_buyers, credits, path, cfg):
    c = cfg["walletfinder"]
    done = [t for t in winners if t["address"] in cache and cache[t["address"]].get("complete")]
    yes = [r for r in rows if r["copy_candidate"] == "YES"]
    L = ["# Wallet finder: early buyers of CoreSight winners", "",
         f"Updated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}", "",
         f"- Winners analysed: **{len(done)} / {len(winners)}** (first {c['early_txs']} transactions each)",
         f"- Dead tokens used as a control group: **{n_dead}**",
         f"- Distinct early buyers on winners: **{n_buyers}**",
         f"- Wallets early on >= {c['min_winners']} winners and profiled: **{len(rows)}**",
         f"- Passing every check (copy candidates): **{len(yes)}**",
         f"- Helius credits this run: {credits}", "",
         "**Hindsight warning:** these wallets were picked because they were early on tokens we already",
         "know won. That says nothing reliable about their next trade until we track them forward.", "",
         "Flags: `high_frequency` (bot-like activity), `launch_sniper` (buys in the first slots),",
         "`bundled`, `buys_dead_tokens_too` (indiscriminate), `flipper` (median hold too short to copy).", "",
         "| # | wallet | winners early | dead early | symbols | realized SOL | profitable/checked | tx/day | median hold (min) | flags | copy? |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows[:60], 1):
        w = r["wallet"]
        L.append(f"| {i} | [{w[:6]}…{w[-4:]}]({r['solscan']}) | {r['winners_early']} | {r['dead_early']}/{r['dead_checked']} | "
                 f"{r['symbols'][:40]} | {r['realized_sol']:+.2f} | {r['profitable_tokens']}/{r['pnl_checked']} | "
                 f"{r['tx_per_day']} | {r['median_hold_min']} | {r['flags'] or '-'} | {r['copy_candidate']} |")
    L.append("")
    L.append("Full list with full addresses: `research/watchlist.csv`.")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


# ============================================================== v2
# v1 judged wallets on the very winners they were picked from (hindsight) and let spray bots through:
# a wallet buying 300-400 new tokens a day is early on some winners by chance. v2 judges each wallet on
# its RECENT trading overall, with the CoreSight winners REMOVED, and rejects sprayers.

def profile_wallet(rpc, wallet, max_txs, exclude_mints=()):
    """Aggregate a wallet's last `max_txs` transactions into per-token round trips."""
    from .copytrade import wallet_trades
    sigs = rpc.call("getSignaturesForAddress", [wallet, {"limit": max_txs}]) or []
    per = {}
    times = []
    for s in sigs:
        if s.get("err") is not None or not s.get("blockTime"):
            continue
        try:
            tx = rpc.call("getTransaction", [s["signature"], {"encoding": "jsonParsed",
                                                              "maxSupportedTransactionVersion": TX_VERSION}])
        except RpcError:
            continue
        for mint, side, tokens, sol in wallet_trades(tx, wallet):
            times.append(s["blockTime"])
            p = per.setdefault(mint, {"buy_sol": 0.0, "sell_sol": 0.0, "bought": 0.0, "sold": 0.0,
                                      "first_buy": None, "last_sell": None, "n_buys": 0})
            if side == "buy":
                p["buy_sol"] += -sol
                p["bought"] += tokens
                p["n_buys"] += 1
                p["first_buy"] = min(p["first_buy"] or s["blockTime"], s["blockTime"])
            else:
                p["sell_sol"] += sol
                p["sold"] += tokens
                p["last_sell"] = max(p["last_sell"] or s["blockTime"], s["blockTime"])
    days = max(((max(times) - min(times)) / 86400) if len(times) > 1 else 0, 1 / 24)
    closed, pnls, holds = 0, [], []
    for mint, p in per.items():
        if mint in exclude_mints or p["bought"] <= 0:
            continue                        # winners removed; sells of tokens bought before the window skipped
        frac = min(1.0, p["sold"] / p["bought"])
        if frac >= 0.9:
            closed += 1
            pnls.append(p["sell_sol"] - p["buy_sol"])
            if p["first_buy"] and p["last_sell"] and p["last_sell"] >= p["first_buy"]:
                holds.append((p["last_sell"] - p["first_buy"]) / 60)
    buys = [p for m, p in per.items() if p["n_buys"] and m not in exclude_mints]
    total = sum(pnls)
    wins = [x for x in pnls if x > 0]
    return {
        "window_days": round(days, 2), "txs": len(sigs),
        "tokens_bought_per_day": round(len(buys) / days, 1),
        "avg_buy_sol": round(sum(p["buy_sol"] for p in buys) / max(1, sum(p["n_buys"] for p in buys)), 3),
        "closed_trades": closed, "realized_sol_ex_winners": round(total, 3),
        "win_rate": round(len(wins) / closed, 2) if closed else None,
        "top_win_share": round(max(wins) / total, 2) if wins and total > 0 else None,
        "median_hold_min": round(sorted(holds)[len(holds) // 2], 1) if holds else None,
    }


def v2_verdict(m, c):
    reasons = []
    if m["tokens_bought_per_day"] > c["v2_max_tokens_per_day"]:
        reasons.append("sprays_tokens")
    if m["avg_buy_sol"] < c["v2_min_avg_buy_sol"]:
        reasons.append("buys_too_small")
    if m["closed_trades"] < c["v2_min_closed_trades"]:
        reasons.append("too_few_closed_trades")
    if m["realized_sol_ex_winners"] <= 0:
        reasons.append("loses_money_ex_winners")
    if m["top_win_share"] is not None and m["top_win_share"] > c["v2_max_top_win_share"]:
        reasons.append("one_hit_wonder")
    if m["median_hold_min"] is not None and m["median_hold_min"] < c["v2_min_median_hold_min"]:
        reasons.append("flips_too_fast")
    return reasons


def run_v2(cfg, winners, out_dir="research", api_key=None, post=None, log=print):
    c = cfg["walletfinder"]
    key = api_key if api_key is not None else os.environ.get("HELIUS_API_KEY", "")
    if not key and post is None:
        raise SystemExit("HELIUS_API_KEY not set")
    rpc = Rpc(RPC_URL.format(key=key), min_interval=c["min_interval"], post=post)
    with open(os.path.join(out_dir, "early_buyers_cache.json")) as f:
        cache = json.load(f)
    win_mints = {t["address"] for t in winners}
    sym = {t["address"]: t["symbol"] for t in winners}
    on_winners, on_dead = defaultdict(list), set()
    for mint, r in cache.items():
        for w, info in (r.get("buyers") or {}).items():
            if mint in win_mints:
                on_winners[w].append((sym[mint], info.get("sol_in") or 0, info.get("slot_offset") or 0))
            else:
                on_dead.add(w)
    pool = [w for w, hits in on_winners.items()
            if w not in on_dead and max(h[1] for h in hits) >= c["v2_min_avg_buy_sol"]
            and not all(h[2] <= c["sniper_max_slot_offset"] for h in hits)]
    pool.sort(key=lambda w: -max(h[1] for h in on_winners[w]))
    log(f"[v2] {len(on_winners)} early buyers on winners; {len(pool)} after dead-token, size and sniper filters")

    # stage A: cheap activity filter (1 credit each)
    keep = []
    for w in pool:
        if rpc.calls >= c["v2_credit_budget"]:
            break
        try:
            act = wallet_activity(rpc, w)
        except RpcError:
            continue
        if act.get("per_day") is not None and act["per_day"] <= c["v2_max_tx_per_day"]:
            keep.append((w, act["per_day"]))
    log(f"[v2] {len(keep)} pass the activity filter (<= {c['v2_max_tx_per_day']} tx/day)")

    # stage B: recent overall trading, winners removed
    rows = []
    for w, tpd in keep[: c["v2_max_profiles"]]:
        if rpc.calls >= c["v2_credit_budget"]:
            log("[v2] credit budget reached")
            break
        try:
            m = profile_wallet(rpc, w, c["v2_profile_txs"], exclude_mints=win_mints)
        except RpcError as e:
            log(f"[v2] {w[:6]} failed: {e}")
            continue
        reasons = v2_verdict(m, c)
        rows.append({"wallet": w, "tx_per_day": tpd, **m,
                     "early_on": " ".join(sorted({h[0] for h in on_winners[w]})),
                     "verdict": "COPY CANDIDATE" if not reasons else ",".join(reasons),
                     "solscan": f"https://solscan.io/account/{w}"})
    rows.sort(key=lambda r: (r["verdict"] != "COPY CANDIDATE", -r["realized_sol_ex_winners"]))
    with open(os.path.join(out_dir, "watchlist_v2.csv"), "w", newline="") as f:
        if rows:
            wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            wr.writeheader()
            wr.writerows(rows)
    _write_v2_md(rows, len(on_winners), len(pool), len(keep), rpc.calls, c,
                 os.path.join(out_dir, "..", "WALLETS_V2.md"))
    return rows


def _write_v2_md(rows, n_buyers, n_pool, n_keep, credits, c, path):
    from collections import Counter
    yes = [r for r in rows if r["verdict"] == "COPY CANDIDATE"]
    why = Counter(x for r in rows if r["verdict"] != "COPY CANDIDATE" for x in r["verdict"].split(","))
    L = ["# Wallet finder v2: judged on recent overall trading, winners removed", "",
         f"Updated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}", "",
         "| step | wallets |", "|---|---|",
         f"| early buyers of CoreSight winners | {n_buyers} |",
         f"| not early on dead tokens, bought >= {c['v2_min_avg_buy_sol']} SOL, not a launch sniper | {n_pool} |",
         f"| <= {c['v2_max_tx_per_day']} transactions/day (cheap bot filter) | {n_keep} |",
         f"| profiled (last {c['v2_profile_txs']} transactions each) | {len(rows)} |",
         f"| **pass every v2 check** | **{len(yes)}** |", "",
         f"Checks: <= {c['v2_max_tokens_per_day']} tokens bought/day, avg buy >= {c['v2_min_avg_buy_sol']} SOL, "
         f">= {c['v2_min_closed_trades']} closed trades, profitable with the CoreSight winners removed, "
         f"biggest win < {int(c['v2_max_top_win_share'] * 100)}% of profit, median hold >= {c['v2_min_median_hold_min']} min.", "",
         "Why wallets failed: " + ", ".join(f"{k} {v}" for k, v in why.most_common()), "",
         f"Helius credits: {credits}", "",
         "| # | wallet | verdict | realized SOL (ex winners) | closed | win rate | tokens/day | avg buy SOL | median hold (min) | biggest win share | window (days) | early on |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows[:50], 1):
        w = r["wallet"]
        L.append(f"| {i} | [{w[:6]}…{w[-4:]}]({r['solscan']}) | {r['verdict']} | {r['realized_sol_ex_winners']:+.2f} | "
                 f"{r['closed_trades']} | {r['win_rate']} | {r['tokens_bought_per_day']} | {r['avg_buy_sol']} | "
                 f"{r['median_hold_min']} | {r['top_win_share']} | {r['window_days']} | {r['early_on'][:30]} |")
    L += ["", "Hindsight check: these wallets entered the funnel via known winners, but are judged on their "
          "other recent trades. Book C's forward copying is still the real test."]
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")
