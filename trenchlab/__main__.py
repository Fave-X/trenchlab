"""TrenchLab CLI.

  python -m trenchlab scan            one scan, print the table
  python -m trenchlab run             loop forever (every scan_interval_minutes), collect data
  python -m trenchlab report          lab report: funnel, outcomes, near misses, exit grid
  python -m trenchlab probe [MINT]    save raw API responses to probe/ to verify field mappings
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime

from .gecko import Gecko
from .audit import Auditor, RUGCHECK, GOPLUS
from .db import DB
from .scanner import run_cycle
from .filters import buys_per_buyer
from .lab import build_report
from .http import get_json


def load_cfg(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fmt_usd(x):
    if x is None:
        return "-"
    if x >= 1e6:
        return f"${x / 1e6:.2f}M"
    if x >= 1e3:
        return f"${x / 1e3:.0f}k"
    return f"${x:.0f}"


def print_table(rows, show_all=False, now=None):
    passed = [r for r in rows if r[6]]
    scouted = [r for r in rows if r[2] and not r[6]]
    print(f"\n{datetime.now():%Y-%m-%d %H:%M}  scanned {len(rows)} | passed scout {len(scouted) + len(passed)}"
          f" | FINAL PASS {len(passed)}")
    hdr = f"{'':2}{'symbol':<12}{'score':>6}{'liq':>8}{'1h vol':>8}{'buyers':>7}{'b/buyer':>8}{'b/s':>9}{'1h%':>7}{'age':>6}  flags / kill reasons"
    show = passed + scouted + ([r for r in rows if not r[2]] if show_all else [])
    if not show:
        print("  nothing passed scout this cycle (normal - most pools should die)")
        return
    print(hdr)
    for _, p, sp, kills, flags, sc, final in show:
        mark = "OK" if final else ("~ " if sp else "x ")
        bpb = buys_per_buyer(p)
        bs = f"{p.buys_h1}/{p.sells_h1}" if p.buys_h1 is not None else "-"
        age = p.age_hours(now)
        why = " ".join(flags) if final else ", ".join(kills[:3])
        print(f"{mark:2}{(p.symbol or '?')[:11]:<12}{(sc if sc is not None else 0):>6.0f}{fmt_usd(p.liquidity_usd):>8}"
              f"{fmt_usd(p.vol_h1):>8}{(p.buyers_h1 or 0):>7}{(bpb or 0):>8.2f}{bs:>9}"
              f"{(p.chg_h1 or 0):>6.0f}%{(age or 0):>5.1f}h  {why}")
        if final:
            print(f"   {p.gecko_url()}")
    if passed:
        print("\n  Paper signals only. Manually check holders + Bubblemaps before any real money.")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="trenchlab")
    ap.add_argument("cmd", choices=["scan", "run", "report", "probe"])
    ap.add_argument("mint", nargs="?")
    ap.add_argument("--config", default="config.json")
    ap.add_argument("--db", default="trenchlab.db")
    ap.add_argument("--all", action="store_true", help="also show killed pools in the table")
    args = ap.parse_args(argv)

    cfg = load_cfg(args.config)
    gecko = Gecko(cfg["network"], cfg.get("gecko_min_seconds_between_calls", 2.5))

    if args.cmd == "probe":
        os.makedirs("probe", exist_ok=True)
        net = cfg["network"]
        dumps = {"new_pools": f"/networks/{net}/new_pools?page=1&include=base_token",
                 "trending": f"/networks/{net}/trending_pools?page=1&duration=1h&include=base_token"}
        for name, path in dumps.items():
            data = gecko.raw(path)
            with open(f"probe/gecko_{name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"saved probe/gecko_{name}.json")
            if not args.mint and data and data.get("data"):
                rel = data["data"][0].get("relationships", {})
                args.mint = rel.get("base_token", {}).get("data", {}).get("id", "").split("_", 1)[-1]
        if args.mint:
            for name, url in (("rugcheck", RUGCHECK), ("goplus", GOPLUS)):
                try:
                    data = get_json(url.format(mint=args.mint), min_interval=1.5)
                except Exception as e:
                    data = {"error": str(e)}
                with open(f"probe/{name}_{args.mint[:8]}.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
                print(f"saved probe/{name}_{args.mint[:8]}.json")
        print("Send the probe/ folder to Claude to verify the field mappings.")
        return 0

    db = DB(args.db)
    if args.cmd == "report":
        print(build_report(db, cfg, time.time()))
        return 0

    auditor = Auditor(cfg)
    if args.cmd == "scan":
        rows, tracked = run_cycle(gecko, auditor, db, cfg)
        print_table(rows, args.all)
        print(f"  tracking {tracked} pools for outcomes")
        return 0

    # run loop
    interval = cfg.get("scan_interval_minutes", 5) * 60
    print(f"TrenchLab running every {interval // 60} min. Ctrl+C to stop. Data -> {args.db}")
    cycles = 0
    while True:
        start = time.time()
        try:
            rows, tracked = run_cycle(gecko, auditor, db, cfg)
            print_table(rows)
            print(f"  tracking {tracked} pools for outcomes")
            cycles += 1
            if cycles % 12 == 0:
                auditor._cache.clear()  # re-check audits roughly hourly
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f"[run] cycle failed, will retry: {e}")
        time.sleep(max(5, interval - (time.time() - start)))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nstopped.")
