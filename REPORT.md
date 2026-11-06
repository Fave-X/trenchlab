# TrenchLab report

Updated: 2026-11-06 08:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           4323
passed SCOUT         13
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           11

top kill reasons at first sighting (a pool can have several):
  too_young                     4065
  few_unique_buyers             4031
  liquidity_low                 3849
  volume_below_liquidity        2997
  sells_dominate                1301
  wash_churn                     863
  overheated                     346
  too_old                        226
  missing                        141
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 299 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   11    -7.5%    -7.8%   -38.3%      -       9%
SCOUT PASS, killed later      2    -1.2%   -25.5%   -32.2%      -       0%
KILLED (tracked)            717    +0.0%    -1.3%    -4.4%      -      22%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         4     -3.0%       -       0%
volume_below_liquidity          3     +5.9%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -      33%
70-79       5    -29.7%       -       0%
60-69       4       -         -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       24     -7.2%    -32.4%       -      17%
<15%       13     +0.1%     +1.3%       -      15%
30%+       11     +0.6%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       38     -1.3%     -0.3%       -       8%
<20%       10     -2.3%    -11.9%       -      30%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       48     -1.3%     -0.3%       -      12%
tokens analysed: 32 | helius credits today: 1380/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   10    20%     -3.9%   -19.3%   -29.2%
   -6%     20%   10    20%     -3.9%   -19.3%   -29.2%
   -6%     30%   10    20%     -3.9%   -19.3%   -29.2%
  -10%     12%   10    20%     -4.9%   -20.0%   -29.2%
  -10%     20%   10    20%     -4.9%   -20.0%   -29.2%
  -10%     30%   10    20%     -4.9%   -20.0%   -29.2%
  -15%     12%   10    20%     -5.7%   -20.6%   -29.2%
  -15%     20%   10    20%     -5.7%   -20.6%   -29.2%
  -15%     30%   10    20%     -5.7%   -20.6%   -29.2%
  -25%     12%   10    20%    -12.1%   -25.3%   -67.1%
  -25%     20%   10    20%    -11.4%   -25.3%   -67.1%
  -25%     30%   10    20%    -11.4%   -25.3%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -3.9% per trade over n=10
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $499.34 (-0.1%) | cash $475.00 | open 1 | max drawdown -0.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
open:
  RM           cost $25.00  now $24.34 (-2.6%)  held 0.0h

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
