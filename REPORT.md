# TrenchLab report

Updated: 2026-11-26 17:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           151428
passed SCOUT         304
  killed by SCORE    41
  killed by AUDIT    81
FINAL PASS           182

top kill reasons at first sighting (a pool can have several):
  too_young                   149413
  few_unique_buyers           142096
  liquidity_low               140070
  volume_below_liquidity      105729
  sells_dominate               41023
  wash_churn                   31835
  overheated                   13812
  missing                       4236
  too_old                       1407
  copy_trade                      56

OUTCOMES (median price change from first sighting / first pass; 9186 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  182    -5.6%   -16.1%   -44.4%   -83.0%    59%
SCOUT PASS, killed later    122    +6.0%    +8.4%   -19.5%   -74.6%    48%
KILLED (tracked)          20625    +0.2%   -57.9%   -85.0%    -0.3%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     540    -86.3%    -68.9%    22%
wash_churn                     61     -1.2%    -85.6%    25%
copy_trade                     56    -80.7%    -95.9%    12%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     14    -12.8%    -56.0%    43%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        83    -52.9%    -92.9%    57%
70-79     127    -51.5%    -76.6%    54%
60-69      68    -32.0%    -86.0%    56%
<60        26     -7.4%    -63.7%    46%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1233     +0.1%     -9.1%    -49.9%    26%
<15%      322     +2.3%    -19.5%    -49.8%    32%
15-30%     39     -0.1%     -1.0%     +0.4%    44%
30%+       37     -0.7%     -0.9%     +0.5%    35%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1061     +0.1%     -2.1%    -39.4%    24%
<20%      506     +2.9%    -59.6%    -87.0%    27%
20%+       64     +0.9%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1569     +0.4%     -7.2%    -43.0%    25%
20-40%     38     -0.7%    -99.0%    -99.1%    79%
40%+       24    -97.5%    -99.0%       -      75%
tokens analysed: 1451 | helius credits today: 5795/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  182    21%    -11.0%   -15.1%   -99.7%
   -6%     20%  182    23%    -11.2%   -15.2%   -99.7%
   -6%     30%  182    21%    -11.3%   -16.1%   -99.7%
  -10%     12%  182    25%    -10.8%   -17.8%   -99.7%
  -10%     20%  182    26%    -11.0%   -18.4%   -99.7%
  -10%     30%  182    25%    -11.1%   -18.9%   -99.7%
  -15%     12%  182    29%    -10.7%   -20.1%   -99.7%
  -15%     20%  182    31%    -10.9%   -21.0%   -99.7%
  -15%     30%  182    29%    -11.3%   -21.3%   -99.7%
  -25%     12%  182    32%    -12.8%   -21.3%   -99.7%
  -25%     20%  182    37%    -13.8%   -29.5%   -99.7%
  -25%     30%  182    34%    -14.5%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -10.7% per trade over n=182

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $253.74       $292.12       $434.93
return                        -49.3%        -41.6%        -13.0%
closed trades                    126            98            13
win rate                         21%           19%           23%
avg net / trade               -10.3%        -10.6%        -20.6%
expectancy $/trade            $-1.95        $-2.12        $-5.01
max drawdown                  -52.2%        -46.3%        -15.0%
open now                           0             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $253.74 (-49.3%) | cash $253.74 | open 0 | max drawdown -52.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 126 | win 27/126 (21%) | avg net -10.3% | realized $-246.26 | expectancy $-1.95/trade
exits: stop 93, trail 32, dead_no_route 1
last trades:
  OnlyUp       $13.72 -> $6.99 (-49.0%)  stop  0.2h
  Pompompurin  $13.38 -> $10.37 (-22.5%)  stop  0.2h
  Squirrel     $13.23 -> $4.27 (-67.7%)  stop  0.3h
  PVE          $12.79 -> $8.22 (-35.7%)  stop  0.3h
  Zero         $12.56 -> $11.06 (-12.0%)  stop  0.2h
  Elonmas      $12.48 -> $15.86 (+27.1%)  trail  1.0h
  PAIR         $12.65 -> $17.22 (+36.2%)  trail  1.3h
  duk          $12.88 -> $9.04 (-29.8%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 684, daily_loss_limit 331, cooldown_after_loss 24, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $292.12 (-41.6%) | cash $292.12 | open 0 | max drawdown -46.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 98 | win 19/98 (19%) | avg net -10.6% | realized $-207.88 | expectancy $-2.12/trade
exits: stop 78, trail 20
  (n=98 < 100: noise, not evidence)
last trades:
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
  MONEY        $15.00 -> $13.27 (-11.5%)  stop  0.3h
  Grodia       $14.91 -> $13.02 (-12.7%)  stop  0.3h
  NORFEATH     $14.82 -> $12.87 (-13.2%)  stop  0.5h
  duk          $14.72 -> $12.42 (-15.6%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 165, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 96, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 43, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:rc_danger:Low Liquidity 11, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $434.93 (-13.0%) | cash $434.93 | open 0 | max drawdown -15.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 13 | win 3/13 (23%) | avg net -20.6% | realized $-65.07 | expectancy $-5.01/trade
exits: mirror_sell 11, stop 2
  (n=13 < 100: noise, not evidence)
last trades:
  JENSEN       $23.83 -> $1.96 (-91.8%)  mirror_sell  0.0h
  Caiolo       $21.91 -> $11.85 (-45.9%)  stop  0.2h
  Caiolo       $21.41 -> $33.10 (+54.6%)  mirror_sell  0.5h
  test         $21.99 -> $18.31 (-16.7%)  mirror_sell  0.0h
  LOBBY        $21.81 -> $30.42 (+39.5%)  mirror_sell  0.0h
  GIVE         $22.24 -> $17.38 (-21.9%)  mirror_sell  0.0h
  COSMOS       $21.99 -> $18.46 (-16.0%)  mirror_sell  0.0h
  Pnp          $21.82 -> $20.41 (-6.5%)  mirror_sell  0.2h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 266, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 3 wallets, 1821 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
HSq83t…YPbW   v2-near-hold4       6     0   33%    +5.5%    +6.83
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
