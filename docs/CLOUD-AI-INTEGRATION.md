# APEX Cloud AI Integration Guide

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Overview

Cloud AI APIs exclusively. No local inference. No Docker. HTTPS to user-configured endpoints.
Supported: OpenAI-compatible, Anthropic native, any custom OpenAI-compatible endpoint.

---

## 2. OpenAI-Compatible

POST {base_url}/v1/chat/completions | Auth: Bearer {api_key}
Body: model, messages[{role,content}], temperature, max_tokens, response_format
Response: choices[0].message.content, usage.{prompt,completion,total}_tokens

Providers: OpenAI, Azure, Together, Groq, OpenRouter, DeepSeek, Mistral, Custom

---

## 3. Anthropic Native

POST {base_url}/v1/messages | Auth: x-api-key + anthropic-version: 2023-06-01
Body: model, system (top-level), messages[{role,content}], temperature, max_tokens (required)
Response: content[0].text, usage.{input,output}_tokens

Differences: system is top-level, x-api-key auth, max_tokens required, temp max 1.0

---

## 4. Abstraction Layer

Internal Request: system_prompt, user_prompt, temperature, max_tokens, response_format, timeout_ms
Internal Response: content, tokens{input,output,total}, provider_id, model, latency_ms, cached, cost_estimate
Adapters convert internal to/from provider-specific format.

---

## 5. Structured Output

OpenAI: response_format json_object | Anthropic: instruct via prompt, extract JSON
Schema enforcement: validate, retry once with correction, error if still invalid.

---

## 6. Prompt Standards

System: Role + Context + Task + Output format + Constraints + Examples (few-shot)
Budget: System <1000 tokens, User <3000, Response 2000-4096, Total <8000

---

## 7. Error Handling

400: no retry | 401/403: alert user, skip | 429: wait+retry | 500/502/503: failover | Timeout: failover
Degradation: All providers down -> alert, rule-based mode, retry 30s, auto-resume.

---

## 8. Security

Keys encrypted (safeStorage/DPAPI) | HTTPS only | No keys in URLs | Cert validation | Bodies not persisted

---

## 9. Cost Optimization

1. Caching (TTL) | 2. Model tiering (cheap for simple, expensive for complex)
3. Batching | 4. Truncation | 5. Frequency control | 6. Local rules first

---

*All AI cloud-based. No local inference. Update when adding providers.*
