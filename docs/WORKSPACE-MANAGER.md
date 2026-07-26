# Workspace Manager

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
