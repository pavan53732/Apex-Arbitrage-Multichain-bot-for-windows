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
canonical_source: docs/product-specification/operations/monitoring-observability.md
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

Monitoring, observability, operational metrics, and runtime visibility references.

## What belongs here

Monitoring and observability specifications, metrics references, and operational visibility documents.

## What does not belong here

Recovery playbooks, diagnostics troubleshooting, or performance SLO ownership unless explicitly referenced.

## Expected document classes

- Index
- Reference
- Specification when this folder owns a product behavior boundary
- Guide when the document explains operational usage

## Canonical boundaries

This folder indexes documents in its subdomain and defers behavioral authority to the canonical owner documents listed below.

## Documents

| Document | Purpose |
| --- | --- |
| [Monitoring Observability](../monitoring-observability.md) | Canonical monitoring and observability behavior. |
| [Metrics](./metrics.md) | Metrics reference under monitoring. |

## Adjacent domains

Adjacent domains may reference this folder, but they must not redefine the canonical behavior owned here.
