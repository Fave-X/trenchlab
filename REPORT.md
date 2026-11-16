# TrenchLab report

Updated: 2026-11-16 01:32 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           74664
passed SCOUT         151
  killed by SCORE    20
  killed by AUDIT    35
FINAL PASS           96

top kill reasons at first sighting (a pool can have several):
  too_young                    73385
  few_unique_buyers            70355
  liquidity_low                68787
  volume_below_liquidity       52807
  sells_dominate               19549
  wash_churn                   15378
  overheated                    6481
  missing                       2388
  too_old                        983
  rc_danger                       13

OUTCOMES (median price change from first sighting / first pass; 4354 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                   96    -4.7%    -7.8%   -43.9%   -88.8%    58%
SCOUT PASS, killed later     55    +4.3%    +4.2%   -50.5%   -15.3%    49%
KILLED (tracked)          10571    +0.0%   -55.7%   -79.0%    +0.1%    31%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                      96    -94.8%    -68.9%    52%
too_old                        34     -0.6%     -0.4%     3%
wash_churn                     25     -1.1%    -71.8%    28%
liquidity_low                  19    -65.5%    -49.8%    47%
volume_below_liquidity          7     -2.8%    +15.3%    43%
overheated                      5     -3.6%    -56.0%    60%
sells_dominate                  2    -64.6%       -      50%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        50    -55.0%    -93.4%    72%
70-79      56    -44.3%    -66.7%    50%
60-69      30    -35.2%    -79.9%    47%
<60        15    -31.3%    -15.3%    33%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none      496     -0.1%    -12.0%    -34.1%    34%
<15%       99     +0.2%    -11.2%    -15.5%    29%
15-30%     11     -0.2%     -0.7%     +1.0%    36%
30%+       22     -0.4%     -0.5%     +2.6%     5%
bundled     n   +1h med   +4h med  +24h med   rug%
none      476     +0.0%     -2.3%    -12.8%    28%
<20%      135     -5.9%    -55.2%    -94.9%    44%
20%+       17    +16.6%    -99.0%       -      82%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%      603     -0.1%     -5.5%    -16.0%    31%
20-40%     16     -6.5%    -99.0%    -99.1%    75%
40%+        9    +11.6%    -46.3%       -      56%
tokens analysed: 523 | helius credits today: 484/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%   95    24%     -9.4%   -17.1%   -99.7%
   -6%     20%   95    24%     -9.6%   -17.1%   -99.7%
   -6%     30%   95    25%     -8.0%   -17.1%   -99.7%
  -10%     12%   95    26%     -9.2%   -18.7%   -99.7%
  -10%     20%   95    25%     -9.8%   -19.1%   -99.7%
  -10%     30%   95    27%     -8.0%   -19.3%   -99.7%
  -15%     12%   95    28%     -9.0%   -19.9%   -99.7%
  -15%     20%   95    28%     -9.6%   -20.7%   -99.7%
  -15%     30%   95    31%     -7.7%   -21.0%   -99.7%
  -25%     12%   95    33%    -12.1%   -21.3%   -99.7%
  -25%     20%   95    33%    -14.5%   -30.8%   -99.7%
  -25%     30%   95    35%    -12.8%   -31.0%   -99.7%
  best so far: stop -15%, trail from +30% -> avg -7.7% per trade over n=95
  WARNING: n < 100. This is noise, not evidence. Do not trade on it.

================================================================
A vs B (same sizing, exits and costs; only the entry rule differs)
================================================================
                                   A             B
started                  11-06 08:00   11-07 04:00
equity                       $397.95       $404.84
return                        -20.4%        -19.0%
closed trades                     59            43
win rate                         24%           21%
avg net / trade                -7.2%         -9.4%
expectancy $/trade            $-1.73        $-2.21
max drawdown                  -23.4%        -25.5%
open now                           1             0
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $397.95 (-20.4%) | cash $378.05 | open 1 | max drawdown -23.4%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 59 | win 14/59 (24%) | avg net -7.2% | realized $-102.05 | expectancy $-1.73/trade
exits: stop 42, trail 17
  (n=59 < 100: noise, not evidence)
open:
  BAWSAQ       cost $19.90  now $19.90 (+0.0%)  held 0.0h
last trades:
  billie       $21.80 -> $3.70 (-83.0%)  stop  0.2h
  bill         $20.89 -> $19.84 (-5.0%)  trail  0.3h
  worth        $20.84 -> $13.96 (-33.0%)  stop  0.2h
  Socks        $20.51 -> $18.26 (-11.0%)  stop  0.2h
  WANTED       $20.50 -> $21.41 (+4.4%)  trail  1.7h
  BUTTHOLE     $20.43 -> $17.04 (-16.6%)  stop  0.3h
  rockstar     $20.26 -> $17.49 (-13.7%)  stop  0.2h
  AI           $20.12 -> $15.62 (-22.4%)  stop  0.3h
signals skipped by the sizer/risk rules: already_traded_token 358, daily_loss_limit 244, cooldown_after_loss 11, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $404.84 (-19.0%) | cash $404.84 | open 0 | max drawdown -25.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 43 | win 9/43 (21%) | avg net -9.4% | realized $-95.16 | expectancy $-2.21/trade
exits: stop 34, trail 9
  (n=43 < 100: noise, not evidence)
last trades:
  Sakura       $21.28 -> $46.02 (+116.2%)  trail  1.2h
  CSI          $22.52 -> $19.70 (-12.5%)  stop  0.3h
  SPEED        $22.70 -> $0.05 (-99.8%)  stop  0.3h
  bill         $21.25 -> $15.00 (-29.4%)  stop  0.2h
  HYGG         $20.94 -> $24.47 (+16.9%)  trail  1.3h
  ニャジラ         $21.11 -> $13.78 (-34.7%)  stop  0.7h
  Socks        $20.75 -> $17.11 (-17.5%)  stop  0.5h
  WANTED       $20.56 -> $14.13 (-31.3%)  stop  0.8h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 319, daily_loss_limit 219, setup_rejected:sellers_dominate_now 120, setup_rejected:dumping_now 94, setup_rejected:volume_dried_up 34, setup_rejected:b_bundled 33, setup_rejected:top10_concentrated 29, setup_rejected:operator_cluster 16, setup_rejected:b_received 7, setup_rejected:unknown:lp_lock 6, cooldown_after_loss 6, setup_rejected:rc_danger:Creator history of rugged tokens 3, setup_rejected:lp_not_locked 3, setup_rejected:rc_danger:Low Liquidity 2, setup_rejected:clustered_supply 1, setup_rejected:bundled_buys 1, max_open_positions 1

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
