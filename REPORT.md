# TrenchLab report

Updated: 2026-11-22 12:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           121390
passed SCOUT         237
  killed by SCORE    34
  killed by AUDIT    57
FINAL PASS           146

top kill reasons at first sighting (a pool can have several):
  too_young                   119707
  few_unique_buyers           114280
  liquidity_low               112421
  volume_below_liquidity       85562
  sells_dominate               32081
  wash_churn                   25626
  overheated                   10874
  missing                       3293
  too_old                       1228
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 7302 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  146    -5.0%   -13.2%   -44.0%   -87.5%    59%
SCOUT PASS, killed later     91    +5.4%   +10.7%   -28.1%   -74.6%    47%
KILLED (tracked)          16747    +0.1%   -59.7%   -84.6%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     314    -95.9%    -68.9%    28%
wash_churn                     53     -1.2%    -85.6%    26%
too_old                        46     -0.6%     -0.4%    11%
liquidity_low                  33    -69.9%    -49.8%    61%
overheated                      9     -3.6%    -56.0%    44%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        64    -55.0%    -93.3%    62%
70-79      91    -50.1%    -71.8%    48%
60-69      57    -35.2%    -93.0%    58%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      899     -0.0%    -12.5%    -45.5%    28%
<15%      190     +0.7%    -12.6%    -32.7%    35%
15-30%     38     -1.2%     -2.7%     +0.4%    34%
30%+       33     -0.5%     -0.7%     +1.9%    30%
bundled     n   +1h med   +4h med  +24h med   rug%
none      786     -0.0%     -2.7%    -31.6%    26%
<20%      321     -0.2%    -58.3%    -92.9%    30%
20%+       53     +4.3%    -99.0%       -      79%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1108     +0.0%     -7.4%    -38.9%    27%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       18    -97.5%    -98.6%       -      78%
tokens analysed: 1005 | helius credits today: 4853/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  146    22%     -9.7%   -14.7%   -99.7%
   -6%     20%  146    23%    -10.1%   -14.9%   -99.7%
   -6%     30%  146    21%    -10.0%   -16.7%   -99.7%
  -10%     12%  146    25%     -9.6%   -18.0%   -99.7%
  -10%     20%  146    27%    -10.1%   -18.6%   -99.7%
  -10%     30%  146    25%     -9.9%   -18.9%   -99.7%
  -15%     12%  146    29%     -9.4%   -19.6%   -99.7%
  -15%     20%  146    32%     -9.8%   -20.4%   -99.7%
  -15%     30%  146    29%     -9.9%   -21.0%   -99.7%
  -25%     12%  146    32%    -12.0%   -20.0%   -99.7%
  -25%     20%  146    36%    -13.7%   -29.8%   -99.7%
  -25%     30%  146    34%    -13.9%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.4% per trade over n=146

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $326.41       $347.47
return                        -34.7%        -30.5%
closed trades                     96            78
win rate                         23%           22%
avg net / trade                -8.3%         -8.9%
expectancy $/trade            $-1.79        $-1.95
max drawdown                  -37.7%        -37.3%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $326.41 (-34.7%) | cash $311.32 | open 1 | max drawdown -37.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 96 | win 22/96 (23%) | avg net -8.3% | realized $-172.29 | expectancy $-1.79/trade
exits: stop 70, trail 26
  (n=96 < 100: noise, not evidence)
open:
  UCASH        cost $16.39  now $15.08 (-8.0%)  held 0.5h
last trades:
  Trader       $16.87 -> $13.30 (-21.2%)  stop  0.2h
  PUNANI       $16.69 -> $14.71 (-11.9%)  stop  0.3h
  XV           $16.69 -> $14.12 (-15.4%)  stop  0.2h
  Bigfoot      $16.46 -> $12.98 (-21.2%)  stop  0.2h
  HOUSE        $16.29 -> $14.03 (-13.9%)  stop  0.2h
  SIDOOR       $16.18 -> $17.90 (+10.6%)  trail  0.7h
  STREETS      $16.26 -> $19.94 (+22.7%)  trail  1.0h
  snowball     $16.45 -> $15.21 (-7.5%)  trail  0.3h
signals skipped by the sizer/risk rules: already_traded_token 535, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $347.47 (-30.5%) | cash $330.70 | open 1 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 78 | win 17/78 (22%) | avg net -8.9% | realized $-151.89 | expectancy $-1.95/trade
exits: stop 60, trail 18
  (n=78 < 100: noise, not evidence)
open:
  SIDOOR       cost $17.41  now $16.77 (-3.7%)  held 0.2h
last trades:
  AMC          $18.09 -> $15.90 (-12.1%)  stop  0.2h
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 424, daily_loss_limit 239, setup_rejected:dumping_now 140, setup_rejected:sellers_dominate_now 134, setup_rejected:b_bundled 69, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:clustered_supply 28, setup_rejected:bundled_buys 23, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
