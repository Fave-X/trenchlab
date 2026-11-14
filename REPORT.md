# TrenchLab report

Updated: 2026-11-14 16:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           64724
passed SCOUT         133
  killed by SCORE    18
  killed by AUDIT    30
FINAL PASS           85

top kill reasons at first sighting (a pool can have several):
  too_young                    63524
  few_unique_buyers            61019
  liquidity_low                59777
  volume_below_liquidity       45863
  sells_dominate               17046
  wash_churn                   13239
  overheated                    5614
  missing                       1848
  too_old                        938
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 3737 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   85    -3.8%    -6.5%   -43.9%   -90.9%    60%
SCOUT PASS, killed later     48    +4.7%    +3.4%   -55.0%   -15.3%    46%
KILLED (tracked)           9342    +0.0%   -50.6%   -73.1%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      66    -94.8%    -71.7%    55%
too_old                        33     -0.6%     -0.4%     3%
wash_churn                     23     -1.2%    -71.8%    30%
liquidity_low                  16    -51.1%    -49.8%    50%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      5     -3.6%    -79.6%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        42    -60.4%    -94.0%    71%
70-79      51    -42.3%    -66.7%    51%
60-69      27    -32.0%    -99.8%    48%
<60        13    -32.2%    -15.3%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      426     -0.2%    -10.7%    -32.6%    34%
<15%       87     +0.1%    -11.2%    -15.5%    32%
15-30%     10     -0.6%     -0.7%     +1.0%    30%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      432     -0.2%     -2.1%    -12.6%    27%
<20%       98     -1.4%    -53.7%    -96.6%    47%
20%+       15    +16.6%    -99.0%       -      87%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      523     -0.2%     -3.6%    -15.5%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+        7    -43.5%    -46.3%       -      57%
tokens analysed: 444 | helius credits today: 4179/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   85    25%     -9.5%   -17.1%   -99.7%
   -6%     20%   85    25%     -9.6%   -17.1%   -99.7%
   -6%     30%   85    26%     -7.8%   -17.1%   -99.7%
  -10%     12%   85    27%     -9.3%   -19.3%   -99.7%
  -10%     20%   85    26%     -9.8%   -19.5%   -99.7%
  -10%     30%   85    28%     -7.8%   -19.6%   -99.7%
  -15%     12%   85    29%     -8.7%   -19.9%   -99.7%
  -15%     20%   85    29%     -9.0%   -20.4%   -99.7%
  -15%     30%   85    32%     -7.0%   -20.7%   -99.7%
  -25%     12%   85    34%    -11.0%   -17.1%   -99.7%
  -25%     20%   85    34%    -13.1%   -29.9%   -99.7%
  -25%     30%   85    36%    -11.1%   -30.8%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.0% per trade over n=85
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $435.99       $424.96
return                        -12.8%        -15.0%
closed trades                     51            38
win rate                         25%           21%
avg net / trade                -4.8%         -8.1%
expectancy $/trade            $-1.26        $-1.97
max drawdown                  -23.2%        -21.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $435.99 (-12.8%) | cash $435.99 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 51 | win 13/51 (25%) | avg net -4.8% | realized $-64.01 | expectancy $-1.26/trade
exits: stop 36, trail 15
  (n=51 < 100: noise, not evidence)
last trades:
  Sakura       $20.90 -> $48.56 (+132.3%)  trail  1.2h
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
  Speed        $22.14 -> $17.72 (-20.0%)  stop  1.3h
  BAWSAQ       $21.91 -> $27.10 (+23.7%)  trail  0.8h
  CSI          $22.17 -> $16.28 (-26.6%)  stop  0.2h
  SWJ          $21.88 -> $19.15 (-12.5%)  stop  0.2h
  tinfoil      $21.88 -> $28.30 (+29.3%)  trail  0.3h
  GTA$         $22.06 -> $16.78 (-24.0%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 304, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $424.96 (-15.0%) | cash $424.96 | open 0 | max drawdown -21.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 38 | win 8/38 (21%) | avg net -8.1% | realized $-75.04 | expectancy $-1.97/trade
exits: stop 30, trail 8
  (n=38 < 100: noise, not evidence)
last trades:
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
  FOOD         $21.41 -> $18.94 (-11.6%)  stop  0.3h
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 242, daily_loss_limit 192, setup_rejected:sellers_dominate_now 105, setup_rejected:dumping_now 80, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 20, setup_rejected:operator_cluster 15, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
