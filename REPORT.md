# TrenchLab report

Updated: 2026-11-19 23:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           102965
passed SCOUT         200
  killed by SCORE    30
  killed by AUDIT    41
FINAL PASS           129

top kill reasons at first sighting (a pool can have several):
  too_young                   101433
  few_unique_buyers            97121
  liquidity_low                95409
  volume_below_liquidity       72850
  sells_dominate               27095
  wash_churn                   21256
  overheated                    9032
  missing                       2879
  too_old                       1136
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 6146 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  129    -4.4%   -11.7%   -45.0%   -85.9%    58%
SCOUT PASS, killed later     71    +4.3%    +3.7%   -30.1%   -74.6%    49%
KILLED (tracked)          14070    +0.0%   -60.2%   -82.8%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     197    -94.8%    -68.9%    37%
too_old                        44     -0.6%     -0.4%    11%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  29    -69.3%    -49.8%    55%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        55    -55.6%    -93.6%    71%
70-79      77    -43.9%    -67.4%    51%
60-69      46    -35.2%    -75.3%    50%
<60        22    -28.1%    -63.7%    41%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      707     -0.4%    -16.4%    -39.2%    32%
<15%      129     +0.3%    -11.2%    -32.5%    36%
15-30%     28     -1.0%     -1.0%     +0.4%    32%
30%+       31     -0.3%     -0.5%     +2.6%    16%
bundled     n   +1h med   +4h med  +24h med   rug%
none      647     -0.2%     -2.9%    -16.6%    28%
<20%      214     -7.8%    -58.5%    -93.2%    36%
20%+       34     +6.1%    -98.8%       -      79%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      854     -0.3%     -7.5%    -25.7%    30%
20-40%     26     -0.4%    -98.7%    -99.1%    73%
40%+       15    -96.5%    -98.6%       -      73%
tokens analysed: 759 | helius credits today: 7918/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  129    23%     -9.4%   -15.1%   -99.7%
   -6%     20%  129    24%     -9.8%   -15.9%   -99.7%
   -6%     30%  129    22%     -9.6%   -17.1%   -99.7%
  -10%     12%  129    26%     -9.7%   -18.6%   -99.7%
  -10%     20%  129    26%    -10.2%   -18.6%   -99.7%
  -10%     30%  129    26%    -10.0%   -19.0%   -99.7%
  -15%     12%  129    29%     -9.5%   -19.5%   -99.7%
  -15%     20%  129    31%     -9.9%   -20.4%   -99.7%
  -15%     30%  129    29%    -10.0%   -21.0%   -99.7%
  -25%     12%  129    32%    -12.3%   -21.3%   -99.7%
  -25%     20%  129    35%    -14.3%   -29.9%   -99.7%
  -25%     30%  129    33%    -14.6%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -9.4% per trade over n=129

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
signals skipped by the sizer/risk rules: already_traded_token 473, daily_loss_limit 310, cooldown_after_loss 15, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 123, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 29, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
