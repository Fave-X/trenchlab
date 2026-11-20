# TrenchLab report

Updated: 2026-11-20 02:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           103896
passed SCOUT         204
  killed by SCORE    29
  killed by AUDIT    42
FINAL PASS           133

top kill reasons at first sighting (a pool can have several):
  too_young                   102356
  few_unique_buyers            97997
  liquidity_low                96263
  volume_below_liquidity       73485
  sells_dominate               27355
  wash_churn                   21478
  overheated                    9122
  missing                       2909
  too_old                       1139
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 6205 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  133    -4.4%   -11.7%   -45.5%   -86.4%    56%
SCOUT PASS, killed later     71    +4.3%    +3.7%   -31.3%   -74.6%    49%
KILLED (tracked)          14183    +0.0%   -61.0%   -83.0%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     204    -94.8%    -68.9%    37%
too_old                        44     -0.6%     -0.4%    11%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  30    -68.7%    -49.8%    53%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      7    -12.8%    -56.0%    57%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        56    -55.6%    -93.6%    70%
70-79      79    -47.4%    -67.6%    49%
60-69      48    -35.2%    -75.3%    48%
<60        21    -28.1%    -63.7%    43%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      719     -0.4%    -16.7%    -40.5%    31%
<15%      131     +0.4%    -11.7%    -32.5%    35%
15-30%     28     -1.0%     -1.0%     +0.4%    32%
30%+       32     -0.3%     -0.5%     +2.6%    19%
bundled     n   +1h med   +4h med  +24h med   rug%
none      656     -0.2%     -2.9%    -17.6%    27%
<20%      218     -6.9%    -59.6%    -93.2%    35%
20%+       36     +6.1%    -98.8%       -      78%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      868     -0.3%     -7.6%    -28.4%    29%
20-40%     26     -0.4%    -98.8%    -99.1%    73%
40%+       16    -97.5%    -98.5%       -      75%
tokens analysed: 774 | helius credits today: 1017/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  132    23%     -9.8%   -15.5%   -99.7%
   -6%     20%  132    23%    -10.2%   -16.5%   -99.7%
   -6%     30%  132    22%    -10.0%   -17.3%   -99.7%
  -10%     12%  132    26%     -9.4%   -18.6%   -99.7%
  -10%     20%  132    27%     -9.9%   -18.7%   -99.7%
  -10%     30%  132    26%     -9.7%   -19.1%   -99.7%
  -15%     12%  132    29%     -9.2%   -19.6%   -99.7%
  -15%     20%  132    31%     -9.6%   -20.4%   -99.7%
  -15%     30%  132    30%     -9.7%   -21.0%   -99.7%
  -25%     12%  132    32%    -12.0%   -24.6%   -99.7%
  -25%     20%  132    35%    -13.9%   -29.9%   -99.7%
  -25%     30%  132    33%    -14.2%   -31.0%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.2% per trade over n=132

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $352.76       $344.28
return                        -29.4%        -31.1%
closed trades                     84            66
win rate                         24%           20%
avg net / trade                -7.8%        -10.9%
expectancy $/trade            $-1.75        $-2.36
max drawdown                  -32.8%        -36.7%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $352.76 (-29.4%) | cash $334.72 | open 1 | max drawdown -32.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 84 | win 20/84 (24%) | avg net -7.8% | realized $-147.24 | expectancy $-1.75/trade
exits: stop 61, trail 23
  (n=84 < 100: noise, not evidence)
open:
  iAgent       cost $18.04  now $18.04 (+0.0%)  held 0.0h
last trades:
  DCTY         $18.92 -> $19.28 (+1.9%)  trail  1.3h
  GTASZN       $18.78 -> $10.54 (-43.9%)  stop  0.2h
  FNDR         $18.36 -> $15.03 (-18.1%)  stop  0.2h
  DCTC         $18.20 -> $7.75 (-57.4%)  stop  0.2h
  WhatUp       $18.20 -> $15.50 (-14.8%)  stop  0.2h
  OGTA         $18.12 -> $13.76 (-24.0%)  stop  0.2h
  FIONA        $17.54 -> $31.83 (+81.5%)  trail  0.8h
  AI           $18.04 -> $10.08 (-44.1%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 479, daily_loss_limit 310, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $344.28 (-31.1%) | cash $344.28 | open 0 | max drawdown -36.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 66 | win 13/66 (20%) | avg net -10.9% | realized $-155.72 | expectancy $-2.36/trade
exits: stop 52, trail 14
  (n=66 < 100: noise, not evidence)
last trades:
  Apocrycoin   $18.96 -> $12.29 (-35.2%)  stop  0.3h
  NASDUCK      $18.63 -> $15.05 (-19.2%)  stop  0.2h
  FNDR         $18.45 -> $17.76 (-3.7%)  trail  0.3h
  DCTC         $18.41 -> $7.70 (-58.2%)  stop  0.3h
  GTASZN       $17.88 -> $15.38 (-14.0%)  stop  0.7h
  AI           $17.75 -> $14.69 (-17.2%)  stop  0.2h
  FIONA        $17.75 -> $13.13 (-26.0%)  stop  0.3h
  OGTA         $17.37 -> $14.24 (-18.0%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 125, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 29, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
