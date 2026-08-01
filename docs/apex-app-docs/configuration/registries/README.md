---
metadata_schema_version: 1.0
document_id: DOC-0431
title: Configuration Registries README
plane: Product Specification
domain: Configuration
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/configuration/registries/contract-registry.md
related_concepts:
  - CONCEPT-0383
dependencies:
  - DOC-0383
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Configuration Registries

## Purpose and scope

Contract registry, contract management, and system capability registry documentation.

## What belongs here

Configuration-owned registries and registry management references.

## What does not belong here

Data registry system behavior or market registries unless configuration owns the registry.

## Expected document classes

- Index
- Specification
- Reference
- Policy or Registry where this subdomain owns the concern

## Canonical boundaries

This folder indexes Configuration documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Contract Management](contract-management.md) | Specification |
| [Contract Registry](contract-registry.md) | Registry |
| [System Capability Registry](system-capability-registry.md) | Registry |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
