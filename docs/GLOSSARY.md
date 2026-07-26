# GLOSSARY.md

## Purpose
Defines canonical terminology for APEX so all documentation, code, UI labels, and AI-generated outputs use the same vocabulary.

## Scope
Covers trading, blockchain, AI, desktop, security, and internal project terms.

## Related Documents
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [STRATEGIES.md](./STRATEGIES.md)
- [RISK-ENGINE.md](./RISK-ENGINE.md)
- [AI-PIPELINE.md](./AI-PIPELINE.md)

## Core Terms
- **Opportunity**: a candidate profitable action detected by strategy logic before final execution approval.
- **Trade Plan**: a normalized execution proposal including route, cost estimate, and risk metadata.
- **Execution Pipeline**: the sequence from opportunity detection to signed transaction submission and result capture.
- **Risk Rejection**: a denied action based on policy, limit, or safety guard.
- **Provider Failover**: switching AI providers after availability, latency, or policy failure.
- **Renderer**: the Electron UI process.
- **Main Process**: the privileged Electron backend process.
- **Preload Bridge**: the restricted API surface exposed from privileged context to renderer.
