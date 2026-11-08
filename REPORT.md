# TrenchLab report

Updated: 2026-11-08 04:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           18351
passed SCOUT         51
  killed by SCORE    6
  killed by AUDIT    9
FINAL PASS           36

top kill reasons at first sighting (a pool can have several):
  too_young                    17830
  few_unique_buyers            17233
  liquidity_low                16818
  volume_below_liquidity       13018
  sells_dominate                5069
  wash_churn                    3812
  overheated                    1611
  missing                        504
  too_old                        422
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1030 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   36    -5.5%   -21.6%   -48.2%   -81.8%    44%
SCOUT PASS, killed later     15    +7.3%    -3.3%   -69.2%   +72.1%    33%
KILLED (tracked)           2858    -0.0%    -7.5%   -24.8%    +1.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      17    -93.0%       -      59%
wash_churn                     10    -37.1%       -      50%
too_old                        10     -0.1%     -2.6%     0%
volume_below_liquidity          5     +5.9%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      3    -11.0%       -      33%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        18    -73.5%    -93.2%    72%
70-79      18    -33.6%    -39.0%    28%
60-69      10    -49.8%    -41.6%    30%
<60         5    -50.5%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      142     -2.4%    -10.5%    -11.1%    25%
<15%       31     +0.5%     -8.5%     +7.8%    45%
15-30%      2   +260.4%   +432.0%       -     100%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      141     -1.9%     -2.9%     +0.0%    21%
<20%       35     +1.4%    -48.2%    -98.0%    43%
20%+        8    +24.1%    -99.0%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      175     -1.8%     -4.9%     -0.6%    26%
20-40%      6    -41.0%    -99.0%       -     100%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 151 | helius credits today: 1547/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   36    19%    -14.0%   -19.7%   -99.5%
   -6%     20%   36    19%    -14.2%   -19.7%   -99.5%
   -6%     30%   36    22%     -9.8%   -19.7%   -99.5%
  -10%     12%   36    22%    -14.7%   -20.2%   -99.5%
  -10%     20%   36    22%    -15.1%   -20.2%   -99.5%
  -10%     30%   36    25%    -10.6%   -20.2%   -99.5%
  -15%     12%   36    22%    -15.1%   -20.6%   -99.5%
  -15%     20%   36    22%    -16.0%   -20.9%   -99.5%
  -15%     30%   36    25%    -11.5%   -20.9%   -99.5%
  -25%     12%   36    25%    -20.0%   -29.8%   -99.5%
  -25%     20%   36    25%    -22.8%   -30.0%   -99.5%
  -25%     30%   36    25%    -19.7%   -31.0%   -99.5%
  best so far: stop -6%, trail from +30% -> avg -9.8% per trade over n=36
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $463.28       $503.29
return                         -7.3%         +0.7%
closed trades                     18             7
win rate                         22%           14%
avg net / trade                -8.0%         +3.0%
expectancy $/trade            $-2.04        $+0.60
max drawdown                  -10.8%         -7.4%
open now                           0             1
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
signals skipped by the sizer/risk rules: already_traded_token 96, daily_loss_limit 63, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $503.29 (+0.7%) | cash $478.98 | open 1 | max drawdown -7.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 7 | win 1/7 (14%) | avg net +3.0% | realized $+4.19 | expectancy $+0.60/trade
exits: stop 6, trail 1
  (n=7 < 100: noise, not evidence)
open:
  MAGGIE       cost $25.21  now $24.31 (-3.6%)  held 0.4h
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
  TAOLF        $25.76 -> $23.15 (-10.1%)  stop  0.0h
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 57, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 17, setup_rejected:sellers_dominate_now 2, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
