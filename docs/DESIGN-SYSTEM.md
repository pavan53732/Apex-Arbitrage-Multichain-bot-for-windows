# DESIGN-SYSTEM.md

## Purpose
Defines the reusable design tokens and interaction rules that govern all APEX UI surfaces.

## Scope
Typography, spacing, color roles, elevation, density, layout grid, motion, and accessibility treatment.

## Ownership
UI maintainers own the design system; feature teams consume tokens and patterns but do not redefine them locally.

## Design Principles
- Dark-first desktop productivity UI.
- Dense but readable layout.
- Status information must be immediately scannable.
- Risk and execution state must be visually distinct from informational data.

## Token Categories
### Color
- `bg`, `surface`, `surfaceAlt`, `border`, `textPrimary`, `textSecondary`, `accent`, `success`, `warning`, `danger`, `info`.
- Each token must have a semantic meaning and not be used directly for arbitrary styling.

### Typography
- One base sans family for UI.
- Fixed-size monospace family for logs, addresses, hashes, and code.
- Scale defined for page title, section title, body, caption, and numeric emphasis.

### Spacing
- Use a fixed spacing scale only.
- Avoid ad hoc pixel values except for border rendering and one-off icon alignment.

### Elevation and Borders
- Panels use subtle elevation.
- Critical state surfaces use border + color + icon, not color alone.

### Accessibility
- All interactive elements require keyboard focus visibility.
- Color contrast must meet or exceed WCAG AA for text.
- Status must never be encoded by color alone.
- Modals and drawers must trap focus and be dismissible by keyboard.

## Interaction Rules
- Primary actions appear as a single clear CTA.
- Destructive actions require explicit confirmation.
- Disabled state must explain why the action is unavailable.
- Busy state must preserve layout and indicate progress.

## Component Styling Rules
- Components consume tokens only; do not redefine local semantic colors.
- Variants must be documented before use.
- Charts and tables must preserve legibility under dense data.

## Cross-References
- [`UI-COMPONENT-SPEC.md`](./UI-COMPONENT-SPEC.md)
- [`DESIGNER-PROTOCOLS.md`](./DESIGNER-PROTOCOLS.md)
- [`PERMISSION-MODEL.md`](./PERMISSION-MODEL.md)
