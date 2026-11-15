# TrenchLab report

Updated: 2026-11-15 19:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           72956
passed SCOUT         147
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           92

top kill reasons at first sighting (a pool can have several):
  too_young                    71687
  few_unique_buyers            68740
  liquidity_low                67178
  volume_below_liquidity       51572
  sells_dominate               19075
  wash_churn                   15055
  overheated                    6354
  missing                       2355
  too_old                        978
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4254 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   92    -4.2%    -7.8%   -44.0%   -89.9%    60%
SCOUT PASS, killed later     55    +4.3%    +4.2%   -50.6%   -15.3%    49%
KILLED (tracked)          10371    +0.0%   -55.6%   -78.1%    +0.1%    31%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      87    -94.8%    -68.9%    53%
too_old                        34     -0.6%     -0.4%     3%
wash_churn                     25     -1.1%    -71.8%    28%
liquidity_low                  18    -65.5%    -49.8%    50%
volume_below_liquidity          7     -2.8%    +15.3%    43%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        48    -55.0%    -93.8%    73%
70-79      54    -44.7%    -66.7%    52%
60-69      30    -37.4%    -79.9%    47%
<60        15    -30.1%    -15.3%    33%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      482     -0.0%    -11.7%    -35.1%    35%
<15%       99     +0.2%    -11.2%    -24.0%    28%
15-30%     10     -0.6%     -0.7%     +1.0%    40%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      472     +0.0%     -2.3%    -13.9%    28%
<20%      125     -4.7%    -55.2%    -94.9%    44%
20%+       16    +13.0%    -99.0%       -      88%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      590     -0.0%     -5.3%    -17.1%    31%
20-40%     16     -6.5%    -99.0%    -99.1%    75%
40%+        7    -43.5%    -46.3%       -      71%
tokens analysed: 508 | helius credits today: 4953/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   92    25%     -9.0%   -15.8%   -99.7%
   -6%     20%   92    25%     -9.3%   -16.0%   -99.7%
   -6%     30%   92    26%     -7.6%   -17.1%   -99.7%
  -10%     12%   92    27%     -8.9%   -18.6%   -99.7%
  -10%     20%   92    26%     -9.5%   -19.0%   -99.7%
  -10%     30%   92    28%     -7.7%   -19.4%   -99.7%
  -15%     12%   92    29%     -8.6%   -19.8%   -99.7%
  -15%     20%   92    29%     -9.2%   -20.6%   -99.7%
  -15%     30%   92    32%     -7.3%   -20.8%   -99.7%
  -25%     12%   92    34%    -10.6%   -17.4%   -99.7%
  -25%     20%   92    34%    -13.1%   -30.0%   -99.7%
  -25%     30%   92    36%    -11.4%   -30.9%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.3% per trade over n=92
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $405.22       $404.84
return                        -19.0%        -19.0%
closed trades                     57            43
win rate                         25%           21%
avg net / trade                -6.8%         -9.4%
expectancy $/trade            $-1.66        $-2.21
max drawdown                  -23.2%        -25.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $405.22 (-19.0%) | cash $405.22 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 57 | win 14/57 (25%) | avg net -6.8% | realized $-94.78 | expectancy $-1.66/trade
exits: stop 40, trail 17
  (n=57 < 100: noise, not evidence)
last trades:
  tinfoil      $21.88 -> $28.30 (+29.3%)  trail  0.3h
  GTA$         $22.06 -> $16.78 (-24.0%)  stop  0.2h
  billie       $21.80 -> $3.70 (-83.0%)  stop  0.2h
  bill         $20.89 -> $19.84 (-5.0%)  trail  0.3h
  worth        $20.84 -> $13.96 (-33.0%)  stop  0.2h
  Socks        $20.51 -> $18.26 (-11.0%)  stop  0.2h
  WANTED       $20.50 -> $21.41 (+4.4%)  trail  1.7h
  BUTTHOLE     $20.43 -> $17.04 (-16.6%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 351, daily_loss_limit 242, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $404.84 (-19.0%) | cash $404.84 | open 0 | max drawdown -25.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 43 | win 9/43 (21%) | avg net -9.4% | realized $-95.16 | expectancy $-2.21/trade
exits: stop 34, trail 9
  (n=43 < 100: noise, not evidence)
last trades:
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
  bill         $21.25 -> $15.00 (-29.4%)  stop  0.2h
  HYGG         $20.94 -> $24.47 (+16.9%)  trail  1.3h
  ニャジラ         $21.11 -> $13.78 (-34.7%)  stop  0.7h
  Socks        $20.75 -> $17.11 (-17.5%)  stop  0.5h
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 295, daily_loss_limit 211, setup_rejected:sellers_dominate_now 116, setup_rejected:dumping_now 90, setup_rejected:b_bundled 33, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:operator_cluster 15, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
