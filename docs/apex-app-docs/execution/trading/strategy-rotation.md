---
metadata_schema_version: 1.0
document_id: DOC-0296
title: Strategy Rotation
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/execution/trading/strategy-rotation.md
related_concepts:
  - CONCEPT-0296
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Strategy Rotation documentation.
scope: Reference documentation.
---

# Strategy Rotation

## Document type
Document type: [CONTRACT]

## Purpose
Defines how strategies are evaluated, selected, deployed, monitored, and rotated.

## State machine
```mermaid
stateDiagram-v2
  [*] --> IDLE
  IDLE --> EVALUATING
  EVALUATING --> SELECTING
  SELECTING --> DEPLOYING
  DEPLOYING --> MONITORING
  MONITORING --> ROTATING
  MONITORING --> FALLBACK
  ROTATING --> EVALUATING
  FALLBACK --> EVALUATING
```

## Lifecycle model
- Initial state: `IDLE` — no strategy is deployed.
- Terminal state: none — the rotation loop continues.
- Allowed transitions: as shown in the state machine.
- Forbidden transitions: deploying without evaluation; rotating without monitoring.
- Recovery: a strategy that fails SLO returns to `FALLBACK` and is re-evaluated.
- Failure: an SLO breach disables the strategy and alerts operations.

## Scoring
Score = configurable weighted combination of win rate, Sharpe ratio, recent performance, and regime alignment.

## Configuration
- `ENABLED_STRATEGIES`.
- `MIN_PERFORMANCE_SCORE`.
- `ROTATION_COOLDOWN_MINUTES`.

## Rotation rules
- Only enabled strategies participate; a disabled strategy is excluded from selection.
- A strategy below `MIN_PERFORMANCE_SCORE` is not selected.
- Rotation respects `ROTATION_COOLDOWN_MINUTES` to prevent thrashing.
- If a strategy fails SLO, disable it and alert through `../../operations/notifications/notification-center.md`.
- Fallback strategies keep the engine operating while primary strategies re-evaluate.

## Cross-references
- `../../runtime/orchestrator.md`
- `../../ai/orchestration/ai-consensus.md`
- `../../performance/performance-slos.md`
- `../../security/security-contracts.md`

## Operational Contract

This document owns strategy evaluation, selection, deployment, monitoring, and rotation. Individual strategy behavior is owned by the strategy owners; this document manages the set of active strategies.

## Example
A strategy that breaches its SLO is disabled and rotated out; the fallback strategy keeps scanning while it re-evaluates.
