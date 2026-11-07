# TrenchLab report

Updated: 2026-11-07 06:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           11154
passed SCOUT         28
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           20

top kill reasons at first sighting (a pool can have several):
  too_young                    10795
  few_unique_buyers            10503
  liquidity_low                10137
  volume_below_liquidity        7875
  sells_dominate                3241
  wash_churn                    2290
  overheated                     956
  missing                        364
  too_old                        303
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 697 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   20    -5.5%   -21.3%   -44.0%   -60.1%    35%
SCOUT PASS, killed later      8    +6.2%    +6.7%   -73.5%   +72.1%    38%
KILLED (tracked)           1632    -0.1%    -3.3%    -8.4%    +0.5%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      9    -37.1%       -      56%
too_old                         9     +0.2%     -6.7%     0%
too_young                       7    -94.0%       -      71%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -68.2%    -93.4%    64%
70-79      11    -31.2%     +2.6%     9%
60-69       5    -41.2%       -      40%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       78     -2.9%     -7.6%     +5.7%    18%
<15%       19     +0.6%     +0.4%     -0.8%    37%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -0.6%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none       88     -1.9%     -1.4%     +2.6%    10%
<20%       14     +3.2%    -51.7%    -34.6%    71%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      101     -1.9%     -2.3%     +2.6%    19%
20-40%      3    +16.6%    -99.2%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 81 | helius credits today: 1321/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   20    20%    -10.7%   -19.3%   -65.0%
   -6%     20%   20    20%    -10.7%   -19.3%   -65.0%
   -6%     30%   20    20%    -11.0%   -19.3%   -65.0%
  -10%     12%   20    20%    -12.9%   -20.6%   -65.0%
  -10%     20%   20    20%    -12.9%   -20.6%   -65.0%
  -10%     30%   20    20%    -13.2%   -20.6%   -65.0%
  -15%     12%   20    20%    -13.2%   -21.2%   -65.0%
  -15%     20%   20    20%    -13.2%   -21.2%   -65.0%
  -15%     30%   20    20%    -13.5%   -21.2%   -65.0%
  -25%     12%   20    25%    -15.0%   -25.3%   -67.1%
  -25%     20%   20    25%    -18.5%   -29.5%   -76.1%
  -25%     30%   20    20%    -21.2%   -30.4%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -10.7% per trade over n=20
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $478.13       $497.87
return                         -4.4%         -0.4%
closed trades                      6             0
win rate                         33%             -
avg net / trade               -13.3%             -
expectancy $/trade            $-3.36             -
max drawdown                   -5.4%         -0.4%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $478.13 (-4.4%) | cash $455.87 | open 1 | max drawdown -5.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 6 | win 2/6 (33%) | avg net -13.3% | realized $-20.14 | expectancy $-3.36/trade
exits: stop 3, trail 3
  (n=6 < 100: noise, not evidence)
open:
  Alice        cost $23.99  now $22.26 (-7.2%)  held 0.9h
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 49, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $497.87 (-0.4%) | cash $475.00 | open 1 | max drawdown -0.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
open:
  Alice        cost $25.00  now $22.87 (-8.5%)  held 0.4h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 11, setup_rejected:top10_concentrated 6, setup_rejected:dumping_now 2

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
