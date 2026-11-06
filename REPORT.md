# TrenchLab report

Updated: 2026-11-06 07:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           4078
passed SCOUT         12
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           10

top kill reasons at first sighting (a pool can have several):
  too_young                     3855
  few_unique_buyers             3795
  liquidity_low                 3637
  volume_below_liquidity        2804
  sells_dominate                1228
  wash_churn                     800
  overheated                     325
  too_old                        191
  missing                        140
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   10    -8.7%    -6.8%   -44.0%      -      10%
SCOUT PASS, killed later      2    -1.2%   -25.5%   -32.2%      -       0%
KILLED (tracked)            665    +0.0%    -0.7%    -0.7%      -      60%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      88%
volume_below_liquidity          3     +5.9%       -      33%
too_old                         3     -3.0%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -      33%
70-79       5    -31.2%       -       0%
60-69       3       -         -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       22     -6.8%    -32.4%       -      32%
<15%       13     +0.3%     +1.1%       -      15%
30%+       11     +0.6%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       37     -1.3%     -0.3%       -      16%
<20%        9     +5.4%    -29.7%       -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       46     -0.8%     -0.8%       -      20%
tokens analysed: 30 | helius credits today: 1169/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    9    22%     -1.5%   -18.7%   -29.2%
   -6%     20%    9    22%     -1.5%   -18.7%   -29.2%
   -6%     30%    9    22%     -1.5%   -18.7%   -29.2%
  -10%     12%    9    22%     -2.6%   -19.9%   -29.2%
  -10%     20%    9    22%     -2.6%   -19.9%   -29.2%
  -10%     30%    9    22%     -2.6%   -19.9%   -29.2%
  -15%     12%    9    22%     -3.5%   -20.1%   -29.2%
  -15%     20%    9    22%     -3.5%   -20.1%   -29.2%
  -15%     30%    9    22%     -3.5%   -20.1%   -29.2%
  -25%     12%    9    44%     -3.4%   -10.5%   -67.1%
  -25%     20%    9    44%     -3.4%   -10.5%   -67.1%
  -25%     30%    9    44%     -3.4%   -10.5%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -1.5% per trade over n=9
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
