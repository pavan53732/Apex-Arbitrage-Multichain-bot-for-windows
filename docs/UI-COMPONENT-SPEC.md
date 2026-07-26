# UI-COMPONENT-SPEC.md

## Purpose
Defines the APEX component library, ownership of each component type, and the required behavior of common UI surfaces.

## Scope
Buttons, inputs, tables, cards, dialogs, navigation, status surfaces, diagnostics views, and trading dashboard widgets.

## Ownership
- Shared primitives live in the design-system layer.
- Feature-specific composites live in the owning feature folder.
- No component may duplicate behavior that already exists in a shared primitive without explicit justification.

## Core Component Requirements
### Buttons
- Variants: primary, secondary, destructive, ghost, icon.
- States: default, hover, focus, active, disabled, loading.

### Inputs
- Variants: text, password, select, checkbox, toggle, number, search.
- Must support validation message, helper text, and error state.

### Tables and Lists
- Must support dense data presentation, sorting, filtering, empty states, and loading state.
- Long values such as addresses or hashes should be truncatable with copy affordance.

### Cards and Panels
- Used for dashboard metrics, strategy summaries, risk summaries, and provider status.
- Panels must have a title, optional subtitle, and clearly separated body.

### Dialogs and Drawers
- Used only when a confirmation or multi-step interaction is required.
- Must trap focus and expose a safe cancel path.

### Navigation
- Must make the current section obvious.
- State changes in navigation must not destroy unsaved form state without confirmation.

## Domain-Specific Components
- strategy summary card
- risk exposure badge
- provider health indicator
- chain selector
- quote comparison table
- execution preview panel
- audit timeline
- diagnostics log viewer
- settings form groups

## State Requirements
Each component must define:
- loading state,
- empty state,
- error state,
- disabled state,
- success/confirmation state where applicable.

## Accessibility Requirements
- All controls keyboard accessible.
- All images/icons that convey meaning require accessible labels or nearby text.
- Error text must be programmatically associated with fields.

## Cross-References
- [`DESIGN-SYSTEM.md`](./DESIGN-SYSTEM.md)
- [`FEATURE-MATRIX.md`](./FEATURE-MATRIX.md)
- [`STATE-MANAGEMENT.md`](./STATE-MANAGEMENT.md)
