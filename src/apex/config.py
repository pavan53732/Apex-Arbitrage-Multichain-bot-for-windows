"""Configuration loading and phase gating.

Implements the parts of `docs/apex-app-docs/configuration/core/configuration.md`
and `docs/apex-app-docs/execution/risk-policy/policy-engine.md` that the Phase 1
slice depends on.

Two rules from the specification drive this module:

* A missing or invalid required value blocks the dependent path. The Policy
  Engine specification states that no implicit default is substituted for a
  required threshold, because a silently defaulted limit is indistinguishable
  from an intentionally configured one.
* Phase 1 is simulation-only. The execution phase is part of configuration, and
  a configuration that claims a live phase is rejected by this slice rather than
  honoured, because no execution path exists to honour it with.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class ConfigError(Exception):
    """Raised when configuration is missing, malformed, or out of range.

    Configuration failures are explicit. The Policy Engine specification
    requires that a dependent execution path block rather than proceed on an
    assumed value, so this is an error rather than a warning.
    """


class ExecutionPhase(str, Enum):
    """MVP execution phases.

    Defined by `docs/apex-app-docs/execution/risk-policy/risk-engine.md` §0.
    Only `SIMULATION_ONLY` is implemented; the later phases exist so that a
    configuration naming them is rejected explicitly rather than
    misinterpreted as simulation.
    """

    SIMULATION_ONLY = "simulation_only"
    OPERATOR_APPROVED = "operator_approved"
    AUTONOMOUS = "autonomous"


@dataclass(frozen=True)
class RpcConfig:
    """Endpoint configuration for a single chain.

    `docs/apex-app-docs/market/connectivity/rpc-manager.md` requires multi-RPC
    redundancy and treats a single endpoint as insufficient for autonomous
    operation. Redundancy is therefore represented here even though Phase 1
    never submits a transaction.
    """

    chain_id: int
    endpoints: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.chain_id <= 0:
            raise ConfigError(f"chain_id must be positive, got {self.chain_id}")
        if not self.endpoints:
            raise ConfigError(f"chain {self.chain_id} declares no RPC endpoints")


@dataclass(frozen=True)
class Config:
    """Validated runtime configuration for the Phase 1 slice."""

    phase: ExecutionPhase
    rpc: RpcConfig
    max_slippage_bps: int
    quote_freshness_ms: int
    min_edge_bps: int = 0
    metadata: Mapping[str, Any] = field(default_factory=dict)

    @property
    def live_execution_permitted(self) -> bool:
        """Whether live execution is permitted under the configured phase.

        Always False in this slice. Phase 1 rejects live execution
        unconditionally, and no later phase is implemented.
        """
        return False


_REQUIRED_KEYS = ("phase", "chain_id", "rpc_endpoints", "max_slippage_bps", "quote_freshness_ms")


def load_config(raw: Mapping[str, Any]) -> Config:
    """Build a validated `Config` from a raw mapping.

    Every required key must be present and within range. Absence is not
    defaulted, and an out-of-range value is rejected rather than clamped: a
    clamped limit would silently weaken a threshold the operator set
    deliberately.
    """
    if not isinstance(raw, Mapping):
        raise ConfigError(f"configuration must be a mapping, got {type(raw).__name__}")

    missing = [key for key in _REQUIRED_KEYS if key not in raw]
    if missing:
        raise ConfigError(f"missing required configuration keys: {', '.join(sorted(missing))}")

    phase_raw = raw["phase"]
    try:
        phase = ExecutionPhase(phase_raw)
    except ValueError:
        permitted = ", ".join(p.value for p in ExecutionPhase)
        raise ConfigError(f"unknown execution phase {phase_raw!r}; expected one of: {permitted}")

    if phase is not ExecutionPhase.SIMULATION_ONLY:
        raise ConfigError(
            f"phase {phase.value!r} is not implemented. This build is simulation-only "
            f"and has no execution path; refusing to start in a phase it cannot honour."
        )

    endpoints = raw["rpc_endpoints"]
    if isinstance(endpoints, str) or not isinstance(endpoints, (list, tuple)):
        raise ConfigError("rpc_endpoints must be a list of endpoint URLs")

    rpc = RpcConfig(chain_id=_as_int(raw, "chain_id"), endpoints=tuple(endpoints))

    max_slippage_bps = _as_int(raw, "max_slippage_bps")
    if not 0 <= max_slippage_bps <= 10_000:
        raise ConfigError(f"max_slippage_bps must be within 0..10000, got {max_slippage_bps}")

    quote_freshness_ms = _as_int(raw, "quote_freshness_ms")
    if quote_freshness_ms <= 0:
        raise ConfigError(f"quote_freshness_ms must be positive, got {quote_freshness_ms}")

    min_edge_bps = _as_int(raw, "min_edge_bps") if "min_edge_bps" in raw else 0
    if min_edge_bps < 0:
        raise ConfigError(f"min_edge_bps must not be negative, got {min_edge_bps}")

    return Config(
        phase=phase,
        rpc=rpc,
        max_slippage_bps=max_slippage_bps,
        quote_freshness_ms=quote_freshness_ms,
        min_edge_bps=min_edge_bps,
        metadata=dict(raw.get("metadata", {})),
    )


def _as_int(raw: Mapping[str, Any], key: str) -> int:
    """Read an integer configuration value without silent coercion.

    Booleans are rejected explicitly: Python treats `bool` as a subclass of
    `int`, so `True` would otherwise be accepted as the value 1.
    """
    value = raw[key]
    if isinstance(value, bool) or not isinstance(value, int):
        raise ConfigError(f"{key} must be an integer, got {type(value).__name__}")
    return value
