# APEX Frequently Asked Questions

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026

---

## General

### What is APEX?
APEX is a Windows desktop application for automated arbitrage trading across
multiple EVM blockchains. It uses cloud AI to score and execute opportunities.

### Do I need to know how to code?
No. APEX is a packaged `.exe` you install and use through a GUI. Power users
can author custom skills (JSON), but it's optional.

### Is APEX open source?
The codebase is on GitHub. The desktop app is the primary deliverable.

### How is APEX different from a simple arbitrage bot?
APEX is **modular**: it hosts many independent strategies under one architecture,
with full safety pipelines (Discovery → Risk → Simulation → Execution → Learning).
It also learns from every trade.

### Does APEX guarantee profits?
**No.** Arbitrage is risky. Markets can move against you between detection and
execution. APEX maximizes risk-adjusted profit, not raw profit. You can lose money.

---

## Platform & Tech

### Why Windows-only?
APEX is built on Electron for distribution simplicity. macOS/Linux are not
currently targets (the underlying code is mostly cross-platform; a Mac build
is on the roadmap).

### Why no Docker?
APEX is a single-user desktop app. Adding Docker would be overhead with no
benefit. All services run in the Electron main process.

### Why cloud AI only? Why not run LLMs locally?
For v3, APEX ships cloud-only to keep the install simple and small. **But**
you can point APEX at a self-hosted OpenAI-compatible server (LM Studio,
Ollama, vLLM, llama.cpp) on your machine — that gives you local AI with
zero cloud calls. See `AI-SETTINGS.md` §3.3.

### What chains are supported?
Initial: Ethereum, BNB Chain, Polygon, Arbitrum, Optimism, Base.
Planned: Avalanche, Linea, zkSync Era, Scroll, Mantle, Gnosis, Celo, Sonic.
See `CHAIN-INTEGRATION.md` for the full roadmap and how to add more.

### What DEXs are supported?
Uniswap V2/V3, SushiSwap, PancakeSwap, Curve, Balancer initially.
See `DEX-INTEGRATION.md` for the full list and how to add more.

---

## Cost & Pricing

### How much does APEX cost?
The application is free. **You pay for:**
- AI API usage (depends on the model — `gpt-4o-mini` is ~$0.15 per million input tokens; `claude-3-5-haiku` is similarly cheap)
- Blockchain gas (paid to the network, not to APEX)
- Optional: bridge fees

### How much will AI cost me?
Typical usage: **$1–$10 per day** depending on how many skills you enable and
how chatty they are. Heavy backtesting can be $50+/day. You can set hard caps
in AI Settings.

### Does APEX have a free trial for the AI part?
APEX itself is free, but you bring your own API keys. Many providers (Groq,
Together, Google AI Studio) offer free tiers. You can also use a local model
for $0 AI cost.

### Are there hidden fees?
No. APEX takes no cut. No telemetry sold, no "premium" tier, no in-app purchases.

---

## Security

### Where are my API keys stored?
Encrypted via Electron `safeStorage` (Windows DPAPI). Never plaintext, never logged.

### Where are my private keys stored?
Encrypted with your passphrase (Argon2id) + safeStorage. Decrypted only at
signing time, zeroed immediately after.

### Does APEX phone home?
No. No telemetry by default. Auto-update is opt-out and only checks GitHub.

### Can my keys be extracted?
With DPAPI, only by code running as your user account. APEX's renderer is
sandboxed; only the main process can decrypt. We follow the standard Electron
hardening checklist. See `SECURITY.md` for the full threat model.

### What if my laptop is stolen?
Your DPAPI-encrypted keys can only be decrypted by your Windows user account.
The thief would also need your wallet passphrase (which is not stored anywhere
on disk). So: enable Windows login (PIN/biometric) and use a strong wallet
passphrase.

### Is APEX code-signed?
Not yet. SmartScreen will warn on first install — click "More info → Run anyway".
Code signing is on the v3.1 roadmap.

---

## Trading

### Does APEX need my private key?
Only if you enable execution skills. For analysis-only, you don't need any
wallet. We strongly recommend a **dedicated trading wallet** with limited funds.

### Can I lose money?
Yes. Arbitrage is risky. APEX has many safety layers (risk scoring,
simulation, circuit breaker, stop-loss) but cannot eliminate all risk.
Start small.

### Can I paper-trade first?
Yes — enable only `*_analysis_*` skills and `portfolio-aggregator`. You get
full intelligence without execution. Paper-trading mode (where APEX simulates
trades against live data) is on the v3.1 roadmap.

### What is "simulation before execution"?
Every opportunity runs through a full dry-run before any transaction is signed:
flash loan availability, gas, DEX routing, swap math, profit, revert conditions.
Only if the simulation passes does APEX actually send a transaction.

### What's a flash loan?
A flash loan lets you borrow huge sums with no collateral, **as long as you
repay in the same transaction**. APEX uses flash loans to do arbitrage with
zero upfront capital. The whole trade (borrow → swap → repay) is one atomic tx.

### How does APEX choose which opportunities to execute?
Multi-factor AI scoring: expected profit, risk, gas, slippage, MEV probability,
protocol health, historical success rate. The user-configured thresholds then
filter.

### What if the AI is wrong?
That's why we have `anomaly-circuit-breaker` and `pre-trade-risk` skills.
On abnormal conditions, APEX pauses all execution and alerts you. You can
also set hard limits (max daily loss, max position size) that the AI cannot override.

---

## Skills & AI

### What's a skill?
A user-toggleable capability. See `SKILLS.md` for the full list and the
mental model (skill = user-facing capability; agent = AI brain inside it).

### How do I add a custom skill?
v3.1+ supports user-authored skills via JSON. For now, all skills ship with APEX.

### How do I add a new AI provider?
**AI Settings → Add Provider** → pick a template or "Custom" → fill in base URL,
model, key. The provider becomes available immediately.

### Why isn't my self-hosted LM Studio / Ollama working?
Check:
- Server is running (`curl http://localhost:1234/v1/models`)
- Base URL is correct (default ports: LM Studio 1234, Ollama 11434, vLLM 8000)
- API key field is empty (unless you set one in the local server)
- Use the **Discover Models** button to populate the model dropdown

### Can I use multiple AI providers at once?
Yes. APEX picks the best one per call (using your priority + cost + latency),
and auto-failover if one fails.

### What if all my providers go down?
APEX enters a "rule-based mode" (heuristics only, no AI), keeps monitoring,
and auto-resumes AI when providers return. You see a clear banner.

### How do I reduce AI cost?
- Use cheaper models (gpt-4o-mini, claude-3-5-haiku, local)
- Enable semantic cache
- Lower context windows
- Use local AI for non-critical skills
- Set daily quotas / monthly cost caps

### Will my prompts be used to train the provider's model?
That depends on the provider's terms. OpenAI, Anthropic, etc. have "no
training on API data" policies for paid tiers. Read your provider's terms.
APEX itself does not transmit data anywhere except to the providers you configure.

---

## Wallets

### Which wallets are supported?
- Any EVM private key (MetaMask export, hardware wallet planned)
- Multi-wallet support: add as many as you like
- Per-wallet config: name, chains, max position size

### Can I use a hardware wallet (Ledger, Trezor)?
Planned for v3.1 (Ledger via WebHID, Trezor via WebUSB).

### Should I put my whole portfolio into APEX?
**No.** Use a dedicated trading wallet with only the capital you intend to
actively trade.

---

## Updates & Support

### How do I update?
APEX auto-checks every 4 hours. You can also manually check:
**Settings → General → Check for Updates**.

### How do I report a bug?
GitHub Issues: https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows/issues

### How do I report a security issue?
See `SECURITY.md` for responsible disclosure. Do not file public GitHub issues
for security bugs.

### Where can I ask questions?
- GitHub Discussions (planned)
- This FAQ
- In-app Help

---

## Roadmap

### What's next?
- v3.1: Code signing, custom user skills, paper trading, more chains
- v3.2: Hardware wallets, Telegram/Discord notifications, mobile companion (read-only)
- v4.0: Non-EVM chains (Solana, Sui), advanced strategies (market making, statistical arb)

See `ENHANCEMENT-ROADMAP.md` for the detailed plan.

---

*If your question isn't here, check `TROUBLESHOOTING.md` or open a GitHub issue.*
