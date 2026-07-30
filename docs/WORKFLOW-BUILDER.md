---
last_updated: 2026-07-29
type: REFERENCE
owner: UI Team
status: Canonical
version: 1.0.0
purpose: Workflow Builder documentation.
scope: Reference documentation.
canonical_source: docs/WORKFLOW-BUILDER.md
---

# Workflow Builder

## Document type
This document is an overview, reference, or index as noted below.

# Workflow Builder

## Purpose
Defines user-authored automation workflows that connect events, gates, actions, and notifications.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DRAFT
  DRAFT --> VALIDATING
  VALIDATING --> ACTIVE
  ACTIVE --> PAUSED
  PAUSED --> ACTIVE
  ACTIVE --> RETIRED
```

## Contract
Workflows are event-driven and policy-checked before activation.

## Failure modes
Invalid graph, policy violation, missing action handler, loop detection.

## Recovery
Pause workflow, require correction, or route to fallback manual operation.

## Cross-references
- `EVENT-BUS.md`
- `POLICY-ENGINE.md`
- `ORCHESTRATOR.md`
- `dashboard/UI-DASHBOARD-SPEC.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
