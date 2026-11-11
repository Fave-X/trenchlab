# TrenchLab report

Updated: 2026-11-11 01:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           38975
passed SCOUT         91
  killed by SCORE    10
  killed by AUDIT    19
FINAL PASS           62

top kill reasons at first sighting (a pool can have several):
  too_young                    38126
  few_unique_buyers            36637
  liquidity_low                35914
  volume_below_liquidity       27549
  sells_dominate               10302
  wash_churn                    8098
  overheated                    3392
  missing                       1056
  too_old                        689
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 2053 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   62    -5.2%    -8.2%   -44.7%   -90.4%    55%
SCOUT PASS, killed later     29    +7.3%    +0.7%   -62.0%    +9.6%    45%
KILLED (tracked)           6091    +0.0%   -24.9%   -54.2%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      43    -89.1%    -71.7%    49%
too_old                        22     +0.0%     -2.6%     0%
wash_churn                     12     -1.0%       -      42%
liquidity_low                  11    -49.1%       -      36%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        28    -70.6%    -93.8%    79%
70-79      33    -39.9%    -66.7%    48%
60-69      23    -35.2%    -99.8%    35%
<60         7    -32.2%     +9.6%    14%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      285     -0.6%    -10.9%    -15.5%    33%
<15%       64     +0.1%    -11.7%    -10.8%    33%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      287     -0.4%     -2.9%     -4.7%    27%
<20%       73     -0.0%    -44.7%    -94.9%    42%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      357     -0.3%     -5.3%    -11.1%    31%
20-40%     10    -51.5%    -99.1%       -      80%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 296 | helius credits today: 272/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   61    20%    -12.7%   -17.5%   -99.7%
   -6%     20%   61    21%    -12.7%   -17.5%   -99.7%
   -6%     30%   61    23%    -10.1%   -18.5%   -99.7%
  -10%     12%   61    21%    -13.8%   -19.9%   -99.7%
  -10%     20%   61    21%    -14.3%   -20.1%   -99.7%
  -10%     30%   61    25%    -11.4%   -20.1%   -99.7%
  -15%     12%   61    21%    -14.3%   -20.4%   -99.7%
  -15%     20%   61    23%    -14.4%   -20.7%   -99.7%
  -15%     30%   61    26%    -11.5%   -20.7%   -99.7%
  -25%     12%   61    26%    -16.6%   -29.2%   -99.7%
  -25%     20%   61    28%    -18.2%   -29.9%   -99.7%
  -25%     30%   61    31%    -15.4%   -30.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -10.1% per trade over n=61
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $425.76       $458.32
return                        -14.8%         -8.3%
closed trades                     31            18
win rate                         23%           22%
avg net / trade                -9.6%         -9.5%
expectancy $/trade            $-2.38        $-2.37
max drawdown                  -18.1%        -16.2%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $425.76 (-14.8%) | cash $404.76 | open 1 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 31 | win 7/31 (23%) | avg net -9.6% | realized $-73.82 | expectancy $-2.38/trade
exits: stop 23, trail 8
  (n=31 < 100: noise, not evidence)
open:
  mihao        cost $21.42  now $21.01 (-1.9%)  held 0.9h
last trades:
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 127, cooldown_after_loss 7, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $458.32 (-8.3%) | cash $434.43 | open 1 | max drawdown -16.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 18 | win 4/18 (22%) | avg net -9.5% | realized $-42.71 | expectancy $-2.37/trade
exits: stop 14, trail 4
  (n=18 < 100: noise, not evidence)
open:
  HOLD         cost $22.86  now $23.90 (+4.5%)  held 0.2h
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
