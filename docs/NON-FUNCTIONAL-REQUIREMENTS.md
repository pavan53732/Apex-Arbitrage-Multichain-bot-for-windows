# NON-FUNCTIONAL-REQUIREMENTS.md

## Purpose
Defines cross-cutting system qualities required of the application beyond functional behavior.

## Scope
Security, reliability, maintainability, auditability, usability, portability, performance, recoverability.

## Requirements
- The app must fail safe by default.
- Secrets must be encrypted at rest.
- Core domain logic must be testable without Electron.
- Documentation must remain the implementation source of truth.
- User-facing safety controls must be available before enabling automation.
