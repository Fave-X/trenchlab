# TrenchLab report

Updated: 2026-11-07 03:08 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           10211
passed SCOUT         27
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           19

top kill reasons at first sighting (a pool can have several):
  too_young                     9860
  few_unique_buyers             9632
  liquidity_low                 9275
  volume_below_liquidity        7213
  sells_dominate                3023
  wash_churn                    2071
  overheated                     856
  missing                        340
  too_old                        299
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 635 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   19    -5.6%   -17.3%   -44.7%   -79.9%    32%
SCOUT PASS, killed later      8   +13.9%    -3.3%   -73.5%   +72.1%    25%
KILLED (tracked)           1473    -0.1%    -2.6%    -8.5%    +0.8%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      9    -37.1%       -      56%
too_old                         9     +0.7%     -6.7%     0%
too_young                       7    -98.9%       -      71%
volume_below_liquidity          4     +5.9%     -4.6%    25%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -70.4%    -93.4%    45%
70-79      10    -32.6%    -66.4%    10%
60-69       5    -41.2%       -      40%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       75     -2.9%     -7.6%     +5.7%    16%
<15%       17     +0.3%     -2.0%     +7.8%    35%
15-30%      1   +442.6%       -         -       0%
30%+        8     -1.4%     -0.6%     +0.8%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       83     -1.9%     -0.5%     +2.6%    10%
<20%       14     -2.3%    -51.7%    -34.6%    57%
20%+        4    +31.6%    -99.2%       -      50%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       96     -1.9%     -1.7%     +2.6%    17%
20-40%      3    -33.5%    -99.2%       -      67%
40%+        2   +442.6%       -         -       0%
tokens analysed: 77 | helius credits today: 893/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   19    21%    -11.1%   -19.9%   -65.0%
   -6%     20%   19    21%    -11.1%   -19.9%   -65.0%
   -6%     30%   19    21%    -11.1%   -19.9%   -65.0%
  -10%     12%   19    21%    -13.4%   -21.0%   -65.0%
  -10%     20%   19    21%    -13.4%   -21.0%   -65.0%
  -10%     30%   19    21%    -13.4%   -21.0%   -65.0%
  -15%     12%   19    21%    -13.8%   -21.3%   -65.0%
  -15%     20%   19    21%    -13.8%   -21.3%   -65.0%
  -15%     30%   19    21%    -13.8%   -21.3%   -65.0%
  -25%     12%   19    26%    -15.7%   -29.2%   -67.1%
  -25%     20%   19    26%    -19.3%   -29.9%   -76.1%
  -25%     30%   19    21%    -21.8%   -31.0%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -11.1% per trade over n=19
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $479.86 (-4.0%) | cash $479.86 | open 0 | max drawdown -5.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 6 | win 2/6 (33%) | avg net -13.3% | realized $-20.14 | expectancy $-3.36/trade
exits: stop 3, trail 3
  (n=6 < 100: noise, not evidence)
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 42, daily_loss_limit 31, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
