# TrenchLab report

Updated: 2026-11-17 15:52 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           86210
passed SCOUT         169
  killed by SCORE    22
  killed by AUDIT    36
FINAL PASS           111

top kill reasons at first sighting (a pool can have several):
  too_young                    84839
  few_unique_buyers            81209
  liquidity_low                79733
  volume_below_liquidity       60732
  sells_dominate               22598
  wash_churn                   17915
  overheated                    7563
  missing                       2556
  too_old                       1029
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 5120 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  111    -4.2%   -11.5%   -45.0%   -88.1%    58%
SCOUT PASS, killed later     58    +4.3%    +3.9%   -49.0%   -52.9%    50%
KILLED (tracked)          12022    +0.0%   -56.7%   -80.1%    +0.4%    30%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     120    -94.1%    -68.9%    48%
too_old                        37     -0.7%     -0.4%     5%
wash_churn                     32     -1.1%    -71.8%    28%
liquidity_low                  24    -69.3%    -49.8%    54%
volume_below_liquidity          7     -2.8%    +30.3%    43%
overheated                      6    -12.8%    -56.0%    67%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        51    -58.0%    -93.6%    75%
70-79      63    -41.9%    -67.4%    48%
60-69      38    -45.2%    -79.8%    47%
<60        17    -31.3%    -52.9%    41%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      565     -0.3%    -18.4%    -33.1%    34%
<15%      114     +0.2%     -9.8%    -32.5%    31%
15-30%     20     -1.4%     -2.9%     +1.0%    30%
30%+       23     -0.4%     -0.5%     +2.6%     9%
bundled     n   +1h med   +4h med  +24h med   rug%
none      541     -0.2%     -3.5%    -13.9%    28%
<20%      160     -3.5%    -58.2%    -91.4%    42%
20%+       21     +8.6%    -99.0%       -      81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      696     -0.2%     -9.0%    -20.4%    31%
20-40%     15     -4.8%    -99.0%    -99.1%    80%
40%+       11    -43.5%    -46.3%       -      73%
tokens analysed: 609 | helius credits today: 4221/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  110    26%     -8.8%   -16.0%   -99.7%
   -6%     20%  110    26%     -9.3%   -17.1%   -99.7%
   -6%     30%  110    25%     -9.1%   -17.6%   -99.7%
  -10%     12%  110    28%     -9.5%   -18.6%   -99.7%
  -10%     20%  110    27%    -10.3%   -19.1%   -99.7%
  -10%     30%  110    26%    -10.0%   -19.4%   -99.7%
  -15%     12%  110    30%    -10.0%   -19.8%   -99.7%
  -15%     20%  110    30%    -10.8%   -20.6%   -99.7%
  -15%     30%  110    29%    -10.7%   -21.1%   -99.7%
  -25%     12%  110    34%    -13.0%   -24.6%   -99.7%
  -25%     20%  110    34%    -15.5%   -30.4%   -99.7%
  -25%     30%  110    33%    -15.5%   -31.0%   -99.7%
  best so far: stop -6%, trail from +12% -> avg -8.8% per trade over n=110

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $366.00       $410.05
return                        -26.8%        -18.0%
closed trades                     69            53
win rate                         23%           23%
avg net / trade                -8.5%         -7.1%
expectancy $/trade            $-1.94        $-1.70
max drawdown                  -29.6%        -29.0%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $366.00 (-26.8%) | cash $347.70 | open 1 | max drawdown -29.6%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 69 | win 16/69 (23%) | avg net -8.5% | realized $-134.00 | expectancy $-1.94/trade
exits: stop 50, trail 19
  (n=69 < 100: noise, not evidence)
open:
  GEKKO        cost $18.30  now $18.30 (+0.0%)  held 0.0h
last trades:
  6STAR        $19.75 -> $16.35 (-17.2%)  stop  0.2h
  Marvin       $19.65 -> $16.98 (-13.6%)  stop  0.8h
  FiveM        $19.66 -> $0.01 (-100.0%)  stop  4.0h
  BAWSAQ       $18.38 -> $35.64 (+93.9%)  trail  1.0h
  bul          $19.24 -> $12.80 (-33.5%)  stop  0.2h
  CHAR         $18.92 -> $15.13 (-20.0%)  stop  1.2h
  KATIA        $18.73 -> $13.75 (-26.6%)  stop  0.3h
  GROKIA       $18.48 -> $14.90 (-19.4%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 405, daily_loss_limit 251, cooldown_after_loss 13, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $410.05 (-18.0%) | cash $410.05 | open 0 | max drawdown -29.0%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 53 | win 12/53 (23%) | avg net -7.1% | realized $-89.95 | expectancy $-1.70/trade
exits: stop 41, trail 12
  (n=53 < 100: noise, not evidence)
last trades:
  WIGGLES      $20.12 -> $16.41 (-18.4%)  stop  1.3h
  Anthropig    $19.77 -> $17.19 (-13.1%)  stop  1.5h
  Trader       $19.64 -> $14.98 (-23.7%)  stop  0.7h
  BAWSAQ       $19.64 -> $17.51 (-10.9%)  stop  1.2h
  BAWSAQ       $19.30 -> $37.05 (+92.0%)  trail  1.0h
  LEOSTAR      $20.19 -> $17.80 (-11.9%)  stop  2.2h
  bul          $20.07 -> $27.86 (+38.8%)  trail  1.5h
  KATIA        $20.67 -> $21.60 (+4.5%)  trail  1.0h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 369, daily_loss_limit 219, setup_rejected:sellers_dominate_now 122, setup_rejected:dumping_now 98, setup_rejected:volume_dried_up 46, setup_rejected:b_bundled 35, setup_rejected:top10_concentrated 33, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
