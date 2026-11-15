# TrenchLab report

Updated: 2026-11-15 16:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           71892
passed SCOUT         146
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           91

top kill reasons at first sighting (a pool can have several):
  too_young                    70633
  few_unique_buyers            67721
  liquidity_low                66172
  volume_below_liquidity       50762
  sells_dominate               18817
  wash_churn                   14855
  overheated                    6265
  missing                       2336
  too_old                        972
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4205 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   91    -3.8%    -7.3%   -43.9%   -89.9%    58%
SCOUT PASS, killed later     55    +4.3%    +4.4%   -50.6%   -15.3%    47%
KILLED (tracked)          10241    +0.0%   -55.7%   -77.6%    +0.1%    31%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      86    -95.0%    -68.9%    52%
too_old                        34     -0.6%     -0.4%     3%
wash_churn                     24     -1.1%    -71.8%    29%
liquidity_low                  18    -62.2%    -49.8%    50%
volume_below_liquidity          7     -2.8%    +15.3%    43%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        48    -55.0%    -93.8%    71%
70-79      54    -42.3%    -66.7%    50%
60-69      29    -37.4%    -79.9%    48%
<60        15    -30.1%    -15.3%    27%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      479     -0.0%    -11.7%    -35.1%    34%
<15%       96     +0.2%    -11.2%    -24.0%    29%
15-30%     10     -0.6%     -0.7%     +1.0%    40%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      470     +0.0%     -2.3%    -13.9%    27%
<20%      121     -5.9%    -55.4%    -94.9%    44%
20%+       16    +13.0%    -99.0%       -      88%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      584     -0.0%     -5.5%    -17.1%    30%
20-40%     16     -6.5%    -99.0%    -99.1%    75%
40%+        7    -43.5%    -46.3%       -      71%
tokens analysed: 502 | helius credits today: 4316/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   91    25%     -8.9%   -14.5%   -99.7%
   -6%     20%   91    25%     -9.2%   -15.0%   -99.7%
   -6%     30%   91    26%     -7.5%   -17.1%   -99.7%
  -10%     12%   91    27%     -8.8%   -18.7%   -99.7%
  -10%     20%   91    26%     -9.5%   -19.3%   -99.7%
  -10%     30%   91    29%     -7.6%   -19.5%   -99.7%
  -15%     12%   91    30%     -8.5%   -19.9%   -99.7%
  -15%     20%   91    30%     -8.9%   -20.4%   -99.7%
  -15%     30%   91    32%     -7.0%   -20.7%   -99.7%
  -25%     12%   91    34%    -10.6%   -17.1%   -99.7%
  -25%     20%   91    34%    -12.9%   -29.9%   -99.7%
  -25%     30%   91    36%    -11.1%   -30.9%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.0% per trade over n=91
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $408.62       $404.84
return                        -18.3%        -19.0%
closed trades                     56            43
win rate                         25%           21%
avg net / trade                -6.7%         -9.4%
expectancy $/trade            $-1.63        $-2.21
max drawdown                  -23.2%        -25.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $408.62 (-18.3%) | cash $408.62 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 56 | win 14/56 (25%) | avg net -6.7% | realized $-91.38 | expectancy $-1.63/trade
exits: stop 39, trail 17
  (n=56 < 100: noise, not evidence)
last trades:
  SWJ          $21.88 -> $19.15 (-12.5%)  stop  0.2h
  tinfoil      $21.88 -> $28.30 (+29.3%)  trail  0.3h
  GTA$         $22.06 -> $16.78 (-24.0%)  stop  0.2h
  billie       $21.80 -> $3.70 (-83.0%)  stop  0.2h
  bill         $20.89 -> $19.84 (-5.0%)  trail  0.3h
  worth        $20.84 -> $13.96 (-33.0%)  stop  0.2h
  Socks        $20.51 -> $18.26 (-11.0%)  stop  0.2h
  WANTED       $20.50 -> $21.41 (+4.4%)  trail  1.7h
signals skipped by the sizer/risk rules: already_traded_token 349, daily_loss_limit 242, cooldown_after_loss 11, max_open_positions 5

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 293, daily_loss_limit 208, setup_rejected:sellers_dominate_now 114, setup_rejected:dumping_now 90, setup_rejected:b_bundled 33, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:operator_cluster 15, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
