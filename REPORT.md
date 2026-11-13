# TrenchLab report

Updated: 2026-11-13 14:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           56814
passed SCOUT         119
  killed by SCORE    15
  killed by AUDIT    25
FINAL PASS           79

top kill reasons at first sighting (a pool can have several):
  too_young                    55709
  few_unique_buyers            53555
  liquidity_low                52560
  volume_below_liquidity       40386
  sells_dominate               14883
  wash_churn                   11466
  overheated                    4881
  missing                       1506
  too_old                        878
  rc_danger                       12

OUTCOMES (median price change from first sighting / first pass; 3223 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   79    -3.7%    -7.3%   -44.0%   -92.1%    58%
SCOUT PASS, killed later     40    +4.6%    +1.3%   -52.8%   +22.4%    45%
KILLED (tracked)           8377    +0.0%   -43.6%   -68.7%    -0.1%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      55    -94.8%    -71.7%    55%
too_old                        27     -0.4%     -0.4%     4%
liquidity_low                  16    -40.0%    -49.8%    50%
wash_churn                     15    +11.9%    -71.8%    33%
volume_below_liquidity          6     +1.5%    +15.3%    50%
overheated                      4    -12.8%    -79.6%    75%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        39    -63.7%    -94.5%    74%
70-79      44    -39.9%    -65.9%    45%
60-69      25    -32.0%    -99.8%    48%
<60        11    -32.2%    +22.4%    27%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      378     -0.1%    -10.9%    -20.4%    34%
<15%       76     +0.1%    -12.1%    -24.2%    34%
15-30%      9     -1.0%     -1.3%     +1.0%    33%
30%+       17     -0.3%     -0.3%     +2.6%     6%
bundled     n   +1h med   +4h med  +24h med   rug%
none      376     -0.2%     -2.8%    -11.3%    28%
<20%       91     -0.8%    -51.5%    -96.6%    46%
20%+       13    +16.6%    -99.0%       -      92%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      462     -0.2%     -6.6%    -12.4%    31%
20-40%     14     -4.6%    -99.0%    -99.1%    79%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 386 | helius credits today: 2396/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   79    24%     -9.8%   -17.1%   -99.7%
   -6%     20%   79    24%    -10.0%   -17.1%   -99.7%
   -6%     30%   79    25%     -8.0%   -17.5%   -99.7%
  -10%     12%   79    27%     -9.5%   -19.3%   -99.7%
  -10%     20%   79    25%    -10.1%   -19.5%   -99.7%
  -10%     30%   79    28%     -7.9%   -19.6%   -99.7%
  -15%     12%   79    28%     -9.1%   -19.9%   -99.7%
  -15%     20%   79    28%     -9.9%   -20.4%   -99.7%
  -15%     30%   79    30%     -7.7%   -20.7%   -99.7%
  -25%     12%   79    33%    -10.7%   -17.1%   -99.7%
  -25%     20%   79    33%    -13.2%   -29.7%   -99.7%
  -25%     30%   79    35%    -11.1%   -30.1%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.7% per trade over n=79
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $442.70       $450.43
return                        -11.5%         -9.9%
closed trades                     45            36
win rate                         24%           22%
avg net / trade                -4.8%         -5.4%
expectancy $/trade            $-1.27        $-1.38
max drawdown                  -23.2%        -21.7%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $442.70 (-11.5%) | cash $442.70 | open 0 | max drawdown -23.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 45 | win 11/45 (24%) | avg net -4.8% | realized $-57.30 | expectancy $-1.27/trade
exits: stop 32, trail 13
  (n=45 < 100: noise, not evidence)
last trades:
  AIB          $21.42 -> $17.45 (-18.6%)  stop  0.2h
  MAX          $21.22 -> $16.96 (-20.1%)  stop  0.2h
  BITCOINU     $21.01 -> $11.81 (-43.8%)  stop  0.2h
  plumber      $20.55 -> $13.36 (-35.0%)  stop  0.2h
  AI           $20.55 -> $18.01 (-12.4%)  stop  0.3h
  FOOD         $20.06 -> $36.70 (+83.0%)  trail  1.0h
  Sakura       $20.90 -> $48.56 (+132.3%)  trail  1.2h
  FASTMOON     $22.28 -> $19.42 (-12.8%)  stop  1.3h
signals skipped by the sizer/risk rules: already_traded_token 247, daily_loss_limit 226, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $450.43 (-9.9%) | cash $450.43 | open 0 | max drawdown -21.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 36 | win 8/36 (22%) | avg net -5.4% | realized $-49.57 | expectancy $-1.38/trade
exits: stop 28, trail 8
  (n=36 < 100: noise, not evidence)
last trades:
  NIHAONOON    $22.04 -> $19.02 (-13.7%)  stop  0.3h
  AIB          $21.89 -> $22.83 (+4.3%)  trail  0.8h
  FLC          $21.93 -> $19.19 (-12.5%)  stop  0.2h
  Huang        $21.80 -> $15.36 (-29.5%)  stop  0.5h
  AI           $21.47 -> $23.90 (+11.3%)  trail  0.3h
  plumber      $21.60 -> $17.86 (-17.3%)  stop  0.7h
  FOOD         $21.41 -> $18.94 (-11.6%)  stop  0.3h
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 201, daily_loss_limit 118, setup_rejected:sellers_dominate_now 87, setup_rejected:dumping_now 55, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 27, setup_rejected:b_bundled 13, setup_rejected:operator_cluster 7, setup_rejected:b_received 7, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
