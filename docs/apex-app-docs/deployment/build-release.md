---
metadata_schema_version: 1.0
document_id: DOC-0222
title: Build Release
plane: Product Specification
domain: Deployment
class: Workflow
authority: Canonical
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/deployment/build-release.md
related_concepts:
  - CONCEPT-0222
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Deployment
type: REFERENCE
purpose: Build Release Cicd documentation.
scope: Reference documentation.
---

# Build Release

## Document type
Document type: [CONTRACT]

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

## Stage rules
- **Build** compiles all packages and fails on dependency-graph or module-import violations.
- **Test** runs unit, integration, and backtesting suites; failures block the pipeline.
- **Package** produces installer packages and update metadata from the signed build output.
- **Sign** signs executables, plugin archives, and release artifacts per `code-signing.md`.
- **Publish** distributes to the release channel and update server.
- **Verify update path** exercises the upgrade from the previous release on a staging machine.

## Windows gates
- Build must produce signed artifacts, installer packages, and update metadata.
- Release must block if signing, smoke tests, or rollback checks fail.
- Generated artifacts are staged outside source control; the repository never contains build output.

## Artifact policy
- Build output is staged outside source control; the repository never contains build output.
- Artifacts carry checksums and version metadata.
- Artifacts are reproducible from a clean checkout.
- Release artifacts are retained per the retention policy and never overwritten in place.
- A failed stage leaves the previous release current and marks the pipeline failed.
- Release notes and version metadata are produced by the same build that produced the artifacts.

## Cross-references
- `./windows-deployment.md`
- `./deployment.md`
- `../testing/testing-guide.md`
- `./code-signing.md`

## Operational Contract

This document owns the build, test, package, sign, and release stages for the Windows app and the gates between them. Packaging content and signing policy are owned by `windows-deployment.md` and `code-signing.md`; this document sequences and gates them.

## Example
A release is blocked when the signing gate fails, leaving the prior release current until the failure is resolved.
