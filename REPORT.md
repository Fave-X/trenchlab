# TrenchLab report

Updated: 2026-11-17 00:41 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           81786
passed SCOUT         162
  killed by SCORE    21
  killed by AUDIT    35
FINAL PASS           106

top kill reasons at first sighting (a pool can have several):
  too_young                    80441
  few_unique_buyers            77046
  liquidity_low                75579
  volume_below_liquidity       57659
  sells_dominate               21469
  wash_churn                   16891
  overheated                    7126
  missing                       2486
  too_old                       1021
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4821 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  106    -3.4%   -11.7%   -45.2%   -88.5%    59%
SCOUT PASS, killed later     56    +4.3%    +4.4%   -50.5%   -52.9%    48%
KILLED (tracked)          11436    +0.0%   -55.7%   -79.2%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     108    -94.1%    -68.9%    49%
too_old                        37     -0.6%     -0.4%     5%
wash_churn                     29     -1.1%    -71.8%    28%
liquidity_low                  24    -68.7%    -49.8%    50%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        51    -58.0%    -93.6%    75%
70-79      60    -44.3%    -66.9%    50%
60-69      35    -45.2%    -60.0%    49%
<60        16    -31.3%    -52.9%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      532     -0.3%    -16.7%    -32.6%    34%
<15%      110     +0.4%    -11.2%    -13.9%    31%
15-30%     20     -1.4%     -0.2%     +1.0%    30%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      511     -0.2%     -2.8%    -12.8%    28%
<20%      154     -3.5%    -58.2%    -91.4%    42%
20%+       19     +9.3%    -99.0%       -      84%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      659     -0.3%     -7.5%    -16.6%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+       10    -43.5%     +5.8%       -      70%
tokens analysed: 571 | helius credits today: 189/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  106    26%     -8.7%   -14.7%   -99.7%
   -6%     20%  106    26%     -9.2%   -16.0%   -99.7%
   -6%     30%  106    25%     -9.0%   -17.3%   -99.7%
  -10%     12%  106    28%     -9.4%   -18.4%   -99.7%
  -10%     20%  106    27%    -10.2%   -18.9%   -99.7%
  -10%     30%  106    26%     -9.9%   -19.2%   -99.7%
  -15%     12%  106    30%    -10.0%   -19.6%   -99.7%
  -15%     20%  106    30%    -10.7%   -20.6%   -99.7%
  -15%     30%  106    29%    -10.7%   -21.1%   -99.7%
  -25%     12%  106    34%    -12.9%   -19.6%   -99.7%
  -25%     20%  106    34%    -15.4%   -30.0%   -99.7%
  -25%     30%  106    33%    -15.5%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.7% per trade over n=106

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $379.80       $398.53
return                        -24.0%        -20.3%
closed trades                     64            49
win rate                         23%           18%
avg net / trade                -9.1%        -10.2%
expectancy $/trade            $-2.07        $-2.33
max drawdown                  -29.3%        -29.0%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $379.80 (-24.0%) | cash $349.15 | open 1 | max drawdown -29.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 64 | win 15/64 (23%) | avg net -9.1% | realized $-132.47 | expectancy $-2.07/trade
exits: stop 46, trail 18
  (n=64 < 100: noise, not evidence)
open:
  BAWSAQ       cost $18.38  now $30.64 (+66.7%)  held 0.7h
last trades:
  BUTTHOLE     $20.43 -> $17.04 (-16.6%)  stop  0.3h
  rockstar     $20.26 -> $17.49 (-13.7%)  stop  0.2h
  AI           $20.12 -> $15.62 (-22.4%)  stop  0.3h
  BAWSAQ       $19.90 -> $14.39 (-27.7%)  stop  0.2h
  WIGGLES      $19.62 -> $20.44 (+4.2%)  trail  0.3h
  6STAR        $19.75 -> $16.35 (-17.2%)  stop  0.2h
  Marvin       $19.65 -> $16.98 (-13.6%)  stop  0.8h
  FiveM        $19.66 -> $0.01 (-100.0%)  stop  4.0h
signals skipped by the sizer/risk rules: already_traded_token 379, daily_loss_limit 251, cooldown_after_loss 12, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $398.53 (-20.3%) | cash $366.67 | open 1 | max drawdown -29.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 49 | win 9/49 (18%) | avg net -10.2% | realized $-114.03 | expectancy $-2.33/trade
exits: stop 40, trail 9
  (n=49 < 100: noise, not evidence)
open:
  BAWSAQ       cost $19.30  now $31.86 (+65.1%)  held 0.7h
last trades:
  Socks        $20.75 -> $17.11 (-17.5%)  stop  0.5h
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
  rockstar     $20.24 -> $17.10 (-15.5%)  stop  0.2h
  Marvin       $20.08 -> $17.44 (-13.1%)  stop  0.8h
  WIGGLES      $20.12 -> $16.41 (-18.4%)  stop  1.3h
  Anthropig    $19.77 -> $17.19 (-13.1%)  stop  1.5h
  Trader       $19.64 -> $14.98 (-23.7%)  stop  0.7h
  BAWSAQ       $19.64 -> $17.51 (-10.9%)  stop  1.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 364, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 96, setup_rejected:volume_dried_up 38, setup_rejected:b_bundled 33, setup_rejected:top10_concentrated 32, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
