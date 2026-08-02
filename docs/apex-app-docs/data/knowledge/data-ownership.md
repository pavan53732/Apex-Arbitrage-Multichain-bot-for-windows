---
metadata_schema_version: 1.0
document_id: DOC-0268
title: Data Ownership
plane: Product Specification
domain: Data
class: Policy
authority: Canonical
status: Active
owner: Security Team
version: 1.1.0
canonical_source: docs/apex-app-docs/data/knowledge/data-ownership.md
related_concepts:
  - CONCEPT-0268
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Data
type: STANDARD
purpose: Data Ownership documentation.
scope: Reference documentation.
---

# Data Ownership

## Document type
Document type: [REFERENCE]

## Purpose
Defines ownership of settings, workspace, plugin data, cache, AI memory, trades, and wallets.

## Scope
This document assigns data-domain ownership across the APEX platform. It is the ownership map; behavior for each domain is owned by its canonical owner.

## Ownership map
- **Settings** — owned by the configuration system; persisted per user and per workspace.
- **Workspace** — owned by the workspace manager; layout, providers, and bindings.
- **Plugin data** — owned by the plugin sandbox; isolated per plugin and revoked on uninstall.
- **Cache** — owned by the cache manager; acceleration only, never the source of truth.
- **AI memory** — owned by the AI memory system; scoped and governed by the AI governance rules.
- **Trades** — owned by the trading and execution systems; recorded in the execution lifecycle.
- **Wallets** — owned by the wallet management system; keys held in the OS keychain.

## Ownership rules
- Each domain has exactly one canonical owner; the owner defines the schema and lifecycle.
- Cross-domain reads follow the data flow; a consumer never mutates another domain's store.
- Retention and deletion follow the data governance rules for each domain.
- Ownership changes update this map and the affected owner in the same change.

## Stewardship
- Each domain owner is the steward of its data; the steward defines retention and access.
- Cross-domain consumers request access through the owning domain.
- Stewardship is recorded in the ownership map and the registries.

## Change management
- An ownership change updates the map, the affected owner, and the registries together.
- No domain store is mutated by a non-owner; mutations flow through the owning system.
- A new data domain is assigned exactly one owner at creation; an unowned domain is a documentation gap.
- Disputed ownership is resolved by the map and the registries before any store change proceeds.
- Deletion and retention follow the data governance rules of the owning domain.
- A domain store's schema is defined by its owner; consumers adapt to it, never bypass it.

## Cross-references
- `./data-governance.md`
- `./data-flow.md`
- `../state/state-management.md`
- `../persistence/database-schema.md`
- `../../ai/memory/ai-memory-system.md`

## Operational Contract

This document owns the data-ownership map. It does not own any data domain's behavior; each domain's canonical owner does. Conflicts in ownership are resolved by this map and the registries.

## Example
Plugin data is scoped to its plugin sandbox and fully removed on uninstall, per the plugin sandbox contract.
