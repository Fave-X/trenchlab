# TrenchLab report

Updated: 2026-11-11 03:35 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           39451
passed SCOUT         92
  killed by SCORE    10
  killed by AUDIT    19
FINAL PASS           63

top kill reasons at first sighting (a pool can have several):
  too_young                    38589
  few_unique_buyers            37096
  liquidity_low                36341
  volume_below_liquidity       27886
  sells_dominate               10423
  wash_churn                    8191
  overheated                    3432
  missing                       1085
  too_old                        699
  rc_danger                        4

OUTCOMES (median price change from first sighting / first pass; 2065 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   63    -5.0%    -7.8%   -45.0%   -90.4%    54%
SCOUT PASS, killed later     29    +7.3%    +0.7%   -62.0%    +9.6%    45%
KILLED (tracked)           6154    +0.0%   -25.6%   -54.5%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      44    -89.1%    -71.7%    50%
too_old                        23     +0.0%     -2.6%     0%
wash_churn                     13     -1.0%       -      38%
liquidity_low                  11    -29.5%       -      36%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  2    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        28    -70.6%    -93.8%    79%
70-79      34    -42.3%    -66.7%    47%
60-69      23    -35.2%    -99.8%    35%
<60         7    -32.2%     +9.6%    14%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      290     -0.5%    -11.0%    -16.0%    33%
<15%       63     +0.1%    -12.1%    -12.3%    33%
15-30%      7     -1.0%     -0.2%     +1.0%    43%
30%+       15     -0.2%     +0.2%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      289     -0.4%     -3.0%     -7.4%    27%
<20%       75     -0.2%    -44.8%    -94.9%    43%
20%+       11    +16.6%    -99.0%       -      91%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      361     -0.3%     -6.6%    -11.5%    30%
20-40%     10    -51.5%    -99.1%       -      80%
40%+        4    +11.6%     +5.8%       -      50%
tokens analysed: 299 | helius credits today: 633/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   63    22%    -11.5%   -17.1%   -99.7%
   -6%     20%   63    24%    -11.5%   -17.1%   -99.7%
   -6%     30%   63    25%     -8.9%   -17.5%   -99.7%
  -10%     12%   63    24%    -12.5%   -19.5%   -99.7%
  -10%     20%   63    24%    -13.0%   -19.9%   -99.7%
  -10%     30%   63    27%    -10.2%   -19.9%   -99.7%
  -15%     12%   63    25%    -12.2%   -20.2%   -99.7%
  -15%     20%   63    27%    -12.3%   -20.4%   -99.7%
  -15%     30%   63    30%     -9.5%   -20.4%   -99.7%
  -25%     12%   63    30%    -14.5%   -29.1%   -99.7%
  -25%     20%   63    32%    -16.0%   -29.9%   -99.7%
  -25%     30%   63    35%    -13.3%   -30.1%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -8.9% per trade over n=63
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $430.41       $467.82
return                        -13.9%         -6.4%
closed trades                     32            20
win rate                         25%           25%
avg net / trade                -8.6%         -6.2%
expectancy $/trade            $-2.14        $-1.61
max drawdown                  -18.1%        -16.2%
open now                           2             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $430.41 (-13.9%) | cash $388.42 | open 2 | max drawdown -18.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 32 | win 8/32 (25%) | avg net -8.6% | realized $-68.42 | expectancy $-2.14/trade
exits: stop 23, trail 9
  (n=32 < 100: noise, not evidence)
open:
  DACITY       cost $21.58  now $20.41 (-5.4%)  held 0.3h
  NIHAO        cost $21.58  now $21.58 (+0.0%)  held 0.1h
last trades:
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
  AICoin       $22.46 -> $45.74 (+103.7%)  trail  0.8h
  X            $23.62 -> $12.50 (-47.1%)  stop  0.2h
  HCAT         $23.06 -> $11.26 (-51.2%)  stop  0.2h
  Catcity      $22.47 -> $18.52 (-17.6%)  stop  0.2h
  LEONIDA      $22.28 -> $5.07 (-77.2%)  stop  0.3h
  HOLD         $21.42 -> $19.28 (-10.0%)  stop  0.1h
  mihao        $21.42 -> $26.82 (+25.2%)  trail  2.2h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 136, cooldown_after_loss 8, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $467.82 (-6.4%) | cash $467.82 | open 0 | max drawdown -16.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 20 | win 5/20 (25%) | avg net -6.2% | realized $-32.18 | expectancy $-1.61/trade
exits: stop 15, trail 5
  (n=20 < 100: noise, not evidence)
last trades:
  NVIDIH       $24.40 -> $21.45 (-12.1%)  stop  0.5h
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
  FAIR         $24.47 -> $19.42 (-20.6%)  stop  0.7h
  BORLY        $24.22 -> $18.90 (-22.0%)  stop  0.5h
  YouTube      $24.14 -> $0.05 (-99.8%)  stop  0.2h
  MEOW         $23.95 -> $26.31 (+9.9%)  trail  2.8h
  HOLD         $22.86 -> $36.92 (+61.5%)  trail  0.7h
  X            $23.57 -> $20.04 (-15.0%)  stop  0.3h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 177, daily_loss_limit 118, setup_rejected:sellers_dominate_now 57, setup_rejected:dumping_now 46, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 13, setup_rejected:b_received 7, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, cooldown_after_loss 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
