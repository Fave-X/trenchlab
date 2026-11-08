# TrenchLab report

Updated: 2026-11-08 02:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           17738
passed SCOUT         48
  killed by SCORE    6
  killed by AUDIT    9
FINAL PASS           33

top kill reasons at first sighting (a pool can have several):
  too_young                    17235
  few_unique_buyers            16668
  liquidity_low                16246
  volume_below_liquidity       12582
  sells_dominate                4918
  wash_churn                    3695
  overheated                    1559
  missing                        499
  too_old                        406
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 995 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   33    -6.6%   -21.9%   -48.2%   -81.8%    45%
SCOUT PASS, killed later     15    +7.3%    +4.2%   -84.2%   +72.1%    27%
KILLED (tracked)           2745    -0.1%    -7.1%   -24.2%    +1.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      17    -89.1%       -      59%
wash_churn                     10    -37.1%       -      50%
too_old                        10     -0.1%     -2.6%     0%
volume_below_liquidity          5     +5.9%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      3    -11.0%       -      33%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        15    -73.1%    -93.2%    80%
70-79      18    -33.6%    -39.0%    22%
60-69      10    -53.3%    -41.6%    30%
<60         5    -58.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      139     -2.4%     -8.5%     -4.7%    24%
<15%       29     +0.9%     -8.5%     +7.8%    38%
15-30%      2   +260.4%   +963.4%       -     100%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      137     -1.9%     -2.9%     +0.5%    20%
<20%       34     +3.2%    -46.5%    -96.6%    41%
20%+        8    +31.6%    -99.0%       -      88%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      170     -1.9%     -3.0%     -0.4%    25%
20-40%      6    +16.6%    -99.0%       -      83%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 147 | helius credits today: 972/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   33    18%    -12.4%   -19.9%   -65.0%
   -6%     20%   33    18%    -12.7%   -19.9%   -65.0%
   -6%     30%   33    21%     -8.9%   -19.9%   -65.0%
  -10%     12%   33    18%    -13.8%   -20.4%   -65.0%
  -10%     20%   33    18%    -14.2%   -20.4%   -65.0%
  -10%     30%   33    21%    -10.3%   -20.4%   -65.0%
  -15%     12%   33    18%    -14.2%   -20.7%   -65.0%
  -15%     20%   33    18%    -15.1%   -21.0%   -65.0%
  -15%     30%   33    21%    -11.3%   -21.0%   -65.0%
  -25%     12%   33    21%    -19.6%   -29.9%   -67.1%
  -25%     20%   33    21%    -22.5%   -30.1%   -76.1%
  -25%     30%   33    21%    -20.2%   -31.0%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -8.9% per trade over n=33
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $463.28       $504.19
return                         -7.3%         +0.8%
closed trades                     18             7
win rate                         22%           14%
avg net / trade                -8.0%         +3.0%
expectancy $/trade            $-2.04        $+0.60
max drawdown                  -10.8%         -7.2%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $463.28 (-7.3%) | cash $463.28 | open 0 | max drawdown -10.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 18 | win 4/18 (22%) | avg net -8.0% | realized $-36.72 | expectancy $-2.04/trade
exits: stop 13, trail 5
  (n=18 < 100: noise, not evidence)
last trades:
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
  FRODO        $24.01 -> $20.82 (-13.3%)  stop  0.3h
  TAOLF        $23.66 -> $29.60 (+25.1%)  trail  0.8h
  CLAUDIA      $24.09 -> $19.43 (-19.3%)  stop  0.5h
  BLEND        $23.55 -> $20.73 (-12.0%)  stop  2.7h
  invest       $23.69 -> $15.38 (-35.1%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 96, daily_loss_limit 36, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $504.19 (+0.8%) | cash $504.19 | open 0 | max drawdown -7.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 7 | win 1/7 (14%) | avg net +3.0% | realized $+4.19 | expectancy $+0.60/trade
exits: stop 6, trail 1
  (n=7 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
  TAOLF        $25.76 -> $23.15 (-10.1%)  stop  0.0h
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 53, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 14, setup_rejected:sellers_dominate_now 2, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
