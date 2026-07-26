# Interface: Notification Channel

## Purpose
Defines outbound notification channel contracts.

## Methods
- Send(severity, title, body, metadata).
- Acknowledge(id).

## Validation
- `severity`, `title`, `body`, and `metadata` are required.
- `id` is required for acknowledgements.
- `metadata` must include channel, source, and timestamp.

## Cross-references
- `NOTIFICATION-CENTER.md`
- `RUNTIME-OPERATIONS.md`
