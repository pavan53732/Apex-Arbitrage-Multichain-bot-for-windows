"""Fixture-repository harness for validator tests.

The validators operate on a repository, not on isolated inputs, so testing them
in isolation requires building a repository. This module constructs minimal but
structurally valid repositories in a temporary directory, which tests then
mutate to create the specific defect under test.

The approach is deliberate. Asserting a validator's behaviour against the real
repository would couple the tests to the corpus: every document added would
risk breaking them, and a validator could pass simply because the corpus
happens to be clean. A purpose-built fixture makes each test state exactly the
condition it exercises.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

import pytest

# The validators are imported as top-level modules, matching how runner.py
# loads them, so the package root must be importable.
VALIDATORS_ROOT = Path(__file__).resolve().parent.parent
if str(VALIDATORS_ROOT) not in sys.path:
    sys.path.insert(0, str(VALIDATORS_ROOT))

from validator_sdk import (  # noqa: E402  (path set above)
    MarkdownDiscovery,
    RegistryLoader,
    ValidationContext,
    ValidatorConfig,
)

DOCUMENT_REGISTRY_HEADER = (
    "| Document ID | Path | Title | Plane | Domain | Class | Authority | Status | "
    "Owner | Version | Concept Role | Canonical Source | Related Concepts | "
    "Dependencies | Consumers | Supersedes | Superseded By |"
)
DOCUMENT_REGISTRY_SEPARATOR = "| --- " * 17 + "|"

CONCEPT_REGISTRY_HEADER = (
    "| Concept ID | Concept Code | Concept Type | Concept Name | "
    "Canonical Concept ID | Canonical Document ID | Canonical Path | Plane | "
    "Domain | Status | Related Documents | Notes |"
)
CONCEPT_REGISTRY_SEPARATOR = "| --- " * 12 + "|"

# The loader keys on this exact header text.
TRACEABILITY_HEADER = (
    "| Traceability ID | Source ID | Relationship | Target ID | Status | Notes |"
)
TRACEABILITY_SEPARATOR = "| --- " * 6 + "|"

# The three registries are themselves tracked documents.
_REGISTRY_DOCS = (
    ("DOC-9001", "Document Registry", "DOCUMENT-REGISTRY.md"),
    ("DOC-9002", "Concept Registry", "CONCEPT-REGISTRY.md"),
    ("DOC-9003", "Traceability Registry", "TRACEABILITY-REGISTRY.md"),
    ("DOC-9005", "Glossary", "GLOSSARY.md"),
)

# The documentation map is tracked too, but lives outside registries/.
_MAP_DOC = (
    "DOC-9004",
    "Documentation Map",
    "docs/apex-repository-docs/documentation-lifecycle/documentation-map.md",
)


@dataclass
class DocSpec:
    """A document to place into a fixture repository.

    Defaults describe a well-formed canonical specification, so a test only
    states the fields relevant to the defect it is exercising.
    """

    doc_id: str
    path: str
    title: str = "Test Document"
    plane: str = "Product Specification"
    domain: str = "Runtime"
    class_: str = "Specification"
    authority: str = "Canonical"
    status: str = "Active"
    owner: str = "Runtime Team"
    version: str = "1.0.0"
    concept_role: str = "Owner"
    concept_id: str | None = None
    dependencies: list[str] = field(default_factory=list)
    consumers: list[str] = field(default_factory=list)
    body: str | None = None
    register: bool = True
    frontmatter_overrides: dict[str, str] = field(default_factory=dict)
    omit_fields: tuple[str, ...] = ()

    @property
    def concept(self) -> str:
        return self.concept_id or f"CONCEPT-{self.doc_id.split('-')[1]}"


def _yaml_list(name: str, values: list[str]) -> str:
    if not values:
        return f"{name}: []"
    lines = [f"{name}:"] + [f"  - {v}" for v in values]
    return "\n".join(lines)


def _default_body(spec: DocSpec) -> str:
    """A body satisfying the completeness and state-machine validators.

    Keeps unrelated validators quiet so a test failure points at the defect
    under test rather than at incidental noise.
    """
    return f"""
# {spec.title}

## Purpose
Fixture document for validator testing.

## Scope
Validator test fixtures only.

## State Machine
```mermaid
stateDiagram-v2
  [*] --> IDLE
  IDLE --> ACTIVE
  ACTIVE --> [*]
```

## Failure Handling
Fixture documents do not fail.

## Cross-references
- None.
"""


class FixtureRepo:
    """A temporary repository the validators can run against."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.docs: list[DocSpec] = []
        (root / "docs" / "apex-repository-docs" / "registries").mkdir(parents=True, exist_ok=True)
        (root / "docs" / "apex-app-docs").mkdir(parents=True, exist_ok=True)
        (root / "validators").mkdir(parents=True, exist_ok=True)
        self._write_config()

    def _write_config(self) -> None:
        (self.root / ".validator-config.yaml").write_text(
            "metadata_schema_version: \"1.0\"\n"
            "repository_root: \".\"\n"
            "registries_dir: \"docs/apex-repository-docs/registries\"\n"
            "ignored_paths:\n  - \".git\"\n  - \"__pycache__\"\n"
            "ignored_files:\n  - \"README.md\"\n"
            "ignored_patterns: []\n"
            "max_file_size_mb: 10\n"
            "validator_timeout_seconds: 30\n"
            "validators: {}\n",
            encoding="utf-8",
        )

    def add(self, spec: DocSpec) -> "FixtureRepo":
        self.docs.append(spec)
        return self

    def add_doc(self, doc_id: str, path: str, **kwargs: object) -> "FixtureRepo":
        return self.add(DocSpec(doc_id=doc_id, path=path, **kwargs))  # type: ignore[arg-type]

    def write(self) -> "FixtureRepo":
        """Materialise every document and registry onto disk."""
        for spec in self.docs:
            self._write_doc(spec)
        self._write_document_registry()
        self._write_concept_registry()
        self._write_traceability_registry()
        self._write_documentation_map()
        self._write_domain_readmes()
        self._write_glossary()
        return self

    def _write_glossary(self) -> None:
        """Write the glossary the terminology validator reads.

        Its absence disables VAL-011 entirely, so the fixture would exercise
        nothing. Six columns, matching the real registry schema.
        """
        target = self._registry_path("GLOSSARY.md")
        rows = self._registry_frontmatter(
            "DOC-9005", "Glossary", "GLOSSARY.md"
        ) + [
            "# Glossary",
            "",
            "| Term ID | Term | Canonical Definition | Concept ID | Domain | Related Terms |",
            "| --- | --- | --- | --- | --- | --- |",
            "| TERM-0001 | Orchestrator | The central runtime coordinator | CONCEPT-0001 | Runtime | coordinator |",
            "| TERM-0002 | Worker Pool | A managed set of execution workers | CONCEPT-0002 | Runtime | worker |",
        ]
        target.write_text("\n".join(rows) + "\n", encoding="utf-8")

    def _write_domain_readmes(self) -> None:
        """Write the domain README each plane root requires.

        The orphan detector treats a domain folder without a README as an
        error, so their absence would fail every fixture for a reason no test
        is exercising. READMEs are excluded from discovery by config, so these
        are navigation surfaces only.
        """
        for domain in ("apex-app-docs", "apex-repository-docs"):
            target = self.root / "docs" / domain / "README.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            concepts = [
                d.concept for d in self.docs
                if d.register and d.concept_role == "Owner"
            ]
            lines = [f"# {domain}", "", "## Canonical owner map", ""]
            lines += [f"- {c}" for c in concepts]
            target.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def _write_documentation_map(self) -> None:
        """Write the reachability surface the orphan detector reads.

        Without it every canonical document is unreachable, so the fixture
        would fail orphan detection for a reason unrelated to any test.
        """
        target = (
            self.root / "docs" / "apex-repository-docs"
            / "documentation-lifecycle" / "documentation-map.md"
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        rows = self._registry_frontmatter(
            "DOC-9004",
            "Documentation Map",
            "documentation-map.md",
            domain="Documentation Lifecycle",
            class_="Index",
            canonical_source=_MAP_DOC[2],
        ) + ["# Documentation Map", "", "## Registered Document Reachability", ""]
        reachable = [d.doc_id for d in self.docs if d.register]
        reachable += [rid for rid, _, _ in _REGISTRY_DOCS] + ["DOC-9004"]
        rows += [f"- `{doc_id}`" for doc_id in reachable]
        rows += ["", "## Concept Reachability", ""]
        rows += [
            f"- `{d.concept}`"
            for d in self.docs
            if d.register and d.concept_role == "Owner"
        ]
        target.write_text("\n".join(rows) + "\n", encoding="utf-8")

    def _write_doc(self, spec: DocSpec) -> None:
        target = self.root / spec.path
        target.parent.mkdir(parents=True, exist_ok=True)

        fields: dict[str, str] = {
            "metadata_schema_version": "1.0",
            "document_id": spec.doc_id,
            "title": spec.title,
            "plane": spec.plane,
            "domain": spec.domain,
            "class": spec.class_,
            "authority": spec.authority,
            "status": spec.status,
            "owner": spec.owner,
            "version": spec.version,
            "canonical_source": spec.path,
            "related_concepts": _yaml_list("related_concepts", [spec.concept]),
            "dependencies": _yaml_list("dependencies", spec.dependencies),
            "consumers": _yaml_list("consumers", spec.consumers),
            "validator_coverage": "validator_coverage: []",
            "supersedes": "supersedes: []",
            "superseded_by": "superseded_by: []",
            "last_updated": "2026-08-02",
            "concept_role": spec.concept_role,
            "owned_domains": _yaml_list(
                "owned_domains", [spec.domain] if spec.concept_role == "Owner" else []
            ),
        }
        fields.update(spec.frontmatter_overrides)

        lines = ["---"]
        for key, value in fields.items():
            if key in spec.omit_fields:
                continue
            lines.append(value if value.startswith(f"{key}:") else f"{key}: {value}")
        lines.append("---")

        body = spec.body if spec.body is not None else _default_body(spec)
        target.write_text("\n".join(lines) + "\n" + body, encoding="utf-8")

    @staticmethod
    def _registry_frontmatter(
        doc_id: str,
        title: str,
        filename: str,
        *,
        domain: str = "Registries",
        class_: str = "Registry",
        canonical_source: str | None = None,
    ) -> list[str]:
        """Frontmatter for a registry file.

        The registries are themselves tracked documents, so they must carry
        valid metadata or the metadata validator reports them as defects the
        test never intended to create.
        """
        return [
            "---",
            "metadata_schema_version: 1.0",
            f"document_id: {doc_id}",
            f"title: {title}",
            "plane: Repository Operating Model",
            f"domain: {domain}",
            f"class: {class_}",
            "authority: Canonical",
            "status: Active",
            "owner: Runtime Team",
            "version: 1.0.0",
            f"canonical_source: "
            f"{canonical_source or f'docs/apex-repository-docs/registries/{filename}'}",
            "related_concepts: []",
            "dependencies: []",
            "consumers: []",
            "validator_coverage: []",
            "supersedes: []",
            "superseded_by: []",
            "last_updated: 2026-08-02",
            "concept_role: Index",
            "owned_domains: []",
            "---",
            "",
        ]

    def _write_document_registry(self) -> None:
        rows = self._registry_frontmatter(
            "DOC-9001", "Document Registry", "DOCUMENT-REGISTRY.md"
        ) + [
            "# Document Registry",
            "",
            DOCUMENT_REGISTRY_HEADER,
            DOCUMENT_REGISTRY_SEPARATOR,
        ]
        # The registries are tracked documents and must appear in the registry
        # they define, or cross-reference validation reports them as unknown.
        for reg_id, reg_title, reg_file in _REGISTRY_DOCS:
            rows.append(
                f"| {reg_id} | docs/apex-repository-docs/registries/{reg_file} | "
                f"{reg_title} | Repository Operating Model | Registries | Registry | "
                f"Canonical | Active | Runtime Team | 1.0.0 | Index | "
                f"docs/apex-repository-docs/registries/{reg_file} |  |  |  |  |  |"
            )
        map_id, map_title, map_path = _MAP_DOC
        rows.append(
            f"| {map_id} | {map_path} | {map_title} | Repository Operating Model | "
            f"Documentation Lifecycle | Index | Canonical | Active | Runtime Team | "
            f"1.0.0 | Index | {map_path} |  |  |  |  |  |"
        )
        for spec in self.docs:
            if not spec.register:
                continue
            rows.append(
                f"| {spec.doc_id} | {spec.path} | {spec.title} | {spec.plane} | "
                f"{spec.domain} | {spec.class_} | {spec.authority} | {spec.status} | "
                f"{spec.owner} | {spec.version} | {spec.concept_role} | {spec.path} | "
                f"{spec.concept} | {', '.join(spec.dependencies)} | "
                f"{', '.join(spec.consumers)} |  |  |"
            )
        self._registry_path("DOCUMENT-REGISTRY.md").write_text(
            "\n".join(rows) + "\n", encoding="utf-8"
        )

    def _write_concept_registry(self) -> None:
        rows = self._registry_frontmatter(
            "DOC-9002", "Concept Registry", "CONCEPT-REGISTRY.md"
        ) + ["# Concept Registry", "", CONCEPT_REGISTRY_HEADER, CONCEPT_REGISTRY_SEPARATOR]
        for spec in self.docs:
            if not spec.register or spec.concept_role != "Owner":
                continue
            rows.append(
                f"| {spec.concept} | CODE-{spec.doc_id.split('-')[1]} | Semantic | "
                f"{spec.title} | {spec.concept} | {spec.doc_id} | {spec.path} | "
                f"{spec.plane} | {spec.domain} | Active | {spec.doc_id} | Canonical owner |"
            )
        self._registry_path("CONCEPT-REGISTRY.md").write_text(
            "\n".join(rows) + "\n", encoding="utf-8"
        )

    def _write_traceability_registry(self) -> None:
        rows = self._registry_frontmatter(
            "DOC-9003", "Traceability Registry", "TRACEABILITY-REGISTRY.md"
        ) + ["# Traceability Registry", "", TRACEABILITY_HEADER, TRACEABILITY_SEPARATOR]
        for index, spec in enumerate(self.docs, start=1):
            if not spec.register or spec.concept_role != "Owner":
                continue
            rows.append(
                f"| TRACE-{index:04d} | {spec.doc_id} | Defines | {spec.concept} | "
                f"Active | Canonical document owner for active concept. |"
            )
        self._registry_path("TRACEABILITY-REGISTRY.md").write_text(
            "\n".join(rows) + "\n", encoding="utf-8"
        )

    def _registry_path(self, name: str) -> Path:
        return self.root / "docs" / "apex-repository-docs" / "registries" / name

    def edit(self, path: str, transform) -> "FixtureRepo":
        """Rewrite a file through `transform`, for introducing defects."""
        target = self.root / path
        target.write_text(transform(target.read_text(encoding="utf-8")), encoding="utf-8")
        return self

    def context(self) -> ValidationContext:
        """Build a ValidationContext over this fixture, as the runner would."""
        config = ValidatorConfig.load(self.root)
        concepts, documents, traces = RegistryLoader.load_all(self.root)
        return ValidationContext(
            repository_root=self.root,
            changed_files=[],
            all_markdown_files=MarkdownDiscovery.find_all(self.root, config),
            concept_registry=concepts,
            document_registry=documents,
            traceability_registry=traces,
            config=config,
            previous_results=[],
        )

    def run(self, validator_id: str):
        """Run one validator against this fixture and return its result."""
        from runner import ValidatorRunner

        module_name = ValidatorRunner.VALIDATOR_MODULES[validator_id]
        module = __import__(module_name)
        config = ValidatorConfig.load(self.root)
        validator = module.Validator(config)
        return validator.validate(self.context())


ADR_BODY = """
# ADR 0001 Fixture Decision

## Status
Accepted.

## Context
A fixture ADR so ADR consistency validation has an input.

## Decision
Use fixture repositories for validator tests.

## Consequences
Validator behaviour becomes verifiable in isolation.

## Affected Components
- `DOC-0001`

## Cross-references
- `../../runtime/orchestrator.md`
"""


@pytest.fixture
def repo(tmp_path: Path) -> FixtureRepo:
    """An empty fixture repository rooted in a temporary directory."""
    return FixtureRepo(tmp_path)


@pytest.fixture
def healthy_repo(tmp_path: Path) -> FixtureRepo:
    """A structurally valid repository that every validator should accept.

    Tests derive defects from this baseline, so a failure indicates the defect
    rather than an unrelated shortcoming in the fixture.
    """
    return (
        FixtureRepo(tmp_path)
        .add_doc(
            "DOC-0001",
            "docs/apex-app-docs/runtime/orchestrator.md",
            title="Orchestrator",
            domain="Runtime",
        )
        .add_doc(
            "DOC-0002",
            "docs/apex-app-docs/runtime/worker-pool.md",
            title="Worker Pool",
            domain="Runtime",
            dependencies=["DOC-0001"],
        )
        .add_doc(
            # An ADR, so the ADR consistency validator has something to inspect.
            "DOC-0003",
            "docs/apex-app-docs/architecture/decisions/0001-fixture-decision.md",
            title="ADR 0001 Fixture Decision",
            domain="Architecture",
            class_="ADR",
            consumers=["DOC-0001"],
            body=ADR_BODY,
        )
        .write()
    )


def codes(result) -> set[str]:
    """Error codes emitted by a result, as plain strings."""
    return {str(getattr(e.code, "value", e.code)) for e in result.errors}


def warning_codes(result) -> set[str]:
    return {str(getattr(w.code, "value", w.code)) for w in result.warnings}
