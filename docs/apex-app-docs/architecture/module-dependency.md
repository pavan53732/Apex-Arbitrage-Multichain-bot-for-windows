---
metadata_schema_version: 1.0
document_id: DOC-0083
title: Module Dependency
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/architecture/module-dependency.md
related_concepts:
  - CONCEPT-0083
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Architecture
type: REFERENCE
purpose: Module Dependency documentation.
scope: Reference documentation.
---

# Module Dependency

## Document type
Document type: [CONTRACT]

## Purpose
Defines the dependency graph and import rules between modules and packages in the APEX implementation.

## Scope
Import-level dependency policy across packages. Runtime service dependency is owned by the runtime service registry; this document governs code-level module imports.

## Ownership
- Owns import dependency policy only.
- Does not own runtime behavior or service lifecycle.

## Import rules
- Imports must follow the dependency direction defined by `./dependency-graph.md`; reverse imports are prohibited.
- A package may import another package only if the target is a declared dependency of the source.
- No cyclic imports between packages are permitted; cycles must be broken by extracting the shared module.
- Platform-independent core packages must not import Windows-specific packages; the reverse direction is allowed.
- Import depth is kept shallow: a package imports at the layer directly below it, not through transitive shortcuts.
- New imports must be reflected in the dependency graph and validated by the build.

## Boundary rules
- `core` packages contain domain logic with no platform dependencies.
- `windows` packages contain desktop, service, and OS integration and depend on core.
- `adapters` translate external interfaces into domain models and depend only on core contracts.

## Verification
- Import rules are enforced at build time; a violation blocks the build.
- The dependency graph is regenerated and diffed on every build.
- A new import must be declared in the module manifest.

## Package boundaries
- `core` — domain logic, no platform imports.
- `adapters` — external integrations, import core contracts only.
- `windows` — desktop and service integration, imports core and adapters.
- Cross-package cycles fail validation.
- `contracts` — shared schemas and typed definitions; imported by every layer.
- `scripts` and `tests` — tooling and suites; never imported by runtime packages.
- A platform-neutral package must not gain a platform import without an explicit architecture decision.
- A new package is added here and to the component diagrams in the same change.

## Cross-references
- `./project-structure.md`
- `./architecture.md`
- `./dependency-graph.md`

## Operational Contract

This document owns code-level module import policy. Violations are detected at build time and block the build. Runtime dependency behavior is owned elsewhere; this document only governs static imports.

## Example
A Windows service package imports the execution core for order submission but the execution core never imports a Windows package.
