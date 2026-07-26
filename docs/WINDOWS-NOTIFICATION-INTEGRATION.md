# Windows Notification Integration

## Document type
This document is an overview, reference, or index as noted below.

# Windows Notification Integration

## Purpose
Defines how the app uses Windows toasts, tray notifications, and Action Center behavior.

## Ownership
- Owns Windows notification delivery, persistence, and user preference handling.
- Does not own business alert logic, which belongs to monitoring and trading owners.

## Notification contract
- Must define toast titles, body text, severity mapping, and click actions.
- Must define delivery behavior on restart and offline recovery.

## Cross-references
- `NOTIFICATION-CENTER.md`
- `MONITORING-OBSERVABILITY.md`
- `UI-DASHBOARD-SPEC.md`
- `INTERFACE-NOTIFICATION-CHANNEL.md`
