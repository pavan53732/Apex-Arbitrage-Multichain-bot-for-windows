# Bootstrap Sequence

## Purpose
Authoritative owner for bootstrap sequence.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `APEX-OS.md`
- `ARCHITECTURE.md`

## Operational Contract
Defines deterministic startup order across kernel, registries, config, database, workers, providers, AI, chains, and dashboard readiness.

## Example
Kernel starts before workers and providers before the dashboard becomes interactive.

## Bootstrap steps
- Must define ordered startup steps, service registration, and UAC handling.
