# TrenchLab report

Updated: 2026-11-05 20:25 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           444
passed SCOUT         3
  killed by SCORE    0
  killed by AUDIT    0
FINAL PASS           3

top kill reasons at first sighting (a pool can have several):
  few_unique_buyers              380
  too_young                      359
  liquidity_low                  338
  volume_below_liquidity         309
  sells_dominate                 147
  wash_churn                      99
  too_old                         70
  overheated                      32
  missing                          9

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    3      -     -21.3%      -        -       0%
KILLED (tracked)            129    +0.1%    +2.0%      -        -      28%

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
70-79       1       -         -       0%
60-69       1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none        8       -         -         -       0%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%        8       -         -         -       0%
tokens analysed: 4 | helius credits today: 107/25000

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
