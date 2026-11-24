"""Wallet finder tests on a fake chain: a smart wallet, a sniper bot, a flipper, noise."""
import copy
import csv
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from trenchlab import walletfinder as wf
from test_trenchlab import CFG

NOW = 1_800_000_000


def trade_tx(mint, trader, side, tokens, sol, slot, ts, acct):
    pre_tok = 0 if side == "buy" else tokens
    post_tok = tokens if side == "buy" else 0
    lam_pre, lam_post = 10 * 10**9, int(10 * 10**9 + sol * 10**9)
    return {"slot": slot, "blockTime": ts, "meta": {"err": None,
            "preBalances": [lam_pre], "postBalances": [lam_post],
            "preTokenBalances": [{"mint": mint, "owner": trader, "accountIndex": 1, "uiTokenAmount": {"uiAmount": pre_tok}}],
            "postTokenBalances": [{"mint": mint, "owner": trader, "accountIndex": 1, "uiTokenAmount": {"uiAmount": post_tok}}]},
            "transaction": {"message": {"accountKeys": [{"pubkey": trader}, {"pubkey": acct}]}}}


class Chain:
    """Winners W1..W3, dead tokens D1..D3.
    SMART: buys each winner ~2 min after launch, sells hours later for profit, quiet wallet.
    SNIPER: buys EVERY token (winners and dead) in the launch slot, very busy.
    FLIP: early on 2 winners, sells within 30s.
    Retail R*: one token each."""

    def __init__(self):
        self.txs = {}
        self.sigs = {}            # address -> newest-first list of {signature, slot, blockTime, err}
        self.busy = {"SNIPER"}
        for i, m in enumerate(["W1", "W2", "W3", "D1", "D2", "D3"]):
            base = 1000 * (i + 1)
            t0 = NOW - 86400 * (i + 1)
            evs = [("SNIPER", "buy", 0, 0)]
            if m.startswith("W"):
                evs += [("SMART", "buy", 300, 120)]
                if m != "W3":
                    evs += [("FLIP", "buy", 200, 60)]
            evs += [(f"R{m}{k}", "buy", 400 + k, 200 + k) for k in range(3)]
            mint_sigs = []
            for trader, side, dslot, dsec in evs:
                sig = f"{m}:{trader}:{side}"
                acct = f"ACC_{trader}_{m}"
                self.txs[sig] = trade_tx(m, trader, side, 100, -1.0, base + dslot, t0 + dsec, acct)
                mint_sigs.append({"signature": sig, "slot": base + dslot, "blockTime": t0 + dsec, "err": None})
                self.sigs.setdefault(acct, []).append({"signature": sig, "slot": base + dslot, "blockTime": t0 + dsec, "err": None})
            # exits
            for trader, dsec, sol in (("SMART", 3 * 3600, 3.0), ("FLIP", 90, 1.05)):
                if (trader, m) == ("FLIP", "W3") or not m.startswith("W"):
                    continue
                sig = f"{m}:{trader}:sell"
                acct = f"ACC_{trader}_{m}"
                self.txs[sig] = trade_tx(m, trader, "sell", 100, sol, base + 5000, t0 + dsec, acct)
                self.sigs[acct].append({"signature": sig, "slot": base + 5000, "blockTime": t0 + dsec, "err": None})
            mint_sigs.sort(key=lambda s: s["slot"])
            self.sigs[m] = list(reversed(mint_sigs))
            for a in list(self.sigs):
                if a.startswith("ACC_"):
                    self.sigs[a].sort(key=lambda s: -s["slot"])
        self.calls = 0

    def __call__(self, payload):
        self.calls += 1
        m, p = payload["method"], payload["params"]
        if m == "getSignaturesForAddress":
            addr, opts = p
            if addr in self.busy:
                return {"result": [{"signature": f"x{i}", "blockTime": NOW - i * 10} for i in range(opts["limit"])]}
            if addr in ("SMART", "FLIP") or addr.startswith("R"):
                return {"result": [{"signature": f"w{i}", "blockTime": NOW - i * 7200} for i in range(40)]}
            lst = self.sigs.get(addr, [])
            if opts.get("before"):
                return {"result": []}
            return {"result": lst[: opts["limit"]]}
        if m == "getTransaction":
            return {"result": self.txs.get(p[0])}
        raise AssertionError(m)


class TestParse(unittest.TestCase):
    def test_parse_buy_sell(self):
        b = wf.parse_trade(trade_tx("M", "A", "buy", 50, -0.5, 10, NOW, "ACC"), "M")
        self.assertEqual((b["trader"], b["side"], b["tokens"], b["token_account"]), ("A", "buy", 50, "ACC"))
        self.assertAlmostEqual(b["sol"], -0.5)
        s = wf.parse_trade(trade_tx("M", "A", "sell", 50, 0.8, 11, NOW, "ACC"), "M")
        self.assertEqual(s["side"], "sell")
        self.assertIsNone(wf.parse_trade(trade_tx("OTHER", "A", "buy", 50, -0.5, 10, NOW, "ACC"), "M"))


class TestRun(unittest.TestCase):
    def test_classification(self):
        chain = Chain()
        cfg = copy.deepcopy(CFG)
        cfg["walletfinder"].update({"min_interval": 0, "max_dead_frac": 0.5})
        winners = [{"symbol": s, "address": s} for s in ("W1", "W2", "W3")]
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "research")
            rows = wf.run(cfg, winners, ["D1", "D2", "D3"], out_dir=out, post=chain, log=lambda *a: None)
            by = {r["wallet"]: r for r in rows}
            self.assertEqual(set(by), {"SMART", "SNIPER", "FLIP"})      # retail: only 1 winner each
            self.assertEqual(by["SMART"]["copy_candidate"], "YES")
            self.assertEqual(by["SMART"]["winners_early"], 3)
            self.assertAlmostEqual(by["SMART"]["realized_sol"], 6.0)    # 3 x (+3 - 1)
            self.assertIn("buys_dead_tokens_too", by["SNIPER"]["flags"])
            self.assertIn("launch_sniper", by["SNIPER"]["flags"])
            self.assertIn("high_frequency", by["SNIPER"]["flags"])
            self.assertIn("flipper", by["FLIP"]["flags"])
            self.assertEqual(rows[0]["wallet"], "SMART")                  # copy candidates first
            self.assertTrue(os.path.exists(os.path.join(out, "watchlist.csv")))
            with open(os.path.join(d, "WALLETS.md")) as f:
                md = f.read()
            self.assertIn("Hindsight warning", md)
            # second run uses the cache for stage 1
            before = chain.calls
            wf.run(cfg, winners, ["D1", "D2", "D3"], out_dir=out, post=chain, log=lambda *a: None)
            self.assertLess(chain.calls - before, before)


if __name__ == "__main__":
    unittest.main()
