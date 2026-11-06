# TrenchLab report

Updated: 2026-11-06 15:11 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           6493
passed SCOUT         15
  killed by SCORE    1
  killed by AUDIT    2
FINAL PASS           12

top kill reasons at first sighting (a pool can have several):
  too_young                     6200
  few_unique_buyers             6070
  liquidity_low                 5862
  volume_below_liquidity        4525
  sells_dominate                1956
  wash_churn                    1389
  overheated                     541
  too_old                        255
  missing                        195
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 435 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   12    -5.5%   -10.6%   -44.4%      -      17%
SCOUT PASS, killed later      3    -4.1%   -25.5%   -32.2%      -       0%
KILLED (tracked)            985    +0.0%    -1.2%    -2.2%    -9.8%    25%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         5     -1.4%       -       0%
volume_below_liquidity          3     +5.9%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   2    -82.9%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         5    -58.2%       -      40%
70-79       6    -31.2%       -       0%
60-69       3    -39.9%       -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       35     -2.2%    -11.0%    +39.9%    20%
<15%       12     -0.6%     +0.9%     -2.6%    17%
30%+       12     +0.1%     -0.4%    -14.9%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       50     -0.3%     +0.3%     -2.6%    12%
<20%        9    -14.8%    -46.5%       -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       59     -1.3%     -0.2%     -2.6%    15%
tokens analysed: 41 | helius credits today: 2286/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   12    17%     -4.9%   -17.9%   -29.2%
   -6%     20%   12    17%     -4.9%   -17.9%   -29.2%
   -6%     30%   12    17%     -4.9%   -17.9%   -29.2%
  -10%     12%   12    17%     -8.6%   -20.0%   -44.6%
  -10%     20%   12    17%     -8.6%   -20.0%   -44.6%
  -10%     30%   12    17%     -8.6%   -20.0%   -44.6%
  -15%     12%   12    17%     -9.3%   -20.6%   -44.6%
  -15%     20%   12    17%     -9.3%   -20.6%   -44.6%
  -15%     30%   12    17%     -9.3%   -20.6%   -44.6%
  -25%     12%   12    25%    -12.2%   -19.9%   -67.1%
  -25%     20%   12    25%    -18.0%   -30.1%   -76.1%
  -25%     30%   12    25%    -17.0%   -30.1%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -4.9% per trade over n=12
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $483.79 (-3.2%) | cash $483.79 | open 0 | max drawdown -3.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 0/3 (0%) | avg net -21.8% | realized $-16.21 | expectancy $-5.40/trade
exits: stop 2, trail 1
  (n=3 < 100: noise, not evidence)
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
signals skipped by the sizer/risk rules: already_traded_token 28

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
