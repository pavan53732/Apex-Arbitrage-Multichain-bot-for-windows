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

Product operations specifications and references for observing, diagnosing, recovering, and operating the application.

## What does not belong here

Repository execution policy, product execution engines, market logic, or UI behavior unless operational ownership is explicit.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| diagnostics | CONCEPT-0333 | [Diagnostics](./diagnostics/diagnostics.md) | [Diagnostics README](./diagnostics/README.md) |
| monitoring | CONCEPT-0336 | [Monitoring Observability](./monitoring/monitoring-observability.md) | [Monitoring README](./monitoring/README.md) |
| notifications | CONCEPT-0345 | [Notification Center](./notifications/notification-center.md) | [Operations Notifications README](./notifications/README.md) |
| recovery | CONCEPT-0337 | [Recovery Coordination](./recovery/recovery-coordination.md) | [Operations Recovery README](./recovery/README.md) |
| reliability | CONCEPT-0338 | [Runtime Operations](./reliability/runtime-operations.md) | [Operations Reliability README](./reliability/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Guide for operational procedures

## Relationship to adjacent domains

Operations provides observability and recovery surfaces for all product domains but must not redefine their primary behavior.

## Subdomain navigation

### diagnostics

- Concept: `CONCEPT-0333`
- Canonical owner: [Diagnostics](./diagnostics/diagnostics.md)
- Folder README: [Diagnostics README](./diagnostics/README.md)

Documents:

- [Diagnostics](./diagnostics/diagnostics.md) — Specification
- [Error Catalog](./diagnostics/error-catalog.md) — Index
- [Error Codes](./diagnostics/error-codes.md) — Reference
- [Error Handling and Logging](./diagnostics/error-handling-and-logging.md) — Specification
- [Troubleshooting](./diagnostics/troubleshooting.md) — Reference

### monitoring

- Concept: `CONCEPT-0336`
- Canonical owner: [Monitoring Observability](./monitoring/monitoring-observability.md)
- Folder README: [Monitoring README](./monitoring/README.md)

Documents:

- [Arbitrage Monitoring](./monitoring/arbitrage-monitoring.md) — Reference
- [Health Checks](./monitoring/health-checks.md) — Specification
- [Metrics](./monitoring/metrics.md) — Reference
- [Monitoring Observability](./monitoring/monitoring-observability.md) — Specification

### notifications

- Concept: `CONCEPT-0345`
- Canonical owner: [Notification Center](./notifications/notification-center.md)
- Folder README: [Operations Notifications README](./notifications/README.md)

Documents:

- [Notification Center](./notifications/notification-center.md) — Reference

### recovery

- Concept: `CONCEPT-0337`
- Canonical owner: [Recovery Coordination](./recovery/recovery-coordination.md)
- Folder README: [Operations Recovery README](./recovery/README.md)

Documents:

- [Failure Matrix](./recovery/failure-matrix.md) — Index
- [Failure Recovery Matrix](./recovery/failure-recovery-matrix.md) — Index
- [Recovery And Failover](./recovery/recovery-and-failover.md) — Reference
- [Recovery Coordination](./recovery/recovery-coordination.md) — Specification
- [Recovery Playbook](./recovery/recovery-playbook.md) — Reference
- [Self Healing](./recovery/self-healing.md) — Reference

### reliability

- Concept: `CONCEPT-0338`
- Canonical owner: [Runtime Operations](./reliability/runtime-operations.md)
- Folder README: [Operations Reliability README](./reliability/README.md)

Documents:

- [Enterprise Operations](./reliability/enterprise-operations.md) — Reference
- [Operations](./reliability/operations.md) — Reference
- [Provider Resilience](./reliability/provider-resilience.md) — Specification
- [Queue Management](./reliability/queue-management.md) — Reference
- [Runtime Operations](./reliability/runtime-operations.md) — Specification

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
