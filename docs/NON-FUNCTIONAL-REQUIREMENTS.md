# NON-FUNCTIONAL-REQUIREMENTS.md

## Purpose
Defines system-wide non-functional constraints and quality attributes.

## Categories
- security
- reliability
- performance
- maintainability
- observability
- usability
- testability

## Core Requirements
- all privileged operations mediated by main process,
- typed validation on all external boundaries,
- docs remain single source of truth,
- critical workflows auditable,
- UI remains functional in degraded-but-safe modes.

## Cross-References
- [`SECURITY.md`](./SECURITY.md)
- [`PERFORMANCE-TARGETS.md`](./PERFORMANCE-TARGETS.md)
- [`TESTING-GUIDE.md`](./TESTING-GUIDE.md)
