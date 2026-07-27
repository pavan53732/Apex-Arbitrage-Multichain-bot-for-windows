# Windows Network Resilience

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Windows Team

## Purpose
Defines how the desktop app and backend survive Windows network changes — proxy handling, Wi-Fi/Ethernet changes, VPN reconnects, DNS refresh, captive portals, reconnect backoff, offline recovery, and cross-subsystem integration.

---

## 1. Network Change Detection

| Event | Detection Method | Action |
|-------|-----------------|--------|
| **Wi-Fi disconnect** | Windows `WM_WLAN_NOTIFICATION` / NetworkStatus API | Start reconnect backoff |
| **Ethernet disconnect** | Windows `WM_NETWORK_CHANGE` / `NotifyAddrChange` | Start reconnect backoff |
| **VPN disconnect** | Network interface change notification | Pause trading, start reconnect |
| **VPN reconnect** | VPN interface re-detected | Resume trading, verify RPC access |
| **IP address change** | `NotifyUnicastIpAddressChange` | Flush DNS, reconnect RPC |
| **DNS server change** | `NotifyIpInterfaceChange` | Re-resolve all RPC endpoints |
| **Network profile change** | Windows `NetworkProfile` API | Re-evaluate proxy, firewall rules |
| **Captive portal** | HTTP probe to known endpoint → redirect detected | Show notification, block trading |

---

## 2. Reconnect Backoff Algorithm

```
1. Network disconnect detected.
2. Immediate reconnect attempt (no backoff).
3. If immediate fails → enter exponential backoff:
   backoff_ms = base_backoff × 2^(attempt_count) × jitter
   base_backoff: windows.network.reconnect_base_ms (default 1000ms)
   max_backoff: windows.network.reconnect_max_ms (default 30000ms)
   jitter: random ±10%

4. Backoff schedule:
   Attempt 1: 1000ms
   Attempt 2: 2000ms
   Attempt 3: 4000ms
   Attempt 4: 8000ms
   Attempt 5: 16000ms
   Attempt 6: 30000ms (max)
   Attempt 7+: 30000ms every 30s

5. Network reconnect detected → cancel backoff → immediate reconnect.
6. After 10 consecutive failures → emit network.critical.offline event.
```

---

## 3. Proxy Handling

### 3.1 Proxy Detection

| Method | Order | Source | Config Key |
|--------|-------|--------|------------|
| **Manual config** | 1st | `network.proxy.url` | `network.proxy.url` |
| **Windows system proxy** | 2nd | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` | `network.proxy.use_system: true` |
| **Environment variables** | 3rd | `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` | `network.proxy.use_env: true` |
| **PAC file** | 4th | Windows WinHTTP AutoProxy | `network.proxy.use_pac: true` |
| **No proxy** | 5th | Direct connection | — |

### 3.2 Proxy Configuration

| Proxy Type | Support | Auth | Protocol |
|-----------|---------|------|----------|
| **HTTP proxy** | Yes | Basic, NTLM, Kerberos | HTTP/HTTPS |
| **HTTPS proxy** | Yes | Basic, NTLM, Kerberos | HTTPS |
| **SOCKS5 proxy** | Yes | None or username/password | TCP |
| **PAC file** | Yes (auto-detect) | Per PAC rules | Varies |
| **No proxy (direct)** | Yes | — | TCP |

### 3.3 Proxy Exclusions

| Exclusion | Description |
|-----------|-------------|
| `localhost` | Local IPC (never proxied) |
| `127.0.0.1` | Local IPC (never proxied) |
| `*.local` | Local network (never proxied) |
| `NO_PROXY` env var | Custom exclusion list |
| `network.proxy.excluded_domains` | Config exclusion list |

---

## 4. DNS Handling

### 4.1 DNS Resolution Strategy

| Strategy | Order | Fallback | Config Key |
|----------|-------|----------|------------|
| **System DNS** | 1st | — | Default |
| **Custom DNS** | 2nd | System DNS | `network.dns.servers` |
| **DNS-over-HTTPS** | 3rd | Custom DNS | `network.dns.doh_enabled: false` |

### 4.2 DNS Refresh Rules

| Trigger | Action |
|---------|--------|
| **IP change** | Flush DNS cache, re-resolve all RPC endpoints |
| **DNS server change** | Flush DNS cache, re-resolve |
| **RPC endpoint failure** | Re-resolve before retry |
| **VPN connect** | Flush DNS, re-resolve (VPN may change DNS) |
| **Scheduled** | Every `network.dns.refresh_interval_ms` (default 3600000ms = 1h) |

---

## 5. Captive Portal Handling

```
1. On network change, probe http://connectivitycheck.gstatic.com/generate_204.
2. Expected: HTTP 204 No Content.
3. If redirect (3xx) detected → captive portal suspected.
4. Show notification: "Network restricted — trading paused."
5. Trading engine enters Paused mode.
6. Continue probing every 30s.
7. If 204 received → captive portal cleared → resume trading.
8. If captive portal persists > 5 min → emit network.captive_portal event.
```

---

## 6. Offline Recovery

```
1. Network offline → trading paused.
2. Dashboard shows "Offline" banner + cached data.
3. RPC connections closed.
4. Reconnect attempts per backoff algorithm (§2).
5. On reconnect:
   a. Flush DNS, re-resolve endpoints.
   b. Re-establish RPC connections (each chain).
   c. Re-subscribe to WebSocket feeds.
   d. Re-open event bus subscriptions.
   e. Resume trading engine (if operator hasn't halted).
   f. Run recovery scan (incomplete trades that may have settled while offline).
6. On permanent offline (> 5 min with all attempts failed):
   a. Emit network.critical.offline event.
   b. Dashboard shows "No network" overlay.
   c. Trading remains paused.
```

---

## 7. Cross-Subsystem Integration

| Caller | Purpose | Contract |
|--------|---------|----------|
| RPC Manager | RPC endpoint reconnection | `network.reconnect.rpc` API |
| AI Gateway | AI provider reconnection | `network.reconnect.ai` API |
| Trading Engine | Pause/resume on network change | `system.mode.transition` event |
| Dashboard | Show network status | `dashboard.network` IPC channel |
| Provider Resilience | Provider endpoint reconnection | `network.reconnect.provider` API |
| Windows App Architecture | Power event → network reconnect | `system.power.resume` event |

| Config Key | Default | Description |
|-----------|---------|-------------|
| `network.proxy.url` | `""` | Manual proxy URL |
| `network.proxy.use_system` | `true` | Use Windows system proxy |
| `network.proxy.use_env` | `true` | Use HTTP_PROXY/HTTPS_PROXY env vars |
| `network.dns.refresh_interval_ms` | `3600000` | DNS refresh interval |
| `network.dns.doh_enabled` | `false` | DNS-over-HTTPS |
| `windows.network.reconnect_base_ms` | `1000` | Reconnect backoff base |
| `windows.network.reconnect_max_ms` | `30000` | Reconnect backoff max |

---

## Cross-References

- **PROVIDER-RESILIENCE.md** — Provider failover and resilience.
- **RPC-MANAGER.md** — RPC endpoint management and failover.
- **AI-GATEWAY.md** — AI provider network handling.
- **RUNTIME-OPERATIONS.md** — Runtime network operations.
- **WINDOWS-APP-ARCHITECTURE.md** — Power event network recovery.
- **TRADING-ENGINE.md** — Trading pause/resume on network change.
- **CONFIGURATION-REFERENCE.md** — Network config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade network resilience: 8 network change detections, reconnect backoff algorithm, proxy handling (5 methods + 5 types + exclusions), DNS handling (3 strategies + 5 refresh triggers), captive portal handling, offline recovery sequence, cross-subsystem integration | Windows Team |
| 0.1.0 | 2026-07-27 | Initial stub | Windows Team |
