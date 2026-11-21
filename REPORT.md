# TrenchLab report

Updated: 2026-11-21 06:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           112308
passed SCOUT         216
  killed by SCORE    33
  killed by AUDIT    45
FINAL PASS           138

top kill reasons at first sighting (a pool can have several):
  too_young                   110705
  few_unique_buyers           105783
  liquidity_low               104020
  volume_below_liquidity       79260
  sells_dominate               29668
  wash_churn                   23574
  overheated                   10003
  missing                       3093
  too_old                       1172
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 6752 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  138    -5.2%   -11.5%   -45.2%   -87.5%    60%
SCOUT PASS, killed later     78    +4.3%    +3.7%   -31.7%   -74.6%    51%
KILLED (tracked)          15417    +0.0%   -62.3%   -84.7%    +0.1%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     260    -95.5%    -68.9%    32%
too_old                        46     -0.6%     -0.4%    11%
wash_churn                     42    -23.3%    -85.6%    31%
liquidity_low                  30    -69.3%    -49.8%    60%
overheated                      8     -3.6%    -56.0%    50%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        59    -55.3%    -93.4%    68%
70-79      82    -51.5%    -69.9%    54%
60-69      50    -35.2%    -92.5%    56%
<60        25     -7.4%    -63.7%    44%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      815     -0.2%    -11.0%    -43.5%    29%
<15%      153     +0.4%    -13.1%    -32.9%    38%
15-30%     36     -1.4%     -2.0%     +0.4%    33%
30%+       32     -0.5%     -0.7%     +1.9%    28%
bundled     n   +1h med   +4h med  +24h med   rug%
none      722     -0.0%     -2.6%    -25.7%    27%
<20%      266     -4.1%    -58.4%    -92.9%    32%
20%+       48     -0.5%    -99.0%       -      79%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      986     -0.1%     -6.8%    -34.1%    28%
20-40%     32     -4.6%    -99.0%    -99.1%    75%
40%+       18    -97.5%    -98.6%       -      78%
tokens analysed: 887 | helius credits today: 2141/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  138    22%     -9.9%   -15.0%   -99.7%
   -6%     20%  138    23%    -10.3%   -15.5%   -99.7%
   -6%     30%  138    21%    -10.2%   -17.1%   -99.7%
  -10%     12%  138    25%     -9.7%   -18.6%   -99.7%
  -10%     20%  138    27%    -10.2%   -18.7%   -99.7%
  -10%     30%  138    25%     -9.8%   -19.1%   -99.7%
  -15%     12%  138    29%     -9.4%   -19.6%   -99.7%
  -15%     20%  138    32%     -9.8%   -20.4%   -99.7%
  -15%     30%  138    30%     -9.7%   -21.0%   -99.7%
  -25%     12%  138    33%    -11.7%   -20.0%   -99.7%
  -25%     20%  138    36%    -13.5%   -29.8%   -99.7%
  -25%     30%  138    34%    -13.6%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.4% per trade over n=138

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $333.85       $354.75
return                        -33.2%        -29.1%
closed trades                     89            75
win rate                         22%           23%
avg net / trade                -8.5%         -8.7%
expectancy $/trade            $-1.87        $-1.94
max drawdown                  -35.8%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $333.85 (-33.2%) | cash $333.85 | open 0 | max drawdown -35.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 89 | win 20/89 (22%) | avg net -8.5% | realized $-166.15 | expectancy $-1.87/trade
exits: stop 66, trail 23
  (n=89 < 100: noise, not evidence)
last trades:
  OGTA         $18.12 -> $13.76 (-24.0%)  stop  0.2h
  FIONA        $17.54 -> $31.83 (+81.5%)  trail  0.8h
  AI           $18.04 -> $10.08 (-44.1%)  stop  0.2h
  iAgent       $18.04 -> $16.18 (-10.3%)  stop  0.5h
  RUGGED       $17.54 -> $10.00 (-43.0%)  stop  0.5h
  AMC          $17.17 -> $13.19 (-23.2%)  stop  0.2h
  RUDY         $16.97 -> $15.02 (-11.5%)  stop  0.2h
  Trader       $16.87 -> $13.30 (-21.2%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 503, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $354.75 (-29.1%) | cash $354.75 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 75 | win 17/75 (23%) | avg net -8.7% | realized $-145.25 | expectancy $-1.94/trade
exits: stop 57, trail 18
  (n=75 < 100: noise, not evidence)
last trades:
  RUGGED       $17.21 -> $19.12 (+11.1%)  trail  0.3h
  CATMARIO     $17.21 -> $13.84 (-19.6%)  stop  0.5h
  HNYDRIP      $17.12 -> $38.11 (+122.6%)  trail  0.7h
  AMC          $18.09 -> $15.90 (-12.1%)  stop  0.2h
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:sellers_dominate_now 133, setup_rejected:dumping_now 132, setup_rejected:b_bundled 50, setup_rejected:volume_dried_up 47, setup_rejected:operator_cluster 36, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
