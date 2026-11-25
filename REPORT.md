# TrenchLab report

Updated: 2026-11-25 19:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           144835
passed SCOUT         283
  killed by SCORE    38
  killed by AUDIT    73
FINAL PASS           172

top kill reasons at first sighting (a pool can have several):
  too_young                   142900
  few_unique_buyers           136103
  liquidity_low               133783
  volume_below_liquidity      101556
  sells_dominate               38836
  wash_churn                   30325
  overheated                   13196
  missing                       4202
  too_old                       1376
  copy_trade                      49

OUTCOMES (median price change from first sighting / first pass; 8784 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  172    -5.4%   -13.2%   -43.2%   -83.0%    58%
SCOUT PASS, killed later    111    +5.6%   +10.7%    -7.2%   -74.6%    47%
KILLED (tracked)          19902    +0.2%   -59.6%   -85.6%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     484    -90.6%    -68.9%    24%
wash_churn                     57    -23.3%    -85.6%    26%
too_old                        52     -0.6%     -0.4%    10%
copy_trade                     49    -95.9%    -95.6%     8%
liquidity_low                  36    -69.3%    -49.8%    56%
overheated                     12    -21.9%    -56.0%    50%
volume_below_liquidity          8     +1.2%    +30.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        79    -52.9%    -93.2%    57%
70-79     114    -43.9%    -75.0%    51%
60-69      65    -30.1%    -86.0%    55%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1152     +0.2%    -11.0%    -51.4%    26%
<15%      305     +1.7%    -11.2%    -32.5%    30%
15-30%     36     -0.1%     -2.9%     +0.4%    44%
30%+       36     -0.7%     -1.1%     +0.8%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      995     +0.1%     -2.2%    -35.1%    25%
<20%      473     +3.4%    -58.4%    -87.0%    27%
20%+       61     -0.7%    -99.0%       -      84%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1470     +0.4%     -7.1%    -40.8%    26%
20-40%     36     -2.6%    -99.0%    -99.1%    78%
40%+       23    -98.5%    -99.4%       -      78%
tokens analysed: 1351 | helius credits today: 5211/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  172    22%     -9.9%   -14.9%   -99.7%
   -6%     20%  172    23%    -10.2%   -15.0%   -99.7%
   -6%     30%  172    21%    -10.3%   -15.7%   -99.7%
  -10%     12%  172    25%     -9.9%   -17.3%   -99.7%
  -10%     20%  172    26%    -10.3%   -17.8%   -99.7%
  -10%     30%  172    24%    -10.3%   -18.6%   -99.7%
  -15%     12%  172    29%     -9.8%   -19.8%   -99.7%
  -15%     20%  172    31%    -10.2%   -20.7%   -99.7%
  -15%     30%  172    29%    -10.5%   -21.2%   -99.7%
  -25%     12%  172    33%    -12.0%   -19.6%   -99.7%
  -25%     20%  172    37%    -13.2%   -29.3%   -99.7%
  -25%     30%  172    34%    -13.8%   -30.8%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.8% per trade over n=172

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $277.39       $299.99       $438.16
return                        -44.5%        -40.0%        -12.4%
closed trades                    117            94             6
win rate                         21%           20%           17%
avg net / trade                -9.6%        -10.5%        -42.4%
expectancy $/trade            $-1.90        $-2.13       $-10.31
max drawdown                  -47.4%        -44.8%        -13.0%
open now                           0             0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $277.39 (-44.5%) | cash $277.39 | open 0 | max drawdown -47.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 117 | win 25/117 (21%) | avg net -9.6% | realized $-222.61 | expectancy $-1.90/trade
exits: stop 86, trail 30, dead_no_route 1
last trades:
  DUVAL        $14.04 -> $8.66 (-38.3%)  stop  0.2h
  BOOBS        $13.77 -> $10.97 (-20.4%)  stop  0.2h
  4CHAN        $13.77 -> $25.64 (+86.2%)  trail  1.3h
  PERRO        $14.45 -> $12.30 (-14.8%)  stop  0.3h
  BASKET       $14.12 -> $19.47 (+37.9%)  trail  1.0h
  JaoJiu       $14.39 -> $11.41 (-20.7%)  stop  0.2h
  Pompom       $14.24 -> $12.17 (-14.5%)  stop  0.2h
  GRAUDIA      $14.14 -> $8.83 (-37.6%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 658, daily_loss_limit 331, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $299.99 (-40.0%) | cash $299.99 | open 0 | max drawdown -44.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 94 | win 19/94 (20%) | avg net -10.5% | realized $-200.01 | expectancy $-2.13/trade
exits: stop 74, trail 20
  (n=94 < 100: noise, not evidence)
last trades:
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
  PERRO        $15.87 -> $13.75 (-13.4%)  stop  0.2h
  4CHAN        $15.51 -> $12.17 (-21.5%)  stop  0.2h
  Amend        $15.34 -> $12.38 (-19.3%)  stop  0.5h
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 452, daily_loss_limit 265, setup_rejected:dumping_now 157, setup_rejected:sellers_dominate_now 146, setup_rejected:b_bundled 90, setup_rejected:volume_dried_up 60, setup_rejected:operator_cluster 43, setup_rejected:lp_not_locked 41, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $438.16 (-12.4%) | cash $438.16 | open 0 | max drawdown -13.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 6 | win 1/6 (17%) | avg net -42.4% | realized $-61.84 | expectancy $-10.31/trade
exits: mirror_sell 5, stop 1
  (n=6 < 100: noise, not evidence)
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
  BEAST        $24.80 -> $29.54 (+19.1%)  mirror_sell  0.2h
  JENSEN       $25.04 -> $0.93 (-96.3%)  stop  0.3h
  JENSEN       $23.83 -> $7.18 (-69.9%)  mirror_sell  0.0h
  JENSEN       $23.83 -> $1.96 (-91.8%)  mirror_sell  0.0h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 264, copy:no_pool 53, daily_loss_limit 50, copy:no_price_at_delay 29

BOOK C per wallet  (watching 2 wallets, 1771 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
