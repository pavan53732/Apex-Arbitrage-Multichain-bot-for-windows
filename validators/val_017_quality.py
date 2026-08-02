"""
VAL-017: Documentation Quality Validator
Produces objective quality scoring using deterministic metrics from validator outputs,
registry data, and document content analysis. No subjective heuristics.
"""

from __future__ import annotations
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


# Class-specific weights for quality dimensions
CLASS_WEIGHTS = {
    "Specification": {
        "completeness": 0.25, "authority": 0.15, "responsibility": 0.10,
        "references": 0.10, "traceability": 0.10, "examples": 0.05,
        "freshness": 0.05, "failure_handling": 0.05, "security": 0.05,
        "performance": 0.05, "lifecycle": 0.05,
    },
    "Guide": {
        "completeness": 0.15, "authority": 0.15, "responsibility": 0.10,
        "references": 0.15, "traceability": 0.10, "examples": 0.10,
        "freshness": 0.05, "lifecycle": 0.05, "terminology": 0.10,
        "testing": 0.05,
    },
    "Index": {
        "completeness": 0.10, "authority": 0.10, "responsibility": 0.10,
        "references": 0.25, "traceability": 0.10, "freshness": 0.05,
        "lifecycle": 0.05, "terminology": 0.10, "consumers": 0.10,
        "cross_references": 0.05,
    },
    "ADR": {
        "completeness": 0.20, "authority": 0.20, "responsibility": 0.15,
        "references": 0.10, "traceability": 0.15, "freshness": 0.05,
        "lifecycle": 0.10, "terminology": 0.05,
    },
    "Policy": {
        "completeness": 0.20, "authority": 0.20, "responsibility": 0.10,
        "references": 0.10, "traceability": 0.10, "freshness": 0.05,
        "lifecycle": 0.05, "enforcement": 0.10, "exceptions": 0.10,
    },
    "Reference": {
        "completeness": 0.15, "authority": 0.15, "responsibility": 0.10,
        "references": 0.15, "traceability": 0.10, "examples": 0.10,
        "freshness": 0.05, "lifecycle": 0.05, "terminology": 0.05,
        "cross_references": 0.10,
    },
    "Registry": {
        "completeness": 0.25, "authority": 0.20, "responsibility": 0.10,
        "references": 0.10, "traceability": 0.15, "freshness": 0.10,
        "lifecycle": 0.10,
    },
    "Workflow": {
        "completeness": 0.20, "authority": 0.15, "responsibility": 0.10,
        "references": 0.10, "traceability": 0.10, "examples": 0.10,
        "freshness": 0.05, "lifecycle": 0.05, "failure_handling": 0.10,
        "steps": 0.05,
    },
    "Historical": {
        "completeness": 0.10, "authority": 0.10, "references": 0.20,
        "traceability": 0.20, "freshness": 0.05, "lifecycle": 0.35,
    },
}

DEFAULT_WEIGHTS = {
    "completeness": 0.15, "authority": 0.15, "responsibility": 0.10,
    "references": 0.15, "traceability": 0.15, "freshness": 0.10,
    "lifecycle": 0.10, "examples": 0.05, "terminology": 0.05,
}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-017"
    NAME = "Documentation Quality Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Produces objective quality scoring using deterministic metrics from validator outputs and document analysis"
    CATEGORY = "quality"
    SEVERITY = "INFO"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    STALE_DAYS = 365
    FRESH_DAYS = 30

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        warnings = []
        infos = []
        checked = 0
        scores: dict[str, dict] = {}

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            if doc_id == "unknown":
                continue

            doc_class = metadata.get("class", "")
            authority = metadata.get("authority", "")
            status = metadata.get("status", "")

            weights = CLASS_WEIGHTS.get(doc_class, DEFAULT_WEIGHTS)
            entry = context.document_registry.get(doc_id)

            dims = {}

            # D1: Completeness — based on section heading coverage
            dims["completeness"] = self._score_completeness(body, doc_class)

            # D2: Authority — concept_role and canonical_source validity
            dims["authority"] = self._score_authority(metadata, entry)

            # D3: Single Responsibility — related_concepts count
            dims["responsibility"] = self._score_responsibility(metadata)

            # D4: References — inbound + outbound link density
            dims["references"] = self._score_references(body, doc_id, context)

            # D5: Traceability — registry relationship coverage
            dims["traceability"] = self._score_traceability(doc_id, context)

            # D6: Examples — code blocks or structured examples
            dims["examples"] = self._score_examples(body)

            # D7: Freshness — days since last_updated
            dims["freshness"] = self._score_freshness(metadata)

            # D8: Lifecycle — status progression
            dims["lifecycle"] = self._score_lifecycle(status, metadata)

            # D9: Failure Handling
            dims["failure_handling"] = self._score_section_present(body, ["failure", "error handl", "recovery", "fault"])

            # D10: Security
            dims["security"] = self._score_section_present(body, ["security", "permission", "trust boundar", "secret"])

            # D11: Performance
            dims["performance"] = self._score_section_present(body, ["performance", "slo", "latency", "throughput", "budget"])

            # D12: Terminology — glossary terms consistently used
            dims["terminology"] = self._score_terminology(body)

            # D13: Consumers
            dims["consumers"] = self._score_consumers(entry)

            # D14: Cross-references
            dims["cross_references"] = self._score_crossrefs(body, context)

            # D15: Enforcement (Policy docs)
            dims["enforcement"] = self._score_section_present(body, ["enforcement", "compliance"])

            # D16: Exceptions (Policy docs)
            dims["exceptions"] = self._score_section_present(body, ["exception", "exemption", "waiver"])

            # D17: Testing
            dims["testing"] = self._score_section_present(body, ["test", "validation"])

            # D18: Steps (Workflow docs)
            dims["steps"] = self._score_steps(body)

            # Compute weighted score
            total_weight = 0.0
            weighted_sum = 0.0
            for dim, weight in weights.items():
                score = dims.get(dim, 0.5)
                weighted_sum += weight * score
                total_weight += weight

            quality_score = int((weighted_sum / total_weight) * 100) if total_weight > 0 else 50
            quality_score = max(0, min(100, quality_score))

            scores[doc_id] = {
                "doc_id": doc_id,
                "path": rel_str,
                "class": doc_class,
                "overall": quality_score,
                "dimensions": {k: round(v, 2) for k, v in dims.items() if v > 0},
            }

            infos.append(ValidationWarning(
                code="QUALITY_SCORE",
                file=rel_str, line=1,
                message=f"Quality score: {quality_score}/100",
                severity="INFO",
                rule="Quality score computed from deterministic metrics.",
                suggestion="",
            ))

            # Flag low-quality documents
            if quality_score < 25:
                warnings.append(ValidationWarning(
                    code="QUALITY_DEFICIENT",
                    file=rel_str, line=1,
                    message=f"Document {doc_id} quality score {quality_score}/100 is DEFICIENT",
                    severity="WARNING",
                    rule="Documents with quality < 25 require rewrite or archival.",
                    suggestion="Rewrite or archive this document.",
                ))

        # Compute domain-level quality aggregates
        domain_scores = defaultdict(list)
        for doc_id, s in scores.items():
            entry = context.document_registry.get(doc_id)
            if entry:
                domain_scores[entry.domain].append(s["overall"])

        for domain, dscores in sorted(domain_scores.items()):
            avg = sum(dscores) / len(dscores)
            infos.append(ValidationWarning(
                code="DOMAIN_QUALITY",
                file="", line=1,
                message=f"Domain '{domain}': avg quality {avg:.1f}/100 across {len(dscores)} documents",
                severity="INFO",
                rule="Domain-level quality aggregate.",
                suggestion=f"{'Review domain' if avg < 50 else 'Domain quality acceptable'}.",
            ))

        return self._result_pass(checked, warnings + infos)

    # ── Scoring functions (all return 0.0–1.0) ──

    def _score_completeness(self, body: str, doc_class: str) -> float:
        headings = [l.strip().lstrip("#").strip().lower() for l in body.split("\n") if l.strip().startswith("#")]
        expected = {
            "Specification": ["purpose", "scope", "dependencies", "architecture"],
            "Guide": ["purpose", "scope", "steps"],
            "ADR": ["context", "decision", "consequences"],
            "Policy": ["purpose", "scope", "rules"],
            "Reference": ["purpose", "scope", "description"],
            "Index": ["purpose", "scope", "navigation"],
            "Registry": ["purpose", "registry metadata"],
            "Workflow": ["purpose", "scope", "steps"],
            "Historical": ["purpose"],
        }.get(doc_class, ["purpose", "scope"])
        if not headings:
            return 0.0
        found = sum(1 for e in expected if any(self._partial_match(e, h) for h in headings))
        return min(1.0, found / max(1, len(expected)))

    def _score_authority(self, metadata: dict, entry) -> float:
        score = 0.5
        role = metadata.get("concept_role", "")
        doc_path = entry.path if entry else ""
        csource = metadata.get("canonical_source", "")
        # Owner docs should have canonical_source pointing to themselves
        if role == "Owner" and csource and csource == doc_path:
            score += 0.3
        elif role in ("Reference", "Index", "Historical Reference"):
            score += 0.2
        if entry and entry.authority == "Canonical":
            score += 0.2
        return min(1.0, score)

    def _score_responsibility(self, metadata: dict) -> float:
        related = metadata.get("related_concepts", [])
        if not related:
            return 0.5
        count = len([c for c in related if c and str(c).startswith("CONCEPT-")])
        if count == 1:
            return 1.0
        if count <= 3:
            return 0.7
        return 0.3

    def _score_references(self, body: str, doc_id: str, context: ValidationContext) -> float:
        import re
        links = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", body)
        doc_refs = re.findall(r"DOC-\d{4}", body)
        concept_refs = re.findall(r"CONCEPT-\d{4}", body)
        total = len(links) + len(doc_refs) + len(concept_refs)
        lines = max(1, len(body.split("\n")))
        density = total / lines
        expected = 0.05
        return min(1.0, density / expected)

    def _score_traceability(self, doc_id: str, context: ValidationContext) -> float:
        count = 0
        for trace in context.traceability_registry.values():
            if trace.source_id == doc_id or trace.target_id == doc_id:
                count += 1
        expected = 3
        return min(1.0, count / expected)

    def _score_examples(self, body: str) -> float:
        import re
        code_blocks = len(re.findall(r"```", body)) // 2
        if code_blocks >= 3:
            return 1.0
        if code_blocks >= 1:
            return 0.5
        return 0.0

    def _score_freshness(self, metadata: dict) -> float:
        lu = metadata.get("last_updated", "")
        if not lu:
            return 0.3
        try:
            if isinstance(lu, str):
                d = datetime.fromisoformat(lu)
            else:
                d = lu
            days = (datetime.now(timezone.utc) - d.replace(tzinfo=timezone.utc)).days
            if days <= self.FRESH_DAYS:
                return 1.0
            if days <= self.STALE_DAYS:
                return 1.0 - (days - self.FRESH_DAYS) / (self.STALE_DAYS - self.FRESH_DAYS) * 0.7
            return 0.3
        except (ValueError, TypeError):
            return 0.3

    def _score_lifecycle(self, status: str, metadata: dict) -> float:
        status_scores = {
            "Active": 1.0, "Approved": 0.8, "Review": 0.5,
            "Draft": 0.4, "Experimental": 0.3, "Deprecated": 0.2,
            "Archived": 0.1, "Superseded": 0.0,
        }
        return status_scores.get(status, 0.3)

    def _score_section_present(self, body: str, keywords: list[str]) -> float:
        headings = [l.strip().lstrip("#").strip().lower() for l in body.split("\n") if l.strip().startswith("#")]
        for kw in keywords:
            for h in headings:
                if kw in h:
                    return 1.0
        body_lower = body.lower()
        for kw in keywords:
            if kw in body_lower:
                return 0.5
        return 0.0

    def _score_terminology(self, body: str) -> float:
        # Count glossary terms used
        known_terms = [
            "orchestrator", "worker", "workspace", "pipeline", "plugin", "provider",
            "kernel", "state machine", "contract", "event bus", "ipc", "adr",
            "canonical source", "registry", "plane", "domain",
            "trading engine", "risk engine", "policy engine", "decision engine",
            "simulation engine", "routing engine",
        ]
        body_lower = body.lower()
        found = sum(1 for t in known_terms if t in body_lower)
        if found == 0:
            return 0.5
        return min(1.0, found / 5)

    def _score_consumers(self, entry) -> float:
        if not entry:
            return 0.0
        consumers = entry.consumers or []
        count = len([c for c in consumers if c and c.strip()])
        return min(1.0, count / 2)

    def _score_crossrefs(self, body: str, context: ValidationContext) -> float:
        import re
        doc_refs = set(re.findall(r"DOC-\d{4}", body))
        resolved = sum(1 for d in doc_refs if d in context.document_registry)
        if not doc_refs:
            return 0.5
        return resolved / len(doc_refs)

    def _score_steps(self, body: str) -> float:
        headings = [l.strip().lstrip("#").strip().lower() for l in body.split("\n") if l.strip().startswith("#")]
        for h in headings:
            if "step" in h or "procedure" in h or "workflow" in h:
                return 1.0
        numbered_steps = sum(1 for l in body.split("\n") if l.strip() and l.strip()[0].isdigit() and ". " in l[:5])
        return min(1.0, numbered_steps / 5)

    def _partial_match(self, target: str, heading: str) -> bool:
        return target in heading or heading in target
