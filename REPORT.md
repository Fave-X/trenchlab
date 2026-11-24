# TrenchLab report

Updated: 2026-11-24 08:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           134346
passed SCOUT         262
  killed by SCORE    37
  killed by AUDIT    65
FINAL PASS           160

top kill reasons at first sighting (a pool can have several):
  too_young                   132572
  few_unique_buyers           126342
  liquidity_low               124258
  volume_below_liquidity       94630
  sells_dominate               35754
  wash_churn                   28176
  overheated                   12127
  missing                       3709
  too_old                       1291
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 8163 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  160    -5.2%   -13.3%   -42.6%   -83.7%    58%
SCOUT PASS, killed later    102    +5.6%    +7.5%   -13.5%   -75.1%    49%
KILLED (tracked)          18619    +0.1%   -61.0%   -85.4%    +0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     410    -90.6%    -68.9%    25%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        51     -0.7%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        73    -54.0%    -93.2%    60%
70-79     102    -41.9%    -72.2%    52%
60-69      62    -29.5%    -89.0%    55%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1052     +0.0%    -10.5%    -46.6%    26%
<15%      251     +3.3%    -14.2%    -40.1%    33%
15-30%     45     -0.2%     -1.7%     +0.4%    31%
30%+       37     -0.7%     -0.8%     +1.9%    35%
bundled     n   +1h med   +4h med  +24h med   rug%
none      918     +0.0%     -2.2%    -33.1%    25%
<20%      408     +3.2%    -58.2%    -92.1%    28%
20%+       59     -5.1%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1328     +0.3%     -6.4%    -40.0%    26%
20-40%     35     -4.5%    -99.0%    -99.1%    77%
40%+       22    -98.6%    -99.0%       -      77%
tokens analysed: 1220 | helius credits today: 2829/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  160    22%    -10.1%   -14.6%   -99.7%
   -6%     20%  160    23%    -10.4%   -14.9%   -99.7%
   -6%     30%  160    21%    -10.5%   -15.5%   -99.7%
  -10%     12%  160    25%    -10.0%   -17.1%   -99.7%
  -10%     20%  160    26%    -10.4%   -17.6%   -99.7%
  -10%     30%  160    24%    -10.5%   -18.6%   -99.7%
  -15%     12%  160    29%     -9.8%   -19.6%   -99.7%
  -15%     20%  160    32%    -10.2%   -20.4%   -99.7%
  -15%     30%  160    29%    -10.6%   -21.1%   -99.7%
  -25%     12%  160    34%    -11.8%   -17.4%   -99.7%
  -25%     20%  160    37%    -13.5%   -29.7%   -99.7%
  -25%     30%  160    34%    -13.7%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.8% per trade over n=160

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $282.40       $327.86
return                        -43.5%        -34.4%
closed trades                    108            86
win rate                         21%           22%
avg net / trade               -10.1%         -9.5%
expectancy $/trade            $-2.01        $-2.00
max drawdown                  -45.7%        -39.7%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $282.40 (-43.5%) | cash $282.40 | open 0 | max drawdown -45.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 108 | win 23/108 (21%) | avg net -10.1% | realized $-217.60 | expectancy $-2.01/trade
exits: stop 79, trail 28, dead_no_route 1
last trades:
  COPIUM       $15.21 -> $13.38 (-12.0%)  stop  1.0h
  Fly          $15.11 -> $13.32 (-11.9%)  stop  0.2h
  cCAT         $15.02 -> $17.11 (+13.9%)  trail  0.3h
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
  ChristmASS   $15.10 -> $9.98 (-33.9%)  stop  0.2h
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
  Jesus        $14.62 -> $4.59 (-68.6%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 609, daily_loss_limit 322, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $327.86 (-34.4%) | cash $327.86 | open 0 | max drawdown -39.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 86 | win 19/86 (22%) | avg net -9.5% | realized $-172.14 | expectancy $-2.00/trade
exits: stop 66, trail 20
  (n=86 < 100: noise, not evidence)
last trades:
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
  MCAT         $17.32 -> $18.54 (+7.0%)  trail  3.5h
  cCAT         $17.38 -> $13.20 (-24.0%)  stop  0.2h
  UCASH        $17.17 -> $17.37 (+1.2%)  trail  0.8h
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 436, daily_loss_limit 240, setup_rejected:dumping_now 144, setup_rejected:sellers_dominate_now 142, setup_rejected:b_bundled 76, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:clustered_supply 38, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
