# TrenchLab report

Updated: 2026-11-19 16:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           100797
passed SCOUT         193
  killed by SCORE    27
  killed by AUDIT    41
FINAL PASS           125

top kill reasons at first sighting (a pool can have several):
  too_young                    99297
  few_unique_buyers            95090
  liquidity_low                93422
  volume_below_liquidity       71345
  sells_dominate               26464
  wash_churn                   20858
  overheated                    8853
  missing                       2813
  too_old                       1116
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 6054 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  125    -4.4%    -9.9%   -44.7%   -86.4%    56%
SCOUT PASS, killed later     68    +4.3%    +3.9%   -31.3%   -74.6%    50%
KILLED (tracked)          13815    +0.0%   -59.3%   -82.9%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     177    -94.8%    -68.9%    40%
too_old                        41     -0.6%     -0.4%     7%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  27    -69.9%    -49.8%    56%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        54    -58.0%    -93.6%    72%
70-79      73    -39.9%    -67.6%    48%
60-69      46    -35.2%    -75.3%    46%
<60        20    -29.7%    -63.7%    45%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      681     -0.3%    -16.7%    -39.2%    32%
<15%      124     +0.4%    -11.2%    -32.5%    34%
15-30%     26     -0.7%     -0.7%     +1.0%    27%
30%+       25     -0.5%     -0.6%     +2.6%    16%
bundled     n   +1h med   +4h med  +24h med   rug%
none      623     -0.2%     -3.0%    -15.5%    27%
<20%      202     -6.0%    -58.5%    -93.2%    37%
20%+       31     +7.9%    -98.8%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      818     -0.3%     -8.5%    -25.7%    30%
20-40%     25     -0.1%    -98.7%    -99.1%    68%
40%+       13    -96.5%    -98.5%       -      77%
tokens analysed: 726 | helius credits today: 5315/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  125    24%     -8.9%   -14.9%   -99.7%
   -6%     20%  125    25%     -9.4%   -15.1%   -99.7%
   -6%     30%  125    23%     -9.2%   -17.1%   -99.7%
  -10%     12%  125    26%     -9.2%   -18.2%   -99.7%
  -10%     20%  125    27%     -9.8%   -18.6%   -99.7%
  -10%     30%  125    26%     -9.5%   -19.0%   -99.7%
  -15%     12%  125    30%     -9.0%   -19.5%   -99.7%
  -15%     20%  125    31%     -9.6%   -20.4%   -99.7%
  -15%     30%  125    30%     -9.6%   -21.0%   -99.7%
  -25%     12%  125    33%    -11.8%   -21.3%   -99.7%
  -25%     20%  125    35%    -14.0%   -29.9%   -99.7%
  -25%     30%  125    34%    -14.0%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.9% per trade over n=125

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $350.79       $355.08
return                        -29.8%        -29.0%
closed trades                     81            63
win rate                         23%           21%
avg net / trade                -8.2%        -10.5%
expectancy $/trade            $-1.84        $-2.30
max drawdown                  -32.5%        -34.7%
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
signals skipped by the sizer/risk rules: already_traded_token 473, daily_loss_limit 256, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $355.08 (-29.0%) | cash $355.08 | open 0 | max drawdown -34.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 63 | win 13/63 (21%) | avg net -10.5% | realized $-144.92 | expectancy $-2.30/trade
exits: stop 49, trail 14
  (n=63 < 100: noise, not evidence)
last trades:
  NVIDIANS     $19.38 -> $12.07 (-37.7%)  stop  0.3h
  KATIA        $19.01 -> $20.77 (+9.3%)  trail  1.8h
  ANT          $19.10 -> $16.29 (-14.7%)  stop  0.8h
  Apocrycoin   $18.96 -> $12.29 (-35.2%)  stop  0.3h
  NASDUCK      $18.63 -> $15.05 (-19.2%)  stop  0.2h
  FNDR         $18.45 -> $17.76 (-3.7%)  trail  0.3h
  DCTC         $18.41 -> $7.70 (-58.2%)  stop  0.3h
  GTASZN       $17.88 -> $15.38 (-14.0%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 231, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 122, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 28, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
