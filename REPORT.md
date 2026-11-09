# TrenchLab report

Updated: 2026-11-09 02:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           25008
passed SCOUT         66
  killed by SCORE    7
  killed by AUDIT    12
FINAL PASS           47

top kill reasons at first sighting (a pool can have several):
  too_young                    24365
  few_unique_buyers            23454
  liquidity_low                22860
  volume_below_liquidity       17683
  sells_dominate                6768
  wash_churn                    5220
  overheated                    2218
  missing                        745
  too_old                        525
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1330 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   47    -5.4%   -17.3%   -44.0%   -85.9%    47%
SCOUT PASS, killed later     19   +10.8%   +11.6%   -85.0%    +9.6%    47%
KILLED (tracked)           4058    +0.0%   -12.3%   -39.0%    +1.3%    25%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      27    -65.9%    -68.9%    41%
too_old                        15     +0.7%     -2.6%     0%
wash_churn                     10    -37.1%       -      50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
liquidity_low                   4    -86.9%       -      75%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        21    -72.7%    -93.2%    81%
70-79      26    -39.9%    -64.2%    35%
60-69      14    -35.2%    -41.6%    29%
<60         5    -41.4%     +9.6%    20%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      208     -0.5%     -9.7%    -11.6%    26%
<15%       40     +0.9%    -24.9%     +7.8%    38%
15-30%      4    +39.0%     -0.1%     +1.0%    50%
30%+       12     +0.1%     +0.1%     +1.9%     8%
bundled     n   +1h med   +4h med  +24h med   rug%
none      202     -0.6%     -3.0%     -0.8%    22%
<20%       54     +1.4%    -44.7%    -93.2%    37%
20%+        8    +24.1%    -99.0%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      254     -0.3%     -5.3%     -2.9%    26%
20-40%      7     +1.3%    -99.0%       -      86%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 210 | helius credits today: 798/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   47    21%    -11.4%   -17.1%   -99.5%
   -6%     20%   47    23%    -11.4%   -17.1%   -99.5%
   -6%     30%   47    26%     -8.0%   -18.5%   -99.5%
  -10%     12%   47    21%    -12.6%   -19.9%   -99.5%
  -10%     20%   47    23%    -12.9%   -20.1%   -99.5%
  -10%     30%   47    28%     -9.2%   -20.1%   -99.5%
  -15%     12%   47    21%    -12.9%   -20.2%   -99.5%
  -15%     20%   47    23%    -13.6%   -20.4%   -99.5%
  -15%     30%   47    28%     -9.9%   -20.4%   -99.5%
  -25%     12%   47    23%    -18.2%   -29.2%   -99.5%
  -25%     20%   47    26%    -20.7%   -29.9%   -99.5%
  -25%     30%   47    30%    -17.1%   -30.9%   -99.5%
  best so far: stop -6%, trail from +30% -> avg -8.0% per trade over n=47
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $477.48       $493.26
return                         -4.5%         -1.3%
closed trades                     18             9
win rate                         22%           11%
avg net / trade                -8.0%         -2.5%
expectancy $/trade            $-2.04        $-0.75
max drawdown                  -10.8%         -9.3%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $477.48 (-4.5%) | cash $440.12 | open 1 | max drawdown -10.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 18 | win 4/18 (22%) | avg net -8.0% | realized $-36.72 | expectancy $-2.04/trade
exits: stop 13, trail 5
  (n=18 < 100: noise, not evidence)
open:
  NVIDIH       cost $23.16  now $37.36 (+61.3%)  held 0.9h
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
equity $493.26 (-1.3%) | cash $493.26 | open 0 | max drawdown -9.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 9 | win 1/9 (11%) | avg net -2.5% | realized $-6.74 | expectancy $-0.75/trade
exits: stop 8, trail 1
  (n=9 < 100: noise, not evidence)
last trades:
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
  TAOLF        $25.76 -> $23.15 (-10.1%)  stop  0.0h
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
  MAGGIE       $25.21 -> $18.19 (-27.8%)  stop  0.5h
  ELYSION      $24.86 -> $20.95 (-15.7%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 110, daily_loss_limit 94, setup_rejected:dumping_now 34, setup_rejected:sellers_dominate_now 31, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_received 6, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
