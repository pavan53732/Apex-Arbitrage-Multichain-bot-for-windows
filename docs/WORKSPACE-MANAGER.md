---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.1
purpose: Workspace Manager documentation.
scope: Reference documentation.
canonical_source: docs/WORKSPACE-MANAGER.md
---

# Workspace Manager

## Document type
[REFERENCE]. This document is a short reference pointer. It is not a
[CONTRACT] and must not be treated as one — the front-matter `type` was
previously set to `CONTRACT` while the body explicitly stated "This
document is an overview, reference, or index", which is a direct
Prime-Directive violation (short docs must declare their type
consistently). The authoritative Workspace Manager service CONTRACT —
state machine, schema, API, events, configuration ownership, and
cross-subsystem wiring — is owned exclusively by
**`docs/DASHBOARD-WORKSPACES.md`**. This file exists only as a stable,
short-form entry point referenced elsewhere in the documentation set
(see `docs/DOCUMENTATION-MAP.md`, `docs/README.md`).

## Purpose
Defines workspace ownership, layout, settings, providers, dashboards, strategies, and wallets for each workspace.

## State machine
```mermaid
stateDiagram-v2
  [*] --> LOADING
  LOADING --> RESTORING
  RESTORING --> ACTIVE
  ACTIVE --> SAVING
  SAVING --> SAVED
  SAVED --> ACTIVE
```

## Cross-references
- `DASHBOARD-WORKSPACES.md`
- `WINDOWS-DESKTOP.md`
- `CONFIGURATION-PROFILES.md`

## Operational Contract
Defines workspace composition, layout, settings, dashboard bindings, provider selection, and recovery state.

## Example
A simulation workspace restores its selected chain, wallet, and layout on reopen.
