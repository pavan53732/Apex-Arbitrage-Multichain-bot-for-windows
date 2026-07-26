# Simulation Engine

## Purpose
Defines paper trading, replay, stress testing, and synthetic failure simulation.

## Ownership
- Owns simulation modes, scenario definitions, deterministic replay, and result reporting.
- Consumes strategy, execution, AI, market, and runtime snapshots.

## Simulation modes
- Paper trading.
- Historical replay.
- Tick-by-tick replay.
- Order book simulation.
- Liquidity simulation.
- Gas simulation.
- Network congestion simulation.
- RPC failure simulation.
- Oracle failure simulation.
- Wallet failure simulation.
- Chain reorganisation simulation.
- AI decision simulation.
- Monte Carlo.
- Stress testing.
- Black swan scenarios.
- Regression testing.
- Benchmark testing.

## Determinism rules
- Same inputs and scenario seed must produce the same simulated outcome class.
- External live dependencies must be disabled unless explicitly marked hybrid.
- Scenario configuration, market snapshot, code version, and replay clock must be recorded.

## Scenario lifecycle
Defined -> Materialized -> Running -> Scored -> Stored -> Released.

### Transition rules
- Defined -> Materialized after scenario parameters are validated.
- Materialized -> Running when the harness starts execution.
- Running -> Scored when the run finishes or aborts safely.
- Scored -> Stored after metrics and artifacts are persisted.
- Stored -> Released when outputs are made available to consumers.

## Idempotency and retry
- Materializing the same scenario definition with the same seed must return the same scenario id.
- Replay execution must be repeatable and must not depend on wall-clock variance unless explicitly modeled.
- Retry is allowed only for harness or infrastructure faults, not to alter outputs.

## Failure and recovery
- Invalid scenario inputs must fail closed with a stable error code.
- Interrupted runs must not contaminate subsequent runs or shared state.
- Live side effects are forbidden unless the scenario is explicitly configured for hybrid integration.

## Persistence
- Persist scenario ids, seeds, market snapshots, configuration hashes, code versions, outputs, metrics, and artifact locations.
- Persist regression baselines and comparison deltas.

## Monitoring
- Scenario execution latency.
- Regression pass/fail rate.
- Resource consumption.
- Harness failure rate.

## Cross-references
- `BACKTESTING.md`
- `STRATEGIES.md`
- `EXECUTION-ENGINE.md`
- `AI-PIPELINE.md`
- `TESTING-GUIDE.md`
