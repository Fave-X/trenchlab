# TrenchLab report

Updated: 2026-11-18 00:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           88652
passed SCOUT         175
  killed by SCORE    23
  killed by AUDIT    40
FINAL PASS           112

top kill reasons at first sighting (a pool can have several):
  too_young                    87249
  few_unique_buyers            83556
  liquidity_low                82048
  volume_below_liquidity       62498
  sells_dominate               23254
  wash_churn                   18474
  overheated                    7788
  missing                       2598
  too_old                       1056
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5243 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  112    -4.4%   -12.0%   -46.7%   -88.5%    58%
SCOUT PASS, killed later     63    +4.3%    +4.2%   -32.2%   -63.7%    48%
KILLED (tracked)          12273    +0.0%   -57.6%   -80.8%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     127    -93.8%    -68.9%    46%
too_old                        37     -0.7%     -0.4%     5%
wash_churn                     33     -1.2%    -71.8%    30%
liquidity_low                  24    -69.3%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -55.6%    -93.6%    74%
70-79      66    -43.9%    -67.4%    47%
60-69      38    -45.2%    -99.7%    47%
<60        18    -29.7%    -63.7%    39%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      583     -0.2%    -17.8%    -35.1%    33%
<15%      118     +0.2%    -11.2%    -32.7%    32%
15-30%     23     -0.9%     -2.7%     +1.0%    26%
30%+       23     -0.4%     -0.6%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      561     -0.2%     -3.0%    -15.2%    28%
<20%      163     -3.5%    -58.2%    -92.3%    41%
20%+       23     +7.9%    -98.9%       -      78%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      716     -0.2%     -8.8%    -23.6%    31%
20-40%     20     -2.6%    -99.0%    -99.1%    65%
40%+       11    -96.5%    -96.5%       -      73%
tokens analysed: 628 | helius credits today: 293/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  112    26%     -9.0%   -16.0%   -99.7%
   -6%     20%  112    26%     -9.5%   -17.1%   -99.7%
   -6%     30%  112    24%     -9.3%   -17.6%   -99.7%
  -10%     12%  112    28%    -10.0%   -18.9%   -99.7%
  -10%     20%  112    27%    -10.7%   -19.2%   -99.7%
  -10%     30%  112    26%    -10.4%   -19.6%   -99.7%
  -15%     12%  112    29%    -10.5%   -20.0%   -99.7%
  -15%     20%  112    29%    -11.2%   -20.8%   -99.7%
  -15%     30%  112    29%    -11.1%   -21.1%   -99.7%
  -25%     12%  112    33%    -13.5%   -28.3%   -99.7%
  -25%     20%  112    33%    -15.9%   -30.8%   -99.7%
  -25%     30%  112    32%    -15.9%   -31.1%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -9.0% per trade over n=112

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $359.25       $387.58
return                        -28.2%        -22.5%
closed trades                     71            55
win rate                         23%           22%
avg net / trade                -8.8%         -8.8%
expectancy $/trade            $-1.98        $-2.04
max drawdown                  -30.9%        -29.0%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $359.25 (-28.2%) | cash $359.25 | open 0 | max drawdown -30.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 71 | win 16/71 (23%) | avg net -8.8% | realized $-140.75 | expectancy $-1.98/trade
exits: stop 52, trail 19
  (n=71 < 100: noise, not evidence)
last trades:
  FiveM        $19.66 -> $0.01 (-100.0%)  stop  4.0h
  BAWSAQ       $18.38 -> $35.64 (+93.9%)  trail  1.0h
  bul          $19.24 -> $12.80 (-33.5%)  stop  0.2h
  CHAR         $18.92 -> $15.13 (-20.0%)  stop  1.2h
  KATIA        $18.73 -> $13.75 (-26.6%)  stop  0.3h
  GROKIA       $18.48 -> $14.90 (-19.4%)  stop  0.2h
  GEKKO        $18.30 -> $16.05 (-12.3%)  stop  0.2h
  KATIA        $18.19 -> $13.69 (-24.8%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 409, daily_loss_limit 251, cooldown_after_loss 13, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $387.58 (-22.5%) | cash $387.58 | open 0 | max drawdown -29.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 55 | win 12/55 (22%) | avg net -8.8% | realized $-112.42 | expectancy $-2.04/trade
exits: stop 43, trail 12
  (n=55 < 100: noise, not evidence)
last trades:
  Trader       $19.64 -> $14.98 (-23.7%)  stop  0.7h
  BAWSAQ       $19.64 -> $17.51 (-10.9%)  stop  1.2h
  BAWSAQ       $19.30 -> $37.05 (+92.0%)  trail  1.0h
  LEOSTAR      $20.19 -> $17.80 (-11.9%)  stop  2.2h
  bul          $20.07 -> $27.86 (+38.8%)  trail  1.5h
  KATIA        $20.67 -> $21.60 (+4.5%)  trail  1.0h
  JVOLT        $20.50 -> $0.07 (-99.7%)  stop  0.2h
  JALU         $19.48 -> $17.45 (-10.4%)  stop  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 375, daily_loss_limit 219, setup_rejected:sellers_dominate_now 128, setup_rejected:dumping_now 101, setup_rejected:volume_dried_up 46, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 16, setup_rejected:bundled_buys 11, setup_rejected:b_received 8, setup_rejected:lp_not_locked 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
