---
metadata_schema_version: 1.0
document_id: DOC-0127
title: Governance Explainability
plane: Product Specification
domain: AI
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/governance-explainability.md
related_concepts:
  - CONCEPT-0127
dependencies:
  - DOC-0126
  - DOC-0279
  - DOC-0281
  - DOC-0288
consumers:
  - DOC-0049
  - DOC-0114
  - DOC-0126
  - DOC-0273
  - DOC-0288
  - DOC-0297
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Governance Explainability documentation.
scope: Reference documentation.
---

# Governance Explainability

## Document type
This document is an overview, reference, or index as noted below.

# Governance Explainability

## Purpose
Defines the compliance-heavy owner for audit lineage, rationale retention, replayability, and decision trace governance.

## Scope
All decisions, approvals, overrides, policy changes, provider changes, strategy changes, and recovery actions.

## Required fields
Decision ID, actor, timestamp, rationale, confidence, alternatives considered, gates passed, veto source, replay hash, and retention class.

## State machine
```mermaid
stateDiagram-v2
  [*] --> CAPTURED
  CAPTURED --> VALIDATED
  VALIDATED --> STAMPED
  STAMPED --> STORED
  STORED --> REPLAYABLE
  REPLAYABLE --> ARCHIVED
```

## Failure modes
Missing lineage, expired trace, tampered record, incomplete rationale.

## Recovery
Reject non-compliant traces, rebuild from source logs, and escalate to audit.

## Cross-references
- `./explainability.md`
- `../execution/decision-engine.md`
- `../execution/policy-engine.md`
- `../execution/decision-log.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
