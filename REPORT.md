# TrenchLab report

Updated: 2026-11-05 09:26 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           97
passed SCOUT         1
  killed by SCORE    0
  killed by AUDIT    0
FINAL PASS           1

top kill reasons at first sighting (a pool can have several):
  volume_below_liquidity          70
  few_unique_buyers               66
  too_young                       63
  liquidity_low                   59
  wash_churn                      31
  sells_dominate                  25
  too_old                         24
  overheated                      11

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    1      -        -        -        -       0%
KILLED (tracked)             45      -        -        -        -       0%

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

Sampling is every scan cycle (~5 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
