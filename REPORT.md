# TrenchLab report

Updated: 2026-11-10 17:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           36490
passed SCOUT         85
  killed by SCORE    9
  killed by AUDIT    19
FINAL PASS           57

top kill reasons at first sighting (a pool can have several):
  too_young                    35672
  few_unique_buyers            34261
  liquidity_low                33553
  volume_below_liquidity       25716
  sells_dominate                9653
  wash_churn                    7618
  overheated                    3212
  missing                       1009
  too_old                        669
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 1838 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   57    -5.0%   -10.6%   -44.0%   -90.4%    56%
SCOUT PASS, killed later     28    +8.4%    +1.3%   -73.5%    +9.6%    46%
KILLED (tracked)           5803    +0.0%   -25.1%   -54.5%    +0.4%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      40    -89.1%    -71.7%    48%
too_old                        21     -0.3%     -2.6%     0%
wash_churn                     12     -1.0%       -      42%
liquidity_low                   8    -56.2%       -      50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        26    -70.6%    -93.8%    81%
70-79      32    -39.9%    -66.9%    47%
60-69      21    -35.2%    -70.7%    38%
<60         6    -39.8%     +9.6%    17%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      272     -0.6%    -10.9%    -13.9%    32%
<15%       62     +0.1%    -11.7%    -10.8%    34%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      273     -0.4%     -3.0%     -4.2%    26%
<20%       72     +0.2%    -44.7%    -94.9%    43%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      343     -0.3%     -6.0%     -9.3%    30%
20-40%      9    -98.6%    -99.2%       -      89%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 285 | helius credits today: 3773/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   57    21%    -11.7%   -17.5%   -99.7%
   -6%     20%   57    23%    -11.7%   -17.5%   -99.7%
   -6%     30%   57    25%     -8.9%   -18.5%   -99.7%
  -10%     12%   57    23%    -12.8%   -20.1%   -99.7%
  -10%     20%   57    23%    -13.3%   -20.2%   -99.7%
  -10%     30%   57    26%    -10.2%   -20.2%   -99.7%
  -15%     12%   57    23%    -13.3%   -20.4%   -99.7%
  -15%     20%   57    25%    -13.5%   -21.0%   -99.7%
  -15%     30%   57    28%    -10.4%   -21.0%   -99.7%
  -25%     12%   57    26%    -16.5%   -29.7%   -99.7%
  -25%     20%   57    28%    -18.2%   -30.1%   -99.7%
  -25%     30%   57    32%    -15.2%   -31.0%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -8.9% per trade over n=57
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $449.48       $457.29
return                        -10.1%         -8.5%
closed trades                     28            18
win rate                         25%           22%
avg net / trade                -6.9%         -9.5%
expectancy $/trade            $-1.80        $-2.37
max drawdown                  -16.6%        -16.2%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $449.48 (-10.1%) | cash $449.48 | open 0 | max drawdown -16.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 28 | win 7/28 (25%) | avg net -6.9% | realized $-50.52 | expectancy $-1.80/trade
exits: stop 20, trail 8
  (n=28 < 100: noise, not evidence)
last trades:
  TITTYVERSE   $23.95 -> $20.01 (-16.4%)  stop  0.5h
  NVIDIOT      $23.75 -> $11.17 (-53.0%)  stop  0.3h
  FAIR         $23.20 -> $18.42 (-20.6%)  stop  0.2h
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 119, cooldown_after_loss 6, max_open_positions 4

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 175, daily_loss_limit 101, setup_rejected:sellers_dominate_now 54, setup_rejected:dumping_now 41, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, cooldown_after_loss 2, setup_rejected:rc_danger:Low Liquidity 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
