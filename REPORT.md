# TrenchLab report

Updated: 2026-11-06 22:01 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           8629
passed SCOUT         22
  killed by SCORE    2
  killed by AUDIT    4
FINAL PASS           16

top kill reasons at first sighting (a pool can have several):
  too_young                     8303
  few_unique_buyers             8126
  liquidity_low                 7809
  volume_below_liquidity        6057
  sells_dominate                2541
  wash_churn                    1791
  overheated                     729
  missing                        299
  too_old                        280
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 551 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   16    -5.7%   -21.3%   -44.4%   -73.6%    31%
SCOUT PASS, killed later      6   +28.2%    +3.0%   -65.8%      -      33%
KILLED (tracked)           1267    -0.0%    -2.2%    -7.9%    -1.5%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         5     +0.2%     -6.7%     0%
too_young                       5    -98.9%       -     100%
volume_below_liquidity          3     +5.9%    -39.4%    33%
liquidity_low                   3    -86.9%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         8    -58.2%    -73.6%    50%
70-79       9    -32.6%       -      11%
60-69       4    -39.9%       -      50%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       54     -2.5%     -9.1%     +4.9%    20%
<15%       15     +0.3%     +0.9%     +7.9%    40%
30%+        7     -1.4%     -0.6%     +1.1%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       63     -1.7%     -0.2%     +2.6%    13%
<20%       11     -7.8%    -48.2%       -      64%
20%+        2    +31.6%    -99.5%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       74     -1.8%     -0.4%     +2.6%    20%
20-40%      2    +31.6%    -99.5%       -     100%
tokens analysed: 56 | helius credits today: 3618/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   16    12%    -12.0%   -20.0%   -51.8%
   -6%     20%   16    12%    -12.0%   -20.0%   -51.8%
   -6%     30%   16    12%    -12.0%   -20.0%   -51.8%
  -10%     12%   16    12%    -14.8%   -21.2%   -51.8%
  -10%     20%   16    12%    -14.8%   -21.2%   -51.8%
  -10%     30%   16    12%    -14.8%   -21.2%   -51.8%
  -15%     12%   16    12%    -15.3%   -22.9%   -51.8%
  -15%     20%   16    12%    -15.3%   -22.9%   -51.8%
  -15%     30%   16    12%    -15.3%   -22.9%   -51.8%
  -25%     12%   16    19%    -17.5%   -29.5%   -67.1%
  -25%     20%   16    19%    -21.8%   -29.9%   -76.1%
  -25%     30%   16    12%    -24.8%   -31.0%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -12.0% per trade over n=16
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $483.79 (-3.2%) | cash $483.79 | open 0 | max drawdown -3.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 0/3 (0%) | avg net -21.8% | realized $-16.21 | expectancy $-5.40/trade
exits: stop 2, trail 1
  (n=3 < 100: noise, not evidence)
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
signals skipped by the sizer/risk rules: already_traded_token 38, daily_loss_limit 29

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
