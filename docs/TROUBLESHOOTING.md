# APEX Troubleshooting Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026

---

## 1. How to Use This Guide

Symptoms are listed first, grouped by area. Each has:
- **Likely cause**
- **Quick check**
- **Fix**

If your issue isn't here, see §13 for how to get more help (logs, diagnostics, filing an issue).

---

## 2. Installation & Launch

### Symptom: Installer won't run / blocked by SmartScreen
**Likely cause:** APEX is not yet code-signed.
**Fix:** Click "More info" → "Run anyway". This is expected until v3.1 adds code signing (see `SECURITY.md`).

### Symptom: "This app can't run on your PC"
**Likely cause:** Wrong architecture (you have ARM, installer is x64).
**Fix:** APEX is x64 only. ARM64 support is on the roadmap.

### Symptom: Installer fails halfway
**Likely cause:** Disk full, AV interference, or perms.
**Fix:**
1. Free 500MB+ on target drive
2. Temporarily disable AV
3. Run installer again
4. If still fails, see `%TEMP%\apex-installer.log`

### Symptom: App crashes immediately on launch
**Check the log:** `%APPDATA%\APEX\logs\crash-*.log`
**Common causes:**
- Corrupted SQLite DB → rename `%APPDATA%\APEX\apex.db` to `apex.db.bak`; restart (loses local data)
- Encrypted key corrupted → Settings → Reset All
- Missing native module → reinstall via the installer (it does `electron-rebuild`)

---

## 3. AI Configuration

### Symptom: "Test connection failed" with HTTP 401
**Likely cause:** Invalid API key.
**Fix:**
- Re-paste the key carefully
- Confirm the key is for the correct service (OpenAI key vs Anthropic key vs other)
- Check for trailing spaces in the field

### Symptom: "Test connection failed" with HTTP 403
**Likely cause:** Key doesn't have permission for the model/endpoint.
**Fix:** Check your account's model access (e.g. some accounts need o1 model access granted manually).

### Symptom: "Test connection failed" with HTTP 429
**Likely cause:** Rate limit hit (you may have a free tier).
**Fix:** Wait 60s, retry, or raise RPM/TPM in AI Settings (won't help; the issue is the provider side). Consider paid tier.

### Symptom: "Test connection failed" with timeout
**Likely cause:** Network/firewall/proxy.
**Fix:**
- Confirm you can open `https://api.openai.com` (or your provider's URL) in a browser
- If behind a corporate proxy, set the proxy URL in AI Settings → Advanced
- For self-hosted: confirm the local server is running (`curl http://localhost:1234/v1/models`)

### Symptom: "Test connection" works but real calls fail
**Likely cause:** Provider's free tier can't handle the prompt size; or model is unsupported by your account.
**Fix:**
- Check the AI Settings → Diagnostics → Error Log
- Look for "model not found" → switch to a model your account has access to
- Look for "context_length_exceeded" → reduce skill context window

### Symptom: Self-Hosted "Discover Models" returns empty
**Likely cause:** Local server not running, or wrong base URL.
**Fix:**
- LM Studio: confirm "Start Server" is on (default port 1234)
- Ollama: `ollama serve` in a terminal; check `curl http://localhost:11434/v1/models`
- vLLM: `python -m vllm.entrypoints.openai.api_server --port 8000`

### Symptom: "Anthropic API key doesn't look right (expected sk-ant-...)"
**Likely cause:** Wrong key (e.g. an OpenAI key pasted into Anthropic field).
**Fix:** Get the right key from https://console.anthropic.com/settings/keys

---

## 4. Trading & Execution

### Symptom: Skill runs but never finds opportunities
**Likely cause:** Filters too tight, or RPC stale.
**Fix:**
- Lower `min_profit_usd`
- Widen allowed DEXes/protocols
- Check `chain-health` skill output (status bar) — degraded chain = no data
- Confirm your wallet has gas on the chains you're trading

### Symptom: Opportunities found but "rejected by risk"
**Likely cause:** Risk thresholds too conservative.
**Fix:** Settings → Skills → select skill → lower `max_risk_score`, raise `max_position_size`

### Symptom: Trade submitted but reverts on-chain
**Likely cause:** Slippage, front-run, or pool state changed.
**Fix:**
- Lower slippage tolerance
- Enable `mev-protection` skill
- Review the explorer link in the trade detail for the revert reason

### Symptom: "Insufficient funds for gas"
**Likely cause:** Wallet has no native token (ETH/MATIC/BNB) for gas.
**Fix:** Send some native token to the wallet.

### Symptom: Stuck transaction (submitted but never confirms)
**Likely cause:** Gas price too low.
**Fix:** APEX auto-detects stuck txs after 5 minutes; auto-speeds up with a replacement tx. If not, manually speed up via the explorer.

### Symptom: Cross-chain transfer stuck
**Likely cause:** Bridge delays (not APEX).
**Fix:** Check the bridge's status page. APEX shows the current estimated time and updates as the bridge progresses.

---

## 5. Skills

### Symptom: Skill won't enable
**Likely cause:** Required agent not enabled, or no AI provider configured.
**Fix:**
- Settings → AI Configuration → confirm at least one provider is enabled and tested
- Settings → Agents → confirm required agents are enabled
- Check the skill detail panel for the specific error

### Symptom: Skill enabled but never runs
**Likely cause:** Cooldown not elapsed, or schedule not set, or trigger not fired.
**Fix:**
- Skill detail panel shows "Last Run", "Cooldown Remaining", "Next Scheduled"
- For trigger-based skills, check that the trigger event is firing
- For schedule-based, confirm the cron / interval

### Symptom: Skill keeps failing
**Check:** Settings → Skills → click skill → Errors tab
**Common causes:**
- AI provider errors (see §3)
- RPC errors (chain down)
- Contract errors (rejected by contract logic)
- Tool errors (APEX is missing a required data source)

---

## 6. Performance

### Symptom: App uses too much memory
**Typical:** <500MB active, <200MB idle.
**Fix:**
- Disable unused skills
- Settings → Performance → reduce `cache_size_mb`
- Settings → AI Configuration → lower `context_window_tokens`
- Restart the app (truncated caches)

### Symptom: UI is laggy / choppy
**Fix:**
- Settings → Display → disable animations (or enable reduced motion)
- Close unused pages (Dashboard > Trades > etc. each render state)
- Disable heavy charts in Dashboard settings

### Symptom: Slow AI responses
**Fix:**
- Switch to a faster model (e.g. `gpt-4o-mini` or `claude-3-5-haiku`)
- Enable semantic cache (AI Settings → Performance)
- Increase cache TTLs
- Use Self-Hosted if your local server is faster than the cloud

---

## 7. Data & Privacy

### Symptom: "Where is my data stored?"
**Answer:**
- **Windows:** `%APPDATA%\APEX\` (or your portable folder)
- Contents: `apex.db` (SQLite), `keys/` (encrypted blobs), `logs/`, `cache/`

### Symptom: How do I wipe all data?
**Settings → General → Reset All Data** — confirmation required.

### Symptom: How do I back up my data?
**Settings → General → Export Backup** — produces a `.apexbackup` file (no plaintext keys; safe to store). Restore via the same panel.

### Symptom: How do I move APEX to a new PC?
1. Export backup on old PC
2. Install APEX on new PC
3. Import backup
4. Re-add API keys (they can't be exported; only their configs)
5. Re-add wallets (same reason)

---

## 8. Auto-Update

### Symptom: "Update failed"
**Fix:**
- Check internet
- Disable AV temporarily
- Settings → General → "Check for Updates" → see error code
- Common: `EBUSY` (app files locked) → close APEX, retry
- Common: signature verification failed → re-download manually

### Symptom: Stuck on "Downloading update"
**Fix:** Settings → General → Cancel Update → restart APEX → retry.

---

## 9. System Tray

### Symptom: Tray icon missing
**Fix:** Windows may have hidden it. Click the "^" arrow in the system tray → drag APEX back to the visible area.

### Symptom: Closing the window quits the app instead of minimizing to tray
**Fix:** Settings → General → "Minimize to tray on close" → enable.

---

## 10. Logs & Diagnostics

### Where to Find Logs
- **App log:** `%APPDATA%\APEX\logs\apex.log` (JSON, daily rotation, 7 days)
- **AI request traces:** Settings → AI Configuration → Diagnostics → "Export Diagnostics"
- **Skill runs:** Settings → Skills → click skill → Logs
- **Crash reports:** `%APPDATA%\APEX\logs\crash-*.log`

### How to Read Logs
Each line is a JSON object with: `ts, level, msg, request_id?, agent_id?, skill_id?, ...`
Use any JSON viewer, or `tail -f` in PowerShell:
```powershell
Get-Content "$env:APPDATA\APEX\logs\apex.log" -Wait | ForEach-Object { $_ | ConvertFrom-Json | Format-Table -AutoSize }
```

### What to Include in a Bug Report
1. APEX version (Settings → General → About)
2. Windows version
3. Steps to reproduce
4. Expected vs actual
5. Relevant log excerpt (sanitize any keys/addresses)
6. Diagnostics export (no keys included)

---

## 11. Reset & Recovery

### Soft Reset (keeps data, restarts services)
File → Restart Services (or Ctrl+Shift+R)

### Hard Reset (clears all settings, keeps DB)
Settings → General → Reset All Settings

### Nuclear Option (wipes everything)
1. Quit APEX
2. Delete `%APPDATA%\APEX\`
3. Restart APEX (fresh first-run wizard)

---

## 12. Common Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| `E_AUTH` | AI provider auth failed | Check API key |
| `E_RATE` | Rate limit hit | Wait or raise limits |
| `E_TIMEOUT` | Request timed out | Check network, increase timeout |
| `E_RPC` | Chain RPC error | Check chain status, try alternate RPC |
| `E_GAS` | Out of gas | Add native token to wallet |
| `E_SLIPPAGE` | Slippage exceeded | Lower tolerance or wait |
| `E_CONTRACT` | Smart contract rejected | Check skill logs for revert reason |
| `E_CIRCUIT` | Circuit breaker open | Wait 5 min or disable offending skill |
| `E_CONTEXT` | Context window overflow | Reduce context, or switch to model with bigger window |
| `E_TOOL` | Tool execution failed | Check tool logs; may need to retry |

---

## 13. Getting More Help

If your issue persists:
1. **Check `FAQ.md`** for common questions
2. **Search GitHub Issues:** https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows/issues
3. **File a new issue** with the bug report template filled in
4. **Security issues:** see `SECURITY.md` for responsible disclosure — do not file public issues

---

*Most issues are fixed by either: (a) testing your AI connection, (b) checking chain status, or (c) restarting APEX. Try these first.*
