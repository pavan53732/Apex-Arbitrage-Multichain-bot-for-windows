---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Project Structure documentation.
scope: Reference documentation.
canonical_source: docs/PROJECT-STRUCTURE.md
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
- `ARCHITECTURE.md`
- `MODULE-DEPENDENCY.md`
- `BUILD-RELEASE-CICD.md`
- `VERSIONING.md`

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
