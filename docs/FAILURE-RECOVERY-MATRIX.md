---
last_updated: 2026-07-29
type: INDEX
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Failure Recovery Matrix documentation.
scope: Reference documentation.
canonical_source: docs/FAILURE-RECOVERY-MATRIX.md if filename.startswith('docs/') else FAILURE-RECOVERY-MATRIX.md
---

# Failure Recovery Matrix

## Document type
Document type: [REFERENCE]

## Purpose
Maps failure types to recovery behaviours.

## Matrix
- Timeout -> bounded retry.
- Invariant breach -> fail closed.

## Cross-References
- `TRACEABILITY-MATRIX.md`

