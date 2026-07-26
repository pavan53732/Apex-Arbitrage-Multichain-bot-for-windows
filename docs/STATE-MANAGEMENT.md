# STATE-MANAGEMENT.md

## Purpose
Defines how APEX manages runtime state across Electron main process, preload bridge, renderer UI, and local persistence.

## Scope
Store boundaries, ownership of state, synchronization rules, cache strategy, and invalidation behaviour.

## Ownership
- Main process owns authoritative operational state.
- Renderer owns presentation state and user interaction state.
- Persistence owns durable state.
- Preload owns only the minimal bridge state needed to translate typed IPC.

## State Domains
| Domain | Owner | Persistence |
|---|---|---|
| Window lifecycle | main | ephemeral |
| IPC request lifecycle | main/preload | ephemeral |
| Strategy runtime status | main | optional snapshot |
| Risk state / kill switches | main | persisted + in-memory cache |
| Quotes and route cache | main services | short-lived memory |
| UI layout and preferences | renderer + settings service | persisted |
| Form state | renderer | ephemeral |
| AI conversation/task context | main orchestrator | persisted selectively |
| Audit trail | main/db | persisted |

## Source of Truth Rules
- Main process is authoritative for trading, provider, chain, and safety state.
- Renderer may hold local copies for display, but copies must be reconciled with main responses.
- DB is the source of truth for durable history, not transient execution state.
- Cache is an acceleration layer only.

## Recommended Renderer Store Model
- Global app store for authenticated/ready state, environment, and current workspace.
- Feature-local stores for strategy dashboard, AI assistant panel, chain monitor, logs viewer.
- Query/cache layer for async reads from IPC-backed APIs.
- No direct persistence from UI except through explicit settings APIs.

## Synchronization Rules
1. Renderer action -> preload API -> typed IPC command.
2. Main process validates input.
3. Service mutates state and optionally persists.
4. Main emits event or response.
5. Renderer updates derived local stores.

## Conflict Rules
- Main process wins on all authoritative execution state.
- Renderer optimistic updates are allowed only for reversible UI settings.
- If persisted state differs from cached renderer state, renderer must reconcile to main response.

## Cache Strategy
- Quote cache TTL must be short and chain-aware.
- Static reference data may be cached longer.
- Renderer caches should be invalidated on chain change, provider change, strategy mode change, or explicit refresh.

## Persistence Rules
Persist:
- user preferences,
- config settings,
- strategy definitions,
- audit events,
- execution history,
- error summaries,
- AI task artifacts when marked durable.

Do not persist:
- transient loading flags,
- derived chart series that can be recomputed,
- raw secrets in renderer-accessible storage,
- stale quotes beyond TTL.

## Event Sources
- IPC responses
- IPC push events/subscriptions
- scheduled polling tasks
- app lifecycle hooks
- updater events
- chain connectivity events

## Cross-References
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
- [`DATA-FLOW.md`](./DATA-FLOW.md)
- [`EVENT-FLOW.md`](./EVENT-FLOW.md)
- [`DATABASE-SCHEMA.md`](./DATABASE-SCHEMA.md)


For workspace, see `DASHBOARD-WORKSPACES.md`.

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
