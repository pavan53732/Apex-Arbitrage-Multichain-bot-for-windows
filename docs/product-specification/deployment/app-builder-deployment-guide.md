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
version: 1.0.0
canonical_source: docs/product-specification/deployment/app-builder-deployment-guide.md
related_concepts:
  - CONCEPT-0221
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Deployment
type: GUIDE
purpose: App Builder Deployment Guide documentation.
scope: Reference documentation.
---

# App Builder Deployment Guide

## Document type
This document is an overview, reference, or index as noted below.

# App Builder Deployment Guide

## Purpose
Defines how the Windows app is deployed to users and updated safely.

## Ownership
- Owns installer creation, signing, upgrades, uninstall, and first-run setup.
- Does not own feature development or trading behavior.

## Deployment contract
- Must define silent install, first-run config, upgrade path, and rollback behavior.
- Must define telemetry opt-in and post-install validation.

## Cross-references
- `./windows-deployment.md`
- `../configuration/core/configuration.md`
- `../security/security-contracts.md`
- `../reference/changelog.md`
