# TrenchLab report

Updated: 2026-11-25 09:44 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           142045
passed SCOUT         279
  killed by SCORE    38
  killed by AUDIT    72
FINAL PASS           169

top kill reasons at first sighting (a pool can have several):
  too_young                   140164
  few_unique_buyers           133514
  liquidity_low               131423
  volume_below_liquidity       99983
  sells_dominate               37985
  wash_churn                   29731
  overheated                   12939
  missing                       3880
  too_old                       1370
  rc_danger                       21

OUTCOMES (median price change from first sighting / first pass; 8628 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  169    -5.0%   -13.2%   -43.9%   -83.7%    57%
SCOUT PASS, killed later    110    +5.7%    +9.5%    -7.4%   -74.6%    47%
KILLED (tracked)          19636    +0.2%   -59.7%   -85.6%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     475    -90.6%    -68.9%    24%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  36    -69.3%    -49.8%    56%
overheated                     12    -21.9%    -56.0%    50%
copy_trade                      9    -96.3%       -      33%
volume_below_liquidity          8     +1.2%    +30.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        78    -55.0%    -93.2%    58%
70-79     112    -43.9%    -72.2%    49%
60-69      64    -29.5%    -86.0%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1130     +0.1%    -11.0%    -46.0%    26%
<15%      300     +2.2%    -12.1%    -36.5%    31%
15-30%     46     -0.1%     -2.0%     +0.4%    33%
30%+       36     -0.7%     -1.1%     +0.8%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      985     +0.1%     -2.2%    -34.1%    24%
<20%      467     +3.4%    -58.5%    -91.4%    27%
20%+       60     -2.9%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1453     +0.4%     -7.1%    -40.0%    26%
20-40%     36     -2.6%    -99.0%    -99.1%    78%
40%+       23    -98.5%    -99.4%       -      78%
tokens analysed: 1337 | helius credits today: 3470/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  169    22%     -9.6%   -14.7%   -99.7%
   -6%     20%  169    24%     -9.9%   -14.9%   -99.7%
   -6%     30%  169    21%    -10.1%   -15.6%   -99.7%
  -10%     12%  169    25%     -9.6%   -17.1%   -99.7%
  -10%     20%  169    27%    -10.0%   -17.7%   -99.7%
  -10%     30%  169    25%    -10.1%   -18.6%   -99.7%
  -15%     12%  169    30%     -9.4%   -19.6%   -99.7%
  -15%     20%  169    32%     -9.9%   -20.4%   -99.7%
  -15%     30%  169    30%    -10.2%   -21.1%   -99.7%
  -25%     12%  169    34%    -11.7%   -17.8%   -99.7%
  -25%     20%  169    38%    -12.9%   -29.2%   -99.7%
  -25%     30%  169    35%    -13.4%   -30.8%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.4% per trade over n=169

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $287.76       $306.80       $476.69
return                        -42.4%        -38.6%         -4.7%
closed trades                    114            92             4
win rate                         22%           21%           25%
avg net / trade                -9.2%        -10.3%        -23.2%
expectancy $/trade            $-1.86        $-2.10        $-5.83
max drawdown                  -47.4%        -43.6%         -5.3%
open now                           0             1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $287.76 (-42.4%) | cash $287.76 | open 0 | max drawdown -47.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 114 | win 25/114 (22%) | avg net -9.2% | realized $-212.24 | expectancy $-1.86/trade
exits: stop 83, trail 30, dead_no_route 1
last trades:
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
  Jesus        $14.62 -> $4.59 (-68.6%)  stop  0.2h
  Scamsem      $14.12 -> $12.59 (-10.9%)  stop  0.2h
  DUVAL        $14.04 -> $8.66 (-38.3%)  stop  0.2h
  BOOBS        $13.77 -> $10.97 (-20.4%)  stop  0.2h
  4CHAN        $13.77 -> $25.64 (+86.2%)  trail  1.3h
  PERRO        $14.45 -> $12.30 (-14.8%)  stop  0.3h
  BASKET       $14.12 -> $19.47 (+37.9%)  trail  1.0h
signals skipped by the sizer/risk rules: already_traded_token 649, daily_loss_limit 331, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $306.80 (-38.6%) | cash $291.46 | open 1 | max drawdown -43.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 92 | win 19/92 (21%) | avg net -10.3% | realized $-193.20 | expectancy $-2.10/trade
exits: stop 72, trail 20
  (n=92 < 100: noise, not evidence)
open:
  Amend        cost $15.34  now $15.34 (+0.0%)  held 0.1h
last trades:
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 450, daily_loss_limit 240, setup_rejected:dumping_now 151, setup_rejected:sellers_dominate_now 146, setup_rejected:b_bundled 90, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 43, setup_rejected:lp_not_locked 41, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, max_open_positions 1

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
signals skipped by the sizer/risk rules: copy:liquidity_too_low 241, copy:no_price_at_delay 23, daily_loss_limit 6, copy:no_pool 1

BOOK C per wallet  (watching 8 wallets, 1498 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       4     0   25%   -23.2%   -23.31
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
