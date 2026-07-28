---
last_updated: 2026-07-29
type: REFERENCE
owner: UI Team
status: Canonical
version: 1.0.0
purpose: Build Release Cicd documentation.
scope: Reference documentation.
canonical_source: docs/BUILD-RELEASE-CICD.md
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
- `WINDOWS-DEPLOYMENT.md`
- `DEPLOYMENT.md`
- `TESTING-GUIDE.md`
- `CODE-SIGNING.md`

## Windows gates
- Build must produce signed artifacts, installer packages, and update metadata.
- Release must block if signing, smoke tests, or rollback checks fail.
