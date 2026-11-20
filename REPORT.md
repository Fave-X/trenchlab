# TrenchLab report

Updated: 2026-11-20 10:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           106469
passed SCOUT         207
  killed by SCORE    30
  killed by AUDIT    42
FINAL PASS           135

top kill reasons at first sighting (a pool can have several):
  too_young                   104912
  few_unique_buyers           100325
  liquidity_low                98592
  volume_below_liquidity       75230
  sells_dominate               27993
  wash_churn                   22072
  overheated                    9408
  missing                       2942
  too_old                       1149
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 6376 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  135    -4.4%   -11.7%   -45.0%   -86.5%    57%
SCOUT PASS, killed later     72    +4.7%    +3.9%   -31.7%   -74.6%    50%
KILLED (tracked)          14642    +0.0%   -62.2%   -83.9%    +0.4%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     227    -94.8%    -68.9%    33%
too_old                        45     -0.6%     -0.4%    11%
wash_churn                     37    -23.3%    -85.6%    32%
liquidity_low                  30    -69.3%    -49.8%    60%
overheated                      8     -3.6%    -56.0%    50%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        56    -55.3%    -93.6%    70%
70-79      79    -47.4%    -67.6%    52%
60-69      50    -35.2%    -86.0%    48%
<60        22    -28.1%    -63.7%    41%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      759     -0.3%    -15.6%    -39.9%    30%
<15%      136     +0.7%    -11.2%    -32.7%    36%
15-30%     28     -1.0%     -1.0%     +0.4%    32%
30%+       32     -0.3%     -0.5%     +2.6%    19%
bundled     n   +1h med   +4h med  +24h med   rug%
none      683     -0.2%     -2.9%    -20.2%    27%
<20%      234     -6.0%    -58.4%    -93.2%    33%
20%+       38     +7.9%    -98.9%       -      79%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      913     -0.2%     -7.4%    -31.6%    29%
20-40%     26     -0.4%    -98.8%    -99.1%    73%
40%+       16    -97.5%    -98.6%       -      75%
tokens analysed: 816 | helius credits today: 4067/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  135    22%     -9.7%   -14.9%   -99.7%
   -6%     20%  135    24%    -10.1%   -15.1%   -99.7%
   -6%     30%  135    21%    -10.0%   -17.1%   -99.7%
  -10%     12%  135    26%     -9.5%   -18.6%   -99.7%
  -10%     20%  135    27%    -10.0%   -18.6%   -99.7%
  -10%     30%  135    25%     -9.9%   -19.0%   -99.7%
  -15%     12%  135    29%     -9.3%   -19.5%   -99.7%
  -15%     20%  135    32%     -9.7%   -20.4%   -99.7%
  -15%     30%  135    29%    -10.0%   -21.0%   -99.7%
  -25%     12%  135    32%    -12.0%   -21.3%   -99.7%
  -25%     20%  135    36%    -13.9%   -29.9%   -99.7%
  -25%     30%  135    33%    -14.4%   -31.0%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.3% per trade over n=135

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $343.35       $361.76
return                        -31.3%        -27.6%
closed trades                     86            70
win rate                         23%           21%
avg net / trade                -8.2%         -8.8%
expectancy $/trade            $-1.82        $-1.97
max drawdown                  -33.9%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $343.35 (-31.3%) | cash $343.35 | open 0 | max drawdown -33.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 86 | win 20/86 (23%) | avg net -8.2% | realized $-156.65 | expectancy $-1.82/trade
exits: stop 63, trail 23
  (n=86 < 100: noise, not evidence)
last trades:
  FNDR         $18.36 -> $15.03 (-18.1%)  stop  0.2h
  DCTC         $18.20 -> $7.75 (-57.4%)  stop  0.2h
  WhatUp       $18.20 -> $15.50 (-14.8%)  stop  0.2h
  OGTA         $18.12 -> $13.76 (-24.0%)  stop  0.2h
  FIONA        $17.54 -> $31.83 (+81.5%)  trail  0.8h
  AI           $18.04 -> $10.08 (-44.1%)  stop  0.2h
  iAgent       $18.04 -> $16.18 (-10.3%)  stop  0.5h
  RUGGED       $17.54 -> $10.00 (-43.0%)  stop  0.5h
signals skipped by the sizer/risk rules: already_traded_token 495, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $361.76 (-27.6%) | cash $361.76 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 70 | win 15/70 (21%) | avg net -8.8% | realized $-138.24 | expectancy $-1.97/trade
exits: stop 54, trail 16
  (n=70 < 100: noise, not evidence)
last trades:
  GTASZN       $17.88 -> $15.38 (-14.0%)  stop  0.7h
  AI           $17.75 -> $14.69 (-17.2%)  stop  0.2h
  FIONA        $17.75 -> $13.13 (-26.0%)  stop  0.3h
  OGTA         $17.37 -> $14.24 (-18.0%)  stop  0.5h
  iAgent       $17.21 -> $15.17 (-11.8%)  stop  0.5h
  RUGGED       $17.21 -> $19.12 (+11.1%)  trail  0.3h
  CATMARIO     $17.21 -> $13.84 (-19.6%)  stop  0.5h
  HNYDRIP      $17.12 -> $38.11 (+122.6%)  trail  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 127, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 29, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
