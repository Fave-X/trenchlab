# TrenchLab report

Updated: 2026-11-07 23:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           16570
passed SCOUT         40
  killed by SCORE    3
  killed by AUDIT    8
FINAL PASS           29

top kill reasons at first sighting (a pool can have several):
  too_young                    16074
  few_unique_buyers            15558
  liquidity_low                15171
  volume_below_liquidity       11757
  sells_dominate                4620
  wash_churn                    3467
  overheated                    1456
  missing                        466
  too_old                        403
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 939 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   29    -7.5%   -21.9%   -44.7%   -81.8%    45%
SCOUT PASS, killed later     11   +15.6%   +16.6%   -84.2%   +72.1%    36%
KILLED (tracked)           2505    -0.0%    -5.1%   -30.1%    +1.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      16    -93.0%       -      56%
wash_churn                     10    -37.1%       -      50%
too_old                        10     -0.1%     -2.6%     0%
volume_below_liquidity          5     +5.9%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      2    -11.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        13    -73.1%    -92.7%    85%
70-79      15    -33.6%    -66.4%    27%
60-69      10    -29.6%    -41.6%    20%
<60         2    -58.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      127     -2.3%     -2.9%     -7.9%    24%
<15%       26     +1.4%     -4.9%     +7.9%    42%
15-30%      1   +442.6%   +963.4%       -     100%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      128     -1.9%     -2.6%     +0.0%    19%
<20%       29     +5.4%    -19.7%    -94.9%    48%
20%+        6    +24.1%    -99.0%       -      83%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      156     -1.5%     -2.7%     -0.4%    24%
20-40%      4    -41.0%    -99.0%       -     100%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 133 | helius credits today: 6393/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   28    18%    -12.5%   -19.7%   -65.0%
   -6%     20%   28    18%    -12.5%   -19.7%   -65.0%
   -6%     30%   28    21%     -8.0%   -19.7%   -65.0%
  -10%     12%   28    18%    -14.1%   -20.6%   -65.0%
  -10%     20%   28    18%    -14.1%   -20.6%   -65.0%
  -10%     30%   28    21%     -9.6%   -20.6%   -65.0%
  -15%     12%   28    18%    -14.6%   -21.1%   -65.0%
  -15%     20%   28    18%    -14.6%   -21.1%   -65.0%
  -15%     30%   28    21%    -10.1%   -21.1%   -65.0%
  -25%     12%   28    21%    -19.1%   -29.9%   -67.1%
  -25%     20%   28    21%    -21.6%   -30.0%   -76.1%
  -25%     30%   28    21%    -18.8%   -31.0%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -8.0% per trade over n=28
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $475.22       $515.19
return                         -5.0%         +3.0%
closed trades                     14             5
win rate                         21%           20%
avg net / trade                -7.4%        +12.8%
expectancy $/trade            $-1.92        $+3.04
max drawdown                   -9.3%         -5.2%
open now                           2             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $475.22 (-5.0%) | cash $425.92 | open 2 | max drawdown -9.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 14 | win 3/14 (21%) | avg net -7.4% | realized $-26.87 | expectancy $-1.92/trade
exits: stop 10, trail 4
  (n=14 < 100: noise, not evidence)
open:
  TAOLF        cost $23.66  now $26.36 (+11.4%)  held 0.4h
  BLEND        cost $23.55  now $22.94 (-2.6%)  held 0.0h
last trades:
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
  debtdog      $24.92 -> $19.88 (-20.2%)  stop  0.2h
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
  FRODO        $24.01 -> $20.82 (-13.3%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 83, daily_loss_limit 31, cooldown_after_loss 3, max_open_positions 1

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 38, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 12, setup_rejected:sellers_dominate_now 2, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
