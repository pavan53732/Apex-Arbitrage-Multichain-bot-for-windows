"""Hash-chained decision ledger.

Implements the Phase 1 subset of
`docs/apex-app-docs/data/state/decision-ledger.md`.

The ledger owns the immutable trace of decisions. Four integrity rules from the
specification drive the implementation:

* **Records are hash-chained; a tampered record is detected on read.** Each
  record carries the digest of its predecessor, so altering any record breaks
  every link after it.
* **A record missing required fields is rejected, not partially stored.** An
  incomplete trace is worse than an absent one, because it looks like evidence.
* **Replays must reproduce the recorded decision deterministically.** A digest
  is computed from the record's content, so a replay that produces different
  content produces a different digest.
* **Nothing may mutate a stored record.** Records are frozen and the chain is
  append-only; there is no update or delete operation.

Phase 1 records decisions that were never executed. `execution_result` and
`post_execution_outcome` are therefore permitted to be explicitly absent, which
is a statement rather than an omission: the trade did not execute because the
phase forbids it.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterator

GENESIS_DIGEST = "0" * 16


class LedgerError(Exception):
    """Raised when a record cannot be appended or the chain fails verification."""


class IncompleteRecord(LedgerError):
    """Raised when a record is missing a required field.

    Distinct from a general ledger failure because the specification names
    incomplete lineage as its own failure mode with its own recovery path.
    """


class TamperDetected(LedgerError):
    """Raised when the hash chain does not verify."""


class DecisionOutcome(str, Enum):
    """Terminal outcomes of a decision, from the Decision Engine state machine."""

    APPROVED = "approved"
    REJECTED = "rejected"
    DEFERRED = "deferred"


# Fields the specification requires on every record. `execution_result` and
# `post_execution_outcome` are required to be *present*, but may be explicitly
# None: in Phase 1 no decision executes, and recording that fact is itself the
# required lineage.
_REQUIRED_FIELDS = (
    "decision_id",
    "timestamp_ms",
    "trigger_event",
    "market_snapshot",
    "recommendation",
    "deterministic_calculations",
    "policy_evaluation",
    "risk_verdict",
    "simulation_result",
    "final_decision",
)


@dataclass(frozen=True)
class DecisionRecord:
    """One immutable entry in the decision ledger.

    Frozen by construction. The specification forbids mutation of a stored
    record, and a frozen dataclass makes that a property of the type rather
    than a convention callers must respect.
    """

    decision_id: str
    timestamp_ms: int
    trigger_event: str
    market_snapshot: str
    recommendation: str
    deterministic_calculations: dict[str, int]
    policy_evaluation: str
    risk_verdict: str
    simulation_result: str
    final_decision: DecisionOutcome
    previous_digest: str
    execution_result: str | None = None
    post_execution_outcome: str | None = None

    def content(self) -> dict[str, Any]:
        """The record's canonical content, excluding its own digest.

        Ordering is fixed and values are JSON-serialised with sorted keys, so
        the same logical record always produces the same bytes. A digest that
        varied with dictionary ordering would make replay verification
        meaningless.
        """
        return {
            "decision_id": self.decision_id,
            "timestamp_ms": self.timestamp_ms,
            "trigger_event": self.trigger_event,
            "market_snapshot": self.market_snapshot,
            "recommendation": self.recommendation,
            "deterministic_calculations": dict(sorted(self.deterministic_calculations.items())),
            "policy_evaluation": self.policy_evaluation,
            "risk_verdict": self.risk_verdict,
            "simulation_result": self.simulation_result,
            "final_decision": self.final_decision.value,
            "execution_result": self.execution_result,
            "post_execution_outcome": self.post_execution_outcome,
            "previous_digest": self.previous_digest,
        }

    @property
    def digest(self) -> str:
        """This record's hash, chaining it to its predecessor."""
        payload = json.dumps(self.content(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _validate(record: DecisionRecord) -> None:
    """Reject a record missing required lineage.

    Checked before append so an incomplete record is never stored. The
    specification is explicit that such a record is rejected rather than
    partially written.
    """
    missing: list[str] = []
    for name in _REQUIRED_FIELDS:
        value = getattr(record, name)
        if value is None:
            missing.append(name)
        elif isinstance(value, str) and not value.strip():
            missing.append(name)
        elif isinstance(value, dict) and not value:
            missing.append(name)
    if missing:
        raise IncompleteRecord(
            f"record {record.decision_id or '<unnamed>'} is missing required "
            f"field(s): {', '.join(missing)}"
        )


@dataclass
class DecisionLedger:
    """An append-only, hash-chained sequence of decision records.

    Exposes no update or delete operation. Reading returns copies of frozen
    records, so a caller cannot reach in and alter stored history.
    """

    _records: list[DecisionRecord] = field(default_factory=list, init=False)

    def __len__(self) -> int:
        return len(self._records)

    def __iter__(self) -> Iterator[DecisionRecord]:
        return iter(tuple(self._records))

    @property
    def head_digest(self) -> str:
        """Digest of the most recent record, or the genesis value when empty."""
        return self._records[-1].digest if self._records else GENESIS_DIGEST

    @property
    def records(self) -> tuple[DecisionRecord, ...]:
        return tuple(self._records)

    def append(
        self,
        *,
        decision_id: str,
        timestamp_ms: int,
        trigger_event: str,
        market_snapshot: str,
        recommendation: str,
        deterministic_calculations: dict[str, int],
        policy_evaluation: str,
        risk_verdict: str,
        simulation_result: str,
        final_decision: DecisionOutcome,
        execution_result: str | None = None,
        post_execution_outcome: str | None = None,
    ) -> DecisionRecord:
        """Append a record, chaining it to the current head.

        The caller does not supply `previous_digest`: the ledger sets it, so a
        caller cannot forge a chain link or insert a record out of order.
        """
        if any(r.decision_id == decision_id for r in self._records):
            raise LedgerError(f"decision_id {decision_id!r} is already recorded")

        record = DecisionRecord(
            decision_id=decision_id,
            timestamp_ms=timestamp_ms,
            trigger_event=trigger_event,
            market_snapshot=market_snapshot,
            recommendation=recommendation,
            deterministic_calculations=dict(deterministic_calculations),
            policy_evaluation=policy_evaluation,
            risk_verdict=risk_verdict,
            simulation_result=simulation_result,
            final_decision=final_decision,
            previous_digest=self.head_digest,
            execution_result=execution_result,
            post_execution_outcome=post_execution_outcome,
        )
        _validate(record)
        self._records.append(record)
        return record

    def verify(self) -> None:
        """Verify the chain, raising `TamperDetected` on the first break.

        Called on read paths that depend on integrity. The specification
        requires a tampered record be detected on read and flagged, so this
        raises rather than returning a boolean a caller might ignore.
        """
        expected_previous = GENESIS_DIGEST
        for index, record in enumerate(self._records):
            if record.previous_digest != expected_previous:
                raise TamperDetected(
                    f"chain broken at position {index} (decision {record.decision_id}): "
                    f"expected previous digest {expected_previous}, found {record.previous_digest}"
                )
            expected_previous = record.digest

    def replay(self) -> tuple[DecisionRecord, ...]:
        """Return the verified chain for replay.

        Verification runs first: a replay over a tampered chain would reproduce
        the tampering rather than detect it.
        """
        self.verify()
        return self.records

    def find(self, decision_id: str) -> DecisionRecord:
        for record in self._records:
            if record.decision_id == decision_id:
                return record
        raise LedgerError(f"no record for decision_id {decision_id!r}")
