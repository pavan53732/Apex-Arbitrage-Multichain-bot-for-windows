---
metadata_schema_version: 1.0
document_id: DOC-0064
title: Workflows README
plane: Repository Operating Model
domain: Workflows
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: REPOSITORY-EXECUTION-MODEL.md
related_concepts:
  - CONCEPT-0004
dependencies:
  - DOC-0004
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Workflows

## Purpose and scope

Durable repository workflows executed locally by contributors or agents.

## What belongs here

Human/agent workflow descriptions, review workflows, and release workflows that do not create remote automation.

## What does not belong here

CI/CD, scheduled automation, bots, logs, or generated workflow output.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| workflows | CONCEPT-0004 | [REPOSITORY-EXECUTION-MODEL.md](../.>/../REPOSITORY-EXECUTION-MODEL.md) | (self) |

## Document classes expected

- Index
- Workflow
- Guide
- Reference

## Relationship to adjacent domains

Workflows defines how work happens in the repository. It is governed by REPOSITORY-EXECUTION-MODEL. All contributors and agents follow these workflows.

## Subdomain navigation

### workflows

- Concept: `CONCEPT-0004`
- Canonical Owner: [REPOSITORY-EXECUTION-MODEL.md](../.>/../REPOSITORY-EXECUTION-MODEL.md)
- Folder README: (self)

Documents:
- (No additional documents in this folder)

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
