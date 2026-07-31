---
metadata_schema_version: 1.0
document_id: DOC-0213
title: Dashboard Layout
plane: Product Specification
domain: Dashboard
class: Specification
authority: Canonical
status: Active
owner: Dashboard Team
version: 1.0.0
canonical_source: docs/product-specification/dashboard/dashboard-layout.md
related_concepts:
  - CONCEPT-0213
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Dashboard
type: CONTRACT
purpose: "Defines the layout model for the Windows desktop dashboard — layout architecture, docking system, layout serialization, workspace restore, DPI scaling, multi-monitor behavior, responsive regions, split views, tab sets, and layout integration contracts."
scope: Dashboard Layout scope and boundaries.
---

# Dashboard Layout

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Dashboard Team

## Purpose
Defines the layout model for the Windows desktop dashboard — layout architecture, docking system, layout serialization, workspace restore, DPI scaling, multi-monitor behavior, responsive regions, split views, tab sets, and layout integration contracts.

---

## 1. Layout Architecture

### 1.1 Primary Regions

```
┌─────────────────────────────────────────────────────┐
│  Title Bar (menu, workspace selector, status icons) │
│  Height: 32px (fixed)                               │
├────────────────────┬────────────────────────────────┤
│                    │                                │
│  Side Panel        │  Main Content Area             │
│  (docked)          │  (tabs, split views, widgets)  │
│  24–300px (resz.)  │  Flexible width                │
│                    │                                │
│  - Navigation      │                                │
│  - Workspace list  │                                │
│  - Quick actions   │                                │
│                    │                                │
├────────────────────┴────────────────────────────────┤
│  Status Bar (health, connections, mode indicator)   │
│  Height: 24px (fixed)                               │
└─────────────────────────────────────────────────────┘
```

### 1.2 Secondary Regions

| Region | Purpose | Collapsible | Default Visibility | Default Size | Min Size | Max Size |
|--------|---------|-------------|-------------------|-------------|----------|----------|
| Right panel | Context inspector, trade detail | Yes | Hidden | 300px wide | 200px | 600px |
| Bottom panel | Log viewer, event stream | Yes | Hidden | 120px tall | 80px | 400px |
| Floating widgets | Charts, heatmaps (overlays) | N/A | Configurable | Per widget | Widget min | Widget max |

---

## 2. Docking System

### 2.1 Dock Anchors

| Anchor | Valid Panels | Default Width/Height | Resizable | Min | Max | Behavior |
|--------|-------------|---------------------|-----------|-----|-----|----------|
| Left | Nav, workspace list, quick actions | 240px | Yes | 24px | 300px | Fixed width, icon mode when < 100px |
| Right | Inspector, trade detail | 300px | Yes | 200px | 600px | Collapsible, auto-hide on focus loss |
| Top | Toolbar | 32px | No | 32px | 32px | Fixed height |
| Bottom | Logs, events | 120px | Yes | 80px | 400px | Resizable, auto-hide option |

### 2.2 Docking Rules

1. Panels can be dragged between anchors — one panel per anchor position.
2. Multiple panels share the same anchor via **tab stacking** (tab bar within panel).
3. Dock/undock transitions are animated (< 200ms slide animation).
4. Panel state (anchor, width, height, visibility) persisted to workspace on every change.
5. Float mode: panels can be detached to standalone Windows windows (see §7).
6. Auto-hide panels: panel slides in on hover, slides out after 3s of no interaction.
7. Collapsed side panel: shows only icons (24px width) with tooltips for labels.
8. Panel resize: drag handle on panel edge, min/max constraints enforced.

### 2.3 Docking Contract

```json
{
  "panel_id": "side-nav",
  "anchor": "left",
  "width": 240,
  "height": null,
  "collapsed": false,
  "auto_hide": false,
  "tab_stack": ["navigation", "workspaces", "quick-actions"],
  "active_tab": "navigation",
  "floating": false,
  "monitor_index": 0,
  "z_index": 100
}
```

---

## 3. Layout Serialization

### 3.1 Layout JSON Schema

The layout is serialized as part of the workspace JSON:

```json
{
  "layout_id": "uuid",
  "version": 3,
  "shell": {
    "title_bar": {
      "visible": true,
      "menu_items": ["file", "edit", "view", "help"],
      "workspace_selector_visible": true,
      "status_icons": ["health", "network", "ai", "mode"]
    },
    "status_bar": {
      "visible": true,
      "height": 24,
      "sections": ["health", "connections", "mode", "alerts"]
    }
  },
  "panels": {
    "left": {
      "panel_id": "side-nav",
      "anchor": "left",
      "width": 240,
      "collapsed": false,
      "auto_hide": false,
      "tab_stack": ["navigation", "workspaces", "quick-actions"],
      "active_tab": "navigation"
    },
    "right": {
      "panel_id": "inspector",
      "anchor": "right",
      "width": 300,
      "visible": false,
      "auto_hide": true
    },
    "bottom": {
      "panel_id": "logs",
      "anchor": "bottom",
      "height": 120,
      "visible": false,
      "auto_hide": false
    }
  },
  "main_content": {
    "tab_set": [
      {"id": "trading", "route": "/trading", "split_view": false},
      {"id": "analysis", "route": "/analysis", "split_view": false}
    ],
    "active_tab": "trading",
    "split_views": {}
  },
  "floating_panels": [],
  "checksum": "sha256-of-above"
}
```

### 3.2 Serialization Rules

- Layout is serialized on every dock change, resize end, panel toggle (debounced 500ms).
- Layout version must match current schema version — mismatches trigger migration.
- Layout checksum validates integrity — corrupt layout triggers fallback.
- Layout is stored at `workspaces/<profile>/<workspace_id>/layout.json`.
- Layout JSON is human-readable (no binary encoding).

### 3.3 Layout Migration

| From Version | To Version | Migration Action |
|-------------|-----------|-----------------|
| 1 → 2 | Add `floating_panels` field | Default to empty array |
| 2 → 3 | Add `shell` and `main_content.split_views` | Default to empty |
| Future | Schema registry validates | Auto-migration with warning log |

---

## 4. Workspace Restore

### 4.1 Restore Sequence

```
1. Load workspace JSON from storage.
2. Validate checksum — if invalid, try .bak file.
3. Validate layout version — if outdated, apply migration.
4. Validate panel dimensions against current monitor dimensions.
5. Clamp any out-of-bounds dimensions to current viewport.
6. Assign widgets to panels based on workspace config.
7. Call onResume() for each widget.
8. Dashboard signals dashboard.ready event.
```

### 4.2 Restore Failure Recovery

| Failure | Recovery Action |
|---------|----------------|
| Workspace file missing | Load default workspace |
| Workspace file corrupt (checksum mismatch) | Try `.bak` file; if also corrupt → default workspace |
| Layout version mismatch | Apply migration; if migration fails → default layout |
| Panel dimensions exceed current viewport | Clamp to viewport bounds with proportional scaling |
| Monitor index unavailable (monitor disconnected) | Move all panels to primary monitor, cascade layout |
| Widget config references unknown widget | Skip widget, show empty panel |

---

## 5. DPI Scaling

### 5.1 DPI Scaling Rules

| Rule | Implementation |
|------|---------------|
| **DPI awareness** | Per-monitor DPI aware (`DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE`) |
| **Coordinate system** | All layout positions stored in **logical pixels** (1x scale) |
| **Rendering** | Scale logical pixels to physical pixels at render time per monitor |
| **Font scaling** | Base font size (`dashboard.font_size`) multiplied by monitor DPI scale |
| **Icon scaling** | SVG icons rendered at physical pixel size |
| **Touch targets** | Minimum 44×44 logical pixels regardless of DPI |
| **Minimum effective resolution** | 1920×1080 at 150% scaling (1280×720 logical) |

### 5.2 DPI Change Handling

| Event | Action |
|-------|--------|
| **Monitor DPI change** | Re-render all widgets on affected monitor at new scale |
| **Monitor DPI change during drag** | Recalculate ghost widget size at new DPI; adjust drop zones |
| **Mixed DPI monitors** | Each panel renders at its host monitor's DPI; no global scaling |
| **DPI change on startup** | Validate saved dimensions against new DPI; clamp if needed |

---

## 6. Multi-Monitor Behavior

### 6.1 Multi-Monitor Layout Rules

| Scenario | Behavior |
|----------|----------|
| Widget on Monitor A | Renders at Monitor A's DPI |
| Drag widget to Monitor B | Ghost widget re-scales during drag at Monitor B's DPI |
| Drop widget on Monitor B | Full re-render at Monitor B's DPI; position saved |
| Monitor disconnect | All panels on disconnected monitor cascade to primary monitor |
| Monitor reconnect | Panels restore to saved positions if monitor index matches |
| New monitor added | No automatic redistribution — user can move panels manually |
| Full-screen on Monitor B | Dashboard respects full-screen on that monitor only |
| Windowed across monitors | Main window on primary, floating panels on secondary |

### 6.2 Multi-Monitor Persistence

```json
{
  "panel_id": "inspector",
  "monitor_index": 1,
  "position": {"x": 0, "y": 32},
  "size": {"width": 300, "height": 800},
  "dpi_scale": 1.25
}
```

- Workspace stores `{monitor_index, x, y, width, height, dpi_scale}` per panel.
- On restore, if `monitor_index` is unavailable, panel moves to primary monitor.
- Position validated against available monitors before rendering.

---

## 7. Float / Detach Mode

### 7.1 Floating Panel Rules

| Rule | Implementation |
|------|---------------|
| **Detach trigger** | Drag panel past dock anchor boundary (> 20px outside anchor) |
| **Detach animation** | Panel slides out of dock → becomes standalone window (200ms) |
| **Floating window** | Independent Windows window with own title bar, close button |
| **Max floating panels** | 3 (configurable via `dashboard.max_floating_panels`) |
| **Floating panel sizing** | Retains last dock size; resizable within widget min/max bounds |
| **Floating panel position** | Positioned near dock anchor exit point; user can move freely |
| **Floating panel data** | Same IPC channels — data independent of dock position |
| **Re-dock trigger** | Drag floating panel title bar back to dock anchor zone |
| **Re-dock animation** | Panel slides back into dock (200ms) |
| **Close floating panel** | Widget enters SUSPENDED state; panel removed from layout |
| **Persist floating panels** | Floating panel state saved to workspace JSON |

### 7.2 Floating Panel Window Properties

| Property | Value |
|----------|-------|
| Window title | Widget name |
| Always-on-top | No (unless operator toggles) |
| Minimize | Minimize to tray (not taskbar) |
| Maximize | Disabled (fixed size within min/max bounds) |
| Show in taskbar | No |
| Owner window | Main dashboard window |

---

## 8. Responsive Behavior

| Viewport Width | Layout Mode | Changes | Animation |
|----------------|-------------|---------|-----------|
| >= 1920px | Full | All panels visible | None |
| 1280–1919px | Compact | Right panel auto-hides; side panel shrinks to icon mode (24px) | 300ms slide |
| 800–1279px | Narrow | Bottom panel collapses; floating widgets hide; tab bar simplifies | 300ms slide |
| < 800px | Minimal | Side panel → hamburger menu; status bar → single-line; tabs → dropdown | 200ms slide |

### Responsive Transition Rules
- Transitions triggered by window resize (debounced 300ms).
- Each transition saves layout state before changing.
- Reverse transition restores saved layout (not default).
- Responsive mode is persisted — on restart, layout restores to last responsive mode.

---

## 9. Tab Sets & Split Views

### 9.1 Tab Set Rules

| Rule | Implementation |
|------|---------------|
| Tab creation | New tab via menu, keyboard shortcut, or workspace restore |
| Tab activation | Click tab label; widget suspend/resume lifecycle triggered |
| Tab reorder | Drag tab label to new position; persisted immediately |
| Tab close | Click tab close button; widget enters UNLOADING state |
| Tab split | Drag tab past split threshold → creates side-by-side split view |
| Tab merge | Drag split tab back to single tab bar → merges |

### 9.2 Split View Rules

| Rule | Implementation |
|------|---------------|
| Split trigger | Tab split handle or menu "Split View" action |
| Split direction | Horizontal (side-by-side) or Vertical (stacked) |
| Split ratio | 50/50 default; adjustable via split handle drag (min 20%) |
| Split persistence | Split state saved in workspace layout JSON |
| Split collapse | Drag split handle to min ratio → merge back to single |
| Max splits | 2 per main content area (3 total sections) |

---

## 10. Cross-Subsystem Integration Contracts

### 10.1 Who Calls Layout

| Caller | Purpose | Contract |
|--------|---------|----------|
| Dashboard Runtime | Init/restore layout | `layout.init` → layout loads from workspace |
| Workspace Manager | Workspace switch | `workspace.switched` → layout saves current, loads target |
| Widget Registry | Widget registration | `widget.registered` → layout allocates slot |
| Windows Desktop | DPI change / monitor change | OS event → layout re-validates dimensions |

### 10.2 Events Layout Emits

| Event | Payload | Consumer |
|-------|---------|----------|
| `layout.changed` | `{change_type, panel_id, anchor, dimensions}` | Workspace Manager (persist), Dashboard Runtime (broadcast) |
| `layout.responsive.transition` | `{from_mode, to_mode, viewport_width}` | Dashboard Runtime, Widgets (broadcast) |

### 10.3 Configuration Layout Owns

| Config Key | Default | Description |
|-----------|---------|-------------|
| `dashboard.layout.default_side_panel_width` | `240` | Default side panel width |
| `dashboard.layout.default_right_panel_width` | `300` | Default right panel width |
| `dashboard.layout.default_bottom_panel_height` | `120` | Default bottom panel height |
| `dashboard.layout.max_floating_panels` | `3` | Maximum floating panels |
| `dashboard.layout.auto_hide_delay_ms` | `3000` | Auto-hide panel delay |
| `dashboard.layout.dock_animation_ms` | `200` | Dock/undock animation duration |
| `dashboard.layout.responsive_transition_ms` | `300` | Responsive mode transition duration |

---

## Cross-References

- **DASHBOARD-WIDGETS.md** — Widget lifecycle, rendering, dependency graph, drag-and-drop.
- **DASHBOARD-WORKSPACES.md** — Workspace lifecycle, persistence, crash recovery.
- **DASHBOARD-RUNTIME.md** — Dashboard initialization, IPC data flow, cross-subsystem integration.
- **WINDOWS-DESKTOP.md** — Windows desktop window management, DPI, multi-monitor.
- **UI-COMPONENT-SPEC.md** — Component design system.
- **CONFIGURATION-REFERENCE.md** — Dashboard config keys.
- **END-TO-END-WIRING-CONTRACT.md** — Cross-subsystem wiring.
- **TRACEABILITY-MATRIX.md** — Layout requirement coverage.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade layout contract: dock contract schema, layout serialization with migration, workspace restore failure recovery, DPI scaling per-monitor, multi-monitor persistence, float/detach mode, responsive transitions, split views, cross-subsystem integration | Dashboard Team |
| 0.3.0 | 2026-07-27 | Full layout architecture, docking, DPI scaling, multi-monitor, responsive breakpoints | Dashboard Team |
| 0.1.0 | 2026-07-27 | Initial stub | Dashboard Team |
