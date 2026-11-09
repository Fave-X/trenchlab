# TrenchLab report

Updated: 2026-11-09 03:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           25150
passed SCOUT         67
  killed by SCORE    7
  killed by AUDIT    12
FINAL PASS           48

top kill reasons at first sighting (a pool can have several):
  too_young                    24506
  few_unique_buyers            23585
  liquidity_low                22990
  volume_below_liquidity       17779
  sells_dominate                6804
  wash_churn                    5253
  overheated                    2233
  missing                        748
  too_old                        525
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1339 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   48    -5.3%   -13.3%   -44.0%   -85.9%    46%
SCOUT PASS, killed later     19   +10.8%   +11.6%   -84.2%    +9.6%    47%
KILLED (tracked)           4082    +0.0%   -12.2%   -38.0%    +1.3%    25%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      27    -65.9%    -68.9%    41%
too_old                        15     +0.7%     -2.6%     0%
wash_churn                     10    -37.1%       -      50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
liquidity_low                   4    -84.9%       -      75%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        21    -72.7%    -93.2%    81%
70-79      27    -39.9%    -64.2%    33%
60-69      14    -35.2%    -41.6%    29%
<60         5    -32.2%     +9.6%    20%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      210     -0.6%     -8.7%    -11.6%    26%
<15%       40     +2.4%    -14.2%     +7.8%    40%
15-30%      4    +39.0%     -0.1%     +1.0%    50%
30%+       12     +0.1%     +0.1%     +1.9%     8%
bundled     n   +1h med   +4h med  +24h med   rug%
none      204     -0.8%     -3.0%     -0.8%    22%
<20%       54     +2.5%    -39.6%    -93.2%    39%
20%+        8    +24.1%    -99.0%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      256     -0.3%     -5.1%     -2.9%    26%
20-40%      7     +1.3%    -99.0%       -      86%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 212 | helius credits today: 1030/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   48    21%    -11.0%   -17.1%   -99.5%
   -6%     20%   48    23%    -11.0%   -17.1%   -99.5%
   -6%     30%   48    25%     -7.7%   -17.8%   -99.5%
  -10%     12%   48    21%    -12.2%   -19.7%   -99.5%
  -10%     20%   48    23%    -12.5%   -20.0%   -99.5%
  -10%     30%   48    27%     -8.9%   -20.0%   -99.5%
  -15%     12%   48    21%    -12.5%   -20.1%   -99.5%
  -15%     20%   48    23%    -13.2%   -20.4%   -99.5%
  -15%     30%   48    27%     -9.5%   -20.4%   -99.5%
  -25%     12%   48    23%    -17.6%   -29.2%   -99.5%
  -25%     20%   48    25%    -20.1%   -29.9%   -99.5%
  -25%     30%   48    29%    -16.6%   -30.5%   -99.5%
  best so far: stop -6%, trail from +30% -> avg -7.7% per trade over n=48
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $479.46       $490.30
return                         -4.1%         -1.9%
closed trades                     18            10
win rate                         22%           10%
avg net / trade                -8.0%         -3.5%
expectancy $/trade            $-2.04        $-0.97
max drawdown                  -10.8%         -9.8%
open now                           2             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $479.46 (-4.1%) | cash $416.25 | open 2 | max drawdown -10.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 18 | win 4/18 (22%) | avg net -8.0% | realized $-36.72 | expectancy $-2.04/trade
exits: stop 13, trail 5
  (n=18 < 100: noise, not evidence)
open:
  NVIDIH       cost $23.16  now $41.12 (+77.6%)  held 1.4h
  BAWSAQ       cost $23.87  now $22.10 (-7.4%)  held 0.4h
last trades:
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
  FRODO        $24.01 -> $20.82 (-13.3%)  stop  0.3h
  TAOLF        $23.66 -> $29.60 (+25.1%)  trail  0.8h
  CLAUDIA      $24.09 -> $19.43 (-19.3%)  stop  0.5h
  BLEND        $23.55 -> $20.73 (-12.0%)  stop  2.7h
  invest       $23.69 -> $15.38 (-35.1%)  stop  0.3h
signals skipped by the sizer/risk rules: daily_loss_limit 168, already_traded_token 98, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $490.30 (-1.9%) | cash $490.30 | open 0 | max drawdown -9.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 10 | win 1/10 (10%) | avg net -3.5% | realized $-9.70 | expectancy $-0.97/trade
exits: stop 9, trail 1
  (n=10 < 100: noise, not evidence)
last trades:
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
  TAOLF        $25.76 -> $23.15 (-10.1%)  stop  0.0h
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
  MAGGIE       $25.21 -> $18.19 (-27.8%)  stop  0.5h
  ELYSION      $24.86 -> $20.95 (-15.7%)  stop  0.5h
  PUSSY        $24.66 -> $21.70 (-12.0%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 110, daily_loss_limit 94, setup_rejected:dumping_now 34, setup_rejected:sellers_dominate_now 32, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_received 6, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
