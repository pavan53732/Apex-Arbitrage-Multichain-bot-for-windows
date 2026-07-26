# MODULE-DEPENDENCY.md

## Purpose
Defines allowed dependencies between top-level application layers and packages.

## Related Documents
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)

## Dependency Matrix
| From | May Depend On | Must Not Depend On |
|---|---|---|
| renderer features | ui-kit, ipc-contracts, shared models | Electron main internals, db, contracts |
| preload | ipc-contracts, shared models | renderer feature modules |
| main app | all non-UI packages | renderer feature modules directly |
| strategy-engine | chain-adapters, dex-adapters, risk-engine, ai-core | renderer, Electron UI |
| risk-engine | shared models, config | renderer, DEX UI, updater |
| db | config, shared models | renderer |
