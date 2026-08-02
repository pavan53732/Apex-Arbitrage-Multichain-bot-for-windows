---
metadata_schema_version: 1.0
document_id: DOC-0340
title: Failure Matrix
plane: Product Specification
domain: Operations
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/recovery/failure-matrix.md
related_concepts:
  - CONCEPT-0340
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
purpose: Failure Matrix documentation.
scope: Reference documentation.
---

# Failure Matrix

## Document type
Document type: [REFERENCE]

## Purpose
Maps failures to actions.

## Examples
- RPC timeout -> retry -> provider switch -> cooldown -> operator intervention.

## Matrix
- AI provider failure -> failover to secondary provider -> cooldown -> alert.
- Plugin sandbox violation -> terminate plugin -> quarantine -> notify operator.
- Execution gas failure -> retry with repriced gas -> abort if over budget.
- Cache inconsistency -> fail closed -> rebuild from source.
- Wallet signing failure -> lock wallet -> require operator recovery.
- Configuration reload failure -> keep last valid config -> alert.
- Update integrity failure -> discard update -> rollback to last good.
- Worker crash -> restart with backoff -> escalate after repeated failures.

## Matrix rules
- Every failure maps to at least one action; an unmapped failure is escalated.
- Actions are ordered: retry, then failover, then cooldown, then operator intervention.
- A failure that recurs beyond its retry budget escalates, never retries forever.

## Action definitions
- **Retry** — bounded, with backoff, preserving idempotency.
- **Failover** — switch to a verified secondary provider or endpoint.
- **Cooldown** — suspend the affected path for a configured duration.
- **Operator intervention** — surface the failure with context and block further autonomous action.
- **Fail closed** — deny the operation until the condition is resolved.
- **Rollback** — return to the last known good state.
- **Quarantine** — isolate the component and exclude it from dispatch.
- Every action records its trigger, outcome, and duration.
- Actions are validated: an action outside policy is rejected before execution.
- The matrix is versioned; a new failure type updates the matrix and the catalog together.
- Matrix rows map one-to-one to error catalog entries.
- Unmapped failures are escalated and become candidate matrix rows.

## Cross-references
- `./failure-recovery-matrix.md`
- `./recovery-playbook.md`
- `./error-catalog.md`

## Operational Contract

This document owns the failure-to-action mapping. Recovery behavior details are owned by the recovery contracts; this matrix is the reference table.

## Example
An RPC timeout follows retry, then provider switch, then cooldown, then operator intervention.
