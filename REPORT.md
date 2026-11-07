# TrenchLab report

Updated: 2026-11-07 08:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           11949
passed SCOUT         29
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           21

top kill reasons at first sighting (a pool can have several):
  too_young                    11582
  few_unique_buyers            11222
  liquidity_low                10863
  volume_below_liquidity        8405
  sells_dominate                3437
  wash_churn                    2493
  overheated                    1053
  missing                        381
  too_old                        311
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 755 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   21    -5.5%   -17.3%   -44.4%   -66.4%    33%
SCOUT PASS, killed later      8    +6.2%    +6.7%   -86.2%   +72.1%    38%
KILLED (tracked)           1778    -0.0%    -3.4%    -9.8%    +0.8%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_old                        10     +0.2%     -6.7%     0%
wash_churn                      9    -37.1%       -      56%
too_young                       9    -94.0%       -      67%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -72.7%    -93.4%    64%
70-79      11    -31.2%    -31.9%     9%
60-69       6    -41.2%       -      33%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       86     -2.4%     -8.3%     +4.9%    19%
<15%       23     +0.8%     -2.0%     -0.8%    35%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -1.0%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none       94     -1.9%     -2.0%     +2.6%    12%
<20%       20     +5.4%    -51.7%    -96.6%    55%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      113     -1.7%     -2.8%     +1.8%    19%
20-40%      3    +16.6%    -99.0%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 93 | helius credits today: 2174/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   21    24%    -10.1%   -18.7%   -65.0%
   -6%     20%   21    24%    -10.1%   -18.7%   -65.0%
   -6%     30%   21    29%     -4.1%   -18.7%   -65.0%
  -10%     12%   21    24%    -12.2%   -20.1%   -65.0%
  -10%     20%   21    24%    -12.2%   -20.1%   -65.0%
  -10%     30%   21    29%     -6.2%   -20.1%   -65.0%
  -15%     12%   21    24%    -12.6%   -21.0%   -65.0%
  -15%     20%   21    24%    -12.6%   -21.0%   -65.0%
  -15%     30%   21    29%     -6.6%   -21.0%   -65.0%
  -25%     12%   21    29%    -14.3%   -21.3%   -67.1%
  -25%     20%   21    29%    -17.6%   -29.2%   -76.1%
  -25%     30%   21    29%    -13.8%   -29.9%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -4.1% per trade over n=21
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $510.82       $522.88
return                         +2.2%         +4.6%
closed trades                      7             3
win rate                         43%           33%
avg net / trade                +6.7%        +31.2%
expectancy $/trade            $+1.46        $+7.63
max drawdown                   -5.4%         -3.8%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $510.82 (+2.2%) | cash $484.74 | open 1 | max drawdown -5.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 7 | win 3/7 (43%) | avg net +6.7% | realized $+10.25 | expectancy $+1.46/trade
exits: trail 4, stop 3
  (n=7 < 100: noise, not evidence)
open:
  SLINGFOLIO   cost $25.51  now $26.08 (+2.2%)  held 0.2h
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
signals skipped by the sizer/risk rules: already_traded_token 60, daily_loss_limit 31, max_open_positions 1

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
signals skipped by the sizer/risk rules: setup_rejected:top10_concentrated 14, setup_rejected:few_buyers_now 14, setup_rejected:dumping_now 3, setup_rejected:sellers_dominate_now 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
