# TrenchLab v0.1

A **read-only** Solana memecoin trench scanner and outcome lab.

It never signs transactions, never asks for a private key, and never touches your wallet. It only reads public data and writes to a local database file (`trenchlab.db`).

## What it does

Every 5 minutes it runs these steps:

1. **SCOUT.** Pulls new and trending Solana pools from GeckoTerminal (free, no key) and applies the trench filters:
   - liquidity above $30k
   - 1h volume above liquidity
   - more buys than sells
   - pool age between 1h and 12h
   - at least 150 unique buyers
   - at most 3 buys per buyer (anti-wash)
   - not up more than 80% in the last hour
   - a `HEATING_UP` flag when 5-min volume × 12 > 1h volume
2. **ANALYST.** Scores the survivors from 0 to 100 and logs every component.
3. **AUDITOR.** Runs RugCheck and GoPlus. It kills on:
   - active mint or freeze authority
   - LP not locked
   - top-10 holders above 30%
   - RugCheck "danger" risks
   - **missing or unknown data**
4. **LOGGER.** Saves **every** pool, passed or killed, with its reasons.
5. **LAB.** Keeps sampling each pool's price for 24 hours, so we learn what actually happened.

`report` then shows you, with data:

- which rules kill losers and which might be killing winners
- whether the score predicts anything
- which stop and trailing-exit combination has the best average return **after costs**

## How it runs: GitHub Actions, no PC needed

`.github/workflows/scan.yml` runs one scan every ~10 minutes on GitHub's free servers.

- **Live report:** [`REPORT.md`](REPORT.md) is updated every run. Open it on GitHub any time, including from your phone.
- **Data:** the database is stored compressed as `trenchlab.db.gz` on the [`data` release](../../releases/tag/data). It is not committed to git, which keeps the repo small. A rolling weekday backup sits next to it.
- **Manual run:** go to the Actions tab → trench-scan → Run workflow.
- **Telegram (optional):** go to repo Settings → Secrets and variables → Actions and add `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.

## Optional: run on Windows instead

1. Check you have Python 3.10 or newer: open **Command Prompt** and type `python --version`. If that fails, install it from python.org and tick **"Add Python to PATH"**.
2. Unzip this folder somewhere, for example `Documents\trenchlab`.
3. Double-click **`test.bat`**. It should end with `OK`.
4. Double-click **`probe.bat`**. This saves raw API responses into `probe\`. Send that folder back to Claude so it can confirm the data fields are read correctly.

No pip installs and no API keys are needed. It uses the Python standard library only.

## Daily use

| File | What it does |
|---|---|
| `scan.bat` | One scan now, prints the table |
| `run.bat` | Runs forever, every 5 min, collecting data. Leave it open. Ctrl+C to stop. |
| `report.bat` | The lab report |

The table shows:

- `OK`: final pass (paper signal only)
- `~`: passed scout but killed by score or audit (the reason is shown)

### Optional: Telegram alerts

Create a bot with @BotFather and get your chat ID. Then, in Command Prompt, before running:

```
set TELEGRAM_BOT_TOKEN=123:abc
set TELEGRAM_CHAT_ID=123456
run.bat
```

## Rules of the lab

- Thresholds live in `config.json`. **Don't change them mid-experiment.** Change them between experiments, in writing, and note the date.
- Judge by **average net return per trade** (expectancy), not win rate.
- Don't trust any result with n < 100 trades.
- Paper results overstate live results. Before real money, run a tiny live test ($20–50) to measure the gap.
- No scanner can make a token rug-proof. Always check holders and Bubblemaps yourself.

Not financial advice.

## Roadmap

- **v0.2 (live):** cabal finder. It traces who funded each top-20 holder using 1-credit Helius RPC calls, links wallets that share a funder (ignoring busy exchange-like funders), and kills on: largest linked cluster > 15% of supply, total clustered > 30%, fresh wallets > 40%. A daily credit budget keeps it inside the free plan. Near-miss pools are also analysed for research, so the `CABAL CHECK` report section can test whether the signal predicts rugs. The `HELIUS_API_KEY` repo secret is required.
- **later:** same-block sniper detection, two-hop funding, supply received vs bought
- **v0.3 (live):** paper trader. Every FINAL PASS becomes a simulated trade on a $500 paper bank:
  - **sizing:** 0.5% risk per trade with a −10% stop, so $25 positions
  - **limits:** at most 2 open, at most 20% exposure, one entry per token, a 30-min cooldown after a loss, and a 3% daily loss limit
  - **exits:** stop, a trailing stop (armed at +20%, trails 10%), a 24h time stop, and "dead" after 6 cycles without a price (valued at $0)
  - **pricing:** constant-product model from the pool's own liquidity plus fees, or real Jupiter quotes when the `JUPITER_API_KEY` secret is set (free key at portal.jup.ag)
  - **report:** the `PAPER TRADER` section, with a ledger reconciliation check
- **v0.4 (live, 2026-11-07):** paper **book B, "pullback"**. It runs next to book A with the same $500 start, sizing, exits and costs, so only the entry rule differs. B buys tokens 2–24h old that are 30–60% below their high, have bounced at least 5% off a low that is at least 20 min old, still have $30k+ liquidity (at least 50% of their peak), have buyers back (75+ buyers/h, buys ≥ sells), pass the audit, and pass stricter cabal checks (bundled ≤ 5%, fresh ≤ 20%, received ≤ 10%). The report shows an `A vs B` table.
- **later:** wallet Copyability Score; chain-heat monitor; Robinhood Chain support
