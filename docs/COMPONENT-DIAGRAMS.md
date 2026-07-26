# COMPONENT-DIAGRAMS.md

## Purpose
Textual component diagrams for AI agents and human maintainers.

## System Diagram
```text
Renderer UI <-> Preload Bridge <-> Main Process <-> Domain Services
                                       |-> DB
                                       |-> AI Providers
                                       |-> Chain Clients
                                       |-> DEX Clients
                                       |-> Risk Engine
                                       |-> Strategy Engine
```

## Cross-References
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- [`MODULE-DEPENDENCY.md`](./MODULE-DEPENDENCY.md)
