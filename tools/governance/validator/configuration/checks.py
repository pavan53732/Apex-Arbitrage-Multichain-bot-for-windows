"""CONFIG-001: every configuration key referenced by more than one
document must be referenced consistently -- specifically, this
validator flags configuration keys that appear to be near-duplicates
(same key differing only by case or separator style, e.g. `RPC_TIMEOUT`
vs `rpc-timeout` vs `rpc.timeout`), which is a common source of runtime
configuration bugs (two subsystems believing they read/write the same
setting when the actual keys differ).
"""
from __future__ import annotations

import re

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "CONFIG-001"
CATEGORY = "configuration"


def _canonical_key(key: str) -> str:
    """Normalise a configuration key for near-duplicate comparison:
    lowercase, strip surrounding backticks/whitespace, collapse
    separators (-, _, .) to a single delimiter."""
    k = key.strip().strip("`").lower()
    k = re.sub(r"[-_.]+", "_", k)
    return k


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    variants_by_canonical: dict[str, set[str]] = {}
    owners_by_canonical: dict[str, set[str]] = {}

    for d in docs:
        for cfg_key in d.configuration:
            canonical = _canonical_key(cfg_key)
            variants_by_canonical.setdefault(canonical, set()).add(cfg_key.strip().strip("`"))
            owners_by_canonical.setdefault(canonical, set()).add(d.path)

    for canonical, variants in variants_by_canonical.items():
        if len(variants) > 1:
            for path in sorted(owners_by_canonical[canonical]):
                findings.append(CategoryFinding(
                    validator_id=VALIDATOR_ID,
                    path=path,
                    severity="LOW",
                    message=f"Configuration key has {len(variants)} inconsistent spelling variants across the corpus: {sorted(variants)}",
                    rule="CONFIG_KEY_SPELLING_CONSISTENT",
                ))
    return findings
