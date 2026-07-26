# PERFORMANCE-TARGETS.md

## Purpose
Defines measurable performance targets for application startup, UI responsiveness, AI provider calls, quote freshness, database access, and execution orchestration.

## Related Documents
- [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md)
- [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md)

## Initial Targets
- cold start to interactive UI: under 3 seconds on supported hardware
- renderer route change: under 150 ms perceived latency
- settings save round-trip: under 300 ms local
- quote freshness during active scanning: under 5 seconds unless chain degraded
- structured AI response timeout: provider-configurable, default 20 seconds
