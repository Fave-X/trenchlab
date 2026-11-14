# TrenchLab report

Updated: 2026-11-14 21:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           66260
passed SCOUT         136
  killed by SCORE    18
  killed by AUDIT    31
FINAL PASS           87

top kill reasons at first sighting (a pool can have several):
  too_young                    65051
  few_unique_buyers            62480
  liquidity_low                61137
  volume_below_liquidity       46922
  sells_dominate               17437
  wash_churn                   13533
  overheated                    5730
  missing                       1977
  too_old                        943
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 3815 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   87    -4.2%    -6.8%   -44.0%   -90.4%    59%
SCOUT PASS, killed later     49    +4.3%    +3.4%   -55.0%   -15.3%    45%
KILLED (tracked)           9491    +0.0%   -51.3%   -73.6%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      68    -94.8%    -71.7%    53%
too_old                        33     -0.7%     -0.4%     3%
wash_churn                     23     -1.2%    -71.8%    30%
liquidity_low                  16    -51.1%    -49.8%    50%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        42    -60.4%    -94.0%    71%
70-79      52    -44.7%    -66.4%    50%
60-69      29    -32.0%    -99.8%    45%
<60        13    -32.2%    -15.3%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      432     -0.2%    -10.5%    -32.6%    34%
<15%       89     +0.1%    -11.2%    -32.5%    31%
15-30%     10     -0.6%     -0.7%     +1.0%    30%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      436     -0.2%     -2.3%    -12.8%    28%
<20%      102     -1.5%    -53.7%    -94.9%    45%
20%+       15    +16.6%    -99.0%       -      87%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      531     -0.2%     -4.5%    -16.0%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+        7    -43.5%    -46.3%       -      57%
tokens analysed: 450 | helius credits today: 5289/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   86    24%    -10.3%   -17.1%   -99.7%
   -6%     20%   86    24%    -10.5%   -17.1%   -99.7%
   -6%     30%   86    26%     -8.7%   -17.3%   -99.7%
  -10%     12%   86    27%    -10.1%   -19.4%   -99.7%
  -10%     20%   86    26%    -10.7%   -19.6%   -99.7%
  -10%     30%   86    28%     -8.7%   -19.8%   -99.7%
  -15%     12%   86    29%     -9.6%   -20.0%   -99.7%
  -15%     20%   86    29%     -9.9%   -20.6%   -99.7%
  -15%     30%   86    31%     -7.9%   -20.8%   -99.7%
  -25%     12%   86    34%    -11.8%   -19.2%   -99.7%
  -25%     20%   86    34%    -13.9%   -29.9%   -99.7%
  -25%     30%   86    36%    -12.0%   -30.8%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.9% per trade over n=86
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $417.89       $424.96
return                        -16.4%        -15.0%
closed trades                     52            38
win rate                         25%           21%
avg net / trade                -6.3%         -8.1%
expectancy $/trade            $-1.58        $-1.97
max drawdown                  -23.2%        -21.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $417.89 (-16.4%) | cash $417.89 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 52 | win 13/52 (25%) | avg net -6.3% | realized $-82.11 | expectancy $-1.58/trade
exits: stop 37, trail 15
  (n=52 < 100: noise, not evidence)
last trades:
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
  Speed        $22.14 -> $17.72 (-20.0%)  stop  1.3h
  BAWSAQ       $21.91 -> $27.10 (+23.7%)  trail  0.8h
  CSI          $22.17 -> $16.28 (-26.6%)  stop  0.2h
  SWJ          $21.88 -> $19.15 (-12.5%)  stop  0.2h
  tinfoil      $21.88 -> $28.30 (+29.3%)  trail  0.3h
  GTA$         $22.06 -> $16.78 (-24.0%)  stop  0.2h
  billie       $21.80 -> $3.70 (-83.0%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 306, daily_loss_limit 227, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $424.96 (-15.0%) | cash $424.96 | open 0 | max drawdown -21.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 38 | win 8/38 (21%) | avg net -8.1% | realized $-75.04 | expectancy $-1.97/trade
exits: stop 30, trail 8
  (n=38 < 100: noise, not evidence)
last trades:
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
  FOOD         $21.41 -> $18.94 (-11.6%)  stop  0.3h
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 255, daily_loss_limit 207, setup_rejected:sellers_dominate_now 112, setup_rejected:dumping_now 84, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 24, setup_rejected:operator_cluster 15, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
