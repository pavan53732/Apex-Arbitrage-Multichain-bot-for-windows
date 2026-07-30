---
type: CONTRACT
owner: Windows Team
status: Canonical
version: 1.0.0
purpose: Defines how the app uses Windows toasts, tray notifications, and Action Center behavior — severity mapping, click actions, delivery on restart, offline recovery, notification preferences, and cross-subsystem integration.
scope: None
last_updated: 2026-07-29
canonical_source: docs/windows/WINDOWS-NOTIFICATION-INTEGRATION.md
---

# Windows Notification Integration

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Windows Team

## Purpose
Defines how the app uses Windows toasts, tray notifications, and Action Center behavior — severity mapping, click actions, delivery on restart, offline recovery, notification preferences, and cross-subsystem integration.

---

## 1. Notification Channels

| Channel | Type | Duration | User Action | Priority | Windows API |
|---------|------|----------|-------------|----------|-------------|
| **Toast** | Action Center toast | 5-25s (based on severity) | Click → opens dashboard to relevant page | Critical, High | `ToastNotification` API |
| **Tray balloon** | System tray popup | 3s auto-dismiss | Click → opens dashboard | Medium | `Shell_NotifyIcon` NIF_INFO |
| **Sound alert** | Audio beep | 1s | None (alert only) | Critical | `PlaySound` API |
| **Overlay banner** | In-dashboard overlay | Persistent until dismissed | Click → resolve/dismiss | High, Critical | Dashboard overlay system |
| **Email** | Email to operator | Persistent | Link → opens dashboard | Critical only | SMTP (configurable) |

---

## 2. Severity Mapping

| Platform Severity | Windows Toast Type | Sound | Duration | Icon | Click Action |
|-------------------|-------------------|-------|----------|------|-------------|
| **Critical** | Urgent toast (persistent in Action Center) | Critical alert sound | Until dismissed | Red exclamation | Opens dashboard to Critical page |
| **High** | Important toast | Warning sound | 25s auto-dismiss | Yellow warning | Opens dashboard to relevant page |
| **Medium** | Standard toast | Notification sound | 10s auto-dismiss | Blue info | Opens dashboard to relevant page |
| **Low** | Tray balloon only | No sound | 3s auto-dismiss | Grey info | Opens dashboard |

### Critical Notification Examples
| Event | Toast Title | Body | Click Target |
|-------|------------|------|-------------|
| Private key leak | ⚠️ Security Alert | "Possible private key exposure detected" | `/admin` page → Security tab |
| Unauthorized wallet access | ⚠️ Security Alert | "Unauthorized wallet access attempt" | `/admin` page → Security tab |
| All AI providers failed | 🚨 AI Failure | "All AI providers unavailable" | `/admin` page → AI status |
| Service crash | 🚨 System Crash | "Backend service crashed — restarting" | `/admin` page → Recovery |
| Network critical offline | 🔴 No Network | "No network connectivity for 5+ minutes" | `/admin` page → Network |

### High Notification Examples
| Event | Toast Title | Body | Click Target |
|-------|------------|------|-------------|
| Trade completed | 💰 Trade Completed | "Profit: $X.XX" | `/trading` page |
| Trade aborted | ❌ Trade Aborted | "Reason: [reason]" | `/trading` page |
| Circuit breaker tripped | ⚡ Circuit Breaker | "[type] breaker activated" | `/trading` page → Risk tab |
| AI provider failed | ⚠️ AI Provider Issue | "[provider] unavailable — using fallback" | `/admin` page → AI status |

---

## 3. Notification Delivery Rules

### 3.1 Rate Limiting

| Rule | Implementation |
|------|---------------|
| **Max toasts per minute** | 3 (excess queued and shown sequentially) |
| **Max tray balloons per minute** | 5 |
| **Critical bypass** | Critical notifications bypass rate limit |
| **Same-event suppression** | If same event type shown in last 60s → suppress (update existing toast) |
| **Aggregate notification** | Multiple similar events → show aggregate ("3 trades completed") |

### 3.2 Delivery on Restart

```
1. On app restart, load undelivered notifications from persistent store.
2. Notifications stored in notification queue (SQLite table `notification_queue`).
3. On restart, show all undelivered Critical notifications immediately.
4. Show High notifications within first 30s (rate-limited).
5. Medium/Low notifications shown during next poll cycle or discarded.
6. Notification store is purged after delivery or after 24h (configurable).
```

### 3.3 Delivery While Offline

- Notifications generated while offline are stored in notification queue.
- On reconnect, stored notifications are delivered per §3.2 rules.
- If notification is > 24h old at delivery time → discard (too stale).

---

## 4. Notification Preferences

| Preference | Default | Config Key | Scope |
|-----------|---------|-----------|-------|
| **Enable toast notifications** | `true` | `notification.toast.enabled` | Global |
| **Enable tray balloons** | `true` | `notification.tray.enabled` | Global |
| **Enable sound alerts** | `true` (Critical only) | `notification.sound.enabled` | Global |
| **Enable email alerts** | `false` | `notification.email.enabled` | Critical only |
| **Email address** | `""` | `notification.email.address` | Operator only |
| **Suppress Medium/Low while active** | `false` | `notification.suppress_non_critical_while_trading` | Global |
| **Quiet hours** | `22:00-08:00` | `notification.quiet_hours.start/end` | Global (no sounds) |
| **Per-event preferences** | Override per event type | `notification.events.<type>.enabled` | Per event |

---

## 5. Cross-Subsystem Integration

| Caller | Purpose | Contract |
|--------|---------|----------|
| Trading Engine | Trade completion/abort notification | `trade.completed` / `trade.aborted` events |
| Risk Engine | Circuit breaker notification | `risk.circuit_breaker.tripped` event |
| Security Manager | Security violation notification | `security.violation` event |
| AI Pipeline | AI provider failure notification | `ai.provider.failed` event |
| Health Checker | Health issue notification | `health.check.failed` event |
| Recovery Coordination | Recovery result notification | `system.recovery.completed` event |
| Windows App Architecture | Sleep/resume notification | `system.power.resume` event |

| Config Key | Default | Description |
|-----------|---------|-------------|
| `notification.toast.enabled` | `true` | Toast notifications |
| `notification.tray.enabled` | `true` | Tray balloon notifications |
| `notification.sound.enabled` | `true` | Sound alerts (Critical only) |
| `notification.email.enabled` | `false` | Email alerts |
| `notification.max_toasts_per_minute` | `3` | Toast rate limit |
| `notification.quiet_hours.start` | `22:00` | Quiet hours start |
| `notification.quiet_hours.end` | `08:00` | Quiet hours end |

---

## Cross-References

- **NOTIFICATION-CENTER.md** — Platform notification center (business logic).
- **MONITORING-OBSERVABILITY.md** — Alert thresholds and notification triggers.
- **EVENT-OWNERSHIP-MATRIX.md** — Notification event ownership.
- **INTERFACE-NOTIFICATION-CHANNEL.md** — Notification channel interface.
- **PERMISSION-MODEL.md** — Notification permission per role.
- **WINDOWS-APP-ARCHITECTURE.md** — Tray notification behavior.
- **CONFIGURATION-REFERENCE.md** — Notification config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade Windows notification contract: 5 notification channels, severity mapping (4 levels with sound/duration/icon/action), notification inventory (5 critical + 4 high examples), rate limiting rules, delivery on restart, delivery while offline, notification preferences (8 settings), cross-subsystem integration | Windows Team |
| 0.1.0 | 2026-07-27 | Initial stub | Windows Team |
