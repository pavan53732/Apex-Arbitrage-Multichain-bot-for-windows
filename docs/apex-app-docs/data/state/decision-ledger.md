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
canonical_source: docs/apex-app-docs/data/state/decision-ledger.md
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
Document type: [CONTRACT]

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
- Unique Decision ID.
- Timestamp.
- Trigger event.
- Market snapshot.
- AI recommendation.
- Deterministic calculations.
- Policy evaluation.
- Risk score.
- Simulation result.
- Final decision.
- Execution result.
- Post-execution outcome.

## Ledger Semantics
Defines the immutable trace of autonomous decisions, simulation outputs, execution results, and outcomes.

## Integrity rules
- Records are hash-chained; a tampered record is detected on read and flagged.
- A record missing required fields or with incomplete lineage is rejected, not partially stored.
- Replays must reproduce the recorded decision deterministically; a replay mismatch escalates to audit.
- Archived records remain readable but are excluded from live replay.

## Failure modes
Missing record, tampered record, incomplete lineage, replay mismatch.

## Recovery
Rebuild from source logs, reject incomplete traces, escalate to audit.

## Cross-references
- `../../execution/risk-policy/decision-engine.md`
- `../../ai/explainability/governance-explainability.md`
- `../../ai/explainability/explainability.md`
- `../../execution/decision-log.md`

## Operational Contract

This document owns the immutable decision ledger. The decision engine produces decisions; the ledger records them with lineage. Nothing may mutate a stored record.

## Example
A trade decision records market snapshot, risk score, and post-execution outcome, hash-chained to the prior record.
