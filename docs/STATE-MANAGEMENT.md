# STATE-MANAGEMENT.md

## Purpose
Defines how state is created, owned, synchronized, cached, and invalidated across Electron main, preload, renderer, and shared packages.

## Scope
Covers renderer stores, server-like local state, IPC-driven updates, cache policy, optimistic updates, persistence boundaries, and synchronization rules.

## Related Documents
- [DATA-FLOW.md](./DATA-FLOW.md)
- [EVENT-FLOW.md](./EVENT-FLOW.md)
- [IPC-PROTOCOL.md](./IPC-PROTOCOL.md)
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)

## State Ownership Model
- Main process owns privileged runtime state: wallets, active sessions, background jobs, chain connections, strategy execution state.
- Renderer owns presentation state: routing, panel visibility, selected filters, table sort, transient forms.
- Shared packages own domain models and serializers, not mutable global state.

## Recommended Store Boundaries
- `appStore`: app status, version, window info, update state.
- `settingsStore`: non-secret preferences and effective config snapshots.
- `portfolioStore`: balances, positions, PnL, exposure summaries.
- `strategyStore`: strategy enablement, run state, opportunities, execution queue.
- `logStore`: live log stream, filters, diagnostics.
- `uiStore`: dialogs, toasts, layout state.

## Synchronization Rules
- Renderer never mutates privileged state directly.
- All privileged mutations occur through validated IPC commands.
- Main process emits normalized events after state changes.
- Renderer stores subscribe to IPC events and reconcile using entity IDs and timestamps.

## Cache Strategy
- Chain balances and quotes are short-lived caches.
- Static metadata may be cached longer.
- Failed fetches must not poison cache permanently.
- Cache TTLs must be explicit in implementation and documented per domain.

## Persistence Rules
- UI state may persist locally when non-sensitive.
- Secrets, wallet material, and decrypted credentials must never enter renderer persistence.
- Strategy runtime state should be reconstructible from main-process sources.

## AI Agent Guidance
- Prefer unidirectional data flow.
- Avoid hidden mutable singletons inside renderer features.
- State transitions should be observable and testable.
