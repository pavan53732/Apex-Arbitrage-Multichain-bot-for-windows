# Verification Prompt for Prompt {PROMPT_NUMBER}

## Your Task: Verify Execution of Prompt {PROMPT_NUMBER}

You are verifying that **Prompt {PROMPT_NUMBER}** was executed correctly.

### What Prompt {PROMPT_NUMBER} Should Have Done:

**Folder Analyzed:** `{FOLDER_PATH}`
**Expected Feature Name:** `{FEATURE_NAME}`

### Verification Checklist:

Execute these checks in order:

#### 1. Check progress.md
```powershell
Get-Content "generated-prompts\progress.md" | Select-String "Prompt {PROMPT_NUMBER}:"
```
**Expected:** Should find entry like "Prompt {PROMPT_NUMBER}: Executed - Added 'Feature: [Name]' to features/[owner].md"

#### 2. Identify Owner File
Based on folder path `{FOLDER_PATH}`, determine which .md file should own this feature:
- ai-modules/* → ai-modules.md
- backend/* → backend.md
- dashboard/* → dashboard.md
- config/* → config.md
- contracts/* → contracts.md
- security/* → security.md
- tests/* → testing.md
- deploy/* → deployment.md
- docs/* → docs.md

#### 3. Check Owner File Has New Feature
```powershell
$ownerFile = "features\[owner].md"  # Replace [owner] with actual owner
Get-Content $ownerFile | Select-String "## Feature.*{FEATURE_NAME}"
```
**Expected:** Should find feature section with name containing "{FEATURE_NAME}"

#### 4. Verify Feature Content
```powershell
$content = Get-Content "features\[owner].md" -Raw
# Check for required sections
$content -match "Feature Files:"
$content -match "Technologies:"
$content -match "Windows Implementation:"
```
**Expected:** All three sections should exist

#### 5. Count Implementation Bullets
```powershell
$content = Get-Content "features\[owner].md" -Raw
$lastFeature = ($content -split "## Feature")[-1]
($lastFeature | Select-String "^- " -AllMatches).Matches.Count
```
**Expected:** Should be >= 8 bullets

#### 6. Check Reference Files Updated
Based on feature type, check if 1-4 reference files were updated with cross-references.

### Validation Report Format:

After running all checks, provide this report:

```
VERIFICATION REPORT - PROMPT {PROMPT_NUMBER}
================================

✅/❌ Progress.md updated
✅/❌ Owner file identified: [owner].md
✅/❌ Feature section added
✅/❌ Feature Files section present
✅/❌ Technologies section present
✅/❌ Windows Implementation section present
✅/❌ Minimum 8 implementation bullets
✅/❌ Reference files updated

OVERALL: ✅ PASSED / ❌ FAILED

Issues Found (if any):
- [List any issues]
```

### If Verification FAILS:

Provide specific details:
1. What was missing
2. What was incorrect
3. Suggested fix

### If Verification PASSES:

Confirm: "Prompt {PROMPT_NUMBER} executed correctly. Ready for Prompt {NEXT_PROMPT}."
