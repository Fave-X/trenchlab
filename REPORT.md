# TrenchLab report

Updated: 2026-11-08 10:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           20116
passed SCOUT         55
  killed by SCORE    5
  killed by AUDIT    10
FINAL PASS           40

top kill reasons at first sighting (a pool can have several):
  too_young                    19566
  few_unique_buyers            18846
  liquidity_low                18444
  volume_below_liquidity       14238
  sells_dominate                5511
  wash_churn                    4249
  overheated                    1812
  missing                        541
  too_old                        447
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1115 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   40    -5.3%   -13.2%   -46.5%   -77.7%    40%
SCOUT PASS, killed later     15   +10.8%   +11.6%   -78.9%   +72.1%    40%
KILLED (tracked)           3155    -0.0%    -9.7%   -32.9%    +0.8%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      19    -93.0%       -      58%
wash_churn                     10    -37.1%       -      50%
too_old                        10     -0.1%     -2.6%     0%
volume_below_liquidity          5     +5.9%     +0.4%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      2    -11.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        18    -73.1%    -93.2%    72%
70-79      23    -32.6%    -64.2%    26%
60-69      10    -49.8%    -41.6%    30%
<60         4    -41.4%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      165     -1.4%     -8.0%    -10.2%    23%
<15%       29     +0.5%    -34.2%     +7.8%    48%
15-30%      2   +260.4%   +432.0%       -     100%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      161     -1.2%     -2.9%     -0.6%    19%
<20%       36     +0.6%    -50.5%    -96.6%    44%
20%+        8    +24.1%    -99.0%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      196     -0.9%     -5.3%     -1.3%    24%
20-40%      6    -41.0%    -99.2%       -     100%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 165 | helius credits today: 3007/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   40    20%    -13.2%   -19.7%   -99.5%
   -6%     20%   40    22%    -13.2%   -19.7%   -99.5%
   -6%     30%   40    25%     -9.2%   -19.7%   -99.5%
  -10%     12%   40    20%    -14.1%   -20.1%   -99.5%
  -10%     20%   40    22%    -14.2%   -20.1%   -99.5%
  -10%     30%   40    28%     -9.9%   -20.1%   -99.5%
  -15%     12%   40    20%    -14.5%   -20.4%   -99.5%
  -15%     20%   40    22%    -15.0%   -20.6%   -99.5%
  -15%     30%   40    28%    -10.7%   -20.6%   -99.5%
  -25%     12%   40    22%    -19.7%   -29.8%   -99.5%
  -25%     20%   40    25%    -21.9%   -30.0%   -99.5%
  -25%     30%   40    28%    -18.8%   -31.0%   -99.5%
  best so far: stop -6%, trail from +30% -> avg -9.2% per trade over n=40
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $463.28       $497.17
return                         -7.3%         -0.6%
closed trades                     18             8
win rate                         22%           12%
avg net / trade                -8.0%         -0.8%
expectancy $/trade            $-2.04        $-0.35
max drawdown                  -10.8%         -8.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $463.28 (-7.3%) | cash $463.28 | open 0 | max drawdown -10.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 18 | win 4/18 (22%) | avg net -8.0% | realized $-36.72 | expectancy $-2.04/trade
exits: stop 13, trail 5
  (n=18 < 100: noise, not evidence)
last trades:
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
  FRODO        $24.01 -> $20.82 (-13.3%)  stop  0.3h
  TAOLF        $23.66 -> $29.60 (+25.1%)  trail  0.8h
  CLAUDIA      $24.09 -> $19.43 (-19.3%)  stop  0.5h
  BLEND        $23.55 -> $20.73 (-12.0%)  stop  2.7h
  invest       $23.69 -> $15.38 (-35.1%)  stop  0.3h
signals skipped by the sizer/risk rules: daily_loss_limit 122, already_traded_token 96, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $497.17 (-0.6%) | cash $497.17 | open 0 | max drawdown -8.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 8 | win 1/8 (12%) | avg net -0.8% | realized $-2.83 | expectancy $-0.35/trade
exits: stop 7, trail 1
  (n=8 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
  TAOLF        $25.76 -> $23.15 (-10.1%)  stop  0.0h
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
  MAGGIE       $25.21 -> $18.19 (-27.8%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 63, setup_rejected:top10_concentrated 29, setup_rejected:dumping_now 19, setup_rejected:volume_dried_up 17, daily_loss_limit 12, setup_rejected:sellers_dominate_now 2, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
