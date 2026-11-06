# TrenchLab report

Updated: 2026-11-06 12:21 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           5625
passed SCOUT         15
  killed by SCORE    1
  killed by AUDIT    2
FINAL PASS           12

top kill reasons at first sighting (a pool can have several):
  too_young                     5339
  few_unique_buyers             5241
  liquidity_low                 5041
  volume_below_liquidity        3899
  sells_dominate                1671
  wash_churn                    1210
  overheated                     466
  too_old                        249
  missing                        184
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 386 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   12    -6.5%   -13.3%   -44.0%      -      17%
SCOUT PASS, killed later      3    -4.1%   -25.5%   -32.2%      -       0%
KILLED (tracked)            894    +0.0%    -1.0%    -6.1%    -9.8%    23%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         5     -3.0%       -       0%
volume_below_liquidity          3     +5.9%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   2    -82.9%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         4    -68.2%       -      50%
70-79       6    -31.2%       -       0%
60-69       4    -39.9%       -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       32     -6.8%    -32.2%       -      16%
<15%       12     -0.6%     +0.9%     -2.6%    17%
30%+       12     +0.1%     -0.6%    -14.9%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       47     -1.3%     -0.2%     -8.7%     9%
<20%        9    -14.8%    -44.7%       -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       56     -1.4%     -0.6%     -8.7%    12%
tokens analysed: 39 | helius credits today: 1904/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   12    25%     -3.6%   -17.9%   -29.2%
   -6%     20%   12    25%     -3.6%   -17.9%   -29.2%
   -6%     30%   12    25%     -3.6%   -17.9%   -29.2%
  -10%     12%   12    25%     -7.3%   -20.0%   -44.6%
  -10%     20%   12    25%     -7.3%   -20.0%   -44.6%
  -10%     30%   12    25%     -7.3%   -20.0%   -44.6%
  -15%     12%   12    25%     -7.9%   -20.6%   -44.6%
  -15%     20%   12    25%     -7.9%   -20.6%   -44.6%
  -15%     30%   12    25%     -7.9%   -20.6%   -44.6%
  -25%     12%   12    25%    -12.1%   -19.9%   -67.1%
  -25%     20%   12    25%    -17.9%   -30.1%   -76.1%
  -25%     30%   12    25%    -17.9%   -30.1%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -3.6% per trade over n=12
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $490.93 (-1.8%) | cash $464.58 | open 1 | max drawdown -2.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 1 | win 0/1 (0%) | avg net -43.9% | realized $-10.97 | expectancy $-10.97/trade
exits: stop 1
  (n=1 < 100: noise, not evidence)
open:
  APPLEPAID    cost $24.45  now $26.35 (+7.8%)  held 0.2h
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
signals skipped by the sizer/risk rules: already_traded_token 11

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
