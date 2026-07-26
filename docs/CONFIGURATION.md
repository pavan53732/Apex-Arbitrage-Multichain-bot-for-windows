# CONFIGURATION.md

## Purpose
Defines the complete runtime configuration model for APEX, including environment variables, defaults, validation rules, secrets handling, feature flags, and configuration loading order.

## Scope
Covers local development, packaged Windows desktop execution, CI environments, AI provider settings, chain settings, storage paths, logging levels, and kill-switch controls.

## Related Documents
- [AI-SETTINGS.md](./AI-SETTINGS.md)
- [CLOUD-AI-INTEGRATION.md](./CLOUD-AI-INTEGRATION.md)
- [SECURITY.md](./SECURITY.md)
- [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md)
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)

## Load Order
1. Built-in application defaults.
2. Packaged app config file.
3. `.env.local` for development only.
4. OS environment variables.
5. User-saved settings stored in encrypted local configuration.
6. Runtime overrides from validated UI settings.

Later layers override earlier layers only when validation passes.

## Configuration Domains
- App runtime
- Window and desktop behavior
- AI providers
- Chains and RPC endpoints
- DEX adapters
- Database paths and retention
- Logging and diagnostics
- Feature flags
- Safety controls

## Environment Variables
| Key | Required | Default | Validation | Notes |
|---|---|---|---|---|
| `NODE_ENV` | Yes | `production` | one of `development`, `test`, `production` | runtime mode |
| `APEX_APP_ENV` | No | `desktop` | one of `desktop`, `ci` | deployment profile |
| `APEX_DATA_DIR` | No | OS app-data path | writable absolute path | local app storage |
| `APEX_LOG_LEVEL` | No | `info` | one of `debug`, `info`, `warn`, `error` | structured logger level |
| `OPENAI_API_KEY` | Conditional | none | non-empty if provider enabled | secret |
| `ANTHROPIC_API_KEY` | Conditional | none | non-empty if provider enabled | secret |
| `GEMINI_API_KEY` | Conditional | none | non-empty if provider enabled | secret |
| `OPENROUTER_API_KEY` | Conditional | none | non-empty if provider enabled | secret |
| `DEFAULT_AI_PROVIDER` | No | `openai` | provider enum | initial routing choice |
| `DEFAULT_AI_MODEL` | No | provider-specific | non-empty | initial model |
| `RPC_ETHEREUM` | Conditional | none | valid https URL | chain endpoint |
| `RPC_BASE` | Conditional | none | valid https URL | chain endpoint |
| `RPC_ARBITRUM` | Conditional | none | valid https URL | chain endpoint |
| `DATABASE_FILENAME` | No | `apex.sqlite` | file name only | stored under data dir |
| `APEX_ENABLE_AUTOTRADE` | No | `false` | boolean | hard-gated feature flag |
| `APEX_ENABLE_DEVTOOLS` | No | `false` | boolean | disabled in production builds |
| `APEX_ENABLE_VERBOSE_IPC_LOGS` | No | `false` | boolean | diagnostic-only |
| `APEX_KILL_SWITCH_DEFAULT` | No | `true` | boolean | safe boot default |

## Validation Rules
- All config must pass a central schema before use.
- Secret-bearing keys must never be logged in plaintext.
- URL settings must require `https` except explicit localhost development overrides.
- Feature flags must be boolean and documented here before use.
- Unknown config keys should be rejected in strict mode and warned in compatibility mode.

## Secrets Handling
- API keys entered through UI must be encrypted at rest.
- Environment variable secrets are read-only inputs and must never be copied into logs.
- The app must mask secrets in diagnostics and export bundles.
- See [SECURITY.md](./SECURITY.md) for encryption details.

## Persisted User Settings
Persisted settings should include:
- selected providers and models,
- enabled chains,
- UI preferences,
- safe non-secret feature flags,
- window preferences.

Secrets must be stored separately from general preferences.

## AI Agent Guidance
- Do not add new environment variables without updating this file.
- If a feature requires configuration, define key, default, validation, and ownership here first.
- Generated config loaders must mirror this document exactly.
