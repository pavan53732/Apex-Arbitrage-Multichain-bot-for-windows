"""SECURITY-001: a behavioural root whose purpose/scope text mentions
security-sensitive concerns (credentials, secrets, signing, auth,
permission, sandbox, encryption) must declare explicit `## Security`
content -- a subsystem that talks about handling secrets/credentials
but has zero documented security controls is a genuine gap.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "SECURITY-001"
CATEGORY = "security"

SECURITY_SENSITIVE_KEYWORDS = [
    "credential", "secret", "signing", "sign ", "auth", "permission",
    "sandbox", "encrypt", "trust boundary", "threat model",
]


def _mentions_security_concern(doc: DocumentMetadata) -> bool:
    blob = " ".join([doc.purpose or "", doc.scope or ""]).lower()
    return any(kw in blob for kw in SECURITY_SENSITIVE_KEYWORDS)


def run(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    root_paths: set[str] | None = None,
) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    root_paths = root_paths or set()
    for d in docs:
        if d.path in root_paths and _mentions_security_concern(d) and not d.security:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=d.path,
                severity="MEDIUM",
                message="Purpose/scope mentions security-sensitive concerns but declares no explicit Security section",
                rule="SECURITY_SENSITIVE_ROOT_HAS_SECURITY_SECTION",
            ))
    return findings
