---
metadata_schema_version: 1.0
document_id: DOC-0061
title: Contribution README
plane: Repository Operating Model
domain: Contribution
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/contribution/contributing.md
related_concepts:
  - CONCEPT-0062
dependencies:
  - DOC-0062
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Contribution

## Purpose and scope

Contributor-facing repository guidance for humans and AI agents.

## What belongs here

Contribution guides, collaboration expectations, and contribution workflow documentation.

## What does not belong here

Product user guides, product onboarding, or product feature documentation.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| contribution | CONCEPT-0062 | [Contributing](./contributing.md) | (self) |

## Document classes expected

- Index
- Guide
- Reference
- Specification

## Relationship to adjacent domains

Contribution is governed by Repository Operating Model standards. It applies to all contributors working on both Repository Operating Model and Product Specification domains.

## Subdomain navigation

### contribution

- Concept: `CONCEPT-0062`
- Canonical Owner: [Contributing](./contributing.md)
- Folder README: (self)

Documents:
- [Contributing](./contributing.md) — Guide

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
