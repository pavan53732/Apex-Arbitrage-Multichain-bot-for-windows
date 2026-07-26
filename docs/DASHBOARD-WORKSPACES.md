# Dashboard Workspaces

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.3.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Dashboard Team

## Purpose
Defines workspace persistence, restore, sharing, and isolation for desktop sessions — with workspace lifecycle, autosave semantics, crash recovery, and multi-profile support.

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

- **DASHBOARD-LAYOUT.md** — Layout model and panel placement.
- **TRACEABILITY-MATRIX.md** — Requirement-to-document mapping and governance validation.
- **DASHBOARD-WIDGETS.md** — Widget lifecycle and data binding.
- **DASHBOARD-RUNTIME.md** — Dashboard initialization and data flow.
- **WORKSPACE-MANAGER.md** — Workspace manager service.
- **UI-COMPONENT-SPEC.md** — Design system.
- **CONFIGURATION-REFERENCE.md** — Workspace config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.3.0 | 2026-07-27 | Full workspace lifecycle, schema, save triggers, crash recovery, multi-profile, management API | Dashboard Team |
| 0.1.0 | 2026-07-27 | Initial stub | Dashboard Team |