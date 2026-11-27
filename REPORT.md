# TrenchLab report

Updated: 2026-11-27 00:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           153707
passed SCOUT         313
  killed by SCORE    42
  killed by AUDIT    85
FINAL PASS           186

top kill reasons at first sighting (a pool can have several):
  too_young                   151676
  few_unique_buyers           144197
  liquidity_low               142231
  volume_below_liquidity      107297
  sells_dominate               41642
  wash_churn                   32324
  overheated                   14061
  missing                       4256
  too_old                       1414
  copy_trade                      58

OUTCOMES (median price change from first sighting / first pass; 9333 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  186    -5.6%   -19.1%   -44.7%   -83.0%    60%
SCOUT PASS, killed later    127    +6.1%    +8.4%    -7.4%   -75.1%    47%
KILLED (tracked)          20898    +0.1%   -57.8%   -85.1%    -0.3%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     561    -88.2%    -68.9%    22%
wash_churn                     61     -1.2%    -85.6%    25%
copy_trade                     58    -75.8%    -95.9%    12%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     16    -12.8%    -56.0%    38%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        86    -52.9%    -92.9%    57%
70-79     131    -51.5%    -77.2%    53%
60-69      69    -32.0%    -86.0%    57%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1259     +0.2%     -9.2%    -49.9%    25%
<15%      341     +2.4%    -17.8%    -49.8%    31%
15-30%     41     -0.1%     -1.3%     +0.4%    44%
30%+       38     -0.7%     -0.9%     +0.5%    37%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1086     +0.1%     -2.2%    -39.2%    24%
<20%      526     +3.0%    -60.6%    -91.4%    27%
20%+       67     -2.9%    -99.0%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1614     +0.4%     -7.3%    -43.0%    25%
20-40%     38     -2.6%    -99.0%    -99.1%    79%
40%+       27    -97.5%    -99.0%       -      74%
tokens analysed: 1496 | helius credits today: 431/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  185    22%    -11.1%   -15.1%   -99.7%
   -6%     20%  185    23%    -11.2%   -15.1%   -99.7%
   -6%     30%  185    21%    -11.4%   -15.9%   -99.7%
  -10%     12%  185    25%    -10.9%   -17.7%   -99.7%
  -10%     20%  185    26%    -11.1%   -18.2%   -99.7%
  -10%     30%  185    25%    -11.1%   -18.7%   -99.7%
  -15%     12%  185    29%    -10.7%   -20.1%   -99.7%
  -15%     20%  185    31%    -11.0%   -21.0%   -99.7%
  -15%     30%  185    29%    -11.3%   -21.3%   -99.7%
  -25%     12%  185    32%    -12.9%   -21.3%   -99.7%
  -25%     20%  185    37%    -13.8%   -29.3%   -99.7%
  -25%     30%  185    34%    -14.5%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -10.7% per trade over n=185

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $248.75       $284.52       $426.32
return                        -50.3%        -43.1%        -14.7%
closed trades                    129           100            14
win rate                         22%           19%           21%
avg net / trade               -10.4%        -10.9%        -22.0%
expectancy $/trade            $-1.95        $-2.15        $-5.27
max drawdown                  -52.2%        -47.7%        -15.5%
open now                           1             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $248.75 (-50.3%) | cash $236.23 | open 1 | max drawdown -52.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 129 | win 28/129 (22%) | avg net -10.4% | realized $-251.25 | expectancy $-1.95/trade
exits: stop 95, trail 33, dead_no_route 1
open:
  DEXDATA      cost $12.52  now $12.52 (+0.0%)  held 0.0h
last trades:
  PVE          $12.79 -> $8.22 (-35.7%)  stop  0.3h
  Zero         $12.56 -> $11.06 (-12.0%)  stop  0.2h
  Elonmas      $12.48 -> $15.86 (+27.1%)  trail  1.0h
  PAIR         $12.65 -> $17.22 (+36.2%)  trail  1.3h
  duk          $12.88 -> $9.04 (-29.8%)  stop  0.2h
  KURO         $12.69 -> $15.15 (+19.4%)  trail  0.3h
  Hoppy        $12.81 -> $7.02 (-45.2%)  stop  0.2h
  Vetocat      $12.52 -> $10.86 (-13.3%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 696, daily_loss_limit 331, cooldown_after_loss 24, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $284.52 (-43.1%) | cash $284.52 | open 0 | max drawdown -47.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 100 | win 19/100 (19%) | avg net -10.9% | realized $-215.48 | expectancy $-2.15/trade
exits: stop 80, trail 20
last trades:
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
  MONEY        $15.00 -> $13.27 (-11.5%)  stop  0.3h
  Grodia       $14.91 -> $13.02 (-12.7%)  stop  0.3h
  NORFEATH     $14.82 -> $12.87 (-13.2%)  stop  0.5h
  duk          $14.72 -> $12.42 (-15.6%)  stop  0.2h
  PAIR         $14.61 -> $9.69 (-33.7%)  stop  0.5h
  Hoppy        $14.36 -> $11.68 (-18.7%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 166, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 96, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 43, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:rc_danger:Low Liquidity 11, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $426.32 (-14.7%) | cash $404.48 | open 1 | max drawdown -15.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 14 | win 3/14 (21%) | avg net -22.0% | realized $-73.77 | expectancy $-5.27/trade
exits: mirror_sell 12, stop 2
  (n=14 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $21.84 (+0.4%)  held 7.2h
last trades:
  Caiolo       $21.91 -> $11.85 (-45.9%)  stop  0.2h
  Caiolo       $21.41 -> $33.10 (+54.6%)  mirror_sell  0.5h
  test         $21.99 -> $18.31 (-16.7%)  mirror_sell  0.0h
  LOBBY        $21.81 -> $30.42 (+39.5%)  mirror_sell  0.0h
  GIVE         $22.24 -> $17.38 (-21.9%)  mirror_sell  0.0h
  COSMOS       $21.99 -> $18.46 (-16.0%)  mirror_sell  0.0h
  Pnp          $21.82 -> $20.41 (-6.5%)  mirror_sell  0.2h
  Max          $21.71 -> $13.01 (-40.1%)  mirror_sell  0.3h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 266, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 3 wallets, 1824 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
HSq83t…YPbW   v2-near-hold4       7     1   29%    -1.0%    -1.87
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
