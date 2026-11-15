# TrenchLab report

Updated: 2026-11-15 05:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           68494
passed SCOUT         140
  killed by SCORE    19
  killed by AUDIT    32
FINAL PASS           89

top kill reasons at first sighting (a pool can have several):
  too_young                    67265
  few_unique_buyers            64587
  liquidity_low                63057
  volume_below_liquidity       48385
  sells_dominate               17996
  wash_churn                   14064
  overheated                    5923
  missing                       2219
  too_old                        951
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 3989 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   89    -3.8%    -7.3%   -43.9%   -90.4%    58%
SCOUT PASS, killed later     51    +4.2%    +3.9%   -55.0%   -15.3%    43%
KILLED (tracked)           9745    +0.0%   -53.4%   -75.2%    -0.2%    31%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      71    -94.8%    -68.9%    54%
too_old                        33     -0.7%     -0.4%     3%
wash_churn                     24     -1.2%    -71.8%    29%
liquidity_low                  17    -62.2%    -49.8%    47%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        45    -55.6%    -94.0%    67%
70-79      53    -44.7%    -66.4%    51%
60-69      29    -35.2%    -99.8%    45%
<60        13    -32.2%    -15.3%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      445     -0.2%    -10.5%    -34.1%    34%
<15%       93     +0.1%    -11.2%    -24.0%    30%
15-30%     10     -0.6%     -0.7%     +1.0%    40%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      446     -0.1%     -2.2%    -12.9%    28%
<20%      108     -3.5%    -55.2%    -94.9%    44%
20%+       16    +17.1%    -99.0%       -      88%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      547     -0.2%     -4.4%    -16.6%    31%
20-40%     16     -4.6%    -99.0%    -99.1%    75%
40%+        7    -43.5%    -46.3%       -      71%
tokens analysed: 466 | helius credits today: 1243/25000

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
equity                       $409.96       $425.14
return                        -18.0%        -15.0%
closed trades                     54            39
win rate                         24%           21%
avg net / trade                -6.8%         -8.6%
expectancy $/trade            $-1.67        $-2.08
max drawdown                  -23.2%        -23.1%
open now                           0             1
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
signals skipped by the sizer/risk rules: already_traded_token 327, daily_loss_limit 242, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $425.14 (-15.0%) | cash $397.77 | open 1 | max drawdown -23.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 39 | win 8/39 (21%) | avg net -8.6% | realized $-81.29 | expectancy $-2.08/trade
exits: stop 31, trail 8
  (n=39 < 100: noise, not evidence)
open:
  HYGG         cost $20.94  now $27.37 (+30.7%)  held 1.2h
last trades:
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
  FOOD         $21.41 -> $18.94 (-11.6%)  stop  0.3h
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
  bill         $21.25 -> $15.00 (-29.4%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 289, daily_loss_limit 208, setup_rejected:sellers_dominate_now 114, setup_rejected:dumping_now 85, setup_rejected:volume_dried_up 30, setup_rejected:top10_concentrated 29, setup_rejected:b_bundled 24, setup_rejected:operator_cluster 15, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
