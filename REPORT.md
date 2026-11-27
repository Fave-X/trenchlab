# TrenchLab report

Updated: 2026-11-27 21:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           160014
passed SCOUT         334
  killed by SCORE    42
  killed by AUDIT    97
FINAL PASS           195

top kill reasons at first sighting (a pool can have several):
  too_young                   157913
  few_unique_buyers           150023
  liquidity_low               148121
  volume_below_liquidity      111667
  sells_dominate               43243
  wash_churn                   33818
  overheated                   14712
  missing                       4337
  too_old                       1450
  copy_trade                      63

OUTCOMES (median price change from first sighting / first pass; 9674 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  195    -5.5%   -19.1%   -44.4%   -82.6%    61%
SCOUT PASS, killed later    139    +6.7%   +11.6%   -13.5%   -74.6%    46%
KILLED (tracked)          21793    +0.2%   -55.6%   -85.0%    -0.3%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     609    -82.8%    -68.9%    21%
copy_trade                     63    -75.8%    -94.2%    11%
wash_churn                     61     -1.2%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     19    -12.8%    -56.0%    37%
volume_below_liquidity          9     +1.2%    +40.3%    33%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        96    -52.9%    -92.9%    53%
70-79     140    -52.0%    -77.5%    56%
60-69      71    -30.1%    -89.0%    56%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1344     +0.4%     -9.0%    -53.4%    25%
<15%      360     +3.4%    -19.5%    -53.6%    31%
15-30%     41     -0.2%     -2.9%     +1.0%    46%
30%+       40     -0.7%     -1.1%     +0.5%    40%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1156     +0.2%     -2.1%    -40.8%    24%
<20%      557     +3.3%    -58.5%    -92.1%    26%
20%+       72     +0.1%    -99.2%  +1071.7%    83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1717     +0.6%     -6.9%    -45.5%    25%
20-40%     41     -0.7%    -99.1%    -99.1%    80%
40%+       27    -98.5%    -99.4%  +1071.7%    78%
tokens analysed: 1601 | helius credits today: 8009/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  195    21%    -11.0%   -15.1%   -99.7%
   -6%     20%  195    23%    -11.0%   -15.1%   -99.7%
   -6%     30%  195    21%    -11.3%   -15.9%   -99.7%
  -10%     12%  195    25%    -11.1%   -17.7%   -99.7%
  -10%     20%  195    27%    -11.3%   -18.6%   -99.7%
  -10%     30%  195    25%    -11.5%   -19.1%   -99.7%
  -15%     12%  195    28%    -11.5%   -20.3%   -99.7%
  -15%     20%  195    31%    -11.7%   -21.0%   -99.7%
  -15%     30%  195    29%    -12.2%   -21.4%   -99.7%
  -25%     12%  195    32%    -13.6%   -21.3%   -99.7%
  -25%     20%  195    36%    -14.5%   -29.6%   -99.7%
  -25%     30%  195    33%    -15.6%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -11.0% per trade over n=195

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $232.01       $276.35       $400.70
return                        -53.6%        -44.7%        -19.9%
closed trades                    138           106            19
win rate                         22%           20%           16%
avg net / trade               -10.7%        -11.0%        -23.7%
expectancy $/trade            $-1.94        $-2.12        $-5.44
max drawdown                  -55.4%        -49.4%        -20.4%
open now                           0             1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $232.01 (-53.6%) | cash $232.01 | open 0 | max drawdown -55.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 138 | win 30/138 (22%) | avg net -10.7% | realized $-267.99 | expectancy $-1.94/trade
exits: stop 102, trail 35, dead_no_route 1
last trades:
  DragonRiders $12.44 -> $10.43 (-16.2%)  stop  0.2h
  KAI          $12.36 -> $13.64 (+10.3%)  trail  3.3h
  SpaceXCoin   $12.25 -> $21.94 (+79.1%)  trail  2.2h
  Kibo         $12.81 -> $11.47 (-10.4%)  stop  0.5h
  WINSTON      $12.74 -> $10.21 (-19.8%)  stop  0.2h
  MEMECARD     $12.62 -> $7.43 (-41.1%)  stop  0.2h
  VICAT        $12.36 -> $0.05 (-99.6%)  stop  0.7h
  Zhaki        $12.38 -> $9.55 (-22.9%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 744, daily_loss_limit 331, cooldown_after_loss 26, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $276.35 (-44.7%) | cash $260.94 | open 1 | max drawdown -49.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 106 | win 21/106 (20%) | avg net -11.0% | realized $-225.14 | expectancy $-2.12/trade
exits: stop 84, trail 22
open:
  MEMECARD     cost $13.92  now $15.41 (+10.7%)  held 1.0h
last trades:
  PAIR         $14.61 -> $9.69 (-33.7%)  stop  0.5h
  Hoppy        $14.36 -> $11.68 (-18.7%)  stop  0.5h
  DEXDATA      $14.23 -> $12.68 (-10.9%)  stop  0.7h
  KAI          $14.15 -> $15.35 (+8.5%)  trail  2.2h
  DragonRiders $14.14 -> $16.08 (+13.7%)  trail  3.3h
  Fireball     $14.30 -> $11.10 (-22.3%)  stop  0.3h
  DIHBALL      $14.30 -> $9.82 (-31.3%)  stop  0.2h
  Split        $13.92 -> $10.35 (-25.6%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 177, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 104, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 51, setup_rejected:clustered_supply 47, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, cooldown_after_loss 12, setup_rejected:rc_danger:Low Liquidity 11, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:unknown:rugcheck_no_report 1, max_open_positions 1

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
  santa        cost $21.75  now $25.89 (+19.0%)  held 27.4h
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
