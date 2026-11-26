# TrenchLab report

Updated: 2026-11-26 22:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           152924
passed SCOUT         309
  killed by SCORE    42
  killed by AUDIT    84
FINAL PASS           183

top kill reasons at first sighting (a pool can have several):
  too_young                   150898
  few_unique_buyers           143471
  liquidity_low               141486
  volume_below_liquidity      106775
  sells_dominate               41429
  wash_churn                   32115
  overheated                   13972
  missing                       4249
  too_old                       1412
  copy_trade                      58

OUTCOMES (median price change from first sighting / first pass; 9263 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  183    -5.5%   -18.2%   -44.7%   -83.0%    60%
SCOUT PASS, killed later    126    +6.0%    +8.4%   -13.5%   -74.6%    47%
KILLED (tracked)          20805    +0.1%   -58.0%   -85.3%    -0.4%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     554    -87.2%    -68.9%    22%
wash_churn                     61     -1.2%    -85.6%    25%
copy_trade                     58    -75.8%    -95.9%    12%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     15    -12.8%    -56.0%    40%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        84    -52.9%    -92.9%    57%
70-79     129    -51.5%    -76.6%    53%
60-69      69    -34.0%    -86.0%    57%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1247     +0.1%     -9.9%    -49.9%    26%
<15%      336     +2.4%    -19.5%    -45.0%    31%
15-30%     40     -0.1%     -1.3%     +0.4%    42%
30%+       38     -0.7%     -0.9%     +0.5%    37%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1076     +0.1%     -2.2%    -39.2%    24%
<20%      519     +3.1%    -60.6%    -87.0%    27%
20%+       66     -0.7%    -99.0%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1597     +0.4%     -7.4%    -42.6%    25%
20-40%     38     -2.6%    -99.0%    -99.1%    79%
40%+       26    -98.5%    -99.0%       -      73%
tokens analysed: 1479 | helius credits today: 7949/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  183    22%    -10.9%   -15.1%   -99.7%
   -6%     20%  183    23%    -11.0%   -15.1%   -99.7%
   -6%     30%  183    21%    -11.2%   -15.9%   -99.7%
  -10%     12%  183    25%    -10.7%   -17.7%   -99.7%
  -10%     20%  183    27%    -10.9%   -18.2%   -99.7%
  -10%     30%  183    25%    -10.9%   -18.7%   -99.7%
  -15%     12%  183    29%    -10.5%   -20.1%   -99.7%
  -15%     20%  183    32%    -10.8%   -21.0%   -99.7%
  -15%     30%  183    30%    -11.1%   -21.3%   -99.7%
  -25%     12%  183    33%    -12.7%   -21.3%   -99.7%
  -25%     20%  183    37%    -13.7%   -29.3%   -99.7%
  -25%     30%  183    34%    -14.3%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -10.5% per trade over n=183

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $256.21       $287.20       $425.71
return                        -48.8%        -42.6%        -14.9%
closed trades                    127            99            14
win rate                         22%           19%           21%
avg net / trade               -10.1%        -10.9%        -22.0%
expectancy $/trade            $-1.92        $-2.15        $-5.27
max drawdown                  -52.2%        -47.2%        -15.5%
open now                           0             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $256.21 (-48.8%) | cash $256.21 | open 0 | max drawdown -52.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 127 | win 28/127 (22%) | avg net -10.1% | realized $-243.79 | expectancy $-1.92/trade
exits: stop 93, trail 33, dead_no_route 1
last trades:
  Pompompurin  $13.38 -> $10.37 (-22.5%)  stop  0.2h
  Squirrel     $13.23 -> $4.27 (-67.7%)  stop  0.3h
  PVE          $12.79 -> $8.22 (-35.7%)  stop  0.3h
  Zero         $12.56 -> $11.06 (-12.0%)  stop  0.2h
  Elonmas      $12.48 -> $15.86 (+27.1%)  trail  1.0h
  PAIR         $12.65 -> $17.22 (+36.2%)  trail  1.3h
  duk          $12.88 -> $9.04 (-29.8%)  stop  0.2h
  KURO         $12.69 -> $15.15 (+19.4%)  trail  0.3h
signals skipped by the sizer/risk rules: already_traded_token 693, daily_loss_limit 331, cooldown_after_loss 24, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $287.20 (-42.6%) | cash $287.20 | open 0 | max drawdown -47.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 99 | win 19/99 (19%) | avg net -10.9% | realized $-212.80 | expectancy $-2.15/trade
exits: stop 79, trail 20
  (n=99 < 100: noise, not evidence)
last trades:
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
  MONEY        $15.00 -> $13.27 (-11.5%)  stop  0.3h
  Grodia       $14.91 -> $13.02 (-12.7%)  stop  0.3h
  NORFEATH     $14.82 -> $12.87 (-13.2%)  stop  0.5h
  duk          $14.72 -> $12.42 (-15.6%)  stop  0.2h
  PAIR         $14.61 -> $9.69 (-33.7%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 166, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 96, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 43, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:rc_danger:Low Liquidity 11, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $425.71 (-14.9%) | cash $404.48 | open 1 | max drawdown -15.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 14 | win 3/14 (21%) | avg net -22.0% | realized $-73.77 | expectancy $-5.27/trade
exits: mirror_sell 12, stop 2
  (n=14 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $21.23 (-2.4%)  held 4.9h
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
