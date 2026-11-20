# TrenchLab report

Updated: 2026-11-20 01:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           103630
passed SCOUT         201
  killed by SCORE    29
  killed by AUDIT    41
FINAL PASS           131

top kill reasons at first sighting (a pool can have several):
  too_young                   102093
  few_unique_buyers            97747
  liquidity_low                96024
  volume_below_liquidity       73303
  sells_dominate               27287
  wash_churn                   21410
  overheated                    9097
  missing                       2896
  too_old                       1137
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 6190 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  131    -4.4%   -11.7%   -45.5%   -86.4%    57%
SCOUT PASS, killed later     70    +4.3%    +3.4%   -31.3%   -74.6%    50%
KILLED (tracked)          14150    +0.0%   -60.8%   -82.9%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     200    -94.8%    -68.9%    37%
too_old                        44     -0.6%     -0.4%    11%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  30    -69.3%    -49.8%    53%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      7    -12.8%    -56.0%    57%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        55    -55.6%    -93.6%    71%
70-79      78    -47.4%    -67.6%    50%
60-69      47    -35.2%    -75.3%    49%
<60        21    -28.1%    -63.7%    43%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      713     -0.4%    -16.7%    -40.5%    31%
<15%      131     +0.3%    -11.7%    -32.5%    35%
15-30%     28     -1.0%     -1.0%     +0.4%    32%
30%+       32     -0.3%     -0.5%     +2.6%    19%
bundled     n   +1h med   +4h med  +24h med   rug%
none      652     -0.2%     -2.9%    -17.6%    27%
<20%      216     -7.8%    -59.6%    -93.2%    36%
20%+       36     +4.3%    -98.8%       -      78%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      862     -0.3%     -7.6%    -28.4%    29%
20-40%     26     -0.4%    -98.8%    -99.1%    73%
40%+       16    -97.5%    -98.5%       -      75%
tokens analysed: 768 | helius credits today: 445/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  131    23%     -9.5%   -15.1%   -99.7%
   -6%     20%  131    24%     -9.9%   -15.9%   -99.7%
   -6%     30%  131    22%     -9.8%   -17.1%   -99.7%
  -10%     12%  131    26%     -9.1%   -18.6%   -99.7%
  -10%     20%  131    27%     -9.6%   -18.6%   -99.7%
  -10%     30%  131    26%     -9.4%   -19.0%   -99.7%
  -15%     12%  131    29%     -8.9%   -19.5%   -99.7%
  -15%     20%  131    31%     -9.3%   -20.4%   -99.7%
  -15%     30%  131    30%     -9.5%   -21.0%   -99.7%
  -25%     12%  131    32%    -11.7%   -21.3%   -99.7%
  -25%     20%  131    35%    -13.7%   -29.9%   -99.7%
  -25%     30%  131    34%    -14.0%   -31.0%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -8.9% per trade over n=131

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $360.72       $346.25
return                        -27.9%        -30.7%
closed trades                     83            65
win rate                         24%           20%
avg net / trade                -7.3%        -10.8%
expectancy $/trade            $-1.68        $-2.35
max drawdown                  -32.8%        -36.3%
open now                           0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $360.72 (-27.9%) | cash $360.72 | open 0 | max drawdown -32.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 83 | win 20/83 (24%) | avg net -7.3% | realized $-139.28 | expectancy $-1.68/trade
exits: stop 60, trail 23
  (n=83 < 100: noise, not evidence)
last trades:
  DCTY         $18.92 -> $15.61 (-17.5%)  stop  0.3h
  DCTY         $18.92 -> $19.28 (+1.9%)  trail  1.3h
  GTASZN       $18.78 -> $10.54 (-43.9%)  stop  0.2h
  FNDR         $18.36 -> $15.03 (-18.1%)  stop  0.2h
  DCTC         $18.20 -> $7.75 (-57.4%)  stop  0.2h
  WhatUp       $18.20 -> $15.50 (-14.8%)  stop  0.2h
  OGTA         $18.12 -> $13.76 (-24.0%)  stop  0.2h
  FIONA        $17.54 -> $31.83 (+81.5%)  trail  0.8h
signals skipped by the sizer/risk rules: already_traded_token 476, daily_loss_limit 310, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $346.25 (-30.7%) | cash $330.04 | open 1 | max drawdown -36.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 65 | win 13/65 (20%) | avg net -10.8% | realized $-152.59 | expectancy $-2.35/trade
exits: stop 51, trail 14
  (n=65 < 100: noise, not evidence)
open:
  OGTA         cost $17.37  now $16.22 (-6.6%)  held 0.4h
last trades:
  ANT          $19.10 -> $16.29 (-14.7%)  stop  0.8h
  Apocrycoin   $18.96 -> $12.29 (-35.2%)  stop  0.3h
  NASDUCK      $18.63 -> $15.05 (-19.2%)  stop  0.2h
  FNDR         $18.45 -> $17.76 (-3.7%)  trail  0.3h
  DCTC         $18.41 -> $7.70 (-58.2%)  stop  0.3h
  GTASZN       $17.88 -> $15.38 (-14.0%)  stop  0.7h
  AI           $17.75 -> $14.69 (-17.2%)  stop  0.2h
  FIONA        $17.75 -> $13.13 (-26.0%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 125, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 29, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
