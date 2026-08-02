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
Document type: [REGISTRY]

## Purpose
Registry for official and community plugins.

## Registry
This is a registry only. Development standards are defined by `./plugin-sdk.md`.

## Registry entry requirements
- Every marketplace entry declares lifecycle state, permissions, version compatibility, and update policy.
- Entries are versioned; a plugin version bump requires re-verification of signature and compatibility.
- A plugin is listed only after validation, signing, and approval; unsigned plugins are developer-mode only.

## Marketplace rules
- Plugin install, removal, sandbox, and ranking follow the plugin lifecycle and sandbox contracts.
- Trust and signature checks run before activation; a failed check blocks installation.
- Compatibility is verified against the host API version before listing.
- Community plugins are distinguished from official plugins by their ownership and update policy.

## Ranking
- Ranking considers validation status, version freshness, and usage signals.
- A withdrawn or unmaintained plugin is demoted and flagged, not silently removed.

## Listing process
- Submit, validate, sign, approve, list, update, withdraw.
- Each step is recorded in the marketplace entry.
- A plugin can be updated only through a new version that is re-verified.

## Compatibility
- Host API version compatibility is checked before listing.
- A breaking host change flags incompatible plugins for re-validation.

## Trust
- Signature and trust checks run before activation.
- Unsigned plugins are developer-mode only and never listed publicly.
- Trust anchors are maintained and rotated under the plugin security contracts.
- A compromised plugin is withdrawn, flagged, and quarantined across installs.
- Marketplace entries are immutable for audit; corrections create a new revision.
- A withdrawn plugin's consumers are notified and blocked from activation.
- Marketplace moderation and listing policy follow the plugin lifecycle contract.
- Listing metadata is versioned with the plugin package.

## Cross-references
- `./plugin-sdk.md`
- `./plugin-lifecycle.md`
- `./plugin-sandbox-contract.md`
- `../execution/trading/strategies.md`

## Governance Rules
Marketplace entries must declare lifecycle state, permissions, version compatibility, and update policy.

## Example
A strategy plugin is listed only after validation, signing, and approval; its compatibility is checked against the host API before listing.
