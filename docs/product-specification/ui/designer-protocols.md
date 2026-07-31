---
metadata_schema_version: 1.0
document_id: DOC-0395
title: Designer Protocols
plane: Product Specification
domain: UI
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.1
canonical_source: docs/product-specification/ui/designer-protocols.md
related_concepts:
  - CONCEPT-0395
dependencies:
  - DOC-0123
  - DOC-0125
  - DOC-0238
  - DOC-0366
  - DOC-0390
  - DOC-0396
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0391
  - DOC-0393
  - DOC-0394
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Designer Protocols documentation.
scope: Reference documentation.
---

# Designer Protocols

## Document type
[REFERENCE]. This document's front-matter `type` was previously set to
`CONTRACT` while its own body stated "This document is an overview,
reference, or index" — a direct Prime-Directive violation (a document
must declare a single, consistent type). This file is a UI/UX design
system reference (color, typography, spacing, components, accessibility,
patterns) and is correctly classified as [REFERENCE], not [CONTRACT].

## Version
**Version:** 1.0.1 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

# APEX Designer Protocols - UI/UX Design System, Components, Patterns, and Standards

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** The single source of truth for every visual and interaction decision in APEX.

---

## 1. Design Philosophy

APEX is a professional trading desktop app for Windows. It must communicate
**trust, precision, real-time awareness, and control**. Every pixel serves a purpose.

### 1.1 Principles
1. **Clarity Over Decoration** — no ornament; if it doesn't inform or aid action, cut it
2. **Dark-First** — trading apps live in dimmed rooms; dark theme is the default
3. **Real-Time Awareness** — live data must be visually distinct from static data
4. **Progressive Disclosure** — summary first, details on demand
5. **Keyboard-First** — power users must be able to operate the entire app without a mouse
6. **Consistent Spacing** — 4px base grid, no magic numbers
7. **Accessible** — WCAG 2.1 AA compliance is non-negotiable
8. **No Surprises** — destructive actions require confirmation, statuses are honest


### 1.2 AI Usage Policy
1. **Cloud AI Only** — production AI must use approved cloud providers with paid API keys; local LLM inference is unsupported in production.
2. **No Silent Fallback to Local Models** — if cloud providers fail, the system must fall back only to approved cloud fallback providers or safe no-trade behavior.
3. **Provider Governance** — model routing, token usage, and cost controls are governed by the AI pipeline and configuration policy.

---

## 2. Color System

### 2.1 Brand & Surface
| Token | Hex | Usage |
|-------|-----|-------|
| `bg.primary` | `#0a0a0f` | Window background |
| `bg.secondary` | `#12121a` | Card / panel background |
| `bg.tertiary` | `#1a1a2e` | Hover, raised surface |
| `bg.overlay` | `rgba(0,0,0,0.6)` | Modal scrim |

### 2.2 Text
| Token | Hex | Usage |
|-------|-----|-------|
| `text.primary` | `#e4e4e7` | Body text, headings |
| `text.secondary` | `#a1a1aa` | Sub-labels, captions |
| `text.muted` | `#52525b` | Disabled, reserved example |
| `text.inverted` | `#0a0a0f` | On light / accent backgrounds |

### 2.3 Accent
| Token | Hex | Usage |
|-------|-----|-------|
| `accent.primary` | `#6366f1` | Primary action, focus, links |
| `accent.hover` | `#818cf8` | Hover state |
| `accent.pressed` | `#4f46e5` | Pressed state |
| `accent.subtle` | `rgba(99,102,241,0.12)` | Selected row tint |

### 2.4 Semantic
| Token | Hex | Usage |
|-------|-----|-------|
| `success` | `#22c55e` | Profit, connected, success toast |
| `danger` | `#ef4444` | Loss, error, destructive, disconnected |
| `warning` | `#f59e0b` | Caution, syncing, untested |
| `info` | `#3b82f6` | Informational, neutral highlight |
| `border.default` | `#27272a` | Default border |
| `border.strong` | `#3f3f46` | Emphasized border |
| `focus.ring` | `#6366f1` | Keyboard focus |

### 2.5 Status
| State | Color | Animation |
|-------|-------|-----------|
| Connected | `#22c55e` | 2s ease-in-out pulse |
| Disconnected | `#ef4444` | none |
| Syncing | `#f59e0b` | 1.5s rotate (spinner) |
| Idle | `#52525b` | none |

---

## 3. Typography

- **UI Font:** `Inter` (self-hosted, weights 400/500/600/700)
- **Mono Font:** `JetBrains Mono` (weights 400/500) — for numbers, addresses, code
- **Numeric:** `font-variant-numeric: tabular-nums` always

| Role | Size | Weight | Line height |
|------|------|--------|-------------|
| Display | 28px | 700 | 1.2 |
| H1 | 22px | 600 | 1.25 |
| H2 | 18px | 600 | 1.3 |
| H3 | 16px | 600 | 1.4 |
| Body | 14px | 400 | 1.5 |
| Body Strong | 14px | 500 | 1.5 |
| Caption | 12px | 400 | 1.4 |
| Micro | 11px | 500 | 1.3, uppercase, tracking 0.05em |

---

## 4. Spacing & Layout Grid

Base unit: **4px**. Allowed increments: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80.

Common paddings: card `24px`, button `0 16px`, input `0 12px`, modal `32px`.

### 4.1 Layout Regions
- **Sidebar:** 240px expanded, 64px collapsed (icons only)
- **Top Bar:** 48px fixed
- **Status Bar:** 32px fixed at bottom
- **Content Area:** flex-1, max-width none, scrollable
- **Min window:** 1024 × 680
- **Default window:** 1400 × 900
- **Below 1280px wide:** sidebar auto-collapses
- **Snap to:** no snap; user-controlled

---

## 5. Component Library

All components live in `src/components/`. Reuse them — never inline ad-hoc styles.

### 5.1 Button
- **Heights:** sm 28px, md 36px, lg 44px
- **Radius:** 8px
- **Padding:** 0 16px (md)
- **Variants:** primary, secondary, ghost, danger, danger-ghost
- **States:** default, hover (+4% lightness), pressed (-4%), disabled (40% opacity, no pointer)
- **Loading:** spinner replaces label, width preserved
- **Icon-only:** square button, 36×36, icon 16px
- **Keyboard:** Enter/Space to activate, focus ring 2px `focus.ring`

### 5.2 Card
- `bg.secondary` background
- 1px `border.default`
- 12px radius
- Padding 16px (compact) or 24px (default)
- No shadow (depth via border + bg)
- Optional `title`, `subtitle`, `actions` slot in header
- Optional `loading` skeleton state

### 5.3 Input
- Height 36px
- `bg.primary` background, 1px `border.default`
- 8px radius
- Label above (12px caption), helper text below (12px secondary)
- States: default, focus (border `accent.primary`, 2px ring), error (border `danger`, error text below), disabled
- Variants: text, password (with eye toggle), number (with stepper), search (with leading icon)
- **API key inputs** must use `type="password"` by default with reveal toggle; never autofill

### 5.4 Select
- Native `<select>` is banned (inconsistent rendering). Use a custom dropdown:
  - Trigger matches Input style
  - Menu: 8px radius, 240px max width, scroll if > 8 options
  - Option: 32px height, hover `bg.tertiary`, selected has check icon

### 5.5 Toggle / Switch
- 32×18 track, 14px thumb
- Off: `bg.tertiary` track, `text.secondary` thumb
- On: `accent.primary` track, white thumb
- Label right of switch, help text below
- Keyboard: Space to toggle, focus ring

### 5.6 Table
- Header: 11px uppercase, `text.secondary`, 40px row height
- Body rows: 40px, alternating `bg.primary` and `bg.secondary` (subtle zebra)
- Hover: `bg.tertiary`
- Numeric columns: right-aligned, mono font, tabular-nums
- Sorting: clickable header, sort icon, default sort state persisted
- Selection: checkbox column optional, selected row gets `accent.subtle` background
- Empty state: centered illustration + message + optional action
- Loading: skeleton rows, 8 rows

### 5.7 Tabs
- Underline style
- 40px height
- Active: `accent.primary` 2px underline, `text.primary` label
- Inactive: `text.secondary`, hover `text.primary`
- Optional count badge in `bg.tertiary`
- Keyboard: ← / → to navigate, Enter to activate

### 5.8 Modal
- Scrim: `bg.overlay`
- Panel: `bg.secondary`, 12px radius, max 480px (sm) / 720px (md) / 90vw (lg)
- Header: title + close button (Esc also closes)
- Body: scrollable
- Footer: right-aligned actions, primary on the right
- **Destructive actions** in footer require a typed-confirmation or explicit checkbox
- Trap focus, restore focus to opener on close

### 5.9 Toast
- Bottom-right, max 3 stacked
- 5s auto-dismiss (10s for errors)
- Variants: success, info, warning, error
- 4px left border in semantic color
- Title + optional description, optional action button
- Click to dismiss, × button always present

### 5.10 Status Indicators
- **Status Dot:** 8px circle, color per state, optional pulse
- **Status Bar Item:** icon + label + value, used in status bar
- **Connection Chip:** 8px dot + label (Connected/Disconnected/Syncing), 24px height

### 5.11 Empty / Loading / Error States
Every async view must define all three:
- **Empty:** illustration + headline + sub-copy + optional CTA
- **Loading:** skeleton matching final layout, no spinners for content
- **Error:** icon + headline + reason + retry button + copy-details toggle

### 5.12 Charts (Recharts-based)
- Dark theme by default
- Axis labels: `text.secondary`, 11px
- Grid lines: `border.default`, 1px, dashed
- Series colors: cycle through `accent.primary`, `success`, `warning`, `info`, `danger`
- Tooltip: `bg.secondary` card, mono for numbers
- Always show legend unless only one series
- Crosshair on hover; no click interactions unless intentional

### 5.13 AI-Specific Components
- **StreamingText:** displays tokens as they arrive, with subtle 1px caret; "Stop" button in corner
- **ConfidenceBar:** 0-100 horizontal bar, color from `danger` to `success` gradient
- **ToolCallCard:** collapsible card showing tool name, args, result, latency
- **AgentStatusPill:** dot + agent name + state (idle/thinking/calling_tool/streaming/done/error)
- **ReasoningTrace:** collapsible expandable section for "thinking" content
- **CostBadge:** `tokens in/out` + `$cost` in mono, muted color

---

## 6. Navigation

### 6.1 Sidebar
- Logo at top (24px, links to Dashboard)
- Primary nav: Dashboard, Trades, Opportunities, Skills, Agents, Settings
- Each item: 20px icon + 14px label, 40px height
- Active state: `accent.subtle` background, 2px left border `accent.primary`
- Collapse toggle at bottom (also: `Ctrl+B`)
- Footer: user avatar, version, connection status

### 6.2 Top Bar
- Left: page title (H1)
- Center: global search (Ctrl+K) — searches trades, tokens, agents, skills
- Right: theme toggle, notifications bell (with count), settings gear, window controls

### 6.3 Status Bar
- Left: chain status chips (green dot = healthy, red = down, syncing = spinner)
- Center: current gas gwei per chain
- Right: AI status (last call, daily cost), app version

---

## 7. Animation

- **Micro:** 150ms ease-out (hover, focus)
- **Transitions:** 300ms `cubic-bezier(0.4, 0, 0.2, 1)` (panel open, route change)
- **Live pulse:** 2s ease-in-out infinite (status dot when live)
- **Number flash:** 200ms background color tween (green/red on change)
- **Page enter:** 10px upward slide + fade-in 200ms
- **Page exit:** 10px downward slide + fade-out 150ms
- **Streaming text:** caret blink 1s step-end
- **No gratuitous animation:** if it doesn't aid comprehension, remove it
- Respect `prefers-reduced-motion`: disable non-essential animations

---

## 8. Iconography

- Library: **Lucide React** (16/20/24px, 1.5px stroke)
- Custom icons only for: chain logos (load from `assets/chains/`), APEX logo
- Icons inherit `currentColor`; never hardcode color
- Icon button: 36×36, icon 16px, 8px radius

---

## 9. Keyboard Shortcuts (App-Wide)

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Global search / command palette |
| `Ctrl+B` | Toggle sidebar |
| `Ctrl+,` | Open Settings |
| `Ctrl+1..9` | Jump to page (1=Dashboard, 2=Trades, etc.) |
| `Ctrl+S` | Save (in settings) |
| `Ctrl+T` | Test connection (in AI Settings) |
| `Ctrl+R` | Reset (in settings, with confirm) |
| `Ctrl+N` | Add new (context-dependent) |
| `Esc` | Close modal / cancel |
| `Tab` / `Shift+Tab` | Navigate forward / back |
| `↑` `↓` | Navigate lists |
| `Enter` | Activate / open |
| `?` | Show shortcut cheat sheet |

Shortcuts are surfaced in the **Help → Shortcuts** modal and discoverable via `Ctrl+K`.

---

## 10. Theming

- **Default theme:** Dark (defined in §2)
- **Light theme:** defined as override palette (see Appendix A)
- **Toggle:** Top bar, persisted in SQLite
- **System follow:** optional, listens to `prefers-color-scheme`
- **Per-component overrides:** allowed for charts only

---

## 11. Accessibility (WCAG 2.1 AA)

- All text contrast ≥ 4.5:1; large text ≥ 3:1
- Color is never the sole indicator (use icon + text)
- All interactive elements keyboard reachable
- Focus ring: 2px `accent.primary` outline, 2px offset
- ARIA labels on icon-only buttons, form fields, live regions
- Screen reader announcements for: toasts, status changes, streaming AI start/stop
- Respect `prefers-reduced-motion`
- DPI-aware: layouts tested at 100/125/150/200%
- No flashing content > 3 Hz (seizure safety)
- Form errors associated via `aria-describedby`

---

## 12. Patterns

### 12.1 Destructive Action Confirmation
Pattern: clicking Delete/Reset opens a Modal with:
- Title naming the action and target
- Plain-language description of what will be removed
- For high-impact: text input "type the provider name to confirm"
- Cancel + Confirm (danger variant) buttons

### 12.2 Long-Running Operation
- Show progress bar if determinate, spinner if indeterminate
- Show elapsed time after 2s
- "Cancel" button if operation supports it
- On completion: success toast + auto-dismiss OR result dialog
- On failure: error toast with "Retry" + "Copy details"

### 12.3 AI Settings Page — Full Pattern
- Title: "AI Configuration"
- Subtitle: "Configure your cloud AI providers for APEX intelligence"
- Status header: aggregate health across providers (green/yellow/red dot + label)
- Provider cards (vertical, expandable):
  - Header: name, type chip, status dot, enable toggle, kebab menu (Edit, Duplicate, Reset, Delete)
  - Body (when expanded): all fields from `../ai/ai-settings.md` §3
  - Footer: Test, Save, Reset buttons (Save disabled until dirty + valid)
  - "Add Provider" button below all cards
- Per-provider "Advanced" disclosure: proxy, custom headers, request timeout, retry policy
- Bottom: "Save All" / "Reset All" / "Clear AI Cache" / "Export Diagnostics (no keys)"

### 12.4 Streaming AI Response
- Card with agent name + model
- "Stop" button top-right
- Tokens appear left-to-right in mono
- Below: collapsed "Reasoning" (if model produces it)
- Footer on completion: latency, input/output tokens, cost, copy button

### 12.5 Trade Row
- Mono hash (truncated middle, hover full)
- Pair `ETH/USDC` + chain badge
- Profit / Loss: green or red, mono
- Status chip
- Time (relative, e.g. "2m ago"; hover → absolute)
- Row click → drawer with full details

### 12.6 Empty Dashboard
- Centered: illustration, "No active strategies yet", sub-copy
- CTAs: "Enable a skill" / "Configure AI" / "Read the quickstart"

---

## 13. Microcopy Tone

- **Direct, not chatty:** "Trade failed" not "Oh no, that didn't work"
- **Active voice:** "Reset saved providers" not "Providers will be reset"
- **Specific:** "API key rejected (401)" not "Something went wrong"
- **Honest:** "Cannot reach OpenAI — check your network" not "Please try again"
- **No exclamation marks in errors.** Success toasts can use one.

---

## 14. Responsive Behavior

APEX is desktop-only. We define behavior for:
- **≥ 1440px:** full layout, expanded sidebar by default
- **1280–1439px:** expanded sidebar, tighter padding
- **1024–1279px:** sidebar collapsed, status bar condensed
- **< 1024px:** show "Please enlarge your window" overlay; app still runs but warns

Mobile and tablet are explicitly **not** goals.

---

## 15. Versioning & Breaking Changes

- **Patch versions** (3.0.x): tokens added, no removals
- **Minor versions** (3.x.0): new components, deprecations allowed
- **Major versions** (x.0.0): breaking token renames, removals
- All changes recorded in `../reference/changelog.md` with date and PR link

---

## Appendix A — Light Theme Override

(Future work; current spec ships Dark only. Light is a v3.1 milestone.)

| Token | Dark | Light |
|-------|------|-------|
| `bg.primary` | `#0a0a0f` | `#fafafa` |
| `bg.secondary` | `#12121a` | `#ffffff` |
| `text.primary` | `#e4e4e7` | `#18181b` |
| `text.secondary` | `#a1a1aa` | `#52525b` |
| `border.default` | `#27272a` | `#e4e4e7` |

(All accent and semantic colors stay constant across themes.)

---

*If a designer or engineer is making a UI decision in APEX, this document has the answer. If it doesn't, propose the change here first.*

## Cross-references
- `./ui-component-spec.md`
- `../windows/windows-desktop.md`
- `../ai/ai-settings.md`
- `./user-flows.md`
- `../ai/cloud-ai-integration.md`

## Governance Rules
Defines design review flow, component conventions, naming, and artifact handoff requirements.

## Example
A new panel must pass layout and accessibility review before release.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.1 | 2026-07-29 | Corrected front-matter `type` from `CONTRACT` to `REFERENCE` to resolve an internal self-contradiction (body previously stated this is "an overview, reference, or index"). Rewrote the Document type section to state the correction explicitly. Substantive design-system content unchanged. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section (superseded by 1.0.1 above; incorrectly declared [CONTRACT] compliance at the time). | Runtime Team |
