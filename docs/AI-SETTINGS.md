# AI Settings

## Purpose
Defines user-facing AI configuration, provider selection, fallback ordering, and cost controls.

## Policy
- Production AI uses cloud providers with paid API keys only.
- Local LLM inference is not supported in the production configuration.
- Provider enablement, ordering, and cost caps must match `AI-PIPELINE.md` and `CLOUD-AI-INTEGRATION.md`.

## Cross-references
- `AI-PIPELINE.md`
- `CLOUD-AI-INTEGRATION.md`
- `CONFIGURATION.md`
- `AI-CAPABILITY-MATRIX.md`
- `PROMPT-ENGINEERING.md`
- `AI-COST-MANAGEMENT.md`

## Governance Rules
Defines AI provider selection, model preferences, temperature, max tokens, streaming, vision, reasoning, JSON, embeddings, and save/test actions.

## Example
A balanced profile uses reasoning with a smaller context window and JSON output enabled.

## Validation
- Validate provider enablement against `AI-PROVIDER-MANAGER.md`.
- Validate capability requirements against `MODEL-CAPABILITY-NEGOTIATION.md`.
- Reject profiles that omit required provider, model, or cost settings.

## Lifecycle
- Settings are loaded at startup, validated before use, and revalidated on profile change.
- Provider lifecycle details remain owned by `AI-PROVIDER-MANAGER.md`.
