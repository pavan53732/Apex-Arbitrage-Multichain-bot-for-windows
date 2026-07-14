# Apex Arbitrage

A **real, working** cross-venue arbitrage detection bot with a backend API and a
live WebSocket stream. It scans token prices across multiple DEX "venues",
detects profitable **direct (cross-venue)** and **triangular** arbitrage
opportunities, scores them net of fees and slippage, and (optionally) executes
them against a paper portfolio.

This is a functioning application with a passing end-to-end test suite — not a
skeleton. Every source file under `src/` contains real logic.

## Architecture

```
src/
  index.js                 # entrypoint: wires config, store, source, engine, server
  config.js                # config loader (+ env overrides)
  logger.js                # leveled console logger
  pricing/
    priceSource.js         # PriceSource base + market builder
    coingeckoSource.js     # real live prices (CoinGecko, aggregate USD)
    mockSource.js          # deterministic market with real cross-venue mispricing
    index.js               # factory: createPriceSource(config)
  arbitrage/
    profit.js              # fee / slippage / net-multiplier math
    detector.js            # direct + triangular opportunity detection
  engine/
    engine.js              # scan loop, event emitter, auto-execute
    executor.js            # simulated trade executor (paper portfolio)
  storage/
    store.js               # JSON-file / in-memory persistence
  server/
    app.js                 # Express REST + WebSocket live stream
test/
  unit/                    # profit math, detector
  integration/             # engine, executor, price sources
  e2e/                     # HTTP API + WebSocket stream
```

## Run it

```bash
npm install
npm start                 # boots API on :8080 (mock pricing, engine off)

# or with options
APEX_PORT=8080 \
APEX_PRICE_SOURCE=mock \      # 'mock' (default) or 'coingecko' (live prices)
APEX_ENGINE_ENABLED=true \    # start scanning immediately
APEX_AUTO_EXECUTE=true \      # simulate executing top opportunities
node src/index.js
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | liveness + engine status |
| GET | `/config` | public venues / tokens / engine settings |
| GET | `/prices` | latest market snapshot |
| GET | `/opportunities` | detected opportunities (newest first) |
| GET | `/trades` | executed (simulated) trades |
| GET | `/stats` | scans, profits, paper balance |
| POST | `/engine/start` | start the scan loop |
| POST | `/engine/stop` | stop the scan loop |
| POST | `/engine/scan` | run a single scan and return opportunities |
| WS | `/stream` | live `opportunities` / `trade` / `status` events |

## How detection works

- **Direct arbitrage**: buy a token at the cheapest venue, sell at the dearest.
  Net multiplier = `(priceMax/priceMin) · (1−fees) · (1−slippage)`.
- **Triangular arbitrage**: route `USD → A → B → C → USD`, choosing the best
  venue per leg, net of per-leg fees and slippage.
- An opportunity is reported only when `netProfit% ≥ minProfitPct` and total
  slippage stays under `maxSlippagePct`.

## Tests

```bash
npm test                  # all suites (unit + integration + e2e)
npm run test:unit
npm run test:integration
npm run test:e2e
```

## Notes on data sources

- `mock` (default) produces a deterministic market with genuine cross-venue
  mispricing, so the bot demonstrably finds and executes arbitrage out of the box.
- `coingecko` pulls **live** aggregate USD prices (no API key required). Because
  CoinGecko returns a single aggregate price per coin rather than per-venue
  order books, it shows real market prices but yields few cross-venue spreads.
  Wiring per-venue DEX order-book feeds (e.g. 1inch / DEX subgraphs) is the
  natural next step to find real-time arbitrage on live data.
