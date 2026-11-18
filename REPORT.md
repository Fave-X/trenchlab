# TrenchLab report

Updated: 2026-11-18 07:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           90762
passed SCOUT         181
  killed by SCORE    25
  killed by AUDIT    39
FINAL PASS           117

top kill reasons at first sighting (a pool can have several):
  too_young                    89347
  few_unique_buyers            85555
  liquidity_low                84053
  volume_below_liquidity       64000
  sells_dominate               23830
  wash_churn                   18935
  overheated                    7981
  missing                       2621
  too_old                       1064
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5421 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  117    -3.4%    -9.9%   -46.7%   -86.9%    56%
SCOUT PASS, killed later     64    +4.7%    +3.9%   -32.5%   -63.7%    48%
KILLED (tracked)          12514    +0.0%   -58.4%   -81.1%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     128    -93.5%    -68.9%    48%
too_old                        38     -0.7%     -0.4%     5%
wash_churn                     34     -1.2%    -71.8%    29%
liquidity_low                  24    -69.3%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    74%
70-79      69    -43.9%    -66.9%    45%
60-69      41    -39.6%    -84.9%    46%
<60        18    -31.7%    -63.7%    39%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      594     -0.3%    -18.0%    -38.9%    33%
<15%      116     +0.1%    -11.2%    -32.5%    34%
15-30%     25     -0.9%     -2.0%     +1.0%    24%
30%+       23     -0.4%     -0.6%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      570     -0.2%     -3.5%    -15.8%    28%
<20%      163     -5.9%    -58.3%    -93.2%    42%
20%+       25     +7.9%    -98.7%       -      76%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      725     -0.3%     -9.1%    -24.6%    31%
20-40%     20     -2.6%    -99.0%    -99.1%    70%
40%+       13    -23.0%    -32.9%       -      62%
tokens analysed: 638 | helius credits today: 1802/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  117    26%     -8.9%   -14.5%   -99.7%
   -6%     20%  117    26%     -9.4%   -15.0%   -99.7%
   -6%     30%  117    24%     -9.2%   -17.1%   -99.7%
  -10%     12%  117    28%     -9.3%   -18.2%   -99.7%
  -10%     20%  117    27%    -10.0%   -18.7%   -99.7%
  -10%     30%  117    26%     -9.7%   -19.1%   -99.7%
  -15%     12%  117    31%     -9.5%   -19.6%   -99.7%
  -15%     20%  117    31%    -10.3%   -20.7%   -99.7%
  -15%     30%  117    30%    -10.2%   -21.1%   -99.7%
  -25%     12%  117    34%    -12.4%   -21.3%   -99.7%
  -25%     20%  117    34%    -15.0%   -30.1%   -99.7%
  -25%     30%  117    33%    -15.0%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.9% per trade over n=117

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $357.56       $382.03
return                        -28.5%        -23.6%
closed trades                     73            57
win rate                         22%           23%
avg net / trade                -8.9%         -9.0%
expectancy $/trade            $-1.99        $-2.07
max drawdown                  -31.7%        -30.0%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $357.56 (-28.5%) | cash $337.13 | open 1 | max drawdown -31.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 73 | win 16/73 (22%) | avg net -8.9% | realized $-145.02 | expectancy $-1.99/trade
exits: stop 54, trail 19
  (n=73 < 100: noise, not evidence)
open:
  SHIT         cost $17.85  now $20.42 (+14.4%)  held 1.5h
last trades:
  bul          $19.24 -> $12.80 (-33.5%)  stop  0.2h
  CHAR         $18.92 -> $15.13 (-20.0%)  stop  1.2h
  KATIA        $18.73 -> $13.75 (-26.6%)  stop  0.3h
  GROKIA       $18.48 -> $14.90 (-19.4%)  stop  0.2h
  GEKKO        $18.30 -> $16.05 (-12.3%)  stop  0.2h
  KATIA        $18.19 -> $13.69 (-24.8%)  stop  0.2h
  NVIDIANS     $17.96 -> $15.67 (-12.7%)  stop  0.1h
  ANT          $17.85 -> $15.87 (-11.1%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 417, daily_loss_limit 251, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $382.03 (-23.6%) | cash $382.03 | open 0 | max drawdown -30.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 57 | win 13/57 (23%) | avg net -9.0% | realized $-117.97 | expectancy $-2.07/trade
exits: stop 44, trail 13
  (n=57 < 100: noise, not evidence)
last trades:
  BAWSAQ       $19.30 -> $37.05 (+92.0%)  trail  1.0h
  LEOSTAR      $20.19 -> $17.80 (-11.9%)  stop  2.2h
  bul          $20.07 -> $27.86 (+38.8%)  trail  1.5h
  KATIA        $20.67 -> $21.60 (+4.5%)  trail  1.0h
  JVOLT        $20.50 -> $0.07 (-99.7%)  stop  0.2h
  JALU         $19.48 -> $17.45 (-10.4%)  stop  0.8h
  NVIDIANS     $19.38 -> $12.07 (-37.7%)  stop  0.3h
  KATIA        $19.01 -> $20.77 (+9.3%)  trail  1.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 392, daily_loss_limit 219, setup_rejected:sellers_dominate_now 128, setup_rejected:dumping_now 105, setup_rejected:volume_dried_up 46, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 19, setup_rejected:operator_cluster 16, setup_rejected:bundled_buys 11, setup_rejected:b_received 10, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
