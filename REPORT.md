# TrenchLab report

Updated: 2026-11-09 22:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           30746
passed SCOUT         75
  killed by SCORE    9
  killed by AUDIT    14
FINAL PASS           52

top kill reasons at first sighting (a pool can have several):
  too_young                    30000
  few_unique_buyers            28880
  liquidity_low                28134
  volume_below_liquidity       21709
  sells_dominate                8229
  wash_churn                    6419
  overheated                    2719
  missing                        938
  too_old                        611
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1578 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   52    -5.0%   -13.2%   -41.9%   -89.9%    56%
SCOUT PASS, killed later     23   +13.1%    +3.1%   -84.2%    +9.6%    43%
KILLED (tracked)           5006    +0.0%   -18.1%   -54.0%    +0.8%    26%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      28    -65.3%    -68.9%    39%
too_old                        19     -0.2%     -2.6%     0%
wash_churn                     12    -37.1%       -      42%
liquidity_low                   7    -29.5%       -      43%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        23    -68.5%    -93.6%    83%
70-79      30    -34.7%    -66.7%    43%
60-69      16    -37.4%    -70.7%    38%
<60         6    -32.2%     +9.6%    17%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      235     -0.7%     -8.0%    -12.8%    29%
<15%       56     +0.4%     -9.8%     -8.3%    34%
15-30%      4    +39.0%     -0.1%     +1.0%    50%
30%+       14     +0.1%     +0.3%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      240     -0.4%     -2.8%     -2.9%    24%
<20%       60     +1.2%    -33.1%    -96.6%    40%
20%+        9    +16.6%    -99.0%       -     100%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      298     -0.3%     -3.1%     -4.2%    28%
20-40%      8    -48.6%    -99.0%       -      88%
40%+        3   +227.1%   +484.6%       -      33%
tokens analysed: 245 | helius credits today: 5124/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   52    19%    -13.9%   -18.1%   -99.7%
   -6%     20%   52    21%    -13.9%   -18.1%   -99.7%
   -6%     30%   52    23%    -10.8%   -18.6%   -99.7%
  -10%     12%   52    21%    -14.7%   -20.0%   -99.7%
  -10%     20%   52    21%    -15.4%   -20.1%   -99.7%
  -10%     30%   52    25%    -12.0%   -20.1%   -99.7%
  -15%     12%   52    21%    -15.3%   -20.4%   -99.7%
  -15%     20%   52    23%    -15.5%   -20.9%   -99.7%
  -15%     30%   52    27%    -12.1%   -20.9%   -99.7%
  -25%     12%   52    25%    -18.1%   -29.4%   -99.7%
  -25%     20%   52    27%    -19.9%   -30.0%   -99.7%
  -25%     30%   52    31%    -16.7%   -30.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -10.8% per trade over n=52
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $434.57       $489.39
return                        -13.1%         -2.1%
closed trades                     24            14
win rate                         21%           21%
avg net / trade               -11.1%         -2.7%
expectancy $/trade            $-2.73        $-0.76
max drawdown                  -16.4%        -10.8%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $434.57 (-13.1%) | cash $434.57 | open 0 | max drawdown -16.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 24 | win 5/24 (21%) | avg net -11.1% | realized $-65.43 | expectancy $-2.73/trade
exits: stop 18, trail 6
  (n=24 < 100: noise, not evidence)
last trades:
  BLEND        $23.55 -> $20.73 (-12.0%)  stop  2.7h
  invest       $23.69 -> $15.38 (-35.1%)  stop  0.3h
  BAWSAQ       $23.87 -> $21.06 (-11.8%)  stop  0.7h
  NVIDIH       $23.16 -> $41.65 (+79.8%)  trail  1.8h
  TITTYVERSE   $23.95 -> $20.01 (-16.4%)  stop  0.5h
  NVIDIOT      $23.75 -> $11.17 (-53.0%)  stop  0.3h
  FAIR         $23.20 -> $18.42 (-20.6%)  stop  0.2h
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
signals skipped by the sizer/risk rules: daily_loss_limit 168, already_traded_token 101, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $489.39 (-2.1%) | cash $489.39 | open 0 | max drawdown -10.8%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 14 | win 3/14 (21%) | avg net -2.7% | realized $-10.61 | expectancy $-0.76/trade
exits: stop 11, trail 3
  (n=14 < 100: noise, not evidence)
last trades:
  Pepetide     $25.63 -> $17.23 (-32.8%)  stop  0.2h
  MAGGIE       $25.21 -> $18.19 (-27.8%)  stop  0.5h
  ELYSION      $24.86 -> $20.95 (-15.7%)  stop  0.5h
  PUSSY        $24.66 -> $21.70 (-12.0%)  stop  0.2h
  TITTYVERSE   $24.51 -> $20.97 (-14.4%)  stop  0.3h
  BUIDL        $24.34 -> $25.54 (+4.9%)  trail  0.5h
  NVIDIH       $24.40 -> $21.45 (-12.1%)  stop  0.5h
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 152, daily_loss_limit 94, setup_rejected:sellers_dominate_now 54, setup_rejected:dumping_now 37, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_received 6, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 1, setup_rejected:b_bundled 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
