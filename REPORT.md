# TrenchLab report

Updated: 2026-11-08 01:02 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           17198
passed SCOUT         44
  killed by SCORE    5
  killed by AUDIT    8
FINAL PASS           31

top kill reasons at first sighting (a pool can have several):
  too_young                    16698
  few_unique_buyers            16152
  liquidity_low                15749
  volume_below_liquidity       12195
  sells_dominate                4775
  wash_churn                    3604
  overheated                    1521
  missing                        480
  too_old                        405
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 975 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   31    -5.7%   -21.3%   -46.5%   -85.9%    45%
SCOUT PASS, killed later     13    +7.3%   +14.1%   -84.2%   +72.1%    31%
KILLED (tracked)           2649    -0.0%    -5.4%   -22.3%    +1.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      17    -89.1%       -      59%
wash_churn                     10    -37.1%       -      50%
too_old                        10     -0.1%     -2.6%     0%
volume_below_liquidity          5     +5.9%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      2    -11.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        15    -73.1%    -93.2%    73%
70-79      14    -33.6%    -66.4%    29%
60-69      11    -49.8%    -41.6%    27%
<60         4    -58.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      132     -2.3%     -7.3%     -7.9%    23%
<15%       27     +1.4%     -4.9%     +7.8%    41%
15-30%      2   +260.4%   +963.4%       -     100%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      132     -1.9%     -2.7%     +0.0%    19%
<20%       31     +3.4%    -44.7%    -96.6%    45%
20%+        7    +31.6%    -99.0%       -      86%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      162     -1.5%     -2.8%     -0.4%    24%
20-40%      5    +16.6%    -99.0%       -     100%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 138 | helius credits today: 228/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   30    17%    -12.4%   -19.7%   -65.0%
   -6%     20%   30    17%    -12.6%   -19.7%   -65.0%
   -6%     30%   30    20%     -8.4%   -19.7%   -65.0%
  -10%     12%   30    17%    -13.9%   -20.2%   -65.0%
  -10%     20%   30    17%    -14.0%   -20.2%   -65.0%
  -10%     30%   30    20%     -9.8%   -20.2%   -65.0%
  -15%     12%   30    17%    -14.4%   -20.9%   -65.0%
  -15%     20%   30    17%    -14.5%   -20.9%   -65.0%
  -15%     30%   30    20%    -10.3%   -20.9%   -65.0%
  -25%     12%   30    20%    -19.1%   -29.9%   -67.1%
  -25%     20%   30    20%    -21.5%   -30.0%   -76.1%
  -25%     30%   30    20%    -18.9%   -31.0%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -8.4% per trade over n=30
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $473.35       $512.58
return                         -5.3%         +2.5%
closed trades                     16             6
win rate                         25%           17%
avg net / trade                -6.1%         +9.0%
expectancy $/trade            $-1.60        $+2.10
max drawdown                   -9.3%         -5.7%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $473.35 (-5.3%) | cash $450.86 | open 1 | max drawdown -9.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 16 | win 4/16 (25%) | avg net -6.1% | realized $-25.59 | expectancy $-1.60/trade
exits: stop 11, trail 5
  (n=16 < 100: noise, not evidence)
open:
  BLEND        cost $23.55  now $22.49 (-4.5%)  held 1.9h
last trades:
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
  debtdog      $24.92 -> $19.88 (-20.2%)  stop  0.2h
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
  FRODO        $24.01 -> $20.82 (-13.3%)  stop  0.3h
  TAOLF        $23.66 -> $29.60 (+25.1%)  trail  0.8h
  CLAUDIA      $24.09 -> $19.43 (-19.3%)  stop  0.5h
signals skipped by the sizer/risk rules: already_traded_token 96, daily_loss_limit 31, cooldown_after_loss 4, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $512.58 (+2.5%) | cash $512.58 | open 0 | max drawdown -5.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 6 | win 1/6 (17%) | avg net +9.0% | realized $+12.58 | expectancy $+2.10/trade
exits: stop 5, trail 1
  (n=6 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
  SIZE         $25.99 -> $21.47 (-17.4%)  stop  0.2h
  TAOLF        $25.76 -> $23.15 (-10.1%)  stop  0.0h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 53, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 12, setup_rejected:sellers_dominate_now 2, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
