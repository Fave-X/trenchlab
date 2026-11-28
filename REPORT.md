# TrenchLab report

Updated: 2026-11-28 00:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           161027
passed SCOUT         339
  killed by SCORE    42
  killed by AUDIT    99
FINAL PASS           198

top kill reasons at first sighting (a pool can have several):
  too_young                   158911
  few_unique_buyers           150983
  liquidity_low               149088
  volume_below_liquidity      112420
  sells_dominate               43529
  wash_churn                   34083
  overheated                   14808
  missing                       4355
  too_old                       1459
  copy_trade                      63

OUTCOMES (median price change from first sighting / first pass; 9710 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  198    -5.2%   -17.3%   -44.4%   -83.0%    60%
SCOUT PASS, killed later    141    +6.7%   +13.2%   -19.5%   -74.6%    45%
KILLED (tracked)          21915    +0.2%   -55.6%   -85.0%    -0.3%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     611    -82.1%    -68.9%    21%
wash_churn                     63     -1.2%    -85.6%    24%
copy_trade                     63    -75.8%    -94.2%    11%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     19    -12.8%    -56.0%    37%
volume_below_liquidity          9     -2.8%    +40.3%    33%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        97    -52.9%    -93.2%    53%
70-79     143    -52.5%    -77.5%    55%
60-69      72    -30.1%    -89.0%    56%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1349     +0.5%     -9.0%    -53.4%    25%
<15%      363     +4.0%    -22.8%    -57.4%    31%
15-30%     42     -0.1%     -2.9%     +1.0%    45%
30%+       40     -0.7%     -1.4%     +0.5%    40%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1159     +0.2%     -2.1%    -40.8%    24%
<20%      561     +3.5%    -58.5%    -92.8%    26%
20%+       74     +0.9%    -99.2%  +1071.7%    81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1724     +0.7%     -7.2%    -46.0%    25%
20-40%     42     -0.4%    -99.2%    -99.1%    79%
40%+       28    -97.5%    -99.4%  +1071.7%    75%
tokens analysed: 1610 | helius credits today: 118/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  198    22%    -10.2%   -14.9%   -99.7%
   -6%     20%  198    24%    -10.2%   -15.0%   -99.7%
   -6%     30%  198    21%    -10.6%   -15.8%   -99.7%
  -10%     12%  198    25%    -10.3%   -17.3%   -99.7%
  -10%     20%  198    27%    -10.5%   -18.0%   -99.7%
  -10%     30%  198    25%    -10.8%   -18.9%   -99.7%
  -15%     12%  198    29%    -10.7%   -20.1%   -99.7%
  -15%     20%  198    32%    -10.9%   -21.0%   -99.7%
  -15%     30%  198    29%    -11.5%   -21.4%   -99.7%
  -25%     12%  198    32%    -12.9%   -21.3%   -99.7%
  -25%     20%  198    37%    -13.8%   -29.6%   -99.7%
  -25%     30%  198    34%    -15.0%   -30.9%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -10.2% per trade over n=198

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $232.99       $292.00       $400.70
return                        -53.4%        -41.6%        -19.9%
closed trades                    138           108            19
win rate                         22%           21%           16%
avg net / trade               -10.7%         -9.6%        -23.7%
expectancy $/trade            $-1.94        $-1.93        $-5.44
max drawdown                  -55.4%        -49.4%        -20.4%
open now                           1             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $232.99 (-53.4%) | cash $220.41 | open 1 | max drawdown -55.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 138 | win 30/138 (22%) | avg net -10.7% | realized $-267.99 | expectancy $-1.94/trade
exits: stop 102, trail 35, dead_no_route 1
open:
  MoonBoy      cost $11.60  now $12.58 (+8.5%)  held 0.2h
last trades:
  DragonRiders $12.44 -> $10.43 (-16.2%)  stop  0.2h
  KAI          $12.36 -> $13.64 (+10.3%)  trail  3.3h
  SpaceXCoin   $12.25 -> $21.94 (+79.1%)  trail  2.2h
  Kibo         $12.81 -> $11.47 (-10.4%)  stop  0.5h
  WINSTON      $12.74 -> $10.21 (-19.8%)  stop  0.2h
  MEMECARD     $12.62 -> $7.43 (-41.1%)  stop  0.2h
  VICAT        $12.36 -> $0.05 (-99.6%)  stop  0.7h
  Zhaki        $12.38 -> $9.55 (-22.9%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 748, daily_loss_limit 341, cooldown_after_loss 26, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $292.00 (-41.6%) | cash $292.00 | open 0 | max drawdown -49.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 108 | win 23/108 (21%) | avg net -9.6% | realized $-208.00 | expectancy $-1.93/trade
exits: stop 84, trail 24
last trades:
  DEXDATA      $14.23 -> $12.68 (-10.9%)  stop  0.7h
  KAI          $14.15 -> $15.35 (+8.5%)  trail  2.2h
  DragonRiders $14.14 -> $16.08 (+13.7%)  trail  3.3h
  Fireball     $14.30 -> $11.10 (-22.3%)  stop  0.3h
  DIHBALL      $14.30 -> $9.82 (-31.3%)  stop  0.2h
  Split        $13.92 -> $10.35 (-25.6%)  stop  0.7h
  MEMECARD     $13.92 -> $20.01 (+43.7%)  trail  1.3h
  MoonBoy      $14.05 -> $25.11 (+78.7%)  trail  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 458, daily_loss_limit 269, setup_rejected:dumping_now 178, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 111, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 57, setup_rejected:lp_not_locked 51, setup_rejected:clustered_supply 47, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, cooldown_after_loss 12, setup_rejected:rc_danger:Low Liquidity 11, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:unknown:rugcheck_no_report 1, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $400.70 (-19.9%) | cash $374.81 | open 1 | max drawdown -20.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 19 | win 3/19 (16%) | avg net -23.7% | realized $-103.44 | expectancy $-5.44/trade
exits: mirror_sell 17, stop 2
  (n=19 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $25.89 (+19.0%)  held 30.7h
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
