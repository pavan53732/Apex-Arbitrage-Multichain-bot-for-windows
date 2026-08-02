"""Tests for the Phase 1 pipeline, including the execution block.

The execution-block tests are the most important in this suite. They assert
that the Phase 1 invariant from
`docs/apex-app-docs/execution/risk-policy/risk-engine.md` §0 holds structurally
and cannot be bypassed.
"""

from __future__ import annotations

import pytest

from apex.config import load_config
from apex.dex import Pool, QuoteError
from apex.pipeline import (
    PHASE_1_BLOCK_CODE,
    ExecutionBlocked,
    SimulationPipeline,
    SimulationResult,
)
from apex.rpc import ChainMismatchError, RpcError, RpcPool, static_transport

NOW = 1_000_000

RAW_CONFIG = {
    "phase": "simulation_only",
    "chain_id": 137,
    "rpc_endpoints": ["https://rpc-a.example", "https://rpc-b.example"],
    "max_slippage_bps": 100,
    "quote_freshness_ms": 5_000,
}


def build_pipeline(transport=None) -> SimulationPipeline:
    config = load_config(RAW_CONFIG)
    pool = RpcPool(config.rpc, transport or static_transport({"eth_chainId": "0x89"}))
    return SimulationPipeline(config=config, rpc=pool)


def make_pool(**overrides: object) -> Pool:
    params = dict(
        dex_id="uniswap-v2",
        token_in="USDC",
        token_out="WETH",
        reserve_in=1_000_000_000,
        reserve_out=500_000_000,
        fee_bps=30,
        observed_at_ms=NOW,
    )
    params.update(overrides)
    return Pool(**params)  # type: ignore[arg-type]


def test_end_to_end_simulation_produces_unexecuted_result() -> None:
    pipeline = build_pipeline()
    result = pipeline.evaluate([make_pool()], 1_000_000, now_ms=NOW)

    assert result.chain_id == 137
    assert result.quote.amount_out == 498_003
    assert result.executed is False
    assert result.rejection_code == PHASE_1_BLOCK_CODE
    assert "PHASE_1_EXECUTION_BLOCK" in result.summary


def test_execution_is_always_blocked() -> None:
    """The Phase 1 invariant: any execution attempt is hard rejected."""
    pipeline = build_pipeline()
    result = pipeline.evaluate([make_pool()], 1_000_000, now_ms=NOW)

    with pytest.raises(ExecutionBlocked) as excinfo:
        pipeline.execute(result)
    assert excinfo.value.code == PHASE_1_BLOCK_CODE


def test_execution_blocked_for_every_result_shape() -> None:
    """No input reaches a success path, because none exists."""
    pipeline = build_pipeline()
    for amount in (1_000, 100_000, 1_000_000):
        result = pipeline.evaluate([make_pool()], amount, now_ms=NOW)
        with pytest.raises(ExecutionBlocked):
            pipeline.execute(result)


def test_config_never_permits_live_execution() -> None:
    assert load_config(RAW_CONFIG).live_execution_permitted is False


def test_chain_mismatch_prevents_quoting() -> None:
    """Connectivity is verified before any quote is computed."""
    pipeline = build_pipeline(static_transport({"eth_chainId": "0x1"}))
    with pytest.raises(ChainMismatchError):
        pipeline.evaluate([make_pool()], 1_000_000, now_ms=NOW)


def test_dead_rpc_prevents_quoting() -> None:
    """An absent input is never treated as an unchanged one."""

    def dead(endpoint: str, method: str) -> object:
        raise RpcError("unreachable")

    pipeline = build_pipeline(dead)
    with pytest.raises(RpcError):
        pipeline.evaluate([make_pool()], 1_000_000, now_ms=NOW)


def test_stale_venue_excluded_and_reported() -> None:
    pipeline = build_pipeline()
    result = pipeline.evaluate(
        [make_pool(dex_id="stale", observed_at_ms=NOW - 60_000), make_pool(dex_id="fresh")],
        1_000_000,
        now_ms=NOW,
    )
    assert result.quote.dex_id == "fresh"
    assert len(result.excluded_venues) == 1
    assert "stale" in result.excluded_venues[0]


def test_all_venues_excluded_raises() -> None:
    pipeline = build_pipeline()
    with pytest.raises(QuoteError, match="every venue was excluded"):
        pipeline.evaluate(
            [make_pool(dex_id="a", observed_at_ms=NOW - 60_000)], 1_000, now_ms=NOW
        )


def test_redundancy_warning_surfaced_without_blocking() -> None:
    raw = {**RAW_CONFIG, "rpc_endpoints": ["https://only.example"]}
    config = load_config(raw)
    pool = RpcPool(config.rpc, static_transport({"eth_chainId": "0x89"}))
    pipeline = SimulationPipeline(config=config, rpc=pool)

    result = pipeline.evaluate([make_pool()], 1_000_000, now_ms=NOW)
    assert result.quote.amount_out == 498_003
    assert any("autonomous execution requires at least 2" in w for w in pipeline.warnings)


def test_pipeline_is_reproducible() -> None:
    """Simulation paths must produce reproducible results."""
    outputs = []
    for _ in range(3):
        pipeline = build_pipeline()
        result = pipeline.evaluate([make_pool()], 1_000_000, now_ms=NOW)
        outputs.append(result.quote.amount_out)
    assert len(set(outputs)) == 1


def test_no_execution_capability_exists_in_package() -> None:
    """Structural guard: the slice must not gain a signing or send path.

    Phase 1 has no wallet and no broadcast capability. If a future change adds
    one, this test fails and forces the phase question to be answered
    deliberately rather than incidentally.
    """
    import pathlib

    import apex

    forbidden = ("send_raw_transaction", "sign_transaction", "private_key", "eth_sendRaw")
    package_dir = pathlib.Path(apex.__file__).parent
    for source in package_dir.glob("*.py"):
        text = source.read_text(encoding="utf-8").lower()
        for token in forbidden:
            assert token.lower() not in text, f"{source.name} contains execution capability {token!r}"
