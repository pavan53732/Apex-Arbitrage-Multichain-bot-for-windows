---
metadata_schema_version: 1.0
document_id: DOC-0341
title: Failure Recovery Matrix
plane: Product Specification
domain: Operations
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/recovery/failure-recovery-matrix.md
related_concepts:
  - CONCEPT-0341
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
purpose: Failure Recovery Matrix documentation.
scope: Reference documentation.
---

# Failure Recovery Matrix

## Document type
Document type: [REFERENCE]

## Purpose
Maps failure types to recovery behaviours.

## Matrix
- Timeout -> bounded retry.
- Invariant breach -> fail closed.
- Stale data -> refresh from source before use.
- Partial fill -> reconcile after execution.
- Provider outage -> failover to secondary, then cooldown.
- Reorg -> revalidate and reconcile confirmed state.
- Update failure -> rollback to last known good.
- Plugin violation -> quarantine and notify.

## Recovery rules
- Recovery is bounded: a behaviour that cannot recover within its budget escalates.
- Fail-closed behaviours deny the action; they never degrade to a best-effort mode.
- Every recovery is logged and observable in the recovery metrics.
- Recovery outcomes are verified before a component is declared stable.
- A recovered component re-enters dispatch only after verification passes.
- Recovery preferences are configuration, validated before use.

## Behaviour definitions
- **Bounded retry** — retry with backoff up to a configured budget, then escalate.
- **Fail closed** — deny the operation; never degrade to best-effort.
- **Refresh before use** — refetch stale data from its source before consumption.
- **Reconcile after execution** — settle partial fills against the plan and surface drift.
- **Failover** — switch to a verified secondary provider, then apply cooldown.
- **Revalidate on reorg** — move confirmed state back to pending and reconcile.
- **Rollback** — restore the last known good state and verify integrity.
- **Quarantine** — isolate the violating plugin and notify the operator.
- Every recovery behaviour is recorded with its trigger and outcome.
- Recovery runs within the performance budget or escalates.
- The matrix is the recovery counterpart of the failure matrix and the error catalog.

## Cross-References
- `./failure-matrix.md`
- `./recovery-playbook.md`
- `../../../historical/traceability-matrix.md`

## Operational Contract
This document owns the failure-to-recovery mapping. Detection and health are owned by the monitoring contracts; this matrix defines what each failure type does to recover.

## Example
A provider outage triggers failover to the secondary provider, applies a cooldown, and escalates to the operator if the secondary also fails.
