<!-- markdownlint-disable MD041 -->

You are operating in Cursor IDE with the Roo Code extension. Modes (Architect, Orchestra, Project Research, DevOps, Code) and agents (Qwen 3 Coder, DeepSeek 3.1, Grok Code Fast 1, etc.) are available.

Objective

- Process all prompts in `generated-prompts/` sequentially, one at a time. For each prompt: read it, execute its tasks, update `generated-prompts/progress.md`, then immediately continue to the next prompt. Do not read all prompts at once; enumerate and process one file at a time until all 842 are completed.

Why 842 prompts?
There are 842 prompt files in `generated-prompts/` (matching `prompt-*.md`). They define the complete scope of conversion work. The single-prompt flow runs them one-by-one to keep quality high and changes traceable.

Inputs (provide or extract if obvious)

- Prompt ID and filename (e.g., `generated-prompts/prompt-001-ai-modules.md`).
- Target feature file to update (e.g., `features/ai-modules.md`).
- Current working directory: workspace root (auto-detect).
- Ensure `features/` exists; create if missing.

Strict rules

- Process prompts strictly one at a time; no parallel or batch execution in memory.
- Auto-switch modes/agents only within this one-prompt lifecycle.
- Append-only edits; never delete or truncate existing content.
- Update only these two files: the chosen `features/*.md` and `generated-prompts/progress.md`.

Processing scope and order

- Enumerate files matching `generated-prompts/prompt-*.md` one at a time in numeric order (001 … 842).
- Determine the next unprocessed prompt by scanning `generated-prompts/progress.md` Execution Log (or using the Completed count as an index).
- Resume capability: on restart, skip prompts already logged as executed; continue from the next.
- If file enumeration fails, derive the next filename from Completed+1 (zero-padded to 3 digits). If that file doesn’t exist, increment and check the next ID until an existing prompt file is found; then continue.

Recommended mode/agent handoff

- Project Research Mode + DeepSeek 3.1: Understand the prompt, find referenced files/paths in the repo.
- Architect Mode + Qwen 3 Coder: Translate legacy paths into a Windows desktop feature design.
- Code Mode + Grok Code Fast 1: Append the feature section to the target `features/*.md`.
- DevOps Mode: Update `generated-prompts/progress.md` counters and append one execution log line.
- Return to Orchestra Mode and immediately continue to the next prompt without stopping. Do not wait for user confirmation. Process continuously until all 842 prompts are complete.

Feature output contract (append to target features file)

- Section title: `### Prompt XXX – [Feature Name]`
- Short summary: 2–4 bullets.
- Source paths discovered: bulleted list.
- Windows desktop implementation notes: 5–10 bullets.
- Dependencies or follow-ups: optional.

Progress update contract (edit `generated-prompts/progress.md`)

- Update the counters block at the top using exactly this text layout:
  - Total Prompts: 842
  - Started: [Date already present or set if missing]
  - Last Updated: today’s date
  - Completed: X/842 (increment X by 1 for each successful prompt)
  - Skipped: keep or increment if a prompt is intentionally skipped
  - Errors: increment by 1 for each failure
  - Status: In Progress (or Completed when X == 842)
  - Recent Completions: Prompt XXX (Feature: [Feature Name])

- Under “Execution Log”, append exactly:
  `Prompt XXX: Executed - Added 'Feature: [Feature Name]' to features/YYY.md`
 
Initialization

- If `generated-prompts/progress.md` does not exist, create it with initial counters:
  - Total Prompts: 842
  - Started: today’s date
  - Last Updated: today’s date
  - Completed: 0/842
  - Skipped: 0
  - Errors: 0
  - Status: In Progress
  - Recent Completions: (none)
  - Verify `generated-prompts/progress.md` is writable before starting.

Failure handling (sequential run)

- If a prompt fails, append a log entry with `Failed` and a brief reason (include a timestamp), increment Errors, and continue with the next prompt. Never delete or truncate files.
- If `features/` directory is missing at any point, create it automatically and continue.
- On a generic tool failure, retry the current step once. If it fails again, log the failure with a timestamp, increment Errors, and stop this run; resume from the next prompt on the next run.

Execution steps (loop until all prompts are completed)

1. Discover next unprocessed prompt file (by numeric order and Execution Log/Completed count).

2. Read the complete prompt thoroughly and execute all tasks it specifies. Read every line from start to finish. Execute all tasks and instructions contained within the prompt. Follow the Feature output contract and map to the correct `features/*.md` based on filename/content; append-only. Generate all required outputs and updates (do not summarize instead of performing the work).

3. Discover referenced files.

4. Draft the feature design.

5. Append the feature section to the correct `features/*.md`.

6. Update `generated-prompts/progress.md` counters and append the execution log line.

7. Continue with the next prompt until all 842 are processed.

Start now

Begin from the next unprocessed prompt (default 001 if none processed) and continue sequentially through all 842 without pausing.



 
