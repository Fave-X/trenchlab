"""Paper trader tests: sizing, risk limits, exits, dead pools, Jupiter parsing, reconciliation."""
import copy
import json
import os
import sys
import tempfile
import unittest
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from trenchlab.db import DB
from trenchlab.gecko import parse_pool_list
from trenchlab.paper import PaperTrader, ModelQuoter, JupiterQuoter, paper_report, SOL_MINT, USDC_MINT
from test_trenchlab import gecko_item, payload, CFG, NOW


def pool(addr="P1", mint="M1", price=0.001, liq=50000):
    return parse_pool_list(payload(gecko_item(addr=addr, mint=mint, symbol=addr, price=price, liq=liq)), "solana")[0]


class Env:
    def __init__(self, cfg=None):
        self.dir = tempfile.TemporaryDirectory()
        self.db = DB(os.path.join(self.dir.name, "t.db"))
        self.cfg = cfg or copy.deepcopy(CFG)
        self.log = []
        self.trader = PaperTrader(self.cfg, self.db, quoter=ModelQuoter(self.cfg), log=self.log.append)

    def seen(self, p, ts):
        self.db.upsert_first_seen(p, ts, [], ts + 86400)

    def price(self, p, ts, price, liq=50000):
        self.db.add_sample(p.address, ts, price, liq)


class TestModelQuoter(unittest.TestCase):
    def test_roundtrip_cost(self):
        q = ModelQuoter(CFG)
        state = {"price": 0.001, "liq": 50000}
        tokens, info = q.buy(state, 25.0)
        self.assertAlmostEqual(info["impact_pct"], 0.1, places=3)        # 25 / (50000/2)
        value, _ = q.sell_value(state, tokens)
        rt = value / 25 - 1
        self.assertTrue(-0.03 < rt < -0.02, rt)                          # ~2x1% fee + impact + net fees

    def test_thin_pool_costs_more(self):
        q = ModelQuoter(CFG)
        _, deep = q.buy({"price": 1, "liq": 100000}, 50)
        _, thin = q.buy({"price": 1, "liq": 10000}, 50)
        self.assertGreater(thin["impact_pct"], deep["impact_pct"] * 5)


class TestSizingAndLimits(unittest.TestCase):
    def test_size_is_risk_based(self):
        e = Env()
        p = pool()
        e.seen(p, NOW)
        pid = e.trader.on_signal(p, 75, NOW)
        pos = e.db.open_positions()[0]
        self.assertEqual(pos["id"], pid)
        self.assertAlmostEqual(pos["cost_usd"], 25.0)                    # 0.5% risk / 10% stop = 5% of $500
        self.assertAlmostEqual(e.db.paper_cash(), 475.0)

    def test_limits(self):
        e = Env()
        for i in range(3):
            p = pool(f"P{i}", f"M{i}")
            e.seen(p, NOW)
            e.trader.on_signal(p, 75, NOW)
        self.assertEqual(len(e.db.open_positions()), 2)                  # max 2 open
        self.assertIn(("max_open_positions", 1), e.db.paper_skip_counts())
        p0 = pool("P0", "M0")
        self.assertIsNone(e.trader.on_signal(p0, 90, NOW))               # one entry per token
        self.assertIn("already_traded_token", [r for r, _ in e.db.paper_skip_counts()])

    def test_high_impact_skipped(self):
        e = Env()
        p = pool(liq=1000)                                               # $25 into $1k pool = 5% impact
        e.seen(p, NOW)
        self.assertIsNone(e.trader.on_signal(p, 75, NOW))
        self.assertTrue(any(r.startswith("impact_too_high") for r, _ in e.db.paper_skip_counts()))


class TestExits(unittest.TestCase):
    def open_one(self, e, p, ts=NOW):
        e.seen(p, ts)
        e.price(p, ts, p.price_usd)
        e.trader.on_signal(p, 75, ts)
        return e.db.open_positions()[0]

    def test_stop_then_cooldown_and_reconcile(self):
        e = Env()
        p = self.open_one(e, pool())
        e.price(pool(), NOW + 600, 0.00085)                              # -15%
        e.trader.manage(NOW + 600)
        closed = e.db.closed_positions()
        self.assertEqual(closed[0]["exit_reason"], "stop")
        self.assertLess(closed[0]["exit_value"], 25 * 0.9)               # gap + costs: worse than -10%
        q = pool("Q", "MQ")
        e.seen(q, NOW + 700)
        self.assertIsNone(e.trader.on_signal(q, 80, NOW + 700))          # cooldown after a loss
        rep = paper_report(e.db, e.cfg)
        self.assertIn("ledger reconciles: YES", rep)

    def test_trailing(self):
        e = Env()
        p = pool()
        self.open_one(e, p)
        e.price(p, NOW + 600, 0.0014)                                    # +40%: trail armed
        e.trader.manage(NOW + 600)
        self.assertEqual(len(e.db.open_positions()), 1)
        e.price(p, NOW + 1200, 0.00122)                                  # -13% from peak
        e.trader.manage(NOW + 1200)
        c = e.db.closed_positions()[0]
        self.assertEqual(c["exit_reason"], "trail")
        self.assertGreater(c["exit_value"], 25 * 1.15)

    def test_time_stop(self):
        e = Env()
        p = pool()
        self.open_one(e, p)
        e.price(p, NOW + 86400 + 60, 0.00102)
        e.trader.manage(NOW + 86400 + 60)
        self.assertEqual(e.db.closed_positions()[0]["exit_reason"], "time")

    def test_dead_pool(self):
        e = Env()
        self.open_one(e, pool())
        for i in range(1, 7):                                            # no fresh prices for 6 cycles
            e.trader.manage(NOW + 3600 + i * 600)
        c = e.db.closed_positions()[0]
        self.assertEqual((c["exit_reason"], c["exit_value"]), ("dead_no_route", 0.0))

    def test_daily_loss_limit(self):
        cfg = copy.deepcopy(CFG)
        cfg["paper"]["cooldown_after_loss_min"] = 0
        cfg["paper"]["daily_loss_limit_pct"] = 3                         # $15 on $500
        e = Env(cfg)
        p = pool()
        self.open_one(e, p)
        e.price(p, NOW + 600, 0.0001)                                    # -90%: lose ~$22
        e.trader.manage(NOW + 600)
        q = pool("Q", "MQ")
        e.seen(q, NOW + 700)
        self.assertIsNone(e.trader.on_signal(q, 80, NOW + 700))
        self.assertIn("daily_loss_limit", [r for r, _ in e.db.paper_skip_counts()])


class TestJupiter(unittest.TestCase):
    def test_quotes(self):
        calls = []

        def fetch(url, min_interval=0, headers=None):
            calls.append((url, headers))
            q = {k: v[0] for k, v in parse_qs(urlparse(url).query).items()}
            if q["inputMint"] == SOL_MINT and q["outputMint"] == USDC_MINT:
                return {"outAmount": str(150 * 10**6)}                   # 1 SOL = $150
            if q["inputMint"] == SOL_MINT:
                return {"outAmount": "1000000", "otherAmountThreshold": "970000", "priceImpactPct": "0.004"}
            if q["outputMint"] == SOL_MINT:
                return {"outAmount": "160000000", "otherAmountThreshold": "155000000", "priceImpactPct": "0.01"}
            raise AssertionError(url)

        jq = JupiterQuoter(CFG, "KEY", fetch=fetch)
        raw, info = jq.buy({}, 25.0, "MINTX")
        self.assertEqual(raw, 970000)                                    # worst case within slippage
        self.assertAlmostEqual(info["impact_pct"], 0.4)
        self.assertEqual(calls[-1][1], {"x-api-key": "KEY"})
        self.assertIn("api.jup.ag/swap/v1/quote", calls[-1][0])
        val, _ = jq.sell_value({}, 970000, "MINTX")
        self.assertAlmostEqual(val, 0.155 * 150 - CFG["paper"]["network_fee_usd"])

    def test_no_route(self):
        def fetch(url, min_interval=0, headers=None):
            if "outputMint=" + USDC_MINT in url:
                return {"outAmount": str(150 * 10**6)}
            return {"error": "Could not find any route", "errorCode": "COULD_NOT_FIND_ANY_ROUTE"}
        jq = JupiterQuoter(CFG, "KEY", fetch=fetch)
        raw, info = jq.buy({}, 25.0, "MINTX")
        self.assertIsNone(raw)
        self.assertIn("route", info["error"])


class TestCycleWithTrader(unittest.TestCase):
    def test_signal_to_trade(self):
        from test_trenchlab import FakeFetch
        from trenchlab.gecko import Gecko
        from trenchlab.audit import Auditor
        from trenchlab.scanner import run_cycle
        from trenchlab.lab import build_report
        e = Env()
        fetch = FakeFetch()
        g, a = Gecko("solana", 0, fetch=fetch), Auditor(CFG, fetch=fetch)
        run_cycle(g, a, e.db, CFG, now=NOW, log=lambda *x: None, alert=False, dex_fetch=fetch, trader=e.trader)
        self.assertEqual([p["symbol"] for p in e.db.open_positions()], ["GOOD"])
        for i, px in enumerate([0.00095, 0.00080], start=1):
            fetch.price = px
            run_cycle(g, a, e.db, CFG, now=NOW + i * 600, log=lambda *x: None, alert=False,
                      dex_fetch=fetch, trader=e.trader)
        self.assertEqual(e.db.closed_positions()[0]["exit_reason"], "stop")
        rep = build_report(e.db, CFG, NOW + 1800)
        self.assertIn("PAPER BOOK A", rep)
        self.assertIn("ledger reconciles: YES", rep)


if __name__ == "__main__":
    unittest.main()


class TestNoSameCycleExit(unittest.TestCase):
    def test_entry_not_stopped_in_same_cycle(self):
        e = Env()
        p = pool()
        e.seen(p, NOW)
        e.price(p, NOW, 0.00080)            # stale/other-source sample 20% below the entry quote
        e.trader.on_signal(p, 75, NOW)
        e.trader.manage(NOW)
        self.assertEqual(len(e.db.open_positions()), 1)
        e.price(p, NOW + 600, 0.00080)
        e.trader.manage(NOW + 600)
        self.assertEqual(e.db.closed_positions()[0]["exit_reason"], "stop")
