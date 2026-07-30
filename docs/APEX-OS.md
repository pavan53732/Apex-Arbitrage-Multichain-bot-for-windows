---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Apex Os documentation.
scope: Reference documentation.
canonical_source: docs/APEX-OS.md
---

# Apex Os

## Document type
This document is an overview, reference, or index as noted below.

# APEX OS

## Purpose
Defines the constitution of the platform: vision, mission, philosophy, design principles, architecture principles, runtime principles, AI principles, security principles, extensibility principles, roadmap, non-goals, and evolution strategy.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DEFINED
  DEFINED --> GOVERNING
  GOVERNING --> EVOLVING
  EVOLVING --> GOVERNING
```

## Cross-references
- `APEX-KERNEL.md`
- `ORCHESTRATOR.md`
- `POLICY-ENGINE.md`
- `PLUGIN-SDK.md`
- `windows/WINDOWS-DESKTOP.md`
- `operations/ENTERPRISE-OPERATIONS.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
