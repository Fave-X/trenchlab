# TrenchLab report

Updated: 2026-11-22 16:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           122476
passed SCOUT         239
  killed by SCORE    34
  killed by AUDIT    57
FINAL PASS           148

top kill reasons at first sighting (a pool can have several):
  too_young                   120785
  few_unique_buyers           115284
  liquidity_low               113434
  volume_below_liquidity       86348
  sells_dominate               32339
  wash_churn                   25804
  overheated                   11004
  missing                       3304
  too_old                       1233
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 7355 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  148    -5.0%   -12.5%   -43.9%   -87.5%    58%
SCOUT PASS, killed later     91    +5.4%   +11.1%   -23.8%   -74.6%    48%
KILLED (tracked)          16929    +0.1%   -59.6%   -84.6%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     320    -95.0%    -68.9%    28%
wash_churn                     53    -23.3%    -85.6%    26%
too_old                        46     -0.6%     -0.4%    11%
liquidity_low                  33    -69.9%    -49.8%    61%
overheated                      9     -3.6%    -56.0%    44%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        64    -55.0%    -93.3%    62%
70-79      92    -44.7%    -71.8%    49%
60-69      58    -34.6%    -93.0%    57%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      916     -0.0%    -12.0%    -45.5%    28%
<15%      193     +0.9%    -13.1%    -32.7%    35%
15-30%     38     -1.2%     -2.4%     +0.4%    34%
30%+       33     -0.5%     -0.7%     +1.9%    30%
bundled     n   +1h med   +4h med  +24h med   rug%
none      797     -0.0%     -2.7%    -31.6%    26%
<20%      330     -0.0%    -58.4%    -92.9%    29%
20%+       53     +4.3%    -98.9%       -      79%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1128     +0.0%     -7.4%    -38.9%    27%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       18    -97.5%    -98.6%       -      78%
tokens analysed: 1025 | helius credits today: 6164/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  148    22%     -9.5%   -14.5%   -99.7%
   -6%     20%  148    24%     -9.9%   -14.9%   -99.7%
   -6%     30%  148    22%     -9.8%   -16.1%   -99.7%
  -10%     12%  148    26%     -9.5%   -17.8%   -99.7%
  -10%     20%  148    27%     -9.9%   -18.4%   -99.7%
  -10%     30%  148    26%     -9.7%   -18.7%   -99.7%
  -15%     12%  148    30%     -9.0%   -19.6%   -99.7%
  -15%     20%  148    32%     -9.4%   -20.3%   -99.7%
  -15%     30%  148    30%     -9.5%   -21.0%   -99.7%
  -25%     12%  148    34%    -11.2%   -18.2%   -99.7%
  -25%     20%  148    37%    -12.9%   -29.7%   -99.7%
  -25%     30%  148    35%    -13.2%   -30.8%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.0% per trade over n=148

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $328.00       $346.35
return                        -34.4%        -30.7%
closed trades                     98            79
win rate                         22%           22%
avg net / trade                -8.4%         -8.9%
expectancy $/trade            $-1.80        $-1.94
max drawdown                  -37.7%        -37.3%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $328.00 (-34.4%) | cash $307.32 | open 1 | max drawdown -37.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 98 | win 22/98 (22%) | avg net -8.4% | realized $-176.50 | expectancy $-1.80/trade
exits: stop 72, trail 26
  (n=98 < 100: noise, not evidence)
open:
  MCAT         cost $16.18  now $20.67 (+27.8%)  held 0.5h
last trades:
  XV           $16.69 -> $14.12 (-15.4%)  stop  0.2h
  Bigfoot      $16.46 -> $12.98 (-21.2%)  stop  0.2h
  HOUSE        $16.29 -> $14.03 (-13.9%)  stop  0.2h
  SIDOOR       $16.18 -> $17.90 (+10.6%)  trail  0.7h
  STREETS      $16.26 -> $19.94 (+22.7%)  trail  1.0h
  snowball     $16.45 -> $15.21 (-7.5%)  trail  0.3h
  UCASH        $16.39 -> $14.30 (-12.8%)  stop  0.7h
  MCAT         $16.28 -> $14.16 (-13.0%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 546, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $346.35 (-30.7%) | cash $346.35 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 79 | win 17/79 (22%) | avg net -8.9% | realized $-153.65 | expectancy $-1.94/trade
exits: stop 61, trail 18
  (n=79 < 100: noise, not evidence)
last trades:
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 424, daily_loss_limit 239, setup_rejected:dumping_now 140, setup_rejected:sellers_dominate_now 134, setup_rejected:b_bundled 69, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:clustered_supply 30, setup_rejected:bundled_buys 23, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
