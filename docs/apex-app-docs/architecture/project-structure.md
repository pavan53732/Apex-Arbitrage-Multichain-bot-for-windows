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
canonical_source: docs/apex-app-docs/architecture/project-structure.md
related_concepts:
  - CONCEPT-0085
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Architecture
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
- `../deployment/build-release.md`
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
