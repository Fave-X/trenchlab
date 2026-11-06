# TrenchLab report

Updated: 2026-11-06 03:21 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           2795
passed SCOUT         8
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           6

top kill reasons at first sighting (a pool can have several):
  too_young                     2627
  few_unique_buyers             2586
  liquidity_low                 2474
  volume_below_liquidity        1892
  sells_dominate                 863
  wash_churn                     580
  overheated                     230
  too_old                        141
  missing                        102
  score_below                      1

OUTCOMES (median price change from first sighting / first pass)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                    6   -12.8%    -6.8%   -56.1%      -      17%
SCOUT PASS, killed later      2   +29.6%   +17.5%   +14.1%      -      50%
KILLED (tracked)            459    +0.7%    +0.4%    +0.9%      -      52%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -49.3%       -      75%
volume_below_liquidity          3       -         -       0%
too_old                         3     -3.0%       -       0%
too_young                       3       -         -      67%
liquidity_low                   1    -82.9%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         3    -56.1%       -      33%
70-79       3    +60.4%       -      33%
60-69       1       -         -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       20     -1.9%     -0.1%       -      25%
<15%       11     +0.1%     +1.3%       -       9%
30%+        6     -1.5%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       31     -1.4%     +0.3%       -      13%
<20%        6     +6.5%     +6.5%       -      33%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       37     -1.3%     +0.4%       -      16%
tokens analysed: 25 | helius credits today: 802/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%    6    17%     -5.2%   -18.6%   -29.2%
   -6%     20%    6    17%     -5.2%   -18.6%   -29.2%
   -6%     30%    6    17%     -5.2%   -18.6%   -29.2%
  -10%     12%    6    17%     -5.2%   -18.6%   -29.2%
  -10%     20%    6    17%     -5.2%   -18.6%   -29.2%
  -10%     30%    6    17%     -5.2%   -18.6%   -29.2%
  -15%     12%    6    17%     -6.5%   -22.2%   -29.2%
  -15%     20%    6    17%     -6.5%   -22.2%   -29.2%
  -15%     30%    6    17%     -6.5%   -22.2%   -29.2%
  -25%     12%    6    17%    -13.0%   -19.9%   -67.1%
  -25%     20%    6    17%    -13.0%   -19.9%   -67.1%
  -25%     30%    6    17%    -13.0%   -19.9%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -5.2% per trade over n=6
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
