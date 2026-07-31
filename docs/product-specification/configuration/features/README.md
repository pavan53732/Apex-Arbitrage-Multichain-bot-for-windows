---
metadata_schema_version: 1.0
document_id: DOC-0430
title: Configuration Features README
plane: Product Specification
domain: Configuration
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/configuration/features/feature-flags.md
related_concepts:
  - CONCEPT-0388
dependencies:
  - DOC-0388
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Configuration Features

## Purpose and scope

Feature flags, feature gates, and feature rollout governance documentation.

## What belongs here

Feature flag and rollout control documents.

## What does not belong here

Core configuration profiles or product registries unless feature rollout owns the concern.

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
| [Feature Flag Governance And Rollout Matrix](./feature-flag-governance-and-rollout-matrix.md) | Specification |
| [Feature Flags](./feature-flags.md) | Reference |
| [Feature Gates](./feature-gates.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
