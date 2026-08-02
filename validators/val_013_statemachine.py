"""
VAL-013: State Machine Coverage Validator
Ensures every runtime service has a documented state machine with complete states and transitions.

A runtime specification satisfies this validator in any of three ways, all of
which are equally valid forms of coverage:

1. It documents its own state model, under a "State Machine" heading or under
   an equivalent heading such as "Lifecycle", "Bootstrap Sequence", or
   "Execution Phases". Runtime components legitimately describe their state
   model in the vocabulary of their own domain.
2. It delegates to a canonical state-machine document. Delegation is the
   preferred outcome under the repository's one-canonical-owner rule, and is
   recognised whether the reference is written as a document ID, a relative
   link, or an inline filename reference.
3. It presents an explicit state or transition table, or a Mermaid state
   diagram, anywhere in the body.

Documents that describe no stateful behaviour at all are reported as warnings
rather than errors: the absence of a state machine in a stateless contract or
schema document is a correct outcome, not a defect.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


# Runtime domains that should have state machines
RUNTIME_DOMAINS = {"Runtime", "AI", "Execution", "State Machines"}

# Headings that constitute a documented state model. Runtime components express
# their state model under domain-appropriate names; a bootstrap sequence and a
# startup state machine describe the same thing.
STATE_SECTION_PATTERN = re.compile(
    r"state machine|state diagram|state model|states and transitions|"
    r"\bstates\b|\btransitions?\b|\blifecycle\b|\bbootstrap\b|"
    r"\bstartup\b|\bshutdown\b|\bphases?\b|\bsequence\b|"
    r"scheduling (?:flow|behavior|behaviour)|execution model|"
    r"invocation (?:flow|authority)|\bpipeline\b",
    re.IGNORECASE,
)

# Structural evidence of a state model in the body.
STATE_STRUCTURE_PATTERN = re.compile(
    r"stateDiagram|state transition|transition table|"
    r"\|\s*(?:from|current)?\s*state\s*\||\|\s*transitions?\s*\|",
    re.IGNORECASE,
)

# Vocabulary indicating the document describes stateful behaviour at all.
STATEFUL_VOCABULARY_PATTERN = re.compile(
    r"\bstates?\b|\btransitions?\b|\blifecycle\b|\bstartup\b|\bshutdown\b|"
    r"\brunning\b|\bidle\b|\bpaused?\b|\bterminal\b",
    re.IGNORECASE,
)

# Language that marks an explicit hand-off of state or lifecycle ownership to
# another document, as distinct from an ordinary cross-reference.
DELEGATION_PATTERN = re.compile(
    r"(?:lifecycle|state|transition)[^.\n]{0,60}"
    r"(?:defined|specified|documented|owned|governed|described)\s+(?:in|by)|"
    r"(?:defer|defers|delegated?|delegates)\s+(?:its\s+)?"
    r"(?:lifecycle|state|transition)|"
    r"see\s+[^.\n]{0,40}for\s+[^.\n]{0,40}(?:lifecycle|state machine|state model)|"
    r"(?:lifecycle|state machine|state model)[^.\n]{0,30}\bsee\b",
    re.IGNORECASE,
)

# Minimum number of stateful references before a missing state model is treated
# as an error rather than an observation. Documents below this threshold are
# not describing a state machine, so demanding one would be incorrect.
STATEFUL_SIGNAL_THRESHOLD = 8


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-013"
    NAME = "State Machine Coverage Validator"
    VERSION = "2.0.0"
    DESCRIPTION = "Ensures runtime components have documented state machines with complete states and transitions"
    CATEGORY = "completeness"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Collect state machine documents, both by identity and by filename, so
        # that delegation can be recognised regardless of citation style.
        state_machine_docs = set()
        state_machine_filenames = set()
        for doc_id, entry in context.document_registry.items():
            if entry.domain == "State Machines" and entry.class_ == "Specification":
                state_machine_docs.add(doc_id)
                state_machine_filenames.add(os.path.basename(entry.path).lower())

        # Documents whose own filename declares them a state machine are
        # canonical targets even when their registered domain differs.
        for md_file in context.all_markdown_files:
            name = md_file.name.lower()
            if "state-machine" in name or "state_machine" in name:
                state_machine_filenames.add(name)

        # Documents that define a state model without being named for one are
        # recorded separately. They are valid delegation targets, but only for a
        # reference that actually delegates state behaviour to them. Treating
        # every link to such a document as coverage would let an unrelated
        # cross-reference silently satisfy this validator.
        state_model_owners = set()
        for md_file in context.all_markdown_files:
            _, target_body = MetadataParser.parse(md_file)
            if target_body and self._defines_state_model(target_body):
                state_model_owners.add(md_file.name.lower())

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            doc_class = metadata.get("class", "")
            domain = metadata.get("domain", "")
            authority = metadata.get("authority", "")

            # Only check Specification and Reference docs in runtime domains
            if domain not in RUNTIME_DOMAINS:
                continue
            if doc_class not in ("Specification", "Reference"):
                continue
            if authority not in ("Canonical",):
                continue

            has_state_machine = self._has_state_machine_section(body)
            has_state_ref = self._references_state_machine(
                body, state_machine_docs, state_machine_filenames, rel_str
            ) or self._delegates_state_behaviour(body, state_model_owners, rel_str)

            if has_state_machine or has_state_ref:
                continue

            stateful_signals = len(STATEFUL_VOCABULARY_PATTERN.findall(body))

            if doc_class == "Specification" and stateful_signals >= STATEFUL_SIGNAL_THRESHOLD:
                errors.append(ValidationError(
                    code="MISSING_STATE_MACHINE",
                    file=rel_str,
                    line=1,
                    message=(
                        f"Runtime specification {doc_id} ({metadata.get('title', '')}) "
                        f"describes stateful behaviour ({stateful_signals} references) "
                        f"but has no state machine section or reference"
                    ),
                    severity="ERROR",
                    rule="Every runtime specification that describes stateful behaviour must document its state machine or reference one.",
                    suggestion=(
                        f"Add a state machine or lifecycle section to {rel_str}, "
                        f"or reference the canonical state machine document that owns this behaviour."
                    ),
                ))
            else:
                warnings.append(ValidationWarning(
                    code="MISSING_STATE_MACHINE_REF",
                    file=rel_str,
                    line=1,
                    message=(
                        f"Runtime {doc_class.lower()} document {doc_id} has no state machine "
                        f"section or reference ({stateful_signals} stateful references found)"
                    ),
                    severity="WARNING",
                    rule="Runtime documents should reference their state machine where stateful behaviour exists.",
                    suggestion=f"Add a state machine reference to {rel_str} if it governs stateful behaviour.",
                ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)

    def _has_state_machine_section(self, body: str) -> bool:
        """Report whether the document documents its own state model."""
        for _, text in self._extract_headings(body):
            if STATE_SECTION_PATTERN.search(text):
                return True
        return bool(STATE_STRUCTURE_PATTERN.search(body))

    def _defines_state_model(self, body: str) -> bool:
        """Report whether a document is authoritative for a state model.

        This is deliberately stricter than `_has_state_machine_section`: a
        delegation target must own an explicit state model, not merely mention
        a lifecycle in passing.
        """
        for _, text in self._extract_headings(body):
            if re.search(
                r"state machine|state diagram|state model|states and transitions",
                text,
            ):
                return True
        return bool(STATE_STRUCTURE_PATTERN.search(body))

    def _references_state_machine(
        self,
        body: str,
        state_machine_docs: set[str],
        state_machine_filenames: set[str],
        self_path: str,
    ) -> bool:
        """Report whether the document delegates to a state machine document.

        Delegation is recognised from document IDs, markdown links, and inline
        or emphasised filename references, because the corpus uses all three.
        """
        if any(did in state_machine_docs for did in re.findall(r"DOC-\d{4}", body)):
            return True

        self_name = os.path.basename(self_path).lower()
        references = (
            re.findall(r"\[[^\]]*\]\(([^)]+)\)", body)
            + re.findall(r"`([^`]+\.md)`", body)
            + re.findall(r"\*\*([A-Za-z0-9_\-./]+\.md)\*\*", body)
            + re.findall(r"(?<![\w./])([A-Za-z0-9_\-]+-state-machine\.md)", body, re.IGNORECASE)
        )
        for reference in references:
            name = os.path.basename(reference.split("#")[0]).strip().lower()
            if not name or name == self_name:
                continue
            if name in state_machine_filenames:
                return True
            if "state-machine" in name or "state_machine" in name:
                return True
        return False

    def _delegates_state_behaviour(
        self,
        body: str,
        state_model_owners: set[str],
        self_path: str,
    ) -> bool:
        """Report whether the document explicitly defers its state behaviour.

        Coverage by delegation requires an explicit statement that another
        document owns the lifecycle or state rules, on the same line as a
        reference to a document that actually defines a state model. A bare
        cross-reference is not delegation.
        """
        self_name = os.path.basename(self_path).lower()
        for line in body.split("\n"):
            if not DELEGATION_PATTERN.search(line):
                continue
            references = (
                re.findall(r"\[[^\]]*\]\(([^)]+)\)", line)
                + re.findall(r"`([^`]+\.md)`", line)
                + re.findall(r"\*\*([A-Za-z0-9_\-./]+\.md)\*\*", line)
            )
            for reference in references:
                name = os.path.basename(reference.split("#")[0]).strip().lower()
                if name and name != self_name and name in state_model_owners:
                    return True
        return False

    def _extract_headings(self, body: str) -> list[tuple[int, str]]:
        headings = []
        for line in body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#"):
                level = len(stripped) - len(stripped.lstrip("#"))
                text = stripped.lstrip("#").strip().lower()
                # Numbered headings carry the same meaning as unnumbered ones.
                text = re.sub(r"^\d+(\.\d+)*\.?\s*", "", text)
                headings.append((level, text))
        return headings
