# TrenchLab report

Updated: 2026-11-14 05:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           61617
passed SCOUT         129
  killed by SCORE    18
  killed by AUDIT    27
FINAL PASS           84

top kill reasons at first sighting (a pool can have several):
  too_young                    60442
  few_unique_buyers            58098
  liquidity_low                56949
  volume_below_liquidity       43704
  sells_dominate               16267
  wash_churn                   12506
  overheated                    5315
  missing                       1722
  too_old                        926
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 3540 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   84    -3.8%    -6.8%   -44.0%   -90.4%    60%
SCOUT PASS, killed later     45    +3.0%    +1.3%   -52.8%   -15.3%    44%
KILLED (tracked)           8948    +0.0%   -49.9%   -71.7%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      66    -93.5%    -71.7%    52%
too_old                        32     -0.6%     -0.4%     3%
wash_churn                     19     -1.0%    -71.8%    32%
liquidity_low                  16    -51.1%    -49.8%    50%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      5     -3.6%    -79.6%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        39    -63.7%    -94.0%    77%
70-79      50    -39.9%    -66.4%    48%
60-69      27    -35.2%    -99.8%    44%
<60        13    -32.2%    -15.3%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      408     -0.2%    -10.5%    -31.6%    34%
<15%       84     -0.6%    -11.2%    -12.4%    33%
15-30%      9     -1.0%     -1.3%     +1.0%    33%
30%+       21     -0.4%     -0.6%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      411     -0.2%     -2.3%    -12.0%    28%
<20%       96     -1.4%    -55.2%    -96.6%    46%
20%+       15    +16.6%    -99.0%       -      87%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      500     -0.2%     -4.5%    -13.9%    31%
20-40%     16     -4.6%    -99.0%    -99.1%    75%
40%+        6    -43.5%     +5.8%       -      50%
tokens analysed: 423 | helius credits today: 1724/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   84    25%     -9.1%   -15.8%   -99.7%
   -6%     20%   84    25%     -9.2%   -15.8%   -99.7%
   -6%     30%   84    26%     -7.4%   -17.1%   -99.7%
  -10%     12%   84    27%     -8.8%   -19.0%   -99.7%
  -10%     20%   84    26%     -9.4%   -19.4%   -99.7%
  -10%     30%   84    29%     -7.4%   -19.6%   -99.7%
  -15%     12%   84    29%     -8.4%   -19.8%   -99.7%
  -15%     20%   84    29%     -9.2%   -20.4%   -99.7%
  -15%     30%   84    31%     -7.1%   -20.6%   -99.7%
  -25%     12%   84    33%    -10.4%   -15.5%   -99.7%
  -25%     20%   84    33%    -13.0%   -29.8%   -99.7%
  -25%     30%   84    36%    -11.0%   -30.4%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.1% per trade over n=84
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $445.41       $424.96
return                        -10.9%        -15.0%
closed trades                     49            38
win rate                         24%           21%
avg net / trade                -5.1%         -8.1%
expectancy $/trade            $-1.33        $-1.97
max drawdown                  -23.2%        -21.8%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $445.41 (-10.9%) | cash $412.97 | open 1 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 49 | win 12/49 (24%) | avg net -5.1% | realized $-65.15 | expectancy $-1.33/trade
exits: stop 35, trail 14
  (n=49 < 100: noise, not evidence)
open:
  tinfoil      cost $21.88  now $32.44 (+48.3%)  held 0.2h
last trades:
  AI           $20.55 -> $18.01 (-12.4%)  stop  0.3h
  FOOD         $20.06 -> $36.70 (+83.0%)  trail  1.0h
  Sakura       $20.90 -> $48.56 (+132.3%)  trail  1.2h
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
  Speed        $22.14 -> $17.72 (-20.0%)  stop  1.3h
  BAWSAQ       $21.91 -> $27.10 (+23.7%)  trail  0.8h
  CSI          $22.17 -> $16.28 (-26.6%)  stop  0.2h
  SWJ          $21.88 -> $19.15 (-12.5%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 279, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 216, daily_loss_limit 128, setup_rejected:sellers_dominate_now 89, setup_rejected:dumping_now 61, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 13, setup_rejected:operator_cluster 8, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
