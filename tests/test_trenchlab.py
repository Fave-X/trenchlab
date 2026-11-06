"""Stdlib unittest suite. Run: python -m unittest discover tests"""
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from trenchlab.gecko import Gecko, parse_pool_list
from trenchlab.filters import scout
from trenchlab.score import score
from trenchlab.audit import check_rugcheck, check_goplus, Auditor
from trenchlab.db import DB
from trenchlab.lab import simulate_exit, price_at, is_rugged, build_report
from trenchlab.scanner import run_cycle

ROOT = os.path.join(os.path.dirname(__file__), "..")
with open(os.path.join(ROOT, "config.json"), encoding="utf-8") as f:
    CFG = json.load(f)

NOW = datetime(2026, 11, 4, 12, 0, tzinfo=timezone.utc).timestamp()


def gecko_item(addr="POOL1", mint="MINT1", symbol="GOOD", age_h=3.0, liq=50000, vol_h1=90000,
               vol_m5=10000, buys=900, sells=600, buyers=400, chg_h1=30.0, price=0.001, mcap=400000):
    created = datetime.fromtimestamp(NOW, timezone.utc) - timedelta(hours=age_h)
    return {
        "id": f"solana_{addr}", "type": "pool",
        "attributes": {
            "address": addr, "name": f"{symbol} / SOL",
            "pool_created_at": created.isoformat().replace("+00:00", "Z"),
            "base_token_price_usd": str(price), "reserve_in_usd": str(liq),
            "fdv_usd": str(mcap), "market_cap_usd": str(mcap),
            "volume_usd": {"m5": str(vol_m5), "h1": str(vol_h1), "h6": "0", "h24": "0"},
            "price_change_percentage": {"m5": "2", "h1": str(chg_h1), "h6": "0"},
            "transactions": {"m5": {"buys": 50, "sells": 30},
                             "h1": {"buys": buys, "sells": sells, "buyers": buyers, "sellers": 300}},
        },
        "relationships": {"base_token": {"data": {"id": f"solana_{mint}", "type": "token"}},
                          "dex": {"data": {"id": "pumpswap"}}},
    }


def payload(*items):
    return {"data": list(items),
            "included": [{"id": i["relationships"]["base_token"]["data"]["id"], "type": "token",
                          "attributes": {"symbol": i["attributes"]["name"].split(" /")[0]}} for i in items]}


CLEAN_RC = {"mintAuthority": None, "freezeAuthority": None, "rugged": False,
            "markets": [{"lp": {"lpLockedPct": 100}}],
            "topHolders": [{"address": "AMM", "pct": 20}] + [{"address": f"h{i}", "pct": 1.5} for i in range(15)],
            "knownAccounts": {"AMM": {"name": "Pump AMM", "type": "AMM"}},
            "risks": [], "score_normalised": 3}
CLEAN_GP = {"code": 1, "result": {"MINT1": {"mintable": {"status": "0"}, "freezable": {"status": "0"},
                                            "closable": {"status": "0"}, "transfer_hook": []}}}


class TestParse(unittest.TestCase):
    def test_parse(self):
        pools = parse_pool_list(payload(gecko_item()), "solana")
        p = pools[0]
        self.assertEqual(p.symbol, "GOOD")
        self.assertEqual(p.token_mint, "MINT1")
        self.assertEqual(p.buyers_h1, 400)
        self.assertAlmostEqual(p.age_hours(NOW), 3.0, places=3)


class TestScout(unittest.TestCase):
    def _p(self, **kw):
        return parse_pool_list(payload(gecko_item(**kw)), "solana")[0]

    def test_good_passes(self):
        ok, kills, flags = scout(self._p(), CFG, NOW)
        self.assertTrue(ok, kills)
        self.assertIn("HEATING_UP", flags)  # 10k*12 > 90k

    def test_each_rule(self):
        cases = {
            "liquidity_low": dict(liq=20000, vol_h1=30000),
            "volume_below_liquidity": dict(vol_h1=40000),
            "sells_dominate": dict(buys=500, sells=600),
            "too_young": dict(age_h=0.5),
            "too_old": dict(age_h=20),
            "few_unique_buyers": dict(buyers=100, buys=200, sells=100),
            "wash_churn": dict(buys=2000, buyers=400),
            "overheated": dict(chg_h1=150),
        }
        for rule, kw in cases.items():
            ok, kills, _ = scout(self._p(**kw), CFG, NOW)
            self.assertFalse(ok, rule)
            self.assertIn(rule, kills, f"{rule}: {kills}")

    def test_missing_data_kills(self):
        item = gecko_item()
        del item["attributes"]["transactions"]["h1"]["buyers"]
        p = parse_pool_list(payload(item), "solana")[0]
        ok, kills, _ = scout(p, CFG, NOW)
        self.assertFalse(ok)
        self.assertIn("missing:buyers_h1", kills)


class TestScore(unittest.TestCase):
    def test_range_and_order(self):
        good = parse_pool_list(payload(gecko_item()), "solana")[0]
        weak = parse_pool_list(payload(gecko_item(buyers=160, buys=330, sells=320, vol_m5=1000,
                                                  vol_h1=31000, liq=30000, chg_h1=78)), "solana")[0]
        sg, _ = score(good)
        sw, _ = score(weak)
        self.assertTrue(0 <= sw < sg <= 100, (sw, sg))
        self.assertGreaterEqual(sg, CFG["score"]["pass_threshold"])


class TestAudit(unittest.TestCase):
    def test_clean(self):
        kills, notes = check_rugcheck(CLEAN_RC, CFG)
        self.assertEqual(kills, [], notes)
        k2, _ = check_goplus(CLEAN_GP, "MINT1", CFG)
        self.assertEqual(k2, [])

    def test_amm_excluded_from_top10(self):
        _, notes = check_rugcheck(CLEAN_RC, CFG)
        self.assertIn("top10=15.0%", notes)

    def test_bad(self):
        bad = dict(CLEAN_RC, mintAuthority="X", markets=[{"lp": {"lpLockedPct": 10}}],
                   risks=[{"name": "Single holder ownership", "level": "danger"}])
        kills, _ = check_rugcheck(bad, CFG)
        self.assertIn("mint_authority_active", kills)
        self.assertTrue(any(k.startswith("lp_not_locked") for k in kills))
        self.assertTrue(any(k.startswith("rc_danger") for k in kills))

    def test_unknown_is_kill(self):
        kills, _ = check_rugcheck(None, CFG)
        self.assertEqual(kills, ["unknown:rugcheck_no_report"])
        kills, _ = check_rugcheck({"markets": []}, CFG)
        self.assertIn("unknown:mint_authority", kills)
        self.assertIn("unknown:lp_lock", kills)
        self.assertIn("unknown:top_holders", kills)

    def test_concentration(self):
        conc = dict(CLEAN_RC, topHolders=[{"address": f"w{i}", "pct": 5} for i in range(10)])
        kills, _ = check_rugcheck(conc, CFG)
        self.assertTrue(any(k.startswith("top10_concentrated") for k in kills))

    def test_goplus_flags(self):
        gp = {"result": {"MINT1": {"mintable": {"status": "1"}, "freezable": {"status": "0"}}}}
        kills, _ = check_goplus(gp, "MINT1", CFG)
        self.assertEqual(kills, ["gp_mintable"])


class TestLab(unittest.TestCase):
    def S(self, pts):
        return [{"ts": NOW + t, "price_usd": p, "liquidity_usd": 50000} for t, p in pts]

    def test_stop_with_gap(self):
        s = self.S([(300, 0.98), (600, 0.80)])  # gaps through -6% stop
        r, why = simulate_exit(s, NOW, 1.0, -6, 20, 10, 0.0)
        self.assertEqual(why, "stop")
        self.assertAlmostEqual(r, -0.20)

    def test_trail(self):
        s = self.S([(300, 1.1), (600, 1.5), (900, 1.3)])
        r, why = simulate_exit(s, NOW, 1.0, -10, 20, 10, 0.0)
        self.assertEqual(why, "trail")
        self.assertAlmostEqual(r, 0.30)

    def test_costs(self):
        s = self.S([(300, 1.0)])
        r, why = simulate_exit(s, NOW, 1.0, -10, 20, 10, 4.0)
        self.assertEqual(why, "time")
        self.assertAlmostEqual(r, 0.98 / 1.02 - 1)

    def test_price_at_and_rug(self):
        s = self.S([(900, 1.2), (3600, 0.05)])
        self.assertEqual(price_at(s, NOW, 900), 1.2)
        self.assertIsNone(price_at(s, NOW, 86400))
        self.assertTrue(is_rugged(s, NOW, 1.0, 50000, CFG))


class FakeFetch:
    """Simulates GeckoTerminal + RugCheck + GoPlus responses over time."""

    def __init__(self):
        self.t = NOW
        self.price = 0.001

    def __call__(self, url, min_interval=0, **kw):
        if "rugcheck" in url:
            return CLEAN_RC
        if "gopluslabs" in url:
            return CLEAN_GP
        if "new_pools" in url:
            if "page=1" not in url:
                return {"data": []}
            return payload(gecko_item(), gecko_item(addr="POOL2", mint="MINT2", symbol="RUGGY",
                                                    buys=3000, buyers=200, sells=100))
        if "trending" in url:
            return {"data": []}
        if "dexscreener" in url:
            addrs = url.rsplit("/", 1)[1].split(",")
            if getattr(self, "dex_down", False):
                raise __import__("trenchlab.http", fromlist=["HttpError"]).HttpError("HTTP 429")
            return {"pairs": [{"pairAddress": a, "priceUsd": str(self.price), "liquidity": {"usd": 50000},
                               "baseToken": {"address": "M" + a if a not in ("POOL1", "POOL2") else
                                             {"POOL1": "MINT1", "POOL2": "MINT2"}[a]}}
                              for a in addrs]}
        if "/multi/" in url:
            addrs = url.rsplit("/", 1)[1].split(",")
            return payload(*[gecko_item(addr=a, mint="M" + a, price=self.price) for a in addrs])
        raise AssertionError(url)


class TestEndToEnd(unittest.TestCase):
    def test_cycles_and_report(self):
        with tempfile.TemporaryDirectory() as d:
            db = DB(os.path.join(d, "t.db"))
            fetch = FakeFetch()
            gecko = Gecko("solana", 0, fetch=fetch)
            auditor = Auditor(CFG, fetch=fetch)
            rows, _ = run_cycle(gecko, auditor, db, CFG, now=NOW, log=lambda *a: None, alert=False,
                                dex_fetch=fetch)
            finals = [r for r in rows if r[6]]
            self.assertEqual([r[1].symbol for r in finals], ["GOOD"])
            killed = [r for r in rows if not r[2]]
            self.assertIn("wash_churn", killed[0][3])

            # later cycles: pools come from tracking via /multi as well as new_pools
            for i, px in enumerate([0.0011, 0.0013, 0.0015, 0.0012], start=1):
                fetch.price = px
                fetch.dex_down = (i == 2)  # one cycle with DexScreener down -> Gecko fallback
                run_cycle(gecko, auditor, db, CFG, now=NOW + i * 3600, log=lambda *a: None, alert=False,
                          dex_fetch=fetch)
            self.assertGreater(len(db.samples_for("POOL1")), 1)
            rep = build_report(db, CFG, NOW + 5 * 3600)
            self.assertIn("FINAL PASS", rep)
            self.assertIn("EXIT GRID", rep)
            self.assertIn("NEAR MISSES", rep)
            self.assertIn("wash_churn", rep)


if __name__ == "__main__":
    unittest.main()


class TestDexScreener(unittest.TestCase):
    def test_parse(self):
        from trenchlab.dexscreener import prices_multi
        calls = []

        def fetch(url, min_interval=0):
            calls.append(url)
            return {"pairs": [{"pairAddress": "A", "priceUsd": "0.5", "liquidity": {"usd": 1234}},
                              {"pairAddress": "B", "priceUsd": None}]}
        out = prices_multi([f"P{i}" for i in range(31)], fetch=fetch)
        self.assertEqual(len(calls), 2)                      # chunks of 30
        self.assertEqual(out["A"], (0.5, 1234.0))
        self.assertNotIn("B", out)                           # no price -> dropped

    def test_rejects_bad_rows(self):
        from trenchlab.dexscreener import prices_multi

        def fetch(url, min_interval=0):
            return {"pairs": [
                {"pairAddress": "ZERO", "priceUsd": "1", "liquidity": {"usd": 0}, "baseToken": {"address": "MZ"}},
                {"pairAddress": "FLIP", "priceUsd": "150", "liquidity": {"usd": 9e4}, "baseToken": {"address": "SOL"}},
                {"pairAddress": "OK", "priceUsd": "0.01", "liquidity": {"usd": 9e4}, "baseToken": {"address": "MOK"}}]}
        out = prices_multi(["ZERO", "FLIP", "OK"], fetch=fetch,
                           expected_base={"ZERO": "MZ", "FLIP": "MFLIP", "OK": "MOK"})
        self.assertEqual(list(out), ["OK"])

    def test_insane_sample_rejected_and_cleanup(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "t.db")
            db = DB(path)
            p = parse_pool_list(payload(gecko_item(liq=50000, price=0.001)), "solana")[0]
            T = DB.DEX_SWITCH_TS + 100
            db.upsert_first_seen(p, T, [], T + 86400)
            self.assertFalse(db.sample_is_sane(p.address, 0.002, 0))        # liq gone, price up: impossible
            self.assertTrue(db.sample_is_sane(p.address, 0.00001, 0))       # liq gone, price crashed: real rug
            self.assertFalse(db.sample_is_sane(p.address, 9.0, 60000))      # 9000x, liq flat: flipped pair
            self.assertTrue(db.sample_is_sane(p.address, 0.005, 120000))    # 5x with liq 2.4x: plausible
            db.add_sample(p.address, T + 600, 0.002, 0)                     # bad, after switch -> removed
            db.add_sample(p.address, T + 1200, 9.0, 60000)                  # bad, after switch -> removed
            db.add_sample(p.address, T + 1800, 0.00001, 5)                  # real rug -> kept
            db.add_sample(p.address, DB.DEX_SWITCH_TS - 600, 0.002, 0)      # before switch (Gecko) -> kept
            db.conn.execute("DELETE FROM meta"); db.commit()
            db2 = DB(path)                                                  # migration runs on open
            prices = sorted(r["price_usd"] for r in db2.samples_for(p.address))
            self.assertEqual(prices, [0.00001, 0.002])
