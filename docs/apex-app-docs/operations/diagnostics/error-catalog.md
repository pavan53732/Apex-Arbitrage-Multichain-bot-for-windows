---
metadata_schema_version: 1.0
document_id: DOC-0339
title: Error Catalog
plane: Product Specification
domain: Operations
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/diagnostics/error-catalog.md
related_concepts:
  - CONCEPT-0339
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: INDEX
purpose: Error Catalog documentation.
scope: Reference documentation.
---

# Error Catalog

## Document type
Document type: [REFERENCE]

## Purpose
Catalogues canonical error families and codes.

## Codes
- AI-1001: Provider request failed.
- RPC-3002: RPC timeout.
- PLUGIN-9001: Sandbox violation.

## Error families
- **AI**: provider, model, prompt, and cost errors.
- **RPC**: timeout, rate limit, and connection errors.
- **PLUGIN**: sandbox, signature, and compatibility errors.
- **EXEC**: gas, slippage, and execution errors.
- **SEC**: permission, secret, and trust errors.
- **CONFIG**: schema, precedence, and reload errors.

## Catalog rules
- Error codes are stable, unique, and never reused.
- Each entry maps to a recovery path in the failure matrix.
- A new error family is added here and in the failure recovery matrix together.
- Errors are surfaced to operators with their code and recovery guidance.
- A retired code is marked retired and never reassigned.
- Codes are namespaced by family prefix (AI, RPC, PLUGIN, EXEC, SEC, CONFIG).
- An error entry records its severity, source component, and expected recovery.
- Unknown errors surface as the family's general code with the raw detail attached.
- The catalog is the single source for error identities; surfaces reference it, never invent codes.
- Diagnostics surfaces render entries from this catalog, not ad hoc strings.
- Recovery mappings are validated: every catalog entry resolves to a matrix row.
- A new family requires approval of its prefix and recovery model here.
- Code ranges are documented per family to prevent collisions.
- Catalog changes are released with the component that introduced the code.
- Operator-facing error text is written in operator language with a code.

## Cross-references
- `./error-codes.md`
- `../recovery/failure-matrix.md`
- `../recovery/failure-recovery-matrix.md`

## Operational Contract

This document owns the canonical error catalog. Error handling behavior is owned by the error-handling contract; this document lists the codes.

## Example
An RPC timeout surfaces as RPC-3002 and maps to the retry-then-failover recovery path.
