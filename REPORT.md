# TrenchLab report

Updated: 2026-11-25 04:24 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           140436
passed SCOUT         276
  killed by SCORE    38
  killed by AUDIT    71
FINAL PASS           167

top kill reasons at first sighting (a pool can have several):
  too_young                   138582
  few_unique_buyers           132020
  liquidity_low               129931
  volume_below_liquidity       98882
  sells_dominate               37518
  wash_churn                   29288
  overheated                   12757
  missing                       3843
  too_old                       1360
  rc_danger                       21

OUTCOMES (median price change from first sighting / first pass; 8487 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  167    -5.0%   -14.1%   -43.9%   -83.7%    57%
SCOUT PASS, killed later    109    +5.6%    +9.5%    -7.4%   -74.6%    48%
KILLED (tracked)          19408    +0.1%   -60.7%   -85.5%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     459    -90.6%    -68.9%    24%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          8     +1.2%    +30.3%    38%
sells_dominate                  3    -75.0%       -      67%
copy_trade                      3    -96.3%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        76    -55.0%    -93.2%    59%
70-79     110    -44.3%    -72.2%    50%
60-69      65    -29.5%    -86.0%    55%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1108     +0.0%    -10.9%    -46.0%    27%
<15%      292     +2.0%    -13.7%    -40.1%    31%
15-30%     46     -0.1%     -1.7%     +0.4%    33%
30%+       36     -0.7%     -1.1%     +0.8%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      967     +0.1%     -2.2%    -35.1%    25%
<20%      454     +3.0%    -60.7%    -91.4%    27%
20%+       61     -0.7%    -99.0%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1422     +0.3%     -7.2%    -40.1%    26%
20-40%     37     -0.7%    -99.0%    -99.1%    76%
40%+       23    -98.5%    -99.0%       -      78%
tokens analysed: 1309 | helius credits today: 1374/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  167    22%    -10.1%   -14.7%   -99.7%
   -6%     20%  167    23%    -10.4%   -14.9%   -99.7%
   -6%     30%  167    21%    -10.5%   -15.6%   -99.7%
  -10%     12%  167    25%    -10.1%   -17.5%   -99.7%
  -10%     20%  167    26%    -10.5%   -17.8%   -99.7%
  -10%     30%  167    25%    -10.5%   -18.6%   -99.7%
  -15%     12%  167    29%     -9.9%   -19.6%   -99.7%
  -15%     20%  167    32%    -10.3%   -20.7%   -99.7%
  -15%     30%  167    29%    -10.7%   -21.2%   -99.7%
  -25%     12%  167    34%    -12.2%   -18.6%   -99.7%
  -25%     20%  167    37%    -13.7%   -29.3%   -99.7%
  -25%     30%  167    34%    -14.3%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.9% per trade over n=167

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $279.56       $310.14       $476.69
return                        -44.1%        -38.0%         -4.7%
closed trades                    111            91             4
win rate                         21%           21%           25%
avg net / trade               -10.5%        -10.1%        -23.2%
expectancy $/trade            $-2.05        $-2.09        $-5.83
max drawdown                  -47.4%        -42.9%         -5.3%
open now                           1             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $279.56 (-44.1%) | cash $258.91 | open 1 | max drawdown -47.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 111 | win 23/111 (21%) | avg net -10.5% | realized $-227.32 | expectancy $-2.05/trade
exits: stop 82, trail 28, dead_no_route 1
open:
  4CHAN        cost $13.77  now $20.65 (+50.0%)  held 1.1h
last trades:
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
  ChristmASS   $15.10 -> $9.98 (-33.9%)  stop  0.2h
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
  Jesus        $14.62 -> $4.59 (-68.6%)  stop  0.2h
  Scamsem      $14.12 -> $12.59 (-10.9%)  stop  0.2h
  DUVAL        $14.04 -> $8.66 (-38.3%)  stop  0.2h
  BOOBS        $13.77 -> $10.97 (-20.4%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 621, daily_loss_limit 331, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $310.14 (-38.0%) | cash $310.14 | open 0 | max drawdown -42.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 91 | win 19/91 (21%) | avg net -10.1% | realized $-189.86 | expectancy $-2.09/trade
exits: stop 71, trail 20
  (n=91 < 100: noise, not evidence)
last trades:
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 450, daily_loss_limit 240, setup_rejected:dumping_now 147, setup_rejected:sellers_dominate_now 145, setup_rejected:b_bundled 77, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 43, setup_rejected:lp_not_locked 40, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $476.69 (-4.7%) | cash $476.69 | open 0 | max drawdown -5.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 4 | win 1/4 (25%) | avg net -23.2% | realized $-23.31 | expectancy $-5.83/trade
exits: mirror_sell 3, stop 1
  (n=4 < 100: noise, not evidence)
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
  BEAST        $24.80 -> $29.54 (+19.1%)  mirror_sell  0.2h
  JENSEN       $25.04 -> $0.93 (-96.3%)  stop  0.3h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 177, copy:no_price_at_delay 12

BOOK C per wallet  (watching 8 wallets, 1320 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       4     0   25%   -23.2%   -23.31
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
