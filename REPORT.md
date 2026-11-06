# TrenchLab report

Updated: 2026-11-06 09:11 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           4543
passed SCOUT         13
  killed by SCORE    1
  killed by AUDIT    1
FINAL PASS           11

top kill reasons at first sighting (a pool can have several):
  too_young                     4284
  few_unique_buyers             4233
  liquidity_low                 4054
  volume_below_liquidity        3150
  sells_dominate                1374
  wash_churn                     932
  overheated                     375
  too_old                        226
  missing                        147
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 307 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   11    -6.5%   -10.6%   -38.3%      -       9%
SCOUT PASS, killed later      2    -1.2%   -25.5%   -32.2%      -       0%
KILLED (tracked)            747    +0.0%    -0.8%    -3.9%      -      22%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         4     -3.0%       -       0%
volume_below_liquidity          3     +5.9%       -      33%
too_young                       3    -98.9%       -     100%
liquidity_low                   1    -82.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         4    -68.2%       -      25%
70-79       5    -29.7%       -       0%
60-69       3       -         -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       24     -7.6%    -32.4%       -      17%
<15%       13     +0.1%     +1.3%       -      15%
30%+       11     +0.6%     -0.8%       -       0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       38     -1.4%     -0.3%       -       8%
<20%       10     -2.3%    -11.9%       -      30%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       48     -1.4%     -0.3%       -      12%
tokens analysed: 32 | helius credits today: 1380/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   11    18%     -4.5%   -18.7%   -29.2%
   -6%     20%   11    18%     -4.5%   -18.7%   -29.2%
   -6%     30%   11    18%     -4.5%   -18.7%   -29.2%
  -10%     12%   11    18%     -5.4%   -19.9%   -29.2%
  -10%     20%   11    18%     -5.4%   -19.9%   -29.2%
  -10%     30%   11    18%     -5.4%   -19.9%   -29.2%
  -15%     12%   11    18%     -6.1%   -20.1%   -29.2%
  -15%     20%   11    18%     -6.1%   -20.1%   -29.2%
  -15%     30%   11    18%     -6.1%   -20.1%   -29.2%
  -25%     12%   11    18%    -11.8%   -19.8%   -67.1%
  -25%     20%   11    18%    -11.3%   -19.8%   -67.1%
  -25%     30%   11    18%    -11.3%   -19.8%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -4.5% per trade over n=11
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $497.70 (-0.5%) | cash $475.00 | open 1 | max drawdown -0.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
open:
  RM           cost $25.00  now $22.70 (-9.2%)  held 0.7h
signals skipped by the sizer/risk rules: already_traded_token 4

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
