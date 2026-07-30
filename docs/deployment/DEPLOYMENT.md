---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Deployment documentation.
scope: Reference documentation.
canonical_source: docs/deployment/DEPLOYMENT.md
---

# Deployment

## Document type
This document is an overview, reference, or index as noted below.

# APEX Deployment & Release Guide

## Purpose
Defines build pipeline, packaging, testing gates, release promotion, rollback expectations, and operator release workflow.

## Ownership
- Owns packaging, installer flow, release channels, and upgrade/rollback procedures.
- Consumes `operations/RUNTIME-OPERATIONS.md`, `guides/TESTING-GUIDE.md`, and `security/SECURITY.md`.

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

## Cross-references
- `windows/WINDOWS-DESKTOP.md`
- `deployment/BUILD-RELEASE-CICD.md`
- `operations/RUNTIME-OPERATIONS.md`
- `security/SECURITY.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Windows deployments
- Must define installer, auto-update, and rollback patterns.

## Required details
- Define installer and update channels.

## Deployment rules
- Define installer, update, rollback, and rollout behavior for Windows.
- Define safe failure and recovery during deployment.

## Deployment rules
- Define Windows deployment packages, permissions, and upgrade flow.
- Define rollback and verification steps.
