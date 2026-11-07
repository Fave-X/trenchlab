# TrenchLab report

Updated: 2026-11-07 19:12 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           15337
passed SCOUT         35
  killed by SCORE    3
  killed by AUDIT    8
FINAL PASS           24

top kill reasons at first sighting (a pool can have several):
  too_young                    14879
  few_unique_buyers            14386
  liquidity_low                14026
  volume_below_liquidity       10845
  sells_dominate                4296
  wash_churn                    3210
  overheated                    1360
  missing                        433
  too_old                        378
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 895 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   24    -5.7%   -17.3%   -44.7%   -81.8%    46%
SCOUT PASS, killed later     11   +15.6%   +16.6%   -84.2%   +72.1%    36%
KILLED (tracked)           2294    -0.0%    -5.2%   -25.9%    +1.2%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      14    -89.1%       -      57%
too_old                        10     -0.1%     -0.4%     0%
wash_churn                      9    -37.1%       -      56%
volume_below_liquidity          5     +1.5%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      2    -11.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        12    -72.7%    -93.2%    75%
70-79      14    -31.2%    -72.1%    29%
60-69       7    -56.9%    -41.6%    29%
<60         2    -58.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      108     -2.4%     -7.3%     +2.6%    22%
<15%       26     +0.6%     -2.6%     +3.5%    42%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        9     -0.3%     -1.0%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      114     -1.8%     -2.6%     +2.6%    17%
<20%       25     +7.5%    -19.7%    -94.9%    52%
20%+        5    +16.6%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      137     -1.5%     -2.6%     +1.1%    23%
20-40%      4    -41.0%    -99.0%       -     100%
40%+        3   +227.1%   +963.4%       -       0%
tokens analysed: 118 | helius credits today: 4620/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   24    17%    -12.8%   -20.0%   -65.0%
   -6%     20%   24    17%    -12.8%   -20.0%   -65.0%
   -6%     30%   24    21%     -7.5%   -20.0%   -65.0%
  -10%     12%   24    17%    -14.6%   -21.1%   -65.0%
  -10%     20%   24    17%    -14.6%   -21.1%   -65.0%
  -10%     30%   24    21%     -9.3%   -21.1%   -65.0%
  -15%     12%   24    17%    -15.1%   -21.3%   -65.0%
  -15%     20%   24    17%    -15.1%   -21.3%   -65.0%
  -15%     30%   24    21%     -9.8%   -21.3%   -65.0%
  -25%     12%   24    21%    -18.5%   -29.5%   -67.1%
  -25%     20%   24    21%    -21.3%   -29.9%   -76.1%
  -25%     30%   24    21%    -18.1%   -31.0%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -7.5% per trade over n=24
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $487.88       $522.88
return                         -2.4%         +4.6%
closed trades                     11             3
win rate                         27%           33%
avg net / trade                -3.9%        +31.2%
expectancy $/trade            $-1.10        $+7.63
max drawdown                   -6.1%         -3.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $487.88 (-2.4%) | cash $487.88 | open 0 | max drawdown -6.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 11 | win 3/11 (27%) | avg net -3.9% | realized $-12.12 | expectancy $-1.10/trade
exits: stop 7, trail 4
  (n=11 < 100: noise, not evidence)
last trades:
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
  debtdog      $24.92 -> $19.88 (-20.2%)  stop  0.2h
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 79, daily_loss_limit 31, max_open_positions 1

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 32, setup_rejected:top10_concentrated 24, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 8, setup_rejected:sellers_dominate_now 1, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
