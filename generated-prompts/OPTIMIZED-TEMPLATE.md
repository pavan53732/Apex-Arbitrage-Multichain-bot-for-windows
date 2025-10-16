
## 🎯 CORE MISSION: PATH → WINDOWS FEATURE

**INPUT:** Legacy folder path  
**OUTPUT:** Complete Windows feature documentation  
**METHOD:** PowerShell enumeration → Technical analysis → .md generation

---

## 🚨 PROJECT ANALYSIS SCOPE RESTRICTION 🚨

**This mode never reads features/*.md; documentation happens only after analysis.**

**WHEN YOU SWITCH TO PROJECT ANALYSIS MODE:**
**FORBIDDEN ACTIONS:**
- ❌ DO NOT analyze the features/ folder in the root directory
- ❌ DO NOT read any .md files from features/ folder
- ❌ DO NOT scan the root project directory
- ❌ DO NOT explore folders outside the specified path

**MANDATORY ACTIONS:**
- ✅ ONLY analyze files in the EXACT path specified in STEP 1.5
- ✅ ONLY use PowerShell output from STEP 2 for file enumeration
- ✅ ONLY work with the target folder path provided in the prompt
- ✅ IGNORE all other folders and files in the project

**EXAMPLE:** If prompt says: `ai-modules\models\trainingOutputs`
- ✅ CORRECT: Analyze ONLY files in `C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\ai-modules\models\trainingOutputs`
- ❌ WRONG: Reading features/ai-modules.md from root directory
- ❌ WRONG: Scanning other folders in the project
- ❌ WRONG: Analyzing files outside the specified path

**VERIFICATION:** Before analyzing ANY file, ask yourself:
- Is this file inside the target path from STEP 1.5?
- YES → Proceed
- NO → STOP and ignore this file

---

## EXECUTION PROTOCOL

### STEP 1: FILE DISCOVERY
```powershell
try {
    $path = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\[PATH]"
    if (-not (Test-Path $path)) { Write-Host "ERROR: Path not found"; exit 1 }
    
    $files = Get-ChildItem -Path $path -Recurse -File -Force
    $folders = Get-ChildItem -Path $path -Recurse -Directory -Force
    
    Write-Host "TOTAL FILES: $($files.Count) | TOTAL FOLDERS: $($folders.Count)"
    
    if ($files.Count -gt 500) { Write-Host "LARGE FOLDER: Consider chunking" }
    
    $files | Sort-Object FullName | ForEach-Object -Begin {$i=1} -Process { 
        Write-Host "FILE $i/$($files.Count): $($_.FullName)"
        $i++
    }
} catch { Write-Host "ERROR: $($_.Exception.Message)" }
```

### 🚨 LARGE FOLDER PROTOCOL 🚨

**IF PowerShell shows 500+ files:**
- Process in chunks of 200 files per response  
- Use [CONTINUING IN NEXT RESPONSE] at end of chunk
- Use [CONTINUING FROM PREVIOUS] at start of next chunk
- Continue until ALL files documented
- Never skip files between chunks
- Final response must show complete file count validation

**CHUNKING EXAMPLE:**
```
Response 1: Files 1-200 [CONTINUING IN NEXT RESPONSE]
Response 2: [CONTINUING FROM PREVIOUS] Files 201-400 [CONTINUING IN NEXT RESPONSE] 
Response 3: [CONTINUING FROM PREVIOUS] Files 401-500 [COMPLETE]
```

**VERIFICATION:** Total documented files must equal PowerShell count exactly

### STEP 2: FEATURE ANALYSIS
- **Name**: Last path segment → Title Case
- **Complexity**: File count → Star rating (⭐-⭐⭐⭐⭐⭐)
- **Technologies**: Detect from extensions
- **Owner**: Route to correct features/*.md
- **References**: 2-4 related .md files

### 🚨 MANDATORY FOLDER TREE STRUCTURE 🚨

**CRITICAL**: You MUST include a COMPLETE folder tree structure showing ALL nested folders AND ALL FILES.

**REQUIRED FORMAT:**
```
## Folder Structure
FOLDER 1/3: foldername/
├── FOLDER 1/2: subfolder1/
│   ├── FILE 1/3: file1.js
│   ├── FILE 2/3: file2.js
│   └── FILE 3/3: file3.js
├── FOLDER 2/2: subfolder2/
│   ├── FILE 1/2: file4.js
│   └── FILE 2/2: file5.js
└── FILE 1/1: rootfile.js
```

**NUMBERING RULES (STRICT):**
- **FOLDER X/Y: foldername/** where X = current position, Y = total at that level
- **FILE X/Y: filename.ext** where X = current position, Y = total in that folder
- **Each level resets numbering** (1/3, 1/2, NOT 1/3, 4/5)
- **Sequential numbering within each folder**
- **Order at each level: subfolders A→Z, then files A→Z**
- **List EVERY file with detailed descriptions** (20-30 words each)

**FORBIDDEN:**
- ❌ Skipping folders or using "and more folders"
- ❌ Skipping files or using "and more files"
- ❌ Not including the folder tree section
- ❌ Using "[LIST ALL OTHER FILES]" without actually listing them

**VERIFICATION:**
- Count folders in your tree → Must match PowerShell folder count
- Count files in your tree → Must match PowerShell file count
- **Zero-shortcut policy applies globally**

### STEP 3: WINDOWS MAPPING
**Required Components (8-12 bullets):**
- Windows Service (backend engines)
- Electron UI (dashboard components)
- SQLite Database (data storage)
- Task Scheduler (automation)
- Event Log (monitoring)
- Credential Manager (security)
- File System (configuration)
- Registry (settings)

### STEP 4: DOCUMENTATION
**Append to features/[owner].md:**
```markdown
## Feature N: [Name] ⭐⭐⭐ ([Count] files)

Feature Files:
[Group files by purpose - list ALL with 20-30 word descriptions]

Technologies: [Detected stack]

Windows Implementation:
- [8-12 specific implementation bullets]
```

**Add references to related .md files**

### 🚨 MANDATORY FEATURE FILES SECTION 🚨

**CRITICAL**: You MUST list EVERY SINGLE FILE in the Feature Files section with detailed descriptions.

**REQUIRED FORMAT:**
```markdown
**Core Logic (5 files):**
- core/engine.js → Main AI processing engine that orchestrates model loading, manages inference requests, caches predictions in SQLite, and triggers retraining when accuracy drops below threshold (25 words)
- core/router.js → Routes incoming prediction requests to appropriate ML models based on input type, model availability, and load balancing across multiple model instances (24 words)
- core/processor.js → Processes raw blockchain data into normalized feature vectors for ML model consumption, handles data validation, type conversion, and missing value imputation (25 words)
```

**DESCRIPTION LENGTH REQUIREMENTS:**
- **MINIMUM**: 20 words per file
- **MAXIMUM**: 30 words per file
- **FORBIDDEN**: Generic descriptions like "configuration file" or "helper utilities"
- **REQUIRED**: Specific purpose, key functions, dependencies, Windows integration details

**VERIFICATION**: Count words in each description - must be 20-30 words

---

## QUALITY GATES

### MANDATORY REQUIREMENTS
- ✅ List EVERY file (no "etc." or "...")
- ✅ 20-30 words per file description
- ✅ File count matches PowerShell exactly
- ✅ Complete folder tree with FOLDER X/Y and FILE X/Y numbering
- ✅ Technologies section present
- ✅ 8-12 Windows implementation bullets
- ✅ Cross-references added
- ✅ UTF-8 encoding preserved (🚨 ⚠️ ✅ ❌)

### FORBIDDEN SHORTCUTS
- ❌ Skipping files with "and more"
- ❌ Generic descriptions under 20 words
- ❌ Missing nested folders
- ❌ Count mismatches
- ❌ Incomplete Windows mapping
- ❌ Using corrupted UTF-8 characters (ðŸš¨, âš ï¸, âŸŒ, âœ…, â†')

### 🚨 FINAL VALIDATION CHECK - MANDATORY 🚨

**VALIDATION GATE:**
- **Counts match**: PowerShell count = Your tree count = Feature Files count
- **Numbering correct**: FOLDER X/Y and FILE X/Y format used correctly
- **Descriptions 20-30**: Every file description is 20-30 words
- **UTF-8 intact**: Proper UTF-8 emojis used (🚨 ⚠️ ✅ ❌)
- **Zero-shortcut policy applies globally**

**IF ANY VERIFICATION FAILS:**
- STOP and fix the issue immediately
- DO NOT write incomplete files
- DO NOT proceed with mismatched counts

---

## FILE ROUTING TABLE

| File Pattern | Owner .md |
|-------------|----------|
| *.sol, contracts/ | contracts.md |
| backend/, server/, api/ | backend.md |
| dashboard/, ui/, components/ | dashboard.md |
| ai-*, models/, *.py | ai-modules.md |
| test/, *.test.js | testing.md |
| deploy/, ci/, docker/ | deployment.md |
| config/, *.env, settings/ | config.md |
| security/, auth/, encryption/ | security.md |
| docs/, *.md | docs.md |
| install/, setup/, package.json | install-dependencies.md |

---

## WINDOWS TECH STACK

**Backend Services:**
- Node.js Windows Service (node-windows)
- PM2 Process Manager
- SQLite Database (better-sqlite3)

**Frontend Interface:**
- Electron Framework
- React/TypeScript UI
- WebSocket Real-time Updates

**System Integration:**
- Windows Task Scheduler
- Windows Event Log
- Windows Credential Manager
- Windows Registry
- Windows Toast Notifications

**Data & Storage:**
- %AppData% Application Directory
- SQLite for Structured Data
- JSON for Configuration
- CSV/Parquet for Analytics

---

## VALIDATION CHECKLIST

**Before Writing Files:**
- [ ] PowerShell executed successfully
- [ ] All files enumerated completely
- [ ] File descriptions are 20-30 words
- [ ] Complexity score calculated
- [ ] Technologies detected accurately
- [ ] Windows implementation planned
- [ ] Owner .md file determined
- [ ] Reference files identified

**After Writing Files:**
- [ ] Owner .md updated with new feature
- [ ] Reference .md files updated
- [ ] Cross-references added
- [ ] File counts verified
- [ ] No duplicate features created

---

## OUTPUT TEMPLATE

```
- "What does this FEATURE do?" → [1-2 line description]
- "Which MD file OWNS this FEATURE?" → [owner.md] ([reason])
- "Which MD files REFERENCE this FEATURE?" → [md1], [md2] ([reasons])
- "HOW TO IMPLEMENT → OWNER FILE ([owner].md)" →
  [Complete feature documentation]
- "HOW TO IMPLEMENT → REFERENCES" →
  [Cross-reference additions]
```

**CRITICAL:** Execute in order, validate completely, no shortcuts allowed.

---

## 🚨 MANDATORY CHECKPOINT: NUMBERING FORMAT CONFIRMATION ⚠️

**STOP AND READ - DO NOT PROCEED TO STEP 5 WITHOUT COMPLETING THIS CHECKPOINT**

**BEFORE PROCEEDING TO STEP 5, REMEMBER:**
**MANDATORY FOLDER TREE REQUIREMENTS:**
- ✅ **FOLDER X/Y: foldername/** format (X = current position, Y = total at that level)
- ✅ **FILE X/Y: filename.ext** format (X = current position, Y = total in that folder)
- ✅ **Each level resets numbering** (1/3, 1/2, NOT 1/3, 4/5)
- ✅ **Sequential numbering within each folder**
- ✅ **Order at each level: subfolders A→Z, then files A→Z**
- ✅ **List EVERY file with detailed descriptions** (20-30 words each)
- ✅ **Show ALL nested folders and subfolders**
- ✅ **Zero-shortcut policy applies globally**

**IF YOU FORGET THESE REQUIREMENTS, YOUR OUTPUT WILL BE REJECTED!**

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