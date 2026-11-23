# TrenchLab report

Updated: 2026-11-23 05:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           126361
passed SCOUT         248
  killed by SCORE    35
  killed by AUDIT    59
FINAL PASS           154

top kill reasons at first sighting (a pool can have several):
  too_young                   124645
  few_unique_buyers           118935
  liquidity_low               117033
  volume_below_liquidity       89178
  sells_dominate               33414
  wash_churn                   26547
  overheated                   11361
  missing                       3381
  too_old                       1248
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 7538 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  154    -5.0%   -12.5%   -43.9%   -86.9%    57%
SCOUT PASS, killed later     94    +5.6%   +10.7%   -13.5%   -74.6%    49%
KILLED (tracked)          17460    +0.1%   -58.9%   -84.5%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     348    -93.8%    -68.9%    27%
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
70-79      95    -44.3%    -71.4%    51%
60-69      61    -34.0%    -93.0%    54%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      970     +0.0%    -10.9%    -46.0%    27%
<15%      210     +1.3%    -13.1%    -32.9%    34%
15-30%     43     -0.5%     -2.0%     +0.4%    33%
30%+       34     -0.6%     -0.7%     +1.9%    32%
bundled     n   +1h med   +4h med  +24h med   rug%
none      854     +0.0%     -2.5%    -31.6%    25%
<20%      349     +1.0%    -58.2%    -92.9%    29%
20%+       54     -0.4%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1204     +0.2%     -6.8%    -39.4%    26%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       19    -98.5%    -98.6%       -      79%
tokens analysed: 1095 | helius credits today: 2619/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  154    22%     -9.6%   -14.5%   -99.7%
   -6%     20%  154    23%     -9.9%   -14.9%   -99.7%
   -6%     30%  154    21%    -10.0%   -15.3%   -99.7%
  -10%     12%  154    25%     -9.6%   -17.3%   -99.7%
  -10%     20%  154    27%    -10.0%   -17.8%   -99.7%
  -10%     30%  154    25%     -9.9%   -18.6%   -99.7%
  -15%     12%  154    29%     -9.1%   -19.4%   -99.7%
  -15%     20%  154    32%     -9.6%   -20.4%   -99.7%
  -15%     30%  154    29%     -9.9%   -21.0%   -99.7%
  -25%     12%  154    33%    -11.3%   -17.4%   -99.7%
  -25%     20%  154    36%    -13.2%   -29.5%   -99.7%
  -25%     30%  154    33%    -13.7%   -30.7%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.1% per trade over n=154

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $300.49       $343.38
return                        -39.9%        -31.3%
closed trades                    102            81
win rate                         22%           22%
avg net / trade                -9.5%         -8.9%
expectancy $/trade            $-1.96        $-1.93
max drawdown                  -42.2%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $300.49 (-39.9%) | cash $300.49 | open 0 | max drawdown -42.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 102 | win 22/102 (22%) | avg net -9.5% | realized $-199.51 | expectancy $-1.96/trade
exits: stop 75, trail 26, dead_no_route 1
last trades:
  STREETS      $16.26 -> $19.94 (+22.7%)  trail  1.0h
  snowball     $16.45 -> $15.21 (-7.5%)  trail  0.3h
  UCASH        $16.39 -> $14.30 (-12.8%)  stop  0.7h
  MCAT         $16.28 -> $14.16 (-13.0%)  stop  0.2h
  MCAT         $16.18 -> $0.00 (-100.0%)  dead_no_route  1.8h
  OpenIndex    $15.37 -> $12.15 (-20.9%)  stop  0.3h
  COPIUM       $15.21 -> $13.38 (-12.0%)  stop  1.0h
  Fly          $15.11 -> $13.32 (-11.9%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 579, daily_loss_limit 322, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $343.38 (-31.3%) | cash $343.38 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 81 | win 18/81 (22%) | avg net -8.9% | realized $-156.62 | expectancy $-1.93/trade
exits: stop 62, trail 19
  (n=81 < 100: noise, not evidence)
last trades:
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
  MCAT         $17.32 -> $18.54 (+7.0%)  trail  3.5h
  cCAT         $17.38 -> $13.20 (-24.0%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 424, daily_loss_limit 239, setup_rejected:dumping_now 141, setup_rejected:sellers_dominate_now 138, setup_rejected:b_bundled 74, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:clustered_supply 30, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
