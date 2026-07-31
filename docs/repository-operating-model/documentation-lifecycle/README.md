---
metadata_schema_version: 1.0
document_id: DOC-0060
title: Documentation Lifecycle README
plane: Repository Operating Model
domain: Documentation Lifecycle
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/documentation-lifecycle/documentation-lifecycle.md
related_concepts:
  - CONCEPT-0056
  - CONCEPT-0057
  - CONCEPT-0059
  - CONCEPT-0068
dependencies:
  - DOC-0056
  - DOC-0057
  - DOC-0059
  - DOC-0068
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Documentation Lifecycle

## Purpose and scope

Lifecycle, index, and review workflow for durable documentation in the repository.

## What belongs here

Documentation lifecycle policy, documentation map, status review workflow, document lifecycle policy, and navigation surfaces.

## What does not belong here

Temporary migration/audit/completion reports, generated documentation, or product documentation content.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| documentation-lifecycle | CONCEPT-0056 | [Documentation Lifecycle](./documentation-lifecycle.md) | (self) |

## Document classes expected

- Index
- Workflow
- Guide
- Reference
- Policy

## Relationship to adjacent domains

Documentation Lifecycle governs how all documentation (both Repository Operating Model and Product Specification) is created, maintained, and reviewed. It is consumed by all domains.

## Subdomain navigation

### documentation-lifecycle

- Concept: `CONCEPT-0056`
- Canonical Owner: [Documentation Lifecycle](./documentation-lifecycle.md)
- Folder README: (self)

Documents:
- [Documentation Lifecycle](./documentation-lifecycle.md) — Workflow
- [Documentation Status Review Workflow](./documentation-status-review-workflow.md) — Workflow
- [Documentation Map](./documentation-map.md) — Index
- [Document Lifecycle Policy](./document-lifecycle-policy.md) — Policy

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
