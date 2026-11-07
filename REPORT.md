# TrenchLab report

Updated: 2026-11-07 00:01 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           9285
passed SCOUT         24
  killed by SCORE    2
  killed by AUDIT    5
FINAL PASS           17

top kill reasons at first sighting (a pool can have several):
  too_young                     8945
  few_unique_buyers             8756
  liquidity_low                 8417
  volume_below_liquidity        6538
  sells_dominate                2748
  wash_churn                    1903
  overheated                     776
  missing                        318
  too_old                        289
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 575 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   17    -5.7%   -21.6%   -44.7%   -93.4%    29%
SCOUT PASS, killed later      7   +13.9%    -3.3%   -65.8%   +72.1%    29%
KILLED (tracked)           1342    -0.0%    -2.5%    -7.9%    -0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      9    -37.1%       -      56%
too_old                         7     +0.2%     -6.7%     0%
too_young                       6    -94.0%       -      83%
volume_below_liquidity          4     +5.9%    -39.4%    25%
liquidity_low                   3    -86.9%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         8    -58.2%    -93.4%    50%
70-79      10    -38.7%       -      10%
60-69       5    -39.9%       -      40%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       68     -3.8%    -10.5%     +5.7%    16%
<15%       16     +0.1%     +0.7%     +7.8%    38%
15-30%      1       -         -         -       0%
30%+        7     -1.4%     -0.6%     +0.8%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       76     -2.2%     -0.3%     +2.6%    11%
<20%       13    -22.2%    -51.7%    -99.5%    54%
20%+        3    -33.5%    -99.5%       -      67%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       89     -2.3%     -0.6%     +2.6%    17%
20-40%      2    -33.5%    -99.5%       -     100%
40%+        1       -         -         -       0%
tokens analysed: 68 | helius credits today: 203/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   16    12%    -12.0%   -20.0%   -51.8%
   -6%     20%   16    12%    -12.0%   -20.0%   -51.8%
   -6%     30%   16    12%    -12.0%   -20.0%   -51.8%
  -10%     12%   16    12%    -14.8%   -21.2%   -51.8%
  -10%     20%   16    12%    -14.8%   -21.2%   -51.8%
  -10%     30%   16    12%    -14.8%   -21.2%   -51.8%
  -15%     12%   16    12%    -15.3%   -22.9%   -51.8%
  -15%     20%   16    12%    -15.3%   -22.9%   -51.8%
  -15%     30%   16    12%    -15.3%   -22.9%   -51.8%
  -25%     12%   16    19%    -17.5%   -29.5%   -67.1%
  -25%     20%   16    19%    -21.8%   -29.9%   -76.1%
  -25%     30%   16    12%    -24.8%   -31.0%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -12.0% per trade over n=16
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $483.15 (-3.4%) | cash $459.60 | open 1 | max drawdown -3.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 0/3 (0%) | avg net -21.8% | realized $-16.21 | expectancy $-5.40/trade
exits: stop 2, trail 1
  (n=3 < 100: noise, not evidence)
open:
  DCAT         cost $24.19  now $23.55 (-2.6%)  held 0.0h
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
signals skipped by the sizer/risk rules: already_traded_token 38, daily_loss_limit 31

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
