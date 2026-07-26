# Registry System

## Document type
This document is an overview, reference, or index as noted below.

# Registry System

## Purpose
Unifies chain, DEX, token, and oracle registries under one contract.

## Interface
All registries implement `IRegistry` with List(), Get(id), Refresh(), and Watch(change_callback).

## Versioning
Every entry has `schema_version`. Updates must be backward-compatible for 2 versions.

## Validation
- Token addresses must be checksummed.
- Chain IDs must be greater than 0.
- Oracle feeds must have a heartbeat config.

## Governance
Registry updates follow `CONTRACT-MANAGEMENT.md` policies. New entries require manual approval unless auto-import is configured.

## Configuration
- AUTO_REFRESH_INTERVAL.
- VALIDATION_STRICTNESS.
- APPROVAL_REQUIRED_FOR_NEW.

## Cross-references
- `DOMAIN-MODEL.md`
- `CONTRACT-MANAGEMENT.md`
- `MARKET-DATA.md`

## Governance Rules
Defines the unified registry interface, schema versioning, validation, and manual approval semantics.

## Example
A token registry entry is rejected until checksum and version checks pass.
