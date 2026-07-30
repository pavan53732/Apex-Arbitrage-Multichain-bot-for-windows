---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Feature Flags documentation.
scope: Reference documentation.
canonical_source: docs/configuration/FEATURE-FLAGS.md
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
- `configuration/CONFIGURATION.md`
- `POLICY-ENGINE.md`
- `deployment/VERSIONING.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Rollout rules
- Must define environment overrides and strategy rollout controls.

## Required details
- Define rollout, scope, and override behavior.
