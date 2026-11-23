# TrenchLab report

Updated: 2026-11-23 03:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           125520
passed SCOUT         246
  killed by SCORE    35
  killed by AUDIT    58
FINAL PASS           153

top kill reasons at first sighting (a pool can have several):
  too_young                   123809
  few_unique_buyers           118154
  liquidity_low               116273
  volume_below_liquidity       88568
  sells_dominate               33187
  wash_churn                   26383
  overheated                   11284
  missing                       3347
  too_old                       1245
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 7489 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  153    -5.0%   -13.0%   -43.9%   -86.9%    58%
SCOUT PASS, killed later     93    +5.4%   +11.1%   -13.5%   -74.6%    48%
KILLED (tracked)          17328    +0.1%   -59.1%   -84.5%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     341    -94.5%    -68.9%    27%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        49     -0.6%     -0.4%    10%
liquidity_low                  33    -69.9%    -49.8%    61%
overheated                     10    -12.8%    -56.0%    50%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        67    -51.8%    -93.3%    61%
70-79      94    -44.3%    -71.4%    50%
60-69      60    -34.6%    -93.0%    55%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      961     +0.0%    -10.9%    -46.0%    27%
<15%      205     +1.3%    -13.7%    -32.9%    35%
15-30%     41     -0.9%     -2.0%     +0.4%    32%
30%+       34     -0.6%     -0.7%     +1.9%    32%
bundled     n   +1h med   +4h med  +24h med   rug%
none      844     +0.0%     -2.5%    -31.6%    25%
<20%      343     +0.6%    -58.3%    -92.9%    29%
20%+       54     -0.4%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1187     +0.1%     -7.1%    -39.4%    26%
20-40%     35     -4.5%    -99.0%    -99.1%    77%
40%+       19    -98.5%    -98.6%       -      79%
tokens analysed: 1080 | helius credits today: 1360/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  152    22%     -9.6%   -14.7%   -99.7%
   -6%     20%  152    24%     -9.9%   -14.9%   -99.7%
   -6%     30%  152    22%     -9.8%   -15.7%   -99.7%
  -10%     12%  152    26%     -9.5%   -17.6%   -99.7%
  -10%     20%  152    27%     -9.9%   -18.0%   -99.7%
  -10%     30%  152    26%     -9.7%   -18.6%   -99.7%
  -15%     12%  152    30%     -9.1%   -19.4%   -99.7%
  -15%     20%  152    32%     -9.6%   -20.4%   -99.7%
  -15%     30%  152    30%     -9.6%   -21.0%   -99.7%
  -25%     12%  152    34%    -11.4%   -17.4%   -99.7%
  -25%     20%  152    37%    -13.2%   -29.7%   -99.7%
  -25%     30%  152    34%    -13.7%   -30.8%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.1% per trade over n=152

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $304.11       $345.93
return                        -39.2%        -30.8%
closed trades                    100            79
win rate                         22%           22%
avg net / trade                -9.4%         -8.9%
expectancy $/trade            $-1.96        $-1.94
max drawdown                  -41.5%        -37.3%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $304.11 (-39.2%) | cash $288.90 | open 1 | max drawdown -41.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 100 | win 22/100 (22%) | avg net -9.4% | realized $-195.89 | expectancy $-1.96/trade
exits: stop 73, trail 26, dead_no_route 1
open:
  COPIUM       cost $15.21  now $15.21 (+0.0%)  held 0.0h
last trades:
  HOUSE        $16.29 -> $14.03 (-13.9%)  stop  0.2h
  SIDOOR       $16.18 -> $17.90 (+10.6%)  trail  0.7h
  STREETS      $16.26 -> $19.94 (+22.7%)  trail  1.0h
  snowball     $16.45 -> $15.21 (-7.5%)  trail  0.3h
  UCASH        $16.39 -> $14.30 (-12.8%)  stop  0.7h
  MCAT         $16.28 -> $14.16 (-13.0%)  stop  0.2h
  MCAT         $16.18 -> $0.00 (-100.0%)  dead_no_route  1.8h
  OpenIndex    $15.37 -> $12.15 (-20.9%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 577, daily_loss_limit 322, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $345.93 (-30.8%) | cash $329.03 | open 1 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 79 | win 17/79 (22%) | avg net -8.9% | realized $-153.65 | expectancy $-1.94/trade
exits: stop 61, trail 18
  (n=79 < 100: noise, not evidence)
open:
  MCAT         cost $17.32  now $16.91 (-2.4%)  held 2.4h
last trades:
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 424, daily_loss_limit 239, setup_rejected:dumping_now 141, setup_rejected:sellers_dominate_now 134, setup_rejected:b_bundled 74, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:clustered_supply 30, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
