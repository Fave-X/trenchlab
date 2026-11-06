# TrenchLab report

Updated: 2026-11-06 05:31 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           3446
passed SCOUT         10
  killed by SCORE    2
  killed by AUDIT    1
FINAL PASS           7

top kill reasons at first sighting (a pool can have several):
  too_young                     3242
  few_unique_buyers             3202
  liquidity_low                 3063
  volume_below_liquidity        2362
  sells_dominate                1048
  wash_churn                     686
  overheated                     271
  too_old                        175
  missing                        119
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    7    -9.4%    -6.8%   -56.1%      -      14%
SCOUT PASS, killed later      3   +60.4%   +60.4%   +60.4%      -      33%
KILLED (tracked)            565    +1.1%    +0.7%    +0.6%      -      55%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -99.0%       -      75%
volume_below_liquidity          3     +5.9%       -      33%
too_old                         3     -3.0%       -      33%
too_young                       3    -94.3%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -      33%
70-79       4    +15.4%       -      25%
60-69       1       -         -       0%
<60         2   +706.9%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       20     -2.2%     -5.5%       -      35%
<15%       12     +0.3%     +0.9%       -       8%
30%+        6     -1.5%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       31     -1.5%     -0.1%       -      16%
<20%        7     +6.5%    -11.9%       -      43%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       38     -1.4%     -0.1%       -      21%
tokens analysed: 26 | helius credits today: 885/25000

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
