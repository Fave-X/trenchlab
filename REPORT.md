# TrenchLab report

Updated: 2026-11-25 07:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           141506
passed SCOUT         279
  killed by SCORE    38
  killed by AUDIT    72
FINAL PASS           169

top kill reasons at first sighting (a pool can have several):
  too_young                   139639
  few_unique_buyers           133020
  liquidity_low               130933
  volume_below_liquidity       99607
  sells_dominate               37809
  wash_churn                   29586
  overheated                   12888
  missing                       3867
  too_old                       1364
  rc_danger                       21

OUTCOMES (median price change from first sighting / first pass; 8600 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  169    -5.2%   -13.3%   -43.9%   -83.7%    57%
SCOUT PASS, killed later    110    +5.7%    +9.5%    -7.4%   -74.6%    47%
KILLED (tracked)          19559    +0.2%   -59.6%   -85.6%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     467    -92.0%    -68.9%    24%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  36    -69.9%    -49.8%    56%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          8     +1.2%    +30.3%    38%
sells_dominate                  3    -75.0%       -      67%
copy_trade                      3    -96.3%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        78    -55.0%    -93.2%    58%
70-79     112    -44.3%    -72.2%    49%
60-69      64    -29.5%    -86.0%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1120     +0.0%    -11.2%    -46.0%    26%
<15%      295     +2.0%    -14.2%    -40.1%    32%
15-30%     46     -0.1%     -2.0%     +0.4%    33%
30%+       36     -0.7%     -1.1%     +0.8%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      975     +0.0%     -2.2%    -35.1%    25%
<20%      462     +3.3%    -59.6%    -91.4%    27%
20%+       60     -2.9%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1438     +0.3%     -7.3%    -40.1%    26%
20-40%     36     -2.6%    -99.0%    -99.1%    78%
40%+       23    -98.5%    -99.4%       -      78%
tokens analysed: 1322 | helius credits today: 2435/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  169    22%     -9.8%   -14.7%   -99.7%
   -6%     20%  169    24%    -10.1%   -14.9%   -99.7%
   -6%     30%  169    21%    -10.3%   -15.6%   -99.7%
  -10%     12%  169    25%     -9.8%   -17.1%   -99.7%
  -10%     20%  169    27%    -10.2%   -17.7%   -99.7%
  -10%     30%  169    25%    -10.3%   -18.6%   -99.7%
  -15%     12%  169    30%     -9.6%   -19.6%   -99.7%
  -15%     20%  169    32%    -10.1%   -20.4%   -99.7%
  -15%     30%  169    30%    -10.4%   -21.1%   -99.7%
  -25%     12%  169    34%    -11.9%   -17.8%   -99.7%
  -25%     20%  169    38%    -13.1%   -29.2%   -99.7%
  -25%     30%  169    35%    -13.6%   -30.8%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.6% per trade over n=169

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $283.03       $306.80       $476.69
return                        -43.4%        -38.6%         -4.7%
closed trades                    113            92             4
win rate                         21%           21%           25%
avg net / trade                -9.6%        -10.3%        -23.2%
expectancy $/trade            $-1.93        $-2.10        $-5.83
max drawdown                  -47.4%        -43.6%         -5.3%
open now                           1             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $283.03 (-43.4%) | cash $268.29 | open 1 | max drawdown -47.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 113 | win 24/113 (21%) | avg net -9.6% | realized $-217.59 | expectancy $-1.93/trade
exits: stop 83, trail 29, dead_no_route 1
open:
  BASKET       cost $14.12  now $14.74 (+4.4%)  held 0.2h
last trades:
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
  Jesus        $14.62 -> $4.59 (-68.6%)  stop  0.2h
  Scamsem      $14.12 -> $12.59 (-10.9%)  stop  0.2h
  DUVAL        $14.04 -> $8.66 (-38.3%)  stop  0.2h
  BOOBS        $13.77 -> $10.97 (-20.4%)  stop  0.2h
  4CHAN        $13.77 -> $25.64 (+86.2%)  trail  1.3h
  PERRO        $14.45 -> $12.30 (-14.8%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 636, daily_loss_limit 331, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $306.80 (-38.6%) | cash $306.80 | open 0 | max drawdown -43.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 92 | win 19/92 (21%) | avg net -10.3% | realized $-193.20 | expectancy $-2.10/trade
exits: stop 72, trail 20
  (n=92 < 100: noise, not evidence)
last trades:
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 450, daily_loss_limit 240, setup_rejected:dumping_now 151, setup_rejected:sellers_dominate_now 146, setup_rejected:b_bundled 90, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 43, setup_rejected:lp_not_locked 40, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, max_open_positions 1

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
signals skipped by the sizer/risk rules: copy:liquidity_too_low 231, copy:no_price_at_delay 23, copy:no_pool 1

BOOK C per wallet  (watching 8 wallets, 1467 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       4     0   25%   -23.2%   -23.31
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
