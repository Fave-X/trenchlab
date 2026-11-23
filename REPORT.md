# TrenchLab report

Updated: 2026-11-23 19:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           130662
passed SCOUT         257
  killed by SCORE    36
  killed by AUDIT    65
FINAL PASS           156

top kill reasons at first sighting (a pool can have several):
  too_young                   128908
  few_unique_buyers           122954
  liquidity_low               120854
  volume_below_liquidity       92100
  sells_dominate               34712
  wash_churn                   27430
  overheated                   11770
  missing                       3623
  too_old                       1278
  rc_danger                       20

OUTCOMES (median price change from first sighting / first pass; 7732 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  156    -4.7%   -11.7%   -42.6%   -85.9%    58%
SCOUT PASS, killed later    101    +5.4%    +9.1%   -13.5%   -74.6%    48%
KILLED (tracked)          18063    +0.1%   -59.4%   -84.8%    -0.1%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     382    -90.5%    -68.9%    25%
wash_churn                     55    -23.3%    -85.6%    25%
too_old                        49     -0.6%     -0.4%    10%
liquidity_low                  35    -69.9%    -49.8%    57%
overheated                     11    -21.9%    -56.0%    55%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        71    -51.8%    -93.3%    59%
70-79     100    -43.9%    -72.2%    50%
60-69      61    -30.1%    -92.5%    56%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1018     +0.0%     -9.2%    -47.5%    27%
<15%      232     +2.3%    -13.7%    -36.5%    33%
15-30%     43     -0.5%     -2.4%     +0.4%    33%
30%+       34     -0.6%     -0.7%     +1.9%    32%
bundled     n   +1h med   +4h med  +24h med   rug%
none      893     +0.0%     -2.4%    -32.5%    25%
<20%      378     +2.8%    -58.2%    -92.8%    28%
20%+       56     -2.9%    -99.0%       -      80%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1274     +0.2%     -6.1%    -40.0%    26%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       19    -98.5%    -98.6%       -      79%
tokens analysed: 1165 | helius credits today: 8207/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  156    22%     -9.5%   -14.3%   -99.7%
   -6%     20%  156    24%     -9.8%   -14.7%   -99.7%
   -6%     30%  156    21%     -9.9%   -15.1%   -99.7%
  -10%     12%  156    26%     -9.4%   -17.1%   -99.7%
  -10%     20%  156    27%     -9.8%   -17.6%   -99.7%
  -10%     30%  156    25%     -9.8%   -18.5%   -99.7%
  -15%     12%  156    30%     -8.9%   -19.2%   -99.7%
  -15%     20%  156    33%     -9.3%   -20.3%   -99.7%
  -15%     30%  156    30%     -9.6%   -21.0%   -99.7%
  -25%     12%  156    35%    -10.9%   -15.3%   -99.7%
  -25%     20%  156    38%    -12.7%   -29.3%   -99.7%
  -25%     30%  156    35%    -12.7%   -30.5%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -8.9% per trade over n=156

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $301.94       $334.14
return                        -39.6%        -33.2%
closed trades                    104            84
win rate                         22%           23%
avg net / trade                -9.2%         -9.2%
expectancy $/trade            $-1.90        $-1.97
max drawdown                  -42.2%        -38.5%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $301.94 (-39.6%) | cash $301.94 | open 0 | max drawdown -42.2%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 104 | win 23/104 (22%) | avg net -9.2% | realized $-198.06 | expectancy $-1.90/trade
exits: stop 75, trail 28, dead_no_route 1
last trades:
  UCASH        $16.39 -> $14.30 (-12.8%)  stop  0.7h
  MCAT         $16.28 -> $14.16 (-13.0%)  stop  0.2h
  MCAT         $16.18 -> $0.00 (-100.0%)  dead_no_route  1.8h
  OpenIndex    $15.37 -> $12.15 (-20.9%)  stop  0.3h
  COPIUM       $15.21 -> $13.38 (-12.0%)  stop  1.0h
  Fly          $15.11 -> $13.32 (-11.9%)  stop  0.2h
  cCAT         $15.02 -> $17.11 (+13.9%)  trail  0.3h
  JENSEN       $15.13 -> $14.50 (-4.2%)  trail  0.8h
signals skipped by the sizer/risk rules: already_traded_token 588, daily_loss_limit 322, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $334.14 (-33.2%) | cash $334.14 | open 0 | max drawdown -38.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 84 | win 19/84 (23%) | avg net -9.2% | realized $-165.86 | expectancy $-1.97/trade
exits: stop 64, trail 20
  (n=84 < 100: noise, not evidence)
last trades:
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
  SIDOOR       $17.41 -> $15.65 (-10.1%)  stop  0.3h
  MCAT         $17.32 -> $18.54 (+7.0%)  trail  3.5h
  cCAT         $17.38 -> $13.20 (-24.0%)  stop  0.2h
  UCASH        $17.17 -> $17.37 (+1.2%)  trail  0.8h
  FSDV15       $17.18 -> $13.32 (-22.5%)  stop  0.7h
  sexcoin      $16.99 -> $11.40 (-32.9%)  stop  0.5h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 436, daily_loss_limit 239, setup_rejected:sellers_dominate_now 142, setup_rejected:dumping_now 141, setup_rejected:b_bundled 74, setup_rejected:volume_dried_up 59, setup_rejected:operator_cluster 41, setup_rejected:clustered_supply 38, setup_rejected:lp_not_locked 34, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
