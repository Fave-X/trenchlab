# TrenchLab report

Updated: 2026-11-23 23:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           131850
passed SCOUT         260
  killed by SCORE    36
  killed by AUDIT    65
FINAL PASS           159

top kill reasons at first sighting (a pool can have several):
  too_young                   130083
  few_unique_buyers           124063
  liquidity_low               121943
  volume_below_liquidity       92942
  sells_dominate               35040
  wash_churn                   27627
  overheated                   11873
  missing                       3665
  too_old                       1288
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 7837 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  159    -5.0%   -12.5%   -41.3%   -85.9%    57%
SCOUT PASS, killed later    101    +5.4%    +9.1%   -19.5%   -75.1%    50%
KILLED (tracked)          18222    +0.1%   -59.6%   -85.0%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     390    -90.5%    -68.9%    25%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        51     -0.6%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        72    -52.9%    -93.2%    60%
70-79     102    -41.9%    -73.6%    51%
60-69      61    -30.1%    -92.5%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1032     +0.0%    -10.5%    -48.4%    26%
<15%      236     +2.4%    -14.2%    -40.1%    33%
15-30%     43     -0.5%     -2.4%     +0.4%    33%
30%+       36     -0.7%     -0.7%     +1.9%    33%
bundled     n   +1h med   +4h med  +24h med   rug%
none      901     +0.0%     -2.5%    -33.1%    25%
<20%      388     +2.8%    -58.2%    -92.1%    28%
20%+       58     -5.1%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1292     +0.2%     -6.8%    -40.8%    26%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       21    -98.6%    -98.6%       -      76%
tokens analysed: 1183 | helius credits today: 9692/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  159    22%     -9.7%   -14.5%   -99.7%
   -6%     20%  159    23%    -10.0%   -14.9%   -99.7%
   -6%     30%  159    21%    -10.2%   -15.4%   -99.7%
  -10%     12%  159    25%     -9.7%   -17.1%   -99.7%
  -10%     20%  159    26%    -10.1%   -17.5%   -99.7%
  -10%     30%  159    25%    -10.1%   -18.6%   -99.7%
  -15%     12%  159    30%     -9.4%   -19.5%   -99.7%
  -15%     20%  159    32%     -9.9%   -20.4%   -99.7%
  -15%     30%  159    30%    -10.3%   -21.1%   -99.7%
  -25%     12%  159    34%    -11.4%   -17.1%   -99.7%
  -25%     20%  159    37%    -13.2%   -29.6%   -99.7%
  -25%     30%  159    35%    -13.3%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.4% per trade over n=159

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $294.69       $330.06
return                        -41.1%        -34.0%
closed trades                    106            85
win rate                         22%           22%
avg net / trade                -9.5%         -9.4%
expectancy $/trade            $-1.94        $-2.00
max drawdown                  -43.3%        -39.3%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $294.69 (-41.1%) | cash $279.96 | open 1 | max drawdown -43.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 106 | win 23/106 (22%) | avg net -9.5% | realized $-205.31 | expectancy $-1.94/trade
exits: stop 77, trail 28, dead_no_route 1
open:
  JIMMY        cost $14.73  now $14.73 (+0.0%)  held 0.0h
last trades:
  MCAT         $16.18 -> $0.00 (-100.0%)  dead_no_route  1.8h
  OpenIndex    $15.37 -> $12.15 (-20.9%)  stop  0.3h
  COPIUM       $15.21 -> $13.38 (-12.0%)  stop  1.0h
  Fly          $15.11 -> $13.32 (-11.9%)  stop  0.2h
  cCAT         $15.02 -> $17.11 (+13.9%)  trail  0.3h
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
  ChristmASS   $15.10 -> $9.98 (-33.9%)  stop  0.2h
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 589, daily_loss_limit 322, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $330.06 (-34.0%) | cash $330.06 | open 0 | max drawdown -39.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 85 | win 19/85 (22%) | avg net -9.4% | realized $-169.94 | expectancy $-2.00/trade
exits: stop 65, trail 20
  (n=85 < 100: noise, not evidence)
last trades:
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
  MCAT         $17.32 -> $18.54 (+7.0%)  trail  3.5h
  cCAT         $17.38 -> $13.20 (-24.0%)  stop  0.2h
  UCASH        $17.17 -> $17.37 (+1.2%)  trail  0.8h
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 436, daily_loss_limit 240, setup_rejected:sellers_dominate_now 142, setup_rejected:dumping_now 142, setup_rejected:b_bundled 74, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:clustered_supply 38, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
