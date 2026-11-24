-- TrenchLab: early, profitable, non-bot buyers of CoreSight ALPHA winners (Solana)
-- Paste into https://dune.com/queries/new and click Run. Read-only analysis.
-- Winners + call times come from CoreSight's public leaderboard (research/coresight_winners.json).
--
-- For each wallet that bought >= 2 winners BEFORE CoreSight called them:
--   pnl_winners_usd       realized USD on those winners (sells - buys; unsold bags count as 0)
--   median_sec_after_launch / snipes   how soon after the token's first trade it bought
--   tokens_bought_nov / trades_nov     breadth: bots buy hundreds of tokens a month
--   all_tokens_net_usd_nov SOL out minus SOL in across EVERY token it traded in November:
--                         the honest check - did it make money overall, not just on known winners?

WITH winners (mint, symbol, called_at) AS (
  VALUES
    ('BECqBzwZmkzM7A3tWimc2qvm7ookzYi8XACHMZgipump', 'THANKS', TIMESTAMP '2026-11-23 23:07:47'),
    ('Czbd4FtkLf4ELCPNuawbGxcivuCpcLWFFTD4oqWkpump', 'TORQUE', TIMESTAMP '2026-11-23 18:37:00'),
    ('Ddnd1DGVjtE2DT3ZjDXZsNzu6oHbe3GEj5VE9x6avYsA', 'TUGI', TIMESTAMP '2026-11-23 16:05:06'),
    ('2YVAMEteGo2a78TnywsvzMyAGhVpZWynCHJPVYZnZQFj', 'HALO', TIMESTAMP '2026-11-23 13:27:19'),
    ('9AiHB952pXVrHuct9m3RKWoWv4LG52p58FYjMvUkpump', 'HOLD', TIMESTAMP '2026-11-23 09:58:49'),
    ('65ksadfsLqqGt42imSTVSrmV578aksSFzgpGge3dpump', 'AMBER', TIMESTAMP '2026-11-24 01:48:48'),
    ('4ZgqnNi53sRKKegFpYefFjsFE6zQ3T64Xkavcoh7pump', 'CHIBI', TIMESTAMP '2026-11-24 01:57:32'),
    ('5EBsafq3gSutzc9BBieAe5F6YWxstTNgbsJa1iZ737Zx', 'TOGI', TIMESTAMP '2026-11-23 16:00:02'),
    ('FvktmXnnZnoVuLYgdo1FSXeydthfhFC7P8orYCEmpump', '3sat', TIMESTAMP '2026-11-24 05:33:11'),
    ('7Kn92xBncvzp8FUrmZKFnEDd7wS3iLAugr5A8vWBpump', 'P', TIMESTAMP '2026-11-23 23:10:51'),
    ('E2VqbQW3RHGXqfPVZxQGaUfqfipMoQuzWavz6jNfpump', 'GTA 6 Coin', TIMESTAMP '2026-11-23 03:31:04'),
    ('4VMS1tBfAJjEcpxKEyrzbLDYV74sN3dZoQQq3hfTpump', 'RULEBOOK', TIMESTAMP '2026-11-22 13:39:08'),
    ('CB1mdyDC3ZjMbviNPrbeNa9PJrA4q4oEzu4yVwNSpump', 'GTA 6 Coin', TIMESTAMP '2026-11-23 05:25:05'),
    ('v4GK8f24ZJJa5qLoTJ4mJ5d6jsNUXHScwGaRHdfpump', 'MCAT', TIMESTAMP '2026-11-22 13:19:23'),
    ('5KzT4p9dfHsnLWgXNXgAHEam2ZLrbAMRGqHDStQjpump', 'Trumpless', TIMESTAMP '2026-11-23 02:09:27'),
    ('HHXH6PCP6raTucs2zYFkpTHErntN7qJU9r97ECu6pump', 'JEANPHIL', TIMESTAMP '2026-11-22 18:51:11'),
    ('BKSP127UTT12VbipELqWMpLRw744Q36oyhirxC9Wpump', 'MooSom', TIMESTAMP '2026-11-22 09:10:45'),
    ('77gLMe1DMax8pgjGwQYrm5DBGYzLWtiBTMQxM9Jcpump', 'BiaoGe', TIMESTAMP '2026-11-22 08:00:11'),
    ('AUuJPgFkq7BGK4NmgHZMWyScddeUw9x4NizjFDgupump', 'XV', TIMESTAMP '2026-11-21 12:14:19'),
    ('8Wj18dstju6wghWDEsRdRzRmPTz8fD5Z5QwyfHjzpump', 'Share', TIMESTAMP '2026-11-21 14:13:53'),
    ('EoZL4GXLyCyoyh9AwVMqPQSuXh6K1xEwTWp9E8yQpump', 'valor', TIMESTAMP '2026-11-21 21:34:43'),
    ('EK2tRRD5jqNUxohdMjbjnJ5Q3t9TYGBkZVjtMceDpump', 'Emily', TIMESTAMP '2026-11-21 12:49:36'),
    ('7pq9QyFN1cPmC2Sdr3v4CxMcPM9vfNrbKMhxtpXNpump', 'Cyber', TIMESTAMP '2026-11-21 14:36:43'),
    ('GMQpVdb8kadCeCTaGM6jLJtMk49KoeDbECcDvAeBpump', 'BONK(pump)', TIMESTAMP '2026-11-17 21:37:23'),
    ('9J7wHgHQzyvZRcf7wHHXCAtiscRew8UUUH1jYpFmpump', 'GTAVI', TIMESTAMP '2026-11-18 09:24:09'),
    ('A9jbSQDkbdQrA37fYAPf4TSK2GBCuBcGikEmZaRGpump', 'GTAVI', TIMESTAMP '2026-11-21 07:04:31'),
    ('J51xgomTx21VHY62Q7uv2otWRUSq71WeaApLfsAnpump', 'PIPI', TIMESTAMP '2026-11-19 13:56:18'),
    ('GtGuiVyFuGGvDJbdS4tYRCqniB6is8tZiTN9Z7fSpump', 'Snowflake', TIMESTAMP '2026-11-20 04:58:25'),
    ('48UW5PSMpaN1x2YW3ArY4xEiKyP8bJTFfednCHMG3Jcx', 'SNUT', TIMESTAMP '2026-11-16 14:30:33'),
    ('AR29dTAsP9pFuB9ZSa4PpQgkc6nGK9ryRfDdzxhApump', 'SOLBULL', TIMESTAMP '2026-11-16 18:41:39'),
    ('FVzqGqRmr4UH1Fif6dewmwbJ1p4YUZCu8dcw4Efopump', 'HOGE', TIMESTAMP '2026-11-15 06:58:33'),
    ('4W7BNgGspH3YFbLsP5T7AnKAzr6REGMMBGK9xDZKpump', 'chudhaos', TIMESTAMP '2026-11-12 08:16:32'),
    ('84d6bCtraHtQZ2tvyNnshvEUA1ZStBBjfVpt5VS7pump', 'Naiwa', TIMESTAMP '2026-11-02 16:26:03'),
    ('5ca8A8ZJDQHPH8i1p6W7fs2H9D5cxq6sVUqEtqyNpump', 'GLAZE', TIMESTAMP '2026-11-06 14:47:07'),
    ('51SfaAyrYaR8FpibXT4TXtxEpnZSNoDwYVRojtKupump', 'Nothing', TIMESTAMP '2026-10-26 21:53:25'),
    ('69ddGhPEsRZcCcKZ2FCETSxpvbPFgL32senxeSnWpump', 'nut', TIMESTAMP '2026-11-01 04:22:51'),
    ('6kmkcwKxxmoREhkxrbBvwDY3N2KSfpdMMtWtNoPpump', 'LASTTRUCK', TIMESTAMP '2026-11-09 16:07:12')
),
t AS (
  SELECT w.symbol, w.mint, w.called_at, d.trader_id, d.block_time,
         CASE WHEN d.token_bought_mint_address = w.mint THEN 'buy' ELSE 'sell' END AS side,
         COALESCE(d.amount_usd, 0) AS usd
  FROM dex_solana.trades d
  JOIN winners w ON d.token_bought_mint_address = w.mint OR d.token_sold_mint_address = w.mint
  WHERE d.block_month >= DATE '2026-10-01'
),
first_trade AS (SELECT mint, MIN(block_time) AS t0 FROM t GROUP BY 1),
per AS (
  SELECT symbol, mint, trader_id, MAX(called_at) AS called_at,
         MIN(CASE WHEN side = 'buy' THEN block_time END) AS first_buy,
         SUM(CASE WHEN side = 'buy' THEN usd ELSE 0 END) AS buy_usd,
         SUM(CASE WHEN side = 'sell' THEN usd ELSE 0 END) AS sell_usd,
         COUNT(*) AS n_trades
  FROM t GROUP BY 1, 2, 3
),
early AS (
  SELECT p.*, date_diff('second', f.t0, p.first_buy) AS sec_after_launch
  FROM per p JOIN first_trade f ON f.mint = p.mint
  WHERE p.first_buy < p.called_at AND p.buy_usd >= 20
),
agg AS (
  SELECT trader_id,
         COUNT(*) AS winners_early,
         COUNT_IF(sell_usd > buy_usd) AS winners_in_profit,
         ROUND(SUM(sell_usd - buy_usd), 0) AS pnl_winners_usd,
         ROUND(SUM(buy_usd), 0) AS spent_on_winners_usd,
         approx_percentile(sec_after_launch, 0.5) AS median_sec_after_launch,
         COUNT_IF(sec_after_launch <= 10) AS snipes,
         array_join(array_agg(symbol), ', ') AS tokens
  FROM early
  GROUP BY 1
  HAVING COUNT(*) >= 2
),
breadth AS (
  SELECT d.trader_id,
         COUNT(DISTINCT CASE WHEN d.token_sold_mint_address = 'So11111111111111111111111111111111111111112' THEN d.token_bought_mint_address END) AS tokens_bought_nov,
         COUNT(*) AS trades_nov,
         ROUND(SUM(CASE WHEN d.token_sold_mint_address = 'So11111111111111111111111111111111111111112' THEN -COALESCE(d.amount_usd, 0)
                        WHEN d.token_bought_mint_address = 'So11111111111111111111111111111111111111112' THEN COALESCE(d.amount_usd, 0)
                        ELSE 0 END), 0) AS all_tokens_net_usd_nov
  FROM dex_solana.trades d
  JOIN agg a ON a.trader_id = d.trader_id
  WHERE d.block_month = DATE '2026-11-01'
  GROUP BY 1
)
SELECT a.trader_id AS wallet,
       a.winners_early, a.winners_in_profit, a.pnl_winners_usd, a.spent_on_winners_usd,
       a.median_sec_after_launch, a.snipes,
       b.tokens_bought_nov, b.trades_nov, b.all_tokens_net_usd_nov,
       CASE
         WHEN b.trades_nov > 3000 OR b.tokens_bought_nov > 400 THEN 'bot-like (too active)'
         WHEN a.snipes * 2 >= a.winners_early THEN 'launch sniper'
         WHEN a.pnl_winners_usd <= 0 THEN 'lost money on the winners'
         WHEN b.all_tokens_net_usd_nov <= 0 THEN 'loses money overall'
         ELSE 'CANDIDATE'
       END AS verdict,
       a.tokens,
       'https://solscan.io/account/' || a.trader_id AS solscan
FROM agg a
LEFT JOIN breadth b ON a.trader_id = b.trader_id
ORDER BY CASE WHEN b.trades_nov > 3000 OR b.tokens_bought_nov > 400 OR a.snipes * 2 >= a.winners_early
                   OR a.pnl_winners_usd <= 0 OR b.all_tokens_net_usd_nov <= 0 THEN 1 ELSE 0 END,
         b.all_tokens_net_usd_nov DESC
LIMIT 300
