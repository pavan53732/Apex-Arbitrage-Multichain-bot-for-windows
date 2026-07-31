---
metadata_schema_version: 1.0
document_id: DOC-0216
title: Dashboard Workspaces
plane: Product Specification
domain: Dashboard
class: Specification
authority: Canonical
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/product-specification/dashboard/dashboard-workspaces.md
related_concepts:
  - CONCEPT-0216
dependencies: []
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0079
  - DOC-0100
  - DOC-0218
  - DOC-0277
  - DOC-0344
  - DOC-0386
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: CONTRACT
purpose: Defines dashboard workspaces.
scope: Workspace management.
---

# Dashboard Workspaces

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** UI Team

## Purpose
Defines workspace persistence, restore, sharing, and isolation for desktop sessions — with workspace lifecycle, autosave semantics, crash recovery, multi-profile support, workspace state synchronization, cross-subsystem integration, and workspace manager contracts.

---

## 1. Workspace Lifecycle State Machine

```mermaid
stateDiagram-v2
  [*] --> LOADING
  LOADING --> RESTORING
  RESTORING --> ACTIVE: restore success
  RESTORING --> DEFAULT: corrupt / missing workspace
  DEFAULT --> ACTIVE: default workspace loaded
  ACTIVE --> SAVING: save trigger
  SAVING --> SAVED
  SAVED --> ACTIVE
  ACTIVE --> SWITCHING: workspace change
  SWITCHING --> LOADING: target workspace selected
  ACTIVE --> ARCHIVING: workspace deleted
  ARCHIVING --> ARCHIVED
  ARCHIVED --> [*]
```

---

## 2. Workspace Schema

Each workspace is a JSON object:

```json
{
  "workspace_id": "uuid",
  "name": "Default Trading",
  "version": 3,
  "created_at": "ISO8601",
  "updated_at": "ISO8601",
  "layout": {
    "side_panel_width": 240,
    "right_panel_visible": false,
    "bottom_panel_height": 120
  },
  "active_tab": "trading",
  "tabs": [
    {
      "id": "trading",
      "name": "Trading",
      "route": "/trading",
      "widgets": [
        {"id": "spread-monitor", "position": "main", "config": {}},
        {"id": "trade-list", "position": "right", "config": {}}
      ]
    }
  ],
  "widgets": {
    "spread-monitor": {"config": {"pair": "ETH/USDC", "threshold": 0.5}},
    "trade-list": {"config": {"max_items": 50}}
  },
  "filters": {"chains": ["ethereum", "polygon"], "strategies": ["triangular"]},
  "preferences": {
    "theme": "dark",
    "font_size": 14,
    "auto_save_interval_ms": 30000
  },
  "checksum": "sha256-of-above"
}
```

---

## 3. Save Triggers

| Event | Immediate / Debounced | Debounce Ms |
|-------|----------------------|-------------|
| Panel dock/undock | Immediate | 0 |
| Widget config change | Debounced | 500 |
| Tab reorder | Debounced | 500 |
| Layout resize | Debounced (on resize end) | 500 |
| Workspace switch | Immediate | 0 |
| Periodic autosave | Debounced per `AUTO_SAVE_DEBOUNCE_MS` | 30000 |
| Shutdown | Immediate (blocking flush) | 0 |

---

## 4. Crash Recovery

1. On startup, check for last workspace file `<workspace_id>.json.last`.
2. If file exists and is valid → restore normally.
3. If file is corrupt → try `<workspace_id>.json.last.bak` (previous save).
4. If all corrupt → load default workspace.
5. Recover open widget state from widget store (ephemeral data not persisted).

---

## 5. Multi-Profile Workspace

- Each profile has its own workspace set, stored at `workspaces/<profile_name>/`.
- Switching profiles saves the current workspace and loads the target profile's last workspace.
- Workspaces are isolated per profile — no cross-profile data leakage.

---

## 6. Workspace Management

| Action | API / Command | Effect |
|--------|---------------|--------|
| Create workspace | `POST /api/workspace` | New empty workspace |
| Save workspace | `PUT /api/workspace/:id` | Persist current state |
| Switch workspace | `PUT /api/workspace/:id/activate` | Save current, load target |
| Rename workspace | `PUT /api/workspace/:id/name` | Update name |
| Delete workspace | `DELETE /api/workspace/:id` | Archive, do not delete permanently |
| List workspaces | `GET /api/workspace` | All available workspaces |

---

## Cross-References

- **DASHBOARD-LAYOUT.md** — Layout model, panel placement, docking, serialization, multi-monitor.
- **DASHBOARD-WIDGETS.md** — Widget lifecycle, dependency graph, communication, state synchronization.
- **DASHBOARD-RUNTIME.md** — Dashboard initialization, IPC data flow, cross-subsystem integration.
- **WORKSPACE-MANAGER.md** — Workspace manager service implementation.
- **UI-COMPONENT-SPEC.md** — Design system.
- **CONFIGURATION-REFERENCE.md** — Workspace config keys.
- **END-TO-END-WIRING-CONTRACT.md** — Cross-subsystem wiring.
- **TRACEABILITY-MATRIX.md** — Workspace requirement coverage.

---

## 7. Cross-Subsystem Integration

### 7.1 Who Calls Workspace Manager

| Caller | Purpose | Contract |
|--------|---------|----------|
| Dashboard Runtime | Init workspace, workspace switch | `workspace.init` / `workspace.switch` API |
| Layout Manager | Persist layout changes | `workspace.persistLayout` API |
| Widget Registry | Persist widget config | `workspace.persistWidgetConfig` API |
| Config Manager | Apply config to workspace | `workspace.applyConfig` API |
| Windows Desktop | Sleep/resume triggers | `workspace.suspend` / `workspace.resume` OS events |

### 7.2 Who Workspace Manager Calls

| Target | Purpose | Contract |
|--------|---------|----------|
| Dashboard Runtime | Broadcast workspace switch | `dashboard.workspace.switched` broadcast |
| Layout Manager | Load layout from workspace | `layout.load` API |
| Widget Registry | Load widget config | `widget.loadConfig` API |
| Config Manager | Get workspace-specific config | `config.get` API |
| Event Bus | Emit workspace events | `workspace.*` events |

### 7.3 Events Workspace Manager Emits

| Event | Payload | Consumer |
|-------|---------|----------|
| `workspace.created` | `{workspace_id, name, profile}` | Dashboard, Audit |
| `workspace.switched` | `{from_id, to_id, profile}` | Dashboard, Widgets (broadcast) |
| `workspace.saved` | `{workspace_id, trigger, checksum}` | Audit |
| `workspace.deleted` | `{workspace_id, profile}` | Dashboard, Audit |
| `workspace.corrupted` | `{workspace_id, recovery_action}` | Dashboard, Health |

### 7.4 Events Workspace Manager Consumes

| Event | Source | Handler |
|-------|--------|---------|
| `dashboard.ready` | Dashboard Runtime | Load default workspace |
| `config.updated` | Config Manager | Re-apply config to workspace |
| `plugin.loaded` | Plugin Manager | Add plugin widgets to workspace |
| `plugin.unloaded` | Plugin Manager | Remove plugin widgets from workspace |
| `system.shutdown.phase` | Runtime | Flush workspace to disk |

### 7.5 Configuration Workspace Manager Owns

| Config Key | Default | Description |
|-----------|---------|-------------|
| `workspace.auto_save_interval_ms` | `30000` | Autosave debounce interval |
| `workspace.max_per_profile` | `10` | Max workspaces per profile |
| `workspace.storage_path` | `%APPDATA%/apex/workspaces` | Workspace storage directory |
| `workspace.default_name` | `Default Trading` | Default workspace name |
| `workspace.archive_on_delete` | `true` | Archive instead of permanently delete |

### 7.6 State Workspace Manager Owns

| State Domain | Type | Persistence | Recovery |
|-------------|------|-------------|----------|
| Active workspace | Workspace ID | Profile config | Default workspace |
| Workspace list | Array of workspace metadata | Profile config | Scan storage directory |
| Workspace layout | Panel positions, widget config | Workspace JSON | Default layout |
| Workspace filters | Per-workspace filters | Workspace JSON | No filters (reset) |
| Workspace preferences | Theme, font, autosave | Workspace JSON | Defaults |

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | UI Team |
