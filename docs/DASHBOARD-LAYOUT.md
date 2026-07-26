# Dashboard Layout

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.3.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Dashboard Team

## Purpose
Defines the layout model for the Windows desktop dashboard — layout persistence, DPI scaling, multi-monitor support, responsive regions, docking, split views, panels, and tab sets.

---

## 1. Layout Architecture

### 1.1 Primary Regions

```
┌─────────────────────────────────────────────────────┐
│  Title Bar (menu, workspace selector, status icons) │
├────────────────────┬────────────────────────────────┤
│                    │                                │
│  Side Panel        │  Main Content Area             │
│  (docked)          │  (tabs, split views, widgets)  │
│                    │                                │
│  - Navigation      │                                │
│  - Workspace list  │                                │
│  - Quick actions   │                                │
│                    │                                │
├────────────────────┴────────────────────────────────┤
│  Status Bar (health, connections, mode indicator)   │
└─────────────────────────────────────────────────────┘
```

### 1.2 Secondary Regions
| Region | Purpose | Collapsible | Default Visibility |
|--------|---------|-------------|-------------------|
| Right panel | Context inspector, trade detail | Yes | Hidden |
| Bottom panel | Log viewer, event stream | Yes | Hidden |
| Floating widgets | Charts, heatmaps (overlays) | N/A | Configurable |

---

## 2. Docking System

| Anchor | Valid Panels | Behavior |
|--------|-------------|----------|
| Left | Nav, workspace list, quick actions | Fixed width (24–300px), resizable |
| Right | Inspector, trade detail | Collapsible, auto-hide |
| Top | Toolbar | Fixed height (32px) |
| Bottom | Logs, events | Resizable, min height 80px |

### Docking Rules
- Panels can be dragged between anchors.
- Only one panel per anchor position (multiple panels share via tabs).
- Panels are persisted to workspace state on dock/undock.
- Float mode: panels can be detached to standalone windows.

---

## 3. DPI Scaling & Multi-Monitor

| Feature | Implementation |
|---------|---------------|
| DPI awareness | Per-monitor DPI aware (Windows `DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE`) |
| Scaling | All layout positions stored in logical pixels, scaled at render |
| Multi-monitor | Workspace save/restore includes monitor index, display scale |
| Snap restore | On reconnect, panels restore to their original monitor |
| High-DPI fallback | Minimum 1920×1080 effective resolution at 150% scaling |

---

## 4. Responsive Behavior

| Viewport Width | Layout Mode | Changes |
|----------------|-------------|---------|
| >= 1920px | Full | All panels visible |
| 1280–1919px | Compact | Right panel auto-hides; side panel shrinks to icons |
| 800–1279px | Narrow | Bottom panel collapses; floating widgets hide |
| < 800px | Minimal | Side panel collapses to hamburger menu; status bar minimized |

---

## 5. Layout Persistence

- Layout state is serialized to JSON as part of workspace.
- Save trigger: on dock change, resize end, panel toggle (debounced 500ms).
- Auto-restore on workspace load.
- Fallback: default layout on first launch or corrupt layout state.

---

## 6. Tab Sets

- Main content area supports multiple tabs.
- Each tab is an independent scope (e.g., "Trading", "Analysis", "Plugins").
- Tabs can be reordered, split to separate windows, or merged.
- Tab state is persisted in workspace.

---

## Cross-References

- **DASHBOARD-WIDGETS.md** — Widget behavior within panels.
- **DASHBOARD-WORKSPACES.md** — Workspace lifecycle and persistence.
- **DASHBOARD-RUNTIME.md** — Dashboard initialization, page routing, data flow.
- **WINDOWS-DESKTOP.md** — Windows desktop window management.
- **UI-COMPONENT-SPEC.md** — Component design system.
- **CONFIGURATION-REFERENCE.md** — Dashboard config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.3.0 | 2026-07-27 | Full layout architecture, docking, DPI scaling, multi-monitor, responsive breakpoints | Dashboard Team |
| 0.1.0 | 2026-07-27 | Initial stub | Dashboard Team |