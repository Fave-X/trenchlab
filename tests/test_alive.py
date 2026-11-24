"""Alive-check classification tests."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from trenchlab.alive import classify, markdown


class TestClassify(unittest.TestCase):
    def test_statuses(self):
        call, ath = 30000, 5.0                       # peak = $150k
        self.assertEqual(classify({}, call, ath)[0], "dead")
        self.assertEqual(classify({"mcap": 8000, "liq": 20000, "vol24": 50000}, call, ath)[0], "dead")
        self.assertEqual(classify({"mcap": 90000, "liq": 3000, "vol24": 50000}, call, ath)[0], "dead")
        self.assertEqual(classify({"mcap": 40000, "liq": 20000, "vol24": 30000, "chg24": -10,
                                   "buyers1h": 50, "sellers1h": 40}, call, ath)[0], "fading")   # -73% from peak
        self.assertEqual(classify({"mcap": 100000, "liq": 30000, "vol24": 90000, "chg24": 5,
                                   "buyers1h": 50, "sellers1h": 80}, call, ath)[0], "fading")   # sellers dominate
        self.assertEqual(classify({"mcap": 100000, "liq": 30000, "vol24": 90000, "chg24": 5,
                                   "buyers1h": 150, "sellers1h": 90}, call, ath)[0], "thriving")
        self.assertEqual(classify({"mcap": 60000, "liq": 30000, "vol24": 9000, "chg24": 5,
                                   "buyers1h": 50, "sellers1h": 40}, call, ath)[0], "alive")

    def test_markdown(self):
        md = markdown([{"symbol": "X", "status": "alive", "warnings": "", "mcap": 60000, "liq": 30000,
                        "vol24": 9000, "chg24": 5.0, "buyers1h": 50, "sellers1h": 40, "age_d": 3.0,
                        "x_vs_call": 2.0, "from_peak_pct": -60, "pool": "P"}], "now")
        self.assertIn("| **alive** | X | $60k | 2.0x | -60% |", md)


if __name__ == "__main__":
    unittest.main()
