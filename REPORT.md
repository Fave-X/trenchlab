# TrenchLab report

Updated: 2026-11-12 23:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           52626
passed SCOUT         116
  killed by SCORE    15
  killed by AUDIT    25
FINAL PASS           76

top kill reasons at first sighting (a pool can have several):
  too_young                    51553
  few_unique_buyers            49593
  liquidity_low                48667
  volume_below_liquidity       37398
  sells_dominate               13806
  wash_churn                   10503
  overheated                    4470
  missing                       1400
  too_old                        855
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 2883 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   76    -4.4%    -7.8%   -44.4%   -91.5%    61%
SCOUT PASS, killed later     40    +4.6%    +1.3%   -52.8%   +22.4%    45%
KILLED (tracked)           7860    +0.0%   -37.2%   -66.6%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      52    -94.8%    -71.7%    54%
too_old                        25     -0.4%     -0.4%     4%
liquidity_low                  15    -40.0%    -49.8%    40%
wash_churn                     14    +11.9%    -71.8%    36%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      4    -12.8%    -79.6%    75%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        38    -63.7%    -94.5%    76%
70-79      42    -44.7%    -66.4%    48%
60-69      25    -32.0%    -99.8%    48%
<60        11    -32.2%    +22.4%    27%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      348     -0.4%    -11.7%    -23.6%    35%
<15%       76     +0.2%    -11.7%    -12.4%    33%
15-30%      8     -0.6%     -0.7%     +1.0%    38%
30%+       18     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      349     -0.3%     -3.0%     -9.3%    29%
<20%       89     -0.3%    -49.5%    -96.6%    45%
20%+       12    +17.1%    -99.0%       -      92%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      433     -0.3%     -7.2%    -11.6%    32%
20-40%     13     -4.5%    -99.0%    -99.1%    77%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 365 | helius credits today: 4690/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   76    22%    -11.8%   -17.3%   -99.7%
   -6%     20%   76    24%    -11.8%   -17.3%   -99.7%
   -6%     30%   76    25%     -9.7%   -18.5%   -99.7%
  -10%     12%   76    24%    -12.6%   -19.6%   -99.7%
  -10%     20%   76    24%    -13.1%   -19.8%   -99.7%
  -10%     30%   76    26%    -10.8%   -20.0%   -99.7%
  -15%     12%   76    25%    -12.2%   -20.1%   -99.7%
  -15%     20%   76    26%    -12.8%   -20.6%   -99.7%
  -15%     30%   76    29%    -10.5%   -20.9%   -99.7%
  -25%     12%   76    30%    -13.9%   -24.6%   -99.7%
  -25%     20%   76    32%    -16.1%   -29.9%   -99.7%
  -25%     30%   76    34%    -14.0%   -30.8%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -9.7% per trade over n=76
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $411.00       $431.91
return                        -17.8%        -13.6%
closed trades                     40            33
win rate                         22%           21%
avg net / trade                -9.3%         -8.6%
expectancy $/trade            $-2.23        $-2.06
max drawdown                  -20.9%        -21.0%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $411.00 (-17.8%) | cash $411.00 | open 0 | max drawdown -20.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 40 | win 9/40 (22%) | avg net -9.3% | realized $-89.00 | expectancy $-2.23/trade
exits: stop 29, trail 11
  (n=40 < 100: noise, not evidence)
last trades:
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
  DACITY       $21.58 -> $14.66 (-32.0%)  stop  8.3h
  NIHAONOON    $21.56 -> $21.56 (-0.0%)  trail  0.3h
  Max          $21.56 -> $18.83 (-12.7%)  stop  0.7h
  AIB          $21.42 -> $17.45 (-18.6%)  stop  0.2h
  MAX          $21.22 -> $16.96 (-20.1%)  stop  0.2h
  BITCOINU     $21.01 -> $11.81 (-43.8%)  stop  0.2h
signals skipped by the sizer/risk rules: daily_loss_limit 226, already_traded_token 200, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $431.91 (-13.6%) | cash $431.91 | open 0 | max drawdown -21.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 33 | win 7/33 (21%) | avg net -8.6% | realized $-68.09 | expectancy $-2.06/trade
exits: stop 26, trail 7
  (n=33 < 100: noise, not evidence)
last trades:
  NOBUSHIBA    $22.79 -> $20.46 (-10.2%)  stop  7.0h
  pants        $22.47 -> $19.96 (-11.2%)  stop  0.5h
  Max          $22.16 -> $19.66 (-11.3%)  stop  0.2h
  NIHAONOON    $22.04 -> $19.02 (-13.7%)  stop  0.3h
  AIB          $21.89 -> $22.83 (+4.3%)  trail  0.8h
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 192, daily_loss_limit 118, setup_rejected:sellers_dominate_now 86, setup_rejected:dumping_now 53, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:operator_cluster 2, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
