# TrenchLab report

Updated: 2026-11-14 04:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           61315
passed SCOUT         128
  killed by SCORE    19
  killed by AUDIT    27
FINAL PASS           82

top kill reasons at first sighting (a pool can have several):
  too_young                    60148
  few_unique_buyers            57813
  liquidity_low                56674
  volume_below_liquidity       43485
  sells_dominate               16179
  wash_churn                   12431
  overheated                    5286
  missing                       1710
  too_old                        921
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 3522 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   82    -4.2%    -6.8%   -44.0%   -90.4%    61%
SCOUT PASS, killed later     46    +3.0%    +1.3%   -52.8%   -15.3%    43%
KILLED (tracked)           8907    +0.0%   -48.7%   -71.7%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      63    -94.8%    -71.7%    54%
too_old                        32     -0.6%     -0.4%     3%
wash_churn                     18     -1.0%    -71.8%    33%
liquidity_low                  16    -51.1%    -49.8%    50%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      5     -3.6%    -79.6%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        39    -63.7%    -94.0%    77%
70-79      49    -39.9%    -66.4%    49%
60-69      26    -35.2%    -99.8%    46%
<60        14    -32.2%    -15.3%    29%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      402     -0.1%    -10.7%    -31.6%    35%
<15%       83     +0.1%    -11.2%    -12.4%    34%
15-30%     10     -1.2%     -0.7%     +1.0%    30%
30%+       21     -0.4%     -0.6%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      406     -0.2%     -2.4%    -12.0%    28%
<20%       94     -1.4%    -53.7%    -96.6%    47%
20%+       16     +1.8%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      494     -0.2%     -4.7%    -13.9%    32%
20-40%     17     -4.8%    -99.0%    -99.1%    71%
40%+        5    +11.6%     +5.8%       -      60%
tokens analysed: 417 | helius credits today: 1260/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   82    24%     -9.7%   -17.1%   -99.7%
   -6%     20%   82    24%     -9.9%   -17.1%   -99.7%
   -6%     30%   82    26%     -7.9%   -17.3%   -99.7%
  -10%     12%   82    27%     -9.5%   -19.4%   -99.7%
  -10%     20%   82    26%    -10.1%   -19.6%   -99.7%
  -10%     30%   82    28%     -8.0%   -19.8%   -99.7%
  -15%     12%   82    28%     -9.1%   -20.0%   -99.7%
  -15%     20%   82    28%     -9.9%   -20.6%   -99.7%
  -15%     30%   82    30%     -7.8%   -20.8%   -99.7%
  -25%     12%   82    33%    -11.1%   -19.2%   -99.7%
  -25%     20%   82    33%    -13.7%   -29.9%   -99.7%
  -25%     30%   82    35%    -11.7%   -30.8%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.8% per trade over n=82
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $437.58       $424.96
return                        -12.5%        -15.0%
closed trades                     48            38
win rate                         25%           21%
avg net / trade                -5.0%         -8.1%
expectancy $/trade            $-1.30        $-1.97
max drawdown                  -23.2%        -21.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $437.58 (-12.5%) | cash $437.58 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 48 | win 12/48 (25%) | avg net -5.0% | realized $-62.42 | expectancy $-1.30/trade
exits: stop 34, trail 14
  (n=48 < 100: noise, not evidence)
last trades:
  plumber      $20.55 -> $13.36 (-35.0%)  stop  0.2h
  AI           $20.55 -> $18.01 (-12.4%)  stop  0.3h
  FOOD         $20.06 -> $36.70 (+83.0%)  trail  1.0h
  Sakura       $20.90 -> $48.56 (+132.3%)  trail  1.2h
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
  Speed        $22.14 -> $17.72 (-20.0%)  stop  1.3h
  BAWSAQ       $21.91 -> $27.10 (+23.7%)  trail  0.8h
  CSI          $22.17 -> $16.28 (-26.6%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 278, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 210, daily_loss_limit 126, setup_rejected:sellers_dominate_now 89, setup_rejected:dumping_now 61, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 13, setup_rejected:operator_cluster 8, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
