"""SCOUT rules. Each rule either passes or adds a kill reason. Missing data = kill."""


def scout(pool, cfg, now=None):
    """Return (passed: bool, kills: list[str], flags: list[str])."""
    c = cfg["scout"]
    kills, flags = [], []

    def need(name):
        v = getattr(pool, name)
        if v is None:
            kills.append(f"missing:{name}")
        return v

    liq = need("liquidity_usd")
    vol_h1 = need("vol_h1")
    buys = need("buys_h1")
    sells = need("sells_h1")
    buyers = need("buyers_h1")
    chg_h1 = need("chg_h1")
    age = pool.age_hours(now)
    if age is None:
        kills.append("missing:pool_created_at")

    if liq is not None and liq < c["min_liquidity_usd"]:
        kills.append("liquidity_low")
    if liq and vol_h1 is not None and vol_h1 < liq * c["min_vol_h1_to_liquidity"]:
        kills.append("volume_below_liquidity")
    if c.get("require_buys_gt_sells_h1") and buys is not None and sells is not None and buys <= sells:
        kills.append("sells_dominate")
    if age is not None:
        if age < c["min_age_hours"]:
            kills.append("too_young")
        if age > c["max_age_hours"]:
            kills.append("too_old")
    if buyers is not None and buyers < c["min_unique_buyers_h1"]:
        kills.append("few_unique_buyers")
    if buyers and buys is not None and (buys / buyers) > c["max_buys_per_buyer_h1"]:
        kills.append("wash_churn")
    if chg_h1 is not None and chg_h1 > c["max_price_change_h1_pct"]:
        kills.append("overheated")

    if pool.vol_m5 is not None and vol_h1 and pool.vol_m5 * c["heating_up_multiplier"] > vol_h1:
        flags.append("HEATING_UP")

    return (len(kills) == 0, kills, flags)


def buys_per_buyer(pool):
    if not pool.buyers_h1 or pool.buys_h1 is None:
        return None
    return pool.buys_h1 / pool.buyers_h1
