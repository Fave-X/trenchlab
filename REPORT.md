# TrenchLab report

Updated: 2026-11-07 14:22 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           13769
passed SCOUT         31
  killed by SCORE    3
  killed by AUDIT    6
FINAL PASS           22

top kill reasons at first sighting (a pool can have several):
  too_young                    13361
  few_unique_buyers            12898
  liquidity_low                12550
  volume_below_liquidity        9695
  sells_dominate                3863
  wash_churn                    2904
  overheated                    1247
  missing                        401
  too_old                        337
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 846 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   22    -5.5%   -13.3%   -44.4%   -85.9%    41%
SCOUT PASS, killed later      9   +17.2%   +16.6%   -86.2%   +72.1%    33%
KILLED (tracked)           2071    +0.0%    -4.0%   -22.2%    +1.1%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      13    -89.1%       -      54%
too_old                        10     -0.1%     -6.7%     0%
wash_churn                      9    -37.1%       -      56%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%
overheated                      2       -         -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        11    -72.7%    -93.2%    73%
70-79      11    -29.7%    -31.9%    18%
60-69       7    -56.9%       -      29%
<60         2    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none       98     -2.4%     -7.6%     +2.6%    20%
<15%       25     +0.8%     -1.1%     +3.5%    36%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -1.0%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none      106     -1.9%     -2.3%     +2.6%    13%
<20%       22     +7.5%    -44.7%    -94.9%    59%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      127     -1.5%     -2.5%     +1.1%    21%
20-40%      3    +16.6%    -99.0%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 106 | helius credits today: 3357/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   22    18%    -11.9%   -19.3%   -65.0%
   -6%     20%   22    18%    -11.9%   -19.3%   -65.0%
   -6%     30%   22    23%     -6.1%   -19.3%   -65.0%
  -10%     12%   22    18%    -13.9%   -20.6%   -65.0%
  -10%     20%   22    18%    -13.9%   -20.6%   -65.0%
  -10%     30%   22    23%     -8.2%   -20.6%   -65.0%
  -15%     12%   22    18%    -14.4%   -21.2%   -65.0%
  -15%     20%   22    18%    -14.4%   -21.2%   -65.0%
  -15%     30%   22    23%     -8.7%   -21.2%   -65.0%
  -25%     12%   22    23%    -16.4%   -29.2%   -67.1%
  -25%     20%   22    23%    -19.6%   -29.5%   -76.1%
  -25%     30%   22    23%    -16.0%   -30.4%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -6.1% per trade over n=22
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $498.48       $522.88
return                         -0.3%         +4.6%
closed trades                      9             3
win rate                         33%           33%
avg net / trade                +0.0%        +31.2%
expectancy $/trade            $-0.17        $+7.63
max drawdown                   -5.4%         -3.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $498.48 (-0.3%) | cash $498.48 | open 0 | max drawdown -5.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 9 | win 3/9 (33%) | avg net +0.0% | realized $-1.52 | expectancy $-0.17/trade
exits: stop 5, trail 4
  (n=9 < 100: noise, not evidence)
last trades:
  APPLEPAID    $24.45 -> $22.38 (-8.5%)  trail  0.7h
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
signals skipped by the sizer/risk rules: already_traded_token 67, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $522.88 (+4.6%) | cash $522.88 | open 0 | max drawdown -3.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 3 | win 1/3 (33%) | avg net +31.2% | realized $+22.88 | expectancy $+7.63/trade
exits: stop 2, trail 1
  (n=3 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 32, setup_rejected:top10_concentrated 16, setup_rejected:volume_dried_up 14, setup_rejected:dumping_now 6, setup_rejected:sellers_dominate_now 1, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
