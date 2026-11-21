# TrenchLab report

Updated: 2026-11-21 21:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           116550
passed SCOUT         222
  killed by SCORE    33
  killed by AUDIT    47
FINAL PASS           142

top kill reasons at first sighting (a pool can have several):
  too_young                   114896
  few_unique_buyers           109763
  liquidity_low               107954
  volume_below_liquidity       82153
  sells_dominate               30783
  wash_churn                   24527
  overheated                   10436
  missing                       3191
  too_old                       1211
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 7040 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  142    -5.3%   -12.5%   -45.2%   -88.1%    58%
SCOUT PASS, killed later     80    +4.3%    +4.2%   -30.1%   -63.7%    51%
KILLED (tracked)          16031    +0.0%   -61.8%   -84.8%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     282    -95.0%    -68.9%    29%
wash_churn                     49    -23.3%    -85.6%    27%
too_old                        46     -0.6%     -0.4%    11%
liquidity_low                  31    -69.3%    -49.8%    61%
overheated                      9     -3.6%    -56.0%    44%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        59    -55.3%    -93.4%    68%
70-79      83    -52.3%    -72.2%    53%
60-69      55    -34.6%    -92.5%    53%
<60        25     -7.4%    -52.9%    44%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      849     -0.2%    -12.0%    -43.5%    28%
<15%      167     +0.6%    -13.1%    -32.7%    35%
15-30%     35     -1.8%     -2.4%     +0.4%    34%
30%+       32     -0.5%     -0.7%     +1.9%    28%
bundled     n   +1h med   +4h med  +24h med   rug%
none      749     -0.1%     -2.7%    -25.7%    26%
<20%      285     -3.8%    -58.3%    -92.8%    30%
20%+       49     -0.5%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1033     -0.1%     -7.4%    -33.1%    27%
20-40%     33     -4.5%    -99.0%    -99.1%    76%
40%+       17    -98.5%    -98.6%       -      82%
tokens analysed: 933 | helius credits today: 6723/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  142    21%    -10.1%   -15.0%   -99.7%
   -6%     20%  142    23%    -10.4%   -15.5%   -99.7%
   -6%     30%  142    20%    -10.4%   -17.1%   -99.7%
  -10%     12%  142    25%    -10.0%   -18.6%   -99.7%
  -10%     20%  142    26%    -10.5%   -18.7%   -99.7%
  -10%     30%  142    25%    -10.1%   -19.1%   -99.7%
  -15%     12%  142    28%     -9.7%   -19.8%   -99.7%
  -15%     20%  142    31%    -10.1%   -20.4%   -99.7%
  -15%     30%  142    29%    -10.0%   -21.0%   -99.7%
  -25%     12%  142    32%    -12.3%   -24.6%   -99.7%
  -25%     20%  142    35%    -14.0%   -29.9%   -99.7%
  -25%     30%  142    33%    -14.1%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.7% per trade over n=142

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $323.55       $349.92
return                        -35.3%        -30.0%
closed trades                     93            77
win rate                         22%           22%
avg net / trade                -8.9%         -8.9%
expectancy $/trade            $-1.90        $-1.95
max drawdown                  -37.7%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $323.55 (-35.3%) | cash $323.55 | open 0 | max drawdown -37.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 93 | win 20/93 (22%) | avg net -8.9% | realized $-176.45 | expectancy $-1.90/trade
exits: stop 70, trail 23
  (n=93 < 100: noise, not evidence)
last trades:
  RUGGED       $17.54 -> $10.00 (-43.0%)  stop  0.5h
  AMC          $17.17 -> $13.19 (-23.2%)  stop  0.2h
  RUDY         $16.97 -> $15.02 (-11.5%)  stop  0.2h
  Trader       $16.87 -> $13.30 (-21.2%)  stop  0.2h
  PUNANI       $16.69 -> $14.71 (-11.9%)  stop  0.3h
  XV           $16.69 -> $14.12 (-15.4%)  stop  0.2h
  Bigfoot      $16.46 -> $12.98 (-21.2%)  stop  0.2h
  HOUSE        $16.29 -> $14.03 (-13.9%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 520, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $349.92 (-30.0%) | cash $349.92 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 77 | win 17/77 (22%) | avg net -8.9% | realized $-150.08 | expectancy $-1.95/trade
exits: stop 59, trail 18
  (n=77 < 100: noise, not evidence)
last trades:
  HNYDRIP      $17.12 -> $38.11 (+122.6%)  trail  0.7h
  AMC          $18.09 -> $15.90 (-12.1%)  stop  0.2h
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:dumping_now 137, setup_rejected:sellers_dominate_now 133, setup_rejected:b_bundled 69, setup_rejected:volume_dried_up 47, setup_rejected:operator_cluster 36, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 23, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 15, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
