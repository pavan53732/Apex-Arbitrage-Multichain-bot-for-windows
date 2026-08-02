---
metadata_schema_version: 1.0
document_id: DOC-0225
title: Versioning
plane: Product Specification
domain: Deployment
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/deployment/versioning.md
related_concepts:
  - CONCEPT-0225
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Deployment
type: REFERENCE
purpose: Versioning documentation.
scope: Reference documentation.
---

# Versioning

## Document type
Document type: [POLICY]

## Support Doc
This document provides guidance. Canonical version numbers for code, schema, and API are maintained by their respective owners (Schema/Config/API).

## Purpose
Defines versioning rules for configuration, database, API, strategy, plugin, and migration artifacts.

## Scope
This document covers semantic versioning, compatibility, deprecation, and migration behavior.

## Versioned surfaces
- Database schemas.
- Configuration files.
- API contracts.
- Strategy definitions.
- Plugin interfaces.
- Migrations.

## Versioning rules
- Versions follow semantic versioning: major, minor, and patch components are meaningful.
- A breaking change requires a major version bump and a documented migration plan.
- A backward-compatible addition is a minor bump; a bug fix is a patch bump.
- Deprecation is announced one minor version before removal.
- Compatible surfaces may not consume a major version older than their declared floor.

## Compatibility
- Schema, API, and configuration compatibility is enforced by their canonical owners.
- A consumer must declare the minimum version it supports.
- Version mismatches are surfaced by the dependency graph and validators.

## Enforcement
- Version policy is enforced by the validators and the release gate.
- A version mismatch blocks promotion between channels.
- Deprecation windows are tracked in the roadmap.
- A migration must be reversible or paired with a documented forward-only decision.
- Plugin interface versions are checked against the host API version before activation.
- A version bump updates the versioned surface's canonical owner in the same change.

## Cross-references
- `../data/persistence/database-schema.md`
- `../interfaces/api/api-contracts.md`
- `../configuration/core/configuration.md`
- `../reference/implementation-roadmap.md`
- `../architecture/module-dependency.md`

## Governance Rules
Defines version policy for documents, schemas, APIs, plugins, contracts, and compatibility expectations.

## Example
A breaking schema change requires a version bump and migration plan; the migration is reversible and documented.
