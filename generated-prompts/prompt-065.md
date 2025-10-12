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
2. Search for "Prompt 65: Executed" in the Execution Log
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
try {
    $basePath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot"
    $targetPath = Join-Path $basePath "backend/docs"
    
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
- **VERIFICATION**: Count total files found and state the count explicitly: "Found [N] files in [folder-path]"
- **FEATURE NUMBERING**: Always start with "Feature #X:" where X is the prompt number
- **COMPLETE COUNTING**: State exact counts: "Total Files: [N], Total Folders: [M], Total Nested Levels: [L]"
- **SUMMARY FORMAT**: Begin analysis with: "Feature #[X]: [Feature Name] - Found [N] files across [M] folders"
- **MANDATORY COUNTS**: PowerShell already shows counts, but AI must restate them in analysis
- **STRUCTURED OUTPUT**: Format all analysis as numbered features with complete file/folder counts
- **VERIFICATION CHECKLIST**: Before writing files, verify counts match PowerShell output exactly
- **SCAFFOLDED FILES**: Even if files are empty placeholders, they MUST be analyzed for feature intent from filename patterns
- **MINIMUM REQUIREMENT**: If folder has 50+ files, list ALL 50+ files by name

**FILE ENUMERATION EXAMPLES:**

**WRONG (Incomplete):**
```
Found 10 files in backend/plugins/dex-adapters:
- uniswap-v2-adapter.js
- sushiswap-adapter.js
- ... (8 more files)  ← FORBIDDEN!
```

**CORRECT (Complete):**
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

**Rule:** List EVERY SINGLE file by name. No shortcuts. No "etc." No "and more".

**LARGE FOLDER HANDLING (100+ files):**
If folder has 100+ files, list ALL files but group by type for readability:
```
Found 150 files in backend/plugins:

JavaScript files (120):
- adapter-1.js, adapter-2.js, adapter-3.js... (list all 120)

Test files (20):
- test-1.test.js, test-2.test.js... (list all 20)

Config files (10):
- config-1.json, config-2.json... (list all 10)
```
Still list EVERY file, just organize by category.

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

### STEP 4: MAP TO .MD FILES

- Choose the single owner .md from: install-dependencies.md, config.md, backend.md, dashboard.md, ai-modules.md, contracts.md, security.md, testing.md, deployment.md, docs.md
- Choose 1-4 referencing .md files based on real integration needs

### STEP 5: IMPLEMENTATION GUIDE (FILENAME-ONLY, APPEND-ONLY)

- Derive Feature Name from the last segment of the legacy path (see "Feature Name Derivation")
- **FILE COMPLETENESS CHECK**: Feature Files list MUST include representation of ALL files found in STEP 2
- **NO PARTIAL LISTINGS**: Never use "and more files" or "additional files" - be complete and specific
- **SCAFFOLDED FILE ANALYSIS**: Empty files must be analyzed by filename patterns to determine intended purpose

**INTELLIGENT FILE GROUPING BY PURPOSE:**

Group Feature Files by actual function, not just extension:
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
- 1-5 files = Simple ⭐
- 6-15 files = Moderate ⭐⭐
- 16-30 files = Complex ⭐⭐⭐
- 31-50 files = Very Complex ⭐⭐⭐⭐
- 51+ files = Highly Complex ⭐⭐⭐⭐⭐

**TECHNOLOGY STACK DETECTION:**

Detect technologies from file extensions and patterns:
- *.sol → Solidity (Smart Contracts)
- *.jsx, *.tsx → React (UI Framework)
- *.py → Python (likely ML/AI)
- *.ipynb → Jupyter Notebooks (Data Science)
- *.test.js, *.spec.js → Jest/Mocha (Testing)
- *.yaml, *.yml → YAML configs (Deployment)
- *.ts → TypeScript (Type-safe JavaScript)
- *.css, *.scss → Stylesheets (UI Styling)
- *.sql → SQL (Database)
- *.wasm → WebAssembly (Performance)
- *.glb → 3D Assets (AR/VR)
- *.pt, *.pth → PyTorch (ML Models)
- *.h5, *.keras → Keras/TensorFlow (ML Models)
- *.pkl, *.pickle → Pickle (Serialized Data)
- *.joblib → Joblib (ML Persistence)
- *.safetensors → SafeTensors (ML Weights)
- *.msi → Windows Installer (Installation)
- *.asar → Electron Archive (Packaging)
- *.appx → Windows App Package (Distribution)
- *.ckpt → TensorFlow Checkpoints (ML Models)
- *.hdf5 → HDF5 (ML Data)
- *.feather → Feather (ML Data)
- *.arrow → Arrow (ML Data)
- *.caffemodel → Caffe Models (ML Models)
- *.sqlite3 → SQLite3 (Database)
- *.db → Database (Database)
- *.onnx → ONNX (Cross-platform ML)
- *.tflite → TensorFlow Lite (Mobile ML)
- *.pb → Protocol Buffers (TensorFlow)
- *.npy, *.npz → NumPy Arrays (ML Data)
- *.parquet → Parquet (Big Data)
- *.vy → Vyper (Smart Contracts)
- *.abi → ABI (Contract Interface)

**WINDOWS COMPONENT MAPPING:**

Map features to specific Windows technologies:

**For Backend Services:**
- Component: Windows Service (node-windows)
- Process Manager: PM2 or node-windows-service
- Auto-start: Windows Service Manager

**For UI Components:**
- Framework: Electron BrowserWindow
- Renderer: Chromium-based rendering
- IPC: Electron IPC (Main ↔ Renderer)

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

Each bullet should be ONE sentence describing:
- WHAT it does (action)
- WHERE it happens (component/location)
- HOW it integrates (connection method)

**Template:** "[Action] [in/via/using] [Component] [for/to] [Purpose]"

**Examples:**
✓ "Load adapters dynamically from plugin directory at service startup"
✓ "Store configuration in application data directory with JSON format"
✓ "Display real-time metrics in Electron dashboard widget"

✗ "The system will load the adapters" (too vague)
✗ "Load adapters from C:\Program Files\..." (specific path)
✗ "Use dynamic loading with require() and fs.readdir()" (too technical)

### STEP 6: ACTUALLY WRITE TO GITHUB FILES (STRICT APPEND-ONLY)

**CRITICAL: APPEND-ONLY BEHAVIOR**

**Steps to ensure append-only:**
1. Read existing file content FIRST
2. Keep ALL existing content unchanged
3. Add new "## Feature:" section at the VERY END
4. Write the combined content back

**DUPLICATE FEATURE NAME HANDLING:**
- Before writing, check if "## Feature: [Name]" already exists in target file
- If EXISTS: Skip writing (feature already documented)
- If NOT EXISTS: Append new section
- Output: "SKIPPED: Feature '[Name]' already exists in features/[owner].md"

**File Writing Rules:**
- Use create_or_update_file tool to ACTUALLY WRITE to the features/*.md files in the GitHub repo
- **CRITICAL RESTRICTION**: ONLY modify or create .md files inside features/ folder
- **NO NEW PROJECT FILES**: Never create .js, .ts, .py, .sol, .json, or any executable/real implementation files
- **NO NEW FOLDERS**: Never create directories anywhere in the project
- **Creation rule**: If the owner/reference .md does not exist (e.g., config.md, security.md), CREATE features/[name].md and then append
- **APPEND-ONLY**: Read existing content first, then append the new "## Feature:" section to the END
- **Preserve all existing content**: never overwrite, replace, or delete
- Repo: Apex-Arbitrage-Multichain-bot-for-windows (owner: pavan53732, branch: main)

## Input Format

PATH-TO-FEATURE MAPPER
Legacy Path: Apex Arbitrage multi-chain bot/Apex Arbitrage Multichain bot/backend/docs

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

- features/README.md → (feature documentation)
- features/ai-modules.md → (ready for content)
- features/backend.md → (ready for content)
- features/config.md → (ready for content)
- features/contracts.md → (ready for content)
- features/dashboard.md → (ready for content)
- features/deployment.md → (ready for content)
- features/docs.md → (ready for content)
- features/install-dependencies.md → (ready for content)
- features/security.md → (ready for content)
- features/testing.md → (ready for content)

## INTELLIGENT MAPPING RULES (Heuristics)

### File patterns

- presets/*.json → dashboard.md (UI configuration)
- *-adapter.js → backend.md (integration adapters)
- *.test.js → testing.md (tests)
- *-engine.js → backend.md (engine internals)
- *.sol → contracts.md (smart contracts)
- *-config.json → config.md (configuration)
- *-security.* | audit-*| logs/security* → security.md (security)
- docs/*|*.md → docs.md (documentation)
- deploy/*| kubernetes/* | helm/*| terraform/* → deployment.md (deployment)
- ai-*| models/* | train/*| datasets/* | notebooks/* → ai-modules.md (AI/ML)
- *.py → ai-modules.md (Python ML scripts)
- package.json | requirements.txt | *.lock → install-dependencies.md (dependency management)
- .env* | secrets/* | vault/* → security.md (secrets and credentials)
- migrations/* | schema/* → backend.md (database migrations)
- plugins/* → backend.md (plugin system)
- widgets/* | components/* → dashboard.md (UI components)
- storage/* | backup/* | snapshots/* → backend.md (data persistence)
- ci/* | .github/* | .gitlab/* → deployment.md (CI/CD pipelines)
- benchmarks/* | profiling/* → testing.md (performance benchmarks)
- scripts/* → deployment.md (automation scripts)
- public/* | static/* | assets/* → dashboard.md (static assets)
- types/* | interfaces/* → backend.md (type definitions)
- utils/* | helpers/* → backend.md (utility functions)
- vendor/* | third-party/* → install-dependencies.md (external dependencies)

### Folder patterns

- dashboard/* → dashboard.md
- backend/* → backend.md
- ai-modules/* → ai-modules.md
- config/* → config.md
- contracts/* → contracts.md
- security/*, logs/security-* → security.md
- tests/* → testing.md
- deploy/*, scripts/* → deployment.md
- docs/* → docs.md
- archive/* → docs.md (archived documentation)
- examples/* → docs.md (example code and demos)
- research/* → ai-modules.md (research and experiments)
- data/* → backend.md (data storage)
- migrations/* → backend.md (database migrations)
- overlays/* → dashboard.md (UI overlays)
- presets/* → dashboard.md (preset configurations)
- public/* → dashboard.md (public assets)
- storage/* → backend.md (persistent storage)
- vendor/* → install-dependencies.md (third-party code)
- watchdog/* → backend.md (monitoring and alerts)

### Feature Name Derivation (STEP-BY-STEP)

**Given path:** `backend/plugins/dex-adapters`

Step 1: Extract last segment → `dex-adapters`
Step 2: Replace hyphens with spaces → `dex adapters`
Step 3: Title Case each word → `Dex Adapters`
Final: `Dex Adapters`

**More examples:**
- `backend/engine/core` → `Core`
- `dashboard/components/charts` → `Charts`
- `ai-modules/models/training` → `Training`
- `config/chains/ethereum` → `Ethereum`

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

Before writing files, verify:
1. All 5 output sections complete
2. Feature Files list NOT empty (unless scaffolded)
3. Windows Implementation has 2-4 bullets minimum
4. Feature name valid (1-50 chars, Title Case)
5. progress.md will be updated

If ANY check fails: STOP and report issue

## POST-EXECUTION CHECKPOINT

**After completing all tasks above, update progress tracking:**

1. Open `generated-prompts/progress.md`
2. Increment "Completed" counter (X/842 -> X+1/842)
3. Update "Last Updated" to today's date
4. Update "Recent Completions" to: Prompt 65 (Feature: [Feature Name])
5. Append to Execution Log:
   ```
   Prompt 65: Executed - Added 'Feature: [Feature Name]' to features/[owner].md
   ```
6. Save progress.md before moving to next prompt
7. Clean up: Delete any temp_*.ps1 files created during this prompt execution

**Mark this prompt as COMPLETE.**

---



