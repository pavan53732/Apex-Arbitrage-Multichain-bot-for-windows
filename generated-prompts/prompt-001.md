## ðŸŽ¯ DELEGATION FLOW: COMPLETE ALL STEPS

**CRITICAL INSTRUCTION FOR AI AGENT:**

You WILL need to delegate to specialized modes. That's CORRECT. But you MUST COMPLETE the ENTIRE workflow:

**DELEGATION SEQUENCE:**

1. âœ... **DevOps mode** â†' Execute run_terminal_cmd tool to enumerate files

2. âœ... **Project Research mode** â†' Analyze file names and project structure

3. âœ... **Ask mode** â†' Read existing features/*.md files to count features

4. âœ... **Write mode** â†' Write COMPLETE feature documentation

5. **DevOps mode** - Delete temp files

**DO NOT STOP after step 1! COMPLETE ALL 5 STEPS!**

**If you delegate and wait for results, IMMEDIATELY process those results and continue to the NEXT step.**

**Your job is to ORCHESTRATE the COMPLETE workflow from start to finish in ONE session.**

---

You are an expert Windows software architect who converts legacy multi-chain arbitrage components into Windows desktop features with precise, minimal documentation changes.

## ROLE

You analyze legacy file paths from complex blockchain systems and determine how to implement them as Windows desktop features.

## OBJECTIVE

Given a legacy folder path, analyze actual files from the actual filesystem (via PowerShell), determine the Windows feature, map it to the correct owner .md, list referencing .mds, and output an exact HOW TO IMPLEMENT guide with filename-only lists.

---

## âš ï¸ CRITICAL STOP-CHECK BEFORE EXECUTION âš ï¸

**READ THIS FIRST - DO NOT SKIP:**

Before you begin, understand that this prompt has **MANDATORY REQUIREMENTS** that CANNOT be skipped or simplified:

### MANDATORY COMPLIANCE - ZERO TOLERANCE POLICY

**ABSOLUTE REQUIREMENTS:**
- LIST ALL 5000+ FILES (NO EXCEPTIONS)
- LIST ALL 1000+ FOLDERS (NO EXCEPTIONS)  
- WRITE 20-30 WORDS PER FILE (NO EXCEPTIONS)
- CONTINUE UNTIL 100% COMPLETE (NO EXCEPTIONS)

**INSTANT FAILURE CONDITIONS:**
- Using ... or etc = IMMEDIATE FAIL
- Using "and more" = IMMEDIATE FAIL
- Stopping early = IMMEDIATE FAIL
- Skipping ANY file = IMMEDIATE FAIL

**ENFORCEMENT:**
If you skip even 1 file out of 5000, YOU HAVE FAILED.
There is NO acceptable reason to not list a file.
CONTINUE LISTING until EVERY file is documented.

### âŒ FORBIDDEN SHORTCUTS:

- âŒ "and more files..." or "etc." - MUST list EVERY file
- âŒ Incomplete file counts - PowerShell shows 54 files? List ALL 54
- âŒ Missing Technologies section - REQUIRED
- âŒ Less than 8 Windows Implementation bullets - MINIMUM 8-12
- âŒ No references to other .md files - REQUIRED
- âŒ No features documentation update - REQUIRED
- âŒ No temp file cleanup - REQUIRED
- âŒ No feature numbering - MUST count existing features first

### ðŸš¨ MANDATORY: HANDLE 3000+ FILES WITHOUT SKIPPING ðŸš¨

**YOUR PROMPTS MUST HANDLE MASSIVE FOLDERS:**

- âœ... **3000+ files** â†' List EVERY SINGLE file with 20-30 word description
- âœ... **300+ folders** â†' Show COMPLETE nested tree structure
- âœ... **NO SHORTCUTS** â†' FORBIDDEN to skip, summarize, or use "etc."
- âœ... **NO TOKEN EXCUSES** â†' You have 1M token context window (750K words capacity)

**CALCULATION:**

- 3000 files Ã-- 30 words = 90,000 words
- 300 folders Ã-- 10 words = 3,000 words
- Total: ~93,000 words (only 12% of your 750K capacity)

**YOU HAVE 8X MORE CAPACITY THAN NEEDED!**

**IF YOU SKIP EVEN ONE FILE, THE OUTPUT IS REJECTED.**

**EXAMPLES OF WHAT YOU MUST DO:**

âœ... CORRECT (3000 files):

```
Found 3247 files in backend/plugins/

**DEX Adapters (2500 files):**
- uniswap-v2-adapter-001.js â†' Connects to Uniswap V2 mainnet contracts, handles swap routing through optimal pools, manages slippage protection with configurable thresholds, caches pool states in Redis for 30-second intervals to reduce RPC calls
- uniswap-v2-adapter-002.js â†' Implements batch swap functionality for Uniswap V2, aggregates multiple trades into single transaction, optimizes gas costs through multicall patterns, validates token approvals before execution
- uniswap-v3-adapter-001.js â†' Uniswap V3 adapter with concentrated liquidity support, tick-based pricing calculations, multi-hop routing optimization across fee tiers, real-time fee selection based on volatility metrics
... (LIST ALL 2500 FILES - NO SKIPPING)

**MANDATORY: Every single file MUST have:**
- Full filename with extension
- Arrow separator (â†')
- 20-30 word technical description
- NO shortcuts, NO summaries, NO grouping

**Test Files (500 files):**
- uniswap-v2-adapter-001.test.js â†' Unit tests for Uniswap V2 adapter covering swap execution, error handling, gas estimation, slippage calculations, integration with mock blockchain provider, edge cases for failed transactions
... (LIST ALL 500 FILES - NO SKIPPING)


**Config Files (247 files):**
- uniswap-config.json â†' Configuration for Uniswap V2/V3 contract addresses across mainnet, Polygon, Arbitrum, Optimism, includes router addresses, factory addresses, WETH addresses, default slippage settings
... (LIST ALL 247 FILES - NO SKIPPING)

```

âŒ WRONG (skipping):

```
- uniswap-v2-adapter-001.js â†' Uniswap adapter
- uniswap-v2-adapter-002.js â†' Another adapter
... and 2498 more files  â† FORBIDDEN! REJECTED!
```

**FOLDER TREE EXAMPLE (300 folders):**

âœ... CORRECT:

```
backend/
+-- plugins/
|   +-- dex-adapters/
|   |   +-- uniswap/
|   |   |   +-- v2/
|   |   |   |   +-- core/           â†' Core V2 swap logic
|   |   |   |   +-- router/         â†' V2 routing algorithms
|   |   |   |   +-- utils/          â†' V2 helper functions
|   |   |   +-- v3/
|   |   |   |   +-- core/           â†' Core V3 swap logic
|   |   |   |   +-- quoter/         â†' V3 price quotation
|   |   |   |   +-- position/       â†' V3 liquidity positions
|   |   |   +-- common/             â†' Shared Uniswap utilities
|   |   +-- sushiswap/
|   |   |   +-- core/               â†' SushiSwap core logic
|   |   |   +-- router/             â†' SushiSwap routing
... (SHOW ALL 300 FOLDERS - NO SKIPPING)
```

**VALIDATION BEFORE WRITING:

**CHUNKING STRATEGY FOR MASSIVE LISTS:**
- If output exceeds response limit, use CHUNKS
- Chunk 1: Files 1-500 with marker [CONTINUING IN NEXT RESPONSE]
- Chunk 2: Files 501-1000 with marker [CONTINUING FROM PREVIOUS]
- Continue until ALL files are listed
- NEVER skip files between chunks
**

- [ ] PowerShell found 3247 files â†' My output lists 3247 files âœ...
- [ ] PowerShell found 312 folders â†' My folder tree shows 312 folders âœ...
- [ ] Every file has 20-30 word description âœ...
- [ ] No "etc.", "and more", or "..." shortcuts âœ...

**IF ANY CHECK FAILS: STOP AND FIX IT BEFORE WRITING FILES.**

### âœ... QUALITY STANDARDS:

1. **File Enumeration**: If PowerShell finds 54 files, your Feature Files section MUST list all 54 files with descriptions
1. **COMPLETE Grouping**: Group ALL files by purpose - no file left behind
2. **Accurate Counts**: "Core Logic (5 files)" means list exactly 5 files in that group
3. **Technologies**: Detect from file extensions and list them
4. **Windows Implementation**: Write 8-12 detailed, specific bullets
6. **References**: Add feature name to 2-4 other .md files
7. **Progress Update**: Increment counter, update date, add log entry
8. **Cleanup**: Delete temp_*.ps1 files you created
9. **Complete Folder Structure**: Use numbered format 'FOLDER X/Y: foldername/' and 'FILE X/Y: filename.ext' for ALL folders and files; numbering resets per level, folder/file counters are separate, and ordering is folders-first then files (A->Z) at each level

### ðŸ" SELF-CHECK BEFORE WRITING:

Ask yourself:

- [ ] Did I list EVERY file from PowerShell output?
- [ ] Did I count existing features in target .md file?
- [ ] Did I add Technologies section?
- [ ] Did I write 8-12 Windows Implementation bullets?
- [ ] Did I add references to other .md files?
- [ ] Will I delete temp files after completion?

**If you answer NO to ANY question above, DO NOT PROCEED. Go back and COMPLETE it.**

### ðŸ"Š EXAMPLE OF COMPLETE OUTPUT:

```
## Feature 1: Ai Modules â­â­â­â­â­ (Highly Complex - 54 files)

Feature Files:

Core Logic (5 files):
- ai-engine.js â†' Core AI processing
- decisionMaker.js â†' Decision logic
- patternLearner.js â†' Pattern recognition
- scoreArbOpportunity.js â†' Scoring
- modelRouter.js â†' Model routing

[... LIST ALL OTHER 49 FILES IN GROUPS ...]

Technologies: Python, PyTorch, ONNX, Jupyter, Node.js

Windows Implementation:
- Install Python 3.9+ with PyTorch via pip in isolated virtual environment
- Store model weights in application data directory with version control
- Schedule model retraining using Windows Task Scheduler
- Integrate with dashboard via REST API for real-time predictions
- Cache predictions in SQLite database for performance
- Log AI decisions to Windows Event Log for audit trail
- Use Windows ML for hardware-accelerated inference
- Secure API keys using Windows Credential Manager
- Enable auto-updates through Windows update mechanism
- Display AI insights in Electron dashboard with WebGL
- Implement model rollback using file system snapshots
- Monitor AI performance with Windows Performance Counters
```

**This is the MINIMUM acceptable quality. Anything less is INCOMPLETE.**

## Feature 2: Explainability â­â­ (Moderate - 12 files)

Feature Files:

Core Logic (3 files):
- shap-explainer.py â†' SHAP value calculation
- lime-interpreter.py â†' LIME interpretation
- feature-importance.py â†' Feature importance analysis

Visualization (4 files):
- explanation-charts.js â†' Interactive explanation charts
- model-insights.html â†' Explanation dashboard
- report-generator.py â†' PDF report generation
- visualization-utils.js â†' Chart utilities

Configuration (2 files):
- explainability-config.json â†' Explanation settings
- model-metadata.json â†' Model information

Tests (3 files):
- test-shap.py â†' SHAP explanation tests
- test-lime.py â†' LIME explanation tests
- test-visualization.js â†' Chart rendering tests

Technologies: Python, SHAP, LIME, Matplotlib, JavaScript, HTML

Windows Implementation:
- Install Python ML libraries via pip in isolated virtual environment
- Store explanation outputs in application data directory
- Generate visualizations using matplotlib with Windows-compatible backends
- Integrate with dashboard via REST API for real-time explanations
- Cache SHAP values in SQLite database for performance
- Schedule batch explanation jobs using Windows Task Scheduler
- Log explanation requests to Windows Event Log
- Provide explanation export in PDF format using reportlab
- Display interactive charts in Electron dashboard
- Secure explanation data using Windows Credential Manager
- Enable real-time model interpretation updates
- Monitor explanation performance with Windows Performance Counters

## DATA SOURCES

- **Path-Locations.md**: List of all 842 directory paths (numbered 1-842)
- **Standard README.md**: Structure conventions and architecture overview

---

## INSTRUCTIONS

## MODE: PATH-TO-FEATURE MAPPER (INTELLIGENT FILE ANALYSIS + IMPLEMENTATION DOCS)

Always follow Steps 1-5 in order:

### STEP 1: PARSE INPUT PATH

- Expect: Apex Arbitrage multi-chain bot/[folder-path]
- Also accept: Apex Arbitrage Multichain bot/[folder-path] (treat both roots as identical)
- Extract [folder-path] only

### STEP 1.5: MANDATORY PROCESSING REQUIREMENT

**CRITICAL**: ALL folders MUST be processed for COMPLETE feature collection.

```
C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\ai-modules
```

**NO EXCEPTIONS**: Every folder (including archive, examples, research, benchmarks, ci, tests, data, logs, etc.) contains valuable features that must be documented.

**PROCEED TO STEP 2** - No skipping allowed.

### STEP 2: LOOKUP ACTUAL FILES (MANDATORY COMPLETE ENUMERATION)

**CRITICAL: Use PowerShell to verify path exists and enumerate ALL files:**

**EXECUTION INSTRUCTIONS:**

1. Copy the PowerShell code block below EXACTLY as written
1. Execute using run_terminal_cmd tool (PowerShell)
2. Do NOT modify, interpret, or break up the code
3. Execute the ENTIRE block as ONE command

**POWERSHELL COMMAND TO EXECUTE:**

```powershell
try {
    $basePath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot"
    $targetPath = Join-Path $basePath "ai-modules"
    
    Write-Host "Checking path: $targetPath"
    
    if (-not (Test-Path $targetPath)) {
        Write-Host "ERROR: Path does not exist: $targetPath"
        exit 1
    }
    
    $files = Get-ChildItem -Path $targetPath -Recurse -File -Force -ErrorAction Stop
    $folders = Get-ChildItem -Path $targetPath -Recurse -Directory -Force -ErrorAction Stop
    
    Write-Host "TOTAL FILES FOUND: $($files.Count)"
    Write-Host "TOTAL FOLDERS FOUND: $($folders.Count)"
    
    Write-Host "--- COMPLETE FOLDER STRUCTURE (ALL $($folders.Count) FOLDERS) ---"
    $folders | Sort-Object FullName | ForEach-Object { 
        $relativePath = $_.FullName.Replace($targetPath, "").TrimStart('\')
        Write-Host $relativePath
    }
    Write-Host "--- END OF FOLDER STRUCTURE ---"
    
    # Check if we need chunking for large folders
    if ($files.Count -gt 500) {
        Write-Host "LARGE FOLDER: $($files.Count) files - Processing in chunks"
    }
    Write-Host "REMINDER: Must list EVERY file - Use CHUNKS if needed"`
Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"
    $fileIndex = 1
    $files | Sort-Object FullName | ForEach-Object { 
        Write-Host "FILE $fileIndex/$($files.Count): $($_.FullName)"
        $fileIndex++
    }
    Write-Host "--- END OF COMPLETE LIST ---"
    
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
    Write-Host "Failed to enumerate files in: $targetPath"
    exit 1
}
```

**IMPORTANT:** Execute this PowerShell script using run_terminal_cmd tool. Do NOT break it into individual characters or lines.

**ðŸš¨ MANDATORY COUNT VALIDATION - ZERO TOLERANCE ðŸš¨**

**CRITICAL: BEFORE YOU WRITE ANY ANALYSIS, YOU MUST:**

1. **EXECUTE POWERSHELL COMMAND** using run_terminal_cmd tool
2. **READ THE EXACT OUTPUT** until you see "END OF COMPLETE LIST"
3. **EXTRACT THE EXACT NUMBERS** from PowerShell output:
   - Look for "TOTAL FILES FOUND: [NUMBER]"
   - Look for "TOTAL FOLDERS FOUND: [NUMBER]"
4. **VERIFY YOUR ANALYSIS MATCHES EXACTLY**:
   - If PowerShell says "TOTAL FILES FOUND: 54" â†' Your analysis MUST say "54 files"
   - If PowerShell says "TOTAL FOLDERS FOUND: 10" â†' Your analysis MUST say "10 folders"
   - **NO EXCEPTIONS, NO APPROXIMATIONS, NO ROUNDING**

**INSTANT FAILURE CONDITIONS:**
- If PowerShell shows 54 files but you report 59 files = IMMEDIATE FAILURE
- If PowerShell shows 10 folders but you report 8 folders = IMMEDIATE FAILURE
- If you don't execute the PowerShell command = IMMEDIATE FAILURE
- If you don't read the full output = IMMEDIATE FAILURE

**MANDATORY VALIDATION STEPS:**
1. âœ... **Step 1**: Execute PowerShell command using run_terminal_cmd
2. âœ... **Step 2**: Read complete output until "END OF COMPLETE LIST"
3. âœ... **Step 3**: Extract exact numbers from PowerShell output
4. âœ... **Step 4**: State the exact numbers in your analysis
5. âœ... **Step 5**: Verify your file list count matches PowerShell count
6. âœ... **Step 6**: Verify your folder count matches PowerShell count

**ðŸš¨ MANDATORY OUTPUT FORMAT - COPY THIS EXACTLY ðŸš¨**

**BEFORE YOU WRITE ANY ANALYSIS, YOU MUST OUTPUT THIS EXACT FORMAT:**

```
STEP 1: FILE ENUMERATION COMPLETE
[FOLDER-NAME] FILE ENUMERATION RESULTS
TOTAL FILES FOUND: [EXACT NUMBER FROM POWERSHELL]
TOTAL FOLDERS FOUND: [EXACT NUMBER FROM POWERSHELL]

FOLDER STRUCTURE:
[LIST ALL FOLDERS FROM POWERSHELL OUTPUT]

FILE LIST: [EXACT NUMBER] FILES
[LIST ALL FILES FROM POWERSHELL OUTPUT]

ANALYSIS:
Total folder size: [EXACT NUMBER] files across [EXACT NUMBER] folders
File types: [DETECTED TYPES]
Structure shows [DESCRIPTION]
The enumeration is complete and ready for the next step in the process.
```

**CRITICAL RULES:**
- Replace [EXACT NUMBER FROM POWERSHELL] with the actual numbers from PowerShell output
- Replace [LIST ALL FOLDERS] with the actual folder list from PowerShell
- Replace [LIST ALL FILES] with the actual file list from PowerShell
- **DO NOT GUESS OR APPROXIMATE** - use only what PowerShell actually found
- **IF POWERSHELL SHOWS 54 FILES, YOU MUST SHOW 54 FILES**
- **IF POWERSHELL SHOWS 10 FOLDERS, YOU MUST SHOW 10 FOLDERS**

**ðŸš¨ FINAL VALIDATION CHECK - MANDATORY ðŸš¨**

**BEFORE YOU PROCEED TO STEP 3, YOU MUST VERIFY:**

1. **COUNT VERIFICATION**: 
   - PowerShell said: "TOTAL FILES FOUND: [X]"
   - Your analysis says: "[X] files"
   - âœ... MATCH = Continue
   - âŒ MISMATCH = STOP and fix immediately

2. **FOLDER COUNT VERIFICATION**:
   - PowerShell said: "TOTAL FOLDERS FOUND: [Y]"
   - Your analysis says: "[Y] folders"
   - âœ... MATCH = Continue
   - âŒ MISMATCH = STOP and fix immediately

3. **FILE LIST VERIFICATION**:
   - PowerShell listed [X] files
   - Your analysis lists [X] files
   - âœ... MATCH = Continue
   - âŒ MISMATCH = STOP and fix immediately

**IF ANY VERIFICATION FAILS:**
- STOP immediately
- Go back to PowerShell output
- Re-read the exact numbers
- Fix your analysis to match exactly
- DO NOT proceed until all counts match perfectly

**EXAMPLE OF CORRECT VALIDATION:**
```
PowerShell Output: "TOTAL FILES FOUND: 54"
My Analysis: "TOTAL FILES FOUND: 54"
âœ... VERIFICATION PASSED - Counts match exactly

PowerShell Output: "TOTAL FOLDERS FOUND: 10"  
My Analysis: "TOTAL FOLDERS FOUND: 10"
âœ... VERIFICATION PASSED - Counts match exactly
```

**EXAMPLE OF INCORRECT VALIDATION (FAILURE):**
```
PowerShell Output: "TOTAL FILES FOUND: 54"
My Analysis: "TOTAL FILES FOUND: 59"
âŒ VERIFICATION FAILED - Counts do not match
STOP: Fix the count to match PowerShell exactly
```


**VALIDATION REQUIRED:
- If PowerShell command fails or returns error, output "ERROR: Cannot access path" and STOP
- If command succeeds but returns 0 files, check if path exists as empty folder (valid) or path is wrong (error)
- **MUST READ UNTIL "END OF COMPLETE LIST"**: Do not stop reading until you see the end marker
- **MUST LIST EVERY SINGLE FILE**: Enumerate ALL filenames found - no exceptions, no shortcuts
- **MUST INCLUDE SUBFOLDER FILES**: Include all subfolders and nested files
- **FORBIDDEN**: Do not guess, skip, summarize, or use "etc.", "...", "and more files", "additional files", "similar files", "plus X more" - list EVERY filename explicitly
- **VERIFICATION**: Count total files found and state the count explicitly: "Found [N] files in [folder-path]"
- **COUNT MATCHING**: Your file list count MUST match PowerShell count exactly or you FAILED
- **FEATURE NUMBERING**: Always start with "Feature #X:" where X is the prompt number
- **COMPLETE COUNTING**: State exact counts: "Total Files: [N], Total Folders: [M], Total Nested Levels: [L]"
- **SUMMARY FORMAT**: Begin analysis with: "Feature #[X]: [Feature Name] - Found [N] files across [M] folders"
- **MANDATORY COUNTS**: PowerShell already shows counts, but AI must restate them in analysis
- **STRUCTURED OUTPUT**: Format all analysis as numbered features with COMPLETE file/folder counts
- **VERIFICATION CHECKLIST**: 
- **SCAFFOLDED FILES**: Even if files are empty placeholders, they MUST be analyzed for feature intent from filename patterns
- **MINIMUM REQUIREMENT**: If folder has 50+ files, list ALL 50+ files by name
- **NO SHORTCUTS ALLOWED**: If PowerShell shows 60 files, you MUST list all 60 files individually with descriptions

**FILE ENUMERATION EXAMPLES:**

**WRONG (Incomplete):**
```
Found 10 files in backend/plugins/dex-adapters:
- uniswap-v2-adapter.js
- sushiswap-adapter.js
- ... (8 more files)  â† FORBIDDEN!
- and more files  â† FORBIDDEN!
- plus 8 additional files  â† FORBIDDEN!
- similar files  â† FORBIDDEN!
```

**CORRECT (COMPLETE):**
```
Found 10 files in backend/plugins/dex-adapters:
- uniswap-v2-adapter.js
- uniswap-v3-adapter.js
- sushiswap-adapter.js
- curve-adapter.js
- balancer-adapter.js
- adapter-base.js
- adapter-factory.js
- adapter-registry.js
- adapter-config.json
- adapter-utils.js
```

**Rule:** List EVERY SINGLE file by name. No shortcuts. No "etc." No "and more". No "...". No "additional files". No "similar files". No "plus X more". COUNT MUST MATCH POWERSHELL OUTPUT EXACTLY.

**LARGE FOLDER HANDLING (100+ files):**
If folder has 100+ files, list ALL files but group by type for readability:
```
Found 150 files in backend/plugins:

JavaScript files (120):
- adapter-1.js â†' Description
- adapter-2.js â†' Description
- adapter-3.js â†' Description
... (list ALL 120 files individually with descriptions)

Test files (20):
- test-1.test.js â†' Description
- test-2.test.js â†' Description
... (list ALL 20 files individually with descriptions)

Config files (10):
- config-1.json â†' Description
- config-2.json â†' Description
... (list ALL 10 files individually with descriptions)
```
Still list EVERY file individually with descriptions. FORBIDDEN to use "etc." or "and more files". Your count MUST equal 150 total entries.

### STEP 2.5: SUBFOLDER HANDLING

**Rule:** Process the specified folder INCLUDING all files in its subfolders recursively, but treat them as ONE feature (do not create separate features for subfolders).

**Example:**
- Input: `backend/plugins/dex-adapters`
- Include files in: `backend/plugins/dex-adapters/*.js`
- Include files in: `backend/plugins/dex-adapters/tests/*.js` (subfolder files)
- DO NOT process `backend/plugins/dex-adapters/tests/` as separate feature

**All files in all subfolders belong to the SAME feature.**

### STEP 3: ANALYZE FILES FOR WINDOWS FEATURES

- Infer the feature from filenames/extensions and naming patterns

### DECISION TREES FOR COMPLEX SCENARIOS

**Scenario A: Multiple File Types in Same Folder**
```
IF folder contains: .js + .json + .md files
THEN: Primary feature = JavaScript functionality
     Secondary features = Configuration + Documentation
     Owner = Based on primary functionality
     References = Mention secondary features

EXAMPLE: backend/plugins/dex-adapters/
- adapter.js (primary) â†' Dex Adapters feature
- config.json (secondary) â†' Configuration
- README.md (secondary) â†' Documentation
```

**Scenario B: Empty or Scaffolded Folders**
```
IF folder exists but PowerShell finds 0 files
THEN: Feature = Scaffolded [Folder Name]
     Owner = Based on parent path context
     Implementation = "Awaiting development"

EXAMPLE: ai-modules/models/training/
- Empty folder â†' Scaffolded Training Models feature
- Owner = ai-modules.md (based on parent path)
```

**Scenario C: Mixed Legacy/Windows Files**
```
IF folder contains both legacy + Windows files
THEN: Focus on Windows-compatible files
     Legacy files = Reference only
     Owner = Windows functionality

EXAMPLE: dashboard/components/
- legacy-component.js (legacy) â†' Reference only
- windows-component.tsx (Windows) â†' Primary feature
```

**Scenario D: Deeply Nested Structures**
```
IF folder has 3+ levels of nesting
THEN: Process as single feature (not separate sub-features)
     Include all nested files in analysis
     Owner = Based on root folder purpose

EXAMPLE: backend/engine/core/adapters/dex/
- All files belong to "Dex Adapters" feature
- Do not create separate features for each level
```

### CLEAR EXAMPLES: CORRECT vs INCORRECT OUTPUTS

**CORRECT Output Example:**
```
Feature #1: Ai Modules - Found 54 files across 10 folders

- "What does this FEATURE do?" â†' Provides AI-powered trading modules and machine learning capabilities
- "Which MD file OWNS this FEATURE?" â†' ai-modules.md (core AI functionality)
- "Which MD files REFERENCE this FEATURE?" â†' backend.md (integration), dashboard.md (UI)
- "HOW TO IMPLEMENT â†' OWNER FILE (ai-modules.md)" â†'
  Append this section to the end of features/ai-modules.md:
  
  ## Feature 1: Ai Modules
  
  Feature Files:
  - ai-engine.js â†' Core AI processing engine
  - ml-models.json â†' Machine learning model configurations
  - training-data.csv â†' Training datasets for AI models
  
  Windows Implementation:
  - Implement as Windows Service for background AI processing
  - Use Windows ML for local model inference
  - Integrate with Windows Task Scheduler for periodic retraining

- "HOW TO IMPLEMENT â†' REFERENCES" â†'
  - In features/backend.md: Ai Modules â†' see features/ai-modules.md
  - In features/dashboard.md: Ai Modules â†' see features/ai-modules.md
```

**INCORRECT Output Example:**
```
âŒ WRONG - Missing feature numbering
Ai Modules Analysis

âŒ WRONG - Incomplete file listing
Found some files in ai-modules:
- ai-engine.js
- ... (other files)  â† FORBIDDEN!

âŒ WRONG - Missing counts
Feature has various files across multiple folders

âŒ WRONG - Vague implementation
Windows Implementation:
- Make it work on Windows  â† TOO VAGUE!

âŒ WRONG - Missing structured format
The ai-modules feature MUST be implemented by adding files to the appropriate location and ensuring compatibility with the Windows environment.
```

**CONFIDENCE SCORING EXAMPLES:**

**High Confidence (9-10):**
- PowerShell found exact expected file count
- Feature name clearly matches folder purpose
- Owner file assignment is obvious
- All validation checks pass

**Medium Confidence (6-8):**
- PowerShell found most expected files
- Feature name requires some interpretation
- Owner file assignment has alternatives
- Most validation checks pass

**Low Confidence (1-5):**
- PowerShell found significantly fewer files than expected
- Feature name is unclear or ambiguous
- Owner file assignment is uncertain
- Validation checks fail

**If confidence < 7: STOP and request clarification before proceeding**

### STEP 4: MAP TO .MD FILES

- Choose the single owner .md from: install-dependencies.md, config.md, backend.md, dashboard.md, ai-modules.md, contracts.md, security.md, testing.md, deployment.md, docs.md
- Choose 1-4 referencing .md files based on real integration needs

### STEP 5: IMPLEMENTATION GUIDE

**ENHANCED OUTPUT FORMAT WITH FOLDER TREE AND DETAILED DESCRIPTIONS:**

### ðŸš¨ MANDATORY FOLDER TREE SECTION ðŸš¨

**CRITICAL**: You MUST include a COMPLETE folder tree structure showing ALL nested folders AND ALL FILES.

**FORBIDDEN**: Skipping the folder tree section will result in REJECTED output.

**REQUIRED FORMAT:**

### ðŸ"¢ MANDATORY NUMBERING FORMAT

**CRITICAL**: Every folder and file MUST be numbered:

**Folder Format:** `FOLDER X/Y: foldername/` where X = current, Y = total
**File Format:** `FILE X/Y: filename.ext` where X = current, Y = total

**Numbering Rules (STRICT):**
- Per-level reset: Each folder level restarts numbering at 1 for its immediate children (e.g., 1/3, 2/3, 3/3). Do NOT carry numbers across different parent folders.
- Separate sequences: Folder numbering and file numbering are independent. Do NOT interleave or share counters between folders and files.
- Folder totals (Y): Count ONLY sibling folders at that level (exclude files). Example: If a folder has 3 subfolders and 5 files, folder Y = 3.
- File totals (Y): Count ONLY files within that single folder (exclude subfolders). Example: If a folder has 7 files and 2 subfolders, file Y = 7.
- Sequential within scope: Files in a folder must be numbered FILE 1/Y, 2/Y, ..., Y/Y; subfolders at a level must be FOLDER 1/Y, 2/Y, ..., Y/Y.
- Example clarity: Use 1/3 then 1/2 for a child level, NOT 1/3 then 4/5. Each level resets.
- Deterministic ordering: At every folder level, list all subfolders first (sorted Aâ†'Z), then list all files (sorted Aâ†'Z) before descending into deeper levels.
- Exact counts: Compute Y from actual discovered items at that level; never guess or reuse counts from other levels.

**Example:**

```
FOLDER 1/11: backend/contracts/
â"œâ"€â"€ FOLDER 2/11: docs/
â"‚ â"œâ"€â"€ FILE 1/125: README.md
â"‚ â"œâ"€â"€ FILE 2/125: GOVERNANCE.md
â"‚ â""â"€â"€ FILE 3/125: SECURITY.md
â"œâ"€â"€ FOLDER 3/11: interfaces/
â"‚ â"œâ"€â"€ FILE 4/125: IAIAgentInterface.sol
â"‚ â""â"€â"€ FILE 5/125: IAlphaNFT.sol
```

**FORBIDDEN**: Listing without `FOLDER X/Y:` or `FILE X/Y:` prefix

```
Folder Structure:

ai-modules/
â"œâ"€â"€ datasets/
â"‚   â"œâ"€â"€ ai-decision-corpus.json
â"‚   â"œâ"€â"€ features.csv
â"‚   â"œâ"€â"€ profitLabels.json
â"‚   â"œâ"€â"€ trade-history.csv
â"‚   â""â"€â"€ README.md
â"œâ"€â"€ features/
â"‚   â"œâ"€â"€ featureExtractor.js
â"‚   â"œâ"€â"€ gasFeeSpikeFeature.js
â"‚   â"œâ"€â"€ latencyProfileFeature.js
â"‚   â"œâ"€â"€ priceDeltaFeature.js
â"‚   â""â"€â"€ README.md
â"œâ"€â"€ models/
â"‚   â"œâ"€â"€ modelWeights/
â"‚   â"‚   â"œâ"€â"€ decisionNet-v1.pt
â"‚   â"‚   â"œâ"€â"€ patternNet-v2.onnx
â"‚   â"‚   â"œâ"€â"€ scorerModel.json
â"‚   â"‚   â"œâ"€â"€ volatilityClassifier.pkl
â"‚   â"‚   â""â"€â"€ README.md
â"‚   â"œâ"€â"€ trainingOutputs/
â"‚   â"‚   â"œâ"€â"€ accuracy-report.txt
â"‚   â"‚   â"œâ"€â"€ token-risk-score-histogram.png
â"‚   â"‚   â"œâ"€â"€ trade-learning-curve.png
â"‚   â"‚   â""â"€â"€ README.md
â"‚   â""â"€â"€ README.md
â""â"€â"€ [LIST ALL OTHER FOLDERS AND FILES]
```


- Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering (folders first, then files) at each level
- âœ... Show COMPLETE nesting hierarchy for ALL subfolders
- âœ... List EVERY SINGLE FILE in EVERY folder
- âœ... Use tree characters properly (â"œâ"€â"€, â"‚, â""â"€â"€)
- âœ... If PowerShell shows 10 folders, your tree MUST show all 10 folders
- âœ... If PowerShell shows 54 files, your tree MUST show all 54 files
- Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering (folders first, then files) at each level
- âŒ FORBIDDEN: Skipping folders or using "and more folders"
- âŒ FORBIDDEN: Skipping files or using "and more files"
- âŒ FORBIDDEN: Not including the folder tree section
- âŒ FORBIDDEN: Using "[LIST ALL OTHER FILES]" without actually listing them

**VERIFICATION**: 
- Count folders in your tree â†' Must match PowerShell folder count
- Count files in your tree â†' Must match PowerShell file count

ðŸ" **NESTED FOLDER DEPTH VERIFICATION:**
- Count folder depth levels in your tree structure
- Compare against PowerShell output showing deepest path
- If PowerShell shows 8-level nesting, your tree MUST show all 8 levels
- FORBIDDEN: Collapsing nested folders like "parent/child/grandchild" into single line
- REQUIRED: Full tree expansion showing every subfolder at every level

### ðŸ"‹ OUTPUT QUALITY EXAMPLES

âŒ **INCORRECT - FORBIDDEN**:
```
## Folder Structure
- src/
  - Multiple configuration files
  - Various utility scripts (15 files)
  - And more...
```

âœ... **CORRECT - REQUIRED**:
```
## Folder Structure
src/
â"œâ"€â"€ config/
â"‚   â"œâ"€â"€ database.config.js
â"‚   â"œâ"€â"€ api.config.js
â"‚   â"œâ"€â"€ security.config.js
â"œâ"€â"€ utils/
â"‚   â"œâ"€â"€ logger.util.js
â"‚   â"œâ"€â"€ validator.util.js
â"‚   â"œâ"€â"€ formatter.util.js
[... continues for ALL files]
```

âŒ **INCORRECT - FORBIDDEN**:
```
### database.config.js
Configuration file for database settings.
```

âœ... **CORRECT - REQUIRED**:
```
### database.config.js (23 words)
Manages SQLite database connection pooling, query timeout configurations, transaction isolation levels, automatic backup scheduling, and Windows-specific file locking mechanisms for concurrent access prevention in multi-threaded arbitrage operations.
```

### ðŸš¨ MANDATORY FEATURE FILES SECTION ðŸš¨

**CRITICAL**: You MUST list EVERY SINGLE FILE in the Feature Files section with detailed descriptions.


- Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering (folders first, then files) at each level
- âœ... List EVERY file that PowerShell found
- âœ... Group files by purpose (Core Logic, Tests, Config, etc.)
- âœ... Each file gets 20-30 word description
- âœ... If PowerShell shows 54 files, Feature Files section MUST list all 54 files
- âŒ FORBIDDEN: Skipping files or using "and more files"
- âŒ FORBIDDEN: Using "[LIST ALL OTHER FILES]" without actually listing them
- âŒ FORBIDDEN: Summarizing with "etc." or "..."

**VERIFICATION**: Count files in Feature Files section â†' Must match PowerShell file count exactly

ðŸ" **DESCRIPTION LENGTH REQUIREMENTS:**
- MINIMUM: 20 words per file
- MAXIMUM: 30 words per file
- FORBIDDEN: Generic descriptions like "configuration file" or "helper utilities"
- REQUIRED: Specific purpose, key functions, dependencies, Windows integration details
- VERIFICATION: Count words in each description - must be 20-30 words

### Detailed File Descriptions:

Each file MUST have 20-30 word description including:

1. WHAT it does (primary function)
1. WHY it exists (business purpose)
2. HOW it integrates (connections)

Example:
```
**Core Engine (5 files):**
- core/engine.js â†' Main AI processing engine that orchestrates model loading, manages inference requests, caches predictions in SQLite, and triggers retraining when accuracy drops below threshold (25 words)
- core/router.js â†' Routes incoming prediction requests to appropriate ML models based on input type, model availability, and load balancing across multiple model instances (24 words)
- core/processor.js â†' Processes raw blockchain data into normalized feature vectors for ML model consumption, handles data validation, type conversion, and missing value imputation (25 words)
- core/validator.js â†' Validates model predictions against business rules, checks confidence thresholds, filters low-quality predictions, and logs validation failures for model retraining (23 words)
- core/optimizer.js â†' Optimizes model inference performance through batch processing, caching frequently requested predictions, and dynamically adjusting model parameters based on system load (23 words)
```

FORBIDDEN:
- Generic descriptions like "Core AI processing" (too vague)
- Single-word purposes like "Configuration" (insufficient detail)
- Missing integration details (no connections mentioned)
- Skipping files with "and more files" (incomplete)
- Descriptions under 20 words (too short)
- Descriptions over 30 words (too long)

REQUIRED:
- 20-30 words per file minimum (count them!)
- Specific technical details (not generic)
- Integration information (how it connects)
- Business value explanation (why it matters)
- EVERY SINGLE FILE listed (no exceptions)

(FILENAME-ONLY, APPEND-ONLY)

- Derive Feature Name from the last segment of the legacy path (see "Feature Name Derivation")
- **FILE COMPLETENESS CHECK**: Feature Files list MUST include representation of ALL files found in STEP 2
- **NO PARTIAL LISTINGS**: Never use "and more files" or "additional files" - be COMPLETE and specific
- **SCAFFOLDED FILE ANALYSIS**: Empty files must be analyzed by filename patterns to determine intended purpose

**FUNCTIONAL ANALYSIS MATRIX (PRE-GROUPING INTELLIGENCE):**

Before grouping files, analyze EACH file across 5 dimensions:

**1. Data Flow Role:**
- Input â†' Receives external data (RPC calls, API responses, user input)
- Processing â†' Transforms/analyzes data (calculations, ML inference, routing)
- Output â†' Sends data externally (transactions, API calls, UI updates)
- Storage â†' Persists data (database writes, file saves, cache updates)

**1. Execution Context:**
- Main Thread â†' Runs in primary application process (UI rendering, user interactions)
- Background â†' Runs in separate process/worker (heavy computations, monitoring)
- Scheduled â†' Triggered by time/cron (periodic tasks, cleanup, retraining)
- Event-Driven â†' Triggered by events (blockchain events, price changes, alerts)

**2. Dependencies (What It Requires):**
- External Services â†' RPC nodes, APIs, databases, file systems
- Internal Modules â†' Other project files it imports/requires
- Configuration â†' Settings, secrets, environment variables
- Runtime â†' Node.js version, Python packages, system libraries

**3. Dependents (What Depends On It):**
- Direct Consumers â†' Files that import/call this file
- Indirect Consumers â†' Features that rely on its functionality
- UI Components â†' Dashboard elements displaying its data
- External Systems â†' Blockchain contracts, APIs consuming its output

**4. Windows Integration Point:**
- Service â†' Runs as Windows Service (backend engines, monitors)
- UI â†' Electron renderer process (dashboard components, charts)
- Storage â†' File system/registry/database (configs, logs, data)
- Config â†' Settings management (registry, JSON files, env vars)
- Security â†' Credential Manager, encryption, certificates

**INTELLIGENT FILE GROUPING BY PURPOSE:**

After functional analysis, group files by actual function, not just extension:

- **Core Logic**: *-engine.js, *-manager.js, *-handler.js, *-controller.js, *-service.js
- **Adapters/Integrations**: *-adapter.js, *-connector.js, *-client.js, *-provider.js
- **Configuration**: *-config.json, *-config.js, .env, settings.js, constants.js
- **Tests**: *.test.js, *.spec.js, files in /tests/ or /test/ folders
- **Utilities**: *-utils.js, *-helpers.js, *-tools.js, *-lib.js
- **Types/Schemas**: *.d.ts, *-schema.json, *-types.ts, *-interface.ts
- **Documentation**: *.md, README.*, CHANGELOG.*
- **ML Models**: *-model.js, *-training.js, *-inference.js, *-prediction.js
- **Blockchain**: *-blockchain.js, *-wallet.js, *-transaction.js, *-contract.js
- **DeFi**: *-defi.js, *-dex.js, *-swap.js, *-liquidity.js, *-arbitrage.js
- **Other Files**: Files that don't match above categories

**COMPLEXITY SCORING:**

Calculate complexity based on file count:
- 1-5 files = Simple â­
- 6-15 files = Moderate â­â­
- 16-30 files = Complex â­â­â­
- 31-50 files = Very Complex â­â­â­â­
- 51+ files = Highly Complex â­â­â­â­â­

**TECHNOLOGY STACK DETECTION:**

Detect technologies from file extensions and patterns:
- *.sol â†' Solidity (Smart Contracts)
- *.jsx, *.tsx â†' React (UI Framework)
- *.py â†' Python (likely ML/AI)
- *.ipynb â†' Jupyter Notebooks (Data Science)
- *.test.js, *.spec.js â†' Jest/Mocha (Testing)
- *.yaml, *.yml â†' YAML configs (Deployment)
- *.ts â†' TypeScript (Type-safe JavaScript)
- *.css, *.scss â†' Stylesheets (UI Styling)
- *.sql â†' SQL (Database)
- *.wasm â†' WebAssembly (Performance)
- *.pt, *.pth â†' PyTorch (ML Models)
- *.h5, *.keras â†' Keras/TensorFlow (ML Models)
- *.pkl, *.pickle â†' Pickle (Serialized Data)
- *.onnx â†' ONNX (Cross-platform ML)
- *.sqlite3, *.db â†' Database files

**WINDOWS COMPONENT MAPPING:**

Map features to specific Windows technologies:

**For Backend Services:**
- Component: Windows Service (node-windows)
- Process Manager: PM2 or node-windows-service
- Auto-start: Windows Service Manager

**For UI Components:**
- Framework: Electron BrowserWindow
- Renderer: Chromium-based rendering
- IPC: Electron IPC (Main â†' Renderer)

**For Configuration:**
- Registry: HKEY_CURRENT_USER\Software\ApexArbitrage
- Files: %AppData%\ApexArbitrage\config.json
- Hot-reload: fs.watch() on config files

**For Data Storage:**
- Database: SQLite (better-sqlite3)
- Location: %AppData%\ApexArbitrage\data
- Backup: Windows Task Scheduler

**For Logging:**
- System: Windows Event Log (Application)
- Files: %AppData%\ApexArbitrage\logs
- Rotation: winston or pino with rotation

**For Security:**
- Credentials: Windows Credential Manager
- Encryption: AES-256 with node crypto
- Certificates: Windows Certificate Store

**For Notifications:**
- Toast: Windows Toast Notifications
- Tray: Electron system tray
- Badges: Taskbar badge overlay

**For Scheduling:**
- Tasks: Windows Task Scheduler
- Cron: node-cron for in-process scheduling
- Triggers: Event-based or time-based

**WINDOWS IMPLEMENTATION BULLET FORMAT:**

Each bullet MUST be ONE sentence describing:
- WHAT it does (action)
- WHERE it happens (component/location)
- HOW it integrates (connection method)

**Template:** "[Action] [in/via/using] [Component] [for/to] [Purpose]"

**Examples:**
âœ... "Load adapters dynamically from plugin directory at service startup"
âœ... "Store configuration in application data directory with JSON format"
âœ... "Display real-time metrics in Electron dashboard widget"

âŒ "The system will load the adapters" (too vague)
âŒ "Load adapters from C:\Program Files\..." (specific path)
âŒ "Use dynamic loading with require() and fs.readdir()" (too technical)

### MANDATORY OUTPUT FORMAT ENFORCEMENT

**Your output MUST include ALL of these elements:**

1. âœ... **Feature Number**: Count existing "## Feature" headers in target file, then use next number
   - Format: `## Feature [N]: [Feature Name]`
   - Example: If file has 2 features, new one is `## Feature 3:`

1. âœ... **Complexity Score**: Based on file count
   - 1-5 files = â­ (Simple)
   - 6-15 files = â­â­ (Moderate)
   - 16-30 files = â­â­â­ (Complex)
   - 31-50 files = â­â­â­â­ (Very Complex)
   - 51+ files = â­â­â­â­â­ (Highly Complex)

2. âœ... **File Count**: State exact count in header
   - Format: `## Feature [N]: [Name] â­â­â­ (Complex - 25 files)`

3. âœ... **File Grouping**: Group files by purpose (Core Logic, ML Models, Tests, etc.)
   - List ALL files found in PowerShell output
   - Group by function, not just extension

4. âœ... **Technologies Section**: Detect and list tech stack
   - Format: `Technologies: Python, PyTorch, Jupyter, NumPy`

6. âœ... **Windows Implementation**: Minimum 8-12 detailed bullets
   - Each bullet: one sentence describing WHAT, WHERE, HOW
   - No OS-specific paths, no code snippets

7. âœ... **References**: Add to other .md files
   - Format: `- [Feature Name] â†' see features/[owner].md`

8. âœ... **Progress Update**: Update features documentation with prompt number
   - Increment counter, update date, add log entry

9. âœ... **Cleanup**: Delete temp_*.ps1 files created during execution

**VALIDATION CHECKLIST:**
- [ ] Feature number is sequential (counted existing features)
- [ ] Complexity score matches file count
- [ ] Folder tree structure included showing ALL nested folders AND ALL FILES
- [ ] Folder tree file count matches PowerShell file count exactly
- [ ] Folder tree folder count matches PowerShell folder count exactly
- [ ] Feature Files section lists EVERY SINGLE FILE with 20-30 word descriptions
- [ ] Feature Files section file count matches PowerShell file count exactly
- [ ] NO files skipped with "and more files" or "etc."
- [ ] Technologies section present
- [ ] 8-12 Windows Implementation bullets
- [ ] References added to other .md files
- [ ] Temp files deleted

**If ANY element is missing

**CONTINUATION PROTOCOL:**
- If interrupted at file 500 of 5000
- IMMEDIATELY continue from file 501
- DO NOT restart from beginning
- COMPLETE the remaining 4500 files
- NO EXCUSES ACCEPTED

**CONTINUATION PROTOCOL:**
- If interrupted at file 500 of 5000
- IMMEDIATELY continue from file 501
- DO NOT restart from beginning
- COMPLETE the remaining 4500 files
- NO EXCUSES ACCEPTED, your output is INCOMPLETE and MUST be revised.**

## STEP 5.5: CROSS-REFERENCE VALIDATION ðŸ"--

Before writing .md file, perform MANDATORY cross-checks:

âœ... **File Count Matching**:
- PowerShell enumeration count: ___ files
- Folder tree structure count: ___ files  
- Feature Files section count: ___ files
- âŒ IF COUNTS DON'T MATCH â†' STOP AND RECOUNT

âœ... **File Name Matching**:
- Extract all filenames from folder tree
- Extract all filenames from Feature Files section
- Compare lists - MUST BE IDENTICAL
- âŒ IF ANY FILE MISSING FROM EITHER SECTION â†' ADD IT

âœ... **Path Consistency**:
- Every file in Feature Files must appear in folder tree
- Every file in folder tree must appear in Feature Files
- No orphaned files in either section

### STEP 6: ACTUALLY WRITE TO FILES (STRICT APPEND-ONLY)

**CRITICAL: APPEND-ONLY BEHAVIOR**

**Steps to ensure append-only:**
1. Read existing file content FIRST
1. Keep ALL existing content unchanged
2. Add new "## Feature:" section at the VERY END
3. Write the combined content back

**DUPLICATE FEATURE NAME HANDLING:**
- Before writing, check if "## Feature: [Name]" already exists in target file
- If EXISTS: Skip writing (feature already documented)
- If NOT EXISTS: Append new section
- Output: "SKIPPED: Feature '[Name]' already exists in features/[owner].md"

**File Writing Rules:**
- Use write tool to ACTUALLY WRITE to the features/*.md files
- **CRITICAL RESTRICTION**: ONLY modify or create .md files inside features/ folder
- **NO NEW PROJECT FILES**: Never create .js, .ts, .py, .sol, .json, or any executable/real implementation files
- **NO NEW FOLDERS**: Never create directories anywhere in the project
- **Creation rule**: If the owner/reference .md does not exist (e.g., config.md, security.md), CREATE features/[name].md and then append
- **APPEND-ONLY**: Read existing content first, then append the new "## Feature:" section to the END
- **Preserve all existing content**: never overwrite, replace, or delete
**MANDATORY TOOL EXECUTION & VERIFICATION**

**REQUIRED: Use these exact tools in this exact order:**

1. **READ EXISTING FILE FIRST** (MANDATORY):
   `
   Use read_file tool with:
   - filePath: "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\features\[owner].md"
   - Read entire file to preserve existing content
   `

2. **WRITE/CREATE OWNER FILE** (MANDATORY):
   `
   Use create_file tool with:
   - filePath: "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\features\[owner].md" 
   - content: [FULL existing content + new "## Feature:" section appended at end]
   `

3. **WRITE CROSS-REFERENCES TO REFERENCE FILES** (MANDATORY):
   `
   For each reference file, use insert_edit_into_file tool with:
   - filePath: "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\features\[reference].md"
   - code: "Append cross-reference line at end of file"
   `

**MANDATORY VERIFICATION STEPS** (Execute AFTER each file write):

1. **IMMEDIATE READ-BACK VERIFICATION**:
   `
   Use read_file tool to read the target file and CONFIRM the new content exists
   `

2. **SUCCESS CRITERIA - File writing is NOT complete until:**
   -  You can read back the full "## Feature [N]: [Name]" section
   -  Feature Files list is present and complete  
   -  Windows Implementation bullets are present
   -  Cross-reference lines exist in reference files

3. **FAILURE RECOVERY**:
   - If read-back fails: Retry the write operation
   - If still fails after 2 attempts: STOP and report "FILE WRITE FAILED"

**CRITICAL ORDER ENFORCEMENT:**
- **STEP 6 MUST complete ALL file writing BEFORE any cross-references**
- **NO cross-references until owner file write is verified successful**
- **Output "FILE WRITING COMPLETE" only after all verifications pass**


**Group files by actual function, not just extension:**
- **Core Logic**: *-engine.js, *-manager.js, *-handler.js, *-controller.js, *-service.js
- **Adapters/Integrations**: *-adapter.js, *-connector.js, *-client.js, *-provider.js
- **Configuration**: *-config.json, *-config.js, .env, settings.js, constants.js
- **Tests**: *.test.js, *.spec.js, files in /tests/ or /test/ folders
- **Utilities**: *-utils.js, *-helpers.js, *-tools.js, *-lib.js
- **Types/Schemas**: *.d.ts, *-schema.json, *-types.ts, *-interface.ts
- **Documentation**: *.md, README.*, CHANGELOG.*
- **ML Models**: *-model.js, *-training.js, *-inference.js, *-prediction.js
- **Blockchain**: *-blockchain.js, *-wallet.js, *-transaction.js, *-contract.js
- **DeFi**: *-defi.js, *-dex.js, *-swap.js, *-liquidity.js, *-arbitrage.js
- **Other Files**: Files that don't match above categories

**COMPLEXITY SCORING:**

Calculate complexity based on file count:
- 1-5 files = Simple â­
- 6-15 files = Moderate â­â­
- 16-30 files = Complex â­â­â­
- 31-50 files = Very Complex â­â­â­â­
- 51+ files = Highly Complex â­â­â­â­â­

**TECHNOLOGY STACK DETECTION:**

Detect technologies from file extensions and patterns:
- *.sol â†' Solidity (Smart Contracts)
- *.jsx, *.tsx â†' React (UI Framework)
- *.py â†' Python (likely ML/AI)
- *.ipynb â†' Jupyter Notebooks (Data Science)
- *.test.js, *.spec.js â†' Jest/Mocha (Testing)
- *.yaml, *.yml â†' YAML configs (Deployment)
- *.ts â†' TypeScript (Type-safe JavaScript)
- *.css, *.scss â†' Stylesheets (UI Styling)
- *.sql â†' SQL (Database)
- *.wasm â†' WebAssembly (Performance)
- *.glb â†' 3D Assets (AR/VR)
- *.pt, *.pth â†' PyTorch (ML Models)
- *.h5, *.keras â†' Keras/TensorFlow (ML Models)
- *.pkl, *.pickle â†' Pickle (Serialized Data)
- *.joblib â†' Joblib (ML Persistence)
- *.safetensors â†' SafeTensors (ML Weights)
- *.msi â†' Windows Installer (Installation)
- *.asar â†' Electron Archive (Packaging)
- *.appx â†' Windows App Package (Distribution)
- *.ckpt â†' TensorFlow Checkpoints (ML Models)
- *.hdf5 â†' HDF5 (ML Data)
- *.feather â†' Feather (ML Data)
- *.arrow â†' Arrow (ML Data)
- *.caffemodel â†' Caffe Models (ML Models)
- *.sqlite3 â†' SQLite3 (Database)
- *.db â†' Database (Database)
- *.onnx â†' ONNX (Cross-platform ML)
- *.tflite â†' TensorFlow Lite (Mobile ML)
- *.pb â†' Protocol Buffers (TensorFlow)
- *.npy, *.npz â†' NumPy Arrays (ML Data)
- *.parquet â†' Parquet (Big Data)
- *.vy â†' Vyper (Smart Contracts)
- *.abi â†' ABI (Contract Interface)

**WINDOWS COMPONENT MAPPING:**

Map features to specific Windows technologies:

**For Backend Services:**
- Component: Windows Service (node-windows)
- Process Manager: PM2 or node-windows-service
- Auto-start: Windows Service Manager

**For UI Components:**
- Framework: Electron BrowserWindow
- Renderer: Chromium-based rendering
- IPC: Electron IPC (Main â†" Renderer)

**For Configuration:**
- Registry: HKEY_CURRENT_USER\Software\ApexArbitrage
- Files: %AppData%\ApexArbitrage\config.json
- Hot-reload: fs.watch() on config files

**For Data Storage:**
- Database: SQLite (better-sqlite3)
- Location: %AppData%\ApexArbitrage\data
- Backup: Windows Task Scheduler

**For Logging:**
- System: Windows Event Log (Application)
- Files: %AppData%\ApexArbitrage\logs
- Rotation: winston or pino with rotation

**For Security:**
- Credentials: Windows Credential Manager
- Encryption: AES-256 with node crypto
- Certificates: Windows Certificate Store

**For Notifications:**
- Toast: Windows Toast Notifications
- Tray: Electron system tray
- Badges: Taskbar badge overlay

**For Scheduling:**
- Tasks: Windows Task Scheduler
- Cron: node-cron for in-process scheduling
- Triggers: Event-based or time-based

**WINDOWS IMPLEMENTATION BULLET FORMAT:**

Each bullet MUST be ONE sentence describing:
- WHAT it does (action)
- WHERE it happens (component/location)
- HOW it integrates (connection method)

**Template:** "[Action] [in/via/using] [Component] [for/to] [Purpose]"

**Examples:**
âœ" "Load adapters dynamically from plugin directory at service startup"
âœ" "Store configuration in application data directory with JSON format"
âœ" "Display real-time metrics in Electron dashboard widget"

âœ-- "The system will load the adapters" (too vague)
âœ-- "Load adapters from C:\Program Files\..." (specific path)
âœ-- "Use dynamic loading with require() and fs.readdir()" (too technical)


## Input Format

PATH-TO-FEATURE MAPPER
Full Path: C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\ai-modules

## OUTPUT FORMAT (EXACT TEMPLATE - DO NOT DEVIATE)

**Copy this template EXACTLY and fill in the values:**

```
- "What does this FEATURE do?" â†' [your 1-2 line description]
- "Which MD file OWNS this FEATURE?" â†' [owner.md] ([reason])
- "Which MD files REFERENCE this FEATURE?" â†' [md1], [md2] ([reasons])
- "HOW TO IMPLEMENT â†' OWNER FILE ([owner].md)" â†'
  Append this section to the end of features/[owner].md:

  ## Feature [N]: [Feature Name]

  Feature Files:
  - [file1] â†' [description]
  - [file2] â†' [description]
  
  Windows Implementation:
  - [bullet 1]
  - [bullet 2]
  
- "HOW TO IMPLEMENT â†' REFERENCES" â†'
  - In features/[md1]: [Feature Name] â†' see features/[owner].md
  - In features/[md2]: [Feature Name] â†' see features/[owner].md
```

**DO NOT ADD:**
- Headers like "# Analysis" or "## Summary"
- Code blocks with ```markdown
- Extra blank lines
- Explanatory text outside the 5 sections

## FORBIDDEN IN THIS MODE

- No headers, no code fences, no blank lines before/after the 5 sections
- No detailed specs, no "PRIMARY SPECIFICATION", no "INTEGRATION NOTES"
- No acceptance criteria, performance targets, or OS paths (e.g., %APPDATA%)
- No external links
- Do not include directory prefixes in file lists (filenames only)
- Do not create real (non-MD) files or folders anywhere in the project
- Do not create .js, .ts, .py, .sol, .json, config files, or executable code
- Only modify or create .md files in features/ folder
- Creation allowed ONLY for missing owner/reference .md files required by the mapping (e.g., features/config.md, features/security.md)
- No new directories outside features/
- Do not modify or delete any existing content in features/*.md (append-only)

## EXISTING FEATURES FOLDER STRUCTURE

- features/README.md â†' (feature documentation)
- features/ai-modules.md â†' (ready for content)
- features/backend.md â†' (ready for content)
- features/config.md â†' (ready for content)
- features/contracts.md â†' (ready for content)
- features/dashboard.md â†' (ready for content)
- features/deployment.md â†' (ready for content)
- features/docs.md â†' (ready for content)
- features/install-dependencies.md â†' (ready for content)
- features/security.md â†' (ready for content)
- features/testing.md â†' (ready for content)

##  FILE ROUTING QUICK REFERENCE

**CRITICAL**: Write analysis to `features/*.md` based on content type found:

- `.sol` files, smart contracts  `features/contracts.md`
- Backend APIs, servers, `package.json`  `features/backend.md`
- React, dashboard, UI components  `features/dashboard.md`
- Test files, `*.test.js`, `*.spec.js`  `features/testing.md`
- Docker, CI/CD, deployment scripts  `features/deployment.md`
- Config files, `.env`, settings  `features/config.md`
- Security, encryption, auth code  `features/security.md`
- AI/ML models, training scripts  `features/ai-modules.md`
- Documentation, guides, README  `features/docs.md`
- Installers, setup scripts  `features/install-dependencies.md`
- Archives, deprecated code  `features/archive.md`

**If multiple types found**: Write to PRIMARY type file, add cross-references to others.

---

## INTELLIGENT MAPPING RULES (Heuristics)

### File patterns

- presets/*.json â†' dashboard.md (UI configuration)
- *-adapter.js â†' backend.md (integration adapters)
- *.test.js â†' testing.md (tests)
- *-engine.js â†' backend.md (engine internals)
- *.sol â†' contracts.md (smart contracts)
- *-config.json â†' config.md (configuration)
- *-security.* | audit-*| logs/security* â†' security.md (security)
- docs/*|*.md â†' docs.md (documentation)
- deploy/*| kubernetes/* | helm/*| terraform/* â†' deployment.md (deployment)
- ai-*| models/* | train/*| datasets/* | notebooks/* â†' ai-modules.md (AI/ML)
- *.py â†' ai-modules.md (Python ML scripts)
- package.json | requirements.txt | *.lock â†' install-dependencies.md (dependency management)
- .env* | secrets/* | vault/* â†' security.md (secrets and credentials)
- migrations/* | schema/* â†' backend.md (database migrations)
- plugins/* â†' backend.md (plugin system)
- widgets/* | components/* â†' dashboard.md (UI components)
- storage/* | backup/* | snapshots/* â†' backend.md (data persistence)
- ci/* | .gitlab/* â†' deployment.md (CI/CD pipelines)
- benchmarks/* | profiling/* â†' testing.md (performance benchmarks)
- scripts/* â†' deployment.md (automation scripts)
- public/* | static/* | assets/* â†' dashboard.md (static assets)
- types/* | interfaces/* â†' backend.md (type definitions)
- utils/* | helpers/* â†' backend.md (utility functions)
- vendor/* | third-party/* â†' install-dependencies.md (external dependencies)

### Folder patterns

- dashboard/* â†' dashboard.md
- backend/* â†' backend.md
- ai-modules/* â†' ai-modules.md
- config/* â†' config.md
- contracts/* â†' contracts.md
- security/*, logs/security-* â†' security.md
- tests/* â†' testing.md
- deploy/*, scripts/* â†' deployment.md
- docs/* â†' docs.md
- archive/* â†' docs.md (archived documentation)
- examples/* â†' docs.md (example code and demos)
- research/* â†' ai-modules.md (research and experiments)
- data/* â†' backend.md (data storage)
- migrations/* â†' backend.md (database migrations)
- overlays/* â†' dashboard.md (UI overlays)
- presets/* â†' dashboard.md (preset configurations)
- public/* â†' dashboard.md (public assets)
- storage/* â†' backend.md (persistent storage)
- vendor/* â†' install-dependencies.md (third-party code)
- watchdog/* â†' backend.md (monitoring and alerts)

### Feature Name Derivation (STEP-BY-STEP)

**Given path:** `backend/plugins/dex-adapters`

Step 1: Extract last segment â†' `dex-adapters`
Step 2: Replace hyphens with spaces â†' `dex adapters`
Step 3: Title Case each word â†' `Dex Adapters`
Final: `Dex Adapters`

**More examples:**
- `backend/engine/core` â†' `Core`
- `dashboard/components/charts` â†' `Charts`
- `ai-modules/models/training` â†' `Training`
- `config/chains/ethereum` â†' `Ethereum`

## EDGE CASES & SPECIAL HANDLING

### Empty Folders
- If folder exists but has no files in actual filesystem (via PowerShell)
- Still create documentation noting "Scaffolded folder - awaiting implementation"
- Analyze folder name and parent path to infer intended purpose

### Multi-Purpose Folders
- If folder contains mixed file types (e.g., .sol + .js + .py)
- Choose owner based on MAJORITY file type or primary purpose
- Reference ALL other relevant .md files for cross-feature integration

## POST-GENERATION QUALITY CHECKS


### VALIDATION LOOP REQUIREMENT

After EVERY 100 files:
1. COUNT what you listed
2. VERIFY against PowerShell count
3. If mismatch, GO BACK and fix
4. DO NOT proceed until counts match
Before writing files, verify:
1. All 5 output sections COMPLETE
1. Feature Files list NOT empty (unless scaffolded)
2. Windows Implementation has 2-4 bullets minimum
3. Feature name valid (1-50 chars, Title Case)
4. features documentation will be updated

If ANY check fails: STOP and report issue

**CRITICAL VALIDATION POINTS:**
1. After PowerShell enumeration â†' Count files
2. After folder tree creation â†' Verify all files present
3. After Feature Files section â†' Double-check counts match
4. Before writing .md files â†' Triple-check completeness
5. If ANY discrepancy â†' STOP and fix immediately

## Feature:
```


### 20-POINT VALIDATION MATRIX (SYSTEMATIC QUALITY ASSURANCE)

**Execute this checklist before marking prompt COMPLETE:**

**File Enumeration (5 points):**
- [ ] 1. PowerShell executed successfully without errors
- [ ] 1. All files enumerated with "FILE X/Y" format showing progress
- [ ] 2. File count matches PowerShell output exactly
- [ ] 3. No files skipped or summarized with "etc."
- [ ] 4. Subfolder files included recursively

**Feature Analysis (5 points):**
- [ ] 6. Feature number is sequential (counted existing features)
- [ ] 7. Complexity score matches file count (â­ to â­â­â­â­â­)
- [ ] 8. Technologies section present with detected stack
- [ ] 9. Files grouped by purpose (Core Logic, Tests, etc.)
- [ ] 10. Each file has 20-30 word description

**Windows Implementation (5 points):**
- [ ] 11. Minimum 8-12 implementation bullets present
- [ ] 11. Each bullet follows "Action + Component + Purpose" format
- [ ] 12. No OS-specific paths (no C:\, %AppData% literals)
- [ ] 13. Windows components mapped correctly (Service, Electron, etc.)
- [ ] 14. Integration points clearly described

**File Operations (5 points):**
- [ ] 16. Owner .md file updated with append-only behavior
- [ ] 17. Reference .md files updated with cross-references
- [ ] 19. Temp PowerShell files deleted (temp_*.ps1)
- [ ] 20. No duplicate feature names in target files

**SCORING:**
- 20/20 = âœ... PERFECT - Mark COMPLETE
- 18-19/20 = âœ... ACCEPTABLE - Mark COMPLETE with notes
- 15-17/20 = âš ï¸ NEEDS REVIEW - Fix issues before completing
- <15/20 = âŒ FAILED - Do not mark COMPLETE, restart execution

**If score < 18: STOP and fix all failing checks before proceeding**

---


### CONFIDENCE SCORING (AI SELF-ASSESSMENT)

**Rate your confidence in this execution (1-10):**

- **File enumeration accuracy**: [Score] - Did PowerShell find all expected files?
- **Feature mapping correctness**: [Score] - Is the feature correctly identified?
- **Owner file assignment**: [Score] - Is the owner .md file correct?
- **Implementation completeness**: [Score] - Are all required elements present?

**If any score < 7: STOP and review before proceeding**


## STEP 6.5: ERROR RECOVERY PROTOCOL ðŸ"§

IF YOU DISCOVER DURING VALIDATION THAT FILES WERE SKIPPED:

ðŸš¨ **DO NOT SUBMIT INCOMPLETE .md FILE**

**Recovery Steps**:
1. **STOP** - Do not write the .md file yet
1. **RECOUNT** - Re-run PowerShell enumeration command
2. **COMPARE** - Check your folder tree vs PowerShell output
3. **IDENTIFY GAPS** - List which files are missing
4. **ADD MISSING FILES** - Update both folder tree AND Feature Files sections
6. **RE-VALIDATE** - Run through validation checklist again
7. **ONLY THEN** - Write the COMPLETE .md file

**Common Mistakes to Fix**:
- Missing files in deeply nested subfolders (check 8+ levels deep)
- Skipped hidden files or files with special characters
- Incomplete file descriptions (check word count 20-30)
- Folder tree shows files but Feature Files section missing them
- Feature Files section shows files but folder tree missing them
- Count mismatch between PowerShell output and your sections

**Self-Check Questions**:
- [ ] Did I list EVERY file from PowerShell output in folder tree?
- [ ] Did I list EVERY file from PowerShell output in Feature Files?
- [ ] Do both sections have IDENTICAL file counts?
- [ ] Does each file description have 20-30 words?
- [ ] Are all nested folders expanded fully in tree structure?

**If you answer NO to ANY question: DO NOT WRITE FILES. Fix the issue first.**

---

**DO NOT USE:**
- âŒ list_dir tool
- âŒ read_file for enumeration
- âŒ Relative paths like "Apex Arbitrage Multichain bot/ai-modules"

**MUST USE:**
- âœ... run_terminal_cmd tool (PowerShell)
- âœ... Full Windows paths with C:\

**IF TOOL FAILS 2 TIMES: STOP and report error. DO NOT retry same command 3+ times.**



