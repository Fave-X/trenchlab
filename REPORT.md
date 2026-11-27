# TrenchLab report

Updated: 2026-11-27 19:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           159487
passed SCOUT         332
  killed by SCORE    42
  killed by AUDIT    97
FINAL PASS           193

top kill reasons at first sighting (a pool can have several):
  too_young                   157386
  few_unique_buyers           149521
  liquidity_low               147624
  volume_below_liquidity      111275
  sells_dominate               43093
  wash_churn                   33690
  overheated                   14662
  missing                       4325
  too_old                       1450
  copy_trade                      63

OUTCOMES (median price change from first sighting / first pass; 9648 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  193    -5.5%   -19.1%   -44.4%   -82.6%    61%
SCOUT PASS, killed later    139    +6.7%   +11.6%    -7.4%   -74.6%    45%
KILLED (tracked)          21731    +0.2%   -55.6%   -85.0%    -0.3%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     607    -82.8%    -68.9%    21%
copy_trade                     63    -75.8%    -94.2%    11%
wash_churn                     61     -1.2%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  38    -69.3%    -72.0%    55%
overheated                     19    -12.8%    -56.0%    37%
volume_below_liquidity          9     +1.2%    +40.3%    33%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        94    -52.9%    -92.9%    53%
70-79     141    -51.5%    -77.5%    55%
60-69      70    -30.1%    -89.0%    57%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1337     +0.4%     -9.0%    -53.4%    25%
<15%      360     +3.7%    -19.5%    -53.6%    31%
15-30%     41     -0.2%     -2.9%     +1.0%    46%
30%+       40     -0.7%     -1.1%     +0.5%    38%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1150     +0.2%     -2.1%    -40.8%    24%
<20%      556     +3.3%    -59.6%    -92.1%    26%
20%+       72     +0.1%    -99.1%  +1071.7%    82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1710     +0.6%     -6.9%    -45.5%    25%
20-40%     41     -0.7%    -99.0%    -99.1%    78%
40%+       27    -98.5%    -99.4%  +1071.7%    78%
tokens analysed: 1594 | helius credits today: 7510/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  193    21%    -11.0%   -15.1%   -99.7%
   -6%     20%  193    23%    -11.0%   -15.1%   -99.7%
   -6%     30%  193    21%    -11.2%   -15.9%   -99.7%
  -10%     12%  193    25%    -10.6%   -17.5%   -99.7%
  -10%     20%  193    27%    -10.8%   -18.2%   -99.7%
  -10%     30%  193    25%    -11.0%   -19.0%   -99.7%
  -15%     12%  193    28%    -11.0%   -20.2%   -99.7%
  -15%     20%  193    32%    -11.2%   -21.0%   -99.7%
  -15%     30%  193    29%    -11.6%   -21.3%   -99.7%
  -25%     12%  193    32%    -13.2%   -21.3%   -99.7%
  -25%     20%  193    37%    -14.1%   -29.6%   -99.7%
  -25%     30%  193    34%    -15.2%   -31.0%   -99.7%
  best so far: stop -10%, trail from +12% -> avg -10.6% per trade over n=193

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $247.15       $278.42       $401.10
return                        -50.6%        -44.3%        -19.8%
closed trades                    136           105            19
win rate                         22%           20%           16%
avg net / trade                -9.9%        -10.8%        -23.7%
expectancy $/trade            $-1.86        $-2.11        $-5.44
max drawdown                  -52.9%        -48.8%        -20.3%
open now                           0             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $247.15 (-50.6%) | cash $247.15 | open 0 | max drawdown -52.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 136 | win 30/136 (22%) | avg net -9.9% | realized $-252.85 | expectancy $-1.86/trade
exits: stop 100, trail 35, dead_no_route 1
last trades:
  Vetocat      $12.52 -> $10.86 (-13.3%)  stop  0.2h
  DEXDATA      $12.52 -> $11.02 (-12.0%)  stop  0.5h
  DragonRiders $12.44 -> $10.43 (-16.2%)  stop  0.2h
  KAI          $12.36 -> $13.64 (+10.3%)  trail  3.3h
  SpaceXCoin   $12.25 -> $21.94 (+79.1%)  trail  2.2h
  Kibo         $12.81 -> $11.47 (-10.4%)  stop  0.5h
  WINSTON      $12.74 -> $10.21 (-19.8%)  stop  0.2h
  MEMECARD     $12.62 -> $7.43 (-41.1%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 737, daily_loss_limit 331, cooldown_after_loss 26, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $278.42 (-44.3%) | cash $278.42 | open 0 | max drawdown -48.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 105 | win 21/105 (20%) | avg net -10.8% | realized $-221.58 | expectancy $-2.11/trade
exits: stop 83, trail 22
last trades:
  duk          $14.72 -> $12.42 (-15.6%)  stop  0.2h
  PAIR         $14.61 -> $9.69 (-33.7%)  stop  0.5h
  Hoppy        $14.36 -> $11.68 (-18.7%)  stop  0.5h
  DEXDATA      $14.23 -> $12.68 (-10.9%)  stop  0.7h
  KAI          $14.15 -> $15.35 (+8.5%)  trail  2.2h
  DragonRiders $14.14 -> $16.08 (+13.7%)  trail  3.3h
  Fireball     $14.30 -> $11.10 (-22.3%)  stop  0.3h
  DIHBALL      $14.30 -> $9.82 (-31.3%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 172, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 100, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 51, setup_rejected:clustered_supply 47, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:rc_danger:Low Liquidity 11, cooldown_after_loss 9, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:unknown:rugcheck_no_report 1, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $401.10 (-19.8%) | cash $374.81 | open 1 | max drawdown -20.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 19 | win 3/19 (16%) | avg net -23.7% | realized $-103.44 | expectancy $-5.44/trade
exits: mirror_sell 17, stop 2
  (n=19 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $26.29 (+20.9%)  held 25.7h
last trades:
  COSMOS       $21.99 -> $18.46 (-16.0%)  mirror_sell  0.0h
  Pnp          $21.82 -> $20.41 (-6.5%)  mirror_sell  0.2h
  Max          $21.71 -> $13.01 (-40.1%)  mirror_sell  0.3h
  SOL          $21.51 -> $15.04 (-30.1%)  mirror_sell  0.7h
  VCAT         $21.18 -> $17.92 (-15.4%)  mirror_sell  0.2h
  BAOBAO       $21.02 -> $9.54 (-54.6%)  mirror_sell  0.0h
  DOPAMINE     $20.19 -> $14.98 (-25.8%)  mirror_sell  0.5h
  JVRS         $20.22 -> $16.97 (-16.1%)  mirror_sell  0.3h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 267, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 3 wallets, 1836 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
HSq83t…YPbW   v2-near-hold4      12     1   17%   -12.4%   -31.54
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
