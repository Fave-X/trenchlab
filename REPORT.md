# TrenchLab report

Updated: 2026-11-24 22:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           138548
passed SCOUT         269
  killed by SCORE    37
  killed by AUDIT    67
FINAL PASS           165

top kill reasons at first sighting (a pool can have several):
  too_young                   136705
  few_unique_buyers           130243
  liquidity_low               128141
  volume_below_liquidity       97565
  sells_dominate               36991
  wash_churn                   28914
  overheated                   12545
  missing                       3808
  too_old                       1353
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 8418 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  165    -5.0%   -14.1%   -43.9%   -85.3%    58%
SCOUT PASS, killed later    104    +5.6%    +7.5%   -19.5%   -75.1%    49%
KILLED (tracked)          19210    +0.1%   -60.1%   -85.4%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     449    -90.6%    -68.9%    25%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        52     -0.7%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          8     +1.2%    +30.3%    38%
sells_dominate                  3    -75.0%       -      67%
copy_trade                      2    -95.5%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        75    -55.0%    -93.2%    60%
70-79     107    -44.7%    -73.6%    51%
60-69      62    -29.5%    -89.0%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1092     +0.0%    -11.0%    -47.5%    27%
<15%      282     +1.4%    -14.2%    -40.1%    32%
15-30%     45     -0.2%     -1.7%     +0.4%    31%
30%+       36     -0.7%     -1.1%     +0.8%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      954     +0.0%     -2.3%    -38.9%    25%
<20%      441     +2.8%    -60.9%    -91.4%    28%
20%+       60     -2.9%    -99.0%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1397     +0.2%     -7.4%    -41.6%    26%
20-40%     36     -2.6%    -99.0%    -99.1%    78%
40%+       22    -98.6%    -99.0%       -      77%
tokens analysed: 1283 | helius credits today: 8129/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  165    22%    -10.3%   -14.7%   -99.7%
   -6%     20%  165    23%    -10.6%   -14.9%   -99.7%
   -6%     30%  165    21%    -10.8%   -15.6%   -99.7%
  -10%     12%  165    25%    -10.4%   -17.5%   -99.7%
  -10%     20%  165    26%    -10.8%   -17.8%   -99.7%
  -10%     30%  165    24%    -10.8%   -18.6%   -99.7%
  -15%     12%  165    29%    -10.1%   -19.6%   -99.7%
  -15%     20%  165    32%    -10.6%   -20.7%   -99.7%
  -15%     30%  165    29%    -11.0%   -21.2%   -99.7%
  -25%     12%  165    33%    -12.1%   -18.6%   -99.7%
  -25%     20%  165    37%    -13.6%   -29.3%   -99.7%
  -25%     30%  165    34%    -14.2%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -10.1% per trade over n=165

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $275.49       $316.89       $496.05
return                        -44.9%        -36.6%         -0.8%
closed trades                    110            89             2
win rate                         21%           21%            0%
avg net / trade               -10.4%         -9.9%         -7.9%
expectancy $/trade            $-2.04        $-2.06        $-1.97
max drawdown                  -47.0%        -41.7%         -0.8%
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
signals skipped by the sizer/risk rules: already_traded_token 620, daily_loss_limit 331, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $316.89 (-36.6%) | cash $316.89 | open 0 | max drawdown -41.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 89 | win 19/89 (21%) | avg net -9.9% | realized $-183.11 | expectancy $-2.06/trade
exits: stop 69, trail 20
  (n=89 < 100: noise, not evidence)
last trades:
  UCASH        $17.17 -> $17.37 (+1.2%)  trail  0.8h
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 450, daily_loss_limit 240, setup_rejected:dumping_now 145, setup_rejected:sellers_dominate_now 142, setup_rejected:b_bundled 77, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:clustered_supply 38, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $496.05 (-0.8%) | cash $496.05 | open 0 | max drawdown -0.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 2 | win 0/2 (0%) | avg net -7.9% | realized $-3.95 | expectancy $-1.97/trade
exits: mirror_sell 2
  (n=2 < 100: noise, not evidence)
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 62, copy:no_price_at_delay 4

BOOK C per wallet  (watching 8 wallets, 685 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       2     0    0%    -7.9%    -3.95
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
