# TrenchLab report

Updated: 2026-11-07 01:31 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           9734
passed SCOUT         25
  killed by SCORE    2
  killed by AUDIT    5
FINAL PASS           18

top kill reasons at first sighting (a pool can have several):
  too_young                     9389
  few_unique_buyers             9186
  liquidity_low                 8838
  volume_below_liquidity        6874
  sells_dominate                2893
  wash_churn                    1991
  overheated                     809
  missing                        329
  too_old                        294
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 595 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   18    -5.6%   -21.3%   -46.5%   -93.4%    28%
SCOUT PASS, killed later      7   +13.9%    -3.3%   -86.4%   +72.1%    29%
KILLED (tracked)           1394    -0.0%    -2.5%    -7.0%    +0.0%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      9    -37.1%       -      56%
too_old                         8     +0.2%     -6.7%     0%
too_young                       7    -94.0%       -      71%
volume_below_liquidity          4     +5.9%     -4.6%    25%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+         9    -70.4%    -93.4%    44%
70-79      10    -38.7%       -      10%
60-69       5    -80.1%       -      40%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       73     -2.9%    -11.0%     +6.4%    15%
<15%       16     +0.3%     +0.4%     +7.8%    38%
15-30%      1   +442.6%       -         -       0%
30%+        7     -1.4%     -0.6%     +0.8%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       81     -1.9%     -0.4%     +2.6%    10%
<20%       13     -2.3%    -55.2%    -34.6%    54%
20%+        3    +31.6%    -99.5%       -      67%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       93     -1.9%     -2.2%     +2.6%    16%
20-40%      2    -33.5%    -99.5%       -     100%
40%+        2   +442.6%       -         -       0%
tokens analysed: 73 | helius credits today: 526/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   18    22%     -5.9%   -19.3%   -51.8%
   -6%     20%   18    22%     -5.9%   -19.3%   -51.8%
   -6%     30%   18    22%     -5.9%   -19.3%   -51.8%
  -10%     12%   18    22%     -8.4%   -20.6%   -51.8%
  -10%     20%   18    22%     -8.4%   -20.6%   -51.8%
  -10%     30%   18    22%     -8.4%   -20.6%   -51.8%
  -15%     12%   18    22%     -8.8%   -21.2%   -51.8%
  -15%     20%   18    22%     -8.8%   -21.2%   -51.8%
  -15%     30%   18    22%     -8.8%   -21.2%   -51.8%
  -25%     12%   18    28%    -10.8%   -25.3%   -67.1%
  -25%     20%   18    28%    -14.6%   -29.5%   -76.1%
  -25%     30%   18    22%    -17.3%   -30.4%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -5.9% per trade over n=18
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
PAPER TRADER  (pricing: model; start $500.00)
================================================================
equity $505.57 (+1.1%) | cash $434.99 | open 2 | max drawdown -3.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 0/3 (0%) | avg net -21.8% | realized $-16.21 | expectancy $-5.40/trade
exits: stop 2, trail 1
  (n=3 < 100: noise, not evidence)
open:
  DCAT         cost $24.19  now $38.09 (+57.5%)  held 1.5h
  José         cost $24.61  now $32.49 (+32.0%)  held 0.2h
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
signals skipped by the sizer/risk rules: already_traded_token 40, daily_loss_limit 31, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
