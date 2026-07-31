---
metadata_schema_version: 1.0
document_id: DOC-0342
title: Operations README
plane: Product Specification
domain: Operations
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/reliability/runtime-operations.md
related_concepts:
  - CONCEPT-0338
dependencies:
  - DOC-0338
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Operations

## Purpose and scope

Runtime operations, monitoring, diagnostics, recovery, reliability, notifications, and operational support documentation.

## What belongs here

Product operations specifications and references. Repository execution policy belongs under Repository Operating Model.

## What does not belong here

Product implementation APIs, market behavior, trading execution, or UI behavior unless operational ownership is explicit.

## Subdomains

| Subdomain | README | Canonical owner |
| --- | --- | --- |
| diagnostics | [Diagnostics README](diagnostics/README.md) | [Diagnostics](./diagnostics/diagnostics.md) |
| monitoring | [Monitoring README](monitoring/README.md) | [Monitoring Observability](./monitoring/monitoring-observability.md) |
| notifications | [Operations Notifications README](notifications/README.md) | [Notification Center](./notifications/notification-center.md) |
| recovery | [Operations Recovery README](recovery/README.md) | [Recovery Coordination](./recovery/recovery-coordination.md) |
| reliability | [Operations Reliability README](reliability/README.md) | [Runtime Operations](./reliability/runtime-operations.md) |

## Document creation rule

Before adding an operations document, identify the active operations concept owner and place the document in the matching subdomain. Do not create duplicate operations ownership documents.
