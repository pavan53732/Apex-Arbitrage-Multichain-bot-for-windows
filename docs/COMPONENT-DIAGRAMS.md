# COMPONENT-DIAGRAMS.md

## Purpose
Provides structural diagrams of major runtime components and their boundaries.

## Scope
This file owns diagram-oriented representations and should not duplicate long prose owned elsewhere.

## Desktop Runtime
```text
Renderer UI -> Preload API -> IPC Contracts -> Main Process Services -> Packages (AI, Risk, Strategy, DB, Adapters)
```
