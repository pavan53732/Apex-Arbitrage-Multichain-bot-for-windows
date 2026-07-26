# User Flows

## Purpose
Defines end-to-end user journeys and their required validations, failures, and recovery paths.

## Shared flow contract
Every workflow must define preconditions, user actions, system actions, validation rules, decision points, sequence order, state transitions, success paths, failure paths, recovery paths, and completion criteria.

## First launch
Initial app start must verify environment readiness, configuration state, and required permissions.

## Initial setup
The setup flow must configure AI, wallet, chain preferences, and safety policy before trading is enabled.

## AI provider onboarding
Users must be able to select a provider, test it, validate safety, and persist the setting.

## Wallet onboarding
Wallet setup must validate connection, permissions, balances, and signing capability.

## Chain onboarding
Chain onboarding must validate supported networks, RPC health, and finality policy.

## Strategy creation
Strategy creation must validate strategy type, parameters, and risk compatibility.

## Strategy configuration
Strategy configuration must validate market conditions, thresholds, and persistence.

## Backtesting
Backtesting must select a scenario set, run deterministically, and capture results.

## Paper trading
Paper trading must behave like live trading without broadcasting to production chains.

## Live trading
Live trading must require all critical safety gates and operator policy conditions.

## Monitoring
Monitoring must surface health, outcomes, alerts, and recovery actions.

## Notifications
Notifications must route actionable alerts to the operator without exposing unsafe actions.

## Emergency stop
Emergency stop must halt trading, cancel safe work, and preserve state for recovery.

## Crash recovery
Crash recovery must restore state, reconcile outstanding work, and prevent duplicate execution.

## Backup
Backup must capture the minimum state required for deterministic restore.

## Restore
Restore must validate integrity before resuming live work.

## Export and import
Export/import must preserve configuration, strategies, and workflow state according to policy.

## Updates
Updates must validate compatibility and present recovery paths if upgrade fails.

## Settings management
Settings changes must validate policy, persist, and broadcast state change only if safe.

## Cross-references
- `WINDOWS-DESKTOP.md`
- `AI-SETTINGS.md`
- `STRATEGIES.md`
- `EXECUTION-ENGINE.md`
- `RUNTIME-OPERATIONS.md`
