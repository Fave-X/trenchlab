# TrenchLab report

Updated: 2026-11-06 16:31 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           6843
passed SCOUT         16
  killed by SCORE    1
  killed by AUDIT    2
FINAL PASS           13

top kill reasons at first sighting (a pool can have several):
  too_young                     6549
  few_unique_buyers             6411
  liquidity_low                 6193
  volume_below_liquidity        4771
  sells_dominate                2058
  wash_churn                    1460
  overheated                     573
  too_old                        255
  missing                        201
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 460 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   13    -5.5%   -10.6%   -44.0%      -      23%
SCOUT PASS, killed later      3    -4.1%   -25.5%   -32.2%      -       0%
KILLED (tracked)           1025    +0.0%    -1.4%    -3.0%    -9.8%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         5     -1.4%       -       0%
too_young                       4    -98.9%       -      75%
volume_below_liquidity          3     +5.9%       -      33%
liquidity_low                   3    -84.9%       -      33%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         5    -48.2%       -      40%
70-79       7    -31.2%       -       0%
60-69       3    -39.9%       -      33%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       41     -2.4%     -0.3%    +39.9%    17%
<15%       12     +0.1%     +1.1%     -2.6%    25%
30%+       12     +0.1%     -0.4%    -14.9%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       56     -1.3%     +0.2%     -2.6%    11%
<20%        8     -7.8%    -48.2%       -      50%
20%+        1       -         -         -       0%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       64     -1.4%     -0.1%     -2.6%    16%
20-40%      1       -         -         -       0%
tokens analysed: 45 | helius credits today: 2626/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   13    15%     -8.5%   -18.7%   -51.8%
   -6%     20%   13    15%     -8.5%   -18.7%   -51.8%
   -6%     30%   13    15%     -8.5%   -18.7%   -51.8%
  -10%     12%   13    15%    -11.9%   -20.1%   -51.8%
  -10%     20%   13    15%    -11.9%   -20.1%   -51.8%
  -10%     30%   13    15%    -11.9%   -20.1%   -51.8%
  -15%     12%   13    15%    -12.5%   -21.0%   -51.8%
  -15%     20%   13    15%    -12.5%   -21.0%   -51.8%
  -15%     30%   13    15%    -12.5%   -21.0%   -51.8%
  -25%     12%   13    23%    -15.3%   -29.2%   -67.1%
  -25%     20%   13    23%    -20.6%   -31.0%   -76.1%
  -25%     30%   13    15%    -22.0%   -31.0%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -8.5% per trade over n=13
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
signals skipped by the sizer/risk rules: already_traded_token 35, daily_loss_limit 2

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
