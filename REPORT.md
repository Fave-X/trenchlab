# TrenchLab report

Updated: 2026-11-16 04:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           75450
passed SCOUT         152
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           97

top kill reasons at first sighting (a pool can have several):
  too_young                    74159
  few_unique_buyers            71090
  liquidity_low                69517
  volume_below_liquidity       53344
  sells_dominate               19765
  wash_churn                   15520
  overheated                    6539
  missing                       2416
  too_old                        990
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4399 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   97    -4.7%    -9.9%   -43.9%   -88.8%    60%
SCOUT PASS, killed later     55    +4.3%    +4.2%   -50.5%   -52.9%    49%
KILLED (tracked)          10670    +0.0%   -55.0%   -79.0%    +0.1%    31%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      98    -94.5%    -68.9%    51%
too_old                        34     -0.6%     -0.4%     3%
wash_churn                     26     -1.1%    -71.8%    27%
liquidity_low                  20    -68.7%    -49.8%    45%
volume_below_liquidity          7     -2.8%    +15.3%    43%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        50    -55.3%    -93.4%    74%
70-79      57    -44.3%    -66.7%    51%
60-69      30    -35.2%    -79.9%    47%
<60        15    -31.3%    -52.9%    33%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      502     -0.2%    -13.1%    -34.1%    35%
<15%       99     +0.2%    -11.2%    -15.5%    29%
15-30%     11     -0.2%     -0.2%     +1.0%    36%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      482     -0.0%     -2.4%    -12.8%    28%
<20%      135     -5.9%    -57.8%    -92.3%    44%
20%+       17    +16.6%    -99.0%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      609     -0.2%     -6.4%    -17.1%    31%
20-40%     16     -6.5%    -99.0%    -99.1%    75%
40%+        9    +11.6%     +5.8%       -      56%
tokens analysed: 529 | helius credits today: 1257/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   97    25%     -9.4%   -17.1%   -99.7%
   -6%     20%   97    25%     -9.7%   -17.1%   -99.7%
   -6%     30%   97    25%     -8.2%   -17.1%   -99.7%
  -10%     12%   97    27%     -9.3%   -18.7%   -99.7%
  -10%     20%   97    26%     -9.9%   -19.1%   -99.7%
  -10%     30%   97    27%     -8.3%   -19.3%   -99.7%
  -15%     12%   97    29%     -9.0%   -19.9%   -99.7%
  -15%     20%   97    29%     -9.6%   -20.7%   -99.7%
  -15%     30%   97    30%     -8.1%   -21.0%   -99.7%
  -25%     12%   97    33%    -12.1%   -21.3%   -99.7%
  -25%     20%   97    33%    -14.5%   -30.1%   -99.7%
  -25%     30%   97    34%    -13.1%   -31.0%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -8.1% per trade over n=97
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $393.26       $401.69
return                        -21.3%        -19.7%
closed trades                     61            44
win rate                         25%           20%
avg net / trade                -7.4%         -9.5%
expectancy $/trade            $-1.75        $-2.23
max drawdown                  -24.5%        -26.1%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $393.26 (-21.3%) | cash $393.26 | open 0 | max drawdown -24.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 61 | win 15/61 (25%) | avg net -7.4% | realized $-106.74 | expectancy $-1.75/trade
exits: stop 43, trail 18
  (n=61 < 100: noise, not evidence)
last trades:
  worth        $20.84 -> $13.96 (-33.0%)  stop  0.2h
  Socks        $20.51 -> $18.26 (-11.0%)  stop  0.2h
  WANTED       $20.50 -> $21.41 (+4.4%)  trail  1.7h
  BUTTHOLE     $20.43 -> $17.04 (-16.6%)  stop  0.3h
  rockstar     $20.26 -> $17.49 (-13.7%)  stop  0.2h
  AI           $20.12 -> $15.62 (-22.4%)  stop  0.3h
  BAWSAQ       $19.90 -> $14.39 (-27.7%)  stop  0.2h
  WIGGLES      $19.62 -> $20.44 (+4.2%)  trail  0.3h
signals skipped by the sizer/risk rules: already_traded_token 361, daily_loss_limit 244, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $401.69 (-19.7%) | cash $401.69 | open 0 | max drawdown -26.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 44 | win 9/44 (20%) | avg net -9.5% | realized $-98.31 | expectancy $-2.23/trade
exits: stop 35, trail 9
  (n=44 < 100: noise, not evidence)
last trades:
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
  bill         $21.25 -> $15.00 (-29.4%)  stop  0.2h
  HYGG         $20.94 -> $24.47 (+16.9%)  trail  1.3h
  ニャジラ         $21.11 -> $13.78 (-34.7%)  stop  0.7h
  Socks        $20.75 -> $17.11 (-17.5%)  stop  0.5h
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
  rockstar     $20.24 -> $17.10 (-15.5%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 331, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 94, setup_rejected:volume_dried_up 38, setup_rejected:b_bundled 33, setup_rejected:top10_concentrated 29, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
