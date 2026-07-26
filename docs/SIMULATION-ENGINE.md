# Simulation Engine

## Purpose
Defines paper trading, replay, stress testing, and synthetic failure simulation.

## Supported modes
- Paper trading.
- Historical replay.
- Tick-by-tick replay.
- Order book simulation.
- Liquidity simulation.
- Gas simulation.
- Network congestion.
- RPC failures.
- Oracle failures.
- Wallet failures.
- Chain reorganisations.
- AI decision simulation.
- Monte Carlo.
- Stress testing.
- Black swan scenarios.
- Regression testing.
- Benchmark testing.

## Rules
- Simulation must use the same decision paths as live trading wherever possible.
- All synthetic failures must be reproducible from a seed and fixture id.
- Simulation must never broadcast to production chains.

## Cross-references
- `docs/BACKTESTING.md`
- `docs/STRATEGIES.md`
- `docs/EXECUTION-ENGINE.md`
- `docs/AI-PIPELINE.md`
