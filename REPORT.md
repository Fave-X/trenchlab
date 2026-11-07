# TrenchLab report

Updated: 2026-11-07 07:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           11689
passed SCOUT         28
  killed by SCORE    2
  killed by AUDIT    6
FINAL PASS           20

top kill reasons at first sighting (a pool can have several):
  too_young                    11323
  few_unique_buyers            10994
  liquidity_low                10623
  volume_below_liquidity        8228
  sells_dominate                3366
  wash_churn                    2426
  overheated                    1021
  missing                        380
  too_old                        310
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 738 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   20    -5.5%   -17.3%   -44.4%   -66.4%    35%
SCOUT PASS, killed later      8    +6.2%    +6.7%   -86.2%   +72.1%    38%
KILLED (tracked)           1731    -0.0%    -3.4%    -9.7%    +0.5%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_old                        10     +0.2%     -6.7%     0%
wash_churn                      9    -37.1%       -      56%
too_young                       8    -94.0%       -      62%
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
none       84     -2.4%     -9.0%     +4.9%    17%
<15%       22     +0.8%     -2.0%     -0.8%    32%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -1.0%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none       92     -1.9%     -2.0%     +2.6%    10%
<20%       19    +10.5%    -55.2%    -96.6%    53%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      110     -1.7%     -2.9%     +1.8%    17%
20-40%      3    +16.6%    -99.0%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 90 | helius credits today: 1869/25000

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
equity                       $510.25       $543.59
return                         +2.1%         +8.7%
closed trades                      7             1
win rate                         43%          100%
avg net / trade                +6.7%       +123.5%
expectancy $/trade            $+1.46       $+30.88
max drawdown                   -5.4%         -0.9%
open now                           0             2
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
signals skipped by the sizer/risk rules: already_traded_token 55, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $543.59 (+8.7%) | cash $477.57 | open 2 | max drawdown -0.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 1 | win 1/1 (100%) | avg net +123.5% | realized $+30.88 | expectancy $+30.88/trade
exits: trail 1
  (n=1 < 100: noise, not evidence)
open:
  MUTTAPE      cost $26.51  now $39.71 (+49.8%)  held 0.5h
  FUSE         cost $26.80  now $26.31 (-1.8%)  held 0.0h
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 14, setup_rejected:top10_concentrated 10, setup_rejected:dumping_now 3

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
