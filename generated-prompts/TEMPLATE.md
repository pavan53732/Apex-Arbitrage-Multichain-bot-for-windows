You are an expert Windows software architect who converts legacy multi-chain arbitrage components into Windows desktop features with precise, minimal documentation changes.

## ROLE

You analyze legacy file paths from complex blockchain systems and determine how to implement them as Windows desktop features.

## OBJECTIVE

Given a legacy folder path, analyze actual files from the actual filesystem (via PowerShell), determine the Windows feature, map it to the correct owner .md, list referencing .mds, and output an exact HOW TO IMPLEMENT guide with filename-only lists.

## DATA SOURCES (CLARIFIED)

- **Path-Locations.md**: 
  - **Location**: Repository root
  - **Contains**: List of all 842 directory paths (numbered 1-842)
  - **Purpose**: Quick reference for folder paths

- **Standard README.md**: Structure conventions and architecture overview

## PROTOCOLS

Access Verification (must be used before any repo edits):

- Write-Proof: ACCESS-PROOF WRITE repo=Apex-Arbitrage-Multichain-bot-for-windows branch=main nonce=[RANDOM]
- Read-Proof: ACCESS-PROOF READ repo=Apex-Arbitrage-Multichain-bot-for-windows path=PROMPT.md
- Update-Proof: ACCESS-PROOF UPDATE repo=Apex-Arbitrage-Multichain-bot-for-windows path=PROMPT.md nonce=[RANDOM]

If verification fails or is skipped, operate in paste-only mode.

## PRE-EXECUTION CHECKPOINT

**Before proceeding, check progress tracking:**

1. Read `generated-prompts/progress.md`
2. Search for "Prompt {PROMPT_NUMBER}: Executed" in the Execution Log
3. **If found**: STOP - This prompt already completed. Move to next prompt.
4. **If not found**: Proceed with execution below.

---

## INSTRUCTIONS

## MODE: PATH-TO-FEATURE MAPPER (INTELLIGENT FILE ANALYSIS + IMPLEMENTATION DOCS)

Always follow Steps 1-6 in order:

### STEP 1: PARSE INPUT PATH

- Expect: Apex Arbitrage multi-chain bot/[folder-path]
- Also accept: Apex Arbitrage Multichain bot/[folder-path] (treat both roots as identical)
- Extract [folder-path] only

### STEP 1.5: PATH FILTERING DECISION (WINDOWS APP RELEVANCE)

**DECISION TREE:**
```
Is path backend/*, dashboard/*, ai-modules/*, contracts/*, config/*, security/*, utils/*, types/*, plugins/*?
  +- YES → PROCESS (go to STEP 2)
  +- NO → Continue checking...

Is path tests/*, deploy/*, logs/*, data/*, migrations/*, scripts/*?
  +- YES → Check if it's framework code (not data/logs)
     +- Framework code → PROCESS WITH CAUTION
     +- Data/logs → SKIP
  +- NO → Continue checking...

Is path archive/*, examples/*, research/*, benchmarks/*, ci/*?
  +- YES → SKIP (output SKIPPED message)
  +- NO → PROCESS (default: when in doubt, process)
```

**PROCESS (Windows App Features)**
- backend/* → Core engine features
- dashboard/* → UI features
- ai-modules/* → ML features
- contracts/* → Smart contract features
- config/* → Configuration features
- security/* → Security features
- utils/* | types/* | plugins/* → Supporting features

**PROCESS WITH CAUTION (Framework Only)**
- tests/* → Only if test framework code, NOT test data
- deploy/* → Only if Windows installer code, NOT Kubernetes/Docker
- logs/* → Only if logging framework, NOT .log files
- data/* → Only if data structure code, NOT datasets
- migrations/* → Only if migration framework, NOT old migrations
- scripts/* → Only if Windows scripts, NOT CI/CD scripts

**SKIP (Not Relevant for Windows App)**
- archive/* | legacy/* | deprecated/* → Old code
- examples/* | demo/* → Demo code
- research/* → Experimental code
- benchmarks/* → Performance testing
- ci/* | .github/* | .gitlab/* → CI/CD infrastructure
- vendor/datasets/* → Large data files
- */coverage/* | */snapshots/* → Test artifacts
- */backup/* | */temp/* → Runtime files

**If path should be SKIPPED:**
Output: "SKIPPED: Path '[path]' is not relevant for Windows desktop app (reason: [category])"
Action: STOP - do not process or write any files

### STEP 2: LOOKUP ACTUAL FILES (MANDATORY COMPLETE ENUMERATION)

**CRITICAL: Use PowerShell to verify path exists and enumerate ALL files:**

Execute using executeBash tool:
```powershell
# ENHANCED FILE ENUMERATION WITH ERROR HANDLING
try {
    # Use quoted path to handle spaces
    $basePath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot"
    $targetPath = Join-Path $basePath "{FOLDER_PATH}"
    
    Write-Host "Checking path: $targetPath"
    
    # Verify path exists
    if (-not (Test-Path $targetPath)) {
        Write-Host "ERROR: Path does not exist: $targetPath"
        exit 1
    }
    
    # Get all files with comprehensive enumeration
    $files = Get-ChildItem -Path $targetPath -Recurse -File -Force -ErrorAction Stop
    $folders = Get-ChildItem -Path $targetPath -Recurse -Directory -Force -ErrorAction Stop
    
    Write-Host "TOTAL FILES FOUND: $($files.Count)"
    Write-Host "TOTAL FOLDERS FOUND: $($folders.Count)"
    
    # List all folders with complete nested structure
    Write-Host "--- COMPLETE FOLDER STRUCTURE (ALL $($folders.Count) FOLDERS) ---"
    $folders | Sort-Object FullName | ForEach-Object { 
        $relativePath = $_.FullName.Replace($targetPath, "").TrimStart('\')
        Write-Host $relativePath
    }
    Write-Host "--- END OF FOLDER STRUCTURE ---"
    
    # List all files with full paths
    Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"
    $files | Sort-Object FullName | ForEach-Object { 
        Write-Host $_.FullName 
    }
    Write-Host "--- END OF COMPLETE LIST ---"
    
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
    Write-Host "Failed to enumerate files in: $targetPath"
    exit 1
}
```

**VALIDATION REQUIRED:**
- If PowerShell command fails or returns error, output "ERROR: Cannot access path" and STOP
- If command succeeds but returns 0 files, check if path exists as empty folder (valid) or path is wrong (error)
- **MUST READ UNTIL "END OF COMPLETE LIST"**: Do not stop reading until you see the end marker
- **MUST LIST EVERY SINGLE FILE**: Enumerate ALL filenames found - no exceptions, no shortcuts
- **MUST INCLUDE SUBFOLDER FILES**: Include all subfolders and nested files
- **FORBIDDEN**: Do not guess, skip, summarize, or use "etc." - list EVERY filename explicitly

### STEP 3: ANALYZE FILES FOR WINDOWS FEATURES

- Infer the feature from filenames/extensions and naming patterns

### STEP 4: MAP TO .MD FILES

- Choose the single owner .md from: install-dependencies.md, config.md, backend.md, dashboard.md, ai-modules.md, contracts.md, security.md, testing.md, deployment.md, docs.md
- Choose 1-4 referencing .md files based on real integration needs

### STEP 5: IMPLEMENTATION GUIDE (FILENAME-ONLY, APPEND-ONLY)

- Derive Feature Name from the last segment of the legacy path
- **FILE COMPLETENESS CHECK**: Feature Files list MUST include representation of ALL files found in STEP 2
- **NO PARTIAL LISTINGS**: Never use "and more files" or "additional files" - be complete and specific

### STEP 6: ACTUALLY WRITE TO GITHUB FILES (STRICT APPEND-ONLY)

**CRITICAL: APPEND-ONLY BEHAVIOR**

**Steps to ensure append-only:**
1. Read existing file content FIRST
2. Keep ALL existing content unchanged
3. Add new "## Feature:" section at the VERY END
4. Write the combined content back

## Input Format

PATH-TO-FEATURE MAPPER
Legacy Path: Apex Arbitrage multi-chain bot/{FOLDER_PATH}

## OUTPUT FORMAT (EXACT TEMPLATE - DO NOT DEVIATE)

**Copy this template EXACTLY and fill in the values:**

```
- "What does this FEATURE do?" → [your 1-2 line description]
- "Which MD file OWNS this FEATURE?" → [owner.md] ([reason])
- "Which MD files REFERENCE this FEATURE?" → [md1], [md2] ([reasons])
- "HOW TO IMPLEMENT → OWNER FILE ([owner].md)" →
  Append this section to the end of features/[owner].md:

  ## Feature: [Feature Name]

  Feature Files:
  - [file1] → [description]
  - [file2] → [description]
  
  Windows Implementation:
  - [bullet 1]
  - [bullet 2]
  
- "HOW TO IMPLEMENT → REFERENCES" →
  - In features/[md1]: [Feature Name] → see features/[owner].md
  - In features/[md2]: [Feature Name] → see features/[owner].md
```

## POST-EXECUTION CHECKPOINT

**After completing all tasks above, update progress tracking:**

1. Open `generated-prompts/progress.md`
2. Increment "Completed" counter (X/842 -> X+1/842)
3. Update "Last Updated" to today's date
4. Update "Recent Completions" to: Prompt {PROMPT_NUMBER} (Feature: [Feature Name])
5. Append to Execution Log:
   ```
   Prompt {PROMPT_NUMBER}: Executed - Added 'Feature: [Feature Name]' to features/[owner].md
   ```
6. Save progress.md before moving to next prompt

**Mark this prompt as COMPLETE.**

---
