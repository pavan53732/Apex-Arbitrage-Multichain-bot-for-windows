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

## 🎯 Purpose
Convert legacy components from your 6,165-file system into **Windows-first feature specifications** that clearly show:
- **"What does this FEATURE do?"** → Clear feature description
- **"Which MD file OWNS this FEATURE?"** → Primary specification file  
- **"Which MD files REFERENCE this FEATURE?"** → Integration points

## 📝 How to Use This Prompt
1. **START WITH ACCESS VERIFICATION** using commands above
2. **Copy the entire "YOUR INPUT" template** below
3. **Fill in your component details** 
4. **Submit to AI** 
5. **Receive clear guidance** on exactly which MD files to update

---

# 🗂️ PATH-TO-FEATURE MAPPER MODE (SIMPLE 3-LINE MAPPING ONLY)

## 🚀 CRITICAL: This mode returns EXACTLY 3 lines - NOTHING MORE!

### Input Format:
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/[your-folder-path]
```

### 🚨 MANDATORY Output Format (AI MUST FOLLOW EXACTLY):
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ [ONE sentence describing the feature - maximum 20 words]

📁 "Which MD file OWNS this FEATURE?"
→ **[filename].md** ([short reason - maximum 10 words])

🔗 "Which MD files REFERENCE this FEATURE?"
→ **[file1].md**, **[file2].md**, **[file3].md** ([short reason for each])
```

### ❌ FORBIDDEN in PATH-TO-FEATURE MAPPER:
- **NO detailed specifications**
- **NO "PRIMARY SPECIFICATION" sections**
- **NO "INTEGRATION NOTES" sections**
- **NO acceptance criteria**
- **NO performance targets**
- **NO Windows implementation details**
- **ONLY the 3-line mapping above**

### Path Mapping Rules:
- **backend/engine/** → backend.md
- **backend/plugins/** → backend.md  
- **backend/data/** → backend.md
- **backend/gas/** → backend.md
- **backend/mempool/** → backend.md
- **dashboard/** → dashboard.md
- **dashboard/widgets/** → dashboard.md
- **dashboard/overlays/** → dashboard.md
- **dashboard/presets/** → dashboard.md
- **ai-modules/** → ai-modules.md
- **ai-modules/models/** → ai-modules.md
- **config/** → config.md
- **contracts/** → contracts.md
- **security/** → security.md
- **logs/security/** → security.md
- **logs/audit/** → security.md
- **tests/** → testing.md
- **deploy/installer/** → install-dependencies.md
- **docs/** → docs.md

---

# 🔄 FULL FEATURE MAPPING REQUEST TEMPLATE

## YOUR INPUT (Copy and Fill This Section)

```
APEX WINDOWS FEATURE MAPPING REQUEST

=== COMPONENT ANALYSIS ===
Component Name: [Name of your legacy component or new feature idea]
Component Type: [Feature | Subsystem | Adapter | Service | UI Widget | Config | Documentation]
Original Purpose: [What did this do in your old system? Or what should this new feature do?]
Priority Level: [P0-Critical | P1-High | P2-Medium | P3-Nice-to-have]

=== WINDOWS IMPLEMENTATION ===
Runtime Needs: [Electron Desktop | Node.js Service | Python Scripts | Windows Service]
Data Storage: [SQLite Database | File Logs | Cache | Registry]
User Interface: [Dashboard Widget | Configuration Panel | System Tray | None]
Security Requirements: [API Key Storage | Wallet Integration | Log Redaction | Encryption]
Performance Target: [Response time, throughput, or other measurable goals]

=== FEATURE MAPPING QUESTION ===
Please tell me:
1. "What does this FEATURE do?" → [Clear 1-sentence description]
2. "Which MD file OWNS this FEATURE?" → [Primary file that contains the main specification]
3. "Which MD files REFERENCE this FEATURE?" → [List of files that need integration notes]
```

---

## 📂 Available MD Files (Your Options)

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

## 💡 Worked Examples

### **Example 1: PATH-TO-FEATURE MAPPER (Simple)**

**Your Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/logs/security-log
```

**AI Response (MUST BE EXACTLY THIS FORMAT):**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Tracks security events and authentication attempts for compliance monitoring

📁 "Which MD file OWNS this FEATURE?"
→ **security.md** (security logging belongs to security system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **backend.md** (generates events), **dashboard.md** (security alerts), **config.md** (log settings), **docs.md** (monitoring guide)
```

### **Example 2: PATH-TO-FEATURE MAPPER (Dashboard)**

**Your Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/dashboard/presets
```

**AI Response (MUST BE EXACTLY THIS FORMAT):**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Manages pre-configured dashboard layouts and themes for different user types

📁 "Which MD file OWNS this FEATURE?"
→ **dashboard.md** (UI presets belong to dashboard system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **config.md** (preset storage), **docs.md** (usage guide), **testing.md** (preset switching tests)
```

### **Example 3: PATH-TO-FEATURE MAPPER (Backend)**

**Your Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/backend/engine/utils
```

**AI Response (MUST BE EXACTLY THIS FORMAT):**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Provides core execution utilities for math, timing, and retry logic

📁 "Which MD file OWNS this FEATURE?"
→ **backend.md** (engine utilities belong to backend system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **testing.md** (unit tests), **docs.md** (API reference), **config.md** (utility settings)
```

---

## 🔍 Feature-Based Thinking Guide

### **Instead of asking "Where does this folder go?"**
Ask: **"What does this FEATURE do for Windows users?"**

### **Instead of thinking about file paths**
Think: **"Which MD file should OWN this functionality?"**

### **Instead of complex integration**
Focus: **"Which MD files need to REFERENCE this feature?"**

### **Key Questions for Any Component:**
1. **Purpose**: What value does this provide to users?
2. **Owner**: Which MD file contains the main specification?
3. **References**: Which other MD files need integration notes?
4. **Implementation**: How does this work on Windows specifically?
5. **Testing**: How do we validate this feature works correctly?

---

## 📋 Quality Checklist

### **For PATH-TO-FEATURE MAPPER:**
- [ ] Input starts with "PATH-TO-FEATURE MAPPER"
- [ ] Response is EXACTLY 3 lines (no more, no less)
- [ ] No detailed specifications included
- [ ] Owner file is from the allowed list
- [ ] Reference files are from the allowed list

### **For Full Feature Mapping:**
- [ ] Component name is clear and descriptive
- [ ] Priority level matches business importance
- [ ] Windows implementation needs are specified
- [ ] Performance targets are measurable
- [ ] Security requirements are identified

---

## 🚀 Ready to Use!

**ALWAYS START WITH ACCESS VERIFICATION:**
```
ACCESS-PROOF WRITE repo=Apex-Arbitrage-Multichain-bot-for-windows branch=main nonce=<YOUR-RANDOM>
```

**For quick path mapping, use PATH-TO-FEATURE MAPPER mode:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: [your-folder-path]
```

**For detailed feature specification, use the full template above.**

**This approach transforms your complex 6,165-file system into manageable Windows desktop features, one path at a time!**