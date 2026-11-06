# TrenchLab report

Updated: 2026-11-06 00:50 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           1963
passed SCOUT         6
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           4

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers             1818
  too_young                     1815
  liquidity_low                 1737
  volume_below_liquidity        1357
  sells_dominate                 623
  wash_churn                     422
  overheated                     153
  too_old                        125
  missing                         54
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    4   -14.3%    -2.5%   -56.1%      -      25%
SCOUT PASS, killed later      2   +29.6%   +17.5%      -        -      50%
KILLED (tracked)            329    +0.6%    +0.2%    +1.4%      -      45%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      6    -49.3%       -     100%
volume_below_liquidity          3       -         -       0%
too_old                         3     -7.0%       -       0%
too_young                       2       -         -     100%
liquidity_low                   1    -82.9%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -56.1%       -      33%
70-79       1       -         -     100%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       15     -2.2%    -43.7%       -      33%
<15%        5     -0.2%       -         -      20%
30%+        6     -1.5%     -1.4%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       21     -1.8%     -3.0%       -      19%
<20%        5     +6.5%    -68.2%       -      40%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       26     -1.5%     -3.0%       -      23%
tokens analysed: 18 | helius credits today: 223/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    4    25%     -1.7%   -22.2%   -29.2%
   -6%     20%    4    25%     -1.7%   -22.2%   -29.2%
   -6%     30%    4    25%     -1.7%   -22.2%   -29.2%
  -10%     12%    4    25%     -1.7%   -22.2%   -29.2%
  -10%     20%    4    25%     -1.7%   -22.2%   -29.2%
  -10%     30%    4    25%     -1.7%   -22.2%   -29.2%
  -15%     12%    4    25%     -1.7%   -22.2%   -29.2%
  -15%     20%    4    25%     -1.7%   -22.2%   -29.2%
  -15%     30%    4    25%     -1.7%   -22.2%   -29.2%
  -25%     12%    4    25%    -10.0%   -19.9%   -67.1%
  -25%     20%    4    25%    -10.0%   -19.9%   -67.1%
  -25%     30%    4    25%    -10.0%   -19.9%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -1.7% per trade over n=4
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
