# TrenchLab report

Updated: 2026-11-15 11:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           70453
passed SCOUT         144
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           89

top kill reasons at first sighting (a pool can have several):
  too_young                    69206
  few_unique_buyers            66391
  liquidity_low                64840
  volume_below_liquidity       49731
  sells_dominate               18510
  wash_churn                   14538
  overheated                    6120
  missing                       2299
  too_old                        964
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4120 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   89    -3.8%    -7.3%   -44.0%   -89.9%    60%
SCOUT PASS, killed later     55    +4.3%    +4.6%   -49.0%   -15.3%    44%
KILLED (tracked)          10019    +0.0%   -55.2%   -76.8%    -0.2%    31%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      80    -94.9%    -68.9%    55%
too_old                        34     -0.7%     -0.4%     3%
wash_churn                     24     -1.1%    -71.8%    29%
liquidity_low                  17    -62.2%    -49.8%    47%
volume_below_liquidity          7     +1.5%    +15.3%    43%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        48    -52.8%    -93.8%    67%
70-79      53    -42.3%    -66.4%    51%
60-69      29    -37.4%    -79.9%    48%
<60        14    -30.1%    -15.3%    29%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      468     -0.2%    -10.9%    -37.0%    34%
<15%       95     +0.1%    -11.2%    -24.0%    29%
15-30%     10     -0.6%     -0.7%     +1.0%    40%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      462     -0.0%     -2.3%    -14.9%    27%
<20%      118     -4.7%    -55.2%    -94.9%    43%
20%+       15    +16.6%    -99.0%       -      93%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      572     -0.2%     -5.1%    -20.4%    31%
20-40%     16     -6.5%    -99.0%    -99.1%    75%
40%+        7    -43.5%    -46.3%       -      71%
tokens analysed: 490 | helius credits today: 3119/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   89    25%     -9.0%   -17.1%   -99.7%
   -6%     20%   89    25%     -9.3%   -17.1%   -99.7%
   -6%     30%   89    26%     -7.6%   -17.1%   -99.7%
  -10%     12%   89    27%     -8.9%   -19.3%   -99.7%
  -10%     20%   89    26%     -9.5%   -19.5%   -99.7%
  -10%     30%   89    28%     -7.6%   -19.6%   -99.7%
  -15%     12%   89    29%     -8.3%   -19.9%   -99.7%
  -15%     20%   89    29%     -8.8%   -20.4%   -99.7%
  -15%     30%   89    31%     -6.9%   -20.7%   -99.7%
  -25%     12%   89    34%    -10.5%   -17.1%   -99.7%
  -25%     20%   89    34%    -12.9%   -29.9%   -99.7%
  -25%     30%   89    36%    -11.1%   -30.9%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -6.9% per trade over n=89
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $409.96       $414.90
return                        -18.0%        -17.0%
closed trades                     54            41
win rate                         24%           22%
avg net / trade                -6.8%         -8.7%
expectancy $/trade            $-1.67        $-2.08
max drawdown                  -23.2%        -23.7%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $409.96 (-18.0%) | cash $409.96 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 54 | win 13/54 (24%) | avg net -6.8% | realized $-90.04 | expectancy $-1.67/trade
exits: stop 38, trail 16
  (n=54 < 100: noise, not evidence)
last trades:
  BAWSAQ       $21.91 -> $27.10 (+23.7%)  trail  0.8h
  CSI          $22.17 -> $16.28 (-26.6%)  stop  0.2h
  SWJ          $21.88 -> $19.15 (-12.5%)  stop  0.2h
  tinfoil      $21.88 -> $28.30 (+29.3%)  trail  0.3h
  GTA$         $22.06 -> $16.78 (-24.0%)  stop  0.2h
  billie       $21.80 -> $3.70 (-83.0%)  stop  0.2h
  bill         $20.89 -> $19.84 (-5.0%)  trail  0.3h
  worth        $20.84 -> $13.96 (-33.0%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 332, daily_loss_limit 242, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $414.90 (-17.0%) | cash $414.90 | open 0 | max drawdown -23.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 41 | win 9/41 (22%) | avg net -8.7% | realized $-85.10 | expectancy $-2.08/trade
exits: stop 32, trail 9
  (n=41 < 100: noise, not evidence)
last trades:
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
  FOOD         $21.41 -> $18.94 (-11.6%)  stop  0.3h
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
  bill         $21.25 -> $15.00 (-29.4%)  stop  0.2h
  HYGG         $20.94 -> $24.47 (+16.9%)  trail  1.3h
  ニャジラ         $21.11 -> $13.78 (-34.7%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 293, daily_loss_limit 208, setup_rejected:sellers_dominate_now 114, setup_rejected:dumping_now 85, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 24, setup_rejected:operator_cluster 15, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
