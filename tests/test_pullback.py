"""Book B (pullback) tests + migration of the old single paper bank into book A."""
import copy
import os
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from trenchlab.db import DB
from trenchlab.gecko import parse_pool_list
from trenchlab.paper import PaperTrader, ModelQuoter, comparison_report, paper_report
from trenchlab import pullback
from test_trenchlab import gecko_item, payload, CFG, NOW


def mk_pool(addr="B1", mint="MB1", age_h=6, price=1.0, liq=60000, **kw):
    return parse_pool_list(payload(gecko_item(addr=addr, mint=mint, symbol=addr, age_h=age_h,
                                              price=price, liq=liq, **kw)), "solana")[0]


def seed(db, pool, path, start, liq=60000):
    """path: list of (minutes_after_start, price) samples"""
    db.upsert_first_seen(pool, start, ["too_old"], start + 86400)
    for m, px in path:
        db.add_sample(pool.address, start + m * 60, px, liq if not callable(liq) else liq(m))


GOOD_PATH = [(0, 1.0), (10, 1.5), (20, 2.0), (30, 1.6), (40, 1.2), (50, 1.0), (60, 1.02),
             (70, 1.06), (80, 1.1)]   # -45% from high, low 30 min ago, +10% bounce


class TestPriceCandidates(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        self.db = DB(os.path.join(self.d.name, "t.db"))
        self.start = NOW - 80 * 60

    def test_good_setup(self):
        seed(self.db, mk_pool(), GOOD_PATH, self.start)
        c = pullback.price_candidates(self.db, CFG, NOW)
        self.assertEqual([a for a, _ in c], ["B1"])
        self.assertAlmostEqual(c[0][1]["drawdown_pct"], -45.0)
        self.assertAlmostEqual(c[0][1]["bounce_pct"], 10.0)

    def test_rejections(self):
        cases = {
            "still falling": GOOD_PATH[:-3] + [(60, 0.98), (70, 0.95), (80, 1.0)],      # low is only 10 min old
            "too deep": [(0, 1.0), (20, 3.0), (40, 0.8), (60, 0.82), (80, 0.9)] + [(5, 1), (15, 1)],
            "no dip": [(m, 1.0 + m / 100) for m in range(0, 90, 10)],
        }
        for name, path in cases.items():
            db = DB(os.path.join(self.d.name, name.replace(" ", "_") + ".db"))
            seed(db, mk_pool(), sorted(path), self.start)
            self.assertEqual(pullback.price_candidates(db, CFG, NOW), [], name)

    def test_liquidity_drain_and_age(self):
        seed(self.db, mk_pool(), GOOD_PATH, self.start, liq=lambda m: 60000 if m < 60 else 25000)
        self.assertEqual(pullback.price_candidates(self.db, CFG, NOW), [])
        db2 = DB(os.path.join(self.d.name, "young.db"))
        seed(db2, mk_pool(age_h=1), GOOD_PATH, self.start)
        self.assertEqual(pullback.price_candidates(db2, CFG, NOW), [])


class TestFilters(unittest.TestCase):
    def test_activity(self):
        ok = mk_pool(buyers=200, buys=500, sells=400, vol_h1=30000, liq=60000)
        self.assertEqual(pullback.activity_kills(ok, CFG), [])
        bad = mk_pool(buyers=40, buys=100, sells=300, vol_h1=5000, liq=60000)
        k = pullback.activity_kills(bad, CFG)
        self.assertIn("few_buyers_now", k)
        self.assertIn("sellers_dominate_now", k)
        self.assertIn("volume_dried_up", k)

    def test_strict_cabal(self):
        self.assertEqual(pullback.strict_cabal_kills({"same_slot_pct": 0, "fresh_pct": 5, "received_pct": 0}, CFG), [])
        k = pullback.strict_cabal_kills({"same_slot_pct": 12, "fresh_pct": 30, "received_pct": 15}, CFG)
        self.assertEqual(len(k), 3)


class FakeGecko:
    def __init__(self, pools):
        self.pools = pools

    def pools_multi(self, addrs):
        return [p for p in self.pools if p.address in addrs]


class FakeAuditor:
    def __init__(self):
        self.known_accounts = {}

    def audit(self, mint):
        return (True, [], []) if mint != "MBAD" else (False, ["mint_authority_active"], [])


class FakeCabal:
    enabled = True
    runs_this_cycle = 0

    def check(self, mint, now, known=None, research=False):
        if mint == "MBUNDLE":
            return [], {"same_slot_pct": 15, "fresh_pct": 0, "received_pct": 0}
        return [], {"same_slot_pct": 0, "fresh_pct": 5, "received_pct": 0}


class TestRun(unittest.TestCase):
    def test_end_to_end(self):
        d = tempfile.TemporaryDirectory()
        db = DB(os.path.join(d.name, "t.db"))
        start = NOW - 80 * 60
        live = []
        for addr, mint in (("B1", "MB1"), ("B2", "MBAD"), ("B3", "MBUNDLE")):
            seed(db, mk_pool(addr, mint), GOOD_PATH, start)
            live.append(mk_pool(addr, mint, price=1.1, buyers=200, buys=500, sells=400, vol_h1=30000))
        cfg = copy.deepcopy(CFG)
        tb = PaperTrader(cfg, db, quoter=ModelQuoter(cfg), log=lambda *a: None, book="B")
        ta = PaperTrader(cfg, db, quoter=ModelQuoter(cfg), log=lambda *a: None, book="A")
        n = pullback.run(db, FakeGecko(live), FakeAuditor(), FakeCabal(), tb, cfg, NOW, log=lambda *a: None)
        self.assertEqual(n, 1)
        opens = db.open_positions("B")
        self.assertEqual([p["symbol"] for p in opens], ["B1"])
        self.assertEqual(db.open_positions("A"), [])                    # books are independent
        skips = dict(db.paper_skip_counts("B"))
        self.assertIn("setup_rejected:mint_authority_active", skips)
        self.assertIn("setup_rejected:b_bundled", skips)
        # second run: no re-entry on the same token
        self.assertEqual(pullback.run(db, FakeGecko(live), FakeAuditor(), FakeCabal(), tb, cfg, NOW + 600,
                                      log=lambda *a: None), 0)
        rep = comparison_report(db)
        self.assertIn("A vs B", rep)
        self.assertIn("PAPER BOOK B", paper_report(db, cfg, "B"))
        self.assertIn("ledger reconciles: YES", paper_report(db, cfg, "B"))
        self.assertAlmostEqual(db.paper_cash("A"), 500.0)


class TestMigration(unittest.TestCase):
    def test_old_single_bank_becomes_book_a(self):
        d = tempfile.TemporaryDirectory()
        path = os.path.join(d.name, "old.db")
        c = sqlite3.connect(path)
        c.executescript("""
            CREATE TABLE paper_bank (id INTEGER PRIMARY KEY CHECK (id = 1), start_usd REAL, cash REAL, created_ts REAL);
            INSERT INTO paper_bank VALUES (1, 500, 479.86, 1793950000);
            CREATE TABLE paper_positions (id INTEGER PRIMARY KEY AUTOINCREMENT, pool_address TEXT, token_mint TEXT,
              symbol TEXT, mode TEXT, entry_ts REAL, cost_usd REAL, tokens REAL, score REAL, entry_info TEXT,
              last_value REAL, peak_value REAL, misses INTEGER DEFAULT 0, exit_ts REAL, exit_value REAL, exit_reason TEXT);
            INSERT INTO paper_positions (pool_address, token_mint, symbol, mode, entry_ts, cost_usd, tokens,
              exit_ts, exit_value, exit_reason) VALUES ('P','M','RM','model',1,25,1,2,14.03,'stop');
            CREATE TABLE paper_skips (ts REAL, pool_address TEXT, symbol TEXT, reason TEXT);
            CREATE TABLE paper_equity (ts REAL, equity REAL, cash REAL, n_open INTEGER);
        """)
        c.commit()
        c.close()
        db = DB(path)
        self.assertAlmostEqual(db.paper_cash("A"), 479.86)
        self.assertEqual([p["symbol"] for p in db.closed_positions("A")], ["RM"])
        self.assertEqual(db.paper_books(), ["A"])


if __name__ == "__main__":
    unittest.main()
