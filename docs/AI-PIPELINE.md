# APEX AI Pipeline - Cloud AI Provider Abstraction and Routing

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Overview

Abstraction layer between agents and cloud AI providers. Handles registration,
formatting, parsing, failover, rate limiting, caching. All cloud-based. No Docker.

### Goals
1. Provider-agnostic (agents unaware of provider)
2. Failover-resilient (auto fallback)
3. Cost-aware (cheapest equivalent)
4. Latency-optimized (fastest for time-sensitive)
5. Cache-friendly (TTL-based)

---

## 2. Architecture

Agent Orchestrator -> AI Pipeline Router -> [OpenAI Compat | Anthropic Native | Custom EP-1 | Custom EP-2] -> Cloud APIs

### Components
1. Provider Registry (from AI Settings)
2. Request Builder (per-provider format)
3. HTTP Client (HTTPS calls)
4. Response Parser (normalize)
5. Failover Manager (retry plus cascade)
6. Rate Limiter (token bucket)
7. Response Cache (memory plus SQLite)
8. Cost Tracker (tokens plus estimates)

---

## 3. Provider Interface

- provider_id, provider_type (openai_compatible or anthropic_native)
- base_url, api_key (encrypted), model_name
- max_tokens, temperature, is_enabled, priority
- rate_limit_rpm, rate_limit_tpm

### OpenAI-Compatible
- POST {base_url}/v1/chat/completions | Auth: Bearer {api_key}
- Compatible: OpenAI, Azure, Together, Groq, OpenRouter, DeepSeek, Mistral, Custom

### Anthropic Native
- POST {base_url}/v1/messages | Auth: x-api-key plus anthropic-version header
- System prompt as top-level field

---

## 4. Request Lifecycle

1. Agent submits request (system_prompt, user_prompt, temperature, max_tokens, format, priority, timeout)
2. Cache check (SHA-256 hash key)
3. Provider selection (filter enabled, sort priority, check rate limits)
4. Request formatting (per provider spec)
5. HTTPS call (timeout, retry headers)
6. Response parsing (extract content, tokens, validate schema)
7. Failover if needed (429/500/502/503/timeout -> next provider, max 3)
8. Cache store (TTL: 300s market, 3600s analysis)
9. Return normalized (content, tokens, provider, latency, cached, cost)

---

## 5. Rate Limiting

Token bucket per provider: RPM plus TPM buckets. Check before request, deduct after.
Defaults: OpenAI 500 RPM/150K TPM, Anthropic 300 RPM/100K TPM, Custom user-set.

---

## 6. Caching

- L1 In-Memory: 60s prices, 300s analysis
- L2 SQLite: 3600s analysis, 86400s static
- Key: SHA-256(provider_type + model + system_prompt + user_prompt + temperature)

---

## 7. Cost Tracking

Per request: provider, model, tokens, cost estimate, timestamp, agent, skill.
Pricing: gpt-4o $2.50/$10, gpt-4o-mini $0.15/$0.60, claude-sonnet $3/$15, claude-haiku $0.25/$1.25.

---

## 8. Error Handling

- AUTH (401/403): Alert user, skip provider
- RATE (429): Wait plus retry or failover
- SERVER (500/502/503): Failover
- TIMEOUT: Failover
- INVALID: Retry with correction
- NETWORK: Queue, alert

Retry: max 2/provider, exponential backoff (1s/2s/4s), max 3 failovers, 30s total.
Circuit breaker: 5 fails/60s -> open 120s -> half-open test -> close/reopen.

---

## 9. Security

- Keys NEVER in logs | Stored via safeStorage (DPAPI)
- HTTPS only | Cert pinning optional | Bodies not persisted | Cache has no keys

---

*Critical infrastructure. Reliable, fast, transparent.*
