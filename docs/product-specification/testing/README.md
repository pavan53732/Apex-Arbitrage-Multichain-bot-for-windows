---
metadata_schema_version: 1.0
document_id: DOC-0234
title: Testing README
plane: Product Specification
domain: Testing
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/testing/README.md
related_concepts:
  - CONCEPT-0234
dependencies:
  - DOC-0232
  - DOC-0233
  - DOC-0235
  - DOC-0236
consumers:
  - DOC-0049
  - DOC-0058
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
---

# Testing

## Purpose and scope

Product testing strategy, test registries, backtesting, and local validation behavior.

## Document classes expected

- Index
- Guide
- Reference
- Specification where this folder owns a canonical boundary
- Registry only in registry folders
- Historical only in historical folders
- Generated only in generated folders

## Canonical boundaries

Testing specifications, guides, and registries.

## What does not belong here

CI/CD workflows or temporary test reports.

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0232 | [Testing](./testing.md) | Specification | Canonical | Active |
| DOC-0233 | [Test Case Registry](./test-case-registry.md) | Registry | Canonical | Active |
| DOC-0235 | [Testing Guide](./testing-guide.md) | Guide | Canonical | Active |
| DOC-0236 | [Backtesting](./backtesting.md) | Reference | Canonical | Active |
