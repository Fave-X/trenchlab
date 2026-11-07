# TrenchLab report

Updated: 2026-11-07 10:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           12647
passed SCOUT         29
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           21

top kill reasons at first sighting (a pool can have several):
  too_young                    12276
  few_unique_buyers            11865
  liquidity_low                11518
  volume_below_liquidity        8886
  sells_dominate                3615
  wash_churn                    2665
  overheated                    1123
  missing                        390
  too_old                        314
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 798 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   21    -5.6%   -13.3%   -44.0%   -79.8%    33%
SCOUT PASS, killed later      8    +6.2%    +6.7%   -86.2%   +72.1%    38%
KILLED (tracked)           1887    -0.0%    -3.5%   -13.9%    +1.2%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      12    -94.0%       -      50%
too_old                        10     -0.1%     -6.7%     0%
wash_churn                      9    -37.1%       -      56%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -72.7%    -93.3%    64%
70-79      11    -29.7%    -31.9%     9%
60-69       6    -41.2%       -      33%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       90     -2.4%     -7.3%     +3.7%    19%
<15%       23     +0.8%     +0.7%     -0.8%    35%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -1.0%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none       97     -1.9%     -1.4%     +2.6%    11%
<20%       21     +7.5%    -44.7%    -94.9%    57%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      117     -1.7%     -1.7%     +1.1%    20%
20-40%      3    +16.6%    -99.0%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 97 | helius credits today: 2660/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   21    19%    -11.0%   -18.7%   -65.0%
   -6%     20%   21    19%    -11.0%   -18.7%   -65.0%
   -6%     30%   21    24%     -5.0%   -18.7%   -65.0%
  -10%     12%   21    19%    -13.1%   -20.1%   -65.0%
  -10%     20%   21    19%    -13.1%   -20.1%   -65.0%
  -10%     30%   21    24%     -7.1%   -20.1%   -65.0%
  -15%     12%   21    19%    -13.6%   -21.0%   -65.0%
  -15%     20%   21    19%    -13.6%   -21.0%   -65.0%
  -15%     30%   21    24%     -7.6%   -21.0%   -65.0%
  -25%     12%   21    24%    -15.7%   -29.1%   -67.1%
  -25%     20%   21    24%    -19.0%   -29.2%   -76.1%
  -25%     30%   21    24%    -15.3%   -29.9%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -5.0% per trade over n=21
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $506.15       $522.88
return                         +1.2%         +4.6%
closed trades                      8             3
win rate                         38%           33%
avg net / trade                +3.8%        +31.2%
expectancy $/trade            $+0.77        $+7.63
max drawdown                   -5.4%         -3.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $506.15 (+1.2%) | cash $506.15 | open 0 | max drawdown -5.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 8 | win 3/8 (38%) | avg net +3.8% | realized $+6.15 | expectancy $+0.77/trade
exits: stop 4, trail 4
  (n=8 < 100: noise, not evidence)
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 64, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $522.88 (+4.6%) | cash $522.88 | open 0 | max drawdown -3.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 1/3 (33%) | avg net +31.2% | realized $+22.88 | expectancy $+7.63/trade
exits: stop 2, trail 1
  (n=3 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 23, setup_rejected:top10_concentrated 14, setup_rejected:volume_dried_up 9, setup_rejected:dumping_now 4, setup_rejected:sellers_dominate_now 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
