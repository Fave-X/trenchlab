# TrenchLab report

Updated: 2026-11-06 00:11 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           1749
passed SCOUT         6
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           4

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers             1614
  too_young                     1604
  liquidity_low                 1549
  volume_below_liquidity        1217
  sells_dominate                 559
  wash_churn                     374
  overheated                     141
  too_old                        123
  missing                         34
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    4   -14.3%    -6.8%   -68.2%      -       0%
SCOUT PASS, killed later      2   +29.6%   +17.5%      -        -      50%
KILLED (tracked)            304    +0.5%    +0.5%    +2.9%      -      42%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      5       -         -      80%
volume_below_liquidity          3       -         -       0%
too_old                         3       -         -       0%
too_young                       2       -         -     100%
liquidity_low                   1    -82.9%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -       0%
70-79       1       -         -     100%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       14     -1.9%    -55.8%       -      29%
<15%        4     -1.3%       -         -       0%
30%+        6     -1.5%     +0.5%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       20     -1.6%     +0.4%       -      15%
<20%        4     +4.2%    -68.2%       -      25%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       24     -1.4%    -21.5%       -      17%
tokens analysed: 16 | helius credits today: 101/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    4    25%     -4.2%   -22.2%   -29.2%
   -6%     20%    4    25%     -4.2%   -22.2%   -29.2%
   -6%     30%    4    25%     -4.2%   -22.2%   -29.2%
  -10%     12%    4    25%     -4.2%   -22.2%   -29.2%
  -10%     20%    4    25%     -4.2%   -22.2%   -29.2%
  -10%     30%    4    25%     -4.2%   -22.2%   -29.2%
  -15%     12%    4    25%     -4.2%   -22.2%   -29.2%
  -15%     20%    4    25%     -4.2%   -22.2%   -29.2%
  -15%     30%    4    25%     -4.2%   -22.2%   -29.2%
  -25%     12%    4    25%    -12.5%   -19.9%   -67.1%
  -25%     20%    4    25%    -12.5%   -19.9%   -67.1%
  -25%     30%    4    25%    -12.5%   -19.9%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -4.2% per trade over n=4
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
