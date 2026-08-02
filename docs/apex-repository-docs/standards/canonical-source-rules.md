---
metadata_schema_version: 1.0
document_id: DOC-0052
title: Canonical Source Rules
plane: Repository Operating Model
domain: Standards
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-repository-docs/standards/canonical-source-rules.md
related_concepts:
  - CONCEPT-0052
dependencies: []
consumers:
  - DOC-0055
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Standards
type: STANDARD
purpose: Canonical Source Rules documentation.
scope: Reference documentation.
---

# Canonical Source Rules

## Document type
Document type: [REFERENCE]

## Purpose
Defines which document wins when documents conflict, and the discipline required to keep one canonical source of truth per concept.

## Scope
Applies to all documentation conflicts in the repository knowledge system, including conflicts between planes, classes, and authority levels.

## Conflict resolution rules
- **Owner document wins over index or overview.** A canonical owner defines the concept; an index or overview only navigates to it.
- **Schema wins for field definitions.** Where a schema and a prose document define the same field, the schema is authoritative for the field's shape.
- **ADR wins for architecture decisions.** An accepted ADR records a decision and takes precedence over later prose that contradicts it, until superseded by a new ADR.
- **Canonical wins over derived.** A canonical document defines; a derived document summarizes or navigates and must defer.
- **Specification wins over guide.** A guide explains a specification and must not silently override it.
- **Registry wins for identity.** Concept IDs, document IDs, and ownership relationships are authoritative in the registries.

## Authority levels
- Canonical — the single source of truth for its concept.
- Derived — produced from a canonical source; must stay aligned with it.
- Reference — navigational or supporting; never authoritative over a canonical owner.
- Historical — records past state; not a source of truth.
- Generated — non-canonical by default and never authoritative (ROM-010).

## Edit-first discipline
- Do not edit a lower-authority file in a way that silently overrides a canonical file.
- If two files appear to define the same concept, clarify or establish a canonical relationship before proceeding.
- If a file is replaced, make the replacement relationship explicit in `supersedes` and `superseded_by`.

## Enforcement
- Validators enforce authority consistency (ROM-009) and canonical ownership (ROM-001).
- A derived document that overrides a canonical owner fails validation.

## Common conflicts
- Index vs owner: the owner wins.
- Guide vs specification: the specification wins.
- Old ADR vs new ADR: the accepted, non-superseded ADR wins.
- Reference vs canonical: the canonical owner wins.
- Historical vs active: the active document wins; historical records document past state only.

## Cross-references
- `./dependency-authority-rules.md`
- `../../REBUILD-SYSTEM-SPECIFICATION.md`
- `../registries/CONCEPT-REGISTRY.md`
- `../registries/DOCUMENT-REGISTRY.md`

## Operational Contract

This document owns the conflict-resolution rules for canonical sources. It does not own any individual concept; concepts are owned by their canonical owners. Validators enforce authority consistency (ROM-009) and canonical ownership (ROM-001) against these rules.

## Example
A schema and a reference doc disagree on a field's optionality; the schema definition wins for the field, and the reference doc is corrected to match.
