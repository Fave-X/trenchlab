# TrenchLab report

Updated: 2026-11-10 03:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           32243
passed SCOUT         80
  killed by SCORE    9
  killed by AUDIT    16
FINAL PASS           55

top kill reasons at first sighting (a pool can have several):
  too_young                    31482
  few_unique_buyers            30277
  liquidity_low                29551
  volume_below_liquidity       22778
  sells_dominate                8606
  wash_churn                    6694
  overheated                    2839
  missing                        943
  too_old                        620
  score_below                      2

OUTCOMES (median price change from first sighting / first pass; 1651 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   55    -5.0%   -10.6%   -44.0%   -89.9%    53%
SCOUT PASS, killed later     25   +19.1%    +7.3%   -78.9%    +9.6%    44%
KILLED (tracked)           5236    +0.0%   -20.7%   -50.7%    +0.7%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      32    -65.3%    -68.9%    41%
too_old                        19     -0.2%     -2.6%     0%
wash_churn                     12     -1.0%       -      42%
liquidity_low                   8    -29.5%       -      38%
volume_below_liquidity          5     +5.9%    +15.3%    40%
overheated                      2    -11.0%       -      50%
sells_dominate                  1    -54.2%       -       0%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        24    -68.5%    -93.6%    83%
70-79      31    -39.9%    -66.9%    42%
60-69      19    -39.6%    -70.7%    32%
<60         6    -39.8%     +9.6%    17%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      243     -0.8%     -9.7%    -12.8%    30%
<15%       58     +0.3%    -12.1%     -8.3%    33%
15-30%      4    +39.0%     -0.1%     +1.0%    50%
30%+       14     +0.1%     +0.3%     +2.6%     7%
bundled     n   +1h med   +4h med  +24h med   rug%
none      244     -0.4%     -3.0%     -2.9%    25%
<20%       65     +0.6%    -36.6%    -96.6%    38%
20%+       10    +24.1%    -99.0%       -      90%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      306     -0.3%     -5.3%     -4.2%    28%
20-40%      9     +1.3%    -99.2%       -      78%
40%+        4    +11.6%   +484.6%       -      50%
tokens analysed: 255 | helius credits today: 872/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   54    20%    -12.4%   -17.3%   -99.7%
   -6%     20%   54    22%    -12.4%   -17.3%   -99.7%
   -6%     30%   54    24%     -9.4%   -18.0%   -99.7%
  -10%     12%   54    22%    -13.5%   -20.0%   -99.7%
  -10%     20%   54    22%    -14.1%   -20.1%   -99.7%
  -10%     30%   54    26%    -10.8%   -20.1%   -99.7%
  -15%     12%   54    22%    -14.1%   -20.4%   -99.7%
  -15%     20%   54    24%    -14.2%   -20.9%   -99.7%
  -15%     30%   54    28%    -11.0%   -20.9%   -99.7%
  -25%     12%   54    26%    -17.4%   -29.4%   -99.7%
  -25%     20%   54    28%    -19.2%   -30.0%   -99.7%
  -25%     30%   54    31%    -16.1%   -30.9%   -99.7%
  best so far: stop -6%, trail from +30% -> avg -9.4% per trade over n=54
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $449.13       $483.11
return                        -10.2%         -3.4%
closed trades                     25            15
win rate                         24%           20%
avg net / trade                -8.0%         -3.9%
expectancy $/trade            $-2.03        $-1.04
max drawdown                  -16.6%        -11.1%
open now                           1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $449.13 (-10.2%) | cash $426.67 | open 1 | max drawdown -16.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 25 | win 6/25 (24%) | avg net -8.0% | realized $-50.87 | expectancy $-2.03/trade
exits: stop 18, trail 7
  (n=25 < 100: noise, not evidence)
open:
  AICoin       cost $22.46  now $22.46 (+0.0%)  held 0.0h
last trades:
  invest       $23.69 -> $15.38 (-35.1%)  stop  0.3h
  BAWSAQ       $23.87 -> $21.06 (-11.8%)  stop  0.7h
  NVIDIH       $23.16 -> $41.65 (+79.8%)  trail  1.8h
  TITTYVERSE   $23.95 -> $20.01 (-16.4%)  stop  0.5h
  NVIDIOT      $23.75 -> $11.17 (-53.0%)  stop  0.3h
  FAIR         $23.20 -> $18.42 (-20.6%)  stop  0.2h
  ORBIT        $23.12 -> $0.03 (-99.9%)  stop  1.8h
  BORLY        $21.73 -> $36.28 (+67.0%)  trail  1.8h
signals skipped by the sizer/risk rules: daily_loss_limit 169, already_traded_token 106, cooldown_after_loss 6, max_open_positions 4

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $483.11 (-3.4%) | cash $460.12 | open 1 | max drawdown -11.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 15 | win 3/15 (20%) | avg net -3.9% | realized $-15.66 | expectancy $-1.04/trade
exits: stop 12, trail 3
  (n=15 < 100: noise, not evidence)
open:
  BORLY        cost $24.22  now $22.99 (-5.1%)  held 0.4h
last trades:
  MAGGIE       $25.21 -> $18.19 (-27.8%)  stop  0.5h
  ELYSION      $24.86 -> $20.95 (-15.7%)  stop  0.5h
  PUSSY        $24.66 -> $21.70 (-12.0%)  stop  0.2h
  TITTYVERSE   $24.51 -> $20.97 (-14.4%)  stop  0.3h
  BUIDL        $24.34 -> $25.54 (+4.9%)  trail  0.5h
  NVIDIH       $24.40 -> $21.45 (-12.1%)  stop  0.5h
  STOKE        $24.25 -> $28.63 (+18.1%)  trail  0.8h
  FAIR         $24.47 -> $19.42 (-20.6%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 171, daily_loss_limit 94, setup_rejected:sellers_dominate_now 54, setup_rejected:dumping_now 37, setup_rejected:top10_concentrated 29, setup_rejected:volume_dried_up 23, setup_rejected:b_bundled 7, setup_rejected:b_received 6, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
