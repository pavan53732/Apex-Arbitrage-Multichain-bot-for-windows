# Permission Model

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Security Team

## Purpose
Defines the complete role/action permission matrix — roles, actions, scopes, enforcement points, Windows-specific permissions (UAC, service accounts, scheduled tasks), and integration with trust boundaries and security contracts.

---

## 1. Role Definitions

| Role | ID | Scope | Description | Max Concurrent Sessions |
|------|----|-------|-------------|------------------------|
| **Operator** | `role.operator` | Full system | Full administrative access; configure, deploy, manage wallets, override trades, manage secrets | 2 |
| **Trader** | `role.trader` | Trading only | View markets, create/edit strategies, view positions, submit trades (within risk limits) | 5 |
| **Viewer** | `role.viewer` | Read-only | View dashboard, view trades, view logs, view positions — no mutation actions | 10 |
| **Plugin** | `role.plugin` | Sandboxed | Declared capabilities only (e.g., `core.trade.signal`, `core.ohlc.data`) — no direct system access | Per plugin |
| **Service** | `role.service` | Background service | Automated trading operations; no dashboard access; follows configured policies | 1 |

---

## 2. Role/Action Permission Matrix

### 2.1 System-Level Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| Configure system settings | ✓ | — | — | — | — |
| Manage feature flags | ✓ | — | — | — | — |
| Restart/shutdown service | ✓ | — | — | — | — (auto per policy) |
| Switch runtime mode (Active/Paused/Safe) | ✓ | — | — | — | — (auto per health) |
| View system health | ✓ | ✓ | ✓ | — | ✓ (internal) |
| Export diagnostics | ✓ | — | — | — | — |
| Manage users/roles | ✓ | — | — | — | — |

### 2.2 Trading Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| View market data | ✓ | ✓ | ✓ | ✓ (within capability) | ✓ (internal) |
| Create/edit strategy | ✓ | ✓ | — | — | — |
| Override trade decision | ✓ | — | — | — | — |
| Submit trade (within risk limits) | ✓ | ✓ | — | ✓ (signal only) | ✓ (auto per strategy) |
| Cancel in-flight trade | ✓ | — | — | — | — (auto per timeout) |
| View trade history | ✓ | ✓ | ✓ | — | ✓ (internal) |
| View positions | ✓ | ✓ | ✓ | — | ✓ (internal) |
| View P&L | ✓ | ✓ | ✓ | — | ✓ (internal) |

### 2.3 Wallet Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| Add/remove wallet | ✓ | — | — | — | — |
| View wallet balance (anonymized) | ✓ | ✓ (anonymized) | ✓ (anonymized) | — | ✓ (internal, raw) |
| View wallet addresses | ✓ | ✓ | — | — | — |
| Initiate transfer | ✓ | — | — | — | — |
| View transaction history | ✓ | ✓ | ✓ (anonymized) | — | ✓ (internal) |

### 2.4 Security Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| Manage secrets (add, rotate, delete) | ✓ | — | — | — | — |
| View security violations | ✓ | — | — | — | ✓ (internal) |
| Approve/deny trust boundary overrides | ✓ | — | — | — | — |
| View audit log | ✓ | ✓ (subset) | — | — | — |
| Initiate incident response | ✓ | — | — | — | — |

### 2.5 AI Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| Configure AI providers | ✓ | — | — | — | — |
| View AI recommendations | ✓ | ✓ | ✓ | — | ✓ (internal) |
| Override AI decision | ✓ | — | — | — | — |
| View AI cost metrics | ✓ | ✓ | ✓ | — | ✓ (internal) |
| Reset AI memory | ✓ | — | — | — | — |

### 2.6 Plugin Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| Install/uninstall plugin | ✓ | — | — | — | — |
| Enable/disable plugin | ✓ | — | — | — | — |
| Configure plugin settings | ✓ | ✓ (for owned plugins) | — | — | — |
| View plugin marketplace | ✓ | ✓ | ✓ | — | — |
| View plugin status | ✓ | ✓ | ✓ | — | ✓ (internal) |
| Grant plugin capability escalation | ✓ | — | — | — | — |

### 2.7 Dashboard Actions

| Action | Operator | Trader | Viewer | Plugin | Service |
|--------|----------|--------|--------|--------|---------|
| Modify dashboard layout | ✓ | ✓ | — | — | — |
| Switch workspace | ✓ | ✓ | ✓ (view only) | — | — |
| Create/edit workspace | ✓ | ✓ | — | — | — |
| Export dashboard data | ✓ | ✓ | ✓ (limited) | — | — |

---

## 3. Enforcement Points

| Enforcement Layer | Mechanism | Checks |
|-------------------|-----------|--------|
| **IPC preload bridge** | Role-based call filtering per IPC message type | Every IPC call from UI → backend validates role before processing |
| **API gateway** | Role + scope validation on API request headers | Reject unauthorized requests before they reach backend logic |
| **Dashboard UI** | Action visibility based on user role | Hide action buttons/menu items user cannot perform |
| **Plugin sandbox** | Capability grant filtering | Block IPC calls from plugin beyond declared capabilities |
| **Trading engine** | Role check before trade submission | Trader role required for manual trades; Operator for overrides |
| **Security gateway** | Trust boundary + role check | Cross-domain access requires Operator role + explicit authorization |
| **Service mode** | Automated operations follow configured policies | No role needed (internal automation); policies define limits |

---

## 4. Windows-Specific Permissions

### 4.1 User Account Types

| Account Type | UAC Level | Access Scope | Example |
|-------------|-----------|-------------|---------|
| **Standard user** | Standard | Dashboard + trading (Trader role) | Regular trader using the app |
| **Administrator** | Elevated (UAC prompt) | Full system (Operator role) | IT admin managing wallets and secrets |
| **Service account** | SYSTEM | Background operations (Service role) | Windows service running trading engine |
| **Limited user** | Standard (restricted) | Dashboard viewing only (Viewer role) | Audit viewer |

### 4.2 UAC Elevation Boundaries

| Action | Requires UAC Elevation? | Reason |
|--------|------------------------|--------|
| Install/uninstall service | Yes | Modifies Windows SCM registry |
| Add/remove Windows firewall rules | Yes | Modifies system security settings |
| Register/unregister Windows Defender exclusion | Yes | Modifies system security |
| Access OS credential manager for secret storage | Yes (first time) | Access to system-level credential store |
| Modify config files in program directory | Yes | Write to protected directory |
| Modify config in user app data directory | No | User-level config is permitted |
| Start/stop Windows service | Yes | Service control requires admin |
| View dashboard and trade (normal operation) | No | Normal user-level operation |

### 4.3 Scheduled Task Permissions

| Task | Scheduler | Account | Permission |
|------|-----------|---------|------------|
| Auto-start service on boot | Windows Task Scheduler | SYSTEM | Service-only access |
| Periodic config reload | App internal scheduler | Service account | Read config only |
| Periodic health checks | App internal scheduler | Service account | Read-only probes |
| Secret rotation reminder | App internal scheduler | Service account | Notification only; actual rotation requires Operator |
| Auto-update check | App internal scheduler | Service account | Check only; install requires Operator approval |

---

## 5. Session Management

| Aspect | Rule |
|--------|------|
| Session token format | JWT with role, scope, expiry, and session ID |
| Session expiry | 30 min (configurable: `security.session.timeout_ms`) |
| Session renewal | Automatic renewal on activity; explicit re-auth on expiry |
| Concurrent session limit | Per role (see §1) |
| Session invalidation | On role change, secret rotation, or operator command |
| Plugin sessions | No JWT; capability grants via manifest (see PLUGIN-SDK.md) |
| Service sessions | No JWT; internal automation with configured policies |

---

## Cross-References

- **SECURITY.md** — Overall security architecture.
- **SECURITY-CONTRACTS.md** — Security contracts and policies.
- **TRUST-BOUNDARIES.md** — Trust domain enforcement matrix.
- **PLUGIN-SANDBOX-CONTRACT.md** — Plugin capability grants.
- **AI-SAFETY-BOUNDARY.md** — AI role-based safety boundaries.
- **IPC-PROTOCOL.md** — IPC message authentication.
- **WINDOWS-SERVICE-INTEGRATION.md** — Windows service permissions.
- **TRACEABILITY-MATRIX.md** — REQ-SECURITY-002.
- **CONFIGURATION-REFERENCE.md** — `security.*` config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Full 7-category role/action matrix, 7 enforcement points, Windows UAC/service permissions, session management | Security Team |
| 1.0.0 | 2025-01-15 | Initial stub (9 lines) | Security Team |
