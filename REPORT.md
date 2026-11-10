# TrenchLab report

Updated: 2026-11-10 23:51 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           38397
passed SCOUT         88
  killed by SCORE    10
  killed by AUDIT    19
FINAL PASS           59

top kill reasons at first sighting (a pool can have several):
  too_young                    37549
  few_unique_buyers            36079
  liquidity_low                35361
  volume_below_liquidity       27109
  sells_dominate               10159
  wash_churn                    7971
  overheated                    3349
  missing                       1045
  too_old                        688
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 1984 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   59    -5.2%    -8.2%   -44.4%   -89.9%    58%
SCOUT PASS, killed later     29    +7.3%    +0.7%   -62.0%    +9.6%    45%
KILLED (tracked)           6032    +0.0%   -24.5%   -55.1%    +0.5%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      42    -89.1%    -71.7%    48%
too_old                        22     +0.0%     -2.6%     0%
wash_churn                     12     -1.0%       -      42%
liquidity_low                  11    -56.2%       -      36%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        28    -68.5%    -93.8%    79%
70-79      33    -39.9%    -66.7%    48%
60-69      20    -35.2%    -70.7%    40%
<60         7    -32.2%     +9.6%    14%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      281     -0.6%    -10.5%    -14.9%    33%
<15%       64     +0.1%    -11.7%    -10.8%    33%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      283     -0.4%     -2.8%     -4.5%    27%
<20%       73     -0.0%    -44.7%    -94.9%    42%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      353     -0.3%     -4.7%    -10.2%    31%
20-40%     10    -51.5%    -99.1%       -      80%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 294 | helius credits today: 5013/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   59    20%    -12.9%   -18.6%   -99.7%
   -6%     20%   59    22%    -12.9%   -18.6%   -99.7%
   -6%     30%   59    24%    -10.2%   -18.6%   -99.7%
  -10%     12%   59    22%    -13.9%   -20.1%   -99.7%
  -10%     20%   59    22%    -14.5%   -20.2%   -99.7%
  -10%     30%   59    25%    -11.5%   -20.2%   -99.7%
  -15%     12%   59    22%    -14.5%   -20.4%   -99.7%
  -15%     20%   59    24%    -14.6%   -21.0%   -99.7%
  -15%     30%   59    27%    -11.7%   -21.0%   -99.7%
  -25%     12%   59    27%    -16.9%   -29.7%   -99.7%
  -25%     20%   59    29%    -18.6%   -30.1%   -99.7%
  -25%     30%   59    32%    -15.7%   -31.0%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -10.2% per trade over n=59
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $428.32       $457.29
return                        -14.3%         -8.5%
closed trades                     30            18
win rate                         23%           22%
avg net / trade                -9.6%         -9.5%
expectancy $/trade            $-2.39        $-2.37
max drawdown                  -17.6%        -16.2%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $428.32 (-14.3%) | cash $428.32 | open 0 | max drawdown -17.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 30 | win 7/30 (23%) | avg net -9.6% | realized $-71.68 | expectancy $-2.39/trade
exits: stop 22, trail 8
  (n=30 < 100: noise, not evidence)
last trades:
  FAIR         $23.20 -> $18.42 (-20.6%)  stop  0.2h
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 124, cooldown_after_loss 6, max_open_positions 4

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 175, daily_loss_limit 118, setup_rejected:sellers_dominate_now 55, setup_rejected:dumping_now 46, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, cooldown_after_loss 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
