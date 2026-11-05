"""AUDITOR: token security checks. Rule: unknown is never treated as safe.

Field names for RugCheck / GoPlus are parsed defensively. Run `python -m trenchlab probe <mint>`
on first setup to save the raw responses and confirm the mapping.
"""
from .http import get_json, HttpError

RUGCHECK = "https://api.rugcheck.xyz/v1/tokens/{mint}/report"
GOPLUS = "https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses={mint}"


def _get(d, *path):
    for p in path:
        if not isinstance(d, dict):
            return None
        d = d.get(p)
    return d


def check_rugcheck(report, cfg):
    """Return (kills, notes) from a RugCheck full report dict."""
    a = cfg["audit"]
    kills, notes = [], []
    if not report:
        return ["unknown:rugcheck_no_report"], notes

    if report.get("rugged") is True:
        kills.append("rugcheck_rugged")

    token = report.get("token") if isinstance(report.get("token"), dict) else {}
    for key, label in (("mintAuthority", "mint_authority"), ("freezeAuthority", "freeze_authority")):
        if key in report:
            val = report[key]
        elif key in token:
            val = token[key]
        else:
            kills.append(f"unknown:{label}")
            continue
        if val:
            kills.append(f"{label}_active")

    markets = report.get("markets")
    if not markets:
        kills.append("unknown:lp_lock")
    else:
        locked = [m.get("lp", {}).get("lpLockedPct") for m in markets if isinstance(m, dict)]
        locked = [x for x in locked if isinstance(x, (int, float))]
        if not locked:
            kills.append("unknown:lp_lock")
        elif max(locked) < a["min_lp_locked_pct"]:
            kills.append(f"lp_not_locked({max(locked):.0f}%)")

    holders = report.get("topHolders")
    known = report.get("knownAccounts") or {}
    if not isinstance(holders, list):
        kills.append("unknown:top_holders")
    else:
        real = [h for h in holders if isinstance(h, dict)
                and h.get("address") not in known and h.get("owner") not in known]
        top10 = sum(float(h.get("pct") or 0) for h in real[:10])
        notes.append(f"top10={top10:.1f}%")
        if top10 > a["max_top10_pct"]:
            kills.append(f"top10_concentrated({top10:.0f}%)")
        insiders = sum(1 for h in real[:20] if h.get("insider"))
        if insiders:
            notes.append(f"insiders_in_top20={insiders}")

    if a.get("kill_on_rugcheck_danger"):
        for r in report.get("risks") or []:
            if isinstance(r, dict) and str(r.get("level", "")).lower() == "danger":
                kills.append("rc_danger:" + str(r.get("name", "?"))[:40])
    gi = report.get("graphInsidersDetected")
    if gi:
        notes.append(f"graph_insiders={gi}")
    if report.get("score_normalised") is not None:
        notes.append(f"rc_score={report.get('score_normalised')}")
    return kills, notes


def check_goplus(payload, mint, cfg):
    kills, notes = [], []
    res = _get(payload, "result")
    tok = None
    if isinstance(res, dict):
        tok = res.get(mint) or (next(iter(res.values())) if len(res) == 1 else None)
    if not isinstance(tok, dict):
        if cfg["audit"].get("require_goplus"):
            kills.append("unknown:goplus")
        else:
            notes.append("goplus=unknown")
        return kills, notes
    for key, label in (("mintable", "gp_mintable"), ("freezable", "gp_freezable"),
                       ("closable", "gp_closable"),
                       ("balance_mutable_authority", "gp_balance_mutable")):
        st = _get(tok, key, "status")
        if str(st) == "1":
            kills.append(label)
    hooks = tok.get("transfer_hook")
    if isinstance(hooks, list) and hooks:
        kills.append("gp_transfer_hook")
    return kills, notes


class Auditor:
    def __init__(self, cfg, fetch=get_json):
        self.cfg = cfg
        self._fetch = fetch
        self._cache = {}
        self.known_accounts = {}  # mint -> set of AMM/pool/known addresses from RugCheck

    def audit(self, mint):
        """Return (passed, kills, notes). Cached per mint for the session."""
        if mint in self._cache:
            return self._cache[mint]
        a = self.cfg["audit"]
        kills, notes = [], []
        if a.get("use_rugcheck", True):
            try:
                rep = self._fetch(RUGCHECK.format(mint=mint), min_interval=1.5)
            except HttpError as e:
                rep = None
                notes.append(f"rugcheck_error:{e}"[:80])
            if isinstance(rep, dict):
                self.known_accounts[mint] = set((rep.get("knownAccounts") or {}).keys())
            k, n = check_rugcheck(rep, self.cfg)
            kills += k
            notes += n
        if a.get("use_goplus", True):
            try:
                gp = self._fetch(GOPLUS.format(mint=mint), min_interval=1.5)
            except HttpError as e:
                gp = None
                notes.append(f"goplus_error:{e}"[:80])
            k, n = check_goplus(gp, mint, self.cfg)
            kills += k
            notes += n
        out = (len(kills) == 0, kills, notes)
        self._cache[mint] = out
        return out
