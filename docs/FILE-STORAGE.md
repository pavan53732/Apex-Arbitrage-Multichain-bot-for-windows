# FILE-STORAGE.md

## Purpose
Defines all local file paths, storage classes, retention, and cleanup rules.

## Storage Classes
- database
- logs
- cache
- diagnostics bundles
- downloaded update artifacts

## Rules
- No secrets in plaintext files.
- Respect OS app-data directories.
- Support exportable diagnostics bundles with redaction.

## Cross-References
- [`DATABASE-SCHEMA.md`](./DATABASE-SCHEMA.md)
- [`CONFIGURATION.md`](./CONFIGURATION.md)
- [`ERROR-HANDLING-LOGGING.md`](./ERROR-HANDLING-LOGGING.md)
