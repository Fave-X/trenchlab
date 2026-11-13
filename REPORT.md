# TrenchLab report

Updated: 2026-11-13 19:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           58454
passed SCOUT         121
  killed by SCORE    16
  killed by AUDIT    25
FINAL PASS           80

top kill reasons at first sighting (a pool can have several):
  too_young                    57325
  few_unique_buyers            55097
  liquidity_low                54099
  volume_below_liquidity       41490
  sells_dominate               15401
  wash_churn                   11820
  overheated                    5030
  missing                       1545
  too_old                        895
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 3300 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   80    -4.2%    -6.8%   -44.0%   -91.5%    59%
SCOUT PASS, killed later     41    +3.0%    +0.7%   -52.8%   +22.4%    46%
KILLED (tracked)           8557    +0.0%   -48.7%   -70.2%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      57    -94.8%    -71.7%    53%
too_old                        29     -0.4%     -0.4%     3%
wash_churn                     16     -1.0%    -71.8%    38%
liquidity_low                  16    -51.1%    -49.8%    50%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      4    -12.8%    -79.6%    75%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        39    -63.7%    -94.3%    74%
70-79      45    -39.9%    -65.9%    47%
60-69      25    -32.0%    -99.8%    48%
<60        12    -32.2%    +22.4%    33%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      383     -0.2%    -10.7%    -25.7%    34%
<15%       81     -1.3%    -11.2%    -12.4%    35%
15-30%      9     -1.0%     -1.3%     +1.0%    33%
30%+       17     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      384     -0.2%     -2.7%    -11.5%    28%
<20%       92     -0.8%    -51.5%    -96.6%    46%
20%+       14     -8.3%    -99.0%       -      93%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      471     -0.2%     -5.1%    -12.6%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 395 | helius credits today: 3781/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   80    24%     -9.8%   -17.1%   -99.7%
   -6%     20%   80    24%    -10.0%   -17.1%   -99.7%
   -6%     30%   80    25%     -8.1%   -17.3%   -99.7%
  -10%     12%   80    26%     -9.6%   -19.4%   -99.7%
  -10%     20%   80    25%    -10.2%   -19.6%   -99.7%
  -10%     30%   80    28%     -8.1%   -19.8%   -99.7%
  -15%     12%   80    28%     -9.2%   -20.0%   -99.7%
  -15%     20%   80    28%    -10.0%   -20.6%   -99.7%
  -15%     30%   80    30%     -7.9%   -20.8%   -99.7%
  -25%     12%   80    32%    -11.0%   -19.2%   -99.7%
  -25%     20%   80    32%    -13.7%   -29.9%   -99.7%
  -25%     30%   80    35%    -11.7%   -30.8%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.9% per trade over n=80
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $438.29       $450.43
return                        -12.3%         -9.9%
closed trades                     46            36
win rate                         24%           22%
avg net / trade                -5.1%         -5.4%
expectancy $/trade            $-1.34        $-1.38
max drawdown                  -23.2%        -21.7%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $438.29 (-12.3%) | cash $438.29 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 46 | win 11/46 (24%) | avg net -5.1% | realized $-61.71 | expectancy $-1.34/trade
exits: stop 33, trail 13
  (n=46 < 100: noise, not evidence)
last trades:
  MAX          $21.22 -> $16.96 (-20.1%)  stop  0.2h
  BITCOINU     $21.01 -> $11.81 (-43.8%)  stop  0.2h
  plumber      $20.55 -> $13.36 (-35.0%)  stop  0.2h
  AI           $20.55 -> $18.01 (-12.4%)  stop  0.3h
  FOOD         $20.06 -> $36.70 (+83.0%)  trail  1.0h
  Sakura       $20.90 -> $48.56 (+132.3%)  trail  1.2h
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
  Speed        $22.14 -> $17.72 (-20.0%)  stop  1.3h
signals skipped by the sizer/risk rules: already_traded_token 267, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $450.43 (-9.9%) | cash $450.43 | open 0 | max drawdown -21.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 36 | win 8/36 (22%) | avg net -5.4% | realized $-49.57 | expectancy $-1.38/trade
exits: stop 28, trail 8
  (n=36 < 100: noise, not evidence)
last trades:
  NIHAONOON    $22.04 -> $19.02 (-13.7%)  stop  0.3h
  AIB          $21.89 -> $22.83 (+4.3%)  trail  0.8h
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
  FOOD         $21.41 -> $18.94 (-11.6%)  stop  0.3h
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 206, daily_loss_limit 118, setup_rejected:sellers_dominate_now 87, setup_rejected:dumping_now 55, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 27, setup_rejected:b_bundled 13, setup_rejected:operator_cluster 8, setup_rejected:b_received 7, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
