---
type: ADR
owner: Governance Platform
status: Accepted
version: 1.0.0
purpose: WS0 refactored to verification layer; canonical runtime consolidated.
canonical_source: .governance/programme_2.5/phase_0.75/adr_0011_ws0_verification_layer.md
---

# ADR-0011: WS0 Refactored to Governance Verification Layer

## Decision

WS0 (Workstream 0) is refactored from a governance execution engine into a **Governance Verification Layer**. 

All governance computation originates EXCLUSIVELY from the canonical runtime at `tools/governance/`. 

WS0 now ONLY performs:
- Verification of canonical outputs
- Evidence collection from canonical outputs
- Regression checking across canonical executions
- Certification packaging of canonical evidence
- Reporting on canonical governance state

WS0 NEVER performs:
- Repository indexing
- Metadata parsing
- Reference parsing
- Root detection
- Graph construction
- Closure generation
- Validation
- Metrics computation
- Integrity computation
- Freeze computation
- Evidence generation (from scratch)

## Rationale

Prior to this change, WS0 contained duplicate governance runtime logic:
- `test_harness.py` - independent test execution engine
- `loader/fixture_loader.py` - repository fixture loading with root detection
- `generator/golden_generator.py` - synthetic governance output generation
- `comparator/golden_comparator.py` - output comparison logic
- `dashboard/test_dashboard.py` - test result dashboard

These modules independently computed governance state (root detection, document counting, graph generation, metrics), creating a second execution path that diverged from the canonical runtime.

This violated the architectural rule: **exactly one executable governance runtime exists at `tools/governance/`**.

## Consequences

### Removed (Category A - Executable Runtime)
- `.governance/programme_2.5/ws0/test_harness.py`
- `.governance/programme_2.5/ws0/loader/`
- `.governance/programme_2.5/ws0/generator/`
- `.governance/programme_2.5/ws0/comparator/`
- `.governance/programme_2.5/ws0/dashboard/`
- `.governance/programme_2.5/ws0/tests/` (tests for deleted runtime)

### Preserved (Category C - Evidence)
- `.governance/programme_2.5/ws0/ws0_certification_report.json`
- `.governance/programme_2.5/ws0/ws0_certification_package.json`
- `.governance/programme_2.5/ws0/reports/*.json` (all evidence reports)

### Preserved (Category D - Specifications)
- This ADR and related Programme 2.5 architecture documents

### Added (Category B - Verification Wrapper)
- `.governance/programme_2.5/ws0/__init__.py` - `WS0VerificationLayer` class that invokes `tools/governance/cli/main.py`

## Single Execution Pipeline

After this change, there is exactly one governance execution path:

```
Repository
    ↓
Indexer (tools/governance/indexer/repo_indexer.py)
    ↓
Parser (tools/governance/parser/markdown_parser.py)
    ↓
Reference Parser (tools/governance/references/reference_parser.py)
    ↓
Root Detection (tools/governance/closure/orchestrator.py → BehaviouralRootDetector)
    ↓
Closure Engine (tools/governance/closure/closure_engine.py)
    ↓
Validators (tools/governance/validator/governance_validator.py)
    ↓
Metrics (tools/governance/metrics/metrics_engine.py)
    ↓
Evidence (tools/governance/storage/json_export.py)
    ↓
Freeze (tools/governance/freeze/manager.py)
    ↓
Integrity (tools/governance/metrics/metrics_engine.py)
    ↓
Outputs
```

Every governance command traverses this pipeline exclusively through `tools/governance/cli/main.py`.

## Verification

WS0 verification layer invokes the canonical runtime via:
```python
subprocess.run(["python", "-m", "tools.governance.cli.main", "run"], ...)
```

This ensures WS0 can never diverge from canonical governance state.

## Migration Path

Future workstreams (WS1+) MUST:
1. Invoke `tools/governance/` for any governance computation
2. NOT implement independent governance logic
3. Consume canonical outputs for verification/certification only

## Acceptance Criteria

- ✓ Exactly one governance runtime exists (`tools/governance/`)
- ✓ All governance computation originates from `tools/governance/`
- ✓ WS0 contains no independent runtime logic
- ✓ WS0 contains only verification, certification, reporting, and evidence
- ✓ Historical evidence remains intact
- ✓ No duplicate governance computation exists anywhere in repository
- ✓ No placeholder or synthetic execution paths remain
- ✓ Documentation reflects new architecture
- ✓ Repository passes integrity validation using canonical runtime