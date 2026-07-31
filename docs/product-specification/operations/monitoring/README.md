---
metadata_schema_version: 1.0
document_id: DOC-0399
title: Monitoring README
plane: Product Specification
domain: Operations
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/monitoring/monitoring-observability.md
related_concepts:
  - CONCEPT-0336
dependencies:
  - DOC-0336
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Monitoring

## Purpose and scope

Monitoring, observability, health checks, metrics, and arbitrage monitoring documentation.

## What belongs here

Monitoring and observability specifications, metrics references, health checks, and operational monitoring documents.

## What does not belong here

Recovery playbooks, diagnostics troubleshooting, or performance SLO ownership unless explicitly monitoring-related.

## Expected document classes

- Index
- Specification
- Reference
- Guide for operational procedures

## Canonical boundaries

This folder indexes operations documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Arbitrage Monitoring](./arbitrage-monitoring.md) | Reference |
| [Health Checks](./health-checks.md) | Specification |
| [Metrics](metrics.md) | Reference |
| [Monitoring Observability](./monitoring-observability.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
