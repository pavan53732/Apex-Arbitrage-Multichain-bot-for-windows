# Simulation Engine

## Purpose
Defines paper trading, replay, stress testing, and synthetic failure simulation.

## Ownership
- Owns simulation modes, scenario definitions, deterministic replay, and result reporting.
- Consumes strategy, execution, AI, market, and runtime snapshots.

## Shared simulation contract
Simulation entities and accuracy metrics are defined by `DOMAIN-MODEL.md` and `METRICS.md`.
Every simulation defines purpose, inputs, configuration, initial state, execution flow, expected outputs, validation criteria, success metrics, failure scenarios, and recovery behaviour.

## Determinism rules
- Same inputs and scenario seed must produce the same simulated outcome class.
- External live dependencies must be disabled unless explicitly marked hybrid.
- Scenario configuration, market snapshot, code version, and replay clock must be recorded.

## Scenario lifecycle
Defined -> Materialized -> Running -> Scored -> Stored -> Released.

## Simulation modes
- Paper Trading.
- Historical Replay.
- Tick-by-Tick Replay.
- Order Book Simulation.
- Liquidity Simulation.
- Gas Simulation.
- Network Congestion.
- RPC Failures.
- Oracle Failures.
- Wallet Failures.
- Chain Reorganisations.
- AI Decision Simulation.
- Monte Carlo.
- Stress Testing.
- Black Swan Scenarios.
- Regression Testing.
- Benchmark Testing.

## Mode specifications

### Paper Trading
Purpose: validate live workflow with simulated settlement.
Inputs: live-like market snapshots and strategy output.
Configuration: paper mode, no real submission, realistic fees.
Initial state: clean simulated account and portfolio.
Execution flow: generate decisions, simulate fills, update state, reconcile.
Expected outputs: paper fills, PnL, risk state, alerts.
Validation criteria: no live side effects, state consistency.
Success metrics: fill realism, deterministic replay, low drift.
Failure scenarios: missing quotes, stale state, rejected decision.
Recovery behaviour: reset simulated state and replay from checkpoint.

### Historical Replay
Purpose: replay historical market snapshots through live logic.
Inputs: historical snapshots and versioned config.
Configuration: start/end time, seed, version pin.
Initial state: restored from replay checkpoint.
Execution flow: step through snapshots, score, execute simulated actions.
Expected outputs: decisions, fills, PnL, logs.
Validation criteria: deterministic output for identical inputs.
Success metrics: replay fidelity and baseline comparison.
Failure scenarios: missing data, version mismatch.
Recovery behaviour: resume from last completed checkpoint.

### Tick-by-Tick Replay
Purpose: simulate tick-level decision timing.
Inputs: tick stream, quote updates, strategy config.
Configuration: tick mode, cadence, seed.
Initial state: zeroed tick cursor.
Execution flow: process each tick sequentially.
Expected outputs: tick-aligned decisions and fills.
Validation criteria: exact ordering and repeatability.
Success metrics: latency fidelity and decision stability.
Failure scenarios: dropped tick, clock drift.
Recovery behaviour: restart from preserved tick index.

### Order Book Simulation
Purpose: emulate order book depth and queue effects.
Inputs: book snapshots, spread, depth, strategy intent.
Configuration: slippage model and match rules.
Initial state: synthetic book state.
Execution flow: match orders against depth and update book.
Expected outputs: fills, partial fills, remaining depth.
Validation criteria: book conservation and consistent matching.
Success metrics: fill realism and slippage accuracy.
Failure scenarios: depth collapse, spread shock.
Recovery behaviour: restore from prior book snapshot.

### Liquidity Simulation
Purpose: test impact of shallow liquidity.
Inputs: depth curves, route candidates, order size.
Configuration: liquidity stress level.
Initial state: baseline depth state.
Execution flow: apply impact and determine fill quality.
Expected outputs: slippage, partial fills, rejects.
Validation criteria: expected price impact and rejection rules.
Success metrics: liquidity sensitivity fidelity.
Failure scenarios: sudden depth loss.
Recovery behaviour: reset to prior depth snapshot.

### Gas Simulation
Purpose: model fee volatility and transaction economics.
Inputs: gas estimates, fee market, chain state.
Configuration: gas curve and replacement policy.
Initial state: fee baseline.
Execution flow: recalculate route economics under fee changes.
Expected outputs: net edge after gas, replacement signals.
Validation criteria: fee impact and replacement decision consistency.
Success metrics: gas cost realism.
Failure scenarios: fee spike, base fee shock.
Recovery behaviour: reprice and re-evaluate.

### Network Congestion
Purpose: simulate submission delay and queueing pressure.
Inputs: congestion model, RPC latency, mempool pressure.
Configuration: latency multiplier and timeout budget.
Initial state: normal network conditions.
Execution flow: delay broadcasts and confirmations.
Expected outputs: delayed fills, timeouts, retries.
Validation criteria: timeout handling and backoff correctness.
Success metrics: delay fidelity.
Failure scenarios: congestion saturation.
Recovery behaviour: continue from delay-adjusted state.

### RPC Failures
Purpose: validate provider outage handling.
Inputs: RPC error schedule and retry policy.
Configuration: failure injection profile.
Initial state: healthy provider.
Execution flow: force transient or terminal RPC errors.
Expected outputs: retries, failover, hard rejects.
Validation criteria: bounded retry and failover correctness.
Success metrics: recovery rate and rejection correctness.
Failure scenarios: sustained outage.
Recovery behaviour: switch provider or fail closed.

### Oracle Failures
Purpose: validate missing or corrupted oracle inputs.
Inputs: oracle stream and corruption schedule.
Configuration: oracle trust policy.
Initial state: valid oracle state.
Execution flow: inject stale or invalid oracle data.
Expected outputs: reject, pause, alert.
Validation criteria: no decisions on invalid oracle data.
Success metrics: safe rejection and alerting.
Failure scenarios: stale oracle, conflict, outage.
Recovery behaviour: resume only after clean oracle state.

### Wallet Failures
Purpose: validate signing and balance failures.
Inputs: wallet state, nonce state, balance constraints.
Configuration: signing policy and recovery policy.
Initial state: unlocked wallet or simulated wallet.
Execution flow: inject signing errors and balance shortages.
Expected outputs: rejection, retry, halt.
Validation criteria: fail-closed safety and nonce correctness.
Success metrics: safe handling of signing faults.
Failure scenarios: locked wallet, insufficient balance.
Recovery behaviour: reconcile wallet state and retry if safe.

### Chain Reorganisations
Purpose: validate reorg resilience.
Inputs: reorg depth, confirmation policy, transaction history.
Configuration: finality threshold and rollback policy.
Initial state: confirmed transaction state.
Execution flow: rewind affected states and re-evaluate.
Expected outputs: reorg alerts, state rollback, reconciliation.
Validation criteria: no false finality, accurate rollback.
Success metrics: reorg handling correctness.
Failure scenarios: deep reorg.
Recovery behaviour: reconcile to canonical chain state.

### AI Decision Simulation
Purpose: validate AI routing, confidence, and safety gates.
Inputs: prompts, model outputs, evaluation configs.
Configuration: provider set and fallback policy.
Initial state: deterministic prompt set.
Execution flow: produce candidate output, validate, score, and compare.
Expected outputs: confidence, reject reasons, selected model.
Validation criteria: same input yields same output class.
Success metrics: calibration and safety adherence.
Failure scenarios: malformed output, provider failover.
Recovery behaviour: fallback to approved model or human review.

### Monte Carlo
Purpose: estimate distribution of outcomes.
Inputs: stochastic parameter ranges and seeds.
Configuration: trial count and distribution definitions.
Initial state: baseline strategy state.
Execution flow: run many randomized scenarios.
Expected outputs: outcome distributions and percentiles.
Validation criteria: reproducible with same seed set.
Success metrics: distribution stability.
Failure scenarios: invalid distribution, insufficient sample.
Recovery behaviour: rerun with corrected config.

### Stress Testing
Purpose: validate resilience under adverse conditions.
Inputs: degraded liquidity, higher gas, delayed confirmations.
Configuration: stress multipliers.
Initial state: normal operating baseline.
Execution flow: apply combined stressors.
Expected outputs: rejects, slower fills, lower PnL.
Validation criteria: no unsafe live-side effects.
Success metrics: safe failure behavior.
Failure scenarios: overloaded queue, repeated rejections.
Recovery behaviour: reduce stress or halt.

### Black Swan Scenarios
Purpose: test catastrophic tail events.
Inputs: sudden price gap, chain failure, provider outage.
Configuration: extreme shock profile.
Initial state: baseline state.
Execution flow: inject extreme shocks simultaneously.
Expected outputs: emergency stop, alerts, minimal damage.
Validation criteria: fail-closed and recoverable.
Success metrics: containment and safe halt.
Failure scenarios: compounding loss conditions.
Recovery behaviour: manual recovery and reconciliation.

### Regression Testing
Purpose: ensure unchanged behavior across releases.
Inputs: pinned cases, baseline outputs.
Configuration: version pin and tolerance thresholds.
Initial state: reference baseline state.
Execution flow: compare current outputs to expected.
Expected outputs: pass/fail deltas and drift report.
Validation criteria: all must match baseline tolerance.
Success metrics: low drift.
Failure scenarios: output drift, missing baseline.
Recovery behaviour: update baseline only after review.

### Benchmark Testing
Purpose: measure performance and capacity.
Inputs: representative workloads and timing harness.
Configuration: concurrency and repetition count.
Initial state: performance baseline.
Execution flow: run workloads and measure metrics.
Expected outputs: latency, throughput, resource usage.
Validation criteria: performance targets met.
Success metrics: target compliance.
Failure scenarios: saturation, timeout, resource exhaustion.
Recovery behaviour: scale or tune configuration.

## Persistence
Persist scenario ids, seeds, market snapshots, configuration hashes, code versions, outputs, metrics, and artifact locations.

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

- `DOMAIN-MODEL.md`

- `METRICS.md`


For canonical entities and performance tracking, see `DOMAIN-MODEL.md` and `METRICS.md`.


## Enterprise Contract – Simulation Engine
- Interfaces: `INTERFACE-TOOL-CALL.md`.
- State machine: `TRADING-LIFECYCLE.md`, `EXECUTION-LIFECYCLE.md`.
- Security boundaries: `SECURITY-CONTRACTS.md`.
- Performance SLOs: `PERFORMANCE-SLOS.md`.
- Failure modes: non-deterministic simulation, stale market data, invalid assumptions; recover via deterministic replay and abort.

For trading lifecycle, see `TRADING-LIFECYCLE.md`.
For execution lifecycle, see `EXECUTION-LIFECYCLE.md`.
For performance targets, see `PERFORMANCE-SLOS.md`.
## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define deterministic timing, headless mode, and Windows replay concerns.

## Simulation rules
- Define deterministic timing, headless mode, and Windows replay behavior.
- Define result comparison and failure reporting.
