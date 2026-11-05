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
    """Token MINT, supply 1000.
    AMM (known) 400; POOLPDA (program-owned) 100.
    Cabal: C1, C2 bought in ONE transaction (bundle) at slot 100; C3 bought alone, also slot 100;
           C1..C3 funded by FUNDERX (quiet); C4 was handed 30 tokens by C1 (not bought).
    Retail R1..R5 (20 each) bought at different slots, funded by BINANCE (busy).
    OLD (50) is a very active wallet, bought at slot 500."""

    def __init__(self, busy_cabal=False, cabal_funder="FUNDERX"):
        self.holdings = {"AMMVAULT_ACC": ("AMM", 400), "POOL_ACC": ("POOLPDA", 100),
                         "C1_ACC": ("C1", 60), "C2_ACC": ("C2", 60), "C3_ACC": ("C3", 60),
                         "C4_ACC": ("C4", 30), "OLD_ACC": ("OLD", 50)}
        for i in range(1, 6):
            self.holdings[f"R{i}_ACC"] = (f"R{i}", 20)
        self.funder = {"C1": cabal_funder, "C2": cabal_funder, "C3": cabal_funder, "C4": "C1"}
        for i in range(1, 6):
            self.funder[f"R{i}"] = "BINANCE"
        self.busy = {"OLD", "BINANCE"} | ({"C1", "C2", "C3"} if busy_cabal else set())
        self.acq = {"C1": ("BUNDLE1", 100), "C2": ("BUNDLE1", 100), "C3": ("C3BUY", 100),
                    "C4": ("C4XFER", 150), "OLD": ("OLDBUY", 500)}
        for i in range(1, 6):
            self.acq[f"R{i}"] = (f"R{i}BUY", 200 + i)
        self.calls = []

    def _buy_tx(self, buyers):
        keys = [{"pubkey": b} for b in buyers] + [{"pubkey": "AMM"}]
        pre = [10_000_000_000] * len(buyers) + [0]
        post = [10_000_000_000 - 500_000_000] * len(buyers) + [0]
        ptb = [{"mint": "MINT", "owner": "AMM", "uiTokenAmount": {"uiAmount": 1000}}]
        qtb = [{"mint": "MINT", "owner": "AMM", "uiTokenAmount": {"uiAmount": 1000 - 60 * len(buyers)}}]
        qtb += [{"mint": "MINT", "owner": b, "uiTokenAmount": {"uiAmount": 60}} for b in buyers]
        return {"transaction": {"message": {"accountKeys": keys, "instructions": []}},
                "meta": {"preBalances": pre, "postBalances": post,
                         "preTokenBalances": ptb, "postTokenBalances": qtb, "innerInstructions": []}}

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
            if w.endswith("_ACC"):
                owner = w[:-4]
                sig, slot = self.acq[owner]
                return {"result": [{"signature": "later", "slot": slot + 50}, {"signature": sig, "slot": slot}]}
            if w in self.busy:
                return {"result": [{"signature": f"s{i}", "blockTime": NOW - 10**7} for i in range(opts["limit"])]}
            if w == "FUNDERX":
                return {"result": [{"signature": "f1", "blockTime": NOW - 3600}]}
            n = 3 if w.startswith("C") else 50
            age = 3600 * 5 if w.startswith("C") else 86400 * 200
            return {"result": [{"signature": f"{w}_sig{i}", "blockTime": NOW - age + i} for i in range(n, 0, -1)]}
        if m == "getTransaction":
            sig = params[0]
            if sig == "BUNDLE1":
                return {"result": self._buy_tx(["C1", "C2"])}
            if sig.endswith("BUY"):
                return {"result": self._buy_tx([sig[:-3]])}
            if sig == "C4XFER":
                return {"result": {"transaction": {"message": {
                    "accountKeys": [{"pubkey": "C1"}, {"pubkey": "C4"}], "instructions": []}},
                    "meta": {"preBalances": [5_000_000_000, 0], "postBalances": [4_997_000_000, 2_039_280],
                             "preTokenBalances": [{"mint": "MINT", "owner": "C1", "uiTokenAmount": {"uiAmount": 90}}],
                             "postTokenBalances": [{"mint": "MINT", "owner": "C1", "uiTokenAmount": {"uiAmount": 60}},
                                                   {"mint": "MINT", "owner": "C4", "uiTokenAmount": {"uiAmount": 30}}]}}}
            w = sig.split("_sig")[0]
            src = self.funder[w]
            return {"result": {"transaction": {"message": {
                "accountKeys": [{"pubkey": src}, {"pubkey": w}],
                "instructions": [sys_transfer(src, w)]}}, "meta": {"innerInstructions": []}}}
        raise AssertionError((m, params))


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
    def run_chain(self, chain):
        return analyse(Rpc("x", min_interval=0, post=chain), "MINT", CFG, known_accounts={"AMM"}, now=NOW)

    def test_cabal_detected(self):
        m = self.run_chain(FakeChain())
        self.assertEqual(m["holders_analysed"], 10)            # AMM + program-owned PDA dropped
        self.assertEqual(m["largest_cluster_size"], 4)         # C1..C4
        self.assertAlmostEqual(m["largest_cluster_pct"], 21.0)
        self.assertAlmostEqual(m["same_slot_pct"], 18.0)       # C1, C2, C3 at slot 100
        self.assertAlmostEqual(m["received_pct"], 3.0)         # C4 was handed tokens
        self.assertAlmostEqual(m["fresh_pct"], 21.0)
        self.assertEqual(m["acq_traced"], 10)
        kills = verdict(m, CFG)
        self.assertTrue(any(k.startswith("operator_cluster") for k in kills))
        self.assertLess(m["rpc_calls"], CFG["cluster"]["est_credits_per_token"])

    def test_busy_cabal_still_caught_via_acquisition(self):
        """The live-run failure: active wallets can't be funding-traced, but the
        shared bundle transaction and token hand-over still link them."""
        m = self.run_chain(FakeChain(busy_cabal=True, cabal_funder="BINANCE"))
        self.assertGreaterEqual(m["busy_holders"], 4)
        self.assertEqual(m["largest_cluster_size"], 3)         # C1+C2 (same tx) + C4 (handed by C1)
        self.assertAlmostEqual(m["largest_cluster_pct"], 15.0)
        self.assertAlmostEqual(m["same_slot_pct"], 18.0)

    def test_retail_only_is_clean(self):
        ch = FakeChain(cabal_funder="BINANCE")
        ch.acq.update({"C1": ("C1BUY", 101), "C2": ("C2BUY", 102), "C3": ("C3BUY", 103)})
        ch.funder["C4"] = "BINANCE"
        ch.acq["C4"] = ("C4BUY", 104)
        m = self.run_chain(ch)
        self.assertEqual(m["n_clusters"], 0)
        self.assertEqual(m["same_slot_pct"], 0)
        self.assertEqual(m["received_pct"], 0)
        self.assertTrue(all(not k.startswith(("operator", "clustered", "bundled", "received"))
                            for k in verdict(m, CFG)))


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
