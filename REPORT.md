# TrenchLab report

Updated: 2026-11-05 10:44 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           161
passed SCOUT         1
  killed by SCORE    0
  killed by AUDIT    0
FINAL PASS           1

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers              125
  volume_below_liquidity         124
  too_young                      112
  liquidity_low                  108
  sells_dominate                  49
  wash_churn                      45
  too_old                         39
  overheated                      12

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    1      -     -21.3%      -        -       0%
KILLED (tracked)             63      -      +2.0%      -        -      19%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      3       -         -       0%
volume_below_liquidity          2       -         -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
60-69       1       -         -       0%

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    1     0%    -24.4%   -24.4%   -24.4%
   -6%     20%    1     0%    -24.4%   -24.4%   -24.4%
   -6%     30%    1     0%    -24.4%   -24.4%   -24.4%
  -10%     12%    1     0%    -24.4%   -24.4%   -24.4%
  -10%     20%    1     0%    -24.4%   -24.4%   -24.4%
  -10%     30%    1     0%    -24.4%   -24.4%   -24.4%
  -15%     12%    1     0%    -24.4%   -24.4%   -24.4%
  -15%     20%    1     0%    -24.4%   -24.4%   -24.4%
  -15%     30%    1     0%    -24.4%   -24.4%   -24.4%
  -25%     12%    1     0%    -24.4%   -24.4%   -24.4%
  -25%     20%    1     0%    -24.4%   -24.4%   -24.4%
  -25%     30%    1     0%    -24.4%   -24.4%   -24.4%
  best so far: stop -6%, trail from +12% -> avg -24.4% per trade over n=1
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~5 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
