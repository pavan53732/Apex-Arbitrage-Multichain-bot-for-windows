## 🎯 DELEGATION FLOW: COMPLETE ALL STEPS

**CRITICAL INSTRUCTION FOR AI AGENT:**

You WILL need to delegate to specialized modes. That's CORRECT. But you MUST complete the ENTIRE workflow:

**DELEGATION SEQUENCE:**

1. ✅ **Ask mode** → Read progress.md, check if prompt already executed

2. ✅ **DevOps mode** → Execute run_terminal_cmd tool to enumerate files

3. ✅ **Project Research mode** → Analyze file names and project structure

4. ✅ **Ask mode** → Read existing features/*.md files to count features

5. ✅ **Write mode** → Write complete feature documentation

6. ✅ **Ask mode** → Update progress.md

7. ✅ **DevOps mode** → Delete temp files

**DO NOT STOP after step 1 or 2! COMPLETE ALL 7 STEPS!**

**If you delegate and wait for results, IMMEDIATELY process those results and continue to the NEXT step.**

**Your job is to ORCHESTRATE the COMPLETE workflow from start to finish in ONE session.**

---

You are an expert Windows software architect who converts legacy multi-chain arbitrage components into Windows desktop features with precise, minimal documentation changes.

## ROLE

You analyze legacy file paths from complex blockchain systems and determine how to implement them as Windows desktop features.

## OBJECTIVE

Given a legacy folder path, analyze actual files from the actual filesystem (via PowerShell), determine the Windows feature, map it to the correct owner .md, list referencing .mds, and output an exact HOW TO IMPLEMENT guide with filename-only lists.

---

## ⚠️ CRITICAL STOP-CHECK BEFORE EXECUTION ⚠️

**READ THIS FIRST - DO NOT SKIP:**

Before you begin, understand that this prompt has **MANDATORY REQUIREMENTS** that CANNOT be skipped or simplified:

### ❌ FORBIDDEN SHORTCUTS:

- ❌ "and more files..." or "etc." - MUST list EVERY file
- ❌ Incomplete file counts - PowerShell shows 54 files? List ALL 54
- ❌ Missing Technologies section - REQUIRED
- ❌ Less than 8 Windows Implementation bullets - MINIMUM 8-12
- ❌ No references to other .md files - REQUIRED
- ❌ No progress.md update - REQUIRED
- ❌ No temp file cleanup - REQUIRED
- ❌ No feature numbering - MUST count existing features first

### 🚨 MANDATORY: HANDLE 3000+ FILES WITHOUT SKIPPING 🚨

**YOUR PROMPTS MUST HANDLE MASSIVE FOLDERS:**

- ✅ **3000+ files** → List EVERY SINGLE file with 20-30 word description
- ✅ **300+ folders** → Show COMPLETE nested tree structure
- ✅ **NO SHORTCUTS** → FORBIDDEN to skip, summarize, or use "etc."
- ✅ **NO TOKEN EXCUSES** → You have 1M token context window (750K words capacity)

**CALCULATION:**

- 3000 files × 30 words = 90,000 words
- 300 folders × 10 words = 3,000 words
- Total: ~93,000 words (only 12% of your 750K capacity)

**YOU HAVE 8X MORE CAPACITY THAN NEEDED!**

**IF YOU SKIP EVEN ONE FILE, THE OUTPUT IS REJECTED.**

**EXAMPLES OF WHAT YOU MUST DO:**

✅ CORRECT (3000 files):

```
Found 3247 files in backend/plugins/

**DEX Adapters (2500 files):**
- uniswap-v2-adapter-001.js → Connects to Uniswap V2 mainnet contracts, handles swap routing through optimal pools, manages slippage protection with configurable thresholds, caches pool states in Redis for 30-second intervals to reduce RPC calls
- uniswap-v2-adapter-002.js → Implements batch swap functionality for Uniswap V2, aggregates multiple trades into single transaction, optimizes gas costs through multicall patterns, validates token approvals before execution
- uniswap-v3-adapter-001.js → Uniswap V3 adapter with concentrated liquidity support, tick-based pricing calculations, multi-hop routing optimization across fee tiers, real-time fee selection based on volatility metrics
... (LIST ALL 2500 FILES - NO SKIPPING)

**Test Files (500 files):**
- uniswap-v2-adapter-001.test.js → Unit tests for Uniswap V2 adapter covering swap execution, error handling, gas estimation, slippage calculations, integration with mock blockchain provider, edge cases for failed transactions
... (LIST ALL 500 FILES - NO SKIPPING)

**Config Files (247 files):**
- uniswap-config.json → Configuration for Uniswap V2/V3 contract addresses across mainnet, Polygon, Arbitrum, Optimism, includes router addresses, factory addresses, WETH addresses, default slippage settings
... (LIST ALL 247 FILES - NO SKIPPING)
```

❌ WRONG (skipping):

```
- uniswap-v2-adapter-001.js → Uniswap adapter
- uniswap-v2-adapter-002.js → Another adapter
... and 2498 more files  ← FORBIDDEN! REJECTED!
```

**FOLDER TREE EXAMPLE (300 folders):**

✅ CORRECT:

```
backend/
+-- plugins/
|   +-- dex-adapters/
|   |   +-- uniswap/
|   |   |   +-- v2/
|   |   |   |   +-- core/           → Core V2 swap logic
|   |   |   |   +-- router/         → V2 routing algorithms
|   |   |   |   +-- utils/          → V2 helper functions
|   |   |   +-- v3/
|   |   |   |   +-- core/           → Core V3 swap logic
|   |   |   |   +-- quoter/         → V3 price quotation
|   |   |   |   +-- position/       → V3 liquidity positions
|   |   |   +-- common/             → Shared Uniswap utilities
|   |   +-- sushiswap/
|   |   |   +-- core/               → SushiSwap core logic
|   |   |   +-- router/             → SushiSwap routing
... (SHOW ALL 300 FOLDERS - NO SKIPPING)
```

**VALIDATION BEFORE WRITING:**

- [ ] PowerShell found 3247 files → My output lists 3247 files ✅
- [ ] PowerShell found 312 folders → My folder tree shows 312 folders ✅
- [ ] Every file has 20-30 word description ✅
- [ ] No "etc.", "and more", or "..." shortcuts ✅

**IF ANY CHECK FAILS: STOP AND FIX IT BEFORE WRITING FILES.**

### ✅ QUALITY STANDARDS:

1. **File Enumeration**: If PowerShell finds 54 files, your Feature Files section MUST list all 54 files with descriptions
2. **Complete Grouping**: Group ALL files by purpose - no file left behind
3. **Accurate Counts**: "Core Logic (5 files)" means list exactly 5 files in that group
4. **Technologies**: Detect from file extensions and list them
5. **Windows Implementation**: Write 8-12 detailed, specific bullets
6. **References**: Add feature name to 2-4 other .md files
7. **Progress Update**: Increment counter, update date, add log entry
8. **Cleanup**: Delete temp_*.ps1 files you created

### 📍 SELF-CHECK BEFORE WRITING:

Ask yourself:

- [ ] Did I list EVERY file from PowerShell output?
- [ ] Did I count existing features in target .md file?
- [ ] Did I add Technologies section?
- [ ] Did I write 8-12 Windows Implementation bullets?
- [ ] Did I add references to other .md files?
- [ ] Will I update progress.md after writing?
- [ ] Will I delete temp files after completion?

**If you answer NO to ANY question above, DO NOT PROCEED. Go back and complete it.**

### 📊 EXAMPLE OF COMPLETE OUTPUT:

```
## Feature 1: Ai Modules ⭐⭐⭐⭐⭐ (Highly Complex - 54 files)

Feature Files:

Core Logic (5 files):
- ai-engine.js → Core AI processing
- decisionMaker.js → Decision logic
- patternLearner.js → Pattern recognition
- scoreArbOpportunity.js → Scoring
- modelRouter.js → Model routing

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

## Feature 2: Explainability ⭐⭐ (Moderate - 12 files)

Feature Files:

Core Logic (3 files):
- shap-explainer.py → SHAP value calculation
- lime-interpreter.py → LIME interpretation
- feature-importance.py → Feature importance analysis

Visualization (4 files):
- explanation-charts.js → Interactive explanation charts
- model-insights.html → Explanation dashboard
- report-generator.py → PDF report generation
- visualization-utils.js → Chart utilities

Configuration (2 files):
- explainability-config.json → Explanation settings
- model-metadata.json → Model information

Tests (3 files):
- test-shap.py → SHAP explanation tests
- test-lime.py → LIME explanation tests
- test-visualization.js → Chart rendering tests

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

## PRE-EXECUTION CHECKPOINT

**Before proceeding, check progress tracking:**

1. Read `generated-prompts/progress.md`
2. Search for "Prompt 779: Executed" in the Execution Log
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

### STEP 1.5: MANDATORY PROCESSING REQUIREMENT

**CRITICAL**: ALL folders MUST be processed for complete feature collection.

```
storage\\agent-snapshots
```

**NO EXCEPTIONS**: Every folder (including archive, examples, research, benchmarks, ci, tests, data, logs, etc.) contains valuable features that must be documented.

**PROCEED TO STEP 2** - No skipping allowed.

### STEP 2: LOOKUP ACTUAL FILES (MANDATORY COMPLETE ENUMERATION)

**CRITICAL: Use PowerShell to verify path exists and enumerate ALL files:**

**EXECUTION INSTRUCTIONS:**

1. Copy the PowerShell code block below EXACTLY as written
2. Execute using run_terminal_cmd tool (PowerShell)
3. Do NOT modify, interpret, or break up the code
4. Execute the ENTIRE block as ONE command

**POWERSHELL COMMAND TO EXECUTE:**

```powershell
try {
    $basePath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot"
    $targetPath = Join-Path $basePath "storage\\agent-snapshots"
    
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
- **STRUCTURED OUTPUT**: Format all analysis as numbered features with complete file/folder counts
- **VERIFICATION CHECKLIST**: Before writing files, verify counts match PowerShell output exactly
- **SCAFFOLDED FILES**: Even if files are empty placeholders, they MUST be analyzed for feature intent from filename patterns
- **MINIMUM REQUIREMENT**: If folder has 50+ files, list ALL 50+ files by name
- **NO SHORTCUTS ALLOWED**: If PowerShell shows 60 files, you MUST list all 60 files individually with descriptions

**FILE ENUMERATION EXAMPLES:**

**WRONG (Incomplete):**
```
Found 10 files in backend/plugins/dex-adapters:
- uniswap-v2-adapter.js
- sushiswap-adapter.js
- ... (8 more files)  ← FORBIDDEN!
- and more files  ← FORBIDDEN!
- plus 8 additional files  ← FORBIDDEN!
- similar files  ← FORBIDDEN!
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

**Rule:** List EVERY SINGLE file by name. No shortcuts. No "etc." No "and more". No "...". No "additional files". No "similar files". No "plus X more". COUNT MUST MATCH POWERSHELL OUTPUT EXACTLY.

**LARGE FOLDER HANDLING (100+ files):**
If folder has 100+ files, list ALL files but group by type for readability:
```
Found 150 files in backend/plugins:

JavaScript files (120):
- adapter-1.js → Description
- adapter-2.js → Description
- adapter-3.js → Description
... (list ALL 120 files individually with descriptions)

Test files (20):
- test-1.test.js → Description
- test-2.test.js → Description
... (list ALL 20 files individually with descriptions)

Config files (10):
- config-1.json → Description
- config-2.json → Description
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
- adapter.js (primary) → Dex Adapters feature
- config.json (secondary) → Configuration
- README.md (secondary) → Documentation
```

**Scenario B: Empty or Scaffolded Folders**
```
IF folder exists but PowerShell finds 0 files
THEN: Feature = Scaffolded [Folder Name]
     Owner = Based on parent path context
     Implementation = "Awaiting development"

EXAMPLE: ai-modules/models/training/
- Empty folder → Scaffolded Training Models feature
- Owner = ai-modules.md (based on parent path)
```

**Scenario C: Mixed Legacy/Windows Files**
```
IF folder contains both legacy + Windows files
THEN: Focus on Windows-compatible files
     Legacy files = Reference only
     Owner = Windows functionality

EXAMPLE: dashboard/components/
- legacy-component.js (legacy) → Reference only
- windows-component.tsx (Windows) → Primary feature
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
Feature #779: Ai Modules - Found 54 files across 10 folders

- "What does this FEATURE do?" → Provides AI-powered trading modules and machine learning capabilities
- "Which MD file OWNS this FEATURE?" → ai-modules.md (core AI functionality)
- "Which MD files REFERENCE this FEATURE?" → backend.md (integration), dashboard.md (UI)
- "HOW TO IMPLEMENT → OWNER FILE (ai-modules.md)" →
  Append this section to the end of features/ai-modules.md:
  
  ## Feature 1: Ai Modules
  
  Feature Files:
  - ai-engine.js → Core AI processing engine
  - ml-models.json → Machine learning model configurations
  - training-data.csv → Training datasets for AI models
  
  Windows Implementation:
  - Implement as Windows Service for background AI processing
  - Use Windows ML for local model inference
  - Integrate with Windows Task Scheduler for periodic retraining

- "HOW TO IMPLEMENT → REFERENCES" →
  - In features/backend.md: Ai Modules → see features/ai-modules.md
  - In features/dashboard.md: Ai Modules → see features/ai-modules.md
```

**INCORRECT Output Example:**
```
❌ WRONG - Missing feature numbering
Ai Modules Analysis

❌ WRONG - Incomplete file listing
Found some files in ai-modules:
- ai-engine.js
- ... (other files)  ← FORBIDDEN!

❌ WRONG - Missing counts
Feature has various files across multiple folders

❌ WRONG - Vague implementation
Windows Implementation:
- Make it work on Windows  ← TOO VAGUE!

❌ WRONG - Missing structured format
The ai-modules feature should be implemented by adding files to the appropriate location and ensuring compatibility with the Windows environment.
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

### Folder Structure Section:

Generate visual tree showing ALL nested folders with purposes.

Example:
```
ai-modules/
├── core/                    → Core AI engine components
│   ├── engine.js           → Main processing
│   └── router.js           → Model routing
├── models/                  → ML model definitions
│   ├── training/           → Training scripts
│   └── inference/          → Inference engines
└── utils/                  → Helper utilities
```

Rules:
- Show COMPLETE nesting hierarchy
- Add arrow with folder purpose
- Include files with brief purpose
- Use tree characters properly

### Detailed File Descriptions:

Each file MUST have 20-30 word description including:

1. WHAT it does (primary function)
2. WHY it exists (business purpose)
3. HOW it integrates (connections)

Example:
```
**Core Engine (5 files):**
- core/engine.js → Main AI processing engine that orchestrates model loading, manages inference requests, caches predictions in SQLite, and triggers retraining when accuracy drops below threshold
- core/router.js → Routes incoming prediction requests to appropriate ML models based on input type, model availability, and load balancing across multiple model instances
```

FORBIDDEN:
- Generic descriptions like "Core AI processing"
- Single-word purposes like "Configuration"
- Missing integration details

REQUIRED:
- 20-30 words per file minimum
- Specific technical details
- Integration information
- Business value explanation

(FILENAME-ONLY, APPEND-ONLY)

- Derive Feature Name from the last segment of the legacy path (see "Feature Name Derivation")
- **FILE COMPLETENESS CHECK**: Feature Files list MUST include representation of ALL files found in STEP 2
- **NO PARTIAL LISTINGS**: Never use "and more files" or "additional files" - be complete and specific
- **SCAFFOLDED FILE ANALYSIS**: Empty files must be analyzed by filename patterns to determine intended purpose

**FUNCTIONAL ANALYSIS MATRIX (PRE-GROUPING INTELLIGENCE):**

Before grouping files, analyze EACH file across 5 dimensions:

**1. Data Flow Role:**
- Input → Receives external data (RPC calls, API responses, user input)
- Processing → Transforms/analyzes data (calculations, ML inference, routing)
- Output → Sends data externally (transactions, API calls, UI updates)
- Storage → Persists data (database writes, file saves, cache updates)

**2. Execution Context:**
- Main Thread → Runs in primary application process (UI rendering, user interactions)
- Background → Runs in separate process/worker (heavy computations, monitoring)
- Scheduled → Triggered by time/cron (periodic tasks, cleanup, retraining)
- Event-Driven → Triggered by events (blockchain events, price changes, alerts)

**3. Dependencies (What It Requires):**
- External Services → RPC nodes, APIs, databases, file systems
- Internal Modules → Other project files it imports/requires
- Configuration → Settings, secrets, environment variables
- Runtime → Node.js version, Python packages, system libraries

**4. Dependents (What Depends On It):**
- Direct Consumers → Files that import/call this file
- Indirect Consumers → Features that rely on its functionality
- UI Components → Dashboard elements displaying its data
- External Systems → Blockchain contracts, APIs consuming its output

**5. Windows Integration Point:**
- Service → Runs as Windows Service (backend engines, monitors)
- UI → Electron renderer process (dashboard components, charts)
- Storage → File system/registry/database (configs, logs, data)
- Config → Settings management (registry, JSON files, env vars)
- Security → Credential Manager, encryption, certificates

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
- *.pt, *.pth → PyTorch (ML Models)
- *.h5, *.keras → Keras/TensorFlow (ML Models)
- *.pkl, *.pickle → Pickle (Serialized Data)
- *.onnx → ONNX (Cross-platform ML)
- *.sqlite3, *.db → Database files

**WINDOWS COMPONENT MAPPING:**

Map features to specific Windows technologies:

**For Backend Services:**
- Component: Windows Service (node-windows)
- Process Manager: PM2 or node-windows-service
- Auto-start: Windows Service Manager

**For UI Components:**
- Framework: Electron BrowserWindow
- Renderer: Chromium-based rendering
- IPC: Electron IPC (Main → Renderer)

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
✅ "Load adapters dynamically from plugin directory at service startup"
✅ "Store configuration in application data directory with JSON format"
✅ "Display real-time metrics in Electron dashboard widget"

❌ "The system will load the adapters" (too vague)
❌ "Load adapters from C:\Program Files\..." (specific path)
❌ "Use dynamic loading with require() and fs.readdir()" (too technical)

### MANDATORY OUTPUT FORMAT ENFORCEMENT

**Your output MUST include ALL of these elements:**

1. ✅ **Feature Number**: Count existing "## Feature" headers in target file, then use next number
   - Format: `## Feature [N]: [Feature Name]`
   - Example: If file has 2 features, new one is `## Feature 3:`

2. ✅ **Complexity Score**: Based on file count
   - 1-5 files = ⭐ (Simple)
   - 6-15 files = ⭐⭐ (Moderate)
   - 16-30 files = ⭐⭐⭐ (Complex)
   - 31-50 files = ⭐⭐⭐⭐ (Very Complex)
   - 51+ files = ⭐⭐⭐⭐⭐ (Highly Complex)

3. ✅ **File Count**: State exact count in header
   - Format: `## Feature [N]: [Name] ⭐⭐⭐ (Complex - 25 files)`

4. ✅ **File Grouping**: Group files by purpose (Core Logic, ML Models, Tests, etc.)
   - List ALL files found in PowerShell output
   - Group by function, not just extension

5. ✅ **Technologies Section**: Detect and list tech stack
   - Format: `Technologies: Python, PyTorch, Jupyter, NumPy`

6. ✅ **Windows Implementation**: Minimum 8-12 detailed bullets
   - Each bullet: one sentence describing WHAT, WHERE, HOW
   - No OS-specific paths, no code snippets

7. ✅ **References**: Add to other .md files
   - Format: `- [Feature Name] → see features/[owner].md`

8. ✅ **Progress Update**: Update progress.md with prompt number
   - Increment counter, update date, add log entry

9. ✅ **Cleanup**: Delete temp_*.ps1 files created during execution

**VALIDATION CHECKLIST:**
- [ ] Feature number is sequential (counted existing features)
- [ ] Complexity score matches file count
- [ ] ALL files from PowerShell are listed
- [ ] Technologies section present
- [ ] 8-12 Windows Implementation bullets
- [ ] References added to other .md files
- [ ] progress.md updated
- [ ] Temp files deleted

**If ANY element is missing, your output is INCOMPLETE and MUST be revised.**

### STEP 6: ACTUALLY WRITE TO FILES (STRICT APPEND-ONLY)

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
- Use write tool to ACTUALLY WRITE to the features/*.md files
- **CRITICAL RESTRICTION**: ONLY modify or create .md files inside features/ folder
- **NO NEW PROJECT FILES**: Never create .js, .ts, .py, .sol, .json, or any executable/real implementation files
- **NO NEW FOLDERS**: Never create directories anywhere in the project
- **Creation rule**: If the owner/reference .md does not exist (e.g., config.md, security.md), CREATE features/[name].md and then append
- **APPEND-ONLY**: Read existing content first, then append the new "## Feature:" section to the END
- **Preserve all existing content**: never overwrite, replace, or delete

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



## Input Format

PATH-TO-FEATURE MAPPER
Full Path: C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\storage\\agent-snapshots

## OUTPUT FORMAT (EXACT TEMPLATE - DO NOT DEVIATE)

**Copy this template EXACTLY and fill in the values:**

```
- "What does this FEATURE do?" → [your 1-2 line description]
- "Which MD file OWNS this FEATURE?" → [owner.md] ([reason])
- "Which MD files REFERENCE this FEATURE?" → [md1], [md2] ([reasons])
- "HOW TO IMPLEMENT → OWNER FILE ([owner].md)" →
  Append this section to the end of features/[owner].md:

  ## Feature [N]: [Feature Name]

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
- ci/* | .gitlab/* → deployment.md (CI/CD pipelines)
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

### SIMPLIFIED PROGRESS UPDATE

**Step 1: Update Progress**

```powershell
# Read current progress
$progressContent = Get-Content "generated-prompts/progress.md" -Raw

# Update completion count
$newContent = $progressContent -replace "Completed: \d+/842", "Completed: 779/842"
$newContent = $newContent -replace "Last Updated: [^\r\n]*", "Last Updated: $(Get-Date -Format 'MMMM dd, yyyy')"

# Add execution log entry
$logEntry = "`nPrompt 779: Executed - Added 'Feature: [Feature Name]' to features/[owner].md"
$newContent = $newContent -replace "<!-- AI: Append new log entries below this line -->", "<!-- AI: Append new log entries below this line -->$logEntry"

# Write updated content
Set-Content "generated-prompts/progress.md" $newContent -NoNewline
Write-Host "Progress updated successfully"
```

**Step 2: Cleanup**

```powershell
# Delete any temp PowerShell files created during execution
Get-ChildItem "temp_*.ps1" -ErrorAction SilentlyContinue | Remove-Item -Force
Write-Host "Cleanup completed"
```

**Before marking complete, validate generated files:**

```powershell
# Validate generated .md file
$targetFile = "features/[owner].md"

if (Test-Path $targetFile) {
    $content = Get-Content $targetFile -Raw
    
    # Check required elements
    $checks = @{
        "Feature header" = $content -match "## Feature:"
        "Feature files list" = $content -match "Feature Files:"
        "Windows implementation" = $content -match "Windows Implementation:"
        "Minimum bullets" = ($content | Select-String "^- ").Count -ge 8
    }
    
    $allPassed = $true
    foreach ($check in $checks.GetEnumerator()) {
        if (-not $check.Value) {
            Write-Host "❌ Validation failed: $($check.Key)"
            $allPassed = $false
        } else {
            Write-Host "✅ $($check.Key): Passed"
        }
    }
    
    if (-not $allPassed) {
        Write-Host "❌ .md validation failed - prompt incomplete"
        exit 1
    }
} else {
    Write-Host "❌ Target file not found: $targetFile"
    exit 1
}
```

**Mark this prompt as COMPLETE only after all validations pass.**

### 20-POINT VALIDATION MATRIX (SYSTEMATIC QUALITY ASSURANCE)

**Execute this checklist before marking prompt complete:**

**File Enumeration (5 points):**
- [ ] 1. PowerShell executed successfully without errors
- [ ] 2. All files enumerated with "FILE X/Y" format showing progress
- [ ] 3. File count matches PowerShell output exactly
- [ ] 4. No files skipped or summarized with "etc."
- [ ] 5. Subfolder files included recursively

**Feature Analysis (5 points):**
- [ ] 6. Feature number is sequential (counted existing features)
- [ ] 7. Complexity score matches file count (⭐ to ⭐⭐⭐⭐⭐)
- [ ] 8. Technologies section present with detected stack
- [ ] 9. Files grouped by purpose (Core Logic, Tests, etc.)
- [ ] 10. Each file has 20-30 word description

**Windows Implementation (5 points):**
- [ ] 11. Minimum 8-12 implementation bullets present
- [ ] 12. Each bullet follows "Action + Component + Purpose" format
- [ ] 13. No OS-specific paths (no C:\, %AppData% literals)
- [ ] 14. Windows components mapped correctly (Service, Electron, etc.)
- [ ] 15. Integration points clearly described

**File Operations (5 points):**
- [ ] 16. Owner .md file updated with append-only behavior
- [ ] 17. Reference .md files updated with cross-references
- [ ] 18. progress.md updated with prompt number and date
- [ ] 19. Temp PowerShell files deleted (temp_*.ps1)
- [ ] 20. No duplicate feature names in target files

**SCORING:**
- 20/20 = ✅ PERFECT - Mark complete
- 18-19/20 = ✅ ACCEPTABLE - Mark complete with notes
- 15-17/20 = ⚠️ NEEDS REVIEW - Fix issues before completing
- <15/20 = ❌ FAILED - Do not mark complete, restart execution

**If score < 18: STOP and fix all failing checks before proceeding**

---


### CONFIDENCE SCORING (AI SELF-ASSESSMENT)

**Rate your confidence in this execution (1-10):**

- **File enumeration accuracy**: [Score] - Did PowerShell find all expected files?
- **Feature mapping correctness**: [Score] - Is the feature correctly identified?
- **Owner file assignment**: [Score] - Is the owner .md file correct?
- **Implementation completeness**: [Score] - Are all required elements present?

**If any score < 7: STOP and review before proceeding**

**Mark this prompt as COMPLETE only after all validations pass.**

---

**DO NOT USE:**
- ❌ list_dir tool
- ❌ read_file for enumeration
- ❌ Relative paths like "Apex Arbitrage Multichain bot/ai-modules"

**MUST USE:**
- ✅ run_terminal_cmd tool (PowerShell)
- ✅ Full Windows paths with C:\

**IF TOOL FAILS 2 TIMES: STOP and report error. DO NOT retry same command 3+ times.**
