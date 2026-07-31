---
metadata_schema_version: 1.0
document_id: DOC-0055
title: Standards README
plane: Repository Operating Model
domain: Standards
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/standards/canonical-source-rules.md
related_concepts:
  - CONCEPT-0052
  - CONCEPT-0053
  - CONCEPT-0054
  - CONCEPT-0065
dependencies:
  - DOC-0052
  - DOC-0053
  - DOC-0054
  - DOC-0065
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Standards

## Purpose and scope

Repository standards for canonical sources, dependencies, coding, contributions, and README governance.

## What belongs here

Policy documents constraining documentation, repository changes, coding practices, and README structure.

## What does not belong here

Product API or runtime contracts, product configuration schemas, or product feature flags.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| standards | CONCEPT-0052 | [Canonical Source Rules](./canonical-source-rules.md) | (self) |

## Document classes expected

- Policy
- Reference
- Index
- Guide

## Relationship to adjacent domains

Standards are consumed by all Repository Operating Model domains and Product Specification domains. Product domains must not redefine repository standards.

## Subdomain navigation

### standards

- Concept: `CONCEPT-0052`
- Canonical Owner: [Canonical Source Rules](./canonical-source-rules.md)
- Folder README: (self)

Documents:
- [Canonical Source Rules](./canonical-source-rules.md) — Policy
- [Coding Standards](./coding-standards.md) — Policy
- [Dependency Authority Rules](./dependency-authority-rules.md) — Policy
- [README Governance Standard](./readme-governance-standard.md) — Policy

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
