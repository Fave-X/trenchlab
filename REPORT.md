# TrenchLab report

Updated: 2026-11-17 03:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           82634
passed SCOUT         162
  killed by SCORE    21
  killed by AUDIT    35
FINAL PASS           106

top kill reasons at first sighting (a pool can have several):
  too_young                    81284
  few_unique_buyers            77846
  liquidity_low                76365
  volume_below_liquidity       58244
  sells_dominate               21683
  wash_churn                   17082
  overheated                    7197
  missing                       2515
  too_old                       1023
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4904 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  106    -3.4%   -11.5%   -45.0%   -88.1%    59%
SCOUT PASS, killed later     56    +4.3%    +4.4%   -49.0%   -52.9%    48%
KILLED (tracked)          11550    +0.0%   -56.1%   -79.3%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     111    -94.8%    -68.9%    48%
too_old                        37     -0.7%     -0.4%     5%
wash_churn                     30     -1.1%    -71.8%    30%
liquidity_low                  24    -68.7%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        51    -58.0%    -93.6%    75%
70-79      60    -44.3%    -67.3%    50%
60-69      35    -42.4%    -60.0%    49%
<60        16    -29.7%    -52.9%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      539     -0.2%    -16.7%    -33.1%    34%
<15%      111     +0.4%    -11.2%    -13.9%    31%
15-30%     20     -1.4%     -2.9%     +1.0%    30%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      517     -0.2%     -3.0%    -12.9%    27%
<20%      155     -3.5%    -58.2%    -91.4%    42%
20%+       20     +8.6%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      667     -0.2%     -8.4%    -17.1%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+       10    -43.5%    -46.3%       -      70%
tokens analysed: 579 | helius credits today: 857/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  106    26%     -8.5%   -14.7%   -99.7%
   -6%     20%  106    26%     -8.9%   -16.0%   -99.7%
   -6%     30%  106    25%     -8.7%   -17.3%   -99.7%
  -10%     12%  106    28%     -9.2%   -18.4%   -99.7%
  -10%     20%  106    27%    -10.0%   -18.9%   -99.7%
  -10%     30%  106    26%     -9.7%   -19.2%   -99.7%
  -15%     12%  106    30%     -9.7%   -19.6%   -99.7%
  -15%     20%  106    30%    -10.5%   -20.6%   -99.7%
  -15%     30%  106    29%    -10.4%   -21.1%   -99.7%
  -25%     12%  106    34%    -12.6%   -19.6%   -99.7%
  -25%     20%  106    34%    -15.1%   -30.0%   -99.7%
  -25%     30%  106    33%    -15.2%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.5% per trade over n=106

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $384.79       $404.23
return                        -23.0%        -19.2%
closed trades                     65            50
win rate                         25%           20%
avg net / trade                -7.5%         -8.1%
expectancy $/trade            $-1.77        $-1.93
max drawdown                  -29.3%        -29.0%
open now                           0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $384.79 (-23.0%) | cash $384.79 | open 0 | max drawdown -29.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 65 | win 16/65 (25%) | avg net -7.5% | realized $-115.21 | expectancy $-1.77/trade
exits: stop 46, trail 19
  (n=65 < 100: noise, not evidence)
last trades:
  rockstar     $20.26 -> $17.49 (-13.7%)  stop  0.2h
  AI           $20.12 -> $15.62 (-22.4%)  stop  0.3h
  BAWSAQ       $19.90 -> $14.39 (-27.7%)  stop  0.2h
  WIGGLES      $19.62 -> $20.44 (+4.2%)  trail  0.3h
  6STAR        $19.75 -> $16.35 (-17.2%)  stop  0.2h
  Marvin       $19.65 -> $16.98 (-13.6%)  stop  0.8h
  FiveM        $19.66 -> $0.01 (-100.0%)  stop  4.0h
  BAWSAQ       $18.38 -> $35.64 (+93.9%)  trail  1.0h
signals skipped by the sizer/risk rules: already_traded_token 385, daily_loss_limit 251, cooldown_after_loss 12, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $404.23 (-19.2%) | cash $383.53 | open 1 | max drawdown -29.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 50 | win 10/50 (20%) | avg net -8.1% | realized $-96.28 | expectancy $-1.93/trade
exits: stop 40, trail 10
  (n=50 < 100: noise, not evidence)
open:
  LEOSTAR      cost $20.19  now $20.70 (+2.5%)  held 0.9h
last trades:
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
  rockstar     $20.24 -> $17.10 (-15.5%)  stop  0.2h
  Marvin       $20.08 -> $17.44 (-13.1%)  stop  0.8h
  WIGGLES      $20.12 -> $16.41 (-18.4%)  stop  1.3h
  Anthropig    $19.77 -> $17.19 (-13.1%)  stop  1.5h
  Trader       $19.64 -> $14.98 (-23.7%)  stop  0.7h
  BAWSAQ       $19.64 -> $17.51 (-10.9%)  stop  1.2h
  BAWSAQ       $19.30 -> $37.05 (+92.0%)  trail  1.0h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 364, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 96, setup_rejected:volume_dried_up 39, setup_rejected:top10_concentrated 33, setup_rejected:b_bundled 33, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
