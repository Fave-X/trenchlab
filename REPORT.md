# TrenchLab report

Updated: 2026-11-26 04:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           147370
passed SCOUT         294
  killed by SCORE    40
  killed by AUDIT    75
FINAL PASS           179

top kill reasons at first sighting (a pool can have several):
  too_young                   145417
  few_unique_buyers           138405
  liquidity_low               136230
  volume_below_liquidity      103003
  sells_dominate               39874
  wash_churn                   30975
  overheated                   13416
  missing                       4214
  too_old                       1386
  copy_trade                      52

OUTCOMES (median price change from first sighting / first pass; 8920 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  179    -5.7%   -18.2%   -44.0%   -83.3%    58%
SCOUT PASS, killed later    115    +5.8%   +10.7%    -7.4%   -74.6%    47%
KILLED (tracked)          20082    +0.1%   -58.7%   -85.5%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     497    -89.6%    -68.9%    23%
wash_churn                     59     -1.2%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
copy_trade                     52    -90.0%    -96.1%    12%
liquidity_low                  36    -69.3%    -49.8%    58%
overheated                     12    -21.9%    -56.0%    50%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        79    -52.9%    -93.2%    57%
70-79     122    -47.4%    -75.9%    52%
60-69      67    -30.1%    -86.0%    55%
<60        26     -7.4%    -63.7%    46%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1184     +0.0%     -9.2%    -48.4%    26%
<15%      306     +3.3%    -15.6%    -45.0%    32%
15-30%     39     -0.1%     -2.1%     +0.4%    41%
30%+       37     -0.7%     -0.9%     +0.5%    35%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1016     +0.0%     -2.1%    -38.9%    25%
<20%      486     +3.3%    -58.5%    -87.0%    27%
20%+       64     +0.1%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1504     +0.3%     -6.9%    -42.1%    26%
20-40%     37     -0.7%    -99.0%    -99.1%    78%
40%+       25    -96.5%    -99.0%       -      72%
tokens analysed: 1386 | helius credits today: 1426/25000

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
equity                       $251.13       $298.26       $428.10
return                        -49.8%        -40.3%        -14.4%
closed trades                    122            95             7
win rate                         20%           20%           14%
avg net / trade               -10.8%        -10.5%        -42.9%
expectancy $/trade            $-2.04        $-2.12       $-10.27
max drawdown                  -51.7%        -45.1%        -15.0%
open now                           1             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $251.13 (-49.8%) | cash $238.57 | open 1 | max drawdown -51.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 122 | win 25/122 (20%) | avg net -10.8% | realized $-248.87 | expectancy $-2.04/trade
exits: stop 91, trail 30, dead_no_route 1
open:
  Zero         cost $12.56  now $12.56 (+0.0%)  held 0.0h
last trades:
  JaoJiu       $14.39 -> $11.41 (-20.7%)  stop  0.2h
  Pompom       $14.24 -> $12.17 (-14.5%)  stop  0.2h
  GRAUDIA      $14.14 -> $8.83 (-37.6%)  stop  0.3h
  4CHAN        $13.87 -> $10.88 (-21.6%)  stop  0.5h
  OnlyUp       $13.72 -> $6.99 (-49.0%)  stop  0.2h
  Pompompurin  $13.38 -> $10.37 (-22.5%)  stop  0.2h
  Squirrel     $13.23 -> $4.27 (-67.7%)  stop  0.3h
  PVE          $12.79 -> $8.22 (-35.7%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 666, daily_loss_limit 331, cooldown_after_loss 24, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $298.26 (-40.3%) | cash $298.26 | open 0 | max drawdown -45.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 95 | win 19/95 (20%) | avg net -10.5% | realized $-201.74 | expectancy $-2.12/trade
exits: stop 75, trail 20
  (n=95 < 100: noise, not evidence)
last trades:
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
  MONEY        $15.00 -> $13.27 (-11.5%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 453, daily_loss_limit 269, setup_rejected:dumping_now 159, setup_rejected:sellers_dominate_now 148, setup_rejected:b_bundled 95, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 47, setup_rejected:lp_not_locked 41, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 14, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $428.10 (-14.4%) | cash $428.10 | open 0 | max drawdown -15.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 7 | win 1/7 (14%) | avg net -42.9% | realized $-71.90 | expectancy $-10.27/trade
exits: mirror_sell 5, stop 2
  (n=7 < 100: noise, not evidence)
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
  BEAST        $24.80 -> $29.54 (+19.1%)  mirror_sell  0.2h
  JENSEN       $25.04 -> $0.93 (-96.3%)  stop  0.3h
  JENSEN       $23.83 -> $7.18 (-69.9%)  mirror_sell  0.0h
  JENSEN       $23.83 -> $1.96 (-91.8%)  mirror_sell  0.0h
  Caiolo       $21.91 -> $11.85 (-45.9%)  stop  0.2h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 266, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 1 wallets, 1797 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
