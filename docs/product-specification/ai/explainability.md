---
metadata_schema_version: 1.0
document_id: DOC-0126
title: Explainability
plane: Product Specification
domain: AI
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/explainability.md
related_concepts:
  - CONCEPT-0126
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - AI
type: REFERENCE
purpose: Explainability documentation.
scope: Reference documentation.
---

# Explainability

## Document type
This document is an overview, reference, or index as noted below.

# Explainability

## Purpose
Defines the mandatory trace format for every decision, recommendation, and action.

## Required fields
Decision ID, rationale, confidence, alternatives considered, inputs used, gates passed, veto source, and timestamp.

## State machine
```mermaid
stateDiagram-v2
  [*] --> CAPTURED
  CAPTURED --> EXPLAINED
  EXPLAINED --> STORED
  STORED --> REPLAYABLE
```

## Failure modes
Missing rationale, incomplete inputs, untraceable decision, expired replay data.

## Recovery
Reject storage, request re-evaluation, or mark the decision as non-compliant.

## Cross-references
- `./ai-orchestration.md`
- `../execution/decision-engine.md`
- `./learning-pipeline.md`
- `../operations/monitoring/metrics.md`

For governance-grade trace compliance, see `./governance-explainability.md`.
## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Arbitrage explanations
- Must explain why opportunities were taken or skipped.

## Required details
- Define why decisions were taken or skipped.

## Explanation rules
- Explain why actions were taken, skipped, or delayed.
- Capture inputs, outputs, and decision context for auditability.

## Explanation rules
- Explain why actions were taken, skipped, or delayed.
- Capture inputs, outputs, and decision context.
