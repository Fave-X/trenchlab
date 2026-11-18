# TrenchLab report

Updated: 2026-11-18 03:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           89578
passed SCOUT         178
  killed by SCORE    24
  killed by AUDIT    39
FINAL PASS           115

top kill reasons at first sighting (a pool can have several):
  too_young                    88170
  few_unique_buyers            84420
  liquidity_low                82931
  volume_below_liquidity       63148
  sells_dominate               23512
  wash_churn                   18685
  overheated                    7889
  missing                       2600
  too_old                       1059
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5344 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  115    -4.2%   -12.5%   -48.2%   -88.1%    57%
SCOUT PASS, killed later     63    +4.3%    +4.2%   -39.8%   -63.7%    49%
KILLED (tracked)          12383    +0.0%   -58.1%   -81.0%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     127    -93.8%    -68.9%    47%
too_old                        37     -0.7%     -0.4%     5%
wash_churn                     34     -1.2%    -71.8%    29%
liquidity_low                  24    -69.3%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    74%
70-79      68    -43.9%    -67.2%    46%
60-69      40    -45.2%    -99.7%    48%
<60        17    -31.3%    -63.7%    41%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      588     -0.3%    -17.9%    -35.1%    33%
<15%      116     +0.1%    -11.2%    -32.5%    34%
15-30%     24     -0.7%     -2.0%     +1.0%    25%
30%+       23     -0.4%     -0.6%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      565     -0.2%     -3.3%    -15.2%    27%
<20%      162     -6.0%    -58.3%    -93.2%    42%
20%+       24     +8.6%    -98.9%       -      79%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      719     -0.3%     -9.0%    -23.0%    31%
20-40%     20     -2.6%    -99.0%    -99.1%    70%
40%+       12    -42.4%    -96.5%       -      67%
tokens analysed: 632 | helius credits today: 951/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  115    25%     -9.1%   -14.9%   -99.7%
   -6%     20%  115    25%     -9.6%   -15.1%   -99.7%
   -6%     30%  115    23%     -9.4%   -17.1%   -99.7%
  -10%     12%  115    27%    -10.1%   -18.6%   -99.7%
  -10%     20%  115    26%    -10.8%   -19.0%   -99.7%
  -10%     30%  115    25%    -10.5%   -19.3%   -99.7%
  -15%     12%  115    30%    -10.4%   -19.6%   -99.7%
  -15%     20%  115    30%    -11.1%   -20.7%   -99.7%
  -15%     30%  115    29%    -11.1%   -21.1%   -99.7%
  -25%     12%  115    33%    -13.3%   -21.3%   -99.7%
  -25%     20%  115    33%    -15.7%   -30.1%   -99.7%
  -25%     30%  115    32%    -15.8%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -9.1% per trade over n=115

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $356.96       $380.27
return                        -28.6%        -23.9%
closed trades                     72            56
win rate                         22%           21%
avg net / trade                -8.8%         -9.3%
expectancy $/trade            $-1.99        $-2.14
max drawdown                  -31.3%        -30.0%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $356.96 (-28.6%) | cash $356.96 | open 0 | max drawdown -31.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 72 | win 16/72 (22%) | avg net -8.8% | realized $-143.04 | expectancy $-1.99/trade
exits: stop 53, trail 19
  (n=72 < 100: noise, not evidence)
last trades:
  BAWSAQ       $18.38 -> $35.64 (+93.9%)  trail  1.0h
  bul          $19.24 -> $12.80 (-33.5%)  stop  0.2h
  CHAR         $18.92 -> $15.13 (-20.0%)  stop  1.2h
  KATIA        $18.73 -> $13.75 (-26.6%)  stop  0.3h
  GROKIA       $18.48 -> $14.90 (-19.4%)  stop  0.2h
  GEKKO        $18.30 -> $16.05 (-12.3%)  stop  0.2h
  KATIA        $18.19 -> $13.69 (-24.8%)  stop  0.2h
  NVIDIANS     $17.96 -> $15.67 (-12.7%)  stop  0.1h
signals skipped by the sizer/risk rules: already_traded_token 410, daily_loss_limit 251, cooldown_after_loss 15, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $380.27 (-23.9%) | cash $380.27 | open 0 | max drawdown -30.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 56 | win 12/56 (21%) | avg net -9.3% | realized $-119.73 | expectancy $-2.14/trade
exits: stop 44, trail 12
  (n=56 < 100: noise, not evidence)
last trades:
  BAWSAQ       $19.64 -> $17.51 (-10.9%)  stop  1.2h
  BAWSAQ       $19.30 -> $37.05 (+92.0%)  trail  1.0h
  LEOSTAR      $20.19 -> $17.80 (-11.9%)  stop  2.2h
  bul          $20.07 -> $27.86 (+38.8%)  trail  1.5h
  KATIA        $20.67 -> $21.60 (+4.5%)  trail  1.0h
  JVOLT        $20.50 -> $0.07 (-99.7%)  stop  0.2h
  JALU         $19.48 -> $17.45 (-10.4%)  stop  0.8h
  NVIDIANS     $19.38 -> $12.07 (-37.7%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 382, daily_loss_limit 219, setup_rejected:sellers_dominate_now 128, setup_rejected:dumping_now 103, setup_rejected:volume_dried_up 46, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 16, setup_rejected:bundled_buys 11, setup_rejected:b_received 10, setup_rejected:lp_not_locked 8, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
