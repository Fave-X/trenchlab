# TrenchLab report

Updated: 2026-11-21 16:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           115270
passed SCOUT         220
  killed by SCORE    33
  killed by AUDIT    47
FINAL PASS           140

top kill reasons at first sighting (a pool can have several):
  too_young                   113640
  few_unique_buyers           108561
  liquidity_low               106764
  volume_below_liquidity       81283
  sells_dominate               30439
  wash_churn                   24311
  overheated                   10313
  missing                       3163
  too_old                       1195
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 6961 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  140    -5.4%   -12.0%   -45.2%   -88.1%    59%
SCOUT PASS, killed later     80    +4.3%    +4.2%   -30.1%   -74.6%    51%
KILLED (tracked)          15848    +0.0%   -62.1%   -84.9%    -0.1%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     276    -95.0%    -68.9%    30%
too_old                        46     -0.6%     -0.4%    11%
wash_churn                     43    -23.3%    -85.6%    30%
liquidity_low                  30    -69.3%    -49.8%    60%
overheated                      9     -3.6%    -56.0%    44%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        59    -55.3%    -93.4%    68%
70-79      83    -52.3%    -72.2%    53%
60-69      53    -34.6%    -92.5%    55%
<60        25     -7.4%    -63.7%    44%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      838     -0.2%    -12.0%    -44.0%    29%
<15%      159     +0.6%    -13.7%    -41.3%    37%
15-30%     36     -1.4%     -2.0%     +0.4%    33%
30%+       32     -0.5%     -0.7%     +1.9%    28%
bundled     n   +1h med   +4h med  +24h med   rug%
none      737     -0.0%     -2.7%    -31.1%    26%
<20%      280     -3.9%    -58.3%    -92.9%    31%
20%+       48     -0.5%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1015     -0.1%     -7.4%    -37.0%    28%
20-40%     32     -4.6%    -99.0%    -99.1%    78%
40%+       18    -97.5%    -98.6%       -      78%
tokens analysed: 916 | helius credits today: 4852/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  140    21%    -10.0%   -15.0%   -99.7%
   -6%     20%  140    23%    -10.3%   -15.5%   -99.7%
   -6%     30%  140    21%    -10.3%   -17.1%   -99.7%
  -10%     12%  140    25%     -9.9%   -18.6%   -99.7%
  -10%     20%  140    26%    -10.3%   -18.7%   -99.7%
  -10%     30%  140    25%     -9.9%   -19.1%   -99.7%
  -15%     12%  140    29%     -9.6%   -19.8%   -99.7%
  -15%     20%  140    31%    -10.0%   -20.4%   -99.7%
  -15%     30%  140    29%     -9.9%   -21.0%   -99.7%
  -25%     12%  140    32%    -12.0%   -24.6%   -99.7%
  -25%     20%  140    36%    -13.8%   -29.9%   -99.7%
  -25%     30%  140    34%    -13.9%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.6% per trade over n=140

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $329.30       $352.04
return                        -34.1%        -29.6%
closed trades                     91            76
win rate                         22%           22%
avg net / trade                -8.7%         -8.8%
expectancy $/trade            $-1.88        $-1.95
max drawdown                  -36.6%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $329.30 (-34.1%) | cash $329.30 | open 0 | max drawdown -36.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 91 | win 20/91 (22%) | avg net -8.7% | realized $-170.70 | expectancy $-1.88/trade
exits: stop 68, trail 23
  (n=91 < 100: noise, not evidence)
last trades:
  AI           $18.04 -> $10.08 (-44.1%)  stop  0.2h
  iAgent       $18.04 -> $16.18 (-10.3%)  stop  0.5h
  RUGGED       $17.54 -> $10.00 (-43.0%)  stop  0.5h
  AMC          $17.17 -> $13.19 (-23.2%)  stop  0.2h
  RUDY         $16.97 -> $15.02 (-11.5%)  stop  0.2h
  Trader       $16.87 -> $13.30 (-21.2%)  stop  0.2h
  PUNANI       $16.69 -> $14.71 (-11.9%)  stop  0.3h
  XV           $16.69 -> $14.12 (-15.4%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 515, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $352.04 (-29.6%) | cash $352.04 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 76 | win 17/76 (22%) | avg net -8.8% | realized $-147.96 | expectancy $-1.95/trade
exits: stop 58, trail 18
  (n=76 < 100: noise, not evidence)
last trades:
  CATMARIO     $17.21 -> $13.84 (-19.6%)  stop  0.5h
  HNYDRIP      $17.12 -> $38.11 (+122.6%)  trail  0.7h
  AMC          $18.09 -> $15.90 (-12.1%)  stop  0.2h
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:dumping_now 136, setup_rejected:sellers_dominate_now 133, setup_rejected:b_bundled 62, setup_rejected:volume_dried_up 47, setup_rejected:operator_cluster 36, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 23, setup_rejected:lp_not_locked 22, setup_rejected:clustered_supply 13, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
