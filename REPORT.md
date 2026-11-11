# TrenchLab report

Updated: 2026-11-11 14:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           42682
passed SCOUT         97
  killed by SCORE    11
  killed by AUDIT    21
FINAL PASS           65

top kill reasons at first sighting (a pool can have several):
  too_young                    41757
  few_unique_buyers            40180
  liquidity_low                39351
  volume_below_liquidity       30197
  sells_dominate               11205
  wash_churn                    8849
  overheated                    3686
  missing                       1167
  too_old                        748
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 2258 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   65    -4.6%    -7.3%   -44.0%   -89.9%    57%
SCOUT PASS, killed later     32    +6.2%    +0.2%   -55.0%    +9.6%    47%
KILLED (tracked)           6586    +0.0%   -28.1%   -57.9%    +0.4%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      49    -94.9%    -71.7%    53%
too_old                        23     -0.2%     -2.6%     0%
wash_churn                     13    +11.9%       -      38%
liquidity_low                  12    -29.5%       -      33%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        31    -68.5%    -93.8%    84%
70-79      35    -42.3%    -66.4%    49%
60-69      23    -28.3%    -70.7%    35%
<60         8    -19.6%     +9.6%    12%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      305     -0.6%    -11.0%    -16.0%    34%
<15%       69     +0.1%     -9.8%    -10.8%    30%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      305     -0.3%     -2.9%     -6.1%    28%
<20%       80     -0.8%    -45.0%    -94.9%    45%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      381     -0.3%     -6.6%    -11.3%    31%
20-40%     11     -4.5%    -99.0%       -      82%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 319 | helius credits today: 2944/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   65    25%    -10.3%   -17.1%   -99.7%
   -6%     20%   65    26%    -10.3%   -17.1%   -99.7%
   -6%     30%   65    26%     -8.4%   -17.5%   -99.7%
  -10%     12%   65    26%    -11.3%   -19.3%   -99.7%
  -10%     20%   65    26%    -11.8%   -19.5%   -99.7%
  -10%     30%   65    28%     -9.7%   -19.9%   -99.7%
  -15%     12%   65    28%    -11.0%   -20.1%   -99.7%
  -15%     20%   65    29%    -11.2%   -20.4%   -99.7%
  -15%     30%   65    31%     -9.0%   -20.4%   -99.7%
  -25%     12%   65    32%    -13.2%   -27.9%   -99.7%
  -25%     20%   65    34%    -14.7%   -29.7%   -99.7%
  -25%     30%   65    35%    -12.7%   -30.1%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -8.4% per trade over n=65
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $431.16       $455.28
return                        -13.8%         -8.9%
closed trades                     35            23
win rate                         26%           22%
avg net / trade                -7.9%         -7.7%
expectancy $/trade            $-1.97        $-1.92
max drawdown                  -18.1%        -16.2%
open now                           0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $431.16 (-13.8%) | cash $431.16 | open 0 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 35 | win 9/35 (26%) | avg net -7.9% | realized $-68.84 | expectancy $-1.97/trade
exits: stop 25, trail 10
  (n=35 < 100: noise, not evidence)
last trades:
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
  mihao        $21.42 -> $26.82 (+25.2%)  trail  2.2h
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
  DACITY       $21.58 -> $14.66 (-32.0%)  stop  8.3h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 160, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $455.28 (-8.9%) | cash $432.95 | open 1 | max drawdown -16.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 23 | win 5/23 (22%) | avg net -7.7% | realized $-44.26 | expectancy $-1.92/trade
exits: stop 18, trail 5
  (n=23 < 100: noise, not evidence)
open:
  NOBUSHIBA    cost $22.79  now $22.33 (-2.0%)  held 0.2h
last trades:
  BORLY        $24.22 -> $18.90 (-22.0%)  stop  0.5h
  YouTube      $24.14 -> $0.05 (-99.8%)  stop  0.2h
  MEOW         $23.95 -> $26.31 (+9.9%)  trail  2.8h
  HOLD         $22.86 -> $36.92 (+61.5%)  trail  0.7h
  X            $23.57 -> $20.04 (-15.0%)  stop  0.3h
  If           $23.39 -> $18.22 (-22.1%)  stop  1.5h
  DACITY       $23.13 -> $19.06 (-17.6%)  stop  0.3h
  BABYMINHAO   $23.13 -> $20.29 (-12.3%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 182, daily_loss_limit 118, setup_rejected:sellers_dominate_now 57, setup_rejected:dumping_now 47, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 4, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
