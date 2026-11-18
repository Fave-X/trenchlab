# TrenchLab report

Updated: 2026-11-18 17:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           93921
passed SCOUT         183
  killed by SCORE    26
  killed by AUDIT    39
FINAL PASS           118

top kill reasons at first sighting (a pool can have several):
  too_young                    92485
  few_unique_buyers            88605
  liquidity_low                86998
  volume_below_liquidity       66324
  sells_dominate               24699
  wash_churn                   19408
  overheated                    8198
  missing                       2710
  too_old                       1079
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5586 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  118    -3.3%    -8.2%   -45.0%   -86.4%    58%
SCOUT PASS, killed later     65    +4.3%    +3.7%   -32.2%   -63.7%    48%
KILLED (tracked)          12851    +0.0%   -58.9%   -81.7%    +0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     140    -93.5%    -68.9%    46%
too_old                        38     -0.6%     -0.4%     8%
wash_churn                     35    -23.3%    -85.6%    31%
liquidity_low                  26    -72.2%    -49.8%    58%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    74%
70-79      69    -41.9%    -67.4%    48%
60-69      42    -37.4%    -75.3%    48%
<60        19    -31.3%    -63.7%    37%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      615     -0.4%    -17.9%    -42.1%    34%
<15%      117     +0.2%    -11.2%    -24.0%    33%
15-30%     24     -0.7%     -1.3%     +1.0%    25%
30%+       23     -0.4%     -0.6%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      582     -0.2%     -3.0%    -17.1%    28%
<20%      172     -6.0%    -58.5%    -93.7%    43%
20%+       25     +7.9%    -98.7%       -      76%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      746     -0.3%     -8.9%    -31.6%    31%
20-40%     22     -2.6%    -98.8%    -99.1%    64%
40%+       11    -96.5%    -96.5%       -      73%
tokens analysed: 655 | helius credits today: 4765/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  118    25%     -8.0%   -14.2%   -99.7%
   -6%     20%  118    25%     -8.5%   -14.9%   -99.7%
   -6%     30%  118    24%     -8.3%   -17.1%   -99.7%
  -10%     12%  118    28%     -8.3%   -18.0%   -99.7%
  -10%     20%  118    28%     -8.9%   -18.6%   -99.7%
  -10%     30%  118    27%     -8.7%   -19.1%   -99.7%
  -15%     12%  118    31%     -8.5%   -19.6%   -99.7%
  -15%     20%  118    31%     -9.2%   -20.6%   -99.7%
  -15%     30%  118    31%     -9.2%   -21.1%   -99.7%
  -25%     12%  118    34%    -11.4%   -19.6%   -99.7%
  -25%     20%  118    35%    -13.9%   -30.0%   -99.7%
  -25%     30%  118    34%    -13.9%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.0% per trade over n=118

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $378.45       $372.55
return                        -24.3%        -25.5%
closed trades                     75            59
win rate                         24%           22%
avg net / trade                -6.9%         -9.5%
expectancy $/trade            $-1.62        $-2.16
max drawdown                  -32.0%        -31.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $378.45 (-24.3%) | cash $378.45 | open 0 | max drawdown -32.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 75 | win 18/75 (24%) | avg net -6.9% | realized $-121.55 | expectancy $-1.62/trade
exits: stop 54, trail 21
  (n=75 < 100: noise, not evidence)
last trades:
  KATIA        $18.73 -> $13.75 (-26.6%)  stop  0.3h
  GROKIA       $18.48 -> $14.90 (-19.4%)  stop  0.2h
  GEKKO        $18.30 -> $16.05 (-12.3%)  stop  0.2h
  KATIA        $18.19 -> $13.69 (-24.8%)  stop  0.2h
  NVIDIANS     $17.96 -> $15.67 (-12.7%)  stop  0.1h
  ANT          $17.85 -> $15.87 (-11.1%)  stop  0.2h
  SHIT         $17.85 -> $19.44 (+8.9%)  trail  3.7h
  Apocrycoin   $17.83 -> $39.70 (+122.7%)  trail  0.7h
signals skipped by the sizer/risk rules: already_traded_token 423, daily_loss_limit 251, cooldown_after_loss 15, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 408, daily_loss_limit 219, setup_rejected:sellers_dominate_now 129, setup_rejected:dumping_now 111, setup_rejected:volume_dried_up 47, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 22, setup_rejected:operator_cluster 21, setup_rejected:clustered_supply 11, setup_rejected:bundled_buys 11, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
