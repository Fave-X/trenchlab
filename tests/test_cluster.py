"""Cabal finder tests with a fake Solana RPC."""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from trenchlab.cluster import Rpc, analyse, verdict, CabalFinder, _first_funder, SYSTEM_PROGRAM
from trenchlab.db import DB

ROOT = os.path.join(os.path.dirname(__file__), "..")
with open(os.path.join(ROOT, "config.json"), encoding="utf-8") as f:
    CFG = json.load(f)
NOW = 1_800_000_000


def sys_transfer(src, dst):
    return {"program": "system", "parsed": {"type": "transfer", "info": {"source": src, "destination": dst}}}


class FakeChain:
    """Token MINT with supply 1000.
    AMMVAULT (owned by AMM, known) 400; POOLPDA (program-owned) 100;
    cabal: C1,C2,C3 hold 60 each, all funded by FUNDERX (quiet wallet) -> one cluster of 18%
    C4 holds 30, funded by C1 (a top holder) -> joins the cabal -> 21%
    retail: R1..R5 hold 20 each, funded by BINANCE (busy) -> no links
    OLD holds 50, has 1000+ txs (busy, not fresh, not traced)"""

    def __init__(self):
        self.holdings = {"AMMVAULT_ACC": ("AMM", 400), "POOL_ACC": ("POOLPDA", 100),
                         "C1_ACC": ("C1", 60), "C2_ACC": ("C2", 60), "C3_ACC": ("C3", 60),
                         "C4_ACC": ("C4", 30), "OLD_ACC": ("OLD", 50)}
        for i in range(1, 6):
            self.holdings[f"R{i}_ACC"] = (f"R{i}", 20)
        self.funder = {"C1": "FUNDERX", "C2": "FUNDERX", "C3": "FUNDERX", "C4": "C1"}
        for i in range(1, 6):
            self.funder[f"R{i}"] = "BINANCE"
        self.calls = []

    def __call__(self, payload):
        m, params = payload["method"], payload["params"]
        self.calls.append(m)
        if m == "getTokenSupply":
            return {"result": {"value": {"uiAmount": 1000}}}
        if m == "getTokenLargestAccounts":
            vals = sorted(self.holdings.items(), key=lambda kv: -kv[1][1])
            return {"result": {"value": [{"address": a, "uiAmount": amt} for a, (_, amt) in vals]}}
        if m == "getMultipleAccounts":
            addrs, opts = params
            if opts["encoding"] == "jsonParsed":
                return {"result": {"value": [
                    {"data": {"parsed": {"info": {"owner": self.holdings[a][0]}}}} for a in addrs]}}
            return {"result": {"value": [
                {"owner": "SomeAmmProgram"} if a == "POOLPDA" else {"owner": SYSTEM_PROGRAM} for a in addrs]}}
        if m == "getSignaturesForAddress":
            w, opts = params
            if w in ("OLD", "BINANCE"):
                return {"result": [{"signature": f"s{i}", "blockTime": NOW - 10**7} for i in range(opts["limit"])]}
            if w == "FUNDERX":
                return {"result": [{"signature": "f1", "blockTime": NOW - 3600}]}
            n = 3 if w.startswith("C") else 50
            age = 3600 * 5 if w.startswith("C") else 86400 * 200
            return {"result": [{"signature": f"{w}_sig{i}", "blockTime": NOW - age + i} for i in range(n, 0, -1)]}
        if m == "getTransaction":
            sig = params[0]
            w = sig.split("_sig")[0]
            src = self.funder[w]
            return {"result": {"transaction": {"message": {
                "accountKeys": [{"pubkey": src}, {"pubkey": w}],
                "instructions": [sys_transfer(src, w)]}}, "meta": {"innerInstructions": []}}}
        raise AssertionError(m)


class TestFirstFunder(unittest.TestCase):
    def test_transfer_and_inner(self):
        tx = {"transaction": {"message": {"accountKeys": [{"pubkey": "PAYER"}], "instructions": []}},
              "meta": {"innerInstructions": [{"instructions": [sys_transfer("SRC", "W")]}]}}
        self.assertEqual(_first_funder(tx, "W"), "SRC")

    def test_fallback_fee_payer(self):
        tx = {"transaction": {"message": {"accountKeys": [{"pubkey": "PAYER"}], "instructions": []}}}
        self.assertEqual(_first_funder(tx, "W"), "PAYER")
        self.assertIsNone(_first_funder(None, "W"))


class TestAnalyse(unittest.TestCase):
    def test_cabal_detected(self):
        chain = FakeChain()
        rpc = Rpc("x", min_interval=0, post=chain)
        m = analyse(rpc, "MINT", CFG, known_accounts={"AMM"}, now=NOW)
        # AMM excluded (known), POOLPDA excluded (program-owned)
        self.assertEqual(m["holders_analysed"], 10)
        self.assertEqual(m["n_clusters"], 1)
        self.assertEqual(m["largest_cluster_size"], 4)       # C1,C2,C3 + C4 (funded by C1)
        self.assertAlmostEqual(m["largest_cluster_pct"], 21.0)  # 60+60+60+30 of 1000
        self.assertAlmostEqual(m["fresh_pct"], 21.0)          # only the C wallets are fresh
        self.assertEqual(m["busy_holders"], 1)                # OLD
        kills = verdict(m, CFG)
        self.assertTrue(any(k.startswith("operator_cluster") for k in kills))
        self.assertFalse(any(k.startswith("fresh_wallets") for k in kills))
        self.assertLess(m["rpc_calls"], CFG["cluster"]["est_credits_per_token"])

    def test_exchange_funding_not_linked(self):
        chain = FakeChain()
        for w in ("C1", "C2", "C3"):
            chain.funder[w] = "BINANCE"
        chain.funder["C4"] = "BINANCE"
        m = analyse(Rpc("x", 0, post=chain), "MINT", CFG, {"AMM"}, NOW)
        self.assertEqual(m["n_clusters"], 0)
        self.assertEqual(verdict(m, CFG), [])


class TestCabalFinder(unittest.TestCase):
    def test_budget_cache_and_failure(self):
        with tempfile.TemporaryDirectory() as d:
            db = DB(os.path.join(d, "t.db"))
            chain = FakeChain()
            cf = CabalFinder(CFG, db, api_key="k", post=chain, log=lambda *a: None)
            kills, m = cf.check("MINT", NOW, {"AMM"})
            self.assertTrue(kills)
            used = db.credits_used(NOW)
            self.assertEqual(used, m["rpc_calls"])
            n_before = len(chain.calls)
            cf.check("MINT", NOW + 60, {"AMM"})            # cached: no new calls
            self.assertEqual(len(chain.calls), n_before)

            def broken(payload):
                return {"error": {"code": -32000, "message": "boom"}}
            cf2 = CabalFinder(CFG, db, api_key="k", post=broken, log=lambda *a: None)
            kills, _ = cf2.check("OTHER", NOW, None)
            self.assertEqual(kills, ["unknown:cluster"])     # unknown is never safe

            db.add_credits(NOW, CFG["cluster"]["daily_credit_budget"])
            kills, _ = cf2.check("THIRD", NOW, None)
            self.assertEqual(kills, ["unknown:cluster_budget"])
            self.assertIsNone(cf2.check("FOURTH", NOW, None, research=True))

    def test_disabled_without_key(self):
        with tempfile.TemporaryDirectory() as d:
            db = DB(os.path.join(d, "t.db"))
            os.environ.pop("HELIUS_API_KEY", None)
            cf = CabalFinder(CFG, db)
            self.assertFalse(cf.enabled)
            self.assertIsNone(cf.check("MINT", NOW))


if __name__ == "__main__":
    unittest.main()


class TestCycleWithCabal(unittest.TestCase):
    def test_cycle(self):
        from test_trenchlab import FakeFetch, NOW as TNOW
        from trenchlab.gecko import Gecko
        from trenchlab.audit import Auditor
        from trenchlab.scanner import run_cycle
        from trenchlab.lab import build_report
        with tempfile.TemporaryDirectory() as d:
            db = DB(os.path.join(d, "t.db"))
            fetch = FakeFetch()
            cf = CabalFinder(CFG, db, api_key="k", post=FakeChain(), log=lambda *a: None)
            rows, _ = run_cycle(Gecko("solana", 0, fetch=fetch), Auditor(CFG, fetch=fetch), db, CFG,
                                now=TNOW, log=lambda *a: None, alert=False, cabal=cf)
            good = [r for r in rows if r[1].symbol == "GOOD"][0]
            self.assertFalse(good[6])  # would have passed, but the cabal finder killed it
            self.assertTrue(any(k.startswith("operator_cluster") for k in good[3]))
            for i in range(1, 4):
                fetch.price = 0.001 * (1 - 0.2 * i)
                run_cycle(Gecko("solana", 0, fetch=fetch), Auditor(CFG, fetch=fetch), db, CFG,
                          now=TNOW + i * 3600, log=lambda *a: None, alert=False, cabal=cf)
            rep = build_report(db, CFG, TNOW + 4 * 3600)
            self.assertIn("CABAL CHECK", rep)
            self.assertIn("helius credits today", rep)
