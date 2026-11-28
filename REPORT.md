# TrenchLab report

Updated: 2026-11-28 02:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           161697
passed SCOUT         344
  killed by SCORE    42
  killed by AUDIT    102
FINAL PASS           200

top kill reasons at first sighting (a pool can have several):
  too_young                   159571
  few_unique_buyers           151616
  liquidity_low               149721
  volume_below_liquidity      112880
  sells_dominate               43704
  wash_churn                   34258
  overheated                   14875
  missing                       4370
  too_old                       1462
  copy_trade                      64

OUTCOMES (median price change from first sighting / first pass; 9845 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  200    -5.2%   -17.3%   -44.0%   -82.6%    60%
SCOUT PASS, killed later    144    +6.7%   +13.2%   -13.5%   -74.6%    45%
KILLED (tracked)          21999    +0.2%   -55.6%   -84.9%    -0.3%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     614    -82.1%    -68.9%    21%
copy_trade                     64    -75.8%    -94.2%    11%
wash_churn                     63     -1.2%    -85.6%    24%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     19    -12.8%    -56.0%    37%
volume_below_liquidity          9     -2.8%    +40.3%    33%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        98    -52.9%    -93.2%    52%
70-79     144    -51.5%    -77.2%    56%
60-69      75    -32.0%    -89.0%    55%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1354     +0.5%     -9.1%    -52.9%    25%
<15%      366     +4.2%    -24.4%    -57.4%    31%
15-30%     43     -0.1%     -2.1%     +1.0%    47%
30%+       40     -0.7%     -1.4%     +0.5%    40%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1165     +0.2%     -2.2%    -40.8%    24%
<20%      564     +4.1%    -58.5%    -92.1%    26%
20%+       74     +2.6%    -99.2%  +1071.7%    82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1733     +0.7%     -7.2%    -45.5%    25%
20-40%     42     -0.4%    -99.2%    -99.1%    81%
40%+       28    -97.5%    -99.4%  +1071.7%    79%
tokens analysed: 1619 | helius credits today: 866/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  200    22%    -10.2%   -14.9%   -99.7%
   -6%     20%  200    24%    -10.3%   -15.0%   -99.7%
   -6%     30%  200    22%    -10.6%   -15.8%   -99.7%
  -10%     12%  200    26%    -10.4%   -17.3%   -99.7%
  -10%     20%  200    28%    -10.5%   -18.0%   -99.7%
  -10%     30%  200    26%    -10.8%   -18.9%   -99.7%
  -15%     12%  200    29%    -10.7%   -20.1%   -99.7%
  -15%     20%  200    32%    -10.9%   -21.0%   -99.7%
  -15%     30%  200    30%    -11.5%   -21.4%   -99.7%
  -25%     12%  200    32%    -12.9%   -21.3%   -99.7%
  -25%     20%  200    37%    -13.8%   -29.5%   -99.7%
  -25%     30%  200    34%    -15.1%   -30.9%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -10.2% per trade over n=200

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $223.92       $296.56       $391.68
return                        -55.2%        -40.7%        -21.7%
closed trades                    141           109            21
win rate                         21%           22%           14%
avg net / trade               -10.9%         -9.3%        -23.6%
expectancy $/trade            $-1.95        $-1.87        $-5.37
max drawdown                  -56.9%        -49.4%        -22.2%
open now                           1             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $223.92 (-55.2%) | cash $213.47 | open 1 | max drawdown -56.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 141 | win 30/141 (21%) | avg net -10.9% | realized $-275.13 | expectancy $-1.95/trade
exits: stop 105, trail 35, dead_no_route 1
open:
  Memeball     cost $11.40  now $10.45 (-8.3%)  held 0.4h
last trades:
  Kibo         $12.81 -> $11.47 (-10.4%)  stop  0.5h
  WINSTON      $12.74 -> $10.21 (-19.8%)  stop  0.2h
  MEMECARD     $12.62 -> $7.43 (-41.1%)  stop  0.2h
  VICAT        $12.36 -> $0.05 (-99.6%)  stop  0.7h
  Zhaki        $12.38 -> $9.55 (-22.9%)  stop  0.2h
  MoonBoy      $11.60 -> $10.25 (-11.6%)  stop  0.3h
  STEADY       $11.53 -> $8.80 (-23.7%)  stop  0.2h
  MAYA         $11.40 -> $8.34 (-26.9%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 760, daily_loss_limit 341, cooldown_after_loss 27, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 458, daily_loss_limit 269, setup_rejected:dumping_now 178, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 111, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 57, setup_rejected:lp_not_locked 55, setup_rejected:clustered_supply 47, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, cooldown_after_loss 12, setup_rejected:rc_danger:Low Liquidity 11, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:unknown:rugcheck_no_report 1, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $391.68 (-21.7%) | cash $365.48 | open 1 | max drawdown -22.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 21 | win 3/21 (14%) | avg net -23.6% | realized $-112.77 | expectancy $-5.37/trade
exits: mirror_sell 19, stop 2
  (n=21 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $26.19 (+20.4%)  held 32.7h
last trades:
  Max          $21.71 -> $13.01 (-40.1%)  mirror_sell  0.3h
  SOL          $21.51 -> $15.04 (-30.1%)  mirror_sell  0.7h
  VCAT         $21.18 -> $17.92 (-15.4%)  mirror_sell  0.2h
  BAOBAO       $21.02 -> $9.54 (-54.6%)  mirror_sell  0.0h
  DOPAMINE     $20.19 -> $14.98 (-25.8%)  mirror_sell  0.5h
  JVRS         $20.22 -> $16.97 (-16.1%)  mirror_sell  0.3h
  ukiki        $20.04 -> $11.38 (-43.2%)  mirror_sell  0.0h
  BUIDL        $19.62 -> $18.95 (-3.4%)  mirror_sell  0.3h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 267, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 3 wallets, 1840 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
HSq83t…YPbW   v2-near-hold4      14     1   14%   -14.0%   -40.87
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
