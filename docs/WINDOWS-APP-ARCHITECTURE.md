# Windows App Architecture

## Purpose
Defines the Windows desktop application structure, including native shell, renderer, backend, and service integration.

## Ownership
- Owns the Windows desktop process model and UI/runtime boundaries.
- Does not own trading logic, provider policy, or chain execution logic.

## Process model
- Main process owns startup, windows, tray, IPC broker, and lifecycle coordination.
- Renderer process owns presentation and user interaction.
- Backend services own trading, execution, data, and AI coordination.

## Windows integration
- Must support system tray, multi-window layouts, multi-monitor behavior, and DPI scaling.
- Must define the transport used for desktop-to-backend IPC.

## Cross-references
- `ARCHITECTURE.md`
- `WINDOWS-DESKTOP.md`
- `IPC-PROTOCOL.md`
- `WORKSPACE-MANAGER.md`
