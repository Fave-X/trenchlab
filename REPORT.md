# TrenchLab report

Updated: 2026-11-07 05:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           10892
passed SCOUT         28
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           20

top kill reasons at first sighting (a pool can have several):
  too_young                    10537
  few_unique_buyers            10269
  liquidity_low                 9897
  volume_below_liquidity        7698
  sells_dominate                3181
  wash_churn                    2227
  overheated                     923
  missing                        362
  too_old                        303
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 684 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   20    -5.6%   -21.3%   -44.4%   -60.1%    30%
SCOUT PASS, killed later      8    +6.2%    +6.7%   -73.5%   +72.1%    25%
KILLED (tracked)           1583    -0.1%    -3.2%    -8.1%    +0.5%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
wash_churn                      9    -37.1%       -      56%
too_old                         9     +0.7%     -6.7%     0%
too_young                       7    -94.0%       -      71%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -68.2%    -93.4%    45%
70-79      10    -32.6%     +2.6%    10%
60-69       6    -41.2%       -      33%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       77     -3.3%     -7.6%     +5.7%    18%
<15%       18     +0.6%     +0.4%     -0.8%    33%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -0.6%     +0.8%     0%
bundled     n   +1h med   +4h med  +24h med   rug%
none       86     -1.9%     -1.1%     +2.6%    10%
<20%       14     +3.2%    -51.7%    -34.6%    64%
20%+        4    +24.1%    -99.0%       -      50%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%       99     -1.9%     -2.0%     +2.6%    18%
20-40%      3    +16.6%    -99.2%       -      67%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 80 | helius credits today: 1286/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   19    21%    -11.1%   -19.9%   -65.0%
   -6%     20%   19    21%    -11.1%   -19.9%   -65.0%
   -6%     30%   19    21%    -11.1%   -19.9%   -65.0%
  -10%     12%   19    21%    -13.4%   -21.0%   -65.0%
  -10%     20%   19    21%    -13.4%   -21.0%   -65.0%
  -10%     30%   19    21%    -13.4%   -21.0%   -65.0%
  -15%     12%   19    21%    -13.8%   -21.3%   -65.0%
  -15%     20%   19    21%    -13.8%   -21.3%   -65.0%
  -15%     30%   19    21%    -13.8%   -21.3%   -65.0%
  -25%     12%   19    26%    -15.7%   -29.2%   -67.1%
  -25%     20%   19    26%    -19.3%   -29.9%   -76.1%
  -25%     30%   19    21%    -21.8%   -31.0%   -76.1%
  best so far: stop -6%, trail from +12% -> avg -11.1% per trade over n=19
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $479.22       $500.00
return                         -4.2%         +0.0%
closed trades                      6             0
win rate                         33%             -
avg net / trade               -13.3%             -
expectancy $/trade            $-3.36             -
max drawdown                   -5.2%          0.0%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $479.22 (-4.2%) | cash $455.87 | open 1 | max drawdown -5.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 6 | win 2/6 (33%) | avg net -13.3% | realized $-20.14 | expectancy $-3.36/trade
exits: stop 3, trail 3
  (n=6 < 100: noise, not evidence)
open:
  Alice        cost $23.99  now $23.34 (-2.7%)  held 0.0h
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 44, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: - | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $500.00 (+0.0%) | cash $500.00 | open 0 | max drawdown 0.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 8, setup_rejected:top10_concentrated 3, setup_rejected:dumping_now 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
