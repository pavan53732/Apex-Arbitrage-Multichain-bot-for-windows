---
metadata_schema_version: 1.0
document_id: DOC-0011
title: Governance README
plane: Repository Operating Model
domain: Governance
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: REBUILD-SYSTEM-SPECIFICATION.md
related_concepts:
  - CONCEPT-0003
  - CONCEPT-0012
dependencies:
  - DOC-0003
  - DOC-0012
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Index
owned_domains: []
---

# Governance

**Parent:** [Repository Operating Model](../README.md)

## Purpose and scope

Repository-level governance and source-of-truth conventions.

## What belongs here

Governance guides, repository policy references, and governance overview documentation.

## What does not belong here

Product feature governance, temporary audit notes, or product-specification governance.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| governance | CONCEPT-0012 | [Governance Overview](governance-overview.md) | (self) |

## Document classes expected

- Index
- Guide
- Reference
- Specification
- Policy
- Historical

## Relationship to adjacent domains

Governance defines repository-operating rules. It is consumed by all Repository Operating Model domains. Product Specification domains must not redefine governance concepts.

## Subdomain navigation

### governance

- Concept: `CONCEPT-0012`
- Canonical Owner: [Governance Overview](governance-overview.md)
- Folder README: (self)

Documents:
- [Governance Overview](governance-overview.md) — Guide

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
