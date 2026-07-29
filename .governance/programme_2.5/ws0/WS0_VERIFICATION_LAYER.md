---
type: REFERENCE
owner: Governance Platform
status: Canonical
version: 1.0.0
purpose: WS0 Verification Layer architecture and usage.
scope: WS0 workstream documentation.
canonical_source: .governance/programme_2.5/ws0/WS0_VERIFICATION_LAYER.md
---

# WS0 - Governance Verification Layer

## Overview

WS0 is **NOT a governance runtime**. It is a **verification layer** that consumes canonical governance outputs from `tools/governance/`.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CANONICAL GOVERNANCE RUNTIME                  │
│                        tools/governance/                           │
│  ┌─────────────┐ ┌────────┐ ┌─────────┐ ┌────────┐ ┌──────────┐ │
│  │   Indexer   │ │ Parser │ │Ref Parse│ │ Roots  │ │ Closure  │ │
│  └──────┬──────┘ └────┬───┘ └────┬────┘ └────┬───┘ └────┬─────┘ │
│         │             │           │           │           │     │
│         ▼             ▼           ▼           ▼           ▼     │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              VALIDATORS → METRICS → EVIDENCE → FREEZE        │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────┬──────────────────────────────────┘
                               │ CANONICAL OUTPUTS
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      WS0 VERIFICATION LAYER                      │
│                  .governance/programme_2.5/ws0/                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────┐ ┌────────────┐  │
│  │ Verification │ │   Evidence   │ │Regression│ │Certification│ │
│  └──────────────┘ └──────────────┘ └──────────┘ └────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## WS0 Responsibilities

| Layer | Responsibility | Implementation |
|-------|----------------|----------------|
| **Verification** | Validate canonical output integrity, schema compliance, hash consistency | `WS0VerificationLayer.verify_canonical_output()` |
| **Evidence Collection** | Aggregate canonical outputs, graphs, freeze records into evidence packages | `WS0VerificationLayer.collect_evidence()` |
| **Regression Checking** | Compare canonical outputs across executions for regressions | `WS0VerificationLayer.run_regression_check()` |
| **Certification** | Package evidence and verification results into certification packages | `WS0VerificationLayer.generate_certification_package()` |
| **Reporting** | Generate verification, evidence, and certification reports | `WS0VerificationLayer.save_report()` |

## What WS0 Does NOT Do

WS0 **never** performs:
- ❌ Repository indexing
- ❌ Metadata parsing  
- ❌ Reference parsing
- ❌ Root detection
- ❌ Graph construction
- ❌ Closure generation
- ❌ Validation
- ❌ Metrics computation
- ❌ Integrity computation
- ❌ Freeze computation
- ❌ Evidence generation (from scratch)

All above are **exclusive** to `tools/governance/`.

## Usage

### CLI Commands

```bash
# Run canonical governance pipeline and verify output
python -m .governance.programme_2.5.ws0 verify [--repo-root PATH] [--config CONFIG]

# Collect evidence from canonical outputs
python -m .governance.programme_2.5.ws0 evidence [--repo-root PATH] [--config CONFIG]

# Generate WS0 certification package
python -m .governance.programme_2.5.ws0 certify [--repo-root PATH] [--config CONFIG]

# Run regression check against baseline
python -m .governance.programme_2.5.ws0 regress --baseline baseline.json [--repo-root PATH]

# Run canonical pipeline directly (bypasses WS0 verification)
python -m tools.governance.cli.main run
```

### Programmatic Usage

```python
from pathlib import Path
from .governance.programme_2_5.ws0 import WS0VerificationLayer

ws0 = WS0VerificationLayer(Path("."))

# Run full verification
output = ws0.run_full_pipeline()
verification = ws0.verify_canonical_output(output["output"])
evidence = ws0.collect_evidence(output["output"])
regression = ws0.run_regression_check(output["output"], baseline_output)
certification = ws0.generate_certification_package(verification, evidence, regression)
```

## Canonical Runtime Integration

WS0 invokes the canonical runtime exclusively through its CLI:

```python
subprocess.run([
    "python", "-m", "tools.governance.cli.main", "run"
], cwd=repo_root, capture_output=True, text=True)
```

This ensures:
- Single source of truth for governance state
- No divergence between WS0 and canonical runtime
- WS0 automatically benefits from canonical runtime improvements

## Evidence Preservation

All historical evidence is preserved in `.governance/programme_2.5/ws0/reports/`:
- `determinism_report.json` - 100-run determinism verification
- `fresh_clone_report.json` - Fresh clone validation
- `corruption_report.json` - Corruption detection results
- `stress_report.json` - Stress test results
- `fuzz_report.json` - Fuzz testing results
- `evidence_report.json` - Aggregated evidence
- `dashboard.json` - Historical test dashboard

Certification records:
- `ws0_certification_report.json` - Full certification audit
- `ws0_certification_package.json` - Certification package

## Related Documents

- ADR-0011: WS0 Refactored to Governance Verification Layer
- ADR-0010: Governance Platform as Standalone Product
- ADR-0009: Governance Platform Architecture Freeze
- `tools/governance/README.md` - Canonical runtime documentation