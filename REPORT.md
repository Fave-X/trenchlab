# TrenchLab report

Updated: 2026-11-12 01:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           45836
passed SCOUT         100
  killed by SCORE    11
  killed by AUDIT    22
FINAL PASS           67

top kill reasons at first sighting (a pool can have several):
  too_young                    44846
  few_unique_buyers            43199
  liquidity_low                42312
  volume_below_liquidity       32514
  sells_dominate               12062
  wash_churn                    9297
  overheated                    3908
  missing                       1250
  too_old                        795
  rc_danger                        9

OUTCOMES (median price change from first sighting / first pass; 2480 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   67    -3.7%    -6.8%   -44.0%   -89.9%    58%
SCOUT PASS, killed later     33    +6.2%    +0.1%   -52.8%    +9.6%    45%
KILLED (tracked)           7014    +0.0%   -27.8%   -59.6%    +0.4%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      49    -94.2%    -71.7%    53%
too_old                        25     -0.4%     +2.5%     4%
wash_churn                     13    +11.9%       -      38%
liquidity_low                  12    -45.9%    -49.8%    50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      4    -12.8%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        31    -68.5%    -94.3%    84%
70-79      38    -39.9%    -66.4%    45%
60-69      23    -28.3%    -41.6%    43%
<60         8    -19.6%     +9.6%    12%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      317     -0.6%    -11.0%    -14.9%    34%
<15%       71     +0.1%    -11.2%     -8.3%    31%
15-30%      8     -0.6%     -0.7%     +1.0%    38%
30%+       17     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      320     -0.3%     -3.0%     -4.5%    28%
<20%       82     -1.3%    -46.6%    -94.9%    45%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      398     -0.3%     -6.9%    -10.2%    31%
20-40%     11     -4.5%    -99.0%       -      82%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 331 | helius credits today: 197/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   67    24%    -10.2%   -17.1%   -99.7%
   -6%     20%   67    25%    -10.2%   -17.1%   -99.7%
   -6%     30%   67    27%     -7.9%   -17.1%   -99.7%
  -10%     12%   67    25%    -11.2%   -18.7%   -99.7%
  -10%     20%   67    25%    -11.7%   -19.3%   -99.7%
  -10%     30%   67    28%     -9.1%   -19.5%   -99.7%
  -15%     12%   67    27%    -10.9%   -19.9%   -99.7%
  -15%     20%   67    28%    -11.0%   -20.2%   -99.7%
  -15%     30%   67    31%     -8.5%   -20.4%   -99.7%
  -25%     12%   67    31%    -13.1%   -21.3%   -99.7%
  -25%     20%   67    33%    -14.5%   -29.2%   -99.7%
  -25%     30%   67    36%    -12.0%   -29.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -7.9% per trade over n=67
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $428.43       $440.74
return                        -14.3%        -11.9%
closed trades                     37            28
win rate                         24%           18%
avg net / trade                -7.8%         -8.7%
expectancy $/trade            $-1.93        $-2.12
max drawdown                  -18.1%        -18.9%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $428.43 (-14.3%) | cash $428.43 | open 0 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 37 | win 9/37 (24%) | avg net -7.8% | realized $-71.57 | expectancy $-1.93/trade
exits: stop 26, trail 11
  (n=37 < 100: noise, not evidence)
last trades:
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
  mihao        $21.42 -> $26.82 (+25.2%)  trail  2.2h
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
  DACITY       $21.58 -> $14.66 (-32.0%)  stop  8.3h
  NIHAONOON    $21.56 -> $21.56 (-0.0%)  trail  0.3h
  Max          $21.56 -> $18.83 (-12.7%)  stop  0.7h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 164, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $440.74 (-11.9%) | cash $440.74 | open 0 | max drawdown -18.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 28 | win 5/28 (18%) | avg net -8.7% | realized $-59.26 | expectancy $-2.12/trade
exits: stop 23, trail 5
  (n=28 < 100: noise, not evidence)
last trades:
  If           $23.39 -> $18.22 (-22.1%)  stop  1.5h
  DACITY       $23.13 -> $19.06 (-17.6%)  stop  0.3h
  BABYMINHAO   $23.13 -> $20.29 (-12.3%)  stop  0.7h
  BOXCAT       $22.87 -> $19.34 (-15.4%)  stop  0.5h
  AIRDROP      $22.69 -> $18.56 (-18.2%)  stop  0.3h
  NOBUSHIBA    $22.79 -> $20.46 (-10.2%)  stop  7.0h
  pants        $22.47 -> $19.96 (-11.2%)  stop  0.5h
  Max          $22.16 -> $19.66 (-11.3%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 184, daily_loss_limit 118, setup_rejected:sellers_dominate_now 57, setup_rejected:dumping_now 51, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
