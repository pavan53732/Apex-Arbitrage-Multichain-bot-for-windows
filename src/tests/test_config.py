"""Tests for configuration loading and phase gating."""

from __future__ import annotations

import pytest

from apex.config import Config, ConfigError, ExecutionPhase, RpcConfig, load_config

VALID = {
    "phase": "simulation_only",
    "chain_id": 137,
    "rpc_endpoints": ["https://rpc-a.example", "https://rpc-b.example"],
    "max_slippage_bps": 50,
    "quote_freshness_ms": 2_000,
}


def test_loads_valid_configuration() -> None:
    config = load_config(VALID)
    assert config.phase is ExecutionPhase.SIMULATION_ONLY
    assert config.rpc.chain_id == 137
    assert config.rpc.endpoints == ("https://rpc-a.example", "https://rpc-b.example")
    assert config.max_slippage_bps == 50
    assert config.min_edge_bps == 0


def test_live_execution_is_never_permitted() -> None:
    """Phase 1 rejects live execution; no configuration can enable it."""
    assert load_config(VALID).live_execution_permitted is False


@pytest.mark.parametrize("key", sorted(VALID))
def test_missing_required_key_is_rejected(key: str) -> None:
    """A required value is never defaulted; its absence blocks the path."""
    raw = {k: v for k, v in VALID.items() if k != key}
    with pytest.raises(ConfigError, match="missing required configuration keys"):
        load_config(raw)


def test_unimplemented_phase_is_refused() -> None:
    """A live phase is refused rather than downgraded to simulation."""
    with pytest.raises(ConfigError, match="not implemented"):
        load_config({**VALID, "phase": "autonomous"})


def test_unknown_phase_is_refused() -> None:
    with pytest.raises(ConfigError, match="unknown execution phase"):
        load_config({**VALID, "phase": "turbo"})


@pytest.mark.parametrize("value", [-1, 10_001])
def test_slippage_out_of_range_is_rejected_not_clamped(value: int) -> None:
    with pytest.raises(ConfigError, match="max_slippage_bps"):
        load_config({**VALID, "max_slippage_bps": value})


def test_zero_freshness_budget_is_rejected() -> None:
    with pytest.raises(ConfigError, match="quote_freshness_ms"):
        load_config({**VALID, "quote_freshness_ms": 0})


def test_boolean_is_not_accepted_as_integer() -> None:
    """`bool` subclasses `int`; True must not pass as the value 1."""
    with pytest.raises(ConfigError, match="must be an integer"):
        load_config({**VALID, "chain_id": True})


def test_string_endpoints_rejected() -> None:
    """A bare string is iterable and would silently become a list of chars."""
    with pytest.raises(ConfigError, match="rpc_endpoints must be a list"):
        load_config({**VALID, "rpc_endpoints": "https://rpc-a.example"})


def test_empty_endpoint_list_rejected() -> None:
    with pytest.raises(ConfigError, match="no RPC endpoints"):
        load_config({**VALID, "rpc_endpoints": []})


def test_non_positive_chain_id_rejected() -> None:
    with pytest.raises(ConfigError, match="chain_id must be positive"):
        RpcConfig(chain_id=0, endpoints=("https://rpc.example",))


def test_config_is_immutable() -> None:
    config = load_config(VALID)
    with pytest.raises(Exception):
        config.max_slippage_bps = 9_999  # type: ignore[misc]


def test_non_mapping_input_rejected() -> None:
    with pytest.raises(ConfigError, match="must be a mapping"):
        load_config(["phase", "simulation_only"])  # type: ignore[arg-type]
