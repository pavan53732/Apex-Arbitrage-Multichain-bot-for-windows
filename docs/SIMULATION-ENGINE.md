# Simulation Engine

## Purpose
This document is the authoritative implementation specification for simulation, replay, synthetic failure testing, and deterministic validation of strategies, execution, AI decisions, and runtime operations.

## Shared simulation contract
Every simulation must define purpose, inputs, configuration, initial state, execution flow, expected outputs, validation criteria, success metrics, failure scenarios, and recovery behavior.

## Common lifecycle
Select scenario -> initialize state -> run deterministic simulation -> collect outputs -> validate -> persist metrics -> reset state.

## Paper Trading
Purpose: validate live-like trading behavior without production chain exposure.
Inputs: market data, strategy config, wallet constraints, AI outputs.
Configuration: paper mode on, chain broadcast disabled.
Initial state: synthetic balances and virtual positions.
Execution flow: generate opportunities, simulate orders, simulate fills, reconcile outcomes.
Expected outputs: simulated fills, PnL, and decision traces.
Validation criteria: no production transaction emission and consistent accounting.
Success metrics: fill accuracy, accounting consistency, and replay determinism.
Failure scenarios: stale market data, simulated execution failure, and recovery timeouts.
Recovery behavior: reset virtual state and continue scenario from last safe checkpoint.

## Historical Replay
Purpose: replay past market conditions deterministically.
Inputs: historical market data and strategy rules.
Configuration: fixed dataset range and deterministic seed.
Initial state: historic starting portfolio and balances.
Execution flow: step through historical events and evaluate decisions.
Expected outputs: reproducible fills and decision traces.
Validation criteria: identical outputs for identical seed and dataset.
Success metrics: replay consistency and comparison fidelity.
Failure scenarios: missing data, corrupted checkpoint, or clock drift.
Recovery behavior: reload checkpoint or abort with deterministic error.

## Tick-by-Tick Replay
Purpose: validate microstructure-sensitive behavior.
Inputs: tick feed, liquidity snapshots, and latency policy.
Configuration: tick granularity, timing model, and slippage rules.
Initial state: defined starting market and portfolio state.
Execution flow: process each tick in order and simulate decisions.
Expected outputs: tick-level orders and fills.
Validation criteria: order of events matches source feed.
Success metrics: sequence fidelity and event determinism.
Failure scenarios: out-of-order ticks or missing tick segments.
Recovery behavior: fail closed or restart from last valid tick.

## Order Book Simulation
Purpose: simulate order-book impact and matching behavior.
Inputs: book depth, queue position, and order placement rules.
Configuration: book model and fill model.
Initial state: synthetic book state.
Execution flow: place orders and update book state.
Expected outputs: simulated match events and partial fills.
Validation criteria: matching rules remain consistent.
Success metrics: fill realism and price impact fidelity.
Failure scenarios: liquidity collapse or book corruption.
Recovery behavior: rebuild book from checkpoint.

## Liquidity Simulation
Purpose: model route viability under liquidity changes.
Inputs: pool depth, route candidates, and slippage rules.
Configuration: liquidity shock settings and thresholds.
Initial state: baseline pool state.
Execution flow: mutate liquidity and evaluate route outcomes.
Expected outputs: fill probability and route viability.
Validation criteria: simulated impact stays within model bounds.
Success metrics: route prediction accuracy.
Failure scenarios: sudden depth loss or fragmentation.
Recovery behavior: reset to baseline state.

## Gas Simulation
Purpose: test gas-cost sensitivity and replacement behavior.
Inputs: fee curves, network congestion, and transaction policy.
Configuration: gas model and fee bounds.
Initial state: normal fee baseline.
Execution flow: vary fees and replay transactions.
Expected outputs: successful or rejected execution under cost pressure.
Validation criteria: cost model matches configured policy.
Success metrics: fee prediction accuracy.
Failure scenarios: fee spike or underpricing.
Recovery behavior: reprice or cancel.

## Network Congestion
Purpose: model latency and transaction delay under congestion.
Inputs: queue depth, RPC delay, and confirmation timing.
Configuration: congestion multiplier and timeout rules.
Initial state: baseline network health.
Execution flow: delay submissions and confirmations.
Expected outputs: delayed fills and retry activity.
Validation criteria: timeout logic triggers at expected thresholds.
Success metrics: recovery latency and timeout accuracy.
Failure scenarios: prolonged congestion or stalled confirmation.
Recovery behavior: retry, replace, or abort per policy.

## RPC Failures
Purpose: validate behavior under provider outages and timeouts.
Inputs: RPC failure schedule and retry policy.
Configuration: error injection profile.
Initial state: healthy provider baseline.
Execution flow: induce errors during critical operations.
Expected outputs: retries, fallback, or safe abort.
Validation criteria: fail-closed behavior is preserved.
Success metrics: recovery success and safe shutdown accuracy.
Failure scenarios: total provider outage or intermittent failures.
Recovery behavior: switch provider or halt execution.

## Oracle Failures
Purpose: validate behavior when reference data becomes unavailable or corrupted.
Inputs: oracle data and corruption schedule.
Configuration: oracle freshness and trust policy.
Initial state: valid oracle state.
Execution flow: corrupt or delay oracle data and observe policy response.
Expected outputs: rejection or fallback to safe data.
Validation criteria: unsafe execution is blocked.
Success metrics: rejection accuracy and recovery time.
Failure scenarios: stale or conflicting oracle feeds.
Recovery behavior: abort or switch to safe mode.

## Wallet Failures
Purpose: validate signing and balance failure behavior.
Inputs: wallet state, permission policy, and balance schedule.
Configuration: wallet error injection.
Initial state: healthy wallet.
Execution flow: simulate signing failure or balance loss.
Expected outputs: safe rejection or operator escalation.
Validation criteria: no invalid transaction emission.
Success metrics: safe abort accuracy.
Failure scenarios: revoked permissions or insufficient balance.
Recovery behavior: pause trading until wallet state is restored.

## Chain Reorganisations
Purpose: validate reorg resilience and reconciliation.
Inputs: reorg depth and chain receipt state.
Configuration: finality policy and reorg thresholds.
Initial state: pending and confirmed transactions.
Execution flow: introduce reorg and recompute finality.
Expected outputs: reorg-aware reconciliation events.
Validation criteria: accounting remains consistent.
Success metrics: reorg detection and reconciliation accuracy.
Failure scenarios: deep reorg or conflicting receipts.
Recovery behavior: replay from last confirmed safe state.

## AI Decision Simulation
Purpose: validate AI ranking and execution gating without live risk.
Inputs: prompt template, context, and model outputs.
Configuration: provider and confidence thresholds.
Initial state: candidate pool and model policy.
Execution flow: simulate prompt, response, validation, and gating.
Expected outputs: deterministic approval, rejection, or hold.
Validation criteria: AI cannot bypass safety policy.
Success metrics: calibration and validation pass rate.
Failure scenarios: bad schema, low confidence, stale context.
Recovery behavior: fallback model or hold decision.

## Monte Carlo
Purpose: explore probabilistic outcome distributions.
Inputs: stochastic market and execution parameters.
Configuration: seed, iterations, and distribution bounds.
Initial state: baseline portfolio and market state.
Execution flow: run multiple randomized trials.
Expected outputs: outcome distribution and confidence intervals.
Validation criteria: seed reproducibility.
Success metrics: distribution stability and variance estimation quality.
Failure scenarios: insufficient sample size or invalid distribution.
Recovery behavior: rerun with corrected parameters.

## Stress Testing
Purpose: test resilience under adverse but plausible conditions.
Inputs: shocks to price, gas, liquidity, latency, and failure rates.
Configuration: stress profiles and thresholds.
Initial state: healthy baseline.
Execution flow: apply stressors and observe response.
Expected outputs: degraded but safe behavior.
Validation criteria: risk thresholds are respected.
Success metrics: survival rate and bounded loss.
Failure scenarios: cascading failures or uncontrolled drawdown.
Recovery behavior: emergency stop or safe pause.

## Black Swan Scenarios
Purpose: validate extreme failure tolerance.
Inputs: severe volatility, liquidity collapse, and infrastructure outage.
Configuration: extreme scenario profile.
Initial state: baseline exposure.
Execution flow: apply extreme shocks.
Expected outputs: fail-closed behavior and emergency stop.
Validation criteria: catastrophic loss is bounded by policy.
Success metrics: containment and recovery readiness.
Failure scenarios: market freeze, outage, or deep reorg.
Recovery behavior: stop trading and require operator intervention.

## Regression Testing
Purpose: ensure changes do not alter expected behavior.
Inputs: canonical scenario set and golden outputs.
Configuration: baseline comparator and tolerances.
Initial state: known-good snapshots.
Execution flow: replay scenarios and compare output deltas.
Expected outputs: diff report.
Validation criteria: deltas stay within accepted tolerance.
Success metrics: regression pass rate.
Failure scenarios: output drift or missed invariants.
Recovery behavior: fail the build and block promotion.

## Benchmark Testing
Purpose: measure throughput, latency, and resource usage.
Inputs: benchmark scenarios and system profiles.
Configuration: iteration count and performance targets.
Initial state: stable system baseline.
Execution flow: run repeated scenarios and capture metrics.
Expected outputs: performance report.
Validation criteria: targets are met or violations flagged.
Success metrics: p95 latency, throughput, and resource efficiency.
Failure scenarios: performance regression or memory blowup.
Recovery behavior: isolate regression and require remediation.

## Cross-references
- Strategies: `STRATEGIES.md`
- Execution: `EXECUTION-ENGINE.md`
- AI: `AI-PIPELINE.md`
- Monitoring: `MONITORING-OBSERVABILITY.md`
- Backtesting: `BACKTESTING.md`
