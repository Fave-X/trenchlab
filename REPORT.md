# TrenchLab report

Updated: 2026-11-06 20:15 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           8034
passed SCOUT         18
  killed by SCORE    1
  killed by AUDIT    3
FINAL PASS           14

top kill reasons at first sighting (a pool can have several):
  too_young                     7715
  few_unique_buyers             7555
  liquidity_low                 7246
  volume_below_liquidity        5622
  sells_dominate                2373
  wash_churn                    1676
  overheated                     672
  missing                        290
  too_old                        274
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 519 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   14    -5.5%   -17.3%   -44.0%      -      29%
SCOUT PASS, killed later      4    -1.2%    +3.0%   -32.2%      -       0%
KILLED (tracked)           1186    +0.0%    -2.3%    -7.0%    -2.6%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      8    -37.1%       -      62%
too_old                         5     +0.2%       -       0%
too_young                       4    -98.9%       -     100%
volume_below_liquidity          3     +5.9%    -39.4%    33%
liquidity_low                   3    -86.9%       -      33%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         6    -48.2%       -      33%
70-79       8    -31.2%       -      12%
60-69       3    -39.9%       -      33%
<60         1    -32.2%       -       0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       51     -2.4%     -7.6%     +4.9%    18%
<15%       13     +0.1%     +1.1%     +7.9%    31%
30%+        7     -1.4%     -0.6%     +2.6%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       61     -1.5%     -0.2%     +3.8%    11%
<20%        9    -22.2%    -48.2%       -      67%
20%+        1    +31.6%       -         -       0%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       70     -1.7%     -0.4%     +3.8%    19%
20-40%      1    +31.6%       -         -       0%
tokens analysed: 51 | helius credits today: 3187/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   14    14%    -10.1%   -19.3%   -51.8%
   -6%     20%   14    14%    -10.1%   -19.3%   -51.8%
   -6%     30%   14    14%    -10.1%   -19.3%   -51.8%
  -10%     12%   14    14%    -13.2%   -20.6%   -51.8%
  -10%     20%   14    14%    -13.2%   -20.6%   -51.8%
  -10%     30%   14    14%    -13.2%   -20.6%   -51.8%
  -15%     12%   14    14%    -13.8%   -22.7%   -51.8%
  -15%     20%   14    14%    -13.8%   -22.7%   -51.8%
  -15%     30%   14    14%    -13.8%   -22.7%   -51.8%
  -25%     12%   14    21%    -16.3%   -29.5%   -67.1%
  -25%     20%   14    21%    -21.3%   -30.4%   -76.1%
  -25%     30%   14    14%    -24.0%   -31.1%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -10.1% per trade over n=14
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
signals skipped by the sizer/risk rules: already_traded_token 38, daily_loss_limit 15

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
