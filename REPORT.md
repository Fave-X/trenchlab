# TrenchLab report

Updated: 2026-11-24 01:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           132268
passed SCOUT         260
  killed by SCORE    36
  killed by AUDIT    65
FINAL PASS           159

top kill reasons at first sighting (a pool can have several):
  too_young                   130500
  few_unique_buyers           124458
  liquidity_low               122332
  volume_below_liquidity       93239
  sells_dominate               35147
  wash_churn                   27713
  overheated                   11913
  missing                       3681
  too_old                       1289
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 7866 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  159    -5.0%   -13.2%   -41.3%   -85.9%    58%
SCOUT PASS, killed later    101    +5.4%    +9.1%   -19.5%   -75.1%    50%
KILLED (tracked)          18259    +0.1%   -60.6%   -85.1%    +0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     393    -90.5%    -68.9%    25%
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
70-79     102    -41.9%    -73.6%    52%
60-69      61    -30.1%    -92.5%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1037     +0.0%     -9.9%    -47.5%    27%
<15%      236     +2.3%    -14.2%    -40.1%    33%
15-30%     43     -0.5%     -2.4%     +0.4%    33%
30%+       36     -0.7%     -0.7%     +1.9%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      902     +0.0%     -2.3%    -33.0%    25%
<20%      392     +2.8%    -58.2%    -92.1%    28%
20%+       58     -5.2%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1297     +0.2%     -6.4%    -40.1%    26%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       21    -98.6%    -98.6%       -      81%
tokens analysed: 1188 | helius credits today: 554/25000

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
equity                       $292.43       $327.86
return                        -41.5%        -34.4%
closed trades                    107            86
win rate                         21%           22%
avg net / trade                -9.6%         -9.5%
expectancy $/trade            $-1.94        $-2.00
max drawdown                  -43.7%        -39.7%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $292.43 (-41.5%) | cash $292.43 | open 0 | max drawdown -43.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 107 | win 23/107 (21%) | avg net -9.6% | realized $-207.57 | expectancy $-1.94/trade
exits: stop 78, trail 28, dead_no_route 1
last trades:
  OpenIndex    $15.37 -> $12.15 (-20.9%)  stop  0.3h
  COPIUM       $15.21 -> $13.38 (-12.0%)  stop  1.0h
  Fly          $15.11 -> $13.32 (-11.9%)  stop  0.2h
  cCAT         $15.02 -> $17.11 (+13.9%)  trail  0.3h
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
  ChristmASS   $15.10 -> $9.98 (-33.9%)  stop  0.2h
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 592, daily_loss_limit 322, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $327.86 (-34.4%) | cash $327.86 | open 0 | max drawdown -39.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 86 | win 19/86 (22%) | avg net -9.5% | realized $-172.14 | expectancy $-2.00/trade
exits: stop 66, trail 20
  (n=86 < 100: noise, not evidence)
last trades:
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
  MCAT         $17.32 -> $18.54 (+7.0%)  trail  3.5h
  cCAT         $17.38 -> $13.20 (-24.0%)  stop  0.2h
  UCASH        $17.17 -> $17.37 (+1.2%)  trail  0.8h
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 436, daily_loss_limit 240, setup_rejected:dumping_now 143, setup_rejected:sellers_dominate_now 142, setup_rejected:b_bundled 74, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:clustered_supply 38, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
