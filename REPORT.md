# TrenchLab report

Updated: 2026-11-26 06:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           148080
passed SCOUT         296
  killed by SCORE    41
  killed by AUDIT    76
FINAL PASS           179

top kill reasons at first sighting (a pool can have several):
  too_young                   146096
  few_unique_buyers           139014
  liquidity_low               136900
  volume_below_liquidity      103388
  sells_dominate               40150
  wash_churn                   31160
  overheated                   13493
  missing                       4214
  too_old                       1392
  copy_trade                      53

OUTCOMES (median price change from first sighting / first pass; 8958 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  179    -5.7%   -18.2%   -44.7%   -83.0%    58%
SCOUT PASS, killed later    117    +5.7%   +10.7%    -7.4%   -74.6%    46%
KILLED (tracked)          20167    +0.1%   -58.3%   -85.4%    -0.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     505    -89.6%    -68.9%    23%
wash_churn                     61     -1.2%    -85.6%    25%
copy_trade                     53    -85.6%    -96.1%    11%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -69.3%    -72.0%    57%
overheated                     13    -21.9%    -56.0%    46%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        80    -52.9%    -93.2%    56%
70-79     122    -51.5%    -76.1%    52%
60-69      67    -32.0%    -86.0%    55%
<60        27     -7.2%    -63.7%    44%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1195     +0.0%     -9.9%    -49.9%    26%
<15%      309     +2.4%    -17.8%    -49.8%    32%
15-30%     38     -0.1%     -1.0%     +0.4%    42%
30%+       37     -0.7%     -0.9%     +0.5%    35%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1028     +0.0%     -2.2%    -39.2%    24%
<20%      488     +3.2%    -59.6%    -91.4%    27%
20%+       63     +0.9%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1518     +0.3%     -7.3%    -43.0%    25%
20-40%     37     -0.7%    -99.0%    -99.1%    78%
40%+       24    -97.5%    -99.0%       -      75%
tokens analysed: 1399 | helius credits today: 2338/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  179    21%    -11.2%   -15.1%   -99.7%
   -6%     20%  179    23%    -11.3%   -15.4%   -99.7%
   -6%     30%  179    21%    -11.4%   -16.4%   -99.7%
  -10%     12%  179    24%    -11.2%   -17.8%   -99.7%
  -10%     20%  179    26%    -11.4%   -18.6%   -99.7%
  -10%     30%  179    24%    -11.4%   -19.0%   -99.7%
  -15%     12%  179    28%    -11.0%   -20.2%   -99.7%
  -15%     20%  179    31%    -11.3%   -21.0%   -99.7%
  -15%     30%  179    28%    -11.6%   -21.3%   -99.7%
  -25%     12%  179    32%    -13.2%   -21.3%   -99.7%
  -25%     20%  179    36%    -14.2%   -29.6%   -99.7%
  -25%     30%  179    34%    -14.9%   -31.0%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -11.0% per trade over n=179

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $249.63       $296.37       $430.40
return                        -50.1%        -40.7%        -13.9%
closed trades                    123            96             7
win rate                         20%           20%           14%
avg net / trade               -10.8%        -10.6%        -42.9%
expectancy $/trade            $-2.04        $-2.12       $-10.27
max drawdown                  -52.0%        -45.5%        -15.0%
open now                           0             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $249.63 (-50.1%) | cash $249.63 | open 0 | max drawdown -52.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 123 | win 25/123 (20%) | avg net -10.8% | realized $-250.37 | expectancy $-2.04/trade
exits: stop 92, trail 30, dead_no_route 1
last trades:
  Pompom       $14.24 -> $12.17 (-14.5%)  stop  0.2h
  GRAUDIA      $14.14 -> $8.83 (-37.6%)  stop  0.3h
  4CHAN        $13.87 -> $10.88 (-21.6%)  stop  0.5h
  OnlyUp       $13.72 -> $6.99 (-49.0%)  stop  0.2h
  Pompompurin  $13.38 -> $10.37 (-22.5%)  stop  0.2h
  Squirrel     $13.23 -> $4.27 (-67.7%)  stop  0.3h
  PVE          $12.79 -> $8.22 (-35.7%)  stop  0.3h
  Zero         $12.56 -> $11.06 (-12.0%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 667, daily_loss_limit 331, cooldown_after_loss 24, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $296.37 (-40.7%) | cash $296.37 | open 0 | max drawdown -45.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 96 | win 19/96 (20%) | avg net -10.6% | realized $-203.63 | expectancy $-2.12/trade
exits: stop 76, trail 20
  (n=96 < 100: noise, not evidence)
last trades:
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
  MONEY        $15.00 -> $13.27 (-11.5%)  stop  0.3h
  Grodia       $14.91 -> $13.02 (-12.7%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 453, daily_loss_limit 269, setup_rejected:dumping_now 164, setup_rejected:sellers_dominate_now 148, setup_rejected:b_bundled 96, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 41, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 19, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $430.40 (-13.9%) | cash $406.69 | open 1 | max drawdown -15.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 7 | win 1/7 (14%) | avg net -42.9% | realized $-71.90 | expectancy $-10.27/trade
exits: mirror_sell 5, stop 2
  (n=7 < 100: noise, not evidence)
open:
  Caiolo       cost $21.41  now $23.70 (+10.7%)  held 0.4h
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
  BEAST        $24.80 -> $29.54 (+19.1%)  mirror_sell  0.2h
  JENSEN       $25.04 -> $0.93 (-96.3%)  stop  0.3h
  JENSEN       $23.83 -> $7.18 (-69.9%)  mirror_sell  0.0h
  JENSEN       $23.83 -> $1.96 (-91.8%)  mirror_sell  0.0h
  Caiolo       $21.91 -> $11.85 (-45.9%)  stop  0.2h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 266, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 1 wallets, 1801 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
HSq83t…YPbW   v2-near-hold4       0     1     -        -    +0.00
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
