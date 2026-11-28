# TrenchLab report

Updated: 2026-11-28 18:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           166624
passed SCOUT         357
  killed by SCORE    42
  killed by AUDIT    112
FINAL PASS           203

top kill reasons at first sighting (a pool can have several):
  too_young                   164465
  few_unique_buyers           156176
  liquidity_low               154307
  volume_below_liquidity      116237
  sells_dominate               45064
  wash_churn                   35492
  overheated                   15363
  missing                       4434
  too_old                       1479
  copy_trade                      69

OUTCOMES (median price change from first sighting / first pass; 10112 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  203    -5.3%   -18.2%   -43.9%   -84.3%    60%
SCOUT PASS, killed later    154    +7.6%   +15.2%    -7.2%   -74.6%    43%
KILLED (tracked)          22651    +0.2%   -55.6%   -84.9%    -0.4%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     671    -81.5%    -68.9%    21%
copy_trade                     69    -69.0%    -94.2%    10%
wash_churn                     64     -1.1%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     21     -3.6%    -56.0%    38%
volume_below_liquidity          9     -2.8%    +40.3%    33%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+       106    -49.4%    -93.3%    50%
70-79     148    -50.8%    -78.0%    55%
60-69      76    -32.0%    -92.1%    54%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1421     +0.5%     -9.1%    -56.1%    24%
<15%      404     +5.6%    -26.5%    -57.5%    31%
15-30%     44     -0.2%     -2.9%     +1.0%    45%
30%+       40     -0.7%     -1.4%     +0.5%    40%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1228     +0.3%     -2.1%    -42.6%    23%
<20%      605     +5.1%    -62.2%    -92.9%    26%
20%+       76     +4.3%    -99.0%  +1071.7%    82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1838     +0.7%     -7.4%    -49.1%    25%
20-40%     42     -0.4%    -99.3%    -99.1%    81%
40%+       29    -97.5%    -99.4%  +1071.7%    76%
tokens analysed: 1722 | helius credits today: 7930/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  203    22%     -9.3%   -14.9%   -99.7%
   -6%     20%  203    24%     -9.3%   -15.1%   -99.7%
   -6%     30%  203    22%     -9.6%   -15.9%   -99.7%
  -10%     12%  203    26%     -9.4%   -17.5%   -99.7%
  -10%     20%  203    28%     -9.5%   -18.2%   -99.7%
  -10%     30%  203    26%     -9.8%   -19.0%   -99.7%
  -15%     12%  203    29%     -9.7%   -20.2%   -99.7%
  -15%     20%  203    32%     -9.9%   -21.0%   -99.7%
  -15%     30%  203    30%    -10.4%   -21.4%   -99.7%
  -25%     12%  203    33%    -12.0%   -21.3%   -99.7%
  -25%     20%  203    37%    -12.8%   -29.6%   -99.7%
  -25%     30%  203    34%    -14.0%   -31.0%   -99.7%
  best so far: stop -6%, trail from +20% -> avg -9.3% per trade over n=203

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $242.99       $293.25       $384.76
return                        -51.4%        -41.3%        -23.0%
closed trades                    144           110            26
win rate                         21%           22%           15%
avg net / trade               -11.0%         -9.4%        -20.3%
expectancy $/trade            $-1.95        $-1.88        $-4.57
max drawdown                  -57.9%        -49.4%        -23.6%
open now                           1             0             2
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $242.99 (-51.4%) | cash $207.72 | open 1 | max drawdown -57.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 144 | win 30/144 (21%) | avg net -11.0% | realized $-281.35 | expectancy $-1.95/trade
exits: stop 108, trail 35, dead_no_route 1
open:
  Artcoin      cost $10.93  now $35.27 (+222.7%)  held 1.2h
last trades:
  VICAT        $12.36 -> $0.05 (-99.6%)  stop  0.7h
  Zhaki        $12.38 -> $9.55 (-22.9%)  stop  0.2h
  MoonBoy      $11.60 -> $10.25 (-11.6%)  stop  0.3h
  STEADY       $11.53 -> $8.80 (-23.7%)  stop  0.2h
  MAYA         $11.40 -> $8.34 (-26.9%)  stop  0.2h
  Memeball     $11.40 -> $10.10 (-11.4%)  stop  2.0h
  SPSC         $11.18 -> $8.27 (-26.0%)  stop  0.3h
  WLFI         $11.03 -> $9.02 (-18.3%)  stop  0.7h
signals skipped by the sizer/risk rules: already_traded_token 768, daily_loss_limit 341, cooldown_after_loss 29, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $293.25 (-41.3%) | cash $293.25 | open 0 | max drawdown -49.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 110 | win 24/110 (22%) | avg net -9.4% | realized $-206.75 | expectancy $-1.88/trade
exits: stop 85, trail 25
last trades:
  DragonRiders $14.14 -> $16.08 (+13.7%)  trail  3.3h
  Fireball     $14.30 -> $11.10 (-22.3%)  stop  0.3h
  DIHBALL      $14.30 -> $9.82 (-31.3%)  stop  0.2h
  Split        $13.92 -> $10.35 (-25.6%)  stop  0.7h
  MEMECARD     $13.92 -> $20.01 (+43.7%)  trail  1.3h
  MoonBoy      $14.05 -> $25.11 (+78.7%)  trail  0.8h
  NBA          $14.60 -> $19.15 (+31.2%)  trail  1.3h
  STEADY       $14.83 -> $11.52 (-22.3%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 458, daily_loss_limit 269, setup_rejected:dumping_now 184, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 124, setup_rejected:operator_cluster 71, setup_rejected:volume_dried_up 61, setup_rejected:lp_not_locked 55, setup_rejected:clustered_supply 47, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:unknown:rugcheck_no_report 15, cooldown_after_loss 12, setup_rejected:rc_danger:Low Liquidity 11, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $384.76 (-23.0%) | cash $340.29 | open 2 | max drawdown -23.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 26 | win 4/26 (15%) | avg net -20.3% | realized $-118.72 | expectancy $-4.57/trade
exits: mirror_sell 24, stop 2
  (n=26 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $25.23 (+16.0%)  held 48.9h
  VIctory      cost $19.24  now $19.24 (+0.0%)  held 0.0h
last trades:
  JVRS         $20.22 -> $16.97 (-16.1%)  mirror_sell  0.3h
  ukiki        $20.04 -> $11.38 (-43.2%)  mirror_sell  0.0h
  BUIDL        $19.62 -> $18.95 (-3.4%)  mirror_sell  0.3h
  HUSS         $19.58 -> $17.36 (-11.3%)  mirror_sell  0.5h
  RALLY        $19.45 -> $26.94 (+38.5%)  mirror_sell  0.5h
  SKS          $19.45 -> $15.29 (-21.4%)  mirror_sell  0.5h
  WARENBUFET   $19.59 -> $18.12 (-7.5%)  mirror_sell  1.2h
  RWA          $19.52 -> $13.92 (-28.7%)  mirror_sell  0.0h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 268, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 31

BOOK C per wallet  (watching 3 wallets, 1859 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
CdF2qk…TyLu   v2-pass             1     1    0%   -45.9%   -10.06
HSq83t…YPbW   v2-near-hold4      19     1   16%   -11.9%   -46.83
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
