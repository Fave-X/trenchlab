# TrenchLab report

Updated: 2026-11-06 10:34 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           4991
passed SCOUT         14
  killed by SCORE    1
  killed by AUDIT    2
FINAL PASS           11

top kill reasons at first sighting (a pool can have several):
  too_young                     4716
  few_unique_buyers             4644
  liquidity_low                 4448
  volume_below_liquidity        3446
  sells_dominate                1489
  wash_churn                    1037
  overheated                     417
  too_old                        241
  missing                        174
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 344 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   11    -6.5%   -13.3%   -38.3%      -       9%
SCOUT PASS, killed later      3    -4.1%   -25.5%   -32.2%      -       0%
KILLED (tracked)            821    +0.0%    -0.9%    -3.9%    -7.4%    22%

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
70-79       6    -29.7%       -       0%
60-69       3       -         -       0%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       27     -7.8%    -32.4%       -      15%
<15%       13     +0.1%     +1.3%     -2.6%    15%
30%+       12     +0.6%     -0.6%    -14.9%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       42     -1.4%     -0.4%     -8.7%     7%
<20%       10     -7.8%    -11.9%       -      30%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       52     -1.4%     -0.4%     -8.7%    12%
tokens analysed: 35 | helius credits today: 1533/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   11    18%     -4.5%   -18.7%   -29.2%
   -6%     20%   11    18%     -4.5%   -18.7%   -29.2%
   -6%     30%   11    18%     -4.5%   -18.7%   -29.2%
  -10%     12%   11    18%     -8.5%   -20.1%   -44.6%
  -10%     20%   11    18%     -8.5%   -20.1%   -44.6%
  -10%     30%   11    18%     -8.5%   -20.1%   -44.6%
  -15%     12%   11    18%     -9.2%   -21.0%   -44.6%
  -15%     20%   11    18%     -9.2%   -21.0%   -44.6%
  -15%     30%   11    18%     -9.2%   -21.0%   -44.6%
  -25%     12%   11    18%    -13.7%   -29.2%   -67.1%
  -25%     20%   11    18%    -15.3%   -29.2%   -67.1%
  -25%     30%   11    18%    -15.3%   -29.2%   -67.1%
  best so far: stop -6%, trail from +12% -> avg -4.5% per trade over n=11
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $489.03 (-2.2%) | cash $489.03 | open 0 | max drawdown -2.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 1 | win 0/1 (0%) | avg net -43.9% | realized $-10.97 | expectancy $-10.97/trade
exits: stop 1
  (n=1 < 100: noise, not evidence)
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
signals skipped by the sizer/risk rules: already_traded_token 9

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
