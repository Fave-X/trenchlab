# TrenchLab report

Updated: 2026-11-11 07:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           40550
passed SCOUT         95
  killed by SCORE    11
  killed by AUDIT    19
FINAL PASS           65

top kill reasons at first sighting (a pool can have several):
  too_young                    39665
  few_unique_buyers            38145
  liquidity_low                37352
  volume_below_liquidity       28649
  sells_dominate               10692
  wash_churn                    8430
  overheated                    3514
  missing                       1128
  too_old                        714
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 2121 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   65    -4.6%    -7.3%   -44.0%   -89.9%    55%
SCOUT PASS, killed later     30    +6.2%    +0.2%   -50.5%    +9.6%    43%
KILLED (tracked)           6283    +0.0%   -26.1%   -55.8%    +0.4%    29%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      46    -94.9%    -71.7%    50%
too_old                        23     -0.2%     -2.6%     0%
wash_churn                     13    +11.9%       -      38%
liquidity_low                  11    -29.5%       -      36%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        29    -70.6%    -93.8%    79%
70-79      35    -39.9%    -66.7%    49%
60-69      23    -28.8%    -70.7%    35%
<60         8    -19.6%     +9.6%    12%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      296     -0.5%    -10.7%    -23.6%    33%
<15%       65     +0.1%    -12.1%    -12.3%    32%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      294     -0.4%     -2.9%     -9.3%    27%
<20%       78     -0.2%    -44.8%    -94.9%    42%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      368     -0.3%     -6.0%    -11.6%    30%
20-40%     11     -4.5%    -99.1%       -      73%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 306 | helius credits today: 1265/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   65    25%    -10.3%   -17.1%   -99.7%
   -6%     20%   65    26%    -10.3%   -17.1%   -99.7%
   -6%     30%   65    28%     -7.7%   -17.1%   -99.7%
  -10%     12%   65    26%    -11.3%   -19.3%   -99.7%
  -10%     20%   65    26%    -11.8%   -19.5%   -99.7%
  -10%     30%   65    29%     -9.0%   -19.5%   -99.7%
  -15%     12%   65    28%    -11.0%   -20.1%   -99.7%
  -15%     20%   65    29%    -11.2%   -20.4%   -99.7%
  -15%     30%   65    32%     -8.4%   -20.4%   -99.7%
  -25%     12%   65    32%    -13.2%   -27.9%   -99.7%
  -25%     20%   65    34%    -14.7%   -29.7%   -99.7%
  -25%     30%   65    37%    -12.0%   -29.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -7.7% per trade over n=65
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $440.41       $462.65
return                        -11.9%         -7.5%
closed trades                     34            21
win rate                         26%           24%
avg net / trade                -7.2%         -7.0%
expectancy $/trade            $-1.82        $-1.78
max drawdown                  -18.1%        -16.2%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $440.41 (-11.9%) | cash $416.50 | open 1 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 34 | win 9/34 (26%) | avg net -7.2% | realized $-61.92 | expectancy $-1.82/trade
exits: stop 24, trail 10
  (n=34 < 100: noise, not evidence)
open:
  DACITY       cost $21.58  now $23.91 (+10.8%)  held 3.9h
last trades:
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
  mihao        $21.42 -> $26.82 (+25.2%)  trail  2.2h
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 149, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $462.65 (-7.5%) | cash $462.65 | open 0 | max drawdown -16.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 21 | win 5/21 (24%) | avg net -7.0% | realized $-37.35 | expectancy $-1.78/trade
exits: stop 16, trail 5
  (n=21 < 100: noise, not evidence)
last trades:
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
  FAIR         $24.47 -> $19.42 (-20.6%)  stop  0.7h
  BORLY        $24.22 -> $18.90 (-22.0%)  stop  0.5h
  YouTube      $24.14 -> $0.05 (-99.8%)  stop  0.2h
  MEOW         $23.95 -> $26.31 (+9.9%)  trail  2.8h
  HOLD         $22.86 -> $36.92 (+61.5%)  trail  0.7h
  X            $23.57 -> $20.04 (-15.0%)  stop  0.3h
  If           $23.39 -> $18.22 (-22.1%)  stop  1.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 179, daily_loss_limit 118, setup_rejected:sellers_dominate_now 57, setup_rejected:dumping_now 46, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, cooldown_after_loss 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
