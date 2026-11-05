# TrenchLab report

Updated: 2026-11-05 20:21 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           405
passed SCOUT         2
  killed by SCORE    0
  killed by AUDIT    0
FINAL PASS           2

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers              342
  too_young                      320
  liquidity_low                  303
  volume_below_liquidity         285
  sells_dominate                 133
  wash_churn                      90
  too_old                         70
  overheated                      28
  missing                          9

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    2      -     -21.3%      -        -       0%
KILLED (tracked)            122    -0.2%    +2.0%      -        -      12%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      5       -         -      20%
volume_below_liquidity          2       -         -       0%
too_old                         2       -         -       0%
liquidity_low                   1       -         -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         1       -         -       0%
60-69       1       -         -       0%

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    2     0%    -26.8%   -26.8%   -29.2%
   -6%     20%    2     0%    -26.8%   -26.8%   -29.2%
   -6%     30%    2     0%    -26.8%   -26.8%   -29.2%
  -10%     12%    2     0%    -26.8%   -26.8%   -29.2%
  -10%     20%    2     0%    -26.8%   -26.8%   -29.2%
  -10%     30%    2     0%    -26.8%   -26.8%   -29.2%
  -15%     12%    2     0%    -26.8%   -26.8%   -29.2%
  -15%     20%    2     0%    -26.8%   -26.8%   -29.2%
  -15%     30%    2     0%    -26.8%   -26.8%   -29.2%
  -25%     12%    2     0%    -48.2%   -48.2%   -67.1%
  -25%     20%    2     0%    -48.2%   -48.2%   -67.1%
  -25%     30%    2     0%    -48.2%   -48.2%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -26.8% per trade over n=2
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
