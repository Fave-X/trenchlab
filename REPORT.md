# TrenchLab report

Updated: 2026-11-14 09:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           62859
passed SCOUT         130
  killed by SCORE    18
  killed by AUDIT    28
FINAL PASS           84

top kill reasons at first sighting (a pool can have several):
  too_young                    61669
  few_unique_buyers            59264
  liquidity_low                58108
  volume_below_liquidity       44585
  sells_dominate               16573
  wash_churn                   12797
  overheated                    5445
  missing                       1742
  too_old                        931
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 3626 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   84    -3.4%    -6.1%   -43.9%   -90.4%    61%
SCOUT PASS, killed later     46    +3.7%    +2.2%   -55.0%   -15.3%    46%
KILLED (tracked)           9108    +0.0%   -50.0%   -72.3%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      65    -94.8%    -71.7%    54%
too_old                        32     -0.6%     -0.4%     3%
wash_churn                     22    +11.9%    -71.8%    27%
liquidity_low                  16    -51.1%    -49.8%    50%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      5     -3.6%    -79.6%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        41    -60.4%    -94.0%    73%
70-79      49    -42.3%    -66.4%    51%
60-69      27    -32.0%    -99.8%    48%
<60        13    -32.2%    -15.3%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      414     -0.2%    -10.9%    -31.6%    34%
<15%       85     +0.1%    -11.2%    -12.4%    33%
15-30%      9     -1.0%     -1.3%     +1.0%    33%
30%+       22     -0.4%     -0.6%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      419     -0.2%     -2.3%    -12.0%    28%
<20%       96     -1.5%    -55.4%    -96.6%    47%
20%+       15    +16.6%    -99.0%       -      87%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      508     -0.2%     -4.5%    -13.9%    31%
20-40%     16     -4.6%    -99.0%    -99.1%    75%
40%+        6    -98.5%    -98.5%       -      67%
tokens analysed: 430 | helius credits today: 2588/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   84    25%     -9.3%   -15.8%   -99.7%
   -6%     20%   84    25%     -9.5%   -15.8%   -99.7%
   -6%     30%   84    26%     -7.6%   -17.1%   -99.7%
  -10%     12%   84    27%     -9.1%   -19.0%   -99.7%
  -10%     20%   84    26%     -9.7%   -19.4%   -99.7%
  -10%     30%   84    29%     -7.6%   -19.6%   -99.7%
  -15%     12%   84    30%     -8.5%   -19.8%   -99.7%
  -15%     20%   84    30%     -8.8%   -20.4%   -99.7%
  -15%     30%   84    32%     -6.8%   -20.6%   -99.7%
  -25%     12%   84    35%    -10.5%   -15.5%   -99.7%
  -25%     20%   84    35%    -12.6%   -29.8%   -99.7%
  -25%     30%   84    37%    -10.7%   -30.4%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -6.8% per trade over n=84
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $441.27       $424.96
return                        -11.7%        -15.0%
closed trades                     50            38
win rate                         26%           21%
avg net / trade                -4.4%         -8.1%
expectancy $/trade            $-1.17        $-1.97
max drawdown                  -23.2%        -21.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $441.27 (-11.7%) | cash $441.27 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 50 | win 13/50 (26%) | avg net -4.4% | realized $-58.73 | expectancy $-1.17/trade
exits: stop 35, trail 15
  (n=50 < 100: noise, not evidence)
last trades:
  FOOD         $20.06 -> $36.70 (+83.0%)  trail  1.0h
  Sakura       $20.90 -> $48.56 (+132.3%)  trail  1.2h
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
  Speed        $22.14 -> $17.72 (-20.0%)  stop  1.3h
  BAWSAQ       $21.91 -> $27.10 (+23.7%)  trail  0.8h
  CSI          $22.17 -> $16.28 (-26.6%)  stop  0.2h
  SWJ          $21.88 -> $19.15 (-12.5%)  stop  0.2h
  tinfoil      $21.88 -> $28.30 (+29.3%)  trail  0.3h
signals skipped by the sizer/risk rules: already_traded_token 293, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 232, daily_loss_limit 153, setup_rejected:sellers_dominate_now 91, setup_rejected:dumping_now 66, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 13, setup_rejected:operator_cluster 8, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
