# Verification for Prompt 802

## Task: Verify that Prompt 802 executed correctly

**Folder that was processed:** `third-party\\bots`
**Expected feature name:** `Bots`

---

## Verification Steps

### Step 1: Read progress.md
Read the file `generated-prompts/progress.md` and check:
- Does it contain "Prompt 802: Executed"?
- Is the completion count updated?

### Step 2: Identify which .md file should own this feature
Based on the folder path `third-party\\bots`, determine the owner:
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
- Does the feature name match or relate to "Bots"?

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
VERIFICATION REPORT - PROMPT 802
==========================================

✅/❌ Progress.md contains "Prompt 802: Executed"
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
Say: "✅ Prompt 802 verified successfully. Ready for Prompt 803."

## If FAILED
List what needs to be fixed and suggest re-running Prompt 802.
