# TrenchLab report

Updated: 2026-11-11 23:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           45285
passed SCOUT         99
  killed by SCORE    11
  killed by AUDIT    22
FINAL PASS           66

top kill reasons at first sighting (a pool can have several):
  too_young                    44299
  few_unique_buyers            42675
  liquidity_low                41795
  volume_below_liquidity       32126
  sells_dominate               11930
  wash_churn                    9214
  overheated                    3876
  missing                       1234
  too_old                        793
  rc_danger                        9

OUTCOMES (median price change from first sighting / first pass; 2448 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   66    -4.2%    -7.3%   -44.0%   -90.4%    59%
SCOUT PASS, killed later     33    +6.2%    +0.1%   -55.0%    +9.6%    45%
KILLED (tracked)           6941    +0.0%   -27.1%   -58.8%    +0.4%    29%

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
70-79      37    -42.3%    -66.4%    46%
60-69      23    -28.3%    -70.7%    43%
<60         8    -19.6%     +9.6%    12%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      316     -0.4%    -11.0%    -15.5%    34%
<15%       71     +0.1%    -11.2%     -9.3%    31%
15-30%      8     -0.6%     -0.7%     +1.0%    38%
30%+       17     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      320     -0.3%     -3.0%     -6.1%    28%
<20%       81     -0.3%    -46.6%    -94.9%    46%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      397     -0.3%     -6.9%    -11.3%    31%
20-40%     11     -4.5%    -99.0%       -      82%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 330 | helius credits today: 4739/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   66    24%    -10.2%   -17.1%   -99.7%
   -6%     20%   66    26%    -10.2%   -17.1%   -99.7%
   -6%     30%   66    27%     -7.9%   -17.3%   -99.7%
  -10%     12%   66    26%    -11.2%   -19.0%   -99.7%
  -10%     20%   66    26%    -11.7%   -19.4%   -99.7%
  -10%     30%   66    29%     -9.1%   -19.7%   -99.7%
  -15%     12%   66    27%    -10.9%   -20.0%   -99.7%
  -15%     20%   66    29%    -11.0%   -20.3%   -99.7%
  -15%     30%   66    32%     -8.5%   -20.4%   -99.7%
  -25%     12%   66    32%    -13.1%   -24.6%   -99.7%
  -25%     20%   66    33%    -14.5%   -29.4%   -99.7%
  -25%     30%   66    36%    -12.1%   -30.0%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -7.9% per trade over n=66
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $431.16       $443.24
return                        -13.8%        -11.4%
closed trades                     36            27
win rate                         25%           19%
avg net / trade                -7.7%         -8.6%
expectancy $/trade            $-1.91        $-2.10
max drawdown                  -18.1%        -18.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $431.16 (-13.8%) | cash $431.16 | open 0 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 36 | win 9/36 (25%) | avg net -7.7% | realized $-68.84 | expectancy $-1.91/trade
exits: stop 25, trail 11
  (n=36 < 100: noise, not evidence)
last trades:
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
  mihao        $21.42 -> $26.82 (+25.2%)  trail  2.2h
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
  DACITY       $21.58 -> $14.66 (-32.0%)  stop  8.3h
  NIHAONOON    $21.56 -> $21.56 (-0.0%)  trail  0.3h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 160, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $443.24 (-11.4%) | cash $443.24 | open 0 | max drawdown -18.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 27 | win 5/27 (19%) | avg net -8.6% | realized $-56.76 | expectancy $-2.10/trade
exits: stop 22, trail 5
  (n=27 < 100: noise, not evidence)
last trades:
  X            $23.57 -> $20.04 (-15.0%)  stop  0.3h
  If           $23.39 -> $18.22 (-22.1%)  stop  1.5h
  DACITY       $23.13 -> $19.06 (-17.6%)  stop  0.3h
  BABYMINHAO   $23.13 -> $20.29 (-12.3%)  stop  0.7h
  BOXCAT       $22.87 -> $19.34 (-15.4%)  stop  0.5h
  AIRDROP      $22.69 -> $18.56 (-18.2%)  stop  0.3h
  NOBUSHIBA    $22.79 -> $20.46 (-10.2%)  stop  7.0h
  pants        $22.47 -> $19.96 (-11.2%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 184, daily_loss_limit 118, setup_rejected:sellers_dominate_now 57, setup_rejected:dumping_now 51, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
