# MODULE-DEPENDENCY.md

## Purpose
Defines allowed and forbidden dependencies between repository packages and runtime layers.

## Dependency Matrix
| From | May Depend On |
|---|---|
| renderer | preload API, shared-types, ipc-contracts |
| preload | ipc-contracts, shared-types |
| main | core, config, db, ai-orchestrator, risk-engine, strategy-engine, chain-clients, dex-clients, logging |
| strategy-engine | core, shared-types, config, logging, chain-clients, dex-clients, risk-engine interfaces |
| db | shared-types, logging, config |
| shared-types | none or schema utilities only |

## Forbidden Dependencies
- renderer -> db
- renderer -> chain/dex adapters
- shared-types -> Electron
- strategies -> renderer
- logging -> feature modules

## Cross-References
- [`PROJECT-STRUCTURE.md`](./PROJECT-STRUCTURE.md)
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)
