## Subsystem Ultra-Granular Map & Generation Cues

## Dashboard Usage Map (Agent and Operator)

---
## AI Agent Self-Validation Protocol

Before, during, and after code generation:
Validate: All references, import paths, config keys, and model links
Lint: All generated JS/TS/Python code with appropriate tools
Test: Generate and run all unit/integration/fuzz/AI tests

## Quick Links

- Health checks: [HEALTHCHECK.md](HEALTHCHECK.md)
- Project tree: [PROJECT TREE COMPLETE STUCTURE .md](PROJECT%20TREE%20COMPLETE%20STUCTURE%20.md)

---

## Agent Self-Test, Error Handling, and Debugging Protocol

All agents must:

Output test and lint results to /logs/ after every generation run

Auto-scan for missing, duplicate, or broken files/folders after codegen

Suggest fixes and validate against all manifest/ files and project tree

If an error or incomplete state is detected, halt further generation and report to operator

---

# Apex Arbitrage Multichain Bot

This project is config-first and multi-chain; networks and protocol addresses are declared in config/chains.json and config/protocols.json, with optional RPC overrides via environment.

## Quick Links

- Chains: [config/chains.json](config/chains.json)
- Protocols: [config/protocols.json](config/protocols.json)
- AI config: [ai-modules/aiConfig.json](ai-modules/aiConfig.json)
- Model weights: [ai-modules/models/modelWeights](ai-modules/models/modelWeights)
- Training outputs: [ai-modules/models/trainingOutputs](ai-modules/models/trainingOutputs)
- API specs: [api_reference.md](api_reference.md), [docs/api/](docs/api/)
- Operator guide: [operator-guide.md](operator-guide.md)
- Dashboard docs: [dashboard/README.md](dashboard/README.md)
- Health checks: [HEALTHCHECK.md](HEALTHCHECK.md)

> Note: Examples in this repository are illustrative; the actual set of enabled networks is always read from config/chains.json at runtime. No networks or protocol addresses should be hardcoded in code.

## Project Structure (synced)

This section is synchronized from 'PROJECT TREE COMPLETE STUCTURE .md' and shows the canonical top-level files and first-level directories; for the full nested tree, open that file.

<!-- BEGIN: SYNCED_PROJECT_TREE -->
```text
- .dockerignore
- .editorconfig
- .env
- .env.example
- .eslintrc
- .flake8
- .gitignore
- .prettierrc
- .stylelintrc
- ai-feedback.sqlite
- ai-training.sqlite
- analytics.sqlite
- api_reference.md
- audit-trail.sqlite
- backup-meta.json
- Bot Blue Print.md
- CHANGELOG.md
- CODE_OF_CONDUCT.md
- compliance.sqlite
- CONTRIBUTING.md
- Dashboard.md
- docker-compose.yml
- forensics.sqlite
- HEALTHCHECK.md
- LEGAL.md
- LICENSE
- logs.sqlite
- Makefile
- manifest.csv
- manifest.json
- manifest.md
- operator-guide.md
- package.json
- PROJECT FILES AND FOLDERS DETAILS .MD
- PROJECT TREE COMPLETE STUCTURE .md
- README.md
- requirements.txt
- roadmap.md
- SECURITY.md
- tsconfig.json
- wall-of-fame.md

- .devcontainer/
- .github/
- .husky/
- .vscode/
- ai-modules/
- archive/
- backend/
- benchmarks/
- ci/
- config/
- dashboard/
- data/
- deploy/
- docs/
- examples/
- logs/
- manifest/
- migrations/
- overlays/
- presets/
- public/
- research/
- scripts/
- storage/
- tests/
- third-party/
- types/
- utils/
- vendor/
- wall-of-fame/
- watchdog/
```
<!-- END: SYNCED_PROJECT_TREE -->

For the complete nested tree (all subfolders and files), see 'PROJECT TREE COMPLETE STUCTURE .md'.

## Project Structure Overview

| Folder/File        | Description                                                                   |
|--------------------|-------------------------------------------------------------------------------|
| `.devcontainer/`   | VS Code dev container config (Docker, Python, Node, full toolchain)           |
| `.github/`         | All GitHub workflows: lint, test, CI/CD, security, PR templates, dependabot   |
| `.husky/`          | Git hooks: pre-commit, pre-push, commit lint, staged lint                     |
| `.vscode/`         | Workspace/editor settings, recommended extensions, launch configs              |
| `ai-modules/`      | All AI/ML logic: scoring, pattern learning, council, data, notebooks, weights |
| `archive/`         | Deprecated modules, legacy configs, migration logs, previous releases          |
| `backend/`         | Bot/engine core, strategy logic, plugins, contract adapters, state, utils      |
| `benchmarks/`      | Stress and perf tests: CPU, gas, mempool, datasets, results                   |
| `ci/`              | External CI/CD integrations: Jenkins, GitLab, Buildkite scripts               |
| `config/`          | All configs: tokens, chains, DEXes, strategies, analytics, compliance         |
| `data/`            | Datasets, logs, backup, audit, ML data, operator state, simulation results    |
| `dashboard/`       | Next.js/React UI: pages, widgets, analytics, overlays, public assets          |
| `deploy/`          | Infra-as-code: k8s, Terraform, Ansible, Helm, cloud configs                   |
| `docs/`            | Architecture, onboarding, ADRs, API refs, threat models, playbooks            |
| `examples/`        | Usage, CLI/test samples, screenshots, dashboards, simulation/testnet configs   |
| `logs/`            | Legacy logs (new logs are in data/logs/)                                      |
| `manifest/`        | Project manifest: inventory files (.json/.csv/.md/tree.txt)                   |
| `migrations/`      | DB/schema/contract migration scripts and logs                                 |
| `overlays/`        | UI overlays: AR, XAI, debug, incident response                                |
| `presets/`         | User/strategy presets, templates, demo configs                                |
| `public/`          | Static assets for dashboard (logos, SVG, themes)                              |
| `research/`        | Experiments, notebooks, alpha, quantum/ML prototypes                          |
| `scripts/`         | Automation: setup, quickstart, update, manifest/batch/py/pwsh scripts         |
| `storage/`         | Key vault, secret backups (encrypted), agent snapshots, strat archives        |
| `tests/`           | Unit, integration, E2E, regression, fuzz, AI/contract tests                   |
| `third-party/`     | External SDKs, connectors, vendor plugins, adapters, oracles                  |
| `types/`           | Shared types: TS/JS/Python/ABI/JSON-Schema, contract ABIs                     |
| `utils/`           | Shared utilities, reusables, ops, simulation helpers                          |
| `vendor/`          | Vendored source/libs, frozen dependencies, binaries, patches                  |
| `wall-of-fame/`    | Contributor records, badges, recognitions, testimonials                       |
| `watchdog/`        | Event listeners, kill switches, failover, circuit breakers, auto-restart      |
| ...                | All root-level configs, legal, manifest, project files, guides, etc.          |

---
 
## Ultra-Granular Folder and Integration Map

**For every folder, subfolder, and key file, AI agents MUST:**

- **Read the local README.md, config, and code stubs**
- **Infer intended file type, dependencies, and function**
- **Wire with other folders strictly via public APIs/interfaces**
- **Never cross-modify outside the assigned context without agent review**
- **Prioritize runtime pluggability, atomic execution, and hot-swap compatibility**

### Example integration flows

- ai-modules/ -> backend/plugins/aiAdapter.js -> dashboard/pages/ai-settings.js  
- backend/plugins/dexAdapter.js <-> contracts/interfaces/IDEX.sol  
- dashboard/components/profitChart.js <- data/logs/profits.db  
- watchdog/autoRestart.js -> backend/core/errorHandler.js  
- config/plugins.json -> dynamic plugin loader at runtime

---

## Agent-Optimized Code Generation Policy (Critical)

- **Always start from root README.md, then recursively walk every folder**
- **For every file and folder:**
  - **If README.md, parse and follow its requirements before codegen**
  - **If code file, generate robust, real, production-level logic**
  - **If config, validate schema, defaults, and usage in code**
  - **If test, cover all edge cases and integration flows**
  - **If interface/ABI, align with Solidity/types in /types and /contracts**
  - **Never create empty placeholders, mocks, or stubs**—always generate real, working code or documented error/NotImplemented exceptions

---

## One-Click Unified Launch (Operator and Agent)

Use the quickstart scripts in `scripts/quickstart/`.

- Windows (PowerShell with Git Bash available): run `bash scripts/quickstart/start-dev.sh`
- macOS/Linux: run `./scripts/quickstart/start-dev.sh`

Supported OS: Windows (Git Bash/WSL or PowerShell + WSL), macOS/Linux (bash).

Notes:

- These scripts set up both Python and Node.js environments and start backend/frontend if configured.
- All logs and errors should print to the terminal and/or `data/logs/`.
- If a dependency is missing, the script should fail fast and print the remediation steps.

---

## AI Agent Self-Validation Protocol

Before, during, and after code generation:
Validate: All references, import paths, config keys, and model links

Lint: All generated JS/TS/Python code with appropriate tools

Test: Generate and run all unit/integration/fuzz/AI tests

Benchmark: Profile main loops, arbitrage simulation, and gas with /benchmarks scripts

Cross-check: README and code for feature/config drift, duplicate or missing files

---
Subsystem Ultra-Granular Map & Generation Cues

ai-modules/

README.md: Model list, feature pipeline, data schema, how to swap/upgrade

models/: All serialized weights, configs, training outputs; agents must create/fetch real files

features/: Isolated extractors; each must be independently testable

integration/: All external agent/LLM/FinGPT/webhook connectors

simulation/: Full trade sim stack; must run in fork/test mode

train/: All trainer scripts must support incremental learning + CLI params

tests/: All core modules must be 90%+ coverage

backend/

core/: Main event loop; enforce atomicity, rollback, plugin interface

plugins/: Each must declare dependencies and interfaces

adapters/: Contracts, DEXs, bridges, oracles; wire with types/ and third-party/

state/: In-memory, persistent, and recovery state

utils/: Must be used across core, plugins, and tests

tests/: Mirror core/ and plugins/ for regression, fuzz, and fork

dashboard/

pages/: UI pages, all with route-level README and test suite

components/: UI/UX elements, overlays, analytics, chart widgets, controls

api/: All backend bridge endpoints; must match backend API

settings/: All runtime plugin/config hot-swap

tests/: 90%+ coverage on all UI components

### contracts/ (if present)

README.md: List of all contracts, deployment guide, test references

interfaces/: All ABI/type links; must be validated by tests/

migrations/: All upgrade, rollback, fork, and deploy scripts

tests/: Full Hardhat/Ether.js test coverage

watchdog/

README.md: Coverage for every module, failure trigger, circuit breaker

killSwitch.js, autoRestart.js: Must be runtime tested (simulate stuck tx, error loop, gas spike, etc.)

config.json: All settings with schema, validation, and sample

data/

db/: All SQLite/NoSQL/JSON DBs

logs/: All logs with rolling history, crash recovery

backups/: Versioned, auto-rotating

---

Dashboard Usage Map (Agent and Operator)

All bot controls, logs, and plugins are accessible via the main dashboard at <http://localhost:3000>

Plugins, chains, strategies, and AI modes can be hot-swapped live via the UI

All runtime data (trades, profits, errors, alerts, test runs) stream in real-time and are exportable from dashboard

Dashboard widgets must auto-update via event/WS bridge, and all controls must trigger backend logic via API calls

---

## AI Agent/Operator Ultra-FAQ

Q: How do I run a single unified bot+UI session?

A:
Use scripts/quickstart/start-dev.sh (Windows via Git Bash/WSL: `bash scripts/quickstart/start-dev.sh`; macOS/Linux: `./scripts/quickstart/start-dev.sh`), or see operator-guide.md for manual backend + dashboard commands.

Q: How do I extend to new chains, DEXs, or flashloan pools?

A:

Add to config/ and implement new plugin/adapter in backend/plugins/ and contracts/interfaces/

Update ai-modules/ scoring logic if needed

Expose new configs via dashboard/plugin selector

Q: How do I retrain, replace, or evaluate an AI/ML model?

A:

Use ai-modules/train/ scripts and follow ai-modules/models/README.md for weight swapping

Validate all new weights in ai-modules/tests/ before rollout

Q: How do I export, backup, or audit all logs/results?

A:

Use node scripts/exportLogs.js or the dashboard Export feature

For DB backup, copy data/db/ and data/backups/

Q: What if a key or secret is compromised?

A:

Immediately trigger killSwitch in dashboard or watchdog/

Rotate key via dashboard/storage/ and re-inject at runtime (NEVER disk)

Q: How do I enable/disable advanced features (AI/Manual mode, ZK sim, speed mode)?

A:

Edit config/mode.json or toggle via dashboard "Mode" panel

---

Agent Self-Test, Error Handling, and Debugging Protocol

All agents must:

Output test and lint results to /logs/ after every generation run

Auto-scan for missing, duplicate, or broken files/folders after codegen

Suggest fixes and validate against all manifest/ files and project tree

If an error or incomplete state is detected, halt further generation and report to operator

---

## Security, Compliance & Recovery

RAM-only, encrypted key management—NO private key ever written to disk.

Circuit breakers, kill switches, auto-heal routines in watchdog/.

Audit, compliance, logs, and traceability built-in from day one.

Backup and recovery scripts in /scripts/ and /data/backups/.

---

## Final Build Sequence (Agent + Human)

1. Parse this README.md (root)

2. Recursively parse all per-folder README.md and config files

3. Generate production-grade, modular, tested code for every required file

4. Validate, lint, test, and output all logs/errors

5. Operator review: All changes must be documented, testable, and PR-reviewed

---

## Author

Name: Korukonda Pavan Kumar (Apex Creator)

Email: [pavan53732@gmail.com](mailto:pavan53732@gmail.com)


Version: 1.0.0

License: MIT

---

> Let the Apex Arbitrage Multichain Bot run. Fully autonomous, always evolving.
