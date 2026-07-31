---
metadata_schema_version: 1.0
document_id: DOC-0220
title: Deployment README
plane: Product Specification
domain: Deployment
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/deployment/README.md
related_concepts:
  - CONCEPT-0220
dependencies:
  - DOC-0219
  - DOC-0221
  - DOC-0222
  - DOC-0223
  - DOC-0224
  - DOC-0225
consumers:
  - DOC-0049
  - DOC-0058
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
---

# Deployment

## Purpose and scope

Windows app deployment, packaging, signing, versioning, install/update behavior.

## Document classes expected

- Index
- Guide
- Reference
- Specification where this folder owns a canonical boundary
- Registry only in registry folders
- Historical only in historical folders
- Generated only in generated folders

## Canonical boundaries

Deployment guides and signing/versioning references.

## What does not belong here

Repository CI/CD workflow files.

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0219 | [Windows Deployment](./windows-deployment.md) | Specification | Canonical | Active |
| DOC-0221 | [App Builder Deployment Guide](./app-builder-deployment-guide.md) | Guide | Canonical | Active |
| DOC-0222 | [Build Release CI/CD](./build-release-cicd.md) | Reference | Canonical | Active |
| DOC-0223 | [Code Signing](./code-signing.md) | Reference | Canonical | Active |
| DOC-0224 | [Deployment](./deployment.md) | Reference | Canonical | Active |
| DOC-0225 | [Versioning](./versioning.md) | Reference | Canonical | Active |
