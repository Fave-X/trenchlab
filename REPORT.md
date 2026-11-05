# TrenchLab report

Updated: 2026-11-05 23:11 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           1341
passed SCOUT         5
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           3

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers             1220
  too_young                     1215
  liquidity_low                 1161
  volume_below_liquidity         921
  sells_dominate                 429
  wash_churn                     269
  overheated                     108
  too_old                        106
  missing                         30
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    3   -17.0%    -6.8%      -        -       0%
SCOUT PASS, killed later      2   +29.6%   -25.5%      -        -      50%
KILLED (tracked)            259    +2.6%    +1.0%    +2.7%      -      40%

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
70-79       1       -         -     100%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       11     -3.3%       -         -      18%
<15%        4     +0.8%       -         -       0%
30%+        6     -1.4%     +0.5%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       18     -1.5%     +0.5%       -       6%
<20%        3     +4.2%       -         -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       21     -0.8%     +0.5%       -      10%
tokens analysed: 13 | helius credits today: 961/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    3     0%    -24.6%   -24.4%   -29.2%
   -6%     20%    3     0%    -24.6%   -24.4%   -29.2%
   -6%     30%    3     0%    -24.6%   -24.4%   -29.2%
  -10%     12%    3     0%    -24.6%   -24.4%   -29.2%
  -10%     20%    3     0%    -24.6%   -24.4%   -29.2%
  -10%     30%    3     0%    -24.6%   -24.4%   -29.2%
  -15%     12%    3     0%    -24.6%   -24.4%   -29.2%
  -15%     20%    3     0%    -24.6%   -24.4%   -29.2%
  -15%     30%    3     0%    -24.6%   -24.4%   -29.2%
  -25%     12%    3     0%    -35.6%   -29.2%   -67.1%
  -25%     20%    3     0%    -35.6%   -29.2%   -67.1%
  -25%     30%    3     0%    -35.6%   -29.2%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -24.6% per trade over n=3
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
