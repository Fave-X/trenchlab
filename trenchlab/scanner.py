"""One scan cycle: SCOUT -> ANALYST score -> AUDITOR -> CABAL FINDER -> log everything -> sample prices."""
import time

from .filters import scout, buys_per_buyer
from .score import score as score_pool
from .notify import telegram
from . import dexscreener
from . import pullback


def fetch_candidates(gecko, cfg, log=print):
    seen = {}
    for page in range(1, cfg.get("gecko_new_pools_pages", 3) + 1):
        try:
            for p in gecko.new_pools(page):
                seen.setdefault(p.address, p)
        except Exception as e:
            log(f"[scout] new_pools page {page} failed: {e}")
    for page in range(1, cfg.get("gecko_trending_pages", 2) + 1):
        try:
            for p in gecko.trending_pools(page):
                seen[p.address] = p  # trending data is at least as fresh
        except Exception as e:
            log(f"[scout] trending page {page} failed: {e}")
    ignore = {s.upper() for s in cfg.get("ignore_base_symbols", [])}
    return [p for p in seen.values() if (p.symbol or "").upper() not in ignore]


def run_cycle(gecko, auditor, db, cfg, now=None, log=print, alert=True, cabal=None, dex_fetch=None,
              trader=None, trader_b=None):
    now = now if now is not None else time.time()
    if dex_fetch is None:
        from .http import get_json as dex_fetch
    lab = cfg["lab"]
    track_s = lab["track_hours"] * 3600
    threshold = cfg["score"]["pass_threshold"]

    pools = fetch_candidates(gecko, cfg, log)
    results = []
    research = []  # near-miss pools to run the cabal finder on for measurement only
    if cabal is not None:
        cabal.runs_this_cycle = 0
    for p in pools:
        passed, kills, flags = scout(p, cfg, now)
        sc, parts, final, audit = None, {}, False, None
        if passed:
            sc, parts = score_pool(p)
            if sc < threshold:
                kills = kills + [f"score_below({sc})"]
            elif cfg["audit"].get("enabled", True) and auditor is not None:
                audit = auditor.audit(p.token_mint)  # (ok, kills, notes)
                kills = kills + audit[1]
                final = audit[0]
            else:
                final = True
            if final and cabal is not None and cabal.enabled:
                known = auditor.known_accounts.get(p.token_mint) if auditor is not None else None
                res = cabal.check(p.token_mint, now, known)
                if res is not None:
                    kills = kills + res[0]
                    final = not res[0]
            elif cabal is not None:
                research.append(p)
        elif (cabal is not None and len(kills) == 1
              and kills[0] in cfg["cluster"]["research_single_kill_rules"]
              and (p.liquidity_usd or 0) >= cfg["cluster"]["research_min_liquidity_usd"]):
            research.append(p)

        trackable = (p.liquidity_usd or 0) >= lab["min_liquidity_to_track_usd"]
        db.upsert_first_seen(p, now, kills, now + track_s if trackable else now)
        if audit is not None:
            db.set_audit(p.address, *audit)
        if final:
            db.mark_first_pass(p.address, now, p.price_usd, sc)
            db.extend_tracking(p.address, now + track_s)
            if trader is not None:
                trader.on_signal(p, sc, now)
        # log an observation when the pool is new, when its decision changes, or while it passes scout
        prev = db.last_obs_state(p.address)
        if prev is None or passed or prev != (int(passed), int(final)):
            db.add_observation(now, p, passed, kills, flags, sc, parts, final,
                               keep_metrics=trackable or passed or final)
        if (trackable or final or db.has_open_position(p.address)) and db.sample_due(p.address, now):
            db.add_sample(p.address, now, p.price_usd, p.liquidity_usd)
        results.append(("pool", p, passed, kills, flags, sc, final))

        if final and alert and not db.was_alerted(p.address):
            bpb = buys_per_buyer(p)
            msg = (f"TRENCHLAB PASS (paper)\n${p.symbol}  score {sc}\n"
                   f"liq ${p.liquidity_usd:,.0f} | 1h vol ${p.vol_h1:,.0f}\n"
                   f"buyers 1h {p.buyers_h1} | buys/buyer {bpb:.2f}\n"
                   f"1h {p.chg_h1:+.0f}% | {' '.join(flags)}\n{p.gecko_url()}\n"
                   "Verify holders + Bubblemaps yourself. NFA.")
            telegram(msg)
            db.mark_alerted(p.address, now)
    db.commit()

    # research: cabal-check a few near misses so the lab can test the signal on non-passers too
    if cabal is not None and cabal.enabled:
        research.sort(key=lambda q: -(q.liquidity_usd or 0))
        for q in research:
            if cabal.runs_this_cycle >= cfg["cluster"]["max_research_per_run"]:
                break
            known = auditor.known_accounts.get(q.token_mint) if auditor is not None else None
            if known is None and auditor is not None and cfg["audit"].get("use_rugcheck", True):
                auditor.audit(q.token_mint)  # fetch RugCheck once to learn AMM/pool accounts
                known = auditor.known_accounts.get(q.token_mint)
            cabal.check(q.token_mint, now, known, research=True)
        db.commit()

    # sample prices for everything still being tracked that we didn't just see
    seen_now = {p.address for p in pools}
    to_track = [a for a in db.tracked_addresses(now) if a not in seen_now and db.sample_due(a, now)]
    if to_track:
        got = {}
        try:  # DexScreener first: much higher rate limit than GeckoTerminal
            got = dexscreener.prices_multi(to_track, cfg["network"], fetch=dex_fetch,
                                           expected_base=db.mints_for(to_track))
        except Exception as e:
            log(f"[lab] dexscreener tracking failed: {e}")
        got = {a: v for a, v in got.items() if db.sample_is_sane(a, *v)}  # bad DexScreener rows -> Gecko
        missing = [a for a in to_track if a not in got]
        cap = cfg["lab"].get("max_gecko_fallback_pools", 240)
        if len(missing) > cap:
            # GeckoTerminal rate-limits shared GitHub IPs; retries can push a run past its time limit.
            # Price what matters most: open paper positions first, then the biggest pools (book B's universe).
            held = {pos["pool_address"] for pos in db.open_positions()}
            liq = {a: (db.get_pool(a)["first_liq"] or 0) if db.get_pool(a) else 0 for a in missing}
            missing.sort(key=lambda a: (a not in held, -liq[a]))
            log(f"[lab] gecko fallback capped: {cap} of {len(missing)} pools")
            missing = missing[:cap]
        if missing:
            try:
                for tp in gecko.pools_multi(missing):
                    got[tp.address] = (tp.price_usd, tp.liquidity_usd)
            except Exception as e:
                log(f"[lab] gecko tracking fallback failed for {len(missing)} pools: {e}")
        for addr, (px, liq) in got.items():
            db.add_sample(addr, now, px, liq)
        db.commit()
    for pos in db.open_positions():
        db.extend_tracking(pos["pool_address"], now + 3600)
    if trader is not None:
        trader.manage(now)
    if trader_b is not None:
        if cabal is not None:
            cabal.runs_this_cycle = 0
        try:
            n = pullback.run(db, gecko, auditor, cabal, trader_b, cfg, now, log)
            if n:
                log(f"[B] {n} pullback entr{'y' if n == 1 else 'ies'}")
        except Exception as e:  # book B must never break the main scan
            log(f"[B] pullback scan failed: {e}")
        trader_b.manage(now)
    return [r for r in results if r[0] == "pool"], len(to_track)
