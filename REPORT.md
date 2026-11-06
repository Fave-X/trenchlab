# TrenchLab report

Updated: 2026-11-06 04:51 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           3238
passed SCOUT         9
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           7

top kill reasons at first sighting (a pool can have several):
  too_young                     3065
  few_unique_buyers             3010
  liquidity_low                 2897
  volume_below_liquidity        2224
  sells_dominate                 990
  wash_churn                     646
  overheated                     249
  too_old                        145
  missing                        106
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    7    -9.4%    -6.8%   -68.2%      -      14%
SCOUT PASS, killed later      2   +29.6%   +17.5%   +14.1%      -      50%
KILLED (tracked)            512    +1.3%    +0.7%    +0.7%      -      56%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -99.0%       -      75%
volume_below_liquidity          3     +5.9%       -       0%
too_old                         3     -3.0%       -       0%
too_young                       3    -94.3%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -68.2%       -      33%
70-79       4    +60.4%       -      25%
60-69       1       -         -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       20     -2.2%     -5.5%       -      30%
<15%       12     +0.3%     +1.3%       -       8%
30%+        6     -1.5%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       31     -1.5%     +0.1%       -      13%
<20%        7     +6.5%     +5.9%       -      43%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       38     -1.4%     +0.2%       -      18%
tokens analysed: 26 | helius credits today: 885/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    7    29%     +6.5%   -17.1%   -29.2%
   -6%     20%    7    29%     +6.5%   -17.1%   -29.2%
   -6%     30%    7    29%     +6.5%   -17.1%   -29.2%
  -10%     12%    7    29%     +5.0%   -20.1%   -29.2%
  -10%     20%    7    29%     +5.0%   -20.1%   -29.2%
  -10%     30%    7    29%     +5.0%   -20.1%   -29.2%
  -15%     12%    7    29%     +3.9%   -21.0%   -29.2%
  -15%     20%    7    29%     +3.9%   -21.0%   -29.2%
  -15%     30%    7    29%     +3.9%   -21.0%   -29.2%
  -25%     12%    7    29%     -4.5%   -29.2%   -67.1%
  -25%     20%    7    29%     -4.5%   -29.2%   -67.1%
  -25%     30%    7    29%     -4.5%   -29.2%   -67.1%
  best so far: stop -6%, trail from +12% -> avg +6.5% per trade over n=7
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
