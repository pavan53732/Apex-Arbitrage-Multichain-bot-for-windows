# DATA-FLOW.md

## Purpose
Describes how data moves through APEX from input sources to execution, persistence, and UI presentation.

## Primary Flows
1. Config load -> service bootstrap -> readiness state.
2. Chain/RPC + DEX quote -> strategy evaluation -> risk evaluation -> execution proposal.
3. User UI action -> preload -> IPC -> service -> DB/audit -> UI response.
4. AI request -> provider adapter -> schema validation -> task result -> persistence/UI.

## Canonical Trading Flow
```text
RPC/DEX data -> normalized market snapshot -> strategy engine -> candidate trade
-> risk engine -> approved proposal -> signer/executor -> result -> audit DB -> renderer
```

## Cross-References
- [`EVENT-FLOW.md`](./EVENT-FLOW.md)
- [`STATE-MANAGEMENT.md`](./STATE-MANAGEMENT.md)
- [`RISK-ENGINE.md`](./RISK-ENGINE.md)
