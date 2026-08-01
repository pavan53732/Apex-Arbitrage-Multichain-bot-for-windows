---
metadata_schema_version: 1.0
document_id: DOC-0429
title: Configuration Core README
plane: Product Specification
domain: Configuration
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/configuration/core/configuration.md
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

# Configuration Core

## Purpose and scope

Configuration profiles, reference keys, and core configuration behavior.

## What belongs here

Core configuration specifications, key references, and profile behavior.

## What does not belong here

Feature rollout and product registry behavior unless configuration core owns the concern.

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
| [Configuration Profiles](configuration-profiles.md) | Reference |
| [Configuration Reference](configuration-reference.md) | Reference |
| [Configuration](configuration.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
