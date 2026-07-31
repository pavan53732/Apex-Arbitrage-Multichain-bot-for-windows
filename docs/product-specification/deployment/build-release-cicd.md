---
metadata_schema_version: 1.0
document_id: DOC-0222
title: Build Release CI/CD
plane: Product Specification
domain: Deployment
class: Reference
authority: Canonical
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/product-specification/deployment/build-release-cicd.md
related_concepts:
  - CONCEPT-0222
dependencies:
  - DOC-0219
  - DOC-0223
  - DOC-0224
  - DOC-0235
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0085
  - DOC-0220
  - DOC-0224
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Build Release Cicd documentation.
scope: Reference documentation.
---

# Build Release Cicd

## Document type
This document is an overview, reference, or index as noted below.

# Build Release CICD

## Purpose
Defines build, test, package, sign, and release stages for the Windows app.

## Ownership
- Owns pipeline stages and build gates.
- Does not own runtime behavior or trading policy.

## Windows release stages
- Build.
- Test.
- Package.
- Sign.
- Publish.
- Verify update path.

## Cross-references
- `./windows-deployment.md`
- `./deployment.md`
- `../testing/testing-guide.md`
- `./code-signing.md`

## Windows gates
- Build must produce signed artifacts, installer packages, and update metadata.
- Release must block if signing, smoke tests, or rollback checks fail.
