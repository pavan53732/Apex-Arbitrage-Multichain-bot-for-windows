# PERMISSION-MODEL.md

## Purpose
Defines runtime permissions and capability boundaries in APEX.

## Rules
- Renderer has no direct filesystem, shell, network secret, or wallet permission.
- Preload exposes least-privilege methods only.
- Main process mediates all privileged operations.
- Live trading capability is feature-flagged and policy-gated.

## Cross-References
- [`SECURITY.md`](./SECURITY.md)
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
