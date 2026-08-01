---
metadata_schema_version: 1.0
document_id: DOC-0250
title: Plugin Marketplace
plane: Product Specification
domain: Plugins
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/plugins/plugin-marketplace.md
related_concepts:
  - CONCEPT-0250
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Plugins
type: REFERENCE
purpose: Plugin Marketplace documentation.
scope: Reference documentation.
---

# Plugin Marketplace

## Document type
This document is an overview, reference, or index as noted below.

# Plugin Marketplace

## Purpose
Registry for official and community plugins.

## Registry
This is a registry only. Development standards are defined by `./plugin-sdk.md`.

## Cross-references
- `./plugin-sdk.md`
- `../execution/trading/strategies.md`

## Governance Rules
Marketplace entries must declare lifecycle state, permissions, version compatibility, and update policy.

## Example
A strategy plugin is listed only after validation, signing, and approval.

## Plugin lifecycle
- Must define installation, sandboxing, versioning, and uninstall behavior.

## Required details
- Define install, remove, sandbox, and ranking behavior.

## Marketplace rules
- Define plugin install, remove, sandbox, ranking, and compatibility behavior.
- Define trust and signature checks before activation.
