# TrenchLab report

Updated: 2026-11-24 16:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           136917
passed SCOUT         264
  killed by SCORE    37
  killed by AUDIT    65
FINAL PASS           162

top kill reasons at first sighting (a pool can have several):
  too_young                   135091
  few_unique_buyers           128728
  liquidity_low               126622
  volume_below_liquidity       96455
  sells_dominate               36499
  wash_churn                   28613
  overheated                   12384
  missing                       3761
  too_old                       1338
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 8297 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  162    -5.2%   -14.9%   -43.9%   -83.7%    59%
SCOUT PASS, killed later    102    +5.6%    +7.5%   -13.5%   -75.1%    49%
KILLED (tracked)          19000    +0.1%   -59.6%   -85.3%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     438    -93.5%    -68.9%    24%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        51     -0.7%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%
copy_trade                      1    -95.5%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        73    -55.0%    -93.2%    60%
70-79     104    -43.9%    -72.2%    52%
60-69      62    -29.5%    -89.0%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1076     +0.0%     -9.9%    -46.6%    26%
<15%      270     +2.1%    -16.8%    -45.0%    33%
15-30%     45     -0.2%     -1.7%     +0.4%    31%
30%+       38     -0.6%     -0.7%     +1.9%    37%
bundled     n   +1h med   +4h med  +24h med   rug%
none      939     +0.0%     -2.1%    -35.1%    25%
<20%      431     +2.6%    -62.2%    -91.4%    28%
20%+       59     -5.1%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1372     +0.2%     -6.8%    -40.1%    26%
20-40%     35     -4.5%    -99.0%    -99.1%    77%
40%+       22    -98.6%    -99.0%       -      77%
tokens analysed: 1259 | helius credits today: 6019/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  162    22%    -10.2%   -14.6%   -99.7%
   -6%     20%  162    23%    -10.5%   -14.9%   -99.7%
   -6%     30%  162    20%    -10.7%   -15.5%   -99.7%
  -10%     12%  162    25%    -10.3%   -17.3%   -99.7%
  -10%     20%  162    26%    -10.7%   -17.8%   -99.7%
  -10%     30%  162    24%    -10.7%   -18.6%   -99.7%
  -15%     12%  162    29%    -10.0%   -19.6%   -99.7%
  -15%     20%  162    31%    -10.5%   -20.6%   -99.7%
  -15%     30%  162    29%    -10.9%   -21.2%   -99.7%
  -25%     12%  162    33%    -12.0%   -18.2%   -99.7%
  -25%     20%  162    37%    -13.6%   -29.7%   -99.7%
  -25%     30%  162    34%    -14.0%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -10.0% per trade over n=162

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $275.49       $320.32       $496.48
return                        -44.9%        -35.9%         -0.7%
closed trades                    110            88             1
win rate                         21%           22%            0%
avg net / trade               -10.4%         -9.8%        -14.1%
expectancy $/trade            $-2.04        $-2.04        $-3.52
max drawdown                  -47.0%        -41.1%         -0.7%
open now                           0             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $275.49 (-44.9%) | cash $275.49 | open 0 | max drawdown -47.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 110 | win 23/110 (21%) | avg net -10.4% | realized $-224.51 | expectancy $-2.04/trade
exits: stop 81, trail 28, dead_no_route 1
last trades:
  cCAT         $15.02 -> $17.11 (+13.9%)  trail  0.3h
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
  ChristmASS   $15.10 -> $9.98 (-33.9%)  stop  0.2h
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
  Jesus        $14.62 -> $4.59 (-68.6%)  stop  0.2h
  Scamsem      $14.12 -> $12.59 (-10.9%)  stop  0.2h
  DUVAL        $14.04 -> $8.66 (-38.3%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 619, daily_loss_limit 322, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $320.32 (-35.9%) | cash $320.32 | open 0 | max drawdown -41.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 88 | win 19/88 (22%) | avg net -9.8% | realized $-179.68 | expectancy $-2.04/trade
exits: stop 68, trail 20
  (n=88 < 100: noise, not evidence)
last trades:
  cCAT         $17.38 -> $13.20 (-24.0%)  stop  0.2h
  UCASH        $17.17 -> $17.37 (+1.2%)  trail  0.8h
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 450, daily_loss_limit 240, setup_rejected:dumping_now 145, setup_rejected:sellers_dominate_now 142, setup_rejected:b_bundled 77, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:clustered_supply 38, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $496.48 (-0.7%) | cash $496.48 | open 0 | max drawdown -0.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 1 | win 0/1 (0%) | avg net -14.1% | realized $-3.52 | expectancy $-3.52/trade
exits: mirror_sell 1
  (n=1 < 100: noise, not evidence)
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 37, copy:no_price_at_delay 2

BOOK C per wallet  (watching 8 wallets, 333 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       1     0    0%   -14.1%    -3.52
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
