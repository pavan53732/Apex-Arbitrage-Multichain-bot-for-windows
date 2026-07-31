---
metadata_schema_version: 1.0
document_id: DOC-0398
title: Diagnostics README
plane: Product Specification
domain: Operations
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/diagnostics.md
related_concepts:
  - CONCEPT-0333
dependencies:
  - DOC-0333
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Diagnostics

## Purpose and scope

Operational diagnostics, troubleshooting, and diagnostic reference material.

## What belongs here

Diagnostics guides, error-code references, troubleshooting guidance, and support-oriented operational references.

## What does not belong here

Recovery orchestration, monitoring SLOs, or runtime behavior owned by adjacent Operations domains.

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
| [Diagnostics](../diagnostics.md) | Canonical diagnostics behavior. |
| [Error Codes](./error-codes.md) | Error-code reference under diagnostics. |
| [Troubleshooting](./troubleshooting.md) | Troubleshooting reference under diagnostics. |

## Adjacent domains

Adjacent domains may reference this folder, but they must not redefine the canonical behavior owned here.
