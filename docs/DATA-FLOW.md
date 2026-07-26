# DATA-FLOW.md

## Purpose
Defines the authoritative data movement paths between user actions, AI analysis, chain data, strategy evaluation, risk approval, execution, persistence, and UI updates.

## Related Documents
- [EVENT-FLOW.md](./EVENT-FLOW.md)
- [STATE-MANAGEMENT.md](./STATE-MANAGEMENT.md)
- [IPC-PROTOCOL.md](./IPC-PROTOCOL.md)

## Primary Flows
1. User changes settings in renderer.
2. Renderer submits validated IPC command.
3. Main process updates config service.
4. Main emits settings-updated event.
5. Renderer store reconciles and re-renders.

6. Strategy scheduler requests quotes and balances.
7. Adapters normalize raw chain/DEX responses.
8. Strategy engine produces opportunities.
9. Risk engine accepts or rejects opportunities.
10. Approved trade plans flow into execution service.
11. Results are persisted and broadcast to renderer.
