# TrenchLab report

Updated: 2026-11-05 23:31 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           1448
passed SCOUT         6
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           4

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers             1324
  too_young                     1315
  liquidity_low                 1265
  volume_below_liquidity        1004
  sells_dominate                 458
  wash_churn                     296
  overheated                     117
  too_old                        113
  missing                         30
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    4   -17.0%    -6.8%      -        -       0%
SCOUT PASS, killed later      2   +29.6%   +17.5%      -        -      50%
KILLED (tracked)            269    +0.8%    +0.7%    +2.7%      -      40%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      5       -         -      60%
too_old                         3       -         -       0%
volume_below_liquidity          2       -         -       0%
liquidity_low                   1    -82.9%       -       0%
too_young                       1       -         -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         2       -         -       0%
70-79       2       -         -      50%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       12     -1.0%       -         -      17%
<15%        4     +0.8%       -         -       0%
30%+        6     -1.5%     +0.5%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       19     -1.7%     +0.5%       -       5%
<20%        3     +4.2%       -         -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       22     -1.4%     +0.5%       -       9%
tokens analysed: 14 | helius credits today: 1022/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    4     0%    -18.8%   -22.2%   -29.2%
   -6%     20%    4     0%    -18.8%   -22.2%   -29.2%
   -6%     30%    4     0%    -18.8%   -22.2%   -29.2%
  -10%     12%    4     0%    -18.8%   -22.2%   -29.2%
  -10%     20%    4     0%    -18.8%   -22.2%   -29.2%
  -10%     30%    4     0%    -18.8%   -22.2%   -29.2%
  -15%     12%    4     0%    -18.8%   -22.2%   -29.2%
  -15%     20%    4     0%    -18.8%   -22.2%   -29.2%
  -15%     30%    4     0%    -18.8%   -22.2%   -29.2%
  -25%     12%    4     0%    -27.1%   -19.9%   -67.1%
  -25%     20%    4     0%    -27.1%   -19.9%   -67.1%
  -25%     30%    4     0%    -27.1%   -19.9%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -18.8% per trade over n=4
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
