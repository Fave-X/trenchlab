# TrenchLab report

Updated: 2026-11-07 15:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           14146
passed SCOUT         32
  killed by SCORE    3
  killed by AUDIT    6
FINAL PASS           23

top kill reasons at first sighting (a pool can have several):
  too_young                    13733
  few_unique_buyers            13253
  liquidity_low                12904
  volume_below_liquidity        9984
  sells_dominate                3963
  wash_churn                    2967
  overheated                    1274
  missing                        409
  too_old                        339
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 856 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   23    -5.6%   -10.8%   -44.4%   -85.9%    39%
SCOUT PASS, killed later      9   +17.2%   +16.6%   -86.2%   +72.1%    33%
KILLED (tracked)           2123    +0.0%    -4.0%   -22.3%    +1.3%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      13    -89.1%       -      54%
too_old                        10     -0.1%     -0.4%     0%
wash_churn                      9    -37.1%       -      56%
volume_below_liquidity          4     +1.5%     -4.6%    50%
liquidity_low                   3    -86.9%       -     100%
overheated                      2     +0.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        12    -72.7%    -93.2%    67%
70-79      12    -29.7%    -31.9%    17%
60-69       6    -56.9%       -      33%
<60         2    -32.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      103     -2.3%     -7.3%     +4.9%    20%
<15%       25     +0.8%     -1.1%     +3.5%    40%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        8     -0.8%     -1.0%     +0.8%    12%
bundled     n   +1h med   +4h med  +24h med   rug%
none      111     -1.7%     -2.3%     +2.6%    14%
<20%       22     +7.5%    -44.7%    -94.9%    59%
20%+        4    +24.1%    -99.0%       -      75%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      132     -1.4%     -2.5%     +2.6%    22%
20-40%      3    +16.6%    -99.0%       -     100%
40%+        2   +442.6%   +963.4%       -       0%
tokens analysed: 111 | helius credits today: 3763/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   23    17%    -12.3%   -19.9%   -65.0%
   -6%     20%   23    17%    -12.3%   -19.9%   -65.0%
   -6%     30%   23    22%     -6.8%   -19.9%   -65.0%
  -10%     12%   23    17%    -14.2%   -21.0%   -65.0%
  -10%     20%   23    17%    -14.2%   -21.0%   -65.0%
  -10%     30%   23    22%     -8.7%   -21.0%   -65.0%
  -15%     12%   23    17%    -14.7%   -21.2%   -65.0%
  -15%     20%   23    17%    -14.7%   -21.2%   -65.0%
  -15%     30%   23    22%     -9.2%   -21.2%   -65.0%
  -25%     12%   23    22%    -17.7%   -29.2%   -67.1%
  -25%     20%   23    22%    -20.7%   -29.9%   -76.1%
  -25%     30%   23    22%    -17.3%   -31.0%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -6.8% per trade over n=23
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $493.44       $522.88
return                         -1.3%         +4.6%
closed trades                     10             3
win rate                         30%           33%
avg net / trade                -2.0%        +31.2%
expectancy $/trade            $-0.66        $+7.63
max drawdown                   -5.4%         -3.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $493.44 (-1.3%) | cash $493.44 | open 0 | max drawdown -5.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 10 | win 3/10 (30%) | avg net -2.0% | realized $-6.56 | expectancy $-0.66/trade
exits: stop 6, trail 4
  (n=10 < 100: noise, not evidence)
last trades:
  AMD          $24.35 -> $21.18 (-13.0%)  stop  1.5h
  DCAT         $24.19 -> $34.87 (+44.2%)  trail  1.7h
  José         $24.61 -> $26.02 (+5.7%)  trail  0.3h
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
  debtdog      $24.92 -> $19.88 (-20.2%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 75, daily_loss_limit 31, max_open_positions 1

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
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 32, setup_rejected:volume_dried_up 16, setup_rejected:top10_concentrated 16, setup_rejected:dumping_now 7, setup_rejected:sellers_dominate_now 1, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
