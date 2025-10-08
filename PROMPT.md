# APEX WINDOWS FEATURE-MAPPING PROMPT (AI-OPTIMIZED)

**Transform ANY legacy component into clear Windows feature specifications**

---

## 🎯 Purpose
Convert legacy components from your 6,165-file system into **Windows-first feature specifications** that clearly show:
- **"What does this FEATURE do?"** → Clear feature description
- **"Which MD file OWNS this FEATURE?"** → Primary specification file  
- **"Which MD files REFERENCE this FEATURE?"** → Integration points

## 📝 How to Use This Prompt
1. **Copy the entire "YOUR INPUT" template** below
2. **Fill in your component details** 
3. **Submit to AI** 
4. **Receive clear guidance** on exactly which MD files to update

---

# 🗂️ PATH-TO-FEATURE MAPPER MODE (NEW - SIMPLE 3-LINE MAPPING)

## Quick Path Mapping
**Just paste any legacy folder path and get instant feature mapping:**

### Input Format:
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/backend/engine/utils/
```

### Expected Output:
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Provides core execution utilities (math, serialization, retry helpers, timing functions) for the arbitrage engine

📁 "Which MD file OWNS this FEATURE?"
→ **backend.md** (engine internals and shared utilities belong to backend runtime)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **testing.md** (unit + performance test coverage), **docs.md** (developer API documentation), **config.md** (tunable retry/backoff settings), **security.md** (prevent secret leakage in logs)
```

## Path Mapping Rules
- **backend/engine/** → backend.md
- **backend/plugins/** → backend.md  
- **dashboard/** → dashboard.md
- **ai-modules/** → ai-modules.md
- **config/** → config.md
- **contracts/** → contracts.md
- **security/** → security.md
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

## 🎯 Expected AI Response Format

### **Feature Classification**
```
✅ FEATURE ANALYSIS COMPLETE

🔍 "What does this FEATURE do?"
→ [Clear, actionable description of the feature's purpose]

📁 "Which MD file OWNS this FEATURE?"
→ **[filename].md** - [Reason why this file is the primary owner]

🔗 "Which MD files REFERENCE this FEATURE?"
→ **[filename1].md** - [What integration notes to add]
→ **[filename2].md** - [What integration notes to add]
→ **[filename3].md** - [What integration notes to add]
```

### **Detailed Specifications**
```markdown
## PRIMARY SPECIFICATION (Paste into [owner-file].md)

### Feature Name: [Clear Feature Name]
- **Purpose**: [What this feature accomplishes for Windows users]
- **Windows Implementation**: 
  - [How this works on Windows desktop]
  - [Technologies and services used]
- **Key Functions**:
  - [Function 1]: [Description]
  - [Function 2]: [Description]
  - [Function 3]: [Description]
- **Performance Targets**: [Measurable goals]
- **Acceptance Criteria**:
  - [ ] [Testable requirement 1]
  - [ ] [Testable requirement 2]
  - [ ] [Testable requirement 3]

## INTEGRATION NOTES (Add to referenced MD files)

### [filename1].md Integration
- **Connection Point**: [How this file connects to the feature]
- **Required Changes**: [What to add to this file]
- **Dependencies**: [What this file needs from the feature]

### [filename2].md Integration
- **Connection Point**: [How this file connects to the feature]
- **Required Changes**: [What to add to this file]
- **Dependencies**: [What this file needs from the feature]
```

---

## 💡 Worked Examples

### **Example 1: Path Mapper Usage**

**Your Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/dashboard/widgets/real-time-monitor/
```

**AI Response:**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Provides real-time monitoring widgets for arbitrage execution status and metrics

📁 "Which MD file OWNS this FEATURE?"
→ **dashboard.md** (UI widgets and real-time displays belong to dashboard system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **backend.md** (data APIs for real-time feeds), **config.md** (widget refresh rates and display settings), **testing.md** (UI automation tests), **docs.md** (widget usage guide)
```

### **Example 2: Complex Backend Path**

**Your Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/backend/plugins/dex-adapters/uniswap-v3/
```

**AI Response:**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Provides Uniswap V3 DEX integration for quote fetching and trade execution

📁 "Which MD file OWNS this FEATURE?"
→ **backend.md** (DEX adapters are core backend execution components)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **config.md** (Uniswap RPC settings and pool configurations), **contracts.md** (Uniswap V3 contract interfaces), **testing.md** (fork testing and integration tests), **security.md** (API key management), **docs.md** (DEX setup guide)
```

### **Example 3: AI Module Path**

**Your Input:**
```
PATH-TO-FEATURE MAPPER

Legacy Path: Apex Arbitrage Multichain bot/ai-modules/models/opportunity-scorer/
```

**AI Response:**
```
✅ PATH-TO-FEATURE MAPPING COMPLETE

🔍 "What does this FEATURE do?"
→ Uses machine learning to score and rank arbitrage opportunities by profitability and risk

📁 "Which MD file OWNS this FEATURE?"
→ **ai-modules.md** (ML models and scoring algorithms belong to AI system)

🔗 "Which MD files REFERENCE this FEATURE?"
→ **backend.md** (opportunity data flow and scoring API integration), **dashboard.md** (opportunity ranking display), **config.md** (model parameters and thresholds), **testing.md** (model accuracy validation), **docs.md** (AI system explanation)
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

### **Before Submitting Your Request:**
- [ ] Component name is clear and descriptive
- [ ] Priority level matches business importance
- [ ] Windows implementation needs are specified
- [ ] Performance targets are measurable
- [ ] Security requirements are identified

### **Expected in AI Response:**
- [ ] Clear "What does this FEATURE do?" answer
- [ ] Single MD file identified as primary owner
- [ ] List of MD files needing integration notes
- [ ] Paste-ready specifications for each file
- [ ] Windows-specific implementation details

---

## 🚀 Ready to Use!

**Now you can simply paste ANY legacy folder path and get instant feature mapping guidance!**

**Examples of paths you can use:**
- `Apex Arbitrage Multichain bot/backend/engine/data/batch-logs/`
- `Apex Arbitrage Multichain bot/dashboard/overlays/ar-vr/`
- `Apex Arbitrage Multichain bot/ai-modules/inference/real-time/`
- `Apex Arbitrage Multichain bot/contracts/governance/voting/`

**This approach transforms your complex 6,165-file system into manageable Windows desktop features, one path at a time!**