---
metadata_schema_version: 1.0
document_id: DOC-0221
title: App Builder Deployment Guide
plane: Product Specification
domain: Deployment
class: Guide
authority: Canonical
status: Active
owner: UI Team
version: 1.1.0
canonical_source: docs/apex-app-docs/deployment/app-builder-deployment-guide.md
related_concepts:
  - CONCEPT-0221
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Deployment
type: GUIDE
purpose: App Builder Deployment Guide documentation.
scope: Reference documentation.
---

# App Builder Deployment Guide

## Document type
Document type: [GUIDE]

## Purpose
Defines how the Windows app is deployed to users and updated safely.

## Ownership
- Owns installer creation, signing, upgrades, uninstall, and first-run setup.
- Does not own feature development or trading behavior.

## Deployment contract
- Must define silent install, first-run config, upgrade path, and rollback behavior.
- Must define telemetry opt-in and post-install validation.
- Uninstall must remove service registrations, scheduled tasks, and user-scope data per the uninstall policy.
- A deployed version is identifiable from the system surface for support and audit.
- Rollback targets are pinned per release; an operator can always return to the last verified release.

## Install flow
- Installers are created from the build pipeline and signed before distribution.
- Silent install is supported for managed environments; interactive install presents first-run configuration.
- First-run setup validates configuration schema, seeds defaults, and creates the workspace.
- Post-install validation verifies the app launches, the service registers, and update checks succeed.

## Upgrade and rollback
- Upgrades follow the update channel and are integrity-checked before application.
- A failed upgrade rolls back to the last known good version rather than leaving a partial install.
- Uninstall removes the app, its service entries, and user data only after explicit confirmation.

## Telemetry
- Telemetry is opt-in; no data is collected before consent.
- Opt-in state is stored per user and reversible from the settings surface.

## First-run setup
- First-run validates the configuration schema.
- Defaults are seeded from the install profile.
- The workspace and service entries are created.
- Post-install validation verifies launch, service registration, and update checks.

## Update behavior
- Updates are integrity-checked before application.
- A failed update rolls back to the last known good version.

## Cross-references
- `./windows-deployment.md`
- `./deployment.md`
- `../configuration/core/configuration.md`
- `../security/security-contracts.md`
- `../reference/changelog.md`

## Operational Contract

This document owns the operator-facing deployment guide for the Windows app. Build, signing, and release stages are owned by `build-release.md` and `deployment.md`; this guide focuses on install, upgrade, uninstall, and first-run behavior.

## Example
A user upgrades from an older build; the update is verified, applied, and rolled back if the post-update health check fails.
