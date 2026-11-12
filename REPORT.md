# TrenchLab report

Updated: 2026-11-12 05:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           47184
passed SCOUT         105
  killed by SCORE    13
  killed by AUDIT    23
FINAL PASS           69

top kill reasons at first sighting (a pool can have several):
  too_young                    46181
  few_unique_buyers            44445
  liquidity_low                43561
  volume_below_liquidity       33484
  sells_dominate               12347
  wash_churn                    9517
  overheated                    4040
  missing                       1270
  too_old                        804
  rc_danger                       10

OUTCOMES (median price change from first sighting / first pass; 2583 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   69    -3.7%    -3.4%   -44.0%   -90.9%    58%
SCOUT PASS, killed later     36    +4.4%    +0.7%   -55.0%   +22.4%    44%
KILLED (tracked)           7220    +0.0%   -30.3%   -61.9%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      49    -94.2%    -71.7%    53%
too_old                        25     -0.4%     -0.4%     4%
wash_churn                     14    +11.9%    -71.8%    36%
liquidity_low                  12    -45.9%    -49.8%    50%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      4    -12.8%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        33    -68.5%    -94.5%    79%
70-79      39    -39.9%    -65.3%    46%
60-69      24    -28.8%    -99.8%    46%
<60         9    -19.6%    +22.4%    11%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      327     -0.3%    -10.9%    -24.6%    34%
<15%       75     +0.3%    -11.7%     -8.3%    31%
15-30%      8     -0.6%     -0.7%     +1.0%    38%
30%+       17     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      330     -0.2%     -2.9%     -9.3%    27%
<20%       85     -0.8%    -44.8%    -94.9%    44%
20%+       12    +17.1%    -99.0%       -      92%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      411     -0.2%     -6.6%    -11.6%    30%
20-40%     12     -1.6%    -99.0%    -99.1%    83%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 344 | helius credits today: 1552/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   69    23%    -10.5%   -17.1%   -99.7%
   -6%     20%   69    25%    -10.5%   -17.1%   -99.7%
   -6%     30%   69    26%     -8.2%   -17.5%   -99.7%
  -10%     12%   69    25%    -11.5%   -19.3%   -99.7%
  -10%     20%   69    25%    -11.9%   -19.5%   -99.7%
  -10%     30%   69    28%     -9.4%   -19.6%   -99.7%
  -15%     12%   69    26%    -11.2%   -19.9%   -99.7%
  -15%     20%   69    28%    -11.3%   -20.2%   -99.7%
  -15%     30%   69    30%     -8.8%   -20.4%   -99.7%
  -25%     12%   69    32%    -12.5%   -17.1%   -99.7%
  -25%     20%   69    33%    -14.5%   -29.2%   -99.7%
  -25%     30%   69    36%    -12.2%   -29.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -8.2% per trade over n=69
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $420.19       $438.66
return                        -16.0%        -12.3%
closed trades                     39            30
win rate                         23%           20%
avg net / trade                -8.4%         -8.4%
expectancy $/trade            $-2.05        $-2.04
max drawdown                  -19.1%        -19.6%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $420.19 (-16.0%) | cash $420.19 | open 0 | max drawdown -19.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 39 | win 9/39 (23%) | avg net -8.4% | realized $-79.81 | expectancy $-2.05/trade
exits: stop 28, trail 11
  (n=39 < 100: noise, not evidence)
last trades:
  mihao        $21.42 -> $26.82 (+25.2%)  trail  2.2h
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
  DACITY       $21.58 -> $14.66 (-32.0%)  stop  8.3h
  NIHAONOON    $21.56 -> $21.56 (-0.0%)  trail  0.3h
  Max          $21.56 -> $18.83 (-12.7%)  stop  0.7h
  AIB          $21.42 -> $17.45 (-18.6%)  stop  0.2h
  MAX          $21.22 -> $16.96 (-20.1%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 192, daily_loss_limit 169, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $438.66 (-12.3%) | cash $438.66 | open 0 | max drawdown -19.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 30 | win 6/30 (20%) | avg net -8.4% | realized $-61.34 | expectancy $-2.04/trade
exits: stop 24, trail 6
  (n=30 < 100: noise, not evidence)
last trades:
  BABYMINHAO   $23.13 -> $20.29 (-12.3%)  stop  0.7h
  BOXCAT       $22.87 -> $19.34 (-15.4%)  stop  0.5h
  AIRDROP      $22.69 -> $18.56 (-18.2%)  stop  0.3h
  NOBUSHIBA    $22.79 -> $20.46 (-10.2%)  stop  7.0h
  pants        $22.47 -> $19.96 (-11.2%)  stop  0.5h
  Max          $22.16 -> $19.66 (-11.3%)  stop  0.2h
  NIHAONOON    $22.04 -> $19.02 (-13.7%)  stop  0.3h
  AIB          $21.89 -> $22.83 (+4.3%)  trail  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 184, daily_loss_limit 118, setup_rejected:sellers_dominate_now 58, setup_rejected:dumping_now 52, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
