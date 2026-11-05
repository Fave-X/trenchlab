"""GeckoTerminal public API (free, no key). Docs: https://www.geckoterminal.com/dex-api"""
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

from .http import get_json

BASE = "https://api.geckoterminal.com/api/v2"


def _f(x):
    """float or None"""
    try:
        return None if x is None else float(x)
    except (TypeError, ValueError):
        return None


def _i(x):
    try:
        return None if x is None else int(x)
    except (TypeError, ValueError):
        return None


@dataclass
class Pool:
    address: str
    network: str
    name: str = ""
    symbol: str = ""
    token_mint: str = ""
    dex: str = ""
    created_ts: float = None
    price_usd: float = None
    liquidity_usd: float = None
    fdv_usd: float = None
    market_cap_usd: float = None
    vol_m5: float = None
    vol_h1: float = None
    vol_h6: float = None
    vol_h24: float = None
    chg_m5: float = None
    chg_h1: float = None
    chg_h6: float = None
    buys_m5: int = None
    sells_m5: int = None
    buys_h1: int = None
    sells_h1: int = None
    buyers_h1: int = None
    sellers_h1: int = None
    source: str = ""
    extra: dict = field(default_factory=dict)

    def age_hours(self, now=None):
        if self.created_ts is None:
            return None
        now = now if now is not None else datetime.now(timezone.utc).timestamp()
        return (now - self.created_ts) / 3600.0

    def gecko_url(self):
        return f"https://www.geckoterminal.com/{self.network}/pools/{self.address}"

    def to_dict(self):
        return asdict(self)


def _parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return None


def parse_pool(item, network, included_tokens=None, source=""):
    a = item.get("attributes", {}) or {}
    rel = item.get("relationships", {}) or {}
    base_id = (((rel.get("base_token") or {}).get("data")) or {}).get("id", "")
    mint = base_id.split("_", 1)[1] if "_" in base_id else base_id
    dex = (((rel.get("dex") or {}).get("data")) or {}).get("id", "")

    symbol = ""
    if included_tokens and base_id in included_tokens:
        symbol = included_tokens[base_id].get("symbol", "") or ""
    name = a.get("name", "") or ""
    if not symbol and "/" in name:
        symbol = name.split("/")[0].strip()

    vol = a.get("volume_usd") or {}
    chg = a.get("price_change_percentage") or {}
    tx = a.get("transactions") or {}
    tm5 = tx.get("m5") or {}
    th1 = tx.get("h1") or {}

    return Pool(
        address=a.get("address") or item.get("id", "").split("_", 1)[-1],
        network=network,
        name=name,
        symbol=symbol,
        token_mint=mint,
        dex=dex,
        created_ts=_parse_ts(a.get("pool_created_at")),
        price_usd=_f(a.get("base_token_price_usd")),
        liquidity_usd=_f(a.get("reserve_in_usd")),
        fdv_usd=_f(a.get("fdv_usd")),
        market_cap_usd=_f(a.get("market_cap_usd")),
        vol_m5=_f(vol.get("m5")),
        vol_h1=_f(vol.get("h1")),
        vol_h6=_f(vol.get("h6")),
        vol_h24=_f(vol.get("h24")),
        chg_m5=_f(chg.get("m5")),
        chg_h1=_f(chg.get("h1")),
        chg_h6=_f(chg.get("h6")),
        buys_m5=_i(tm5.get("buys")),
        sells_m5=_i(tm5.get("sells")),
        buys_h1=_i(th1.get("buys")),
        sells_h1=_i(th1.get("sells")),
        buyers_h1=_i(th1.get("buyers")),
        sellers_h1=_i(th1.get("sellers")),
        source=source,
    )


def parse_pool_list(payload, network, source=""):
    if not payload:
        return []
    included = {t.get("id"): (t.get("attributes") or {})
                for t in payload.get("included", []) or [] if t.get("type") == "token"}
    return [parse_pool(it, network, included, source) for it in payload.get("data", []) or []]


class Gecko:
    def __init__(self, network="solana", min_interval=2.5, fetch=get_json):
        self.network = network
        self.min_interval = min_interval
        self._fetch = fetch

    def _get(self, path):
        return self._fetch(BASE + path, min_interval=self.min_interval)

    def new_pools(self, page=1):
        p = self._get(f"/networks/{self.network}/new_pools?page={page}&include=base_token")
        return parse_pool_list(p, self.network, "new")

    def trending_pools(self, page=1, duration="1h"):
        p = self._get(f"/networks/{self.network}/trending_pools?page={page}&duration={duration}&include=base_token")
        return parse_pool_list(p, self.network, "trending")

    def pools_multi(self, addresses):
        """Fetch up to 30 pools per call."""
        out = []
        for i in range(0, len(addresses), 30):
            chunk = ",".join(addresses[i:i + 30])
            p = self._get(f"/networks/{self.network}/pools/multi/{chunk}")
            out.extend(parse_pool_list(p, self.network, "track"))
        return out

    def raw(self, path):
        return self._get(path)
