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
version: 1.0.0
canonical_source: docs/product-specification/execution/strategy-rotation.md
related_concepts:
  - CONCEPT-0296
dependencies:
  - DOC-0087
  - DOC-0116
  - DOC-0227
  - DOC-0345
  - DOC-0356
consumers:
  - DOC-0049
  - DOC-0285
  - DOC-0319
  - DOC-0320
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Strategy Rotation documentation.
scope: Reference documentation.
---

# Strategy Rotation

## Document type
This document is an overview, reference, or index as noted below.

# Strategy Rotation

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

## Scoring
Score = configurable weighted combination of win rate, Sharpe ratio, recent performance, and regime alignment.

## Configuration
- ENABLED_STRATEGIES.
- MIN_PERFORMANCE_SCORE.
- ROTATION_COOLDOWN_MINUTES.

## Failure modes
If a strategy fails SLO, disable it and alert through `../operations/notification-center.md`.

## Cross-references
- `../runtime/orchestrator.md`
- `../ai/ai-consensus.md`
- `../performance/performance-slos.md`
- `../security/security-contracts.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
