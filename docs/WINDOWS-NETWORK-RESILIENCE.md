# Windows Network Resilience

## Purpose
Defines how the desktop app and backend survive Windows network changes and connectivity loss.

## Ownership
- Owns proxy handling, Wi-Fi/Ethernet changes, VPN changes, and reconnect policy.
- Does not own exchange-specific failover policy or trading strategy behavior.

## Resilience rules
- Must define reconnect backoff, DNS refresh, and proxy detection.
- Must document behavior during captive portals, VPN reconnects, and offline recovery.

## Cross-references
- `PROVIDER-RESILIENCE.md`
- `RUNTIME-OPERATIONS.md`
- `AI-GATEWAY.md`
- `RPC-MANAGER.md`
