"""LAB: measure what actually happened to every pool the scanner saw.

This is where rules get judged by data instead of by vibes:
- did pools that PASSED do better than pools that were KILLED?
- does each kill rule actually avoid losers? (near-miss analysis)
- which stop / trailing exit combination has the best expectancy AFTER costs?

Optimizes average net return per trade (expectancy), NOT win rate.
"""
import json
import statistics
from collections import Counter, defaultdict

HORIZONS = [("15m", 900), ("1h", 3600), ("4h", 14400), ("24h", 86400)]


def price_at(samples, ref_ts, horizon_s):
    """First sample at/after ref_ts+horizon, within a tolerance window."""
    target = ref_ts + horizon_s
    tol = max(600, horizon_s * 0.5)
    for s in samples:
        if s["ts"] >= target:
            return s["price_usd"] if s["ts"] - target <= tol else None
    return None


def reliable(samples, first_price):
    """Drop readings where liquidity shows ~0 but the price has not fallen: both GeckoTerminal and
    DexScreener return these (frozen price, zero reserve) for pools they stopped tracking properly,
    including pumpswap pools whose liquidity can't even be pulled. They are data gaps, not rugs."""
    if not first_price:
        return list(samples)
    return [s for s in samples
            if not (s["liquidity_usd"] is not None and s["liquidity_usd"] < 100
                    and s["price_usd"] is not None and s["price_usd"] >= first_price * 0.5)]


def is_rugged(samples, ref_ts, ref_price, ref_liq, cfg):
    """Rug = price crashed (default -90%), or liquidity vanished (default -80%) WITH the price
    at least halving at that point."""
    lab = cfg["lab"]
    after = [s for s in samples if s["ts"] >= ref_ts]
    if not after or not ref_price:
        return None
    for s in after:
        p, liq = s["price_usd"], s["liquidity_usd"]
        if p is not None and p <= ref_price * (1 - lab["rug_price_drop_pct"] / 100):
            return True
        if (ref_liq and liq is not None and liq <= ref_liq * (1 - lab["rug_liquidity_drop_pct"] / 100)
                and p is not None and p <= ref_price * 0.5):
            return True
    return False


def simulate_exit(samples, entry_ts, entry_price, stop_pct, trail_act_pct, trail_dist_pct,
                  cost_pct, max_hold_s=86400):
    """Paper exit simulation on sampled prices. Gaps are realistic: if price jumps
    straight through the stop between samples, we exit at the (worse) sampled price.
    Returns (net_return, reason) or (None, None) if no data after entry."""
    after = [s for s in samples if entry_ts < s["ts"] <= entry_ts + max_hold_s]
    if not after or not entry_price:
        return None, None
    half = cost_pct / 200.0
    entry_eff = entry_price * (1 + half)
    peak = entry_price
    trailing = False
    exit_price, reason = None, None
    for s in after:
        p = s["price_usd"]
        if p is None:
            continue
        peak = max(peak, p)
        if p <= entry_price * (1 + stop_pct / 100):
            exit_price, reason = p, "stop"
            break
        if not trailing and peak >= entry_price * (1 + trail_act_pct / 100):
            trailing = True
        if trailing and p <= peak * (1 - trail_dist_pct / 100):
            exit_price, reason = p, "trail"
            break
    if exit_price is None:
        exit_price, reason = after[-1]["price_usd"], "time"
    return exit_price * (1 - half) / entry_eff - 1, reason


def _med(xs):
    return statistics.median(xs) if xs else None


def _pct(x):
    return "   -  " if x is None else f"{x * 100:+6.1f}%"


def build_report(db, cfg, now):
    pools = db.all_pools()
    lines = []
    w = lines.append

    # ---------- funnel ----------
    total = len(pools)
    kill_counter = Counter()
    scout_pass = score_kill = audit_kill = final = 0
    for p in pools:
        kills = json.loads(p["first_kills"] or "[]")
        if kills:
            for k in kills:
                k = k.split("(")[0]
                kill_counter[k.split(":")[0] if k.startswith(("missing", "unknown", "rc_danger")) else k] += 1
    obs = db.conn.execute(
        "SELECT pool_address, MAX(scout_pass) sp, MAX(final_pass) fp, GROUP_CONCAT(kills,'|') ks "
        "FROM observations GROUP BY pool_address").fetchall()
    scout_passed = {o["pool_address"] for o in obs if o["sp"]}
    for o in obs:
        if o["sp"]:
            scout_pass += 1
            if o["fp"]:
                final += 1
            elif "score_below" in (o["ks"] or ""):
                score_kill += 1
            else:
                audit_kill += 1

    w("=" * 64)
    w("TRENCHLAB REPORT")
    w("=" * 64)
    w(f"pools seen           {total}")
    w(f"passed SCOUT         {scout_pass}")
    w(f"  killed by SCORE    {score_kill}")
    w(f"  killed by AUDIT    {audit_kill}")
    w(f"FINAL PASS           {final}")
    w("")
    w("top kill reasons at first sighting (a pool can have several):")
    for k, n in kill_counter.most_common(10):
        w(f"  {k:<28}{n:>6}")

    # ---------- outcomes by group ----------
    groups = defaultdict(list)
    data_gaps = 0
    for p in pools:
        raw = db.samples_for(p["pool_address"])
        samples = reliable(raw, p["first_price"])
        data_gaps += len(raw) != len(samples)
        if p["first_pass_ts"]:
            g = "FINAL PASS"
            ref_ts, ref_p = p["first_pass_ts"], p["first_pass_price"]
        else:
            g = "SCOUT PASS, killed later" if p["pool_address"] in scout_passed else "KILLED (tracked)"
            ref_ts, ref_p = p["first_seen_ts"], p["first_price"]
        if not samples or not ref_p:
            continue
        rets = {}
        for name, h in HORIZONS:
            px = price_at(samples, ref_ts, h)
            rets[name] = None if px is None else px / ref_p - 1
        rug = is_rugged(samples, ref_ts, ref_p, p["first_liq"], cfg)
        groups[g].append((p, rets, rug))

    w("")
    w(f"OUTCOMES (median price change from first sighting / first pass; "
      f"{data_gaps} pools had zero-liquidity/frozen-price data gaps, ignored)")
    w(f"{'group':<26}{'n':>5}{'+15m':>9}{'+1h':>9}{'+4h':>9}{'+24h':>9}{'rug%':>7}")
    for g in ["FINAL PASS", "SCOUT PASS, killed later", "KILLED (tracked)"]:
        rows = groups.get(g, [])
        if not rows:
            continue
        meds = [_med([r[1][h] for r in rows if r[1][h] is not None]) for h, _ in HORIZONS]
        rugs = [r[2] for r in rows if r[2] is not None]
        rug_rate = (sum(rugs) / len(rugs)) if rugs else None
        w(f"{g:<26}{len(rows):>5}" + "".join(f"{_pct(m):>9}" for m in meds)
          + (f"{rug_rate * 100:>6.0f}%" if rug_rate is not None else "     -"))

    # ---------- near misses: is each rule pulling its weight? ----------
    near = defaultdict(list)
    for p, rets, rug in groups.get("KILLED (tracked)", []):
        kills = json.loads(p["first_kills"] or "[]")
        if len(kills) == 1:
            near[kills[0].split("(")[0]].append((rets, rug))
    if near:
        w("")
        w("NEAR MISSES: pools killed by exactly ONE rule")
        w("(if these do as well as FINAL PASS, that rule may be killing winners)")
        w(f"{'rule':<28}{'n':>5}{'+4h med':>10}{'+24h med':>10}{'rug%':>7}")
        for rule, rows in sorted(near.items(), key=lambda kv: -len(kv[1])):
            m4 = _med([r[0]["4h"] for r in rows if r[0]["4h"] is not None])
            m24 = _med([r[0]["24h"] for r in rows if r[0]["24h"] is not None])
            rugs = [r[1] for r in rows if r[1] is not None]
            rr = f"{sum(rugs) / len(rugs) * 100:>6.0f}%" if rugs else "     -"
            w(f"{rule:<28}{len(rows):>5}{_pct(m4):>10}{_pct(m24):>10}{rr}")

    # ---------- does the score predict anything? ----------
    buckets = defaultdict(list)
    rows = db.conn.execute(
        "SELECT pool_address, MAX(score) sc FROM observations WHERE score IS NOT NULL GROUP BY pool_address"
    ).fetchall()
    sc_map = {r["pool_address"]: r["sc"] for r in rows}
    for g in ("FINAL PASS", "SCOUT PASS, killed later"):
        for p, rets, rug in groups.get(g, []):
            sc = sc_map.get(p["pool_address"])
            if sc is None:
                continue
            b = "80+" if sc >= 80 else "70-79" if sc >= 70 else "60-69" if sc >= 60 else "<60"
            buckets[b].append((rets, rug))
    if buckets:
        w("")
        w("SCORE CHECK: scout passers by score (higher buckets should do better;")
        w("if they don't, the score is decoration - change it)")
        w(f"{'score':<8}{'n':>5}{'+4h med':>10}{'+24h med':>10}{'rug%':>7}")
        for b in ["80+", "70-79", "60-69", "<60"]:
            rs = buckets.get(b)
            if not rs:
                continue
            m4 = _med([r[0]["4h"] for r in rs if r[0]["4h"] is not None])
            m24 = _med([r[0]["24h"] for r in rs if r[0]["24h"] is not None])
            rugs = [r[1] for r in rs if r[1] is not None]
            rr = f"{sum(rugs) / len(rugs) * 100:>6.0f}%" if rugs else "     -"
            w(f"{b:<8}{len(rs):>5}{_pct(m4):>10}{_pct(m24):>10}{rr}")

    # ---------- does the cabal finder predict anything? ----------
    crow = db.conn.execute(
        "SELECT token_mint, metrics FROM clusters c WHERE ts = "
        "(SELECT MAX(ts) FROM clusters WHERE token_mint=c.token_mint)").fetchall()
    cmap = {}
    for r in crow:
        m = json.loads(r["metrics"] or "{}")
        if "largest_cluster_pct" in m:
            cmap[r["token_mint"]] = m
    if cmap:
        def bucket_cluster(v):
            return "none" if v == 0 else "<15%" if v < 15 else "15-30%" if v < 30 else "30%+"

        def bucket_fresh(v):
            return "<20%" if v < 20 else "20-40%" if v < 40 else "40%+"

        by_c, by_f, by_b = defaultdict(list), defaultdict(list), defaultdict(list)
        for rows_ in groups.values():
            for p, rets, rug in rows_:
                m = cmap.get(p["token_mint"])
                if not m:
                    continue
                by_c[bucket_cluster(m["largest_cluster_pct"])].append((rets, rug))
                by_f[bucket_fresh(m["fresh_pct"])].append((rets, rug))
                if "same_slot_pct" in m:
                    v = m["same_slot_pct"]
                    by_b["none" if v == 0 else "<20%" if v < 20 else "20%+"].append((rets, rug))
        w("")
        w("CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)")
        w("(bigger clusters should rug more / do worse; if not, the cluster rule is noise)")
        for title, data, order in (("cluster", by_c, ["none", "<15%", "15-30%", "30%+"]),
                                   ("bundled", by_b, ["none", "<20%", "20%+"]),
                                   ("fresh", by_f, ["<20%", "20-40%", "40%+"])):
            w(f"{title:<8}{'n':>5}{'+1h med':>10}{'+4h med':>10}{'+24h med':>10}{'rug%':>7}")
            for b in order:
                rs = data.get(b)
                if not rs:
                    continue
                m1 = _med([r[0]["1h"] for r in rs if r[0]["1h"] is not None])
                m4 = _med([r[0]["4h"] for r in rs if r[0]["4h"] is not None])
                m24 = _med([r[0]["24h"] for r in rs if r[0]["24h"] is not None])
                rugs = [r[1] for r in rs if r[1] is not None]
                rr = f"{sum(rugs) / len(rugs) * 100:>6.0f}%" if rugs else "     -"
                w(f"{b:<8}{len(rs):>5}{_pct(m1):>10}{_pct(m4):>10}{_pct(m24):>10}{rr}")
        used = db.credits_used(now)
        w(f"tokens analysed: {len(cmap)} | helius credits today: {used}/{cfg['cluster']['daily_credit_budget']}")

    # ---------- exit grid on final passes ----------
    lab = cfg["lab"]
    grid = lab["exit_grid"]
    passers = [(p, reliable(db.samples_for(p["pool_address"]), p["first_price"]))
               for p, _, _ in groups.get("FINAL PASS", [])]
    passers = [(p, s) for p, s in passers if s]
    w("")
    w(f"EXIT GRID on FINAL PASS entries (round-trip cost {lab['round_trip_cost_pct']}%, "
      f"trail distance {grid['trail_distance_pct']}%)")
    if not passers:
        w("  no passes with price data yet - let it collect for a few days")
    else:
        w(f"{'stop':>6}{'trail@':>8}{'n':>5}{'win%':>7}{'avg net':>10}{'median':>9}{'worst':>9}")
        best = None
        for st in grid["stops_pct"]:
            for act in grid["trail_activate_pct"]:
                res = []
                for p, s in passers:
                    r, _ = simulate_exit(s, p["first_pass_ts"], p["first_pass_price"], st, act,
                                         grid["trail_distance_pct"], lab["round_trip_cost_pct"])
                    if r is not None:
                        res.append(r)
                if not res:
                    continue
                avg = sum(res) / len(res)
                win = sum(1 for r in res if r > 0) / len(res)
                w(f"{st:>5}%{act:>7}%{len(res):>5}{win * 100:>6.0f}%{_pct(avg):>10}{_pct(_med(res)):>9}{_pct(min(res)):>9}")
                if best is None or avg > best[0]:
                    best = (avg, st, act, len(res))
        if best:
            w(f"  best so far: stop {best[1]}%, trail from +{best[2]}% -> avg {_pct(best[0]).strip()} "
              f"per trade over n={best[3]}")
            if best[3] < 100:
                w("  WARNING: n < 100. This is noise, not evidence. Do not trade on it.")
    if cfg.get("paper", {}).get("enabled"):
        from .paper import paper_report, comparison_report
        cmp_ = comparison_report(db)
        if cmp_:
            lines.extend(cmp_.split("\n"))
        for book in (db.paper_books() or ["A"]):
            pr = paper_report(db, cfg, book)
            if pr:
                lines.extend(pr.split("\n"))
    w("")
    w("Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.")
    w("Not financial advice. Paper results overstate live results.")
    return "\n".join(lines)
