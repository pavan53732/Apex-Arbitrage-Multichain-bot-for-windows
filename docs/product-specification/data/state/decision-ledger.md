---
metadata_schema_version: 1.0
document_id: DOC-0273
title: Decision Ledger
plane: Product Specification
domain: Data
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/data/state/decision-ledger.md
related_concepts:
  - CONCEPT-0273
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: Decision Ledger documentation.
scope: Reference documentation.
---

# Decision Ledger

## Document type
This document is an overview, reference, or index as noted below.

# Decision Ledger

## Purpose
Defines the immutable record of every autonomous decision and outcome.

## State machine
```mermaid
stateDiagram-v2
  [*] --> CAPTURED
  CAPTURED --> VALIDATED
  VALIDATED --> HASHED
  HASHED --> STORED
  STORED --> REPLAYABLE
  REPLAYABLE --> ARCHIVED
```

## Required fields
Unique Decision ID, timestamp, trigger event, market snapshot, AI recommendation, deterministic calculations, policy evaluation, risk score, simulation result, final decision, execution result, post-execution outcome.

## Failure modes
Missing record, tampered record, incomplete lineage, replay mismatch.

## Recovery
Rebuild from source logs, reject incomplete traces, escalate to audit.

## Cross-references
- `../../execution/risk-policy/decision-engine.md`
- `../../ai/explainability/governance-explainability.md`
- `../../ai/explainability/explainability.md`
- `../../execution/decision-log.md`

## Ledger Semantics
Defines the immutable trace of autonomous decisions, simulation outputs, execution results, and outcomes.

## Example
A trade decision records market snapshot, risk score, and post-execution outcome.
