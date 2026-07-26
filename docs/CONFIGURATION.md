# CONFIGURATION.md

## Purpose
This document defines every configuration domain in APEX: environment variables, local settings, defaults, validation, secret classification, and feature flags.

## Scope
Runtime config for Electron main process, renderer-safe settings, AI providers, database, chain adapters, logging, updater, and development tooling.

## Ownership
The config package is the only implementation owner allowed to parse or validate environment variables. All consumers receive typed config objects.

## Configuration Principles
- One schema source in `packages/config`.
- Environment variables are parsed once at startup.
- Renderer receives only explicit safe subsets.
- Invalid config fails fast with actionable messages.
- Secrets are never exposed to renderer or logs.

## Configuration Layers
1. Hardcoded defaults in config schema.
2. `.env` and OS environment variables.
3. Secure local secrets storage for API keys or wallet material.
4. User settings stored in SQLite or encrypted app config, depending on sensitivity.

## Secret Classification
| Class | Examples | Storage |
|---|---|---|
| Public | theme, window size, enabled columns | SQLite/settings table |
| Sensitive | AI API keys, RPC auth tokens | OS-protected secure store + encrypted local envelope |
| Critical | wallet private keys, mnemonics | encrypted secret store only; never plaintext in DB |

## Canonical Environment Variables
| Variable | Required | Default | Scope | Notes |
|---|---|---:|---|---|
| `NODE_ENV` | yes | `production` | all | `development`, `test`, `production` |
| `APEX_APP_ENV` | no | `local` | all | logical deployment environment |
| `APEX_LOG_LEVEL` | no | `info` | main/packages | `debug`, `info`, `warn`, `error` |
| `APEX_DATA_DIR` | no | OS app data path | main | root path for local DB, logs, cache |
| `APEX_DB_FILENAME` | no | `apex.sqlite` | main | SQLite filename |
| `APEX_ENABLE_DEVTOOLS` | no | `false` | desktop | allowed only in development |
| `APEX_AI_PROVIDER` | yes | none | AI | primary provider slug |
| `APEX_AI_MODEL_DEFAULT` | yes | none | AI | default model identifier |
| `APEX_AI_TIMEOUT_MS` | no | `30000` | AI | provider call timeout |
| `APEX_AI_MAX_RETRIES` | no | `2` | AI | retry count excluding validation retries |
| `APEX_OPENAI_API_KEY` | conditional | none | AI secret | required when provider is OpenAI |
| `APEX_ANTHROPIC_API_KEY` | conditional | none | AI secret | required when provider is Anthropic |
| `APEX_GEMINI_API_KEY` | conditional | none | AI secret | required when provider is Gemini |
| `APEX_PRIMARY_CHAIN` | no | `ethereum` | chain | default chain context |
| `APEX_SUPPORTED_CHAINS` | yes | none | chain | comma-separated canonical chain IDs |
| `APEX_RPC_ETHEREUM` | conditional | none | chain secret | one env per chain |
| `APEX_RPC_ARBITRUM` | conditional | none | chain secret | one env per chain |
| `APEX_RPC_BASE` | conditional | none | chain secret | one env per chain |
| `APEX_QUOTE_TTL_MS` | no | `1500` | dex | quote cache TTL |
| `APEX_MAX_SLIPPAGE_BPS` | no | `50` | trading | global fail-safe cap |
| `APEX_MAX_POSITION_USD` | no | `1000` | risk | default paper/live limit |
| `APEX_FEATURE_PAPER_TRADING` | no | `true` | feature flag | gate for simulation mode |
| `APEX_FEATURE_LIVE_TRADING` | no | `false` | feature flag | disabled unless explicit |
| `APEX_FEATURE_AI_AUTONOMY` | no | `false` | feature flag | controlled release |
| `APEX_AUTO_UPDATE_CHANNEL` | no | `stable` | desktop | `stable`, `beta`, `alpha` |
| `APEX_SENTRY_DSN` | no | none | observability | optional external telemetry |

## Validation Rules
- Numeric values must be range-validated after parsing.
- Chain lists must map to supported canonical identifiers.
- Provider-specific API key requirements must be enforced conditionally.
- Unknown config keys in persisted settings should be rejected or migrated.

## Renderer-Safe Configuration Surface
Renderer may receive only:
- feature flags safe for UI rendering,
- selected environment label,
- non-secret defaults such as supported chain names,
- window/UI settings.

Renderer must never receive raw provider keys, wallet secrets, filesystem absolute paths unrelated to UI, or unredacted log destinations.

## Feature Flags
| Flag | Purpose | Default | Owner |
|---|---|---:|---|
| `paperTrading` | Simulated order execution | true | trading |
| `liveTrading` | Allows signed real transactions | false | trading/security |
| `aiAutonomy` | Enables AI-triggered autonomous execution proposals | false | AI/risk |
| `advancedDeveloperTools` | Exposes low-level diagnostics | false | platform |
| `experimentalDexAdapters` | Enables adapters not yet production-approved | false | integrations |

## Settings Categories
- UI settings
- provider settings
- chain connectivity settings
- strategy preferences
- safety thresholds
- updater settings
- diagnostics settings

## Failure Behaviour
- Missing required config -> startup failure with actionable error.
- Invalid noncritical persisted setting -> fallback to default + warning log.
- Missing provider key for disabled provider -> no startup failure.
- Missing provider key for selected active provider -> startup failure.

## Implementation Requirements
- Central schema built with `zod`.
- Export `AppConfig`, `RendererConfig`, `FeatureFlags`, and per-domain typed subsets.
- Add migration versioning for persisted config records.
- Keep config resolution deterministic and testable.

## Cross-References
- [`CLOUD-AI-INTEGRATION.md`](./CLOUD-AI-INTEGRATION.md)
- [`AI-SETTINGS.md`](./AI-SETTINGS.md)
- [`DATABASE-SCHEMA.md`](./DATABASE-SCHEMA.md)
- [`PERMISSION-MODEL.md`](./PERMISSION-MODEL.md)
- [`FILE-STORAGE.md`](./FILE-STORAGE.md)
