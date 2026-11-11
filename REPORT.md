# TrenchLab report

Updated: 2026-11-11 02:51 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           39276
passed SCOUT         92
  killed by SCORE    11
  killed by AUDIT    19
FINAL PASS           62

top kill reasons at first sighting (a pool can have several):
  too_young                    38421
  few_unique_buyers            36927
  liquidity_low                36194
  volume_below_liquidity       27766
  sells_dominate               10384
  wash_churn                    8162
  overheated                    3415
  missing                       1067
  too_old                        693
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 2064 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   62    -5.0%    -7.8%   -45.0%   -90.4%    55%
SCOUT PASS, killed later     30    +8.4%    +1.3%   -50.5%    +9.6%    43%
KILLED (tracked)           6122    +0.0%   -25.5%   -54.5%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      44    -89.1%    -71.7%    50%
too_old                        22     +0.0%     -2.6%     0%
wash_churn                     13     -1.0%       -      38%
liquidity_low                  11    -29.5%       -      36%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  2    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        28    -70.6%    -93.8%    79%
70-79      34    -42.3%    -66.7%    47%
60-69      22    -35.2%    -99.8%    36%
<60         8    -15.2%     +9.6%    12%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      288     -0.4%    -11.0%    -16.0%    33%
<15%       64     +0.1%    -11.7%    -12.3%    33%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      288     -0.3%     -3.0%     -7.4%    27%
<20%       75     -0.0%    -44.7%    -94.9%    43%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      360     -0.3%     -6.0%    -11.5%    31%
20-40%     10    -51.5%    -99.1%       -      80%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 298 | helius credits today: 485/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   62    23%    -11.9%   -17.3%   -99.7%
   -6%     20%   62    24%    -11.9%   -17.3%   -99.7%
   -6%     30%   62    26%     -9.3%   -18.0%   -99.7%
  -10%     12%   62    24%    -12.9%   -19.7%   -99.7%
  -10%     20%   62    24%    -13.4%   -20.0%   -99.7%
  -10%     30%   62    27%    -10.6%   -20.0%   -99.7%
  -15%     12%   62    26%    -12.6%   -20.3%   -99.7%
  -15%     20%   62    27%    -12.7%   -20.6%   -99.7%
  -15%     30%   62    31%     -9.9%   -20.6%   -99.7%
  -25%     12%   62    31%    -14.9%   -29.2%   -99.7%
  -25%     20%   62    32%    -16.5%   -29.9%   -99.7%
  -25%     30%   62    35%    -13.8%   -30.5%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -9.3% per trade over n=62
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $433.71       $471.26
return                        -13.3%         -5.7%
closed trades                     31            19
win rate                         23%           26%
avg net / trade                -9.6%         -5.7%
expectancy $/trade            $-2.38        $-1.51
max drawdown                  -18.1%        -16.2%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $433.71 (-13.3%) | cash $404.76 | open 1 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 31 | win 7/31 (23%) | avg net -9.6% | realized $-73.82 | expectancy $-2.38/trade
exits: stop 23, trail 8
  (n=31 < 100: noise, not evidence)
open:
  mihao        cost $21.42  now $28.95 (+35.2%)  held 2.0h
last trades:
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 133, cooldown_after_loss 8, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $471.26 (-5.7%) | cash $447.78 | open 1 | max drawdown -16.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 19 | win 5/19 (26%) | avg net -5.7% | realized $-28.65 | expectancy $-1.51/trade
exits: stop 14, trail 5
  (n=19 < 100: noise, not evidence)
open:
  X            cost $23.57  now $23.48 (-0.4%)  held 0.2h
last trades:
  BUIDL        $24.34 -> $25.54 (+4.9%)  trail  0.5h
  NVIDIH       $24.40 -> $21.45 (-12.1%)  stop  0.5h
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
  FAIR         $24.47 -> $19.42 (-20.6%)  stop  0.7h
  BORLY        $24.22 -> $18.90 (-22.0%)  stop  0.5h
  YouTube      $24.14 -> $0.05 (-99.8%)  stop  0.2h
  MEOW         $23.95 -> $26.31 (+9.9%)  trail  2.8h
  HOLD         $22.86 -> $36.92 (+61.5%)  trail  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 176, daily_loss_limit 118, setup_rejected:sellers_dominate_now 57, setup_rejected:dumping_now 46, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, cooldown_after_loss 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
