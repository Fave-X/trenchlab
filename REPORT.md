# TrenchLab report

Updated: 2026-11-19 02:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           96628
passed SCOUT         187
  killed by SCORE    26
  killed by AUDIT    40
FINAL PASS           121

top kill reasons at first sighting (a pool can have several):
  too_young                    95157
  few_unique_buyers            91190
  liquidity_low                89557
  volume_below_liquidity       68345
  sells_dominate               25445
  wash_churn                   19939
  overheated                    8444
  missing                       2753
  too_old                       1101
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5756 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  121    -3.4%    -8.0%   -44.7%   -86.9%    57%
SCOUT PASS, killed later     66    +4.7%    +3.9%   -31.7%   -74.6%    50%
KILLED (tracked)          13171    +0.0%   -60.6%   -82.7%    +0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     150    -94.5%    -68.9%    46%
too_old                        41     -0.6%     -0.4%     7%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  26    -72.2%    -49.8%    58%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    74%
70-79      70    -39.9%    -67.7%    49%
60-69      45    -35.2%    -75.3%    47%
<60        19    -31.3%    -63.7%    42%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      637     -0.4%    -17.8%    -42.1%    34%
<15%      120     +0.4%    -11.2%    -32.5%    35%
15-30%     24     -0.7%     -1.3%     +1.0%    25%
30%+       24     -0.4%     -0.6%     +2.6%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none      597     -0.2%     -3.0%    -17.1%    28%
<20%      180     -8.0%    -60.8%    -93.2%    42%
20%+       28     +9.3%    -98.7%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      769     -0.3%     -8.8%    -32.1%    31%
20-40%     24     -0.4%    -98.8%    -99.1%    71%
40%+       12    -96.5%    -96.5%       -      75%
tokens analysed: 677 | helius credits today: 804/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  121    25%     -8.4%   -14.5%   -99.7%
   -6%     20%  121    26%     -8.8%   -15.0%   -99.7%
   -6%     30%  121    24%     -8.6%   -17.1%   -99.7%
  -10%     12%  121    27%     -8.7%   -18.2%   -99.7%
  -10%     20%  121    28%     -9.2%   -18.6%   -99.7%
  -10%     30%  121    27%     -9.0%   -19.0%   -99.7%
  -15%     12%  121    30%     -8.9%   -19.5%   -99.7%
  -15%     20%  121    31%     -9.5%   -20.4%   -99.7%
  -15%     30%  121    31%     -9.4%   -21.0%   -99.7%
  -25%     12%  121    33%    -11.6%   -17.8%   -99.7%
  -25%     20%  121    36%    -13.9%   -29.9%   -99.7%
  -25%     30%  121    34%    -14.0%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.4% per trade over n=121

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $367.27       $372.55
return                        -26.5%        -25.5%
closed trades                     78            59
win rate                         24%           22%
avg net / trade                -7.4%         -9.5%
expectancy $/trade            $-1.70        $-2.16
max drawdown                  -32.0%        -31.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $367.27 (-26.5%) | cash $367.27 | open 0 | max drawdown -32.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 78 | win 19/78 (24%) | avg net -7.4% | realized $-132.73 | expectancy $-1.70/trade
exits: stop 56, trail 22
  (n=78 < 100: noise, not evidence)
last trades:
  KATIA        $18.19 -> $13.69 (-24.8%)  stop  0.2h
  NVIDIANS     $17.96 -> $15.67 (-12.7%)  stop  0.1h
  ANT          $17.85 -> $15.87 (-11.1%)  stop  0.2h
  SHIT         $17.85 -> $19.44 (+8.9%)  trail  3.7h
  Apocrycoin   $17.83 -> $39.70 (+122.7%)  trail  0.7h
  DCTY         $18.92 -> $15.61 (-17.5%)  stop  0.3h
  DCTY         $18.92 -> $19.28 (+1.9%)  trail  1.3h
  GTASZN       $18.78 -> $10.54 (-43.9%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 450, daily_loss_limit 251, cooldown_after_loss 15, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 224, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 115, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 40, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 22, setup_rejected:operator_cluster 21, setup_rejected:clustered_supply 13, setup_rejected:bundled_buys 13, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
