# TrenchLab report

Updated: 2026-11-25 22:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           145847
passed SCOUT         287
  killed by SCORE    38
  killed by AUDIT    73
FINAL PASS           176

top kill reasons at first sighting (a pool can have several):
  too_young                   143907
  few_unique_buyers           137005
  liquidity_low               134763
  volume_below_liquidity      102102
  sells_dominate               39263
  wash_churn                   30583
  overheated                   13281
  missing                       4208
  too_old                       1378
  copy_trade                      51

OUTCOMES (median price change from first sighting / first pass; 8852 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  176    -5.5%   -16.1%   -42.6%   -83.3%    58%
SCOUT PASS, killed later    111    +5.6%   +10.7%    -7.2%   -74.6%    48%
KILLED (tracked)          19974    +0.1%   -59.3%   -85.6%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     491    -90.5%    -68.9%    24%
wash_churn                     58     -1.2%    -85.6%    26%
too_old                        52     -0.6%     -0.4%    10%
copy_trade                     51    -95.9%    -96.1%     8%
liquidity_low                  36    -69.3%    -49.8%    56%
overheated                     12    -21.9%    -56.0%    50%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        79    -52.9%    -93.2%    57%
70-79     118    -41.9%    -75.3%    52%
60-69      65    -30.1%    -86.0%    57%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1163     +0.2%    -11.0%    -52.1%    26%
<15%      309     +1.4%    -11.2%    -24.8%    31%
15-30%     37     -0.1%     -1.3%     +0.4%    43%
30%+       36     -0.7%     -1.1%     +0.5%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1005     +0.0%     -2.2%    -35.1%    25%
<20%      479     +3.3%    -58.4%    -82.6%    27%
20%+       61     -0.7%    -99.0%       -      84%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1486     +0.4%     -6.8%    -40.1%    26%
20-40%     36     -2.6%    -99.0%    -99.1%    78%
40%+       23    -98.5%    -99.4%       -      78%
tokens analysed: 1367 | helius credits today: 6604/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  175    22%    -10.5%   -15.1%   -99.7%
   -6%     20%  175    23%    -10.8%   -15.1%   -99.7%
   -6%     30%  175    21%    -11.0%   -15.9%   -99.7%
  -10%     12%  175    25%    -10.5%   -17.7%   -99.7%
  -10%     20%  175    26%    -10.9%   -18.2%   -99.7%
  -10%     30%  175    24%    -10.9%   -18.7%   -99.7%
  -15%     12%  175    29%    -10.4%   -20.1%   -99.7%
  -15%     20%  175    31%    -10.8%   -21.0%   -99.7%
  -15%     30%  175    29%    -11.2%   -21.3%   -99.7%
  -25%     12%  175    33%    -12.6%   -21.3%   -99.7%
  -25%     20%  175    37%    -13.8%   -29.3%   -99.7%
  -25%     30%  175    34%    -14.5%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -10.4% per trade over n=175

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $264.66       $299.99       $438.16
return                        -47.1%        -40.0%        -12.4%
closed trades                    120            94             6
win rate                         21%           20%           17%
avg net / trade               -10.1%        -10.5%        -42.4%
expectancy $/trade            $-1.96        $-2.13       $-10.31
max drawdown                  -49.1%        -44.8%        -13.0%
open now                           1             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $264.66 (-47.1%) | cash $251.43 | open 1 | max drawdown -49.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 120 | win 25/120 (21%) | avg net -10.1% | realized $-235.34 | expectancy $-1.96/trade
exits: stop 89, trail 30, dead_no_route 1
open:
  Squirrel     cost $13.23  now $13.23 (+0.0%)  held 0.0h
last trades:
  PERRO        $14.45 -> $12.30 (-14.8%)  stop  0.3h
  BASKET       $14.12 -> $19.47 (+37.9%)  trail  1.0h
  JaoJiu       $14.39 -> $11.41 (-20.7%)  stop  0.2h
  Pompom       $14.24 -> $12.17 (-14.5%)  stop  0.2h
  GRAUDIA      $14.14 -> $8.83 (-37.6%)  stop  0.3h
  4CHAN        $13.87 -> $10.88 (-21.6%)  stop  0.5h
  OnlyUp       $13.72 -> $6.99 (-49.0%)  stop  0.2h
  Pompompurin  $13.38 -> $10.37 (-22.5%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 664, daily_loss_limit 331, cooldown_after_loss 21, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $299.99 (-40.0%) | cash $299.99 | open 0 | max drawdown -44.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 94 | win 19/94 (20%) | avg net -10.5% | realized $-200.01 | expectancy $-2.13/trade
exits: stop 74, trail 20
  (n=94 < 100: noise, not evidence)
last trades:
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 453, daily_loss_limit 269, setup_rejected:dumping_now 157, setup_rejected:sellers_dominate_now 146, setup_rejected:b_bundled 90, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 43, setup_rejected:lp_not_locked 41, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $438.16 (-12.4%) | cash $438.16 | open 0 | max drawdown -13.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 6 | win 1/6 (17%) | avg net -42.4% | realized $-61.84 | expectancy $-10.31/trade
exits: mirror_sell 5, stop 1
  (n=6 < 100: noise, not evidence)
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
  BEAST        $24.80 -> $29.54 (+19.1%)  mirror_sell  0.2h
  JENSEN       $25.04 -> $0.93 (-96.3%)  stop  0.3h
  JENSEN       $23.83 -> $7.18 (-69.9%)  mirror_sell  0.0h
  JENSEN       $23.83 -> $1.96 (-91.8%)  mirror_sell  0.0h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 264, copy:no_pool 56, daily_loss_limit 53, copy:no_price_at_delay 29

BOOK C per wallet  (watching 1 wallets, 1784 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
