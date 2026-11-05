# TrenchLab report

Updated: 2026-11-05 21:51 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           907
passed SCOUT         4
  killed by SCORE    1
  killed by AUDIT    0
FINAL PASS           3

top kill reasons at first sighting (a pool can have several):
  too_young                      817
  few_unique_buyers              811
  liquidity_low                  766
  volume_below_liquidity         598
  sells_dominate                 300
  wash_churn                     182
  too_old                         73
  overheated                      65
  missing                         29
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    3   -17.0%    -6.8%      -        -       0%
SCOUT PASS, killed later      1      -        -        -        -       0%
KILLED (tracked)            179    +2.8%    +0.7%      -        -      40%

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
80+         2       -         -       0%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none        6     -3.3%       -         -       0%
30%+        5     -1.4%       -         -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none        9     -1.5%       -         -       0%
<20%        2     +1.9%       -         -       0%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       11     -1.4%       -         -       0%
tokens analysed: 7 | helius credits today: 589/25000

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
