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
canonical_source: docs/product-specification/execution/trading/strategy-rotation.md
related_concepts:
  - CONCEPT-0296
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
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
If a strategy fails SLO, disable it and alert through `../../operations/notifications/notification-center.md`.

## Cross-references
- `../../runtime/orchestrator.md`
- `../../ai/orchestration/ai-consensus.md`
- `../../performance/performance-slos.md`
- `../../security/security-contracts.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
