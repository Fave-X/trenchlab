# TrenchLab report

Updated: 2026-11-07 08:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           11846
passed SCOUT         28
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           20

top kill reasons at first sighting (a pool can have several):
  too_young                    11479
  few_unique_buyers            11130
  liquidity_low                10764
  volume_below_liquidity        8337
  sells_dominate                3400
  wash_churn                    2470
  overheated                    1045
  missing                        380
  too_old                        311
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 746 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   20    -5.5%   -17.3%   -44.4%   -66.4%    35%
SCOUT PASS, killed later      8    +6.2%    +6.7%   -86.2%   +72.1%    38%
KILLED (tracked)           1769    -0.0%    -3.4%    -9.7%    +0.5%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_old                        10     +0.2%     -6.7%     0%
wash_churn                      9    -37.1%       -      56%
too_young                       9    -94.0%       -      56%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -72.7%    -93.4%    64%
70-79      11    -31.2%    -31.9%     9%
60-69       5    -41.2%       -      40%
<60         1    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       85     -2.4%     -8.3%     +4.9%    18%
<15%       23     +0.8%     -2.0%     -0.8%    35%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -1.0%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none       93     -1.9%     -2.0%     +2.6%    11%
<20%       20     +5.4%    -51.7%    -96.6%    55%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      112     -1.6%     -2.8%     +1.8%    19%
20-40%      3    +16.6%    -99.0%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 92 | helius credits today: 2098/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   20    20%    -10.7%   -19.3%   -65.0%
   -6%     20%   20    20%    -10.7%   -19.3%   -65.0%
   -6%     30%   20    25%     -4.3%   -19.3%   -65.0%
  -10%     12%   20    20%    -12.9%   -20.6%   -65.0%
  -10%     20%   20    20%    -12.9%   -20.6%   -65.0%
  -10%     30%   20    25%     -6.6%   -20.6%   -65.0%
  -15%     12%   20    20%    -13.2%   -21.2%   -65.0%
  -15%     20%   20    20%    -13.2%   -21.2%   -65.0%
  -15%     30%   20    25%     -6.9%   -21.2%   -65.0%
  -25%     12%   20    25%    -15.0%   -25.3%   -67.1%
  -25%     20%   20    25%    -18.5%   -29.5%   -76.1%
  -25%     30%   20    25%    -14.6%   -30.4%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -4.3% per trade over n=20
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $510.25       $525.27
return                         +2.1%         +5.1%
closed trades                      7             2
win rate                         43%           50%
avg net / trade                +6.7%        +51.9%
expectancy $/trade            $+1.46       $+12.83
max drawdown                   -5.4%         -3.4%
open now                           0             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $510.25 (+2.1%) | cash $510.25 | open 0 | max drawdown -5.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 7 | win 3/7 (43%) | avg net +6.7% | realized $+10.25 | expectancy $+1.46/trade
exits: trail 4, stop 3
  (n=7 < 100: noise, not evidence)
last trades:
  RM           $25.00 -> $14.03 (-43.9%)  stop  1.0h
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
signals skipped by the sizer/risk rules: already_traded_token 58, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $525.27 (+5.1%) | cash $498.85 | open 1 | max drawdown -3.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 2 | win 1/2 (50%) | avg net +51.9% | realized $+25.65 | expectancy $+12.83/trade
exits: trail 1, stop 1
  (n=2 < 100: noise, not evidence)
open:
  FUSE         cost $26.80  now $26.42 (-1.4%)  held 0.5h
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 14, setup_rejected:top10_concentrated 12, setup_rejected:dumping_now 3, setup_rejected:sellers_dominate_now 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
