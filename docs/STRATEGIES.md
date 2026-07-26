# Strategies

## Purpose
Authoritative strategy specification.

## Shared lifecycle
Discover -> Evaluate -> Validate -> Size -> Approve -> Execute -> Monitor -> Exit -> Reconcile -> Learn.

## Supported strategies
### Arbitrage
Detects price spreads and executes synchronized buy/sell actions. Requires quote freshness, gas accounting, and slippage limits.

### Triangular Arbitrage
Uses three-asset loops; requires route consistency and atomic execution where possible.

### Cross-DEX Arbitrage
Captures price deltas between DEXs on the same chain. Requires routeable liquidity and MEV awareness.

### Cross-Chain Arbitrage
Uses cross-chain mispricing; requires bridge latency modeling and finality checks.

### Flash Loan Arbitrage
Requires atomic bundle support and repayment validation.

### Statistical Arbitrage
Requires calibrated statistical thresholds and regime detection.

### Grid Trading
Requires capital partitioning, staggered bands, and rebalancing.

### Scalping
Requires low latency, tight spreads, and rapid cancellation/replacement.

### Momentum
Requires trend confirmation and volume support.

### Mean Reversion
Requires overextension detection and bounded drawdown.

### Market Making
Requires inventory control and spread management.

### Liquidity Provision
Requires impermanent loss modeling and reward tracking.

### Yield Farming
Requires reward estimation and risk gating.

### Dollar-Cost Averaging
Requires schedule validation and budget caps.

### Swing Trading
Requires trend and volatility support.

### AI-assisted strategies
AI may rank or suggest, but never bypass deterministic risk checks.

### Hybrid strategies
Combine multiple archetypes while preserving explicit component rules.

## Cross-references
- Execution: `EXECUTION-ENGINE.md`.
- Risk: `RISK-ENGINE.md`.
- Simulation: `SIMULATION-ENGINE.md`.
- AI: `AI-PIPELINE.md`.

