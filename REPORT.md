# TrenchLab report

Updated: 2026-11-05 22:31 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           1124
passed SCOUT         4
  killed by SCORE    1
  killed by AUDIT    0
FINAL PASS           3

top kill reasons at first sighting (a pool can have several):
  too_young                     1030
  few_unique_buyers             1015
  liquidity_low                  974
  volume_below_liquidity         764
  sells_dominate                 378
  wash_churn                     222
  overheated                      88
  too_old                         77
  missing                         29
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    3   -17.0%    -6.8%      -        -       0%
SCOUT PASS, killed later      1    -1.2%      -        -        -       0%
KILLED (tracked)            206    +1.3%    +2.1%      -        -      43%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      5       -         -      60%
volume_below_liquidity          2       -         -       0%
too_old                         2       -         -       0%
liquidity_low                   1       -         -       0%
too_young                       1       -         -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         2       -         -       0%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none        7     +0.2%       -         -      14%
<15%        1       -         -         -       0%
30%+        6     -1.4%       -         -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       11     -1.5%       -         -       0%
<20%        3     +4.2%       -         -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       14     -0.8%       -         -       7%
tokens analysed: 9 | helius credits today: 751/25000

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
