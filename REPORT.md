# TrenchLab report

Updated: 2026-11-17 22:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           88213
passed SCOUT         174
  killed by SCORE    22
  killed by AUDIT    40
FINAL PASS           112

top kill reasons at first sighting (a pool can have several):
  too_young                    86814
  few_unique_buyers            83140
  liquidity_low                81631
  volume_below_liquidity       62181
  sells_dominate               23158
  wash_churn                   18378
  overheated                    7735
  missing                       2594
  too_old                       1053
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5222 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  112    -4.4%   -11.7%   -46.7%   -88.5%    57%
SCOUT PASS, killed later     62    +4.3%    +3.9%   -49.0%   -52.9%    48%
KILLED (tracked)          12227    +0.0%   -57.5%   -80.6%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     125    -94.1%    -68.9%    47%
too_old                        37     -0.7%     -0.4%     5%
wash_churn                     33     -1.2%    -71.8%    30%
liquidity_low                  24    -69.3%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        53    -58.0%    -93.6%    72%
70-79      65    -43.9%    -67.4%    48%
60-69      39    -47.1%    -99.7%    46%
<60        17    -31.3%    -52.9%    41%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      579     -0.2%    -18.4%    -35.1%    33%
<15%      117     +0.3%    -11.2%    -32.5%    32%
15-30%     23     -0.9%     -2.7%     +1.0%    26%
30%+       23     -0.4%     -0.6%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      558     -0.2%     -3.5%    -15.2%    28%
<20%      161     -4.7%    -58.2%    -91.4%    42%
20%+       23     +7.9%    -98.9%       -      78%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      711     -0.2%     -9.1%    -23.0%    31%
20-40%     20     -2.6%    -99.0%    -99.1%    65%
40%+       11    -96.5%    -96.5%       -      73%
tokens analysed: 624 | helius credits today: 6005/25000

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 375, daily_loss_limit 219, setup_rejected:sellers_dominate_now 122, setup_rejected:dumping_now 100, setup_rejected:volume_dried_up 46, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 16, setup_rejected:bundled_buys 10, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:lp_not_locked 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
