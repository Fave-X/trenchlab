# TrenchLab report

Updated: 2026-11-10 13:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           35186
passed SCOUT         84
  killed by SCORE    9
  killed by AUDIT    19
FINAL PASS           56

top kill reasons at first sighting (a pool can have several):
  too_young                    34393
  few_unique_buyers            33034
  liquidity_low                32309
  volume_below_liquidity       24808
  sells_dominate                9314
  wash_churn                    7422
  overheated                    3119
  missing                        989
  too_old                        648
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 1777 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   56    -5.0%   -10.6%   -44.4%   -90.4%    57%
SCOUT PASS, killed later     28    +8.4%    +1.3%   -73.5%    +9.6%    43%
KILLED (tracked)           5648    +0.0%   -23.8%   -53.9%    +0.4%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      38    -92.1%    -71.7%    45%
too_old                        20     -0.3%     -2.6%     0%
wash_churn                     12     -1.0%       -      42%
liquidity_low                   8    -56.2%       -      50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        26    -70.6%    -93.8%    81%
70-79      32    -42.3%    -66.9%    47%
60-69      20    -35.2%    -70.7%    35%
<60         6    -39.8%     +9.6%    17%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      264     -0.9%    -11.4%    -12.9%    32%
<15%       59     +0.2%    -12.6%     -9.3%    34%
15-30%      5     -0.2%     -0.2%     +1.0%    60%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      262     -0.4%     -3.1%     -3.7%    26%
<20%       70     -0.0%    -45.0%    -94.9%    41%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      330     -0.3%     -7.3%     -7.4%    30%
20-40%      9    -98.6%    -99.2%       -      89%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 278 | helius credits today: 2773/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   56    21%    -11.0%   -17.3%   -99.7%
   -6%     20%   56    23%    -11.0%   -17.3%   -99.7%
   -6%     30%   56    25%     -8.1%   -18.0%   -99.7%
  -10%     12%   56    23%    -12.1%   -20.0%   -99.7%
  -10%     20%   56    23%    -12.6%   -20.1%   -99.7%
  -10%     30%   56    27%     -9.5%   -20.1%   -99.7%
  -15%     12%   56    23%    -12.6%   -20.4%   -99.7%
  -15%     20%   56    25%    -12.8%   -20.9%   -99.7%
  -15%     30%   56    29%     -9.6%   -20.9%   -99.7%
  -25%     12%   56    27%    -15.8%   -29.4%   -99.7%
  -25%     20%   56    29%    -17.6%   -30.0%   -99.7%
  -25%     30%   56    32%    -14.6%   -30.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -8.1% per trade over n=56
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $461.28       $457.29
return                         -7.7%         -8.5%
closed trades                     27            18
win rate                         26%           22%
avg net / trade                -5.3%         -9.5%
expectancy $/trade            $-1.43        $-2.37
max drawdown                  -16.6%        -16.2%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $461.28 (-7.7%) | cash $461.28 | open 0 | max drawdown -16.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 27 | win 7/27 (26%) | avg net -5.3% | realized $-38.72 | expectancy $-1.43/trade
exits: stop 19, trail 8
  (n=27 < 100: noise, not evidence)
last trades:
  NVIDIH       $23.16 -> $41.65 (+79.8%)  trail  1.8h
  TITTYVERSE   $23.95 -> $20.01 (-16.4%)  stop  0.5h
  NVIDIOT      $23.75 -> $11.17 (-53.0%)  stop  0.3h
  FAIR         $23.20 -> $18.42 (-20.6%)  stop  0.2h
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 112, cooldown_after_loss 6, max_open_positions 4

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 175, daily_loss_limit 94, setup_rejected:sellers_dominate_now 54, setup_rejected:dumping_now 37, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, cooldown_after_loss 2, setup_rejected:rc_danger:Low Liquidity 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
