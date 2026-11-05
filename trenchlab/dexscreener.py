"""DexScreener public API (free, no key, ~300 req/min) - used for outcome price tracking,
because GeckoTerminal's per-IP limit is easily hit from shared GitHub runner IPs."""
from .http import get_json

BASE = "https://api.dexscreener.com/latest/dex/pairs/{chain}/{pairs}"


def _f(x):
    try:
        return None if x is None else float(x)
    except (TypeError, ValueError):
        return None


def prices_multi(addresses, chain="solana", fetch=get_json):
    """Return {pair_address: (price_usd, liquidity_usd)} for up to N pairs (30 per call)."""
    out = {}
    for i in range(0, len(addresses), 30):
        chunk = addresses[i:i + 30]
        data = fetch(BASE.format(chain=chain, pairs=",".join(chunk)), min_interval=0.3)
        for p in (data or {}).get("pairs") or []:
            addr = p.get("pairAddress")
            if addr:
                out[addr] = (_f(p.get("priceUsd")), _f((p.get("liquidity") or {}).get("usd")))
    return out
