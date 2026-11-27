# TrenchLab report

Updated: 2026-11-27 14:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           157844
passed SCOUT         328
  killed by SCORE    42
  killed by AUDIT    95
FINAL PASS           191

top kill reasons at first sighting (a pool can have several):
  too_young                   155765
  few_unique_buyers           147998
  liquidity_low               146086
  volume_below_liquidity      110166
  sells_dominate               42640
  wash_churn                   33380
  overheated                   14511
  missing                       4284
  too_old                       1441
  copy_trade                      61

OUTCOMES (median price change from first sighting / first pass; 9551 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  191    -5.3%   -18.2%   -45.0%   -82.6%    60%
SCOUT PASS, killed later    137    +6.7%   +11.6%   -13.5%   -74.6%    45%
KILLED (tracked)          21526    +0.2%   -56.0%   -85.1%    -0.4%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     601    -85.4%    -68.9%    21%
wash_churn                     61     -1.2%    -85.6%    25%
copy_trade                     61    -75.8%    -94.9%    11%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  38    -68.7%    -72.0%    55%
overheated                     19    -12.8%    -56.0%    37%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        94    -52.9%    -92.9%    53%
70-79     137    -52.8%    -76.6%    54%
60-69      70    -30.1%    -89.0%    57%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1326     +0.4%     -9.2%    -52.1%    25%
<15%      354     +4.1%    -19.5%    -53.6%    31%
15-30%     41     -0.2%     -2.9%     +1.0%    46%
30%+       39     -0.7%     -1.1%     +0.5%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1140     +0.2%     -2.2%    -40.0%    24%
<20%      550     +3.5%    -60.6%    -92.1%    26%
20%+       70     +0.1%    -99.2%  +1071.7%    83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1694     +0.7%     -7.2%    -44.5%    25%
20-40%     39     -0.7%    -99.0%    -99.1%    79%
40%+       27    -98.5%    -99.4%  +1071.7%    78%
tokens analysed: 1577 | helius credits today: 6005/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  191    21%    -10.7%   -14.9%   -99.7%
   -6%     20%  191    24%    -10.8%   -15.1%   -99.7%
   -6%     30%  191    21%    -11.0%   -15.7%   -99.7%
  -10%     12%  191    25%    -10.4%   -17.1%   -99.7%
  -10%     20%  191    27%    -10.6%   -17.8%   -99.7%
  -10%     30%  191    25%    -10.7%   -18.7%   -99.7%
  -15%     12%  191    29%    -10.8%   -20.1%   -99.7%
  -15%     20%  191    32%    -11.0%   -21.0%   -99.7%
  -15%     30%  191    29%    -11.4%   -21.3%   -99.7%
  -25%     12%  191    32%    -12.8%   -21.3%   -99.7%
  -25%     20%  191    37%    -13.8%   -29.6%   -99.7%
  -25%     30%  191    34%    -14.9%   -30.9%   -99.7%
  best so far: stop -10%, trail from +12% -> avg -10.4% per trade over n=191

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $254.87       $286.10       $408.93
return                        -49.0%        -42.8%        -18.2%
closed trades                    134           103            17
win rate                         22%           20%           18%
avg net / trade                -9.6%        -10.5%        -24.0%
expectancy $/trade            $-1.83        $-2.08        $-5.59
max drawdown                  -52.9%        -48.1%        -18.8%
open now                           0             0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $254.87 (-49.0%) | cash $254.87 | open 0 | max drawdown -52.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 134 | win 30/134 (22%) | avg net -9.6% | realized $-245.13 | expectancy $-1.83/trade
exits: stop 98, trail 35, dead_no_route 1
last trades:
  KURO         $12.69 -> $15.15 (+19.4%)  trail  0.3h
  Hoppy        $12.81 -> $7.02 (-45.2%)  stop  0.2h
  Vetocat      $12.52 -> $10.86 (-13.3%)  stop  0.2h
  DEXDATA      $12.52 -> $11.02 (-12.0%)  stop  0.5h
  DragonRiders $12.44 -> $10.43 (-16.2%)  stop  0.2h
  KAI          $12.36 -> $13.64 (+10.3%)  trail  3.3h
  SpaceXCoin   $12.25 -> $21.94 (+79.1%)  trail  2.2h
  Kibo         $12.81 -> $11.47 (-10.4%)  stop  0.5h
signals skipped by the sizer/risk rules: already_traded_token 724, daily_loss_limit 331, cooldown_after_loss 26, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $286.10 (-42.8%) | cash $286.10 | open 0 | max drawdown -48.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 103 | win 21/103 (20%) | avg net -10.5% | realized $-213.90 | expectancy $-2.08/trade
exits: stop 81, trail 22
last trades:
  Grodia       $14.91 -> $13.02 (-12.7%)  stop  0.3h
  NORFEATH     $14.82 -> $12.87 (-13.2%)  stop  0.5h
  duk          $14.72 -> $12.42 (-15.6%)  stop  0.2h
  PAIR         $14.61 -> $9.69 (-33.7%)  stop  0.5h
  Hoppy        $14.36 -> $11.68 (-18.7%)  stop  0.5h
  DEXDATA      $14.23 -> $12.68 (-10.9%)  stop  0.7h
  KAI          $14.15 -> $15.35 (+8.5%)  trail  2.2h
  DragonRiders $14.14 -> $16.08 (+13.7%)  trail  3.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 167, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 96, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 51, setup_rejected:clustered_supply 41, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:rc_danger:Low Liquidity 11, cooldown_after_loss 9, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:unknown:rugcheck_no_report 1, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $408.93 (-18.2%) | cash $383.27 | open 1 | max drawdown -18.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 17 | win 3/17 (18%) | avg net -24.0% | realized $-94.98 | expectancy $-5.59/trade
exits: mirror_sell 15, stop 2
  (n=17 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $25.66 (+18.0%)  held 20.5h
last trades:
  LOBBY        $21.81 -> $30.42 (+39.5%)  mirror_sell  0.0h
  GIVE         $22.24 -> $17.38 (-21.9%)  mirror_sell  0.0h
  COSMOS       $21.99 -> $18.46 (-16.0%)  mirror_sell  0.0h
  Pnp          $21.82 -> $20.41 (-6.5%)  mirror_sell  0.2h
  Max          $21.71 -> $13.01 (-40.1%)  mirror_sell  0.3h
  SOL          $21.51 -> $15.04 (-30.1%)  mirror_sell  0.7h
  VCAT         $21.18 -> $17.92 (-15.4%)  mirror_sell  0.2h
  BAOBAO       $21.02 -> $9.54 (-54.6%)  mirror_sell  0.0h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 267, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 3 wallets, 1832 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
HSq83t…YPbW   v2-near-hold4      10     1   20%   -10.7%   -23.09
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
