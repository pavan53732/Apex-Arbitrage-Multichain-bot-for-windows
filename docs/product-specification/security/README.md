---
metadata_schema_version: 1.0
document_id: DOC-0229
title: Security README
plane: Product Specification
domain: Security
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/security/README.md
related_concepts:
  - CONCEPT-0229
dependencies:
  - DOC-0226
  - DOC-0227
  - DOC-0228
  - DOC-0230
  - DOC-0231
consumers:
  - DOC-0049
  - DOC-0058
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
---

# Security

## Purpose and scope

Security contracts, permissions, secrets, trust boundaries, and signing/security behavior.

## Document classes expected

- Index
- Guide
- Reference
- Specification where this folder owns a canonical boundary
- Registry only in registry folders
- Historical only in historical folders
- Generated only in generated folders

## Canonical boundaries

Security specifications and references.

## What does not belong here

Non-security operational failures.

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0226 | [Permission Model](./permission-model.md) | Specification | Canonical | Active |
| DOC-0227 | [Security Contracts](./security-contracts.md) | Specification | Canonical | Active |
| DOC-0228 | [Security](./security.md) | Specification | Canonical | Active |
| DOC-0230 | [Secret Lifecycle](./secret-lifecycle.md) | Reference | Canonical | Active |
| DOC-0231 | [Trust Boundaries](./trust-boundaries.md) | Reference | Canonical | Active |
