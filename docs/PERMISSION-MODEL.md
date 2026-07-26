# PERMISSION-MODEL.md

## Purpose
Defines the desktop security permission model, including which layer may access secrets, filesystem, network, signing, and privileged wallet operations.

## Related Documents
- [SECURITY.md](./SECURITY.md)
- [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md)
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)

## Rules
- Renderer has no direct filesystem, shell, or secret access.
- Preload exposes a minimal allowlisted API.
- Main process owns privileged operations.
