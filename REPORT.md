# TrenchLab report

Updated: 2026-11-25 03:45 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           140222
passed SCOUT         275
  killed by SCORE    38
  killed by AUDIT    70
FINAL PASS           167

top kill reasons at first sighting (a pool can have several):
  too_young                   138371
  few_unique_buyers           131822
  liquidity_low               129730
  volume_below_liquidity       98735
  sells_dominate               37456
  wash_churn                   29254
  overheated                   12736
  missing                       3838
  too_old                       1358
  rc_danger                       21

OUTCOMES (median price change from first sighting / first pass; 8472 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  167    -5.0%   -14.1%   -43.9%   -83.7%    57%
SCOUT PASS, killed later    108    +5.6%    +8.4%    -7.4%   -74.6%    47%
KILLED (tracked)          19381    +0.1%   -60.4%   -85.5%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     458    -90.6%    -68.9%    24%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          8     +1.2%    +30.3%    38%
sells_dominate                  3    -75.0%       -      67%
copy_trade                      3    -96.3%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        76    -55.0%    -93.2%    59%
70-79     110    -44.3%    -72.2%    50%
60-69      64    -29.5%    -86.0%    55%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1108     +0.0%    -10.9%    -46.0%    27%
<15%      291     +2.1%    -13.7%    -40.1%    31%
15-30%     46     -0.1%     -1.7%     +0.4%    30%
30%+       36     -0.7%     -1.1%     +0.8%    36%
bundled     n   +1h med   +4h med  +24h med   rug%
none      967     +0.0%     -2.2%    -35.1%    25%
<20%      453     +3.1%    -60.7%    -91.4%    27%
20%+       61     -0.7%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1421     +0.3%     -7.2%    -40.1%    26%
20-40%     37     -0.7%    -99.0%    -99.1%    76%
40%+       23    -98.5%    -99.0%       -      74%
tokens analysed: 1308 | helius credits today: 1263/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  167    22%    -10.1%   -14.7%   -99.7%
   -6%     20%  167    23%    -10.4%   -14.9%   -99.7%
   -6%     30%  167    21%    -10.6%   -15.6%   -99.7%
  -10%     12%  167    25%    -10.2%   -17.5%   -99.7%
  -10%     20%  167    26%    -10.5%   -17.8%   -99.7%
  -10%     30%  167    25%    -10.6%   -18.6%   -99.7%
  -15%     12%  167    29%     -9.9%   -19.6%   -99.7%
  -15%     20%  167    32%    -10.4%   -20.7%   -99.7%
  -15%     30%  167    29%    -10.7%   -21.2%   -99.7%
  -25%     12%  167    34%    -11.8%   -17.8%   -99.7%
  -25%     20%  167    37%    -13.4%   -29.2%   -99.7%
  -25%     30%  167    34%    -13.9%   -30.8%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.9% per trade over n=167

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $278.25       $312.26       $503.51
return                        -44.4%        -37.5%         +0.7%
closed trades                    111            90             3
win rate                         21%           21%           33%
avg net / trade               -10.5%        -10.1%         +1.1%
expectancy $/trade            $-2.05        $-2.09        $+0.26
max drawdown                  -47.4%        -42.6%         -0.8%
open now                           1             1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $278.25 (-44.4%) | cash $258.91 | open 1 | max drawdown -47.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 111 | win 23/111 (21%) | avg net -10.5% | realized $-227.32 | expectancy $-2.05/trade
exits: stop 82, trail 28, dead_no_route 1
open:
  4CHAN        cost $13.77  now $19.33 (+40.4%)  held 0.4h
last trades:
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
  ChristmASS   $15.10 -> $9.98 (-33.9%)  stop  0.2h
  PONK         $14.84 -> $12.70 (-14.4%)  stop  0.2h
  JIMMY        $14.73 -> $12.48 (-15.3%)  stop  0.3h
  Jesus        $14.62 -> $4.59 (-68.6%)  stop  0.2h
  Scamsem      $14.12 -> $12.59 (-10.9%)  stop  0.2h
  DUVAL        $14.04 -> $8.66 (-38.3%)  stop  0.2h
  BOOBS        $13.77 -> $10.97 (-20.4%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 621, daily_loss_limit 331, cooldown_after_loss 20, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $312.26 (-37.5%) | cash $296.39 | open 1 | max drawdown -42.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 90 | win 19/90 (21%) | avg net -10.1% | realized $-187.74 | expectancy $-2.09/trade
exits: stop 70, trail 20
  (n=90 < 100: noise, not evidence)
open:
  PERRO        cost $15.87  now $15.87 (+0.0%)  held 0.1h
last trades:
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
  JENSEN       $16.71 -> $12.63 (-24.4%)  stop  0.7h
  JIMMY        $16.50 -> $14.30 (-13.3%)  stop  0.3h
  Scamsem      $16.39 -> $11.86 (-27.7%)  stop  0.7h
  GROKIA       $16.17 -> $13.16 (-18.6%)  stop  0.7h
  Holders      $16.02 -> $12.58 (-21.4%)  stop  0.2h
  ChristmASS   $15.84 -> $11.21 (-29.2%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 450, daily_loss_limit 240, setup_rejected:dumping_now 147, setup_rejected:sellers_dominate_now 143, setup_rejected:b_bundled 77, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 43, setup_rejected:lp_not_locked 39, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Low Liquidity 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $503.51 (+0.7%) | cash $475.75 | open 1 | max drawdown -0.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 1/3 (33%) | avg net +1.1% | realized $+0.79 | expectancy $+0.26/trade
exits: mirror_sell 3
  (n=3 < 100: noise, not evidence)
open:
  JENSEN       cost $25.04  now $27.76 (+10.8%)  held 0.3h
last trades:
  BLACKBALLED  $25.00 -> $21.48 (-14.1%)  mirror_sell  0.0h
  DCTY         $24.82 -> $24.39 (-1.7%)  mirror_sell  0.0h
  BEAST        $24.80 -> $29.54 (+19.1%)  mirror_sell  0.2h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 147, copy:no_price_at_delay 9

BOOK C per wallet  (watching 8 wallets, 1183 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
EDBMUo…Zfj7   t2-GTAVI/XV-a       3     1   33%    +1.1%    +0.79
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
