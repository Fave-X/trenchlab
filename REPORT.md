# TrenchLab report

Updated: 2026-11-20 04:20 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           104414
passed SCOUT         206
  killed by SCORE    29
  killed by AUDIT    42
FINAL PASS           135

top kill reasons at first sighting (a pool can have several):
  too_young                   102871
  few_unique_buyers            98465
  liquidity_low                96721
  volume_below_liquidity       73851
  sells_dominate               27459
  wash_churn                   21570
  overheated                    9174
  missing                       2927
  too_old                       1140
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 6251 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  135    -4.3%   -11.5%   -45.5%   -86.4%    56%
SCOUT PASS, killed later     71    +4.3%    +3.7%   -31.3%   -74.6%    51%
KILLED (tracked)          14274    +0.0%   -61.4%   -83.2%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     210    -94.8%    -68.9%    36%
too_old                        44     -0.6%     -0.4%    11%
wash_churn                     36    -23.3%    -85.6%    31%
liquidity_low                  30    -68.7%    -49.8%    53%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      7    -12.8%    -56.0%    57%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        56    -55.6%    -93.6%    70%
70-79      79    -47.4%    -67.6%    51%
60-69      50    -35.2%    -75.3%    46%
<60        21    -28.1%    -63.7%    43%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      727     -0.4%    -17.3%    -40.5%    31%
<15%      133     +0.6%    -11.7%    -32.5%    36%
15-30%     28     -1.0%     -1.0%     +0.4%    32%
30%+       32     -0.3%     -0.5%     +2.6%    19%
bundled     n   +1h med   +4h med  +24h med   rug%
none      659     -0.2%     -3.0%    -17.6%    27%
<20%      224     -6.0%    -59.6%    -93.2%    34%
20%+       37     +7.9%    -98.9%       -      78%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      878     -0.3%     -8.0%    -28.4%    29%
20-40%     26     -0.4%    -98.8%    -99.1%    73%
40%+       16    -97.5%    -98.6%       -      75%
tokens analysed: 784 | helius credits today: 1683/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  134    22%     -9.7%   -15.0%   -99.7%
   -6%     20%  134    24%    -10.1%   -15.5%   -99.7%
   -6%     30%  134    22%     -9.9%   -17.1%   -99.7%
  -10%     12%  134    26%     -9.2%   -18.4%   -99.7%
  -10%     20%  134    28%     -9.7%   -18.6%   -99.7%
  -10%     30%  134    27%     -9.4%   -18.9%   -99.7%
  -15%     12%  134    29%     -9.0%   -19.4%   -99.7%
  -15%     20%  134    32%     -9.4%   -20.3%   -99.7%
  -15%     30%  134    31%     -9.5%   -20.8%   -99.7%
  -25%     12%  134    32%    -11.8%   -20.0%   -99.7%
  -25%     20%  134    36%    -13.6%   -29.8%   -99.7%
  -25%     30%  134    34%    -13.9%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.0% per trade over n=134

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $350.90       $344.14
return                        -29.8%        -31.2%
closed trades                     85            68
win rate                         24%           21%
avg net / trade                -7.8%        -10.6%
expectancy $/trade            $-1.75        $-2.29
max drawdown                  -32.8%        -36.7%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $350.90 (-29.8%) | cash $333.36 | open 1 | max drawdown -32.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 85 | win 20/85 (24%) | avg net -7.8% | realized $-149.10 | expectancy $-1.75/trade
exits: stop 62, trail 23
  (n=85 < 100: noise, not evidence)
open:
  RUGGED       cost $17.54  now $17.54 (+0.0%)  held 0.0h
last trades:
  GTASZN       $18.78 -> $10.54 (-43.9%)  stop  0.2h
  FNDR         $18.36 -> $15.03 (-18.1%)  stop  0.2h
  DCTC         $18.20 -> $7.75 (-57.4%)  stop  0.2h
  WhatUp       $18.20 -> $15.50 (-14.8%)  stop  0.2h
  OGTA         $18.12 -> $13.76 (-24.0%)  stop  0.2h
  FIONA        $17.54 -> $31.83 (+81.5%)  trail  0.8h
  AI           $18.04 -> $10.08 (-44.1%)  stop  0.2h
  iAgent       $18.04 -> $16.18 (-10.3%)  stop  0.5h
signals skipped by the sizer/risk rules: already_traded_token 484, daily_loss_limit 310, cooldown_after_loss 17, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $344.14 (-31.2%) | cash $344.14 | open 0 | max drawdown -36.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 68 | win 14/68 (21%) | avg net -10.6% | realized $-155.86 | expectancy $-2.29/trade
exits: stop 53, trail 15
  (n=68 < 100: noise, not evidence)
last trades:
  FNDR         $18.45 -> $17.76 (-3.7%)  trail  0.3h
  DCTC         $18.41 -> $7.70 (-58.2%)  stop  0.3h
  GTASZN       $17.88 -> $15.38 (-14.0%)  stop  0.7h
  AI           $17.75 -> $14.69 (-17.2%)  stop  0.2h
  FIONA        $17.75 -> $13.13 (-26.0%)  stop  0.3h
  OGTA         $17.37 -> $14.24 (-18.0%)  stop  0.5h
  iAgent       $17.21 -> $15.17 (-11.8%)  stop  0.5h
  RUGGED       $17.21 -> $19.12 (+11.1%)  trail  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 127, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 46, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 29, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
