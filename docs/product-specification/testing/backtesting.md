---
metadata_schema_version: 1.0
document_id: DOC-0236
title: Backtesting
plane: Product Specification
domain: Testing
class: Reference
authority: Reference
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/simulation-engine.md
related_concepts:
  - CONCEPT-0283
dependencies:
  - DOC-0283
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: TEST
purpose: Backtesting documentation.
scope: Reference documentation.
---

# Backtesting

## Document type
This document is an overview, reference, or index as noted below.

# Backtesting

## Purpose
Authoritative simulation and replay specification for validating strategies and AI behavior before live execution.

## Ownership
- Owns historical replay, tick replay, and scenario-based validation for strategies, execution, and AI behavior.
- Does not own live runtime scheduling or chain connectivity.

## Covered modes
Paper trading, historical replay, tick replay, order-book simulation, liquidity simulation, gas fee simulation, network congestion simulation, RPC failure simulation, chain reorganisation simulation, oracle failure simulation, wallet failure simulation, AI decision simulation, Monte Carlo, stress testing, black swan testing.

## Determinism rules
- Scenario seed, historical snapshot, configuration snapshot, and versioned code reference must be recorded.
- Results must be reproducible for the same seed and inputs.
- Any non-deterministic source must be isolated, stubbed, or recorded as part of the scenario definition.

## Replay lifecycle
ScenarioDefined -> SnapshotCaptured -> Replayed -> Evaluated -> Persisted -> Published.

### Transition rules
- ScenarioDefined -> SnapshotCaptured after the historical input set is frozen.
- SnapshotCaptured -> Replayed when the runner begins deterministic execution.
- Replayed -> Evaluated after the strategy, execution, or AI response is completed.
- Evaluated -> Persisted after metrics and outcomes are stored.
- Persisted -> Published after reports and summaries are available to consumers.

## Idempotency and retry
- Re-running the same scenario with the same seed and snapshot must yield the same classification and metrics.
- Retry is allowed only for test harness failures, not to alter scenario outputs.
- A replay must not mutate live runtime state.

## Failure and recovery
- Missing inputs, schema mismatch, or unsupported scenario parameters must fail fast with a stable error code.
- A failed run must not partially overwrite prior scenario results.
- If a replay is interrupted, the runner must resume only from a clean restart with a fresh attempt record.

## Persistence
- Persist scenario id, seed, snapshot hash, configuration hash, code version, metrics, outcome summary, and failure reason.
- Persist report artifacts and benchmark references for regression comparison.

## Monitoring
- Replay throughput.
- Regression drift versus baseline.
- Scenario failure rate.
- Benchmark latency and resource usage.

## Cross-references
- `../execution/simulation-engine.md`
- `../execution/strategies.md`
- `../execution/execution-engine.md`
- `../ai/ai-pipeline.md`
- `./testing-guide.md`
- `../deployment/versioning.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Windows determinism
- Must define line endings, path handling, and timer resolution considerations on Windows.

## Required details
- Define deterministic replay and Windows file/timing differences.

## Backtest rules
- Define deterministic replay, Windows file handling, and timing differences.
- Define comparison against live results.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
