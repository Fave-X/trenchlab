"""Wallet finder v2: judge wallets on recent overall trading with the winners removed."""
import copy
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from trenchlab import walletfinder as wf
from test_trenchlab import CFG
from test_copytrade import swap

NOW = 1_800_000_000


class Chain:
    def __init__(self):
        self.sigs = {}      # wallet -> newest-first sig list
        self.txs = {}
        self.n = 0

    def trade(self, wallet, mint, side, sol, ts, tokens=1000):
        self.n += 1
        sig = f"s{self.n}"
        self.txs[sig] = swap(wallet, mint, side, tokens, sol)
        self.sigs.setdefault(wallet, []).append({"signature": sig, "blockTime": ts, "err": None})

    def __call__(self, payload):
        m, p = payload["method"], payload["params"]
        if m == "getSignaturesForAddress":
            lst = sorted(self.sigs.get(p[0], []), key=lambda s: -s["blockTime"])
            return {"result": lst[: p[1]["limit"]]}
        if m == "getTransaction":
            return {"result": self.txs.get(p[0])}
        raise AssertionError(m)


def build():
    ch = Chain()
    t0 = NOW - 5 * 86400
    # GOOD: 12 round trips over 5 days, 0.5 SOL each, 9 wins of +0.3, 3 losses of -0.2, holds 40 min
    for i in range(12):
        ts = t0 + i * 30000
        ch.trade("GOOD", f"G{i}", "buy", -0.5, ts)
        ch.trade("GOOD", f"G{i}", "sell", 0.8 if i % 4 else 0.3, ts + 2400)
    # SPRAY: 60 tokens a day, tiny buys
    for i in range(60):
        ch.trade("SPRAY", f"S{i}", "buy", -0.05, NOW - 86400 + i * 600)
        ch.trade("SPRAY", f"S{i}", "sell", 0.06, NOW - 86400 + i * 600 + 400)
    # ONEHIT: 11 small losses and one huge win
    for i in range(12):
        ts = t0 + i * 30000
        ch.trade("ONEHIT", f"O{i}", "buy", -0.5, ts)
        ch.trade("ONEHIT", f"O{i}", "sell", 8.0 if i == 0 else 0.4, ts + 3600)
    # WINNERONLY: its only profit is on the CoreSight winner W1; the rest lose
    ch.trade("WINNERONLY", "W1", "buy", -1.0, t0)
    ch.trade("WINNERONLY", "W1", "sell", 20.0, t0 + 7200)
    for i in range(11):
        ts = t0 + 10000 + i * 30000
        ch.trade("WINNERONLY", f"L{i}", "buy", -0.5, ts)
        ch.trade("WINNERONLY", f"L{i}", "sell", 0.3, ts + 3600)
    return ch


class TestProfile(unittest.TestCase):
    def test_profiles_and_verdicts(self):
        ch = build()
        c = CFG["walletfinder"]
        rpc = wf.Rpc("x", min_interval=0, post=ch)
        good = wf.profile_wallet(rpc, "GOOD", 100, exclude_mints={"W1"})
        self.assertEqual(good["closed_trades"], 12)
        self.assertAlmostEqual(good["realized_sol_ex_winners"], 9 * 0.3 - 3 * 0.2)
        self.assertEqual(good["median_hold_min"], 40.0)
        self.assertEqual(wf.v2_verdict(good, c), [])
        spray = wf.profile_wallet(rpc, "SPRAY", 200)
        self.assertIn("sprays_tokens", wf.v2_verdict(spray, c))
        self.assertIn("buys_too_small", wf.v2_verdict(spray, c))
        onehit = wf.profile_wallet(rpc, "ONEHIT", 100)
        self.assertIn("one_hit_wonder", wf.v2_verdict(onehit, c))
        wo = wf.profile_wallet(rpc, "WINNERONLY", 100, exclude_mints={"W1"})
        self.assertIn("loses_money_ex_winners", wf.v2_verdict(wo, c))


class TestRunV2(unittest.TestCase):
    def test_run(self):
        ch = build()
        cfg = copy.deepcopy(CFG)
        cfg["walletfinder"].update({"min_interval": 0})
        cache = {
            "W1": {"complete": True, "buyers": {
                "GOOD": {"sol_in": 0.5, "slot_offset": 40}, "SPRAY": {"sol_in": 0.5, "slot_offset": 40},
                "ONEHIT": {"sol_in": 0.5, "slot_offset": 40}, "WINNERONLY": {"sol_in": 1.0, "slot_offset": 40},
                "DEADTOO": {"sol_in": 2.0, "slot_offset": 40}, "SNIPER": {"sol_in": 2.0, "slot_offset": 0},
                "SMALL": {"sol_in": 0.05, "slot_offset": 40}}},
            "D1": {"complete": True, "buyers": {"DEADTOO": {"sol_in": 1.0, "slot_offset": 5}}},
        }
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "research")
            os.makedirs(out)
            with open(os.path.join(out, "early_buyers_cache.json"), "w") as f:
                json.dump(cache, f)
            rows = wf.run_v2(cfg, [{"symbol": "WIN", "address": "W1"}], out_dir=out, post=ch, log=lambda *a: None)
            by = {r["wallet"]: r for r in rows}
            self.assertNotIn("DEADTOO", by)          # early on a dead token too
            self.assertNotIn("SNIPER", by)           # launch sniper
            self.assertNotIn("SMALL", by)            # too small
            self.assertEqual(by["GOOD"]["verdict"], "COPY CANDIDATE")
            self.assertEqual(rows[0]["wallet"], "GOOD")
            self.assertNotEqual(by["WINNERONLY"]["verdict"], "COPY CANDIDATE")
            with open(os.path.join(d, "WALLETS_V2.md")) as f:
                self.assertIn("pass every v2 check", f.read())


if __name__ == "__main__":
    unittest.main()
