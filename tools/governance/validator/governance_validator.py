from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import networkx as nx
from ..metadata.models import DocumentMetadata

class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

@dataclass
class Finding:
    path: str
    severity: Severity
    message: str
    rule: str

class GovernanceValidator:
    def __init__(self, docs: list[DocumentMetadata], dependency_graph: nx.DiGraph):
        self.docs = docs
        self.graph = dependency_graph
        self.by_path = {d.path: d for d in docs}

    def validate_all(self) -> list[Finding]:
        findings: list[Finding] = []
        findings.extend(self._check_missing_owners())
        findings.extend(self._check_duplicate_owners())
        findings.extend(self._check_broken_references())
        findings.extend(self._check_cycles())
        return findings

    def _check_missing_owners(self) -> list[Finding]:
        findings = []
        for d in self.docs:
            if not d.owner:
                findings.append(Finding(path=d.path, severity=Severity.HIGH, message="Document has no owner", rule="OWNER_REQUIRED"))
        return findings

    def _check_duplicate_owners(self) -> list[Finding]:
        findings = []
        owner_map: dict[str, list[str]] = {}
        for d in self.docs:
            if not d.owner:
                continue
            owner_map.setdefault(d.owner, []).append(d.path)
        for owner, paths in owner_map.items():
            if len(paths) > 1:
                findings.append(Finding(path=paths[0], severity=Severity.HIGH, message=f"Owner {owner} assigned to multiple docs: {paths}", rule="UNIQUE_OWNER"))
        return findings

    def _check_broken_references(self) -> list[Finding]:
        findings = []
        for d in self.docs:
            for ref in d.depends_on + d.required_by + d.cross_references:
                if ref not in self.by_path:
                    findings.append(Finding(path=d.path, severity=Severity.MEDIUM, message=f"Reference to non-existent doc: {ref}", rule="BROKEN_REFERENCE"))
        return findings

    def _check_cycles(self) -> list[Finding]:
        findings = []
        try:
            cycles = list(nx.simple_cycles(self.graph))
        except nx.NetworkXError:
            cycles = []
        for cycle in cycles:
            findings.append(Finding(path=cycle[0], severity=Severity.CRITICAL, message=f"Dependency cycle detected: {cycle}", rule="NO_CYCLES"))
        return findings
