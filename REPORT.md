# TrenchLab report

Updated: 2026-11-09 20:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           30083
passed SCOUT         73
  killed by SCORE    9
  killed by AUDIT    14
FINAL PASS           50

top kill reasons at first sighting (a pool can have several):
  too_young                    29370
  few_unique_buyers            28243
  liquidity_low                27518
  volume_below_liquidity       21213
  sells_dominate                8036
  wash_churn                    6313
  overheated                    2676
  missing                        924
  too_old                        585
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1558 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   50    -5.3%   -17.3%   -41.9%   -89.9%    56%
SCOUT PASS, killed later     23   +13.1%    +7.3%   -85.0%    +9.6%    43%
KILLED (tracked)           4876    +0.0%   -21.6%   -53.9%    +0.8%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      29    -65.3%    -68.9%    38%
too_old                        19     +0.2%     -2.6%     0%
wash_churn                     11    -37.1%       -      45%
liquidity_low                   7    -56.2%       -      43%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        23    -70.6%    -93.6%    83%
70-79      28    -34.7%    -66.7%    43%
60-69      16    -37.4%    -70.7%    38%
<60         6    -32.2%     +9.6%    17%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      232     -1.1%     -8.0%    -13.9%    29%
<15%       53     +0.6%    -11.2%     -8.3%    34%
15-30%      4    +39.0%     -0.1%     +1.0%    50%
30%+       14     +0.1%     +0.3%     +1.9%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      235     -0.5%     -2.9%     -3.3%    24%
<20%       60     +1.2%    -33.1%    -96.6%    40%
20%+        8    +24.1%    -99.0%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      293     -0.3%     -3.8%     -6.1%    28%
20-40%      7     +1.3%    -99.0%       -      86%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 240 | helius credits today: 4627/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   50    20%    -12.0%   -17.3%   -99.5%
   -6%     20%   50    22%    -12.0%   -17.3%   -99.5%
   -6%     30%   50    24%     -8.8%   -18.0%   -99.5%
  -10%     12%   50    22%    -12.9%   -19.7%   -99.5%
  -10%     20%   50    22%    -13.5%   -20.0%   -99.5%
  -10%     30%   50    26%    -10.0%   -20.0%   -99.5%
  -15%     12%   50    22%    -13.5%   -20.3%   -99.5%
  -15%     20%   50    24%    -13.7%   -20.6%   -99.5%
  -15%     30%   50    28%    -10.2%   -20.6%   -99.5%
  -25%     12%   50    24%    -18.4%   -29.4%   -99.5%
  -25%     20%   50    26%    -20.4%   -30.0%   -99.5%
  -25%     30%   50    30%    -17.0%   -30.9%   -99.5%
  best so far: stop -6%, trail from +30% -> avg -8.8% per trade over n=50
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $462.44       $489.39
return                         -7.5%         -2.1%
closed trades                     22            14
win rate                         23%           21%
avg net / trade                -6.6%         -2.7%
expectancy $/trade            $-1.71        $-0.76
max drawdown                  -11.0%        -10.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $462.44 (-7.5%) | cash $462.44 | open 0 | max drawdown -11.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 22 | win 5/22 (23%) | avg net -6.6% | realized $-37.56 | expectancy $-1.71/trade
exits: stop 16, trail 6
  (n=22 < 100: noise, not evidence)
last trades:
  TAOLF        $23.66 -> $29.60 (+25.1%)  trail  0.8h
  CLAUDIA      $24.09 -> $19.43 (-19.3%)  stop  0.5h
  BLEND        $23.55 -> $20.73 (-12.0%)  stop  2.7h
  invest       $23.69 -> $15.38 (-35.1%)  stop  0.3h
  BAWSAQ       $23.87 -> $21.06 (-11.8%)  stop  0.7h
  NVIDIH       $23.16 -> $41.65 (+79.8%)  trail  1.8h
  TITTYVERSE   $23.95 -> $20.01 (-16.4%)  stop  0.5h
  NVIDIOT      $23.75 -> $11.17 (-53.0%)  stop  0.3h
signals skipped by the sizer/risk rules: daily_loss_limit 168, already_traded_token 100, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $489.39 (-2.1%) | cash $489.39 | open 0 | max drawdown -10.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 14 | win 3/14 (21%) | avg net -2.7% | realized $-10.61 | expectancy $-0.76/trade
exits: stop 11, trail 3
  (n=14 < 100: noise, not evidence)
last trades:
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
  MAGGIE       $25.21 -> $18.19 (-27.8%)  stop  0.5h
  ELYSION      $24.86 -> $20.95 (-15.7%)  stop  0.5h
  PUSSY        $24.66 -> $21.70 (-12.0%)  stop  0.2h
  TITTYVERSE   $24.51 -> $20.97 (-14.4%)  stop  0.3h
  BUIDL        $24.34 -> $25.54 (+4.9%)  trail  0.5h
  NVIDIH       $24.40 -> $21.45 (-12.1%)  stop  0.5h
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 146, daily_loss_limit 94, setup_rejected:sellers_dominate_now 54, setup_rejected:dumping_now 37, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_received 6, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
