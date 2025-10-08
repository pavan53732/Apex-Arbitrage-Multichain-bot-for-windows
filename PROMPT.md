

# APEX WINDOWS FEATURE-MAPPING PROMPT (AI-OPTIMIZED)

Goal
Turn any idea or legacy component into a Windows-first feature spec that updates files under features/. Output must be deterministic, machine-parseable (JSON), and human-readable (Markdown).

Use
- Provide the “Your Input” block exactly as described.
- Select a Mode.
- The AI returns one JSON block + one Markdown spec that you can paste into the correct features/*.md files.

Modes
- spec-only: Produce the primary spec + secondary integration notes.
- spec-and-tasks: Spec + implementation tasks broken into 2–3 day chunks.
- delta-update: Update an existing spec; include a clear change log.
- quick-classify: Only return owner file and secondary refs with a 3-line rationale.

Allowed Owner Files (choose exactly one)
- install-dependencies.md
- config.md
- backend.md
- dashboard.md
- ai-modules.md
- docs.md
- contracts.md
- security.md
- testing.md
- deployment.md

Allowed Secondary Refs (choose any)
Same list as above.

Priority Scale
- P0: MVP-critical. Blocks release.
- P1: High value. Next immediately after MVP.
- P2: Important. Post-MVP.
- P3: Nice-to-have.

Windows Constraints (pick/set as needed)
- Runtime: Electron desktop, Node service, Python (optional), .NET (optional)
- Service: Windows Service (background), Tray App (foreground)
- Data: SQLite, rolling file logs, cache
- Storage: %AppData%/ApexArbitrage, %LocalAppData%, encrypted at rest (optional)
- Security: Windows Credential Manager, DPAPI, key redaction
- Networking: localhost only by default; operator-approved RPCs
- Packaging: Signed .exe, NSIS/Inno Setup, auto-update channel

Output Contract (always return JSON first, then Markdown)
1) JSON (strict schema below)
2) Markdown spec (paste-ready):
   - Primary Owner section content
   - Secondary integration notes sections
   - Tasks (if requested)
   - Change Log (for delta-update)

JSON Schema (strict)
{
  "ownerFile": "backend.md",
  "featureName": "Execution Batch Logging",
  "priority": "P0",
  "purpose": "Short purpose in one sentence.",
  "scope": { "in": [], "out": [] },
  "windowsImpl": {
    "runtime": ["Electron", "NodeService"],
    "service": "WindowsService|TrayApp|None",
    "data": ["SQLite", "FileLogs", "Cache"],
    "storage": { "dbPath": "%AppData%/ApexArbitrage/db", "logsPath": "%AppData%/ApexArbitrage/logs" },
    "security": ["Redaction", "DPAPI"],
    "performance": { "eventAppendMs": 2, "queryP95Ms": 50 }
  },
  "interfaces": {
    "apis": ["GET /health"],
    "events": [],
    "ipc": []
  },
  "dataModel": {
    "tables": [],
    "retentionDays": 30,
    "rotation": { "fileMaxMB": 100, "dailyRotate": true }
  },
  "errorHandling": [],
  "observability": {
    "metrics": [],
    "healthChecks": []
  },
  "acceptanceCriteria": [],
  "secondaryFiles": {
    "dashboard.md": [],
    "config.md": [],
    "testing.md": [],
    "security.md": [],
    "deployment.md": [],
    "docs.md": []
  },
  "dependencies": {
    "upstream": [],
    "downstream": []
  },
  "failureModes": [],
  "mitigations": [],
  "mode": "spec-only",
  "tasks": [],
  "changeLog": [],
  "extensions": {
    "lint": { "passed": true, "errors": [], "warnings": [] }
  }
}

Validation Rules (the AI must enforce)
- Reject if ownerFile not in allowed list.
- Reject if priority not in {P0,P1,P2,P3}.
- Require at least one of windowsImpl.runtime or windowsImpl.service.
- Never reference legacy paths; Windows-first only.
- No external links.
- Security: must include at least “Redaction” in security for any logging or credential-related feature.
- Acceptance criteria must be measurable (numbers, durations, thresholds).
- Secondary file keys must be a subset of the allowed files.
- If mode = spec-and-tasks → tasks[] must have 2–6 items with estimates.
- If mode = delta-update → changeLog[] required with date, change, reason, impact.

Your Input (fill and send as-is)

APEX WINDOWS FEATURE MAPPING REQUEST

mode: spec-only | spec-and-tasks | delta-update | quick-classify

Component
- Name:
- Type: Feature | Subsystem | Adapter | Service | UI | Config | Doc
- Original purpose (if any):
- Priority: P0 | P1 | P2 | P3

Ownership
- Primary owner file (one of the allowed list):
- Secondary files (any of the allowed list):

Windows Constraints
- Runtime (choose): Electron | NodeService | Python | .NET
- Service: WindowsService | TrayApp | None
- Data: SQLite | FileLogs | Cache
- Storage: desired base path (default %AppData%/ApexArbitrage)
- Security: CredentialManager | DPAPI | Redaction | AtRestEncryption
- Performance target: [e.g., append <= 2ms; p95 query <= 50ms]

Interfaces (if known)
- APIs:
- Events:
- IPC:

Data Model (if known)
- Tables/files:
- Retention/rotation:

Acceptance (Definition of Done)
- List 3–6 measurable criteria

Dependencies
- Upstream:
- Downstream:

Risks
- List major risks and mitigations

Style Rules (for all AI)
- Start with JSON block exactly matching the schema, then Markdown spec.
- No external links. No screenshots. No legacy paths.
- Use simple, directive language. Avoid fluff.
- Keep sections in a fixed order so they’re easy to diff.
- Do not invent features outside the owner/secondary files list.

Change Management
- For delta-update mode, include a “changeLog” with dated entries and impact tags (Spec|Config|API|Data).
- Preserve field names; add new fields only under the “extensions” key.

Security Defaults
- Never log private keys or seed phrases.
- Mask API tokens by default.
- Local-only endpoints unless explicitly requested.

Minimal Lint Checklist (AI MUST RUN BEFORE RETURNING OUTPUT)
- Owner file is in allowed list.
- Priority is P0/P1/P2/P3.
- windowsImpl includes runtime or service (or both).
- If feature touches logging, credentials, wallets, or RPC keys → windowsImpl.security contains “Redaction”.
- acceptanceCriteria has 3–10 items, each measurable (contains a number or quantifiable threshold).
- No legacy paths (e.g., backend/, contracts/ from old repo) appear anywhere.
- No external links present.
- secondaryFiles keys are a subset of the allowed files; values are short bullet items.
- dataModel.retentionDays is an integer; rotation.fileMaxMB is a number.
- If mode = spec-and-tasks → tasks count 2–6, each with estimateDays.
- If mode = delta-update → changeLog has at least 1 entry with date, change, reason, impact.
- Add extensions.lint with passed true/false and any errors/warnings.

Worked Examples

Example A — Installer Bootstrap (install-dependencies.md, P0, spec-and-tasks)
Your Input
mode: spec-and-tasks

Component
- Name: Installer Bootstrap
- Type: Feature
- Original purpose (if any): One-click Windows installer with runtime checks
- Priority: P0

Ownership
- Primary owner file: install-dependencies.md
- Secondary files: deployment.md, security.md, docs.md, testing.md

Windows Constraints
- Runtime: Electron
- Service: WindowsService
- Data: SQLite
- Storage: %AppData%/ApexArbitrage
- Security: DPAPI, Redaction
- Performance target: Install < 2 minutes on typical hardware

Interfaces
- APIs: GET /health (post-install validation)
- Events: install.started, install.completed, install.failed
- IPC: n/a

Data Model
- Tables/files: installer logs (rolling), config bootstrap file
- Retention/rotation: retain last 5 installer logs

Acceptance
- Signed .exe installer runs offline; verifies runtimes; configures folders; creates shortcut; optional service registration; uninstall cleans up.

Dependencies
- Upstream: code-signing certificates
- Downstream: backend service, dashboard app

Risks
- AV false positives; incomplete uninstalls
- Mitigations: code signing, clean uninstall scripts, clear rollback

Expected Output Summary
- ownerFile: install-dependencies.md
- Secondary integration notes for deployment.md (packaging pipeline), security.md (signing and DPAPI), docs.md (install guide), testing.md (silent install tests).
- Tasks: author NSIS/Inno scripts, sign build, silent install test, uninstall validation.

Example B — Config Engine (config.md, P0, spec-only)
Your Input
mode: spec-only

Component
- Name: Config Engine (Typed + Safe)
- Type: Feature
- Original purpose (if any): Centralized app configuration with validation and safe persistence
- Priority: P0

Ownership
- Primary owner file: config.md
- Secondary files: backend.md, dashboard.md, security.md, testing.md, docs.md, deployment.md

Windows Constraints
- Runtime: NodeService, Electron
- Service: WindowsService
- Data: SQLite, FileLogs
- Storage: %AppData%/ApexArbitrage
- Security: DPAPI, Redaction
- Performance target: Load/validate < 100 ms; hot-reload-safe updates

Interfaces
- APIs: GET /config, PUT /config (validated)
- Events: config.changed
- IPC: subscribe to config updates

Data Model
- Tables/files: config.json (encrypted fields), schema.json
- Retention/rotation: versioned backups (last 5)

Acceptance
- Typed schema with validation; defaults applied; secure persistence of secrets; rollback to last good config; audit of changes.

Expected Output Summary
- ownerFile: config.md
- Secondary notes for backend.md (read-only cache + hot-reload edges), dashboard.md (UI editor with validation), security.md (fields encrypted via DPAPI), testing.md (schema validation tests), deployment.md (migrate on update), docs.md (operator guide).

Example C — Dashboard Shell (dashboard.md, P0, spec-and-tasks)
Your Input
mode: spec-and-tasks

Component
- Name: Dashboard Shell + Streams
- Type: UI
- Original purpose (if any): Operator UI, real-time status, start/stop control
- Priority: P0

Ownership
- Primary owner file: dashboard.md
- Secondary files: backend.md, testing.md, security.md, docs.md

Windows Constraints
- Runtime: Electron
- Service: TrayApp
- Data: Cache
- Storage: %AppData%/ApexArbitrage
- Security: Redaction
- Performance target: Connect to backend < 1s; live widgets update p95 < 200 ms

Interfaces
- APIs: GET /health, GET /metrics
- Events: status.changed, alert.raised
- IPC: ws://localhost:PORT/stream

Data Model
- Tables/files: UI state cache (in-memory or local storage)
- Retention/rotation: n/a

Acceptance
- App shell with connectivity check; start/stop controls; live metrics widget; alert banner; tray icon; graceful reconnection.

Expected Output Summary
- ownerFile: dashboard.md
- Secondary notes for backend.md (health, metrics, start/stop endpoints), testing.md (UI smoke/e2e, offline simulation), security.md (mask sensitive values), docs.md (operator walkthrough).
- Tasks: shell scaffolding, connectivity & reconnection, core widgets, tray integration, e2e smoke tests.

Response Contract (what you’ll get back every time)
- One JSON “feature spec” conforming to the schema (with extensions.lint results).
- One Markdown spec ready to paste into the owner and secondary files.
- Clear Windows implementation details, dependencies, risks, and acceptance criteria.
- Tasks and/or change log sections when requested by mode.

