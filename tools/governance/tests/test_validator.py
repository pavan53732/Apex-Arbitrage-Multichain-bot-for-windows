import networkx as nx
from governance.validator.governance_validator import GovernanceValidator, Severity
from governance.metadata.models import DocumentMetadata

def test_missing_owner():
    docs = [DocumentMetadata(path="docs/A.md")]
    g = nx.DiGraph()
    v = GovernanceValidator(docs, g)
    findings = v.validate_all()
    assert any(f.rule == "OWNER_REQUIRED" for f in findings)
