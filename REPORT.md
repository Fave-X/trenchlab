# TrenchLab report

Updated: 2026-11-06 07:20 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           3975
passed SCOUT         12
  killed by SCORE    2
  killed by AUDIT    1
FINAL PASS           9

top kill reasons at first sighting (a pool can have several):
  too_young                     3752
  few_unique_buyers             3701
  liquidity_low                 3539
  volume_below_liquidity        2730
  sells_dominate                1196
  wash_churn                     781
  overheated                     315
  too_old                        191
  missing                        140
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    9    -9.4%    -6.8%   -44.0%      -      11%
SCOUT PASS, killed later      3   +60.4%   +60.4%   +60.4%      -      33%
KILLED (tracked)            645    +2.5%    +1.2%    +0.5%      -      58%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8     +0.5%       -     100%
volume_below_liquidity          3     +5.9%       -      33%
too_old                         3     -3.0%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -      33%
70-79       5    -29.7%       -      20%
60-69       2       -         -       0%
<60         2   +706.9%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       22     -2.1%    -11.0%       -      36%
<15%       13     +0.3%     +1.1%       -      15%
30%+       11     +0.6%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       37     -0.8%     -0.1%       -      16%
<20%        9     +6.5%    -11.9%       -      44%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       46     +0.1%     -0.1%       -      22%
tokens analysed: 30 | helius credits today: 1169/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    8    25%     +0.8%   -17.9%   -29.2%
   -6%     20%    8    25%     +0.8%   -17.9%   -29.2%
   -6%     30%    8    25%     +0.8%   -17.9%   -29.2%
  -10%     12%    8    25%     -0.4%   -19.4%   -29.2%
  -10%     20%    8    25%     -0.4%   -19.4%   -29.2%
  -10%     30%    8    25%     -0.4%   -19.4%   -29.2%
  -15%     12%    8    25%     -1.4%   -20.6%   -29.2%
  -15%     20%    8    25%     -1.4%   -20.6%   -29.2%
  -15%     30%    8    25%     -1.4%   -20.6%   -29.2%
  -25%     12%    8    25%     -8.8%   -24.0%   -67.1%
  -25%     20%    8    25%     -8.8%   -24.0%   -67.1%
  -25%     30%    8    25%     -8.8%   -24.0%   -67.1%
  best so far: stop -6%, trail from +12% -> avg +0.8% per trade over n=8
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
