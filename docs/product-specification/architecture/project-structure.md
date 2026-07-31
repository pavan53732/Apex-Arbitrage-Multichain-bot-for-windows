---
metadata_schema_version: 1.0
document_id: DOC-0085
title: Project Structure
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/architecture/project-structure.md
related_concepts:
  - CONCEPT-0085
dependencies:
  - DOC-0079
  - DOC-0083
  - DOC-0222
  - DOC-0225
consumers:
  - DOC-0049
  - DOC-0053
  - DOC-0068
  - DOC-0069
  - DOC-0080
  - DOC-0083
  - DOC-0251
  - DOC-0257
  - DOC-0371
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Project Structure documentation.
scope: Reference documentation.
---

# Project Structure

## Document type
This document is an overview, reference, or index as noted below.

# Project Structure

## Purpose
Defines the canonical repository layout and ownership boundaries for implementation.

## Planned layout
The implementation will use a multi-package structure for apps, packages, scripts, assets, tests, and contracts.

## Cross-references
- `./architecture.md`
- `./module-dependency.md`
- `../deployment/build-release-cicd.md`
- `../deployment/versioning.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Repository layout
- Must define the actual directories for app, service, docs, and installers.

## Required details
- Define repo directories and installer layout.

## Repository layout
- Define the actual directories for docs, app, service, installers, and tests.
- Define where Windows packaging artifacts live.

## Structure rules
- Define top-level folders for docs, services, workers, tests, and tools.
- Define boundaries between core and Windows-specific code.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
