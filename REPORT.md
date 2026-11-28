# TrenchLab report

Updated: 2026-11-28 08:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           163637
passed SCOUT         348
  killed by SCORE    42
  killed by AUDIT    104
FINAL PASS           202

top kill reasons at first sighting (a pool can have several):
  too_young                   161493
  few_unique_buyers           153388
  liquidity_low               151510
  volume_below_liquidity      114216
  sells_dominate               44227
  wash_churn                   34759
  overheated                   15081
  missing                       4385
  too_old                       1469
  copy_trade                      67

OUTCOMES (median price change from first sighting / first pass; 9955 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  202    -5.3%   -17.3%   -44.0%   -84.3%    60%
SCOUT PASS, killed later    146    +6.7%   +13.2%   -19.5%   -74.6%    45%
KILLED (tracked)          22292    +0.2%   -55.6%   -84.8%    -0.3%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     642    -81.5%    -68.9%    21%
copy_trade                     67    -72.4%    -94.2%    10%
wash_churn                     63     -1.1%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     21    -12.8%    -56.0%    33%
volume_below_liquidity          9     -2.8%    +40.3%    33%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        99    -52.9%    -93.3%    54%
70-79     146    -51.5%    -77.5%    55%
60-69      76    -34.0%    -92.1%    54%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1383     +0.5%     -9.0%    -54.9%    24%
<15%      382     +4.0%    -26.1%    -57.4%    32%
15-30%     45     -0.1%     -2.9%     +1.0%    44%
30%+       40     -0.7%     -1.4%     +0.5%    40%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1191     +0.2%     -2.2%    -42.1%    24%
<20%      582     +3.3%    -60.8%    -92.8%    26%
20%+       77     +5.9%    -99.1%  +1071.7%    81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1779     +0.6%     -7.2%    -47.5%    25%
20-40%     42     -0.4%    -99.3%    -99.1%    81%
40%+       29    -96.5%    -99.4%  +1071.7%    76%
tokens analysed: 1665 | helius credits today: 3771/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  202    22%    -10.3%   -14.9%   -99.7%
   -6%     20%  202    24%    -10.3%   -15.0%   -99.7%
   -6%     30%  202    21%    -10.6%   -15.8%   -99.7%
  -10%     12%  202    25%    -10.4%   -17.3%   -99.7%
  -10%     20%  202    27%    -10.5%   -18.0%   -99.7%
  -10%     30%  202    25%    -10.8%   -18.9%   -99.7%
  -15%     12%  202    29%    -10.8%   -20.1%   -99.7%
  -15%     20%  202    32%    -10.9%   -21.0%   -99.7%
  -15%     30%  202    29%    -11.5%   -21.4%   -99.7%
  -25%     12%  202    32%    -13.0%   -21.3%   -99.7%
  -25%     20%  202    37%    -13.8%   -29.5%   -99.7%
  -25%     30%  202    34%    -15.1%   -30.9%   -99.7%
  best so far: stop -6%, trail from +20% -> avg -10.3% per trade over n=202

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $220.66       $296.56       $392.39
return                        -55.9%        -40.7%        -21.5%
closed trades                    143           109            24
win rate                         21%           22%           17%
avg net / trade               -11.0%         -9.3%        -20.4%
expectancy $/trade            $-1.95        $-1.87        $-4.65
max drawdown                  -57.5%        -49.4%        -22.7%
open now                           0             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $220.66 (-55.9%) | cash $220.66 | open 0 | max drawdown -57.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 143 | win 30/143 (21%) | avg net -11.0% | realized $-279.34 | expectancy $-1.95/trade
exits: stop 107, trail 35, dead_no_route 1
last trades:
  MEMECARD     $12.62 -> $7.43 (-41.1%)  stop  0.2h
  VICAT        $12.36 -> $0.05 (-99.6%)  stop  0.7h
  Zhaki        $12.38 -> $9.55 (-22.9%)  stop  0.2h
  MoonBoy      $11.60 -> $10.25 (-11.6%)  stop  0.3h
  STEADY       $11.53 -> $8.80 (-23.7%)  stop  0.2h
  MAYA         $11.40 -> $8.34 (-26.9%)  stop  0.2h
  Memeball     $11.40 -> $10.10 (-11.4%)  stop  2.0h
  SPSC         $11.18 -> $8.27 (-26.0%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 767, daily_loss_limit 341, cooldown_after_loss 29, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $296.56 (-40.7%) | cash $296.56 | open 0 | max drawdown -49.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 109 | win 24/109 (22%) | avg net -9.3% | realized $-203.44 | expectancy $-1.87/trade
exits: stop 84, trail 25
last trades:
  KAI          $14.15 -> $15.35 (+8.5%)  trail  2.2h
  DragonRiders $14.14 -> $16.08 (+13.7%)  trail  3.3h
  Fireball     $14.30 -> $11.10 (-22.3%)  stop  0.3h
  DIHBALL      $14.30 -> $9.82 (-31.3%)  stop  0.2h
  Split        $13.92 -> $10.35 (-25.6%)  stop  0.7h
  MEMECARD     $13.92 -> $20.01 (+43.7%)  trail  1.3h
  MoonBoy      $14.05 -> $25.11 (+78.7%)  trail  0.8h
  NBA          $14.60 -> $19.15 (+31.2%)  trail  1.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 458, daily_loss_limit 269, setup_rejected:dumping_now 179, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 114, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 61, setup_rejected:lp_not_locked 55, setup_rejected:clustered_supply 47, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, cooldown_after_loss 12, setup_rejected:rc_danger:Low Liquidity 11, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:unknown:rugcheck_no_report 1, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $392.39 (-21.5%) | cash $366.60 | open 1 | max drawdown -22.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 24 | win 4/24 (17%) | avg net -20.4% | realized $-111.65 | expectancy $-4.65/trade
exits: mirror_sell 22, stop 2
  (n=24 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $25.80 (+18.6%)  held 39.0h
last trades:
  BAOBAO       $21.02 -> $9.54 (-54.6%)  mirror_sell  0.0h
  DOPAMINE     $20.19 -> $14.98 (-25.8%)  mirror_sell  0.5h
  JVRS         $20.22 -> $16.97 (-16.1%)  mirror_sell  0.3h
  ukiki        $20.04 -> $11.38 (-43.2%)  mirror_sell  0.0h
  BUIDL        $19.62 -> $18.95 (-3.4%)  mirror_sell  0.3h
  HUSS         $19.58 -> $17.36 (-11.3%)  mirror_sell  0.5h
  RALLY        $19.45 -> $26.94 (+38.5%)  mirror_sell  0.5h
  SKS          $19.45 -> $15.29 (-21.4%)  mirror_sell  0.5h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 268, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 31

BOOK C per wallet  (watching 3 wallets, 1853 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
HSq83t…YPbW   v2-near-hold4      17     1   18%   -11.2%   -39.76
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
