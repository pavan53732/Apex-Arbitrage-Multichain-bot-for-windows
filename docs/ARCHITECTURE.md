# APEX Architecture - Windows Desktop Multichain Arbitrage Bot

> **Version:** 2.0.0 | **Target:** Windows 10/11 x64 (.exe) | **AI:** Cloud APIs Only

---

## 1. System Overview

APEX is a Windows-native desktop application for detecting and executing
cross-chain and intra-chain arbitrage opportunities. All AI/ML inference is
performed via cloud API calls (OpenAI-compatible and Anthropic endpoints).
No Docker, no containers, no local model hosting.

### High-Level Layers

- **PRESENTATION LAYER:** Electron Renderer (React + TypeScript) - Dashboard, Charts, Trade History, AI Settings Page
- **DESKTOP SHELL LAYER:** Electron Main Process (Node.js) - Window management, IPC bridge, system tray, auto-update, Windows .exe packaging via electron-builder
- **APPLICATION LAYER:** Backend Services (TypeScript) - Agent Orchestrator, Skill Manager, AI Pipeline Router, Strategy Engine, Risk Manager, Execution Engine
- **AI PIPELINE LAYER (Cloud):** Provider Abstraction - OpenAI-compatible endpoint caller, Anthropic Messages API caller, Retry/fallback/rate-limit handling
- **DATA LAYER:** SQLite (trade history, settings, skill registry), Encrypted key-value store (API keys via Electron safeStorage), In-memory caches
- **CHAIN LAYER:** EVM RPC connections (Ethereum, BSC, Polygon, Arbitrum), WebSocket price feeds, Smart contract interactions

---

## 2. Component Architecture

### 2.1 Electron Desktop Shell
- **Main Process:** Node.js runtime hosting all backend services
- **Renderer Process:** React SPA for the UI
- **IPC Bridge:** Secure contextBridge for renderer-to-main communication
- **Packaging:** electron-builder producing NSIS .exe installer for Windows
- **Auto-Update:** electron-updater checking GitHub Releases
- **No Docker:** Everything runs natively on Windows via Node.js

### 2.2 Agent Orchestrator
- Receives tasks from Strategy Engine
- Routes tasks to AI agents via AI Pipeline
- Collects responses, feeds back to decision layers
- Maintains agent conversation context per session

### 2.3 AI Pipeline Router
- **Provider Registry:** Dynamic registration of AI endpoints
- **Request Builder:** Formats prompts per provider spec
- **Response Parser:** Normalizes responses to common format
- **Fallback Chain:** Cascade to secondary on failure
- **Rate Limiter:** Token-bucket per provider

### 2.4 Strategy Engine
- Scans multiple DEXs across chains for price discrepancies
- Calculates profit after gas, slippage, bridge fees
- Uses AI agents for sentiment and prediction scoring
- Outputs ranked opportunity list to Execution Engine

### 2.5 Risk Manager
- Position sizing, max drawdown limits, stop-loss/take-profit
- AI-assisted risk scoring via cloud API
- Circuit breaker: halts trading on anomalies

### 2.6 Execution Engine
- Builds/signs transactions locally (encrypted key storage)
- Submits via RPC with gas optimization
- Monitors status, handles reorgs

### 2.7 Skill Manager
- Registry of bot capabilities (see SKILLS.md)
- Skills enabled/disabled by user
- Composed of one or more agent calls

---

## 3. Data Flow

User Configures AI Settings -> Saved to encrypted store -> Strategy Engine scans chains -> Opportunities detected -> Agent Orchestrator -> AI Pipeline Router -> Cloud AI API -> AI Response -> Risk Manager validates -> Execution Engine executes -> Trade result -> SQLite -> Dashboard UI

---

## 4. Technology Stack

| Layer | Technology |
|-------|-----------|  
| Desktop Shell | Electron 31+ |
| UI Framework | React 18 + TypeScript |
| Styling | Tailwind CSS + shadcn/ui |
| State | Zustand |
| Backend | Node.js 20+ (Electron main) |
| Database | better-sqlite3 |
| Key Storage | Electron safeStorage (DPAPI) |
| Blockchain | ethers.js v6 |
| Contracts | Solidity 0.8.x + Hardhat |
| AI Providers | OpenAI, Anthropic, any OpenAI-compatible |
| Packaging | electron-builder (NSIS) |
| Auto-Update | electron-updater + GitHub Releases |

---

## 5. Windows-Specific

- **No Docker:** All services in Electron main process
- **No WSL:** Pure Windows native execution
- **DPAPI:** API keys encrypted via Windows Data Protection API
- **System Tray:** Minimizes to tray, continues monitoring
- **Startup:** Optional Windows startup via registry
- **Installer:** Single .exe NSIS, no admin for per-user install
- **Portable Mode:** Optional, stores data in app directory

---

## 6. Security (see SECURITY.md)

- API keys via Electron safeStorage (OS-level encryption)
- Private keys stored separately with passphrase
- All AI calls over HTTPS only
- No telemetry by default
- CSP enforced in renderer
- Node integration disabled; IPC via contextBridge only

---

## 7. Performance

- **Worker Threads:** CPU-intensive tasks offloaded
- **Connection Pooling:** Reusable RPC connections
- **Batch AI Calls:** Multiple queries batched
- **Caching:** AI responses cached with TTL
- **Debouncing:** UI updates debounced

---

*This document defines the architectural foundation. All implementation must align.*
