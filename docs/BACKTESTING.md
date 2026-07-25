# APEX Backtesting Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Replay historical data through APEX strategies to evaluate performance before going live.

---

## 1. Overview

Backtesting lets you run APEX's skills against **historical market data**
instead of live feeds. The engine simulates:

- Market data replay (block-by-block)
- Skill execution at the appropriate timestamps
- AI calls (cached from real historical responses, or re-run)
- Trade execution against the historical chain state (via mainnet fork)

You get:
- P&L curve
- Trade log
- Risk metrics (Sharpe, Sortino, max drawdown, win rate)
- Comparison across parameter sets (A/B)

---

## 2. Why Backtest?

- **Validate a strategy** before risking capital
- **Tune parameters** (min profit, slippage, gas strategy) to historical data
- **Stress test** against past black-swan events (Terra/Luna, FTX, etc.)
- **Compare AI models** to see which produces better decisions
- **A/B test system prompts** for the agents

---

## 3. The Backtest Engine

### 3.1 Architecture
```
┌─────────────────────┐
│ Backtest Config     │  (JSON or UI)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Data Loader         │  (historical blocks, prices, AI responses)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Strategy Engine     │  (same as live; takes time parameter)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Simulator           │  (fork replay or simulated execution)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Metrics + Reporter  │  (P&L, risk, charts, export)
└─────────────────────┘
```

### 3.2 Two Modes

#### 3.2.1 Replay Mode (Fast)
- Replay historical price feed + gas + bridge fees
- AI calls use **cached historical responses** (no re-runs)
- Execution is **simulated** (not on a fork): APEX applies slippage/gas/fee models
- Speed: hours of data in seconds
- Best for: parameter sweep, A/B tests, large ranges

#### 3.2.2 Fork Mode (Realistic)
- Spins up a mainnet fork at a historical block
- Re-runs AI calls in real time
- Executes trades against the fork (using real DEX code)
- Speed: hours of data in minutes (depending on data density)
- Best for: validating top strategies before going live

---

## 4. Data Sources

### 4.1 Built-in
APEX downloads and caches:
- **Token prices** (1-min candles, 1y+ history): CoinGecko, DefiLlama
- **Block-level chain state** (logs, transfers): via The Graph, or self-hosted archive node
- **Gas prices**: from chain explorers
- **DEX events** (Swaps, Mints, Burns): The Graph subgraphs

### 4.2 User-provided
- CSV of trades / prices
- Custom backtest data via the `backtest-data-tool` CLI

### 4.3 Data Quality
Each data source is tagged with:
- Source, fetch timestamp, freshness
- Confidence (e.g. low for derived data)
- The backtest report flags low-confidence data ranges

---

## 5. Running a Backtest

### 5.1 From the UI
**Dashboard → Backtest → New Backtest**

1. **Name** your backtest
2. **Date range** (e.g. 2026-01-01 to 2026-06-30)
3. **Chains** (multi-select)
4. **Skills** to include
5. **Initial capital** (USD)
6. **Mode** (Replay / Fork)
7. **Parameter overrides** (optional)
8. **AI model** (if Fork mode)
9. Click **Start**

Live progress bar; estimated time remaining; ETA.

### 5.2 From the CLI (Advanced)
```bash
npm run backtest -- \
  --config=./configs/bt-flash-arb.json \
  --mode=fork \
  --from=2026-01-01 \
  --to=2026-06-30 \
  --output=./results/bt-flash-arb-2026H1.json
```

Config file:
```json
{
  "name": "Flash Loan Arb 2026 H1",
  "skills": ["flash-loan-arb"],
  "chains": [1, 42161, 137],
  "initial_capital_usd": 10000,
  "params": {
    "flash-loan-arb": {
      "min_profit_usd": 5,
      "max_gas_gwei": 100,
      "use_private_pool": true
    }
  },
  "ai_model": "gpt-4o",
  "risk_limits": {
    "max_position_usd": 1000,
    "max_daily_loss_usd": 500
  }
}
```

---

## 6. The Report

Each backtest produces a report with:

### 6.1 Headline Metrics
- **Total P&L** (USD and %)
- **Win rate** (% of profitable trades)
- **Number of trades**
- **Average profit per trade**
- **Sharpe ratio** (risk-adjusted return)
- **Sortino ratio** (downside-risk-adjusted)
- **Max drawdown** (% and USD)
- **Average trade duration**
- **Gas spent** (total, % of P&L)
- **AI cost** (total, $ per trade)

### 6.2 Equity Curve
A line chart of portfolio value over time, with:
- Drawdown overlay
- Trade markers (up = win, down = loss)
- Regime shading (high vol, etc.)

### 6.3 Trade Log
Sortable, filterable table of every simulated trade:
- Timestamp, chain, pair, side, size
- Expected vs actual profit
- Slippage, gas, AI confidence
- Outcome (win/loss/error)
- Reasoning (the AI's explanation)

### 6.4 Per-Skill Breakdown
- Skill name
- Trades, win rate, total P&L, Sharpe
- Best/worst trade
- Average latency

### 6.5 Comparison
If you ran multiple backtests with different params, a side-by-side comparison
table + overlay chart.

### 6.6 Export
- JSON (full raw data)
- CSV (trade log)
- PDF (formatted report)
- Markdown (for sharing)

---

## 7. A/B Testing

To compare two configurations:
1. Run Backtest A with config 1
2. Run Backtest B with config 2
3. Open **Backtest → Compare**
4. Select A and B → see side-by-side

The comparison highlights statistically significant differences (t-test on
P&L distributions, etc.).

Common A/B tests:
- AI model: `gpt-4o` vs `claude-sonnet-4-20250514`
- System prompt version
- Parameter set (e.g. min_profit_usd = 5 vs 10)
- Skill enabled/disabled

---

## 8. Stress Testing

Built-in stress scenarios replay historical black-swan events:
- **Terra/Luna crash** (May 2022)
- **FTX collapse** (Nov 2022)
- **Euler exploit** (March 2023)
- **Curve reentrancy** (July 2023)
- **Custom date range** (any user-defined)

The engine replays the exact market conditions (price action, gas spikes,
liquidity drops) to see how the strategy would have performed.

---

## 9. Walk-Forward Optimization

To avoid overfitting:
1. Split data into train/test (e.g. 70/30)
2. Run optimization on train (find best params)
3. Test those params on test (out-of-sample)
4. If profitable on both → strategy has signal
5. If only on train → overfit, do not deploy

The engine supports automated walk-forward:
```bash
npm run backtest:walk-forward -- --train-pct=70 --step-days=30
```

---

## 10. Caveats

Backtesting is **not a guarantee** of future performance. Known pitfalls:

- **Survivorship bias** — only successful tokens/DEXes are in the data
- **Look-ahead bias** — easy to accidentally use future data
- **Slippage modeling** — historical slippage ≠ future slippage
- **Gas modeling** — historical gas ≠ future gas
- **AI calls** — same prompt may produce different responses over time
- **Liquidity** — a backtest may not capture thin-book moments

Always:
- Use out-of-sample testing
- Paper trade before going live
- Start with small capital
- Monitor continuously

---

## 11. Implementation Notes

- Backtest engine is in `packages/backtest/`
- Replay mode is pure TypeScript, runs anywhere
- Fork mode uses Hardhat mainnet forking under the hood
- AI responses are cached in `backtest_cache` table; can be pre-warmed
- Reports are persisted to `backtest_runs` and `backtest_results` tables

---

## 12. API

```ts
import { backtest } from '@/backtest';

const run = await backtest.start({
  name: 'Test run',
  skills: ['flash-loan-arb'],
  chains: [1],
  from: '2026-01-01',
  to: '2026-06-30',
  mode: 'replay',
  initialCapitalUsd: 10000,
  params: { 'flash-loan-arb': { min_profit_usd: 5 } },
});

await backtest.waitForCompletion(run.id);
const report = await backtest.getReport(run.id);
```

---

*Backtest before you trade. Then backtest some more.*
