---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: Ai Planner documentation.
scope: Reference documentation.
canonical_source: docs/AI-PLANNER.md
---

# Ai Planner

## Document type
This document is an overview, reference, or index as noted below.

# AI Planner

## Purpose
Defines the planner agent contract for goal decomposition, dependency ordering, execution sequencing, and failure recovery.

## State machine
```mermaid
stateDiagram-v2
  [*] --> RECEIVED
  RECEIVED --> DECOMPOSING
  DECOMPOSING --> ORDERING
  ORDERING --> SEQUENCING
  SEQUENCING --> READY
  READY --> MONITORING
```

## Cross-references
- `AI-ORCHESTRATION.md`
- `DECISION-ENGINE.md`
- `AI-CONSENSUS.md`

## Operational Contract
Defines goal decomposition, dependency ordering, sequencing, recovery, and plan emission.

## Example
The planner breaks a multi-step execution request into risk, simulation, and trade tasks.

## Planning rules
- Define plan generation, plan revision, and plan validation.
- Define how plans are rejected when constraints are violated.
