# AI Pipeline

## Purpose
Defines AI request routing, prompt lifecycle, provider routing, confidence scoring, and recovery.

## Ownership
- Owns AI request flow and structured response validation.
- Does not own execution authorization or trading policy.

## Windows concerns
- Must define proxy-aware requests, notification behavior, and local GPU fallback on Windows.
- Must define how AI state is restored after app restart.

## Cross-references
- `AI-PROVIDER-MANAGER.md`
- `MODEL-CAPABILITY-NEGOTIATION.md`
- `RUNTIME-OPERATIONS.md`
- `INTERFACE-AGENT-MESSAGE.md`
