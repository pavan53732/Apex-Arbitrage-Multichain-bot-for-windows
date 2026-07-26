# User Flows

## Purpose
Defines onboarding, wallet setup, chain setup, AI setup, strategy creation, backtesting, paper trading, live trading, monitoring, alerts, emergency stop, crash recovery, backup, restore, export, import, updates, and settings flows.

## Rules
- Each user flow must map to a single owner subsystem.
- Destructive actions require confirmation.
- Recovery flows must start from persisted state, not UI cache.

## Cross-references
- `docs/WINDOWS-DESKTOP.md`
- `docs/UI-COMPONENT-SPEC.md`
- `docs/TRADING-ENGINE.md`
- `docs/STRATEGIES.md`
- `docs/WALLET-MANAGEMENT.md`
- `docs/CONFIGURATION.md`
