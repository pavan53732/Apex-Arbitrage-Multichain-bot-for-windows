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
canonical_source: docs/repository-operating-model/standards/README.md
related_concepts:
  - CONCEPT-0055
dependencies:
  - DOC-0052
  - DOC-0053
  - DOC-0054
consumers:
  - DOC-0049
  - DOC-0058
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
---

# Standards

## Purpose and scope

Repository standards for canonical sources, dependencies, and contributions.

## Document classes expected

- Index
- Guide
- Reference
- Specification where this folder owns a canonical boundary
- Registry only in registry folders
- Historical only in historical folders
- Generated only in generated folders

## Canonical boundaries

Policies constraining documentation and repository changes.

## What does not belong here

Product API or runtime contracts.

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0052 | [Canonical Source Rules](./canonical-source-rules.md) | Policy | Canonical | Active |
| DOC-0053 | [Coding Standards](./coding-standards.md) | Policy | Canonical | Active |
| DOC-0054 | [Dependency Authority Rules](./dependency-authority-rules.md) | Policy | Canonical | Active |
