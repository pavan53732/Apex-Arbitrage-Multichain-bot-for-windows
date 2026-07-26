# Interface: Provider Adapter

## Purpose
Defines provider adapter request and response contracts.

## Methods
- ListModels().
- Infer(prompt, opts).
- HealthCheck().
- Capabilities().

## Validation
- `inference_timeout_ms` must be between 100 and 30000.
- `prompt` must be non-empty.
- `model_id` must be non-empty.
- `capabilities` must include streaming, tool_calling, embeddings, and vision flags.

## Cross-references
- `AI-PROVIDER-MANAGER.md`
- `AI-GATEWAY.md`
- `AI-PIPELINE.md`
