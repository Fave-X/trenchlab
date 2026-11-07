# TrenchLab report

Updated: 2026-11-07 21:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           16180
passed SCOUT         38
  killed by SCORE    3
  killed by AUDIT    8
FINAL PASS           27

top kill reasons at first sighting (a pool can have several):
  too_young                    15692
  few_unique_buyers            15184
  liquidity_low                14810
  volume_below_liquidity       11479
  sells_dominate                4518
  wash_churn                    3384
  overheated                    1422
  missing                        450
  too_old                        398
  score_below                      1

OUTCOMES (median price change from first sighting / first pass; 929 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   27    -6.6%   -21.3%   -46.5%   -81.8%    41%
SCOUT PASS, killed later     11   +15.6%   +16.6%   -84.2%   +72.1%    36%
KILLED (tracked)           2446    -0.0%    -4.8%   -32.0%    +1.3%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      16    -89.1%       -      50%
too_old                        10     -0.1%     -0.4%     0%
wash_churn                      9    -37.1%       -      56%
volume_below_liquidity          5     +1.5%     -4.6%    40%
liquidity_low                   3    -86.9%       -     100%
overheated                      2    -11.0%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        13    -73.1%    -92.7%    69%
70-79      14    -32.6%    -66.4%    29%
60-69       9    -29.6%    -41.6%    22%
<60         2    -58.2%    +72.1%     0%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      123     -2.2%     -5.1%    -11.1%    22%
<15%       25     +1.4%     -4.6%     +7.9%    44%
15-30%      1   +442.6%   +963.4%       -       0%
30%+        9     -0.3%     -0.6%     +0.8%    11%
bundled     n   +1h med   +4h med  +24h med   rug%
none      126     -1.8%     -2.8%     +0.5%    17%
<20%       27     +7.5%     +5.3%    -94.9%    52%
20%+        5    +16.6%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      151     -1.5%     -2.8%     -0.4%    23%
20-40%      4    -41.0%    -99.0%       -     100%
40%+        3   +227.1%   +484.6%       -       0%
tokens analysed: 128 | helius credits today: 5739/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   26    15%    -13.7%   -20.0%   -65.0%
   -6%     20%   26    15%    -13.7%   -20.0%   -65.0%
   -6%     30%   26    19%     -8.8%   -20.0%   -65.0%
  -10%     12%   26    15%    -15.4%   -21.1%   -65.0%
  -10%     20%   26    15%    -15.4%   -21.1%   -65.0%
  -10%     30%   26    19%    -10.5%   -21.1%   -65.0%
  -15%     12%   26    15%    -15.8%   -21.3%   -65.0%
  -15%     20%   26    15%    -15.8%   -21.3%   -65.0%
  -15%     30%   26    19%    -11.0%   -21.3%   -65.0%
  -25%     12%   26    19%    -18.9%   -29.5%   -67.1%
  -25%     20%   26    19%    -21.6%   -29.9%   -76.1%
  -25%     30%   26    19%    -18.6%   -30.5%   -76.1%
  best so far: stop -6%, trail from +30% -> avg -8.8% per trade over n=26
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $475.71       $519.71
return                         -4.9%         +3.9%
closed trades                     13             4
win rate                         23%           25%
avg net / trade                -6.9%        +20.3%
expectancy $/trade            $-1.82        $+4.93
max drawdown                   -8.5%         -4.4%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $475.71 (-4.9%) | cash $452.31 | open 1 | max drawdown -8.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 13 | win 3/13 (23%) | avg net -6.9% | realized $-23.68 | expectancy $-1.82/trade
exits: stop 9, trail 4
  (n=13 < 100: noise, not evidence)
open:
  FRODO        cost $24.01  now $23.40 (-2.5%)  held 0.0h
last trades:
  MUTTAPE      $24.79 -> $8.77 (-64.6%)  stop  0.2h
  Alice        $23.99 -> $54.38 (+126.7%)  trail  2.2h
  SLINGFOLIO   $25.51 -> $21.41 (-16.1%)  stop  0.3h
  duge         $25.31 -> $17.64 (-30.3%)  stop  0.5h
  debtdog      $24.92 -> $19.88 (-20.2%)  stop  0.2h
  Elysion Pad  $24.67 -> $19.11 (-22.6%)  stop  0.2h
  Chonky       $24.39 -> $17.28 (-29.2%)  stop  0.1h
  José         $24.04 -> $19.59 (-18.5%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 80, daily_loss_limit 31, max_open_positions 1

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $519.71 (+3.9%) | cash $519.71 | open 0 | max drawdown -4.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 4 | win 1/4 (25%) | avg net +20.3% | realized $+19.71 | expectancy $+4.93/trade
exits: stop 3, trail 1
  (n=4 < 100: noise, not evidence)
last trades:
  Alice        $25.00 -> $55.88 (+123.5%)  trail  1.7h
  MUTTAPE      $26.51 -> $21.28 (-19.7%)  stop  0.7h
  FUSE         $26.80 -> $24.03 (-10.3%)  stop  0.7h
  Elysion Pad  $26.14 -> $22.97 (-12.1%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 32, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 17, setup_rejected:dumping_now 12, setup_rejected:sellers_dominate_now 1, setup_rejected:lp_not_locked 1, setup_rejected:b_received 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
