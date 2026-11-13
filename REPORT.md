# TrenchLab report

Updated: 2026-11-13 03:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           53902
passed SCOUT         117
  killed by SCORE    15
  killed by AUDIT    25
FINAL PASS           77

top kill reasons at first sighting (a pool can have several):
  too_young                    52816
  few_unique_buyers            50820
  liquidity_low                49846
  volume_below_liquidity       38324
  sells_dominate               14153
  wash_churn                   10773
  overheated                    4591
  missing                       1450
  too_old                        864
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 2951 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   77    -4.3%    -7.8%   -44.0%   -91.5%    60%
SCOUT PASS, killed later     40    +4.6%    +1.3%   -52.8%   +22.4%    45%
KILLED (tracked)           7990    +0.0%   -38.5%   -66.8%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      52    -94.8%    -71.7%    54%
too_old                        27     -0.4%     -0.4%     4%
wash_churn                     15    +11.9%    -71.8%    33%
liquidity_low                  15    -40.0%    -49.8%    40%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      4    -12.8%    -79.6%    75%
sells_dominate                  2    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        39    -63.7%    -94.7%    74%
70-79      42    -42.3%    -65.9%    48%
60-69      25    -32.0%    -99.8%    48%
<60        11    -32.2%    +22.4%    27%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      357     -0.3%    -12.5%    -25.7%    34%
<15%       77     +0.2%    -11.2%    -12.4%    34%
15-30%      8     -0.6%     -0.7%     +1.0%    38%
30%+       18     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      358     -0.2%     -3.1%    -11.5%    28%
<20%       89     -0.3%    -49.5%    -96.6%    45%
20%+       13    +16.6%    -99.0%       -      92%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      442     -0.2%     -7.3%    -12.6%    32%
20-40%     14     -4.6%    -99.0%    -99.1%    79%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 372 | helius credits today: 710/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   77    22%    -11.8%   -17.1%   -99.7%
   -6%     20%   77    23%    -11.8%   -17.1%   -99.7%
   -6%     30%   77    25%     -9.7%   -18.5%   -99.7%
  -10%     12%   77    25%    -11.4%   -19.5%   -99.7%
  -10%     20%   77    25%    -11.9%   -19.6%   -99.7%
  -10%     30%   77    27%     -9.6%   -19.9%   -99.7%
  -15%     12%   77    26%    -11.0%   -20.1%   -99.7%
  -15%     20%   77    27%    -11.5%   -20.4%   -99.7%
  -15%     30%   77    30%     -9.3%   -20.7%   -99.7%
  -25%     12%   77    31%    -12.7%   -21.3%   -99.7%
  -25%     20%   77    32%    -14.9%   -29.9%   -99.7%
  -25%     30%   77    35%    -12.7%   -30.8%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -9.3% per trade over n=77
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $417.91       $428.17
return                        -16.4%        -14.4%
closed trades                     43            34
win rate                         23%           21%
avg net / trade                -7.8%         -8.8%
expectancy $/trade            $-1.91        $-2.11
max drawdown                  -23.2%        -21.2%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $417.91 (-16.4%) | cash $417.91 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 43 | win 10/43 (23%) | avg net -7.8% | realized $-82.09 | expectancy $-1.91/trade
exits: stop 31, trail 12
  (n=43 < 100: noise, not evidence)
last trades:
  NIHAONOON    $21.56 -> $21.56 (-0.0%)  trail  0.3h
  Max          $21.56 -> $18.83 (-12.7%)  stop  0.7h
  AIB          $21.42 -> $17.45 (-18.6%)  stop  0.2h
  MAX          $21.22 -> $16.96 (-20.1%)  stop  0.2h
  BITCOINU     $21.01 -> $11.81 (-43.8%)  stop  0.2h
  plumber      $20.55 -> $13.36 (-35.0%)  stop  0.2h
  AI           $20.55 -> $18.01 (-12.4%)  stop  0.3h
  FOOD         $20.06 -> $36.70 (+83.0%)  trail  1.0h
signals skipped by the sizer/risk rules: already_traded_token 227, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $428.17 (-14.4%) | cash $428.17 | open 0 | max drawdown -21.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 34 | win 7/34 (21%) | avg net -8.8% | realized $-71.83 | expectancy $-2.11/trade
exits: stop 27, trail 7
  (n=34 < 100: noise, not evidence)
last trades:
  pants        $22.47 -> $19.96 (-11.2%)  stop  0.5h
  Max          $22.16 -> $19.66 (-11.3%)  stop  0.2h
  NIHAONOON    $22.04 -> $19.02 (-13.7%)  stop  0.3h
  AIB          $21.89 -> $22.83 (+4.3%)  trail  0.8h
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 196, daily_loss_limit 118, setup_rejected:sellers_dominate_now 86, setup_rejected:dumping_now 54, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 25, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:operator_cluster 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
