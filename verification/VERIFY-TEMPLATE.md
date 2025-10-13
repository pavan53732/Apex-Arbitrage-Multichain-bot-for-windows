# Verification for Prompt {PROMPT_NUMBER}

## Task: Verify that Prompt {PROMPT_NUMBER} executed correctly

**Folder that was processed:** `{FOLDER_PATH}`
**Expected feature name:** `{FEATURE_NAME}`

---

## Verification Steps

### Step 1: Read progress.md
Read the file `generated-prompts/progress.md` and check:
- Does it contain "Prompt {PROMPT_NUMBER}: Executed"?
- Is the completion count updated?

### Step 2: Identify which .md file should own this feature
Based on the folder path `{FOLDER_PATH}`, determine the owner:
- `ai-modules/*` → features/ai-modules.md
- `backend/*` → features/backend.md
- `dashboard/*` → features/dashboard.md
- `config/*` → features/config.md
- `contracts/*` → features/contracts.md
- `security/*` → features/security.md
- `tests/*` → features/testing.md
- `deploy/*` → features/deployment.md
- `docs/*` → features/docs.md

### Step 3: Read the owner .md file
Read the identified owner file and verify:
- Does it contain a new "## Feature" section?
- Does the feature name match or relate to "{FEATURE_NAME}"?

### Step 4: Check feature content completeness
In the new feature section, verify these sections exist:
- [ ] "Feature Files:" section with file listings
- [ ] "Technologies:" section with detected tech stack
- [ ] "Windows Implementation:" section with implementation bullets

### Step 5: Count implementation bullets
Count the bullets in "Windows Implementation:" section:
- Must have at least 8 bullets
- Each bullet should describe WHAT, WHERE, HOW

### Step 6: Check reference files
Check if 1-4 other .md files were updated with cross-references to this feature.

---

## Verification Report

Provide this exact format:

```
VERIFICATION REPORT - PROMPT {PROMPT_NUMBER}
==========================================

✅/❌ Progress.md contains "Prompt {PROMPT_NUMBER}: Executed"
✅/❌ Owner file identified: [name].md
✅/❌ New feature section added
✅/❌ Feature Files section present
✅/❌ Technologies section present  
✅/❌ Windows Implementation section present
✅/❌ Has >= 8 implementation bullets (found: X)
✅/❌ Reference files updated (found: X files)

OVERALL: ✅ PASSED / ❌ FAILED

Issues (if any):
- [List specific issues]
```

---

## If PASSED
Say: "✅ Prompt {PROMPT_NUMBER} verified successfully. Ready for Prompt {NEXT_PROMPT}."

## If FAILED
List what needs to be fixed and suggest re-running Prompt {PROMPT_NUMBER}.
