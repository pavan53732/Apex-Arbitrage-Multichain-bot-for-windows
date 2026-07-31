---
metadata_schema_version: 1.0
document_id: DOC-0108
title: Context Priority Matrix
plane: Product Specification
domain: AI
class: Specification
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/context-priority-matrix.md
related_concepts:
  - CONCEPT-0108
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - AI
type: CONTRACT
purpose: "Defines the complete precedence hierarchy for all context segments injected into AI prompts — pinned, critical, session, knowledge, reflection, history, and external — with enforcement rules, capacity allocation, and pruning strategy."
scope: Context Priority Matrix scope and boundaries.
---

# Context Priority Matrix

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** AI Team

## Purpose
Defines the complete precedence hierarchy for all context segments injected into AI prompts — pinned, critical, session, knowledge, reflection, history, and external — with enforcement rules, capacity allocation, and pruning strategy.

---

## 1. Context Priority Tiers

| Tier | Priority Level | Segment Type | Can Be Pruned? | Prune Order | Max Token Allocation | Description |
|------|---------------|--------------|----------------|-------------|---------------------|-------------|
| **0** | Pinned | System prompt, agent role declaration, behavioral constraints | **Never** | — | 15% of `ai.context.max_tokens` | Always present; defines AI identity and safety boundaries |
| **1** | Critical | User current message, task instruction, constraint block | **Never** | — | 20% of `ai.context.max_tokens` | Core request that must be processed |
| **2** | Session | Current state snapshot (trading, wallet, risk, portfolio) | **Rarely** | Last to prune | 10% of `ai.context.max_tokens` | Live system state that drives decision-making |
| **3** | Knowledge | AI memory entries (recent, high-relevance) | **Yes** | 6th to prune | 15% of `ai.context.max_tokens` | Stored insights, facts, and learned patterns |
| **4** | Reflection | AI reflection results, self-assessment, decision audit trail | **Yes** | 5th to prune | 10% of `ai.context.max_tokens` | AI reasoning about its own prior decisions |
| **5** | History | Conversation history (prior turns, tool results) | **Yes** | 4th to prune | 15% of `ai.context.max_tokens` | Sequential exchange history |
| **6** | Tool Definitions | Registered tool schemas, capability descriptions | **Yes** | 3rd to prune | 10% of `ai.context.max_tokens` | Available tools the AI can invoke |
| **7** | Market Context | Price feeds, recent events, chain activity | **Yes** | 2nd to prune | 10% of `ai.context.max_tokens` | External market data enriching the prompt |
| **8** | External | Low-priority context: documentation references, general knowledge | **Yes** | **First to prune** | 5% of `ai.context.max_tokens` | Supplementary context; lowest value if space constrained |

---

## 2. Pruning Algorithm

When total assembled tokens exceed `ai.context.prune_threshold` (default: 85% of `ai.context.max_tokens`):

```
1. Calculate total tokens across all tiers.
2. If total ≤ prune_threshold → no pruning needed.
3. If total > prune_threshold → prune from highest prune order (8 → 7 → ... → 3):
   a. For each tier (from 8 down to 3):
      i. If tier is prunable and present:
         - Apply pruning action: Summarize → Truncate → Drop → Reference
         - Record action in prompt lifecycle audit trail.
      ii. Recalculate total tokens.
      iii. If total ≤ prune_threshold → stop pruning.
4. If total STILL > prune_threshold after pruning tiers 8–3:
   a. Prune Tier 2 (Session) with Truncate action only.
5. Tiers 0 and 1 are NEVER pruned (hard constraint).
6. If total STILL > prune_threshold after all prunable tiers:
   a. Abort prompt construction with error: "Context budget exceeded even after pruning."
   b. Emit system.error event.
   c. Return error to AI orchestrator.
```

### Pruning Actions (in priority order of application)

| Action | Description | Cost | When Applied |
|--------|-------------|------|--------------|
| **Reference** | Replace content with a lookup key `[memory:session_42]` | 0 tokens (key only) | First choice for knowledge, reflection, history |
| **Summarize** | LLM generates compressed summary of segment | 1 extra AI call (minimal tokens) | When reference lookup is impractical |
| **Truncate** | Keep first N tokens of segment (N = tier allocation × 0.5) | Reduced to N tokens | When summary is too expensive or not available |
| **Drop** | Remove entire segment | 0 tokens | Last resort when truncate is still over budget |

---

## 3. Context Capacity Allocation

| Tier | Allocation % | Default Tokens (8192 max) | Default Tokens (32768 max) | Dynamic? |
|------|-------------|---------------------------|----------------------------|----------|
| 0 Pinned | 15% | 1,228 | 4,915 | No (fixed) |
| 1 Critical | 20% | 1,638 | 6,554 | No (fixed) |
| 2 Session | 10% | 819 | 3,277 | Yes (may expand if tiers 3–8 are pruned) |
| 3 Knowledge | 15% | 1,228 | 4,915 | Yes (prunable, freed tokens go to session) |
| 4 Reflection | 10% | 819 | 3,277 | Yes (prunable) |
| 5 History | 15% | 1,228 | 4,915 | Yes (prunable) |
| 6 Tool Definitions | 10% | 819 | 3,277 | Yes (prunable — remove unused tools first) |
| 7 Market Context | 10% | 819 | 3,277 | Yes (prunable) |
| 8 External | 5% | 410 | 1,638 | Yes (first to prune) |

**Total allocation**: 100% of `ai.context.max_tokens`.

**Dynamic reallocation**: When higher-priority prunable tiers are pruned, freed tokens are redistributed to:
1. Session (Tier 2) — first (most valuable for current decision).
2. Knowledge (Tier 3) — second (if session already at max).

---

## 4. Segment Injection Order

Context segments are injected in strict order (see `./prompt-lifecycle.md` for assembly pipeline):

```
Order: 0 → 1 → 3 → 4 → 2 → 6 → 5 → 7 → 8
       System + User + Memory + Reflection + State + Tools + History + Market + External
```

The order ensures that:
- Never-pruned segments (0, 1) are always first.
- High-value prunable segments (3, 4) come before lower-value ones (7, 8).
- The pruning algorithm can determine cutoff points between segments.

---

## 5. Enforcement Rules

| Rule | Enforcement | Violation |
|------|-------------|-----------|
| Tier 0 (Pinned) must never be removed | Hardcoded constraint in context builder | Build error (cannot proceed) |
| Tier 1 (Critical) must never be removed | Hardcoded constraint in context builder | Build error (cannot proceed) |
| Total tokens must never exceed `ai.context.max_tokens` | Validation step in prompt lifecycle | Prompt construction aborted |
| Pruning must follow tier order (8 → 7 → ... → 3) | Pruning algorithm enforced in code | Architecture test violation |
| Dynamic reallocation must prioritize Tier 2 over Tier 3 | Allocation algorithm enforced | Architecture test violation |
| Each segment must declare its tier in the prompt metadata | Prompt lifecycle metadata | Validation error |

---

## 6. Observability

Every pruning action emits an event:

| Event | Payload |
|-------|---------|
| `ai.context.pruned` | `{tier, action, tokens_before, tokens_after, total_before, total_after}` |
| `ai.context.budget_exceeded` | `{total_tokens, max_tokens, prunable_tokens_remaining}` |

---

## Cross-References

- **PROMPT-LIFECYCLE.md** — Prompt construction pipeline that consumes this matrix.
- **AI-CONTEXT-WINDOW-MANAGEMENT.md** — Context window management policies.
- **AI-STATE-MACHINE.md** — AI state machine that drives context assembly.
- **AI-MEMORY.md** — Memory entries injected at Tier 3.
- **AI-REFLECTION.md** — Reflection entries injected at Tier 4.
- **AI-TOOLS.md** — Tool definitions injected at Tier 6.
- **TRACEABILITY-MATRIX.md** — REQ-AI-002, REQ-AI-005.
- **CONFIGURATION-REFERENCE.md** — `ai.context.*` config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Complete 9-tier priority matrix with capacity allocation, pruning algorithm, enforcement rules, observability | AI Team |
| 1.0.0 | 2025-01-15 | Initial stub (9 lines) | AI Team |
