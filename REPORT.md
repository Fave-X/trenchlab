# TrenchLab report

Updated: 2026-11-16 07:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           76553
passed SCOUT         155
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           100

top kill reasons at first sighting (a pool can have several):
  too_young                    75249
  few_unique_buyers            72103
  liquidity_low                70571
  volume_below_liquidity       54085
  sells_dominate               20061
  wash_churn                   15759
  overheated                    6627
  missing                       2418
  too_old                        995
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4472 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  100    -4.3%    -9.9%   -44.0%   -88.8%    59%
SCOUT PASS, killed later     55    +4.3%    +4.2%   -50.5%   -52.9%    49%
KILLED (tracked)          10846    +0.0%   -55.1%   -78.1%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     104    -94.5%    -68.9%    48%
too_old                        34     -0.6%     -0.4%     6%
wash_churn                     28     -1.2%    -71.8%    29%
liquidity_low                  21    -68.7%    -49.8%    43%
volume_below_liquidity          7     -2.8%    +15.3%    43%
overheated                      6     -3.6%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        50    -55.6%    -93.4%    74%
70-79      59    -44.3%    -66.7%    51%
60-69      31    -35.2%    -79.9%    45%
<60        15    -31.3%    -52.9%    33%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      512     -0.2%    -13.5%    -34.1%    35%
<15%      104     +0.2%    -11.2%    -12.4%    29%
15-30%     11     -0.2%     -0.2%     +1.0%    36%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      487     -0.0%     -2.7%    -12.6%    28%
<20%      144     -4.7%    -57.8%    -92.3%    42%
20%+       18    +16.6%    -99.0%       -      78%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      625     -0.2%     -7.2%    -16.6%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+        9    +11.6%     +5.8%       -      56%
tokens analysed: 543 | helius credits today: 2377/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  100    26%     -9.0%   -16.0%   -99.7%
   -6%     20%  100    26%     -9.2%   -16.0%   -99.7%
   -6%     30%  100    26%     -7.6%   -17.1%   -99.7%
  -10%     12%  100    28%     -8.8%   -18.4%   -99.7%
  -10%     20%  100    27%     -9.4%   -18.6%   -99.7%
  -10%     30%  100    28%     -7.7%   -18.9%   -99.7%
  -15%     12%  100    30%     -9.4%   -19.8%   -99.7%
  -15%     20%  100    30%    -10.0%   -20.6%   -99.7%
  -15%     30%  100    31%     -8.4%   -21.0%   -99.7%
  -25%     12%  100    34%    -12.4%   -19.6%   -99.7%
  -25%     20%  100    34%    -14.7%   -30.0%   -99.7%
  -25%     30%  100    35%    -13.2%   -31.0%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -7.6% per trade over n=100

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $393.52       $401.69
return                        -21.3%        -19.7%
closed trades                     62            44
win rate                         24%           20%
avg net / trade                -7.5%         -9.5%
expectancy $/trade            $-1.78        $-2.23
max drawdown                  -24.8%        -26.1%
open now                           2             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $393.52 (-21.3%) | cash $350.55 | open 2 | max drawdown -24.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 62 | win 15/62 (24%) | avg net -7.5% | realized $-110.14 | expectancy $-1.78/trade
exits: stop 44, trail 18
  (n=62 < 100: noise, not evidence)
open:
  FiveM        cost $19.66  now $23.33 (+18.7%)  held 1.9h
  Marvin       cost $19.65  now $19.65 (+0.0%)  held 0.0h
last trades:
  Socks        $20.51 -> $18.26 (-11.0%)  stop  0.2h
  WANTED       $20.50 -> $21.41 (+4.4%)  trail  1.7h
  BUTTHOLE     $20.43 -> $17.04 (-16.6%)  stop  0.3h
  rockstar     $20.26 -> $17.49 (-13.7%)  stop  0.2h
  AI           $20.12 -> $15.62 (-22.4%)  stop  0.3h
  BAWSAQ       $19.90 -> $14.39 (-27.7%)  stop  0.2h
  WIGGLES      $19.62 -> $20.44 (+4.2%)  trail  0.3h
  6STAR        $19.75 -> $16.35 (-17.2%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 365, daily_loss_limit 244, cooldown_after_loss 12, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $401.69 (-19.7%) | cash $381.61 | open 1 | max drawdown -26.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 44 | win 9/44 (20%) | avg net -9.5% | realized $-98.31 | expectancy $-2.23/trade
exits: stop 35, trail 9
  (n=44 < 100: noise, not evidence)
open:
  Marvin       cost $20.08  now $20.08 (+0.0%)  held 0.0h
last trades:
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
  bill         $21.25 -> $15.00 (-29.4%)  stop  0.2h
  HYGG         $20.94 -> $24.47 (+16.9%)  trail  1.3h
  ニャジラ         $21.11 -> $13.78 (-34.7%)  stop  0.7h
  Socks        $20.75 -> $17.11 (-17.5%)  stop  0.5h
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
  rockstar     $20.24 -> $17.10 (-15.5%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 334, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 94, setup_rejected:volume_dried_up 38, setup_rejected:b_bundled 33, setup_rejected:top10_concentrated 29, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
