"""ANALYST: 0-100 score for scout survivors. Every component is logged so the Lab
can later test whether the score actually predicts anything."""
import math


def _clip(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def score(pool):
    comps = {}
    # unique buyers: 150 -> 0.3, 600+ -> 1.0 (log scale)
    b = pool.buyers_h1 or 0
    comps["buyers"] = _clip(math.log10(max(b, 1) / 50) / math.log10(12)) if b else 0.0
    # buy skew: buys share of h1 txns, 50% -> 0, 70%+ -> 1
    if pool.buys_h1 is not None and pool.sells_h1 is not None and (pool.buys_h1 + pool.sells_h1):
        share = pool.buys_h1 / (pool.buys_h1 + pool.sells_h1)
        comps["buy_skew"] = _clip((share - 0.5) / 0.2)
    else:
        comps["buy_skew"] = 0.0
    # momentum: 5m volume pace vs 1h, plus moderate (not overheated) h1 change
    if pool.vol_h1 and pool.vol_m5 is not None:
        pace = pool.vol_m5 * 12 / pool.vol_h1
        comps["pace"] = _clip((pace - 0.5) / 1.0)
    else:
        comps["pace"] = 0.0
    ch = pool.chg_h1
    comps["trend"] = 0.0 if ch is None else _clip(1 - abs(ch - 25) / 55)
    # turnover: h1 volume / liquidity, 1x -> 0.3, 4x+ -> 1
    if pool.liquidity_usd and pool.vol_h1 is not None:
        comps["turnover"] = _clip(pool.vol_h1 / pool.liquidity_usd / 4)
    else:
        comps["turnover"] = 0.0
    # liquidity depth relative to market cap: liq/mcap 5% -> 0.3, 20%+ -> 1
    mc = pool.market_cap_usd or pool.fdv_usd
    comps["depth"] = _clip((pool.liquidity_usd or 0) / mc / 0.2) if mc else 0.0

    weights = {"buyers": 25, "buy_skew": 20, "pace": 15, "trend": 10, "turnover": 15, "depth": 15}
    total = sum(comps[k] * w for k, w in weights.items())
    return round(total, 1), {k: round(v, 2) for k, v in comps.items()}
