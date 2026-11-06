# TrenchLab report

Updated: 2026-11-06 02:01 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           2330
passed SCOUT         7
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           5

top kill reasons at first sighting (a pool can have several):
  too_young                     2168
  few_unique_buyers             2158
  liquidity_low                 2041
  volume_below_liquidity        1583
  sells_dominate                 732
  wash_churn                     487
  overheated                     175
  too_old                        137
  missing                         95
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    5   -12.8%    -2.5%   -56.1%      -      20%
SCOUT PASS, killed later      2   +29.6%   +17.5%      -        -      50%
KILLED (tracked)            388    +0.6%    +0.3%    +1.8%      -      47%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      7    -49.3%       -      86%
volume_below_liquidity          3       -         -       0%
too_old                         3     -7.0%       -       0%
too_young                       2       -         -     100%
liquidity_low                   1    -82.9%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -56.1%       -      33%
70-79       2       -         -      50%
60-69       1       -         -       0%
<60         1       -         -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       17     -2.1%    -27.2%       -      29%
<15%        5     -0.2%     +1.3%       -      20%
30%+        6     -1.5%     -1.4%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       23     -1.8%     -2.2%       -      17%
<20%        5     +4.8%    -30.8%       -      40%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       28     -1.4%     -2.2%       -      21%
tokens analysed: 20 | helius credits today: 316/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    5    20%     -4.8%   -20.1%   -29.2%
   -6%     20%    5    20%     -4.8%   -20.1%   -29.2%
   -6%     30%    5    20%     -4.8%   -20.1%   -29.2%
  -10%     12%    5    20%     -4.8%   -20.1%   -29.2%
  -10%     20%    5    20%     -4.8%   -20.1%   -29.2%
  -10%     30%    5    20%     -4.8%   -20.1%   -29.2%
  -15%     12%    5    20%     -4.4%   -20.1%   -29.2%
  -15%     20%    5    20%     -4.4%   -20.1%   -29.2%
  -15%     30%    5    20%     -4.4%   -20.1%   -29.2%
  -25%     12%    5    20%    -11.0%   -15.0%   -67.1%
  -25%     20%    5    20%    -11.0%   -15.0%   -67.1%
  -25%     30%    5    20%    -11.0%   -15.0%   -67.1%
  best so far: stop -15%, trail from +12% -> avg -4.4% per trade over n=5
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
