# APEX WINDOWS FEATURE-MAPPING PROMPT (AI-OPTIMIZED)

**Transform ANY legacy component into clear Windows feature specifications**

---

## 🛡️ ACCESS VERIFICATION PROTOCOL (MANDATORY)

### Trust-But-Verify AI Repository Access

**BEFORE ANY REPOSITORY CHANGES, USE ONE OF THESE VERIFICATION COMMANDS:**

### 🔐 Write-Proof (Strongest Verification)
```
ACCESS-PROOF WRITE repo=Apex-Arbitrage-Multichain-bot-for-windows branch=main nonce=WIN-VERIFY-001
```

**Expected AI Response:**
- Creates file: `.apex/verify/WIN-VERIFY-001.json`
- Returns: Commit SHA, file path, SHA-256 hash
- You verify by refreshing repo and checking file exists

### 📖 Read-Proof (Verification)
```
ACCESS-PROOF READ repo=Apex-Arbitrage-Multichain-bot-for-windows path=PROMPT.md
```

**Expected AI Response:**
- Returns: First 120 characters, byte length, SHA-256 hash
- You verify by comparing locally

### ✏️ Update-Proof (Light Verification)
```
ACCESS-PROOF UPDATE repo=Apex-Arbitrage-Multichain-bot-for-windows path=PROMPT.md nonce=WIN-VERIFY-002
```

**Expected AI Response:**
- Appends line: `<!-- access-proof:WIN-VERIFY-002 -->`
- Returns: Commit SHA and last line
- Can revert immediately if requested

### 🚨 AI Safety Protocol
- **If verification PASSES**: AI can make direct repo changes
- **If verification FAILS**: AI switches to paste-only mode
- **No verification**: AI must provide paste-ready content only

---

# 🗂️ PATH-TO-FEATURE MAPPER (INTELLIGENT FILE ANALYSIS)

## 🧠 MANDATORY ANALYSIS PROCESS:

### **STEP 1: PARSE INPUT PATH**
- Extract folder path from: `Apex Arbitrage Multichain bot/[folder-path]`

### **STEP 2: LOOKUP ACTUAL FILES** 
- Search `PROJECT TREE COMPLETE STRUCTURE .md` for exact folder path
- Extract all actual files and subfolders found in that path
- DO NOT use generic assumptions - USE REAL FILE ANALYSIS

### **STEP 3: ANALYZE FILES FOR WINDOWS FEATURES**
- Based on actual file names/extensions found, determine Windows desktop feature
- Examples:
  - `*.json presets` = Dashboard layout management
  - `*.test.js` = Testing functionality
  - `*-adapter.js` = Integration adapter
  - `*.sol contracts` = Smart contract feature
  - `*-engine.js` = Core engine functionality

### **STEP 4: MAP TO .MD FILE**
- Based on feature analysis, assign to appropriate Windows project .md file
- Consider integration needs based on actual file dependencies

---

## 🎯 INPUT FORMAT:
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/[your-folder-path]
```

## 🚨 MANDATORY OUTPUT FORMAT (EXACTLY 3 LINES):
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ [Feature description based on ACTUAL FILES found in the path]

📁 "Which MD file OWNS this FEATURE?"
→ **[filename].md** ([reason based on actual file analysis])

🔗 "Which MD files REFERENCE this FEATURE?"
→ **[file1].md**, **[file2].md**, **[file3].md** ([reasons based on real integration needs])
```

## ❌ ABSOLUTELY FORBIDDEN:
- **NO detailed specifications**
- **NO "PRIMARY SPECIFICATION" sections**  
- **NO "INTEGRATION NOTES" sections**
- **NO acceptance criteria or performance targets**
- **NO Windows implementation details**
- **NO generic responses - MUST analyze actual files**
- **ONLY the 3-line mapping above**

---

## 📋 INTELLIGENT MAPPING RULES (Based on Actual Files):

### **File Pattern Analysis:**
- **presets/*.json** → dashboard.md (UI configuration)
- ***-adapter.js** → backend.md (integration adapters)
- ***.test.js** → testing.md (test functionality)
- ***-engine.js** → backend.md (core engine)
- ***.sol** → contracts.md (smart contracts)
- ***-config.json** → config.md (configuration)
- ***-security.*|audit-*|logs/security** → security.md (security)
- **docs/*|*.md** → docs.md (documentation)
- **deploy/*|kubernetes/*|helm/*|terraform/*** → deployment.md (deployment)
- **ai-*|models/*|train/*|datasets/*|notebooks/*** → ai-modules.md (AI/ML)

### **Folder Pattern Analysis:**
- **dashboard/** → dashboard.md
- **backend/** → backend.md
- **ai-modules/** → ai-modules.md
- **config/** → config.md
- **contracts/** → contracts.md
- **security/**, **logs/security** → security.md
- **tests/** → testing.md
- **deploy/**, **scripts/** → deployment.md
- **docs/** → docs.md

---

## 💡 CORRECT EXAMPLES (Using Real File Analysis):

### **Example 1: Dashboard Presets**
**Input:** `Apex Arbitrage Multichain bot/dashboard/presets`
**Files Found:** advanced-presets.json, ai-presets.json, layout-presets.json, theme-presets.json, user-presets.json
**Output:**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Manages dashboard layout presets and themes for different user roles and scenarios

📁 "Which MD file OWNS this FEATURE?"
→ **dashboard.md** (UI presets and layouts belong to dashboard system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **config.md** (preset storage), **docs.md** (user guide), **testing.md** (preset switching tests), **security.md** (user permissions)
```

### **Example 2: Backend Engine Utils**
**Input:** `Apex Arbitrage Multichain bot/backend/engine/utils`
**Files Found:** math-utils.js, retry-helpers.js, timing-utils.js, serialization.js
**Output:**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Provides core execution utilities for math operations, retries, timing, and data serialization

📁 "Which MD file OWNS this FEATURE?"
→ **backend.md** (engine utilities are core backend functionality)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **testing.md** (utility testing), **docs.md** (API documentation), **config.md** (utility settings)
```

---

## 📂 Available MD Files for Windows Project:

### **Core Windows Features (P0-P1)**
- **install-dependencies.md** - Windows installer, dependency management, bootstrap process
- **config.md** - Configuration system, settings management, validation
- **backend.md** - Core execution engine, arbitrage logic, API services
- **dashboard.md** - User interface, control panels, real-time displays

### **Advanced Features (P1-P2)**
- **ai-modules.md** - Machine learning, decision engines, pattern recognition
- **contracts.md** - Smart contract deployment, blockchain integration
- **security.md** - Authentication, encryption, key management, audit trails

### **Supporting Features (P2-P3)**
- **testing.md** - Quality assurance, automated testing, validation
- **deployment.md** - Windows packaging, distribution, updates
- **docs.md** - User guides, troubleshooting, operator manuals

---

## 🚀 Ready to Use!

**ALWAYS START WITH ACCESS VERIFICATION:**
```
ACCESS-PROOF WRITE repo=Apex-Arbitrage-Multichain-bot-for-windows branch=main nonce=<YOUR-RANDOM>
```

**For intelligent path mapping with real file analysis:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: [your-folder-path]
```

**The AI will analyze the actual files in that path and give you precise Windows feature mapping!**