# Runtime Operations

## Purpose
Defines how the backend runs, recovers, and stays observable in production.

## Ownership
- Owns runtime lifecycle, queues, workers, health, recovery, and deployment behavior.
- Does not own trading strategy logic or market selection.

## Windows concerns
- Must define service mode, tray mode, proxy handling, and firewall-aware connectivity.
- Must define startup and shutdown behavior under Windows sessions.

## Cross-references
- `SERVICE-LIFECYCLE.md`
- `SHUTDOWN-LIFECYCLE.md`
- `HEALTHCHECKS.md`
- `MONITORING-OBSERVABILITY.md`

## Required details
- Define service, tray, proxy, recovery, and monitoring behavior.

## Runtime modes
- Support service mode and tray mode on Windows.
- Define startup checks, drain behavior, and recovery actions.
- Define proxy, firewall, and restart handling.
