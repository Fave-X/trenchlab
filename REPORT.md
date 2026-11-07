# TrenchLab report

Updated: 2026-11-07 23:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           16734
passed SCOUT         40
  killed by SCORE    3
  killed by AUDIT    8
FINAL PASS           29

top kill reasons at first sighting (a pool can have several):
  too_young                    16237
  few_unique_buyers            15712
  liquidity_low                15323
  volume_below_liquidity       11875
  sells_dominate                4658
  wash_churn                    3499
  overheated                    1471
  missing                        471
  too_old                        403
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 944 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   29    -6.6%   -21.6%   -44.7%   -81.8%    45%
SCOUT PASS, killed later     11   +15.6%   +16.6%   -84.2%   +72.1%    36%
KILLED (tracked)           2534    -0.0%    -5.2%   -26.2%    +1.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      17    -93.0%       -      53%
wash_churn                     10    -37.1%       -      50%
too_old                        10     -0.1%     -2.6%     0%
volume_below_liquidity          5     +5.9%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      2    -11.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        14    -73.1%    -92.7%    79%
70-79      14    -33.6%    -66.4%    29%
60-69      10    -29.6%    -41.6%    20%
<60         2    -58.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      128     -2.2%     -2.8%     -7.9%    23%
<15%       27     +0.9%     -4.6%     +7.9%    41%
15-30%      2   +442.6%   +963.4%       -      50%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      130     -1.9%     -2.3%     +0.0%    18%
<20%       29     +5.4%    -19.7%    -94.9%    48%
20%+        7    +24.1%    -99.0%       -      71%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      158     -1.5%     -2.5%     -0.4%    24%
20-40%      5    -41.0%    -99.0%       -      80%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 135 | helius credits today: 6551/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   29    17%    -12.1%   -19.5%   -65.0%
   -6%     20%   29    17%    -12.1%   -19.5%   -65.0%
   -6%     30%   29    21%     -7.7%   -19.5%   -65.0%
  -10%     12%   29    17%    -13.6%   -20.1%   -65.0%
  -10%     20%   29    17%    -13.6%   -20.1%   -65.0%
  -10%     30%   29    21%     -9.3%   -20.1%   -65.0%
  -15%     12%   29    17%    -14.2%   -21.0%   -65.0%
  -15%     20%   29    17%    -14.2%   -21.0%   -65.0%
  -15%     30%   29    21%     -9.8%   -21.0%   -65.0%
  -25%     12%   29    21%    -18.5%   -29.9%   -67.1%
  -25%     20%   29    21%    -20.9%   -29.9%   -76.1%
  -25%     30%   29    21%    -18.1%   -31.0%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -7.7% per trade over n=29
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $479.33       $515.19
return                         -4.1%         +3.0%
closed trades                     15             5
win rate                         27%           20%
avg net / trade                -5.2%        +12.8%
expectancy $/trade            $-1.40        $+3.04
max drawdown                   -9.3%         -5.2%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $479.33 (-4.1%) | cash $455.52 | open 1 | max drawdown -9.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 15 | win 4/15 (27%) | avg net -5.2% | realized $-20.93 | expectancy $-1.40/trade
exits: stop 10, trail 5
  (n=15 < 100: noise, not evidence)
open:
  BLEND        cost $23.55  now $23.81 (+1.1%)  held 0.5h
last trades:
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
  debtdog      $24.92 -> $19.88 (-20.2%)  stop  0.2h
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
  FRODO        $24.01 -> $20.82 (-13.3%)  stop  0.3h
  TAOLF        $23.66 -> $29.60 (+25.1%)  trail  0.8h
signals skipped by the sizer/risk rules: already_traded_token 84, daily_loss_limit 31, cooldown_after_loss 3, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $515.19 (+3.0%) | cash $515.19 | open 0 | max drawdown -5.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 5 | win 1/5 (20%) | avg net +12.8% | realized $+15.19 | expectancy $+3.04/trade
exits: stop 4, trail 1
  (n=5 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 43, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 12, setup_rejected:sellers_dominate_now 2, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
