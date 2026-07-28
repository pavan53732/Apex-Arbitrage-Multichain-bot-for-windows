# APEX Repository Governance Platform

Independent Python engineering toolchain that turns the repository documentation into a
deterministic knowledge platform for autonomous AI agents.

## Install

```bash
pip install -e "tools/governance[dev]"
```

## CLI

```bash
apex-gov run                 # full intelligence pipeline
apex-gov index               # repository index only
apex-gov validate            # governance validators
apex-gov roots               # behavioural roots
apex-gov closure ROOT.md     # dependency closure
apex-gov completeness        # completeness scores
apex-gov blockers            # implementation blockers
apex-gov standardise         # metadata standardisation (Programme 2)
apex-gov graphs              # build knowledge graphs
apex-gov context ROOT.md     # AI context for subsystem
apex-gov search "query"      # semantic search
apex-gov metrics             # repository health metrics
apex-gov repair              # autonomous repair suggestions
apex-gov progress            # show GOVERNANCE-PROGRESS.json
```

## Architecture

- Language: Python 3.11+ (target 3.13)
- CLI: Typer
- Parser: markdown-it-py + PyYAML
- Graphs: NetworkX
- Storage: SQLite + JSON exports
- Config: YAML
- Tests: pytest
- Lint: Ruff + Black + mypy
- CI: GitHub Actions
