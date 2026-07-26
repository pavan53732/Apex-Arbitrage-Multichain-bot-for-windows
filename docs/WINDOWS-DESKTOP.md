# Windows Desktop

## Purpose
Defines the Windows desktop shell for the trading application.

## Ownership
- Owns tray behavior, window lifecycle, DPI scaling, and multi-monitor restore rules.
- Does not own trading logic or execution policy.

## Windows behavior
- Must support minimize-to-tray and restore-from-tray behavior.
- Must define startup, login, reconnect, and notification behavior.
- Must define offline and degraded UI states.

## Cross-references
- `WINDOWS-APP-ARCHITECTURE.md`
- `UI-DASHBOARD-SPEC.md`
- `WINDOWS-NOTIFICATION-INTEGRATION.md`
- `WORKSPACE-MANAGER.md`
