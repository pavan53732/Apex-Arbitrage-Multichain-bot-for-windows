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
version: 1.1.0
canonical_source: docs/apex-repository-docs/standards/canonical-source-rules.md
related_concepts:
  - CONCEPT-0052
  - CONCEPT-0053
  - CONCEPT-0054
  - CONCEPT-0065
  - CONCEPT-0066
  - CONCEPT-0067
  - CONCEPT-0068
  - CONCEPT-0069
  - CONCEPT-0070
  - CONCEPT-0071
  - CONCEPT-0072
  - CONCEPT-0073
  - CONCEPT-0074
  - CONCEPT-0075
  - CONCEPT-0076
  - CONCEPT-0077
  - CONCEPT-0078
dependencies:
  - DOC-0052
  - DOC-0053
  - DOC-0054
  - DOC-0065
  - DOC-0066
  - DOC-0067
  - DOC-0068
  - DOC-0069
  - DOC-0070
  - DOC-0071
  - DOC-0072
  - DOC-0073
  - DOC-0074
  - DOC-0075
  - DOC-0076
  - DOC-0077
  - DOC-0078
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Index
owned_domains: []
---

# Standards

**Parent:** [Repository Operating Model](../README.md)

## Purpose and scope

Repository standards that define how to apply governance rules at the document, code, and architecture level. These standards make governance rules actionable through specific practices, naming conventions, metadata requirements, and implementation constraints.

## What belongs here

Policy documents constraining documentation, repository changes, coding practices, README structure, validation, registry operations, document lifecycle, concept lifecycle, AI agent behavior, and validator implementation architecture.

## What does not belong here

Product API or runtime contracts, product configuration schemas, or product feature flags.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| standards | CONCEPT-0052 | [Canonical Source Rules](canonical-source-rules.md) | (self) |

## Document classes expected

- Policy
- Reference
- Index
- Guide

## Relationship to adjacent domains

Governance defines rules; Standards defines how to apply them. Governance answers "what should the repository be"; Standards answers "how do we enforce it in practice". Governance is strategic; Standards is tactical. Both domains work together: Governance sets policy, Standards provides implementation guidance.

## Subdomain navigation

### standards

- Concept: `CONCEPT-0052`
- Canonical Owner: [Canonical Source Rules](canonical-source-rules.md)
- Folder README: (self)

Documents:
- [Canonical Source Rules](canonical-source-rules.md) — Policy
- [Coding Standards](coding-standards.md) — Policy
- [Dependency Authority Rules](dependency-authority-rules.md) — Policy
- [README Governance Standard](readme-governance-standard.md) — Policy
- [Validation Specification](../validation/validation-specification.md) — Specification
- [Validator Architecture Specification](../validation/validator-architecture-specification.md) — Specification
- [Registry Governance Standard](../registries/registry-governance-standard.md) — Policy
- [Document Lifecycle Policy](../documentation-lifecycle/document-lifecycle-policy.md) — Policy
- [Concept Lifecycle Policy](../registries/concept-lifecycle-policy.md) — Policy
- [AI Capability Matrix](../agent-system/ai-capability-matrix.md) — Policy
- [AI Decision Tree](../agent-system/ai-decision-tree.md) — Policy
- [AI Execution Contract](../agent-system/ai-execution-contract.md) — Policy
- [AI Failure Policy](../agent-system/ai-failure-policy.md) — Policy
- [AI Change Classification Matrix](../agent-system/ai-change-classification-matrix.md) — Policy
- [AI Commit Policy](../agent-system/ai-commit-policy.md) — Policy
- [AI Push Policy](../agent-system/ai-push-policy.md) — Policy
- [AI Workspace Policy](../agent-system/ai-workspace-policy.md) — Policy

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
