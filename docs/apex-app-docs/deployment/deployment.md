---
metadata_schema_version: 1.0
document_id: DOC-0224
title: Deployment
plane: Product Specification
domain: Deployment
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/deployment/deployment.md
related_concepts:
  - CONCEPT-0224
dependencies: []
consumers:
  - DOC-0220
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Deployment
type: REFERENCE
purpose: Deployment documentation.
scope: Reference documentation.
---

# APEX Deployment & Release Guide

## Document type
Document type: [GUIDE]

## Purpose
Defines build pipeline, packaging, testing gates, release promotion, rollback expectations, and operator release workflow.

## Ownership
- Owns packaging, installer flow, release channels, and upgrade/rollback procedures.
- Consumes `../operations/reliability/runtime-operations.md`, `../testing/testing-guide.md`, and `../security/security.md`.

## Release stages
- Build.
- Sign.
- Package.
- Publish.
- Verify.
- Promote.
- Roll back.

## Preconditions
- Tests must pass.
- Configuration schema must validate.
- Migration scripts must be reversible or explicitly documented.
- Release artifacts must include checksums and version metadata.

## Release channels
- Updates flow through the configured channel: `canary`, `beta`, or `production`.
- Promotion between channels requires verification on the lower channel first.
- A release is promoted only when smoke tests and rollback checks pass.

## Rollback
- Every release keeps the previous version available for rollback.
- Rollback restores the prior version and verifies health after restore.
- A failed promotion is rolled back automatically and reported to operators.

## Windows deployments
- Installer packages, permissions, and the upgrade flow follow the Windows deployment contract.
- Deployment failures fail safe: a partial deployment is never presented as current.

## Deployment rules
- Define installer, update, rollback, and rollout behavior for Windows.
- Define safe failure and recovery during deployment.

## Cross-references
- `../windows/windows-desktop.md`
- `./build-release.md`
- `./windows-deployment.md`
- `../operations/reliability/runtime-operations.md`
- `../security/security.md`

## Operational Contract

Defines the packaging, installer flow, release channels, and upgrade/rollback procedures for the APEX Windows app. Stage sequencing and gates are owned by `build-release.md`; this guide covers the operator release workflow end to end.

## Example
A canary release fails post-install health verification; it is rolled back automatically and the prior production version remains current.
