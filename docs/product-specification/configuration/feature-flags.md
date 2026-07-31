---
metadata_schema_version: 1.0
document_id: DOC-0388
title: Feature Flags
plane: Product Specification
domain: Configuration
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/configuration/feature-flags.md
related_concepts:
  - CONCEPT-0388
dependencies: []
consumers:
  - DOC-0389
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Configuration
type: REFERENCE
purpose: Feature Flags documentation.
scope: Reference documentation.
---

# Feature Flags

## Document type
This document is an overview, reference, or index as noted below.

# Feature Flags

## Purpose
Defines controlled rollout states for all product capabilities.

## States
Experimental, Beta, Production, Deprecated, Disabled.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DISABLED
  DISABLED --> EXPERIMENTAL
  EXPERIMENTAL --> BETA
  BETA --> PRODUCTION
  PRODUCTION --> DEPRECATED
  DEPRECATED --> DISABLED
```

## Failure modes
Unsafe rollout, invalid default, conflicting environment override.

## Recovery
Rollback, disable, or pin to previous version.

## Cross-references
- `./configuration.md`
- `../execution/risk-policy/policy-engine.md`
- `../deployment/versioning.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Rollout rules
- Must define environment overrides and strategy rollout controls.

## Required details
- Define rollout, scope, and override behavior.
