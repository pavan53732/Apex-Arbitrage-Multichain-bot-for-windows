---
metadata_schema_version: 1.0
document_id: DOC-0386
title: Configuration Profiles
plane: Product Specification
domain: Configuration
class: Reference
authority: Reference
status: Active
owner: Config Team
version: 1.0.0
canonical_source: docs/product-specification/configuration/configuration.md
related_concepts:
  - CONCEPT-0381
dependencies:
  - DOC-0381
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Configuration Profiles documentation.
scope: Reference documentation.
---

# Configuration Profiles

## Document type
This document is an overview, reference, or index as noted below.

# Configuration Profiles

## Purpose
Defines profile inheritance, overrides, defaults, and switching for platform modes.

## Profiles
Safe, Balanced, Aggressive, Research, Simulation, Developer.

## State machine
```mermaid
stateDiagram-v2
  [*] --> LOADED
  LOADED --> ACTIVE
  ACTIVE --> SWITCHING
  SWITCHING --> ACTIVE
  ACTIVE --> ARCHIVED
```

## Failure modes
Conflicting override, missing parent, invalid profile selection.

## Recovery
Fallback to safe defaults and validate merged config.

## Cross-references
- `./configuration.md`
- `../ai/ai-settings.md`
- `../dashboard/dashboard-workspaces.md`
- `../../historical/traceability-matrix.md`

## Governance Rules
Defines named configuration bundles, defaults, overrides, environment targeting, and validation.

## Example
A production profile enables stricter risk limits than a sandbox profile.

## Arbitrage profiles
- Must define profile presets for low-latency, cross-exchange, and simulation use cases.

## Required details
- Define named profiles and their settings.

## Profile rules
- Define named profiles, their defaults, and arbitrage-specific presets.
- Define profile storage and switching behavior.
