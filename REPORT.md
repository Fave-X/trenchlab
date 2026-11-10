# TrenchLab report

Updated: 2026-11-10 10:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           34264
passed SCOUT         84
  killed by SCORE    9
  killed by AUDIT    19
FINAL PASS           56

top kill reasons at first sighting (a pool can have several):
  too_young                    33475
  few_unique_buyers            32176
  liquidity_low                31444
  volume_below_liquidity       24186
  sells_dominate                9072
  wash_churn                    7194
  overheated                    3020
  missing                        977
  too_old                        644
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 1733 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   56    -4.6%    -8.2%   -44.4%   -90.4%    55%
SCOUT PASS, killed later     28    +8.4%    +1.3%   -78.9%    +9.6%    43%
KILLED (tracked)           5507    +0.0%   -22.9%   -53.1%    +0.4%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      37    -85.3%    -71.7%    46%
too_old                        20     -0.2%     -2.6%     0%
wash_churn                     12     -1.0%       -      42%
liquidity_low                   8    -56.2%       -      50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        26    -70.6%    -93.8%    81%
70-79      31    -42.3%    -66.9%    48%
60-69      21    -37.4%    -70.7%    29%
<60         6    -39.8%     +9.6%    17%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      261     -1.0%    -10.9%    -12.9%    31%
<15%       59     +0.2%    -13.1%     -9.3%    34%
15-30%      5     -0.2%     -0.2%     +1.0%    60%
30%+       15     -0.2%     +0.3%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      260     -0.4%     -3.0%     -3.7%    26%
<20%       69     -0.0%    -44.8%    -94.9%    42%
20%+       11    +16.6%    -99.1%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      327     -0.3%     -7.3%     -7.4%    29%
20-40%      9    -98.6%    -99.2%       -      89%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 275 | helius credits today: 2441/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   55    22%    -10.3%   -17.1%   -99.7%
   -6%     20%   55    24%    -10.3%   -17.1%   -99.7%
   -6%     30%   55    25%     -7.4%   -17.5%   -99.7%
  -10%     12%   55    24%    -11.4%   -19.9%   -99.7%
  -10%     20%   55    24%    -12.0%   -20.1%   -99.7%
  -10%     30%   55    27%     -8.8%   -20.1%   -99.7%
  -15%     12%   55    24%    -12.0%   -20.4%   -99.7%
  -15%     20%   55    25%    -12.1%   -20.7%   -99.7%
  -15%     30%   55    29%     -8.9%   -20.7%   -99.7%
  -25%     12%   55    27%    -15.3%   -29.2%   -99.7%
  -25%     20%   55    29%    -17.0%   -29.9%   -99.7%
  -25%     30%   55    33%    -14.0%   -30.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -7.4% per trade over n=55
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $472.41       $457.29
return                         -5.5%         -8.5%
closed trades                     26            18
win rate                         27%           22%
avg net / trade                -3.7%         -9.5%
expectancy $/trade            $-1.06        $-2.37
max drawdown                  -16.6%        -16.2%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $472.41 (-5.5%) | cash $448.79 | open 1 | max drawdown -16.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 26 | win 7/26 (27%) | avg net -3.7% | realized $-27.59 | expectancy $-1.06/trade
exits: stop 18, trail 8
  (n=26 < 100: noise, not evidence)
open:
  X            cost $23.62  now $23.62 (+0.0%)  held 0.0h
last trades:
  BAWSAQ       $23.87 -> $21.06 (-11.8%)  stop  0.7h
  NVIDIH       $23.16 -> $41.65 (+79.8%)  trail  1.8h
  TITTYVERSE   $23.95 -> $20.01 (-16.4%)  stop  0.5h
  NVIDIOT      $23.75 -> $11.17 (-53.0%)  stop  0.3h
  FAIR         $23.20 -> $18.42 (-20.6%)  stop  0.2h
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 110, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $457.29 (-8.5%) | cash $457.29 | open 0 | max drawdown -16.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 18 | win 4/18 (22%) | avg net -9.5% | realized $-42.71 | expectancy $-2.37/trade
exits: stop 14, trail 4
  (n=18 < 100: noise, not evidence)
last trades:
  TITTYVERSE   $24.51 -> $20.97 (-14.4%)  stop  0.3h
  BUIDL        $24.34 -> $25.54 (+4.9%)  trail  0.5h
  NVIDIH       $24.40 -> $21.45 (-12.1%)  stop  0.5h
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
  FAIR         $24.47 -> $19.42 (-20.6%)  stop  0.7h
  BORLY        $24.22 -> $18.90 (-22.0%)  stop  0.5h
  YouTube      $24.14 -> $0.05 (-99.8%)  stop  0.2h
  MEOW         $23.95 -> $26.31 (+9.9%)  trail  2.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 173, daily_loss_limit 94, setup_rejected:sellers_dominate_now 54, setup_rejected:dumping_now 37, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, cooldown_after_loss 2, setup_rejected:rc_danger:Low Liquidity 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
