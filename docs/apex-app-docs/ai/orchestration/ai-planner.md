---
metadata_schema_version: 1.0
document_id: DOC-0121
title: AI Planner
plane: Product Specification
domain: AI
class: Reference
authority: Reference
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/orchestration/ai-orchestration.md
related_concepts:
  - CONCEPT-0102
dependencies:
  - DOC-0102
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Ai Planner documentation.
scope: Reference documentation.
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
- `./ai-orchestration.md`
- `../../execution/risk-policy/decision-engine.md`
- `./ai-consensus.md`

## Operational Contract
Defines goal decomposition, dependency ordering, sequencing, recovery, and plan emission.

## Example
The planner breaks a multi-step execution request into risk, simulation, and trade tasks.

## Planning rules
- Define plan generation, plan revision, and plan validation.
- Define how plans are rejected when constraints are violated.
