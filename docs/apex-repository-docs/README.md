---
metadata_schema_version: 1.0
document_id: DOC-0010
title: Repository Operating Model README
plane: Repository Operating Model
domain: Governance
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: REBUILD-SYSTEM-SPECIFICATION.md
related_concepts:
  - CONCEPT-0003
  - CONCEPT-0001
  - CONCEPT-0004
  - CONCEPT-0006
  - CONCEPT-0007
  - CONCEPT-0008
  - CONCEPT-0056
  - CONCEPT-0062
dependencies:
  - DOC-0003
  - DOC-0001
  - DOC-0004
  - DOC-0006
  - DOC-0007
  - DOC-0008
  - DOC-0056
  - DOC-0062
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains:
  - Agent System
  - Contribution
  - Documentation Lifecycle
  - Governance
  - Registries
  - Standards
  - Traceability
  - Validation
  - Workflows
---

# Repository Operating Model

## Purpose and scope

How humans and AI agents govern and maintain repository knowledge. This is the top-level domain for all repository-operating concerns.

## What belongs here

Repository governance, agent operating rules, standards, documentation lifecycle, validation policy, traceability, registries, contribution guides, and workflows.

## What does not belong here

Product runtime, market, trading, UI, deployment, AI runtime behavior, or any product-specification concerns.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| agent-system | CONCEPT-0001 | [AGENTS.md](../../AGENTS.md) | [Agent System README](agent-system/README.md) |
| contribution | CONCEPT-0062 | [Contributing](contribution/contributing.md) | [Contribution README](contribution/README.md) |
| documentation-lifecycle | CONCEPT-0056 | [Documentation Lifecycle](documentation-lifecycle/documentation-lifecycle.md) | [Documentation Lifecycle README](documentation-lifecycle/README.md) |
| governance | CONCEPT-0012 | [Governance Overview](governance/governance-overview.md) | [Governance README](governance/README.md) |
| registries | CONCEPT-0007 | [Document Registry](registries/DOCUMENT-REGISTRY.md) | [Registries README](registries/README.md) |
| standards | CONCEPT-0052 | [Canonical Source Rules](standards/canonical-source-rules.md) | [Standards README](standards/README.md) |
| traceability | CONCEPT-0008 | [Traceability Registry](registries/TRACEABILITY-REGISTRY.md) | [Traceability README](traceability/README.md) |
| validation | CONCEPT-0004 | [REPOSITORY-EXECUTION-MODEL.md](../../REPOSITORY-EXECUTION-MODEL.md) | [Validation README](validation/README.md) |
| workflows | CONCEPT-0004 | [REPOSITORY-EXECUTION-MODEL.md](../../REPOSITORY-EXECUTION-MODEL.md) | [Workflows README](workflows/README.md) |

## Document classes expected

- Index
- Guide
- Reference
- Specification
- Policy
- Workflow
- Registry
- Historical
- Generated

## Relationship to adjacent domains

Repository Operating Model is the governance plane. It consumes no product domains. Product Specification domains must not redefine repository governance concepts.

## Subdomain navigation

### agent-system

- Concept: `CONCEPT-0001`
- Canonical Owner: [AGENTS.md](../../AGENTS.md)
- Folder README: [Agent System README](agent-system/README.md)

Documents:
- [Agent Index](agent-system/agent-index.md) — Index
- [Agent Guide](agent-system/agent-guide.md) — Guide
- [Skills](agent-system/skills.md) — Reference
- [Agent Navigation](agent-system/agent-navigation.md) — Reference
- [Agent Profiles README](agent-system/agent-profiles/README.md) — Index

### contribution

- Concept: `CONCEPT-0062`
- Canonical Owner: [Contributing](contribution/contributing.md)
- Folder README: [Contribution README](contribution/README.md)

Documents:
- [Contributing](contribution/contributing.md) — Guide

### documentation-lifecycle

- Concept: `CONCEPT-0056`
- Canonical Owner: [Documentation Lifecycle](documentation-lifecycle/documentation-lifecycle.md)
- Folder README: [Documentation Lifecycle README](documentation-lifecycle/README.md)

Documents:
- [Documentation Lifecycle](documentation-lifecycle/documentation-lifecycle.md) — Workflow
- [Documentation Status Review Workflow](documentation-lifecycle/documentation-status-review-workflow.md) — Workflow
- [Documentation Map](documentation-lifecycle/documentation-map.md) — Index

### governance

- Concept: `CONCEPT-0012`
- Canonical Owner: [Governance Overview](governance/governance-overview.md)
- Folder README: [Governance README](governance/README.md)

Documents:
- [Governance Overview](governance/governance-overview.md) — Guide

### registries

- Concept: `CONCEPT-0007`
- Canonical Owner: [Document Registry](registries/DOCUMENT-REGISTRY.md)
- Folder README: [Registries README](registries/README.md)

Documents:
- [Concept Registry](registries/CONCEPT-REGISTRY.md) — Registry
- [Document Registry](registries/DOCUMENT-REGISTRY.md) — Registry
- [Traceability Registry](registries/TRACEABILITY-REGISTRY.md) — Registry

### standards

- Concept: `CONCEPT-0052`
- Canonical Owner: [Canonical Source Rules](standards/canonical-source-rules.md)
- Folder README: [Standards README](standards/README.md)

Documents:
- [Canonical Source Rules](standards/canonical-source-rules.md) — Policy
- [Coding Standards](standards/coding-standards.md) — Policy
- [Dependency Authority Rules](standards/dependency-authority-rules.md) — Policy
- [README Governance Standard](standards/readme-governance-standard.md) — Policy

### traceability

- Concept: `CONCEPT-0008`
- Canonical Owner: [Traceability Registry](registries/TRACEABILITY-REGISTRY.md)
- Folder README: [Traceability README](traceability/README.md)

Documents:
- [Cross Reference Index](traceability/cross-reference-index.md) — Index
- [Module Ownership Matrix](traceability/module-ownership-matrix.md) — Index

### validation

- Concept: `CONCEPT-0004`
- Canonical Owner: [REPOSITORY-EXECUTION-MODEL.md](../../REPOSITORY-EXECUTION-MODEL.md)
- Folder README: [Validation README](validation/README.md)

Documents:
- (No additional documents in this folder)

### workflows

- Concept: `CONCEPT-0004`
- Canonical Owner: [REPOSITORY-EXECUTION-MODEL.md](../../REPOSITORY-EXECUTION-MODEL.md)
- Folder README: [Workflows README](workflows/README.md)

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
