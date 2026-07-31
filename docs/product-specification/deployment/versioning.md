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
version: 1.0.0
canonical_source: docs/product-specification/deployment/versioning.md
related_concepts:
  - CONCEPT-0225
dependencies:
  - DOC-0083
  - DOC-0251
  - DOC-0266
  - DOC-0371
  - DOC-0381
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0079
  - DOC-0085
  - DOC-0220
  - DOC-0236
  - DOC-0251
  - DOC-0257
  - DOC-0388
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Versioning documentation.
scope: Reference documentation.
---

# Versioning

## Document type
This document is an overview, reference, or index as noted below.

# Versioning

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

## Cross-references
- `../data/database-schema.md`
- `../interfaces/api-contracts.md`
- `../configuration/configuration.md`
- `../reference/implementation-roadmap.md`
- `../architecture/module-dependency.md`

## Governance Rules
Defines version policy for documents, schemas, APIs, plugins, contracts, and compatibility expectations.

## Example
A breaking schema change requires a version bump and migration plan.
