# TrenchLab report

Updated: 2026-11-17 07:23 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           83747
passed SCOUT         164
  killed by SCORE    21
  killed by AUDIT    35
FINAL PASS           108

top kill reasons at first sighting (a pool can have several):
  too_young                    82391
  few_unique_buyers            78885
  liquidity_low                77413
  volume_below_liquidity       59005
  sells_dominate               21963
  wash_churn                   17393
  overheated                    7324
  missing                       2531
  too_old                       1024
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4976 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  108    -3.4%   -11.5%   -44.7%   -88.1%    58%
SCOUT PASS, killed later     56    +4.3%    +4.4%   -49.0%   -52.9%    48%
KILLED (tracked)          11708    +0.0%   -56.5%   -79.8%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     116    -94.8%    -68.9%    47%
too_old                        37     -0.7%     -0.4%     5%
wash_churn                     30     -1.1%    -71.8%    30%
liquidity_low                  24    -69.3%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        51    -58.0%    -93.6%    75%
70-79      61    -43.9%    -67.4%    49%
60-69      36    -42.4%    -79.8%    47%
<60        16    -29.7%    -52.9%    31%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      548     -0.3%    -17.3%    -32.6%    34%
<15%      113     +0.4%    -11.2%    -32.5%    30%
15-30%     20     -1.4%     -2.9%     +1.0%    30%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      526     -0.2%     -3.0%    -12.9%    28%
<20%      157     -4.7%    -58.2%    -91.4%    41%
20%+       20     +8.6%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      678     -0.2%     -8.4%    -18.4%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+       10    -43.5%    -46.3%       -      70%
tokens analysed: 590 | helius credits today: 1955/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  108    27%     -8.5%   -14.7%   -99.7%
   -6%     20%  108    27%     -9.0%   -16.0%   -99.7%
   -6%     30%  108    25%     -8.8%   -17.3%   -99.7%
  -10%     12%  108    29%     -9.2%   -18.4%   -99.7%
  -10%     20%  108    28%    -10.0%   -18.9%   -99.7%
  -10%     30%  108    27%     -9.7%   -19.2%   -99.7%
  -15%     12%  108    31%     -9.8%   -19.6%   -99.7%
  -15%     20%  108    31%    -10.5%   -20.6%   -99.7%
  -15%     30%  108    30%    -10.5%   -21.1%   -99.7%
  -25%     12%  108    34%    -12.6%   -19.6%   -99.7%
  -25%     20%  108    34%    -15.1%   -30.0%   -99.7%
  -25%     30%  108    33%    -15.1%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.5% per trade over n=108

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $374.56       $401.33
return                        -25.1%        -19.7%
closed trades                     67            51
win rate                         24%           20%
avg net / trade                -8.1%         -8.2%
expectancy $/trade            $-1.87        $-1.93
max drawdown                  -29.3%        -29.0%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $374.56 (-25.1%) | cash $374.56 | open 0 | max drawdown -29.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 67 | win 16/67 (24%) | avg net -8.1% | realized $-125.44 | expectancy $-1.87/trade
exits: stop 48, trail 19
  (n=67 < 100: noise, not evidence)
last trades:
  BAWSAQ       $19.90 -> $14.39 (-27.7%)  stop  0.2h
  WIGGLES      $19.62 -> $20.44 (+4.2%)  trail  0.3h
  6STAR        $19.75 -> $16.35 (-17.2%)  stop  0.2h
  Marvin       $19.65 -> $16.98 (-13.6%)  stop  0.8h
  FiveM        $19.66 -> $0.01 (-100.0%)  stop  4.0h
  BAWSAQ       $18.38 -> $35.64 (+93.9%)  trail  1.0h
  bul          $19.24 -> $12.80 (-33.5%)  stop  0.2h
  CHAR         $18.92 -> $15.13 (-20.0%)  stop  1.2h
signals skipped by the sizer/risk rules: already_traded_token 393, daily_loss_limit 251, cooldown_after_loss 13, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $401.33 (-19.7%) | cash $401.33 | open 0 | max drawdown -29.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 51 | win 10/51 (20%) | avg net -8.2% | realized $-98.67 | expectancy $-1.93/trade
exits: stop 41, trail 10
  (n=51 < 100: noise, not evidence)
last trades:
  rockstar     $20.24 -> $17.10 (-15.5%)  stop  0.2h
  Marvin       $20.08 -> $17.44 (-13.1%)  stop  0.8h
  WIGGLES      $20.12 -> $16.41 (-18.4%)  stop  1.3h
  Anthropig    $19.77 -> $17.19 (-13.1%)  stop  1.5h
  Trader       $19.64 -> $14.98 (-23.7%)  stop  0.7h
  BAWSAQ       $19.64 -> $17.51 (-10.9%)  stop  1.2h
  BAWSAQ       $19.30 -> $37.05 (+92.0%)  trail  1.0h
  LEOSTAR      $20.19 -> $17.80 (-11.9%)  stop  2.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 364, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 97, setup_rejected:volume_dried_up 39, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
