"""BOOK B: "pullback" entries (thesis started 2026-11-07).

Why: in the first ~2 days of data (Nov 5-7), FINAL PASS tokens from the momentum filters
(book A) fell a median -45% within 4h and -66% within 24h, and the highest scores did worst.
Buying "trending + heating up" looked like buying the top. Meanwhile two cabal signals
(bundled buys, fresh wallets) separated rugs from non-rugs. Book B tests the opposite idea:

  wait for a token that has ALREADY survived its first dump, is still liquid, has buyers
  coming back, and passes stricter holder-safety checks - then buy the bounce.

Entry rules (all must hold; every rejection is logged with its reason):
  price history (from our own tracking samples):
    - pool age 2-24h, at least 6 reliable price samples
    - price now 30-60% below the highest price we have seen
    - price now >= 5% above the lowest price of the last 2h, and that low is >= 20 min old
      (it has stopped falling)
    - liquidity now >= $30k and >= 50% of the highest liquidity seen (no liquidity drain)
  live activity (fresh GeckoTerminal data):
    - >= 75 unique buyers in the last hour, buys >= sells, 1h volume >= 30% of liquidity
    - not dumping right now (5-min price change > -5%)
  safety:
    - RugCheck/GoPlus audit passes (same as book A)
    - cabal finder: no kill AND bundled-buy share <= 5%, fresh-wallet share <= 20%,
      received-not-bought share <= 10%  (stricter than book A)
Sizing, exits and costs are IDENTICAL to book A, so A vs B isolates the entry rule.
"""
from .lab import reliable


def price_candidates(db, cfg, now):
    """Pools whose tracked price history matches the pullback pattern. Returns [(addr, info)]."""
    c = cfg["pullback"]
    out = []
    rows = db.conn.execute(
        """SELECT pool_address, token_mint, symbol, pool_created_ts, first_price, first_liq
           FROM pools WHERE track_until_ts >= ? AND COALESCE(first_liq, 0) >= ?
             AND pool_created_ts IS NOT NULL AND pool_created_ts BETWEEN ? AND ?""",
        (now, c["min_first_liq_usd"], now - c["max_age_hours"] * 3600, now - c["min_age_hours"] * 3600)).fetchall()
    for r in rows:
        if db.paper_traded_token(r["token_mint"], "B"):
            continue
        s = reliable(db.samples_for(r["pool_address"]), r["first_price"])
        s = [x for x in s if x["price_usd"]]
        if len(s) < c["min_samples"]:
            continue
        last = s[-1]
        if now - last["ts"] > 900:
            continue
        hi = max(x["price_usd"] for x in s)
        p = last["price_usd"]
        dd = p / hi - 1
        if not (-c["max_drawdown_pct"] / 100 <= dd <= -c["min_drawdown_pct"] / 100):
            continue
        window = [x for x in s if x["ts"] >= now - c["low_window_min"] * 60]
        low = min(window, key=lambda x: x["price_usd"])
        if p < low["price_usd"] * (1 + c["min_bounce_pct"] / 100):
            continue
        if now - low["ts"] < c["low_min_age_min"] * 60:
            continue
        liqs = [x["liquidity_usd"] for x in s if x["liquidity_usd"]]
        liq = last["liquidity_usd"] or 0
        if liq < c["min_liq_usd"] or (liqs and liq < max(liqs) * c["min_liq_vs_peak"]):
            continue
        out.append((r["pool_address"], {"drawdown_pct": round(dd * 100, 1),
                                        "bounce_pct": round((p / low["price_usd"] - 1) * 100, 1),
                                        "liq": round(liq)}))
    out.sort(key=lambda t: -t[1]["liq"])
    return out[: c["max_candidates_per_run"]]


def activity_kills(pool, cfg):
    c = cfg["pullback"]
    k = []
    if pool.buyers_h1 is None or pool.buys_h1 is None or pool.sells_h1 is None or pool.vol_h1 is None:
        return ["missing_activity"]
    if pool.buyers_h1 < c["min_buyers_h1"]:
        k.append("few_buyers_now")
    if pool.buys_h1 < pool.sells_h1:
        k.append("sellers_dominate_now")
    if pool.liquidity_usd and pool.vol_h1 < pool.liquidity_usd * c["min_vol_h1_to_liq"]:
        k.append("volume_dried_up")
    if pool.chg_m5 is not None and pool.chg_m5 < -c["max_m5_drop_pct"]:
        k.append("dumping_now")
    return k


def strict_cabal_kills(metrics, cfg):
    c = cfg["pullback"]
    k = []
    if metrics.get("same_slot_pct", 0) > c["max_same_slot_pct"]:
        k.append(f"b_bundled({metrics.get('same_slot_pct', 0):.0f}%)")
    if metrics.get("fresh_pct", 0) > c["max_fresh_pct"]:
        k.append(f"b_fresh({metrics.get('fresh_pct', 0):.0f}%)")
    if metrics.get("received_pct", 0) > c["max_received_pct"]:
        k.append(f"b_received({metrics.get('received_pct', 0):.0f}%)")
    return k


def run(db, gecko, auditor, cabal, trader_b, cfg, now, log=print):
    """Find pullback setups and hand passing ones to book B. Returns number of entries."""
    cands = price_candidates(db, cfg, now)
    if not cands:
        return 0
    info_by = dict(cands)
    try:
        fresh = {p.address: p for p in gecko.pools_multi([a for a, _ in cands])}
    except Exception as e:
        log(f"[B] activity fetch failed: {e}")
        return 0
    entries = 0
    for addr, info in cands:
        pool = fresh.get(addr)
        if pool is None:
            continue
        kills = activity_kills(pool, cfg)
        if not kills and auditor is not None:
            ok, akills, _ = auditor.audit(pool.token_mint)
            kills += akills
        if not kills:
            if cabal is None or not cabal.enabled:
                kills.append("unknown:cluster_disabled")
            else:
                res = cabal.check(pool.token_mint, now, auditor.known_accounts.get(pool.token_mint) if auditor else None)
                if res is None:
                    kills.append("unknown:cluster")
                else:
                    kills += res[0] + strict_cabal_kills(res[1], cfg)
        if kills:
            db.paper_skip(now, pool, "setup_rejected:" + kills[0].split("(")[0], "B")
            continue
        db.extend_tracking(addr, now + 24 * 3600)
        if trader_b.on_signal(pool, None, now, extra=info_by[addr]):
            entries += 1
    db.commit()
    return entries
