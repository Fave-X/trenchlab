# TrenchLab report

Updated: 2026-11-22 03:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           118577
passed SCOUT         226
  killed by SCORE    34
  killed by AUDIT    48
FINAL PASS           144

top kill reasons at first sighting (a pool can have several):
  too_young                   116905
  few_unique_buyers           111672
  liquidity_low               109854
  volume_below_liquidity       83600
  sells_dominate               31333
  wash_churn                   24882
  overheated                   10608
  missing                       3213
  too_old                       1223
  rc_danger                       18

OUTCOMES (median price change from first sighting / first pass; 7147 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  144    -5.2%   -13.0%   -44.4%   -87.5%    58%
SCOUT PASS, killed later     82    +4.3%    +4.6%   -30.1%   -74.6%    52%
KILLED (tracked)          16313    +0.0%   -60.9%   -84.8%    +0.4%    28%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     295    -95.0%    -68.9%    29%
wash_churn                     49     -1.2%    -85.6%    27%
too_old                        46     -0.6%     -0.4%    11%
liquidity_low                  33    -69.9%    -49.8%    61%
overheated                      9     -3.6%    -56.0%    44%
volume_below_liquidity          7     -2.8%    +30.3%    43%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        60    -55.3%    -93.3%    67%
70-79      84    -51.5%    -72.2%    52%
60-69      57    -35.3%    -92.5%    54%
<60        25     -7.4%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      867     -0.2%    -12.5%    -45.0%    28%
<15%      176     +0.7%    -12.1%    -32.5%    36%
15-30%     38     -1.2%     -2.7%     +0.4%    34%
30%+       33     -0.5%     -0.7%     +1.9%    30%
bundled     n   +1h med   +4h med  +24h med   rug%
none      763     -0.1%     -2.7%    -31.1%    26%
<20%      299     -3.6%    -58.3%    -92.8%    30%
20%+       52     -0.4%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1063     -0.0%     -7.4%    -35.1%    27%
20-40%     34     -4.6%    -99.0%    -99.1%    79%
40%+       17    -98.5%    -98.6%       -      82%
tokens analysed: 960 | helius credits today: 1426/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  144    22%     -9.7%   -14.9%   -99.7%
   -6%     20%  144    24%    -10.1%   -15.0%   -99.7%
   -6%     30%  144    22%    -10.0%   -17.0%   -99.7%
  -10%     12%  144    26%     -9.7%   -18.4%   -99.7%
  -10%     20%  144    27%    -10.1%   -18.6%   -99.7%
  -10%     30%  144    26%     -9.7%   -18.9%   -99.7%
  -15%     12%  144    29%     -9.4%   -19.8%   -99.7%
  -15%     20%  144    32%     -9.8%   -20.4%   -99.7%
  -15%     30%  144    30%     -9.7%   -21.0%   -99.7%
  -25%     12%  144    33%    -12.0%   -24.6%   -99.7%
  -25%     20%  144    36%    -13.7%   -29.9%   -99.7%
  -25%     30%  144    34%    -13.8%   -30.9%   -99.7%
  best so far: stop -15%, trail from +12% -> avg -9.4% per trade over n=144

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $328.95       $348.11
return                        -34.2%        -30.4%
closed trades                     95            78
win rate                         23%           22%
avg net / trade                -8.3%         -8.9%
expectancy $/trade            $-1.80        $-1.95
max drawdown                  -37.7%        -37.3%
open now                           0             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $328.95 (-34.2%) | cash $328.95 | open 0 | max drawdown -37.7%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 95 | win 22/95 (23%) | avg net -8.3% | realized $-171.05 | expectancy $-1.80/trade
exits: stop 70, trail 25
  (n=95 < 100: noise, not evidence)
last trades:
  RUDY         $16.97 -> $15.02 (-11.5%)  stop  0.2h
  Trader       $16.87 -> $13.30 (-21.2%)  stop  0.2h
  PUNANI       $16.69 -> $14.71 (-11.9%)  stop  0.3h
  XV           $16.69 -> $14.12 (-15.4%)  stop  0.2h
  Bigfoot      $16.46 -> $12.98 (-21.2%)  stop  0.2h
  HOUSE        $16.29 -> $14.03 (-13.9%)  stop  0.2h
  SIDOOR       $16.18 -> $17.90 (+10.6%)  trail  0.7h
  STREETS      $16.26 -> $19.94 (+22.7%)  trail  1.0h
signals skipped by the sizer/risk rules: already_traded_token 523, daily_loss_limit 310, cooldown_after_loss 18, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $348.11 (-30.4%) | cash $348.11 | open 0 | max drawdown -37.3%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 78 | win 17/78 (22%) | avg net -8.9% | realized $-151.89 | expectancy $-1.95/trade
exits: stop 60, trail 18
  (n=78 < 100: noise, not evidence)
last trades:
  AMC          $18.09 -> $15.90 (-12.1%)  stop  0.2h
  AI           $17.98 -> $19.59 (+8.9%)  trail  0.3h
  RIEMANN      $18.06 -> $13.90 (-23.0%)  stop  0.3h
  Trader       $17.85 -> $12.98 (-27.3%)  stop  0.2h
  JENSEN       $17.61 -> $20.21 (+14.8%)  trail  0.5h
  XV           $17.74 -> $15.04 (-15.2%)  stop  0.2h
  Bigfoot      $17.60 -> $15.48 (-12.1%)  stop  0.5h
  STREETS      $17.50 -> $15.68 (-10.4%)  stop  0.2h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 421, daily_loss_limit 239, setup_rejected:dumping_now 138, setup_rejected:sellers_dominate_now 133, setup_rejected:b_bundled 69, setup_rejected:volume_dried_up 47, setup_rejected:operator_cluster 36, setup_rejected:top10_concentrated 33, setup_rejected:lp_not_locked 29, setup_rejected:bundled_buys 23, setup_rejected:clustered_supply 17, setup_rejected:b_received 10, cooldown_after_loss 8, setup_rejected:unknown:lp_lock 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:rc_danger:Low Liquidity 2, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
