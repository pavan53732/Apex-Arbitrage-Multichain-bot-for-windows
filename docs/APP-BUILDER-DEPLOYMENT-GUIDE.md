---
last_updated: 2026-07-29
type: GUIDE
owner: UI Team
status: Canonical
version: 1.0.0
purpose: App Builder Deployment Guide documentation.
scope: Reference documentation.
canonical_source: docs/APP-BUILDER-DEPLOYMENT-GUIDE.md
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
- `WINDOWS-DEPLOYMENT.md`
- `CONFIGURATION.md`
- `SECURITY-CONTRACTS.md`
- `CHANGELOG.md`
