"""RPC provider pool with health tracking and failover.

Implements the Phase 1 subset of
`docs/apex-app-docs/market/connectivity/rpc-manager.md`.

The specification classifies RPC providers as CONNECTIVITY_AUTHORITY only:
they carry no pricing, validation, or execution authority. Two consequences are
enforced here:

* A provider failure is a routing problem, not a market signal. The pool fails
  over to another endpoint and never fabricates a response, because an invented
  reading would be indistinguishable from an observed one.
* Chain-ID mismatch rejects an endpoint outright. An endpoint reporting a
  different chain would have transactions submitted to the wrong network.

No transport is implemented. The pool is driven by an injected callable so the
Phase 1 slice stays offline and deterministic, per the coding standard that
simulation paths must be reproducible.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Protocol

from .config import RpcConfig


class RpcError(Exception):
    """Raised when no healthy endpoint can serve a request."""


class ChainMismatchError(RpcError):
    """Raised when an endpoint reports a chain ID other than the expected one."""


class Transport(Protocol):
    """Minimal transport contract.

    Returns the endpoint's response for a named method. Raising any exception
    marks the call as failed and triggers failover.
    """

    def __call__(self, endpoint: str, method: str) -> object: ...


@dataclass
class EndpointHealth:
    """Health record for a single endpoint.

    The specification requires tracking success and failure so that a
    persistently failing endpoint is rotated out rather than retried forever.
    """

    endpoint: str
    successes: int = 0
    failures: int = 0
    consecutive_failures: int = 0
    quarantined: bool = False

    def record_success(self) -> None:
        self.successes += 1
        self.consecutive_failures = 0

    def record_failure(self, quarantine_threshold: int) -> None:
        self.failures += 1
        self.consecutive_failures += 1
        if self.consecutive_failures >= quarantine_threshold:
            self.quarantined = True


@dataclass
class RpcPool:
    """An ordered pool of endpoints for one chain.

    Endpoints are tried in declaration order, which the specification treats as
    tier order: higher-reliability providers are declared first.
    """

    config: RpcConfig
    transport: Transport
    quarantine_threshold: int = 3
    health: dict[str, EndpointHealth] = field(init=False)

    def __post_init__(self) -> None:
        self.health = {e: EndpointHealth(e) for e in self.config.endpoints}

    @property
    def healthy_endpoints(self) -> tuple[str, ...]:
        return tuple(e for e in self.config.endpoints if not self.health[e].quarantined)

    @property
    def has_redundancy(self) -> bool:
        """Whether the pool meets the two-healthy-endpoint redundancy floor.

        The specification requires a minimum of two healthy RPCs before
        autonomous (Phase 3) execution. Phase 1 never executes, so this is
        reported rather than enforced — but it is reported truthfully so the
        gate is already meaningful when later phases arrive.
        """
        return len(self.healthy_endpoints) >= 2

    def call(self, method: str) -> object:
        """Invoke `method` on the first healthy endpoint that answers.

        Raises `RpcError` when every endpoint fails. The pool never returns a
        substitute or cached value in that case: an absent reading and a real
        reading must remain distinguishable.
        """
        errors: list[str] = []

        for endpoint in self.config.endpoints:
            record = self.health[endpoint]
            if record.quarantined:
                continue
            try:
                result = self.transport(endpoint, method)
            except Exception as exc:  # noqa: BLE001 - transport failures are expected
                record.record_failure(self.quarantine_threshold)
                errors.append(f"{endpoint}: {exc}")
                continue
            record.record_success()
            return result

        raise RpcError(
            f"no healthy endpoint served {method!r} for chain {self.config.chain_id}; "
            f"attempts: {'; '.join(errors) if errors else 'all endpoints quarantined'}"
        )

    def verify_chain_id(self) -> int:
        """Confirm the pool's endpoints serve the configured chain.

        A mismatch is fatal rather than a failover candidate: an endpoint on the
        wrong network is not a degraded source of the right data.
        """
        reported = self.call("eth_chainId")
        try:
            reported_id = int(reported, 16) if isinstance(reported, str) else int(reported)
        except (TypeError, ValueError):
            raise ChainMismatchError(f"endpoint returned unparsable chain id: {reported!r}")

        if reported_id != self.config.chain_id:
            raise ChainMismatchError(
                f"endpoint reports chain {reported_id}, expected {self.config.chain_id}"
            )
        return reported_id


def static_transport(responses: dict[str, object]) -> Callable[[str, str], object]:
    """Build a deterministic transport for tests and simulation.

    Keeps the Phase 1 slice offline while exercising the real failover logic.
    """

    def _transport(endpoint: str, method: str) -> object:
        if method not in responses:
            raise RpcError(f"no canned response for {method!r}")
        return responses[method]

    return _transport
