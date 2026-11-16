# TrenchLab report

Updated: 2026-11-16 22:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           81048
passed SCOUT         160
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           105

top kill reasons at first sighting (a pool can have several):
  too_young                    79713
  few_unique_buyers            76360
  liquidity_low                74878
  volume_below_liquidity       57136
  sells_dominate               21269
  wash_churn                   16694
  overheated                    7045
  missing                       2477
  too_old                       1014
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4793 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  105    -3.8%   -12.0%   -44.7%   -88.1%    60%
SCOUT PASS, killed later     55    +4.3%    +4.2%   -50.5%   -52.9%    49%
KILLED (tracked)          11355    +0.0%   -55.7%   -79.1%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     107    -94.1%    -68.9%    48%
too_old                        36     -0.6%     -0.4%     6%
wash_churn                     28     -1.1%    -71.8%    29%
liquidity_low                  23    -68.7%    -49.8%    52%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        51    -58.0%    -93.4%    75%
70-79      59    -44.3%    -66.9%    51%
60-69      35    -39.6%    -60.0%    49%
<60        15    -31.3%    -52.9%    33%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      527     -0.3%    -16.2%    -32.6%    34%
<15%      109     +0.2%    -11.2%    -12.3%    30%
15-30%     11     -0.2%     -0.2%     +1.0%    45%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      499     -0.2%     -2.8%    -12.8%    28%
<20%      152     -5.9%    -57.8%    -80.2%    42%
20%+       18    +13.0%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      645     -0.2%     -7.5%    -16.0%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+        9    +11.6%     +5.8%       -      67%
tokens analysed: 563 | helius credits today: 5556/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  105    26%     -9.4%   -14.9%   -99.7%
   -6%     20%  105    26%     -9.9%   -17.1%   -99.7%
   -6%     30%  105    25%     -9.5%   -17.5%   -99.7%
  -10%     12%  105    28%    -10.1%   -18.6%   -99.7%
  -10%     20%  105    27%    -10.9%   -19.0%   -99.7%
  -10%     30%  105    27%    -10.5%   -19.3%   -99.7%
  -15%     12%  105    30%    -10.7%   -19.6%   -99.7%
  -15%     20%  105    30%    -11.5%   -20.7%   -99.7%
  -15%     30%  105    30%    -11.1%   -21.0%   -99.7%
  -25%     12%  105    33%    -13.6%   -21.3%   -99.7%
  -25%     20%  105    33%    -16.2%   -30.1%   -99.7%
  -25%     30%  105    33%    -15.9%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -9.4% per trade over n=105

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $367.53       $391.54
return                        -26.5%        -21.7%
closed trades                     64            47
win rate                         23%           19%
avg net / trade                -9.1%         -9.9%
expectancy $/trade            $-2.07        $-2.28
max drawdown                  -29.3%        -28.0%
open now                           0             2
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $367.53 (-26.5%) | cash $367.53 | open 0 | max drawdown -29.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 64 | win 15/64 (23%) | avg net -9.1% | realized $-132.47 | expectancy $-2.07/trade
exits: stop 46, trail 18
  (n=64 < 100: noise, not evidence)
last trades:
  BUTTHOLE     $20.43 -> $17.04 (-16.6%)  stop  0.3h
  rockstar     $20.26 -> $17.49 (-13.7%)  stop  0.2h
  AI           $20.12 -> $15.62 (-22.4%)  stop  0.3h
  BAWSAQ       $19.90 -> $14.39 (-27.7%)  stop  0.2h
  WIGGLES      $19.62 -> $20.44 (+4.2%)  trail  0.3h
  6STAR        $19.75 -> $16.35 (-17.2%)  stop  0.2h
  Marvin       $19.65 -> $16.98 (-13.6%)  stop  0.8h
  FiveM        $19.66 -> $0.01 (-100.0%)  stop  4.0h
signals skipped by the sizer/risk rules: already_traded_token 377, daily_loss_limit 251, cooldown_after_loss 12, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $391.54 (-21.7%) | cash $353.49 | open 2 | max drawdown -28.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 47 | win 9/47 (19%) | avg net -9.9% | realized $-107.23 | expectancy $-2.28/trade
exits: stop 38, trail 9
  (n=47 < 100: noise, not evidence)
open:
  BAWSAQ       cost $19.64  now $19.64 (+0.0%)  held 0.2h
  Trader       cost $19.64  now $18.41 (-6.3%)  held 0.2h
last trades:
  HYGG         $20.94 -> $24.47 (+16.9%)  trail  1.3h
  ニャジラ         $21.11 -> $13.78 (-34.7%)  stop  0.7h
  Socks        $20.75 -> $17.11 (-17.5%)  stop  0.5h
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
  rockstar     $20.24 -> $17.10 (-15.5%)  stop  0.2h
  Marvin       $20.08 -> $17.44 (-13.1%)  stop  0.8h
  WIGGLES      $20.12 -> $16.41 (-18.4%)  stop  1.3h
  Anthropig    $19.77 -> $17.19 (-13.1%)  stop  1.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 363, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 96, setup_rejected:volume_dried_up 38, setup_rejected:b_bundled 33, setup_rejected:top10_concentrated 30, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
