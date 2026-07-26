# Security Contracts

## Purpose
Defines mandatory security controls for the platform.

## Secret storage
Secrets must use the OS keychain and must never be stored in `.env` files.

## Wallet signing
Wallet signing must require explicit user approval via the desktop UI; headless auto-sign is forbidden.

## Plugin sandbox
Plugins must run in a separate process with CPU and RAM limits.

## Emergency stop
`/admin/emergency-stop` terminates all active orders and locks wallets.

## Audit log
Every state transition must log user ID, timestamp, and immutable hash.

## Cross-references
- `PLUGIN-SDK.md`
- `WALLET-COMMAND-CENTER.md`
- `ORCHESTRATOR.md`
- `HEALTHCHECKS.md`

## Governance Rules
Defines security invariants for wallets, plugins, secrets, approvals, permissions, and emergency controls.

## Example
A wallet action requires explicit permission and audit logging.

## Required details
- Define secret storage, signing, audit logs, and escalation rules.
