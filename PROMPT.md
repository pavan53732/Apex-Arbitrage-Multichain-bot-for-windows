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

# 🗂️ PATH-TO-FEATURE MAPPER (INTELLIGENT FILE ANALYSIS + IMPLEMENTATION)

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

### **STEP 5: IMPLEMENTATION GUIDE (FILENAME-ONLY)**
- Show EXACTLY how to add to the owner MD (no folder paths, filenames only)
- Show EXACTLY what one-line references to add in other MDs
- Use filename-only format for all file lists

---

## 🎯 INPUT FORMAT:
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/[your-folder-path]
```

## 🚨 MANDATORY OUTPUT FORMAT (EXACTLY 5 SECTIONS):
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ [Feature description based on ACTUAL FILES found in the path]

📁 "Which MD file OWNS this FEATURE?"
→ **[filename].md** ([reason based on actual file analysis])

🔗 "Which MD files REFERENCE this FEATURE?"
→ **[file1].md**, **[file2].md**, **[file3].md** ([reasons based on real integration needs])

📝 "HOW TO IMPLEMENT - OWNER FILE ([filename].md):"
## 📊 [Feature Name] System
### **Feature Files**
- `[file1]` - [description]
- `[file2]` - [description]  
- `[file3]` - [description]

### **Windows Implementation**
- [Brief implementation details - no OS paths]

📝 "HOW TO IMPLEMENT - REFERENCES:"
**In [file1].md**, add: "- [Feature reference] (see [owner].md)"
**In [file2].md**, add: "- [Feature reference] (see [owner].md)"
**In [file3].md**, add: "- [Feature reference] (see [owner].md)"
```

## ❌ ABSOLUTELY FORBIDDEN:
- **NO detailed specifications**
- **NO "PRIMARY SPECIFICATION" sections**  
- **NO "INTEGRATION NOTES" sections**
- **NO acceptance criteria or performance targets**
- **NO Windows system paths like %APPDATA%**
- **NO generic responses - MUST analyze actual files**
- **ONLY the 5-section format above**

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
- **performance-*.log|metrics-*.log** → testing.md (performance monitoring)

### **Folder Pattern Analysis:**
- **dashboard/** → dashboard.md
- **backend/** → backend.md
- **ai-modules/** → ai-modules.md
- **config/** → config.md
- **contracts/** → contracts.md
- **security/**, **logs/security** → security.md
- **logs/performance-logs** → testing.md (performance monitoring)
- **tests/** → testing.md
- **deploy/**, **scripts/** → deployment.md
- **docs/** → docs.md

### **Filename-only Rule (for all file lists):**
- Show filenames only (no directories or OS paths)
- Example:
  - `cpu-usage.log` - CPU utilization tracking
  - `memory-stats.log` - Memory consumption data
  - `network-metrics.log` - Network latency measurements
  - `gas-consumption.log` - Gas fee analysis
  - `error-tracking.log` - Error rate monitoring

---

## 💡 CORRECT EXAMPLE (Complete 5-Section Format):

**Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/logs/performance-logs
```

**Output:**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Captures system and execution performance metrics (CPU, memory, network, gas consumption) for monitoring and optimization

📁 "Which MD file OWNS this FEATURE?"
→ **testing.md** (performance monitoring and metrics belong to testing/QA system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **backend.md** (generates performance data), **dashboard.md** (performance widgets), **config.md** (log retention settings), **docs.md** (monitoring guide)

📝 "HOW TO IMPLEMENT - OWNER FILE (testing.md):"
## 📊 Performance Logging System
### **Feature Files**
- `cpu-usage.log` - CPU utilization tracking
- `gas-usage.log` - Gas consumption metrics  
- `memory-usage.log` - Memory utilization data
- `network-usage.log` - Network performance metrics

### **Windows Implementation**
- Node.js logging system writes to project files
- JSON format with timestamps
- Dashboard reads files for real-time display
- Daily rotation with 30-day retention

📝 "HOW TO IMPLEMENT - REFERENCES:"
**In backend.md**, add: "- Performance metrics logged to testing system (see testing.md)"
**In dashboard.md**, add: "- Performance widgets display data from performance logs (see testing.md)"
**In config.md**, add: "- Performance log settings configured in testing.md"
**In docs.md**, add: "- Performance monitoring guide covered in testing.md"
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

**For intelligent path mapping with implementation guide:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: [your-folder-path]
```

**The AI will analyze the actual files AND show you exactly how to implement the feature in your Windows project with filename-only lists!**