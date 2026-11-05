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


def is_rugged(samples, ref_ts, ref_price, ref_liq, cfg):
    lab = cfg["lab"]
    after = [s for s in samples if s["ts"] >= ref_ts]
    if not after or not ref_price:
        return None
    min_p = min(s["price_usd"] for s in after)
    if min_p <= ref_price * (1 - lab["rug_price_drop_pct"] / 100):
        return True
    liqs = [s["liquidity_usd"] for s in after if s["liquidity_usd"] is not None]
    if ref_liq and liqs and min(liqs) <= ref_liq * (1 - lab["rug_liquidity_drop_pct"] / 100):
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
    for p in pools:
        samples = db.samples_for(p["pool_address"])
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
    w("OUTCOMES (median price change from first sighting / first pass)")
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

    # ---------- exit grid on final passes ----------
    lab = cfg["lab"]
    grid = lab["exit_grid"]
    passers = [(p, db.samples_for(p["pool_address"])) for p, _, _ in groups.get("FINAL PASS", [])]
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
    w("")
    w("Sampling is every scan cycle (~5 min), so intra-candle wicks are missed.")
    w("Not financial advice. Paper results overstate live results.")
    return "\n".join(lines)
