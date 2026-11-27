# TrenchLab report

Updated: 2026-11-27 03:42 UTC

```
================================================================
TRENCHLAB REPORT
================================================================
pools seen           154675
passed SCOUT         320
  killed by SCORE    42
  killed by AUDIT    89
FINAL PASS           189

top kill reasons at first sighting (a pool can have several):
  too_young                   152639
  few_unique_buyers           145069
  liquidity_low               143132
  volume_below_liquidity      107949
  sells_dominate               41855
  wash_churn                   32580
  overheated                   14172
  missing                       4258
  too_old                       1415
  copy_trade                      58

OUTCOMES (median price change from first sighting / first pass; 9397 pools had zero-liquidity/frozen-price data gaps, ignored)
group                         n     +15m      +1h      +4h     +24h   rug%
FINAL PASS                  189    -5.5%   -19.8%   -45.0%   -83.0%    60%
SCOUT PASS, killed later    131    +6.2%    +9.5%    -7.4%   -74.6%    46%
KILLED (tracked)          21051    +0.1%   -58.3%   -85.2%    -0.4%    27%

NEAR MISSES: pools killed by exactly ONE rule
(if these do as well as FINAL PASS, that rule may be killing winners)
rule                            n   +4h med  +24h med   rug%
too_young                     574    -88.2%    -68.9%    22%
wash_churn                     61     -1.2%    -85.6%    25%
copy_trade                     58    -75.8%    -95.6%    12%
too_old                        52     -0.6%     -0.4%    10%
liquidity_low                  37    -68.7%    -72.0%    57%
overheated                     16     -3.6%    -56.0%    38%
volume_below_liquidity          8     +1.2%    +40.3%    38%
sells_dominate                  3    -75.0%       -      67%

SCORE CHECK: scout passers by score (higher buckets should do better;
if they don't, the score is decoration - change it)
score       n   +4h med  +24h med   rug%
80+        89    -52.9%    -92.9%    55%
70-79     134    -52.0%    -77.2%    54%
60-69      70    -32.0%    -89.0%    56%
<60        27     -7.2%    -63.7%    48%

CABAL CHECK: tracked pools by largest linked-wallet cluster (% of supply)
(bigger clusters should rug more / do worse; if not, the cluster rule is noise)
cluster     n   +1h med   +4h med  +24h med   rug%
none     1278     +0.1%     -9.1%    -51.4%    25%
<15%      344     +2.8%    -19.5%    -53.6%    31%
15-30%     41     -0.2%     -2.1%     +1.0%    46%
30%+       38     -0.7%     -1.1%     +0.5%    37%
bundled     n   +1h med   +4h med  +24h med   rug%
none     1101     +0.1%     -2.2%    -39.7%    24%
<20%      531     +2.9%    -60.7%    -91.4%    27%
20%+       69     -2.9%    -99.1%  +1071.7%    81%
fresh       n   +1h med   +4h med  +24h med   rug%
<20%     1635     +0.4%     -7.2%    -44.0%    25%
20-40%     39     -0.7%    -99.0%    -99.1%    77%
40%+       27    -98.5%    -99.4%  +1071.7%    78%
tokens analysed: 1518 | helius credits today: 1902/25000

EXIT GRID on FINAL PASS entries (round-trip cost 4.0%, trail distance 10%)
  stop  trail@    n   win%   avg net   median    worst
   -6%     12%  189    21%    -11.3%   -15.1%   -99.7%
   -6%     20%  189    23%    -11.4%   -15.1%   -99.7%
   -6%     30%  189    21%    -11.6%   -15.9%   -99.7%
  -10%     12%  189    24%    -11.1%   -17.5%   -99.7%
  -10%     20%  189    26%    -11.3%   -18.2%   -99.7%
  -10%     30%  189    24%    -11.4%   -18.7%   -99.7%
  -15%     12%  189    28%    -11.4%   -20.2%   -99.7%
  -15%     20%  189    31%    -11.7%   -21.0%   -99.7%
  -15%     30%  189    29%    -12.1%   -21.4%   -99.7%
  -25%     12%  189    32%    -13.5%   -21.3%   -99.7%
  -25%     20%  189    36%    -14.6%   -29.6%   -99.7%
  -25%     30%  189    33%    -15.2%   -30.9%   -99.7%
  best so far: stop -10%, trail from +12% -> avg -11.1% per trade over n=189

================================================================
PAPER BOOKS COMPARED (A and B: same sizing/exits, only the entry differs;
C copies watched wallets with a 30s delay and mirror exits)
================================================================
                                   A             B             C
started                  11-06 08:00   11-07 04:00   11-24 09:00
equity                       $244.61       $282.02       $428.15
return                        -51.1%        -43.6%        -14.4%
closed trades                    131           101            14
win rate                         21%           19%           21%
avg net / trade               -10.4%        -10.9%        -22.0%
expectancy $/trade            $-1.94        $-2.15        $-5.27
max drawdown                  -52.9%        -48.1%        -15.5%
open now                           1             1             1
Judge on expectancy after >=100 trades each, not on win rate or a few days.

================================================================
PAPER BOOK A: momentum (thread filters)
  pricing: model | start $500.00 on 2026-11-06 08:00 UTC
================================================================
equity $244.61 (-51.1%) | cash $232.88 | open 1 | max drawdown -52.9%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 131 | win 28/131 (21%) | avg net -10.4% | realized $-254.76 | expectancy $-1.94/trade
exits: stop 97, trail 33, dead_no_route 1
open:
  KAI          cost $12.36  now $11.73 (-5.1%)  held 1.5h
last trades:
  Elonmas      $12.48 -> $15.86 (+27.1%)  trail  1.0h
  PAIR         $12.65 -> $17.22 (+36.2%)  trail  1.3h
  duk          $12.88 -> $9.04 (-29.8%)  stop  0.2h
  KURO         $12.69 -> $15.15 (+19.4%)  trail  0.3h
  Hoppy        $12.81 -> $7.02 (-45.2%)  stop  0.2h
  Vetocat      $12.52 -> $10.86 (-13.3%)  stop  0.2h
  DEXDATA      $12.52 -> $11.02 (-12.0%)  stop  0.5h
  DragonRiders $12.44 -> $10.43 (-16.2%)  stop  0.2h
signals skipped by the sizer/risk rules: already_traded_token 701, daily_loss_limit 331, cooldown_after_loss 25, max_open_positions 5

================================================================
PAPER BOOK B: pullback (safety-first, buy the dip)
  pricing: model | start $500.00 on 2026-11-07 04:00 UTC
================================================================
equity $282.02 (-43.6%) | cash $268.82 | open 1 | max drawdown -48.1%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 101 | win 19/101 (19%) | avg net -10.9% | realized $-217.03 | expectancy $-2.15/trade
exits: stop 81, trail 20
open:
  KAI          cost $14.15  now $13.20 (-6.7%)  held 0.4h
last trades:
  JaoJiu       $15.31 -> $11.47 (-25.1%)  stop  0.3h
  MONEY        $15.00 -> $13.27 (-11.5%)  stop  0.3h
  Grodia       $14.91 -> $13.02 (-12.7%)  stop  0.3h
  NORFEATH     $14.82 -> $12.87 (-13.2%)  stop  0.5h
  duk          $14.72 -> $12.42 (-15.6%)  stop  0.2h
  PAIR         $14.61 -> $9.69 (-33.7%)  stop  0.5h
  Hoppy        $14.36 -> $11.68 (-18.7%)  stop  0.5h
  DEXDATA      $14.23 -> $12.68 (-10.9%)  stop  0.7h
signals skipped by the sizer/risk rules: setup_rejected:few_buyers_now 457, daily_loss_limit 269, setup_rejected:dumping_now 166, setup_rejected:sellers_dominate_now 149, setup_rejected:b_bundled 96, setup_rejected:volume_dried_up 61, setup_rejected:operator_cluster 53, setup_rejected:lp_not_locked 43, setup_rejected:clustered_supply 38, setup_rejected:top10_concentrated 33, setup_rejected:bundled_buys 24, setup_rejected:b_received 20, setup_rejected:rc_danger:Low Liquidity 11, cooldown_after_loss 9, setup_rejected:rc_danger:Creator history of rugged tokens 7, setup_rejected:unknown:lp_lock 6, max_open_positions 1

================================================================
PAPER BOOK C: copy-trading watched wallets (30s delay, mirror exits)
  pricing: model | start $500.00 on 2026-11-24 09:00 UTC
================================================================
equity $428.15 (-14.4%) | cash $404.48 | open 1 | max drawdown -15.5%
ledger reconciles: YES (cash + open cost = start + realized P&L)
closed 14 | win 3/14 (21%) | avg net -22.0% | realized $-73.77 | expectancy $-5.27/trade
exits: mirror_sell 12, stop 2
  (n=14 < 100: noise, not evidence)
open:
  santa        cost $21.75  now $23.67 (+8.8%)  held 10.0h
last trades:
  Caiolo       $21.91 -> $11.85 (-45.9%)  stop  0.2h
  Caiolo       $21.41 -> $33.10 (+54.6%)  mirror_sell  0.5h
  test         $21.99 -> $18.31 (-16.7%)  mirror_sell  0.0h
  LOBBY        $21.81 -> $30.42 (+39.5%)  mirror_sell  0.0h
  GIVE         $22.24 -> $17.38 (-21.9%)  mirror_sell  0.0h
  COSMOS       $21.99 -> $18.46 (-16.0%)  mirror_sell  0.0h
  Pnp          $21.82 -> $20.41 (-6.5%)  mirror_sell  0.2h
  Max          $21.71 -> $13.01 (-40.1%)  mirror_sell  0.3h
signals skipped by the sizer/risk rules: copy:liquidity_too_low 267, copy:no_pool 57, daily_loss_limit 53, copy:no_price_at_delay 30

BOOK C per wallet  (watching 3 wallets, 1825 wallet trades seen)
wallet        label          closed  open  win%  avg net    P&L $
HSq83t…YPbW   v2-near-hold4       7     1   29%    -1.0%    -1.87
CdF2qk…TyLu   v2-pass             1     0    0%   -45.9%   -10.06
EDBMUo…Zfj7   t2-GTAVI/XV-a       6     0   17%   -42.4%   -61.84
Drop wallets with negative expectancy after ~20 copied trades each.

Sampling is every scan cycle (~10 min), so intra-candle wicks are missed.
Not financial advice. Paper results overstate live results.
```
