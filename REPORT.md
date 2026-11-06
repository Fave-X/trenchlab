# TrenchLab report

Updated: 2026-11-06 07:10 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           3929
passed SCOUT         11
  killed by SCORE    2
  killed by AUDIT    1
FINAL PASS           8

top kill reasons at first sighting (a pool can have several):
  too_young                     3707
  few_unique_buyers             3657
  liquidity_low                 3503
  volume_below_liquidity        2704
  sells_dominate                1182
  wash_churn                     771
  overheated                     311
  too_old                        191
  missing                        132
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    8    -9.4%    -6.8%   -44.0%      -      12%
SCOUT PASS, killed later      3   +60.4%   +60.4%   +60.4%      -      33%
KILLED (tracked)            641    +2.2%    +1.0%    +0.5%      -      57%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8     +0.5%       -     100%
volume_below_liquidity          3     +5.9%       -      33%
too_old                         3     -3.0%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -      33%
70-79       4    -29.7%       -      25%
60-69       2       -         -       0%
<60         2   +706.9%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       21     -2.1%    -11.0%       -      38%
<15%       13     +0.3%     +1.1%       -      15%
30%+        7     -1.4%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       33     -1.4%     -0.1%       -      18%
<20%        8     +6.5%    -11.9%       -      50%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       41     -1.3%     -0.1%       -      24%
tokens analysed: 28 | helius credits today: 989/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    7    29%     +3.6%   -17.1%   -29.2%
   -6%     20%    7    29%     +3.6%   -17.1%   -29.2%
   -6%     30%    7    29%     +3.6%   -17.1%   -29.2%
  -10%     12%    7    29%     +2.2%   -20.1%   -29.2%
  -10%     20%    7    29%     +2.2%   -20.1%   -29.2%
  -10%     30%    7    29%     +2.2%   -20.1%   -29.2%
  -15%     12%    7    29%     +1.1%   -21.0%   -29.2%
  -15%     20%    7    29%     +1.1%   -21.0%   -29.2%
  -15%     30%    7    29%     +1.1%   -21.0%   -29.2%
  -25%     12%    7    29%     -7.4%   -29.2%   -67.1%
  -25%     20%    7    29%     -7.4%   -29.2%   -67.1%
  -25%     30%    7    29%     -7.4%   -29.2%   -67.1%
  best so far: stop -6%, trail from +12% -> avg +3.6% per trade over n=7
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
