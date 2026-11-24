"""Book C (copy-trading) tests with a fake chain and fake candle pricer."""
import copy
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from trenchlab.db import DB
from trenchlab.cluster import Rpc
from trenchlab.paper import PaperTrader, ModelQuoter, paper_report
from trenchlab import copytrade as ct
from trenchlab.gecko import parse_pool_list
from test_trenchlab import gecko_item, payload, CFG

NOW = 1_800_000_000
W = "WaLLeT1111111111111111111111111111111111111"


def swap(wallet, mint, side, tokens, sol, fee_payer=None):
    keys = [{"pubkey": fee_payer or wallet}] + ([{"pubkey": wallet}] if fee_payer else [])
    i = len(keys) - 1
    pre = [10 * 10**9] * len(keys)
    post = list(pre)
    post[i] = pre[i] + int(sol * 10**9)
    pt = 0 if side == "buy" else tokens
    qt = tokens if side == "buy" else 0
    return {"meta": {"err": None, "preBalances": pre, "postBalances": post,
                     "preTokenBalances": [{"mint": mint, "owner": wallet, "uiTokenAmount": {"uiAmount": pt}}],
                     "postTokenBalances": [{"mint": mint, "owner": wallet, "uiTokenAmount": {"uiAmount": qt}}]},
            "transaction": {"message": {"accountKeys": keys}}}


class FakeChain:
    def __init__(self):
        self.sigs = []          # newest first
        self.txs = {}

    def add(self, sig, ts, tx):
        self.sigs.insert(0, {"signature": sig, "blockTime": ts, "err": None})
        self.txs[sig] = tx

    def __call__(self, payload):
        m, p = payload["method"], payload["params"]
        if m == "getSignaturesForAddress":
            opts = p[1]
            out = []
            for s in self.sigs:
                if s["signature"] == opts.get("until"):
                    break
                out.append(s)
            return {"result": out[: opts["limit"]]}
        if m == "getTransaction":
            return {"result": self.txs.get(p[0])}
        raise AssertionError(m)


class FakePricer:
    def __init__(self):
        self.prices = {}        # (pool, side) -> price
        self.asked = []

    def top_pool(self, mint):
        return parse_pool_list(payload(gecko_item(addr="POOL_" + mint, mint=mint, symbol=mint, liq=60000)),
                               "solana")[0]

    def price_at(self, pool, ts, side):
        self.asked.append((pool, ts, side))
        return self.prices.get((pool, side))


class TestParse(unittest.TestCase):
    def test_wallet_trades(self):
        self.assertEqual(ct.wallet_trades(swap(W, "M1", "buy", 100, -1.0), W), [("M1", "buy", 100, -1.0)])
        self.assertEqual(ct.wallet_trades(swap(W, "M1", "sell", 100, 2.0), W), [("M1", "sell", 100, 2.0)])
        # relayer pays the fee: the wallet's own balances still count
        self.assertEqual(ct.wallet_trades(swap(W, "M1", "buy", 50, -0.5, fee_payer="RELAY"), W)[0][1], "buy")
        self.assertEqual(ct.wallet_trades(swap("OTHER", "M1", "buy", 5, -1.0), W), [])

    def test_watchlist_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "w.txt")
            with open(p, "w") as f:
                f.write(f"# comment\n{W}  # smart-1\nnot-a-wallet\n\n")
            self.assertEqual(ct.load_watchlist(p), {W: "smart-1"})


class TestCycle(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        self.db = DB(os.path.join(self.d.name, "t.db"))
        self.cfg = copy.deepcopy(CFG)
        self.trader = PaperTrader(self.cfg, self.db, quoter=ModelQuoter(self.cfg), log=lambda *a: None, book="C")
        self.chain = FakeChain()
        self.rpc = Rpc("x", min_interval=0, post=self.chain)
        self.pricer = FakePricer()
        self.watch = os.path.join(self.d.name, "watch.txt")
        with open(self.watch, "w") as f:
            f.write(f"{W}  # smart-1\n")

    def cycle(self, now):
        return ct.run(self.db, self.trader, self.cfg, now, rpc=self.rpc, pricer=self.pricer,
                      log=lambda *a: None, watch_path=self.watch)

    def test_full_copy_flow(self):
        self.chain.add("old_buy", NOW - 5000, swap(W, "OLD", "buy", 10, -2.0))
        self.assertEqual(self.cycle(NOW), (0, 0))                 # first sight: bookmark only
        self.assertEqual(self.db.open_positions("C"), [])

        self.chain.add("buy1", NOW + 500, swap(W, "TOK", "buy", 1000, -2.0))
        self.chain.add("dust", NOW + 510, swap(W, "DUST", "buy", 1000, -0.01))
        self.pricer.prices[("POOL_TOK", "buy")] = 0.002
        self.assertEqual(self.cycle(NOW + 600), (1, 0))
        pos = self.db.open_positions("C")
        self.assertEqual([p["symbol"] for p in pos], ["TOK"])     # dust buy ignored
        self.assertAlmostEqual(pos[0]["cost_usd"], 25.0)          # fixed 5% of $500
        self.assertIn(("POOL_TOK", NOW + 500 + 30, "buy"), self.pricer.asked)   # priced 30s after wallet

        self.chain.add("sell1", NOW + 1100, swap(W, "TOK", "sell", 1000, 5.0))
        self.pricer.prices[("POOL_TOK", "sell")] = 0.004
        self.assertEqual(self.cycle(NOW + 1200), (0, 1))
        closed = self.db.closed_positions("C")
        self.assertEqual(closed[0]["exit_reason"], "mirror_sell")
        self.assertGreater(closed[0]["exit_value"], 45)           # ~2x minus costs
        rep = paper_report(self.db, self.cfg, "C") + ct.wallet_report(self.db)
        self.assertIn("ledger reconciles: YES", rep)
        self.assertIn("smart-1", rep)

    def test_stale_signal_not_copied(self):
        self.cycle(NOW)
        self.chain.add("late", NOW + 100, swap(W, "TOK", "buy", 1000, -2.0))
        self.pricer.prices[("POOL_TOK", "buy")] = 0.002
        self.assertEqual(self.cycle(NOW + 100 + 31 * 60), (0, 0))  # 31 min old: skipped

    def test_no_price_at_delay_skipped(self):
        self.cycle(NOW)
        self.chain.add("b", NOW + 100, swap(W, "TOK", "buy", 1000, -2.0))
        self.assertEqual(self.cycle(NOW + 600), (0, 0))
        self.assertIn("copy:no_price_at_delay", dict(self.db.paper_skip_counts("C")))


class TestCandle(unittest.TestCase):
    def test_price_at(self):
        def fetch(url, min_interval=0):
            return {"data": {"attributes": {"ohlcv_list": [
                [NOW + 60, 1, 1, 1, 1, 0], [NOW, 1.0, 1.4, 0.8, 1.2, 10], [NOW - 60, 0.9, 1, 0.9, 1, 5]]}}}
        p = ct.CandlePricer(fetch=fetch, min_interval=0)
        self.assertAlmostEqual(p.price_at("POOL", NOW + 30, "buy"), 1.3)    # (high + close) / 2
        self.assertAlmostEqual(p.price_at("POOL", NOW + 30, "sell"), 1.0)   # (low + close) / 2


if __name__ == "__main__":
    unittest.main()
