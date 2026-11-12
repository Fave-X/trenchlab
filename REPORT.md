# TrenchLab report

Updated: 2026-11-12 14:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           49886
passed SCOUT         110
  killed by SCORE    14
  killed by AUDIT    25
FINAL PASS           71

top kill reasons at first sighting (a pool can have several):
  too_young                    48840
  few_unique_buyers            46974
  liquidity_low                46107
  volume_below_liquidity       35399
  sells_dominate               13042
  wash_churn                   10057
  overheated                    4263
  missing                       1296
  too_old                        838
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 2728 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   71    -4.3%    -6.0%   -44.0%   -90.9%    59%
SCOUT PASS, killed later     39    +3.0%    +0.7%   -55.0%   +22.4%    46%
KILLED (tracked)           7572    +0.0%   -33.5%   -63.9%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      51    -94.8%    -71.7%    55%
too_old                        25     -0.4%     -0.4%     4%
wash_churn                     14    +11.9%    -71.8%    36%
liquidity_low                  13    -45.9%    -49.8%    46%
volume_below_liquidity          5     +5.9%    +15.3%    60%
overheated                      4    -12.8%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        36    -67.0%    -94.5%    72%
70-79      39    -42.3%    -65.3%    49%
60-69      25    -32.0%    -99.8%    48%
<60        10    -39.8%    +22.4%    30%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      338     -0.3%    -11.4%    -19.8%    35%
<15%       75     +0.3%    -11.7%     -9.3%    32%
15-30%      8     -0.6%     -0.7%     +1.0%    38%
30%+       17     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      338     -0.2%     -2.9%     -7.4%    28%
<20%       88     -1.3%    -49.5%    -96.6%    45%
20%+       12    +17.1%    -99.0%       -      92%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      422     -0.2%     -7.1%    -11.5%    32%
20-40%     12     -1.6%    -99.0%    -99.1%    83%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 355 | helius credits today: 2874/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   71    23%    -11.2%   -17.1%   -99.7%
   -6%     20%   71    24%    -11.2%   -17.1%   -99.7%
   -6%     30%   71    25%     -8.9%   -18.5%   -99.7%
  -10%     12%   71    24%    -12.1%   -19.5%   -99.7%
  -10%     20%   71    24%    -12.5%   -19.6%   -99.7%
  -10%     30%   71    27%    -10.1%   -19.9%   -99.7%
  -15%     12%   71    25%    -11.8%   -20.1%   -99.7%
  -15%     20%   71    27%    -11.9%   -20.4%   -99.7%
  -15%     30%   71    30%     -9.5%   -20.4%   -99.7%
  -25%     12%   71    31%    -13.3%   -21.3%   -99.7%
  -25%     20%   71    32%    -15.2%   -29.7%   -99.7%
  -25%     30%   71    35%    -12.9%   -30.1%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -8.9% per trade over n=71
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $411.00       $435.92
return                        -17.8%        -12.8%
closed trades                     40            31
win rate                         22%           19%
avg net / trade                -9.3%         -8.5%
expectancy $/trade            $-2.23        $-2.07
max drawdown                  -20.9%        -19.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $411.00 (-17.8%) | cash $411.00 | open 0 | max drawdown -20.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 40 | win 9/40 (22%) | avg net -9.3% | realized $-89.00 | expectancy $-2.23/trade
exits: stop 29, trail 11
  (n=40 < 100: noise, not evidence)
last trades:
  NIHAO        $21.58 -> $19.27 (-10.7%)  stop  1.5h
  VEYL         $21.57 -> $30.37 (+40.8%)  trail  0.7h
  DACITY       $21.58 -> $14.66 (-32.0%)  stop  8.3h
  NIHAONOON    $21.56 -> $21.56 (-0.0%)  trail  0.3h
  Max          $21.56 -> $18.83 (-12.7%)  stop  0.7h
  AIB          $21.42 -> $17.45 (-18.6%)  stop  0.2h
  MAX          $21.22 -> $16.96 (-20.1%)  stop  0.2h
  BITCOINU     $21.01 -> $11.81 (-43.8%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 200, daily_loss_limit 191, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $435.92 (-12.8%) | cash $435.92 | open 0 | max drawdown -19.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 31 | win 6/31 (19%) | avg net -8.5% | realized $-64.08 | expectancy $-2.07/trade
exits: stop 25, trail 6
  (n=31 < 100: noise, not evidence)
last trades:
  BOXCAT       $22.87 -> $19.34 (-15.4%)  stop  0.5h
  AIRDROP      $22.69 -> $18.56 (-18.2%)  stop  0.3h
  NOBUSHIBA    $22.79 -> $20.46 (-10.2%)  stop  7.0h
  pants        $22.47 -> $19.96 (-11.2%)  stop  0.5h
  Max          $22.16 -> $19.66 (-11.3%)  stop  0.2h
  NIHAONOON    $22.04 -> $19.02 (-13.7%)  stop  0.3h
  AIB          $21.89 -> $22.83 (+4.3%)  trail  0.8h
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 186, daily_loss_limit 118, setup_rejected:sellers_dominate_now 85, setup_rejected:dumping_now 52, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, cooldown_after_loss 5, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
