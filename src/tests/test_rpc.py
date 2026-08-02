"""Tests for RPC pool health, failover, and chain verification."""

from __future__ import annotations

import pytest

from apex.config import RpcConfig
from apex.rpc import ChainMismatchError, RpcError, RpcPool, static_transport

CONFIG = RpcConfig(chain_id=137, endpoints=("primary", "secondary", "tertiary"))


def test_uses_first_healthy_endpoint() -> None:
    pool = RpcPool(CONFIG, static_transport({"eth_blockNumber": 42}))
    assert pool.call("eth_blockNumber") == 42
    assert pool.health["primary"].successes == 1
    assert pool.health["secondary"].successes == 0


def test_fails_over_when_primary_errors() -> None:
    def transport(endpoint: str, method: str) -> object:
        if endpoint == "primary":
            raise RpcError("connection refused")
        return 99

    pool = RpcPool(CONFIG, transport)
    assert pool.call("eth_blockNumber") == 99
    assert pool.health["primary"].failures == 1
    assert pool.health["secondary"].successes == 1


def test_endpoint_quarantined_after_consecutive_failures() -> None:
    """A persistently failing endpoint is rotated out, not retried forever."""

    def transport(endpoint: str, method: str) -> object:
        if endpoint == "primary":
            raise RpcError("timeout")
        return 1

    pool = RpcPool(CONFIG, transport, quarantine_threshold=3)
    for _ in range(3):
        pool.call("eth_blockNumber")

    assert pool.health["primary"].quarantined is True
    assert "primary" not in pool.healthy_endpoints


def test_success_resets_consecutive_failures() -> None:
    state = {"fail": True}

    def transport(endpoint: str, method: str) -> object:
        if endpoint == "primary" and state["fail"]:
            raise RpcError("blip")
        return 7

    pool = RpcPool(CONFIG, transport, quarantine_threshold=3)
    pool.call("m")
    assert pool.health["primary"].consecutive_failures == 1

    state["fail"] = False
    pool.call("m")
    assert pool.health["primary"].consecutive_failures == 0
    assert pool.health["primary"].quarantined is False


def test_all_endpoints_failing_raises_rather_than_fabricating() -> None:
    """No substitute value is returned; absence stays distinguishable."""

    def transport(endpoint: str, method: str) -> object:
        raise RpcError("down")

    pool = RpcPool(CONFIG, transport)
    with pytest.raises(RpcError, match="no healthy endpoint"):
        pool.call("eth_blockNumber")


def test_chain_id_verified_from_hex() -> None:
    pool = RpcPool(CONFIG, static_transport({"eth_chainId": "0x89"}))
    assert pool.verify_chain_id() == 137


def test_chain_id_mismatch_is_fatal() -> None:
    """A wrong-network endpoint is rejected, never treated as degraded."""
    pool = RpcPool(CONFIG, static_transport({"eth_chainId": "0x1"}))
    with pytest.raises(ChainMismatchError, match="reports chain 1"):
        pool.verify_chain_id()


def test_unparsable_chain_id_rejected() -> None:
    pool = RpcPool(CONFIG, static_transport({"eth_chainId": "not-a-number"}))
    with pytest.raises(ChainMismatchError, match="unparsable"):
        pool.verify_chain_id()


def test_redundancy_floor_reported_truthfully() -> None:
    single = RpcConfig(chain_id=137, endpoints=("only",))
    pool = RpcPool(single, static_transport({"m": 1}))
    assert pool.has_redundancy is False

    pair = RpcPool(CONFIG, static_transport({"m": 1}))
    assert pair.has_redundancy is True


def test_redundancy_lost_when_endpoints_quarantine() -> None:
    def transport(endpoint: str, method: str) -> object:
        if endpoint in ("primary", "secondary"):
            raise RpcError("down")
        return 1

    pool = RpcPool(CONFIG, transport, quarantine_threshold=1)
    pool.call("m")
    assert pool.has_redundancy is False
