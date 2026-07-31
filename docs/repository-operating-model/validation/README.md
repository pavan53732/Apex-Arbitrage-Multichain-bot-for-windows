---
metadata_schema_version: 1.0
document_id: DOC-0047
title: Validation README
plane: Repository Operating Model
domain: Validation
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: REPOSITORY-EXECUTION-MODEL.md
related_concepts:
  - CONCEPT-0004
  - CONCEPT-0066
  - CONCEPT-0078
dependencies:
  - DOC-0004
  - DOC-0066
  - DOC-0078
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Validation

## Purpose and scope

Local-first validation expectations and quality gates for repository knowledge.

## What belongs here

Validation policy, local quality-gate descriptions, validation specification, validator architecture specification, and validator implementations.

## What does not belong here

Remote pipelines, CI/CD files, generated validation output, or product testing specifications.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| validation | CONCEPT-0004 | [REPOSITORY-EXECUTION-MODEL.md](../../REPOSITORY-EXECUTION-MODEL.md) | (self) |

## Document classes expected

- Index
- Policy
- Reference
- Specification

## Relationship to adjacent domains

Validation defines quality gates for all repository knowledge. It is governed by REPOSITORY-EXECUTION-MODEL. All domains must pass validation before committing.

## Subdomain navigation

### validation

- Concept: `CONCEPT-0004`
- Canonical Owner: [REPOSITORY-EXECUTION-MODEL.md](../../REPOSITORY-EXECUTION-MODEL.md)
- Folder README: (self)

Documents:
- [Validation Specification](./validation-specification.md) — Specification
- [Validator Architecture Specification](./validator-architecture-specification.md) — Specification

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
