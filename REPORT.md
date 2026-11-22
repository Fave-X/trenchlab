# TrenchLab report

Updated: 2026-11-22 20:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           123647
passed SCOUT         242
  killed by SCORE    34
  killed by AUDIT    57
FINAL PASS           151

top kill reasons at first sighting (a pool can have several):
  too_young                   121950
  few_unique_buyers           116389
  liquidity_low               114523
  volume_below_liquidity       87215
  sells_dominate               32656
  wash_churn                   25993
  overheated                   11104
  missing                       3321
  too_old                       1237
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 7407 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  151    -5.0%   -13.0%   -44.0%   -86.9%    58%
SCOUT PASS, killed later     91    +5.4%   +11.1%   -23.8%   -74.6%    48%
KILLED (tracked)          17077    +0.1%   -59.5%   -84.6%    +0.4%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     333    -95.0%    -68.9%    27%
wash_churn                     54    -23.3%    -85.6%    26%
too_old                        47     -0.6%     -0.4%    11%
liquidity_low                  33    -69.9%    -49.8%    61%
overheated                     10     -3.6%    -56.0%    40%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        65    -54.0%    -93.3%    62%
70-79      93    -44.7%    -71.8%    49%
60-69      59    -34.6%    -92.5%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      938     +0.0%    -11.9%    -45.5%    27%
<15%      196     +1.0%    -14.2%    -32.9%    36%
15-30%     38     -1.2%     -2.4%     +0.4%    34%
30%+       34     -0.5%     -0.7%     +1.9%    32%
bundled     n   +1h med   +4h med  +24h med   rug%
none      818     +0.0%     -2.5%    -31.6%    25%
<20%      335     +0.4%    -59.6%    -93.0%    30%
20%+       53     -0.4%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1153     +0.0%     -7.5%    -39.2%    27%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       19    -97.5%    -98.6%       -      79%
tokens analysed: 1050 | helius credits today: 8331/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  150    22%     -9.5%   -14.7%   -99.7%
   -6%     20%  150    23%     -9.9%   -14.9%   -99.7%
   -6%     30%  150    21%     -9.8%   -15.7%   -99.7%
  -10%     12%  150    25%     -9.5%   -17.6%   -99.7%
  -10%     20%  150    27%     -9.9%   -18.0%   -99.7%
  -10%     30%  150    25%     -9.7%   -18.6%   -99.7%
  -15%     12%  150    29%     -9.0%   -19.4%   -99.7%
  -15%     20%  150    32%     -9.5%   -20.4%   -99.7%
  -15%     30%  150    30%     -9.6%   -21.0%   -99.7%
  -25%     12%  150    33%    -11.3%   -17.4%   -99.7%
  -25%     20%  150    37%    -13.2%   -29.7%   -99.7%
  -25%     30%  150    34%    -13.7%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.0% per trade over n=150

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $307.32       $346.35
return                        -38.5%        -30.7%
closed trades                     99            79
win rate                         22%           22%
avg net / trade                -9.3%         -8.9%
expectancy $/trade            $-1.95        $-1.94
max drawdown                  -40.9%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $307.32 (-38.5%) | cash $307.32 | open 0 | max drawdown -40.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 99 | win 22/99 (22%) | avg net -9.3% | realized $-192.68 | expectancy $-1.95/trade
exits: stop 72, trail 26, dead_no_route 1
  (n=99 < 100: noise, not evidence)
last trades:
  Bigfoot      $16.46 -> $12.98 (-21.2%)  stop  0.2h
  HOUSE        $16.29 -> $14.03 (-13.9%)  stop  0.2h
  SIDOOR       $16.18 -> $17.90 (+10.6%)  trail  0.7h
  STREETS      $16.26 -> $19.94 (+22.7%)  trail  1.0h
  snowball     $16.45 -> $15.21 (-7.5%)  trail  0.3h
  UCASH        $16.39 -> $14.30 (-12.8%)  stop  0.7h
  MCAT         $16.28 -> $14.16 (-13.0%)  stop  0.2h
  MCAT         $16.18 -> $0.00 (-100.0%)  dead_no_route  1.8h
signals skipped by the sizer/risk rules: already_traded_token 566, daily_loss_limit 313, cooldown_after_loss 18, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 424, daily_loss_limit 239, setup_rejected:dumping_now 141, setup_rejected:sellers_dominate_now 134, setup_rejected:b_bundled 74, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:clustered_supply 30, setup_rejected:bundled_buys 23, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
