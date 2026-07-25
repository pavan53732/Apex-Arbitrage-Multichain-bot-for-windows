# APEX User Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Audience:** End users of the APEX Windows desktop application.

---

## 1. What is APEX?

APEX is a **Windows desktop application** (single `.exe`) that watches multiple
blockchain networks for arbitrage opportunities, scores them with AI, and can
execute trades automatically when your safety conditions are met.

Key things to know:
- **No Docker, no WSL** — just an `.exe`
- **Cloud AI only** — APEX calls AI services you configure; nothing runs locally
- **You stay in control** — set your AI keys, your risk limits, your wallets
- **Modular** — turn on only the skills you want

---

## 2. Installation

1. Download the latest `APEX-Setup-*.exe` from the [Releases](https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows/releases) page
2. Double-click the installer — no admin required (per-user install)
3. If Windows SmartScreen warns you, click **More info → Run anyway** (we are not yet code-signed; see `SECURITY.md` for our signing roadmap)
4. APEX launches and shows the first-run setup wizard

### 2.1 System Requirements
- **OS:** Windows 10 (21H2+) or Windows 11
- **CPU:** x64, dual-core 1.5GHz+
- **RAM:** 4GB minimum, 8GB recommended
- **Disk:** 400MB for app + data
- **Network:** Stable internet for AI calls and RPC
- **Optional:** Local LLM server (LM Studio, Ollama, vLLM) for fully local AI

### 2.2 Portable Mode
Want a fully portable install? Create a folder, put the unpacked app files
in it, then create an empty file named `portable.flag` in the same folder.
APEX will store all data (database, keys, logs) in that folder instead of
`%APPDATA%\APEX`.

---

## 3. First-Run Setup

The wizard walks you through:

1. **Choose an AI provider**
   - **OpenAI** — easiest if you have an OpenAI API key
   - **Anthropic** — if you have an Anthropic API key
   - **Self-Hosted Local** — if you run LM Studio / Ollama / vLLM on your machine
   - **Custom** — any OpenAI-compatible cloud service (Groq, Together, etc.)
2. **Paste your API key** (or leave blank for local)
3. **Test the connection** — APEX sends a tiny test prompt; shows latency
4. **Add a wallet** (optional, for live trading) — private key is encrypted on your disk
5. **Choose skills** to enable — start with the "safe" preset, expand later
6. **Done** — APEX opens the Dashboard

You can re-run the wizard any time from **Help → Run Setup Wizard**.

---

## 4. AI Configuration (Settings → AI Configuration)

This is the most important page. It controls every AI call APEX makes.

### 4.1 Add a Provider
1. Click **Add Provider**
2. Pick a template (OpenAI, Anthropic, Self-Hosted Local, or a preset like Groq/Together/OpenRouter/DeepSeek/Mistral)
3. The base URL and model name fill in automatically
4. Paste your API key (if needed)
5. Adjust Max Tokens, Temperature, Rate Limits
6. Click **Test Connection** — should turn green within 1-3 seconds
7. Click **Save**

### 4.2 Self-Hosted Local Setup
Most common case: you're running **LM Studio** or **Ollama** on your machine.

**LM Studio:**
1. Open LM Studio, start its local server (default `http://localhost:1234/v1`)
2. In APEX AI Settings, click **Add Provider → Self-Hosted Local → LM Studio**
3. Base URL is prefilled: `http://localhost:1234/v1`
4. Click **Discover Models** — APEX pulls the list of models LM Studio is serving
5. Pick your model from the dropdown
6. Click **Save** (no API key needed)

**Ollama:**
1. In Ollama, ensure the OpenAI-compatible shim is enabled (default in Ollama 0.1.14+)
2. Server is at `http://localhost:11434/v1`
3. In APEX: Add Provider → Self-Hosted Local → Ollama
4. Pick a model you've pulled (e.g. `llama3.1:8b`)
5. Save

> **Tip:** You can run multiple providers simultaneously and APEX will
> automatically pick the best one per call, or failover if one fails.

### 4.3 Switching Models Mid-Session
You can change the model on a provider at any time. In-flight requests finish
on the old model; new requests use the new one. No restart required.

### 4.4 Resetting
- **Reset this provider** — clears all fields to defaults for that provider
- **Reset All** — wipes every provider config and key (irreversible!)

---

## 5. Wallets

### 5.1 Add a Wallet
**Settings → Wallets → Add Wallet**

1. Name your wallet (e.g. "Main", "Hot", "Cold")
2. Paste your private key (or import via Ledger/Hardware planned)
3. Set a passphrase — this encrypts the key on disk
4. Confirm the address shown matches what you expect
5. Save

### 5.2 Security
- Private keys are **never** stored in plaintext
- Encryption uses Argon2id (passphrase) + safeStorage (DPAPI on Windows)
- Keys are decrypted only when signing a transaction
- Keys are zeroed in memory immediately after signing
- APEX never sends your key anywhere

### 5.3 Best Practices
- Use a **dedicated trading wallet** with only the funds you intend to trade
- Never put your long-term cold storage seed here
- Enable **spending limits** in the wallet settings

---

## 6. Skills

Skills are APEX's toggleable capabilities. See `SKILLS.md` for the complete list.

### 6.1 The Safe Preset
**Settings → Skills → Preset: Safe** enables:
- `chain-health` (always-on monitor)
- `portfolio-aggregator` (read-only)
- `market-sentiment` (analysis only)
- `pre-trade-risk` (gates any execution)

This is a great starting point — you get intelligence without execution risk.

### 6.2 Enabling Execution Skills
Execution skills are `high` or `critical` risk. Before enabling:
1. Set up a wallet with limited funds
2. Configure risk limits (max position, max daily loss, slippage cap)
3. Enable `anomaly-circuit-breaker` first (it'll pause everything if something's off)
4. Enable one execution skill at a time; monitor for 24-48 hours
5. Review the Trade History before adding more

### 6.3 Custom Parameters
Most skills have configurable parameters (e.g. "minimum profit threshold").
Click a skill → adjust in the detail panel → save. Changes apply immediately
for new invocations; in-flight skills use the old config.

---

## 7. The Dashboard

### 7.1 What You'll See
- **Top Bar:** app title, global search (Ctrl+K), theme toggle, notifications
- **Sidebar (left):** Dashboard, Trades, Opportunities, Skills, Agents, Settings
- **Main area:** charts and live data
- **Status Bar (bottom):** chain health, current gas, AI status, version

### 7.2 Key Numbers
- **Portfolio Value** — current USD value across all tracked wallets
- **P&L (24h / 7d / 30d)** — realized + unrealized
- **Active Skills** — count of enabled skills running
- **AI Spend (24h)** — total AI cost today
- **Open Opportunities** — top ranked, not yet executed

### 7.3 Real-Time Updates
All numbers update live without page refresh. You'll see:
- Pulse animation on connection status dot
- Number flash (green/red) on P&L changes
- Toast notifications on trade events, AI errors, skill state changes

---

## 8. Trades

### 8.1 Trade History
A sortable, filterable table of every trade. Click any row to see:
- Full transaction hash (with explorer link)
- Input/output amounts per leg
- Gas used
- Net profit/loss
- AI confidence at the time
- Reasoning (if AI was involved)

### 8.2 Export
**Trades → Export** downloads a CSV (for taxes) or JSON (for analysis).
API keys and private keys are never included.

---

## 9. Notifications

APEX can notify you via:
- **In-app toasts** (always on)
- **System notifications** (Windows toast — enable in Settings)
- **Email** (planned)
- **Telegram / Discord webhooks** (planned)

Go to **Settings → Notifications** to configure which events notify you and on which channel.

---

## 10. Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Open command palette / search |
| `Ctrl+B` | Toggle sidebar |
| `Ctrl+,` | Open Settings |
| `Ctrl+1..9` | Jump to page |
| `Ctrl+S` | Save (in any form) |
| `Ctrl+T` | Test AI connection (in AI Settings) |
| `Ctrl+R` | Reset (with confirm) |
| `Esc` | Close modal / cancel |
| `?` | Show all shortcuts |

---

## 11. Troubleshooting

Quick fixes:
- **"No AI providers configured"** — go to AI Settings, add one
- **"Test connection failed"** — check internet, then check the key; try a different region/base URL
- **"Rate limit exceeded"** — wait or reduce the per-provider RPM/TPM in AI Settings
- **App stuck / frozen** — File → Restart; if it persists, see `TROUBLESHOOTING.md`
- **Trade failed** — check chain status (status bar); the tx hash links to the explorer for the revert reason
- **Data folder** — `%APPDATA%\APEX\` (or your portable folder)

For deeper issues, see `TROUBLESHOOTING.md`.

---

## 12. Updating APEX

APEX auto-checks for updates every 4 hours. When one is available:
- A toast appears with "Update Available"
- Click to see release notes
- Click "Download" — runs in background
- When ready, click "Restart to Install"
- Your data and settings are preserved

Disable auto-update in **Settings → General**.

---

## 13. Uninstalling

- **Standard install:** Settings → Apps → APEX → Uninstall
- **Portable install:** delete the folder
- **Data wipe:** delete `%APPDATA%\APEX\` after uninstall
- Your data is **local only**; we have no cloud copy of it

---

## 14. Getting Help

- **In-app:** Help → Documentation opens this site
- **GitHub:** [Issues](https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows/issues) for bugs
- **FAQ:** see `FAQ.md`
- **Security issues:** see `SECURITY.md` for responsible disclosure

---

*Welcome to APEX. Configure your AI, pick your skills, and let's trade.*
