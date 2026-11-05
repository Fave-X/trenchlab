"""CABAL FINDER (v0.2): how many real operators control a token's supply?

Uses only 1-credit standard Solana RPC calls on the Helius free plan:
  getTokenSupply, getTokenLargestAccounts, getMultipleAccounts,
  getSignaturesForAddress, getTransaction

Method (inspired by CrawlScan's operator model):
  1. Top 20 token accounts -> owner wallets. Drop AMM/pool/program accounts.
  2. For each holder wallet: how old / how active is it? (signature count, first activity)
     - "fresh" = few transactions or created very recently.
  3. For wallets with < 1000 transactions, read the FIRST transaction to find who funded it.
  4. Link holders that share a funder, or where one holder funded another.
     Funders that are themselves very busy (>= 1000 txs) are treated as exchanges/services
     and do NOT create links (otherwise everyone funded from Binance would be one "cabal").
  5. Signals: largest cluster % of supply, total clustered %, fresh-wallet %.

Limitations (be honest about them):
  - Only the top 20 holders are analysed.
  - One hop only: wallets funded by different intermediaries that share a grand-funder are missed.
  - Busy-funder heuristic can miss a cabal that funds through an exchange.
  - PDAs that hold no SOL can look like wallets; they are usually "busy" so they rarely cluster.
"""
import json
import os
import time
import urllib.error
import urllib.request

from .http import USER_AGENT

SYSTEM_PROGRAM = "11111111111111111111111111111111"
RPC_URL = "https://mainnet.helius-rpc.com/?api-key={key}"


class RpcError(Exception):
    pass


class Rpc:
    """Minimal JSON-RPC client with rate limiting, retries and credit counting."""

    def __init__(self, url, min_interval=0.13, post=None):
        self.url = url
        self.min_interval = min_interval
        self.calls = 0
        self._last = 0.0
        self._post = post or self._http_post

    def _http_post(self, payload):
        req = urllib.request.Request(
            self.url, data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())

    def call(self, method, params, retries=3):
        payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
        last = None
        for attempt in range(retries + 1):
            wait = self._last + self.min_interval - time.time()
            if wait > 0:
                time.sleep(wait)
            self._last = time.time()
            self.calls += 1
            try:
                resp = self._post(payload)
            except urllib.error.HTTPError as e:
                last = f"HTTP {e.code}"
                if e.code == 429 or e.code >= 500:
                    time.sleep(2 * (attempt + 1))
                    continue
                raise RpcError(f"{method}: {last}")
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                last = str(e)
                time.sleep(2 * (attempt + 1))
                continue
            if "error" in resp:
                err = resp["error"]
                last = f"{err.get('code')}: {err.get('message')}"
                if err.get("code") in (-32429, 429):
                    time.sleep(2 * (attempt + 1))
                    continue
                raise RpcError(f"{method}: {last}")
            return resp.get("result")
        raise RpcError(f"{method}: {last}")


def _first_funder(tx, wallet):
    """Find who sent SOL to `wallet` in its first transaction (or created it)."""
    if not tx:
        return None
    msg = (tx.get("transaction") or {}).get("message") or {}
    ixs = list(msg.get("instructions") or [])
    for inner in (tx.get("meta") or {}).get("innerInstructions") or []:
        ixs.extend(inner.get("instructions") or [])
    for ix in ixs:
        if ix.get("program") != "system":
            continue
        parsed = ix.get("parsed") or {}
        info = parsed.get("info") or {}
        t = parsed.get("type")
        if t in ("transfer", "transferWithSeed") and info.get("destination") == wallet:
            return info.get("source")
        if t in ("createAccount", "createAccountWithSeed") and info.get("newAccount") == wallet:
            return info.get("source")
    keys = msg.get("accountKeys") or []
    if keys:
        payer = keys[0].get("pubkey") if isinstance(keys[0], dict) else keys[0]
        if payer and payer != wallet:
            return payer
    return None


class _UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def analyse(rpc, mint, cfg, known_accounts=None, now=None):
    """Return dict of cluster metrics. Raises RpcError on data failure."""
    c = cfg["cluster"]
    now = now or time.time()
    known = set(known_accounts or [])

    supply = rpc.call("getTokenSupply", [mint])
    total = float(((supply or {}).get("value") or {}).get("uiAmount") or 0)
    if total <= 0:
        raise RpcError("no supply")

    largest = rpc.call("getTokenLargestAccounts", [mint, {"commitment": "confirmed"}])
    accs = (largest or {}).get("value") or []
    if not accs:
        raise RpcError("no holders")
    acc_addrs = [a["address"] for a in accs]
    amounts = {a["address"]: float(a.get("uiAmount") or 0) for a in accs}

    infos = rpc.call("getMultipleAccounts", [acc_addrs, {"encoding": "jsonParsed"}])
    holders = {}  # owner wallet -> pct of total supply
    for addr, info in zip(acc_addrs, (infos or {}).get("value") or []):
        owner = (((((info or {}).get("data") or {}).get("parsed") or {}).get("info")) or {}).get("owner")
        if not owner or owner in known or addr in known:
            continue
        holders[owner] = holders.get(owner, 0.0) + amounts[addr] / total * 100

    # drop program-owned owners (pool authorities, vaults, lockers)
    if holders:
        owners = list(holders)
        oinfo = rpc.call("getMultipleAccounts", [owners, {"encoding": "base64"}])
        for w, info in zip(owners, (oinfo or {}).get("value") or []):
            if info is not None and info.get("owner") != SYSTEM_PROGRAM:
                holders.pop(w, None)

    wallets = sorted(holders, key=lambda w: -holders[w])[: c["max_holders"]]
    analysed_pct = sum(holders[w] for w in wallets)

    fresh, funder_of, busy = {}, {}, set()
    for w in wallets:
        sigs = rpc.call("getSignaturesForAddress", [w, {"limit": 1000}]) or []
        n = len(sigs)
        if n >= 1000:
            busy.add(w)
            fresh[w] = False
            continue
        first = sigs[-1] if sigs else None
        first_t = (first or {}).get("blockTime")
        age_h = (now - first_t) / 3600 if first_t else None
        fresh[w] = n <= c["fresh_max_txs"] or (age_h is not None and age_h <= c["fresh_max_age_hours"])
        if first:
            tx = rpc.call("getTransaction", [first["signature"],
                                             {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}])
            f = _first_funder(tx, w)
            if f:
                funder_of[w] = f

    # funders that are busy services (exchanges, routers) do not link wallets together
    funder_busy = {}
    for f in set(funder_of.values()):
        if f in holders:
            funder_busy[f] = False  # a top holder funding another top holder is always a link
            continue
        s = rpc.call("getSignaturesForAddress", [f, {"limit": c["busy_funder_txs"]}]) or []
        funder_busy[f] = len(s) >= c["busy_funder_txs"]

    uf = _UF()
    for w in wallets:
        uf.find(w)
    for w, f in funder_of.items():
        if funder_busy.get(f):
            continue
        if f in holders and f in wallets:
            uf.union(w, f)
        else:
            uf.union(w, "funder:" + f)

    groups = {}
    for w in wallets:
        groups.setdefault(uf.find(w), []).append(w)
    clusters = [g for g in groups.values() if len(g) >= 2]
    cluster_pcts = sorted((sum(holders[w] for w in g) for g in clusters), reverse=True)
    fresh_pct = sum(holders[w] for w in wallets if fresh.get(w))

    return {
        "holders_analysed": len(wallets),
        "analysed_pct": round(analysed_pct, 2),
        "n_clusters": len(clusters),
        "largest_cluster_size": max((len(g) for g in clusters), default=0),
        "largest_cluster_pct": round(cluster_pcts[0], 2) if cluster_pcts else 0.0,
        "clustered_pct": round(sum(cluster_pcts), 2),
        "fresh_pct": round(fresh_pct, 2),
        "fresh_count": sum(1 for w in wallets if fresh.get(w)),
        "busy_holders": len(busy),
        "rpc_calls": rpc.calls,
    }


def verdict(metrics, cfg):
    c = cfg["cluster"]
    kills = []
    if metrics["largest_cluster_pct"] > c["max_largest_cluster_pct"]:
        kills.append(f"operator_cluster({metrics['largest_cluster_pct']:.0f}%)")
    if metrics["clustered_pct"] > c["max_clustered_pct"]:
        kills.append(f"clustered_supply({metrics['clustered_pct']:.0f}%)")
    if metrics["fresh_pct"] > c["max_fresh_pct"]:
        kills.append(f"fresh_wallets({metrics['fresh_pct']:.0f}%)")
    return kills


class CabalFinder:
    """Wraps analyse() with a per-day credit budget and per-mint caching (via the DB)."""

    def __init__(self, cfg, db, api_key=None, post=None, log=print):
        self.cfg = cfg
        self.db = db
        self.log = log
        key = api_key if api_key is not None else os.environ.get("HELIUS_API_KEY", "")
        self.enabled = bool(key) and cfg.get("cluster", {}).get("enabled", True)
        self.rpc_url = RPC_URL.format(key=key) if key else None
        self._post = post
        self.runs_this_cycle = 0

    def budget_left(self, now):
        return self.cfg["cluster"]["daily_credit_budget"] - self.db.credits_used(now)

    def check(self, mint, now, known_accounts=None, research=False):
        """Return (kills, metrics) or None if skipped. Cached results are reused."""
        if not self.enabled:
            return None
        cached = self.db.get_cluster(mint, now, self.cfg["cluster"]["cache_hours"])
        if cached is not None:
            return json.loads(cached["kills"]), json.loads(cached["metrics"])
        c = self.cfg["cluster"]
        if research and self.runs_this_cycle >= c["max_research_per_run"]:
            return None
        if self.budget_left(now) < c["est_credits_per_token"]:
            return (["unknown:cluster_budget"], {}) if not research else None
        rpc = Rpc(self.rpc_url, post=self._post)
        try:
            m = analyse(rpc, mint, self.cfg, known_accounts, now)
            kills = verdict(m, self.cfg)
        except Exception as e:  # unknown is never safe
            self.db.add_credits(now, rpc.calls)
            self.log(f"[cluster] {mint[:8]} failed: {e}")
            return ["unknown:cluster"], {"error": str(e)[:120]}
        self.db.add_credits(now, rpc.calls)
        self.db.save_cluster(mint, now, m, kills, research)
        self.runs_this_cycle += 1 if research else 0
        return kills, m
