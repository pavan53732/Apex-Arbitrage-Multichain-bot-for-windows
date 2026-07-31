---
metadata_schema_version: 1.0
document_id: DOC-0385
title: Configuration README
plane: Product Specification
domain: Configuration
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/configuration/core/configuration.md
related_concepts:
  - CONCEPT-0381
dependencies:
  - DOC-0381
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Configuration

## Purpose and scope

Configuration core behavior, feature rollout controls, and configuration-owned registries.

## What belongs here

Product configuration specifications, feature flags/gates, profile/reference behavior, and configuration registries.

## What does not belong here

Repository operating settings, data registry implementation, market registries, or runtime operations unless configuration owns the concern.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| core | CONCEPT-0381 | [Configuration](./core/configuration.md) | [Configuration Core README](./core/README.md) |
| features | CONCEPT-0388 | [Feature Flags](./features/feature-flags.md) | [Configuration Features README](./features/README.md) |
| registries | CONCEPT-0383 | [Contract Registry](./registries/contract-registry.md) | [Configuration Registries README](./registries/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Registry
- Policy where rollout/configuration rules are owned

## Relationship to adjacent domains

Configuration is consumed by AI, Runtime, Operations, Security, and Deployment but does not own those domains’ runtime behavior.

## Subdomain navigation

### core

- Concept: `CONCEPT-0381`
- Canonical owner: [Configuration](./core/configuration.md)
- Folder README: [Configuration Core README](./core/README.md)

Documents:

- [Configuration Profiles](./core/configuration-profiles.md) — Reference
- [Configuration Reference](./core/configuration-reference.md) — Reference
- [Configuration](./core/configuration.md) — Specification

### features

- Concept: `CONCEPT-0388`
- Canonical owner: [Feature Flags](./features/feature-flags.md)
- Folder README: [Configuration Features README](./features/README.md)

Documents:

- [Feature Flag Governance And Rollout Matrix](./features/feature-flag-governance-and-rollout-matrix.md) — Specification
- [Feature Flags](./features/feature-flags.md) — Reference
- [Feature Gates](./features/feature-gates.md) — Reference

### registries

- Concept: `CONCEPT-0383`
- Canonical owner: [Contract Registry](./registries/contract-registry.md)
- Folder README: [Configuration Registries README](./registries/README.md)

Documents:

- [Contract Management](./registries/contract-management.md) — Specification
- [Contract Registry](./registries/contract-registry.md) — Registry
- [System Capability Registry](./registries/system-capability-registry.md) — Registry

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
