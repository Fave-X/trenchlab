# TrenchLab report

Updated: 2026-11-19 00:21 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           95982
passed SCOUT         186
  killed by SCORE    26
  killed by AUDIT    40
FINAL PASS           120

top kill reasons at first sighting (a pool can have several):
  too_young                    94517
  few_unique_buyers            90579
  liquidity_low                88953
  volume_below_liquidity       67855
  sells_dominate               25276
  wash_churn                   19805
  overheated                    8388
  missing                       2737
  too_old                       1098
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5705 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  120    -3.3%    -7.8%   -44.7%   -86.4%    57%
SCOUT PASS, killed later     66    +4.7%    +3.9%   -32.2%   -63.7%    47%
KILLED (tracked)          13091    +0.0%   -59.6%   -82.6%    +0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     146    -94.1%    -68.9%    45%
too_old                        39     -0.6%     -0.4%     8%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  26    -72.2%    -49.8%    58%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    74%
70-79      70    -39.9%    -67.4%    49%
60-69      44    -37.4%    -75.3%    45%
<60        19    -31.3%    -63.7%    37%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      631     -0.3%    -17.8%    -41.6%    34%
<15%      119     +0.3%    -11.2%    -24.0%    34%
15-30%     24     -0.7%     -1.3%     +1.0%    25%
30%+       23     -0.4%     -0.6%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      594     -0.2%     -3.0%    -16.6%    28%
<20%      176     -6.9%    -60.8%    -93.7%    42%
20%+       27     +9.3%    -98.8%       -      74%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      762     -0.3%     -8.8%    -31.1%    31%
20-40%     24     -0.4%    -98.9%    -99.1%    62%
40%+       11    -96.5%    -96.5%       -      73%
tokens analysed: 670 | helius credits today: 132/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  120    25%     -8.1%   -14.2%   -99.7%
   -6%     20%  120    26%     -8.5%   -14.9%   -99.7%
   -6%     30%  120    24%     -8.3%   -17.1%   -99.7%
  -10%     12%  120    28%     -8.4%   -18.0%   -99.7%
  -10%     20%  120    28%     -8.9%   -18.6%   -99.7%
  -10%     30%  120    28%     -8.7%   -18.9%   -99.7%
  -15%     12%  120    30%     -8.6%   -19.4%   -99.7%
  -15%     20%  120    32%     -9.2%   -20.4%   -99.7%
  -15%     30%  120    31%     -9.2%   -21.0%   -99.7%
  -25%     12%  120    33%    -11.3%   -17.4%   -99.7%
  -25%     20%  120    36%    -13.6%   -29.9%   -99.7%
  -25%     30%  120    35%    -13.6%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.1% per trade over n=120

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $375.50       $372.55
return                        -24.9%        -25.5%
closed trades                     77            59
win rate                         25%           22%
avg net / trade                -6.9%         -9.5%
expectancy $/trade            $-1.62        $-2.16
max drawdown                  -32.0%        -31.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $375.50 (-24.9%) | cash $375.50 | open 0 | max drawdown -32.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 77 | win 19/77 (25%) | avg net -6.9% | realized $-124.50 | expectancy $-1.62/trade
exits: stop 55, trail 22
  (n=77 < 100: noise, not evidence)
last trades:
  GEKKO        $18.30 -> $16.05 (-12.3%)  stop  0.2h
  KATIA        $18.19 -> $13.69 (-24.8%)  stop  0.2h
  NVIDIANS     $17.96 -> $15.67 (-12.7%)  stop  0.1h
  ANT          $17.85 -> $15.87 (-11.1%)  stop  0.2h
  SHIT         $17.85 -> $19.44 (+8.9%)  trail  3.7h
  Apocrycoin   $17.83 -> $39.70 (+122.7%)  trail  0.7h
  DCTY         $18.92 -> $15.61 (-17.5%)  stop  0.3h
  DCTY         $18.92 -> $19.28 (+1.9%)  trail  1.3h
signals skipped by the sizer/risk rules: already_traded_token 446, daily_loss_limit 251, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $372.55 (-25.5%) | cash $372.55 | open 0 | max drawdown -31.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 59 | win 13/59 (22%) | avg net -9.5% | realized $-127.45 | expectancy $-2.16/trade
exits: stop 46, trail 13
  (n=59 < 100: noise, not evidence)
last trades:
  bul          $20.07 -> $27.86 (+38.8%)  trail  1.5h
  KATIA        $20.67 -> $21.60 (+4.5%)  trail  1.0h
  JVOLT        $20.50 -> $0.07 (-99.7%)  stop  0.2h
  JALU         $19.48 -> $17.45 (-10.4%)  stop  0.8h
  NVIDIANS     $19.38 -> $12.07 (-37.7%)  stop  0.3h
  KATIA        $19.01 -> $20.77 (+9.3%)  trail  1.8h
  ANT          $19.10 -> $16.29 (-14.7%)  stop  0.8h
  Apocrycoin   $18.96 -> $12.29 (-35.2%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 224, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 114, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 22, setup_rejected:operator_cluster 21, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 12, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
