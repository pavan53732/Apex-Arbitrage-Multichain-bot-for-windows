# Windows Desktop

## Purpose
Provides navigation to the authoritative documentation set.

## Cross-references
- `BUILD-RELEASE-CICD.md`
- `DEPLOYMENT.md`
- `API-REFERENCE.md`
- `DASHBOARD-LAYOUT.md`
- `DASHBOARD-WIDGETS.md`
- `UX-GUIDELINES.md`



## State Machine
- LAUNCHING -> LOADING_WORKSPACE -> READY -> SYNCING -> SHUTTING_DOWN.
- SHUTTING_DOWN -> EXIT on successful drain.


## Enterprise Contract – Windows Desktop
- Desktop lifecycle: see `docs/WINDOWS-DESKTOP.md` and `docs/SHUTDOWN-LIFECYCLE.md`.
- Startup sequencing: see `ORCHESTRATOR.md` and `HEALTHCHECKS.md`.
- UI interactions: see `UI-DASHBOARD-SPEC.md`, `INTERFACE-NOTIFICATION-CHANNEL.md`, and `INTERFACE-TOOL-CALL.md`.
- Recovery and session behavior: see `SHUTDOWN-LIFECYCLE.md` and `RUNTIME-OPERATIONS.md`.


For workspace, see `DASHBOARD-WORKSPACES.md`.

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
