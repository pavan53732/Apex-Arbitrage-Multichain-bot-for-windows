---
metadata_schema_version: 1.0
document_id: DOC-0346
title: Operations
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/reliability/operations.md
related_concepts:
  - CONCEPT-0346
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: REFERENCE
purpose: Operations documentation.
scope: Reference documentation.
---

# Operations

## Document type
Document type: [POLICY]

## Purpose
Defines the operator-facing operations model: monitoring, restart, incident response, and maintenance.

## Scope
This document is the operations overview for the APEX platform. Detailed runtime operations are owned by `runtime-operations.md`; monitoring by the monitoring contracts; recovery by the recovery contracts.

## Final rules
- Monitoring runs continuously; a gap in monitoring is treated as a risk.
- Restarts follow the shutdown lifecycle and rehydrate persisted state.
- Incident response follows the recovery playbook; every incident is recorded.
- Maintenance windows are declared and surfaced to operators.
- Service and desktop operator responsibilities are explicit and documented.

## Operator responsibilities
- Desktop operators manage the trading surface, approvals, and wallet actions.
- Service operators manage the Windows service, updates, and maintenance.
- Both follow the runtime operations and recovery contracts.

## Operating cadence
- Monitoring is reviewed on a defined cadence; a gap in monitoring is treated as a risk.
- Maintenance windows are declared and surfaced to operators before execution.
- Incidents are recorded with their timeline, actions, and outcome.

## Restart policy
- Restarts follow the shutdown lifecycle and rehydrate persisted state.
- A restart is scheduled outside active trading windows where possible.
- A failed restart is an incident and follows the recovery playbook.

## Change and maintenance
- Changes are validated before application and rolled back on failure.
- Maintenance activities are logged against the affected components.
- Operator handover notes are retained for continuity.

## Escalation
- Escalation follows the recovery playbook with the error code and actions attempted.
- An incident that exceeds its recovery budget escalates to the defined owners.
- Every escalation and resolution is recorded for trend analysis.

## Availability expectations
- The operations model assumes the performance and recovery budgets are met.
- Operator actions are auditable; every action records its actor and timestamp.
- Degraded modes are explicit and never silently meet normal-operation expectations.

## Cross-references
- `./runtime-operations.md`
- `../monitoring/health-checks.md`
- `../recovery/recovery-playbook.md`

## Operational Contract

This document is the operations overview. Runtime behavior, monitoring, and recovery are owned by their canonical contracts; this document defines the operator model that uses them.

## Example
A service operator performs a scheduled maintenance restart following the shutdown lifecycle, and the incident is recorded if health does not recover.
