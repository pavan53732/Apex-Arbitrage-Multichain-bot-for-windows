---
metadata_schema_version: 1.0
document_id: DOC-0099
title: Workflow Builder
plane: Product Specification
domain: Runtime
class: Reference
authority: Canonical
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/product-specification/runtime/workflow-builder.md
related_concepts:
  - CONCEPT-0099
dependencies:
  - DOC-0087
  - DOC-0217
  - DOC-0253
  - DOC-0281
consumers:
  - DOC-0049
  - DOC-0094
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Workflow Builder documentation.
scope: Reference documentation.
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
- `../interfaces/event-bus.md`
- `../execution/policy-engine.md`
- `./orchestrator.md`
- `../dashboard/ui-dashboard-spec.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
