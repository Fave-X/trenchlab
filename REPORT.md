# TrenchLab report

Updated: 2026-11-05 20:50 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           610
passed SCOUT         3
  killed by SCORE    0
  killed by AUDIT    0
FINAL PASS           3

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers              541
  too_young                      524
  liquidity_low                  481
  volume_below_liquidity         415
  sells_dominate                 210
  wash_churn                     122
  too_old                         71
  overheated                      41
  missing                         29

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    3   -17.0%   -21.3%      -        -       0%
KILLED (tracked)            141    +0.8%    +2.0%      -        -      33%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      5       -         -      60%
volume_below_liquidity          2       -         -       0%
too_old                         2       -         -       0%
liquidity_low                   1       -         -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         1       -         -       0%
70-79       1       -         -       0%
60-69       1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none        3       -         -         -       0%
30%+        5       -         -         -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none        6       -         -         -       0%
<20%        1       -         -         -       0%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%        8       -         -         -       0%
tokens analysed: 4 | helius credits today: 307/25000

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
  -25%     12%    3     0%    -38.6%   -29.2%   -67.1%
  -25%     20%    3     0%    -38.6%   -29.2%   -67.1%
  -25%     30%    3     0%    -38.6%   -29.2%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -24.6% per trade over n=3
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
