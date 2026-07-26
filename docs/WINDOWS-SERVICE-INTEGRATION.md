# Windows Service Integration

## Document type
This document is an overview, reference, or index as noted below.

# Windows Service Integration

## Purpose
Defines how the trading backend can run under the Windows Service Control Manager.

## Ownership
- Owns service install, start, stop, recovery, and session isolation behavior.
- Does not own trading semantics or strategy state machines.

## Service contract
- Must define auto-start, delayed start, recovery actions, and stop timeout behavior.
- Must support service account permissions and boot-time startup.

## Failure handling
- Service failures must trigger restart or failover according to configured policy.
- Shutdown must flush state before SCM stop completion.

## Cross-references
- `SERVICE-LIFECYCLE.md`
- `RUNTIME-OPERATIONS.md`
- `SHUTDOWN-LIFECYCLE.md`
- `RECOVERY-AND-FAILOVER.md`
