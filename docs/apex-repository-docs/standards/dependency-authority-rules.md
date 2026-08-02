---
metadata_schema_version: 1.0
document_id: DOC-0054
title: Dependency Authority Rules
plane: Repository Operating Model
domain: Standards
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/standards/dependency-authority-rules.md
related_concepts:
  - CONCEPT-0054
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Standards
type: STANDARD
purpose: Dependency Authority Rules documentation.
scope: Reference documentation.
---

# Dependency Authority Rules

## Document type
Document type: [REFERENCE]

## Purpose
Defines allowed dependencies, forbidden dependencies, and the circular dependency policy for documents in the repository knowledge system.

## Scope
Applies to every tracked document that declares `dependencies` or `consumers` in its front matter. Dependency authority is a documentation-graph concern; runtime dependency rules are owned by the runtime architecture owners.

## Allowed dependencies
- A derived or reference document may depend on its canonical owner.
- A consumer document may depend on the canonical source it implements, consumes, or traces to.
- Dependencies must resolve to real document IDs or canonical paths (ROM-006).
- Dependencies should be the narrowest set that expresses the relationship; broad fan-out is discouraged.

## Forbidden dependencies
- A canonical owner must not depend on a document that it supersedes or that is archived.
- No document may depend on a generated execution artifact as a source of truth (ROM-010).
- No document may depend on a lower-authority document to define a concept the higher-authority document owns.
- Repository-operating documents must not depend on product-specification documents for governance meaning, and vice versa (ROM-008).

## Circular dependency policy
- Circular dependency chains between documents are prohibited.
- Authority is unidirectional: the hierarchy runs from the Repository Knowledge Model down through plane, domain, class, authority, document, and concept.
- If a cycle is detected, break it by moving the shared concept to its canonical owner and pointing both documents at that owner.

## Resolution rules
- When two documents express the same dependency, the canonical owner declares the authoritative relationship.
- `consumers` must be symmetric with `dependencies`: if A lists B as a dependency, B should list A as a consumer where the registry tracks consumers.

## Enforcement
- Validators enforce dependency resolution (ROM-006) and traceability validity (ROM-007).

## Common violations
- A guide depending on another guide for authority.
- A generated artifact listed as a dependency.
- A cross-plane dependency for governance meaning.
- A consumer depending on an archived document as a live source.
- A document depending on a superseded owner for the concept it now owns.
- A dependency declared in `dependencies` that no longer resolves after a rename.
- A consumer that omits a dependency it visibly implements.

## Cross-references
- `./canonical-source-rules.md`
- `../../REBUILD-SYSTEM-SPECIFICATION.md`
- `../../REPOSITORY-EXECUTION-MODEL.md`
- `../traceability/cross-reference-index.md`

## Operational Contract

This document owns the dependency-authority rules for the documentation graph. Validators enforce resolution (ROM-006) and traceability validity (ROM-007) against these rules. This document does not own runtime service dependencies; those are owned by `docs/apex-app-docs/runtime/registries/service-registry.md`.

## Example
A guide that explains a specification lists the specification as its dependency, and the specification lists the guide as a consumer.
