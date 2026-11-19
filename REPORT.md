# TrenchLab report

Updated: 2026-11-19 06:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           97886
passed SCOUT         191
  killed by SCORE    27
  killed by AUDIT    40
FINAL PASS           124

top kill reasons at first sighting (a pool can have several):
  too_young                    96406
  few_unique_buyers            92378
  liquidity_low                90715
  volume_below_liquidity       69269
  sells_dominate               25727
  wash_churn                   20184
  overheated                    8547
  missing                       2796
  too_old                       1104
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5849 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  124    -4.3%    -8.2%   -44.4%   -86.4%    56%
SCOUT PASS, killed later     67    +4.3%    +3.7%   -31.7%   -74.6%    49%
KILLED (tracked)          13350    +0.0%   -59.7%   -82.8%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     155    -94.9%    -68.9%    45%
too_old                        41     -0.6%     -0.4%     7%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  26    -72.2%    -49.8%    58%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    74%
70-79      72    -37.8%    -67.6%    47%
60-69      46    -35.2%    -75.3%    46%
<60        20    -31.3%    -63.7%    40%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      651     -0.4%    -17.3%    -40.5%    33%
<15%      120     +0.4%    -11.2%    -32.5%    35%
15-30%     25     -0.9%     -1.3%     +1.0%    24%
30%+       25     -0.5%     -0.6%     +2.6%    16%
bundled     n   +1h med   +4h med  +24h med   rug%
none      605     -0.2%     -2.9%    -16.0%    28%
<20%      186     -7.8%    -60.8%    -93.2%    40%
20%+       30     +6.1%    -98.8%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      784     -0.3%     -8.6%    -31.1%    30%
20-40%     24     -0.4%    -98.8%    -99.1%    71%
40%+       13    -96.5%    -97.5%       -      77%
tokens analysed: 693 | helius credits today: 2491/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  124    24%     -8.9%   -15.0%   -99.7%
   -6%     20%  124    25%     -9.3%   -15.5%   -99.7%
   -6%     30%  124    23%     -9.2%   -17.1%   -99.7%
  -10%     12%  124    27%     -9.2%   -18.4%   -99.7%
  -10%     20%  124    27%     -9.8%   -18.7%   -99.7%
  -10%     30%  124    27%     -9.5%   -19.1%   -99.7%
  -15%     12%  124    29%     -9.4%   -19.4%   -99.7%
  -15%     20%  124    31%    -10.0%   -20.4%   -99.7%
  -15%     30%  124    30%    -10.0%   -21.0%   -99.7%
  -25%     12%  124    32%    -12.2%   -19.6%   -99.7%
  -25%     20%  124    35%    -14.4%   -29.9%   -99.7%
  -25%     30%  124    33%    -14.5%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.9% per trade over n=124

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $350.79       $357.58
return                        -29.8%        -28.5%
closed trades                     81            62
win rate                         23%           21%
avg net / trade                -8.2%        -10.4%
expectancy $/trade            $-1.84        $-2.30
max drawdown                  -32.5%        -34.2%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $350.79 (-29.8%) | cash $350.79 | open 0 | max drawdown -32.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 81 | win 19/81 (23%) | avg net -8.2% | realized $-149.21 | expectancy $-1.84/trade
exits: stop 59, trail 22
  (n=81 < 100: noise, not evidence)
last trades:
  SHIT         $17.85 -> $19.44 (+8.9%)  trail  3.7h
  Apocrycoin   $17.83 -> $39.70 (+122.7%)  trail  0.7h
  DCTY         $18.92 -> $15.61 (-17.5%)  stop  0.3h
  DCTY         $18.92 -> $19.28 (+1.9%)  trail  1.3h
  GTASZN       $18.78 -> $10.54 (-43.9%)  stop  0.2h
  FNDR         $18.36 -> $15.03 (-18.1%)  stop  0.2h
  DCTC         $18.20 -> $7.75 (-57.4%)  stop  0.2h
  WhatUp       $18.20 -> $15.50 (-14.8%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 468, daily_loss_limit 251, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $357.58 (-28.5%) | cash $357.58 | open 0 | max drawdown -34.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 62 | win 13/62 (21%) | avg net -10.4% | realized $-142.42 | expectancy $-2.30/trade
exits: stop 48, trail 14
  (n=62 < 100: noise, not evidence)
last trades:
  JALU         $19.48 -> $17.45 (-10.4%)  stop  0.8h
  NVIDIANS     $19.38 -> $12.07 (-37.7%)  stop  0.3h
  KATIA        $19.01 -> $20.77 (+9.3%)  trail  1.8h
  ANT          $19.10 -> $16.29 (-14.7%)  stop  0.8h
  Apocrycoin   $18.96 -> $12.29 (-35.2%)  stop  0.3h
  NASDUCK      $18.63 -> $15.05 (-19.2%)  stop  0.2h
  FNDR         $18.45 -> $17.76 (-3.7%)  trail  0.3h
  DCTC         $18.41 -> $7.70 (-58.2%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 224, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 115, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 22, setup_rejected:operator_cluster 21, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
