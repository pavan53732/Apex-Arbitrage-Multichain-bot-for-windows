"""APEX — Phase 1 vertical slice.

This package is a deliberately narrow implementation of one path through the
APEX specification: configuration, an RPC provider, a DEX adapter, and a
simulated quote. It exists to prove the specification is implementable before
the full system is built.

Phase 1 is simulation-only. `docs/apex-app-docs/execution/risk-policy/risk-engine.md`
states that in Phase 1 live execution is ALWAYS_REJECTED, so nothing in this
package signs, submits, or broadcasts a transaction. There is no wallet, no
private key handling, and no execution path to enable.
"""

__all__ = ["__version__"]

__version__ = "0.1.0"
