# APEX WINDOWS FEATURE MAPPING PROMPT

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

# 🔄 FEATURE MAPPING REQUEST TEMPLATE

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

### **Example 1: Batch Logging System**

**Your Input:**
```
APEX WINDOWS FEATURE MAPPING REQUEST

=== COMPONENT ANALYSIS ===
Component Name: Execution Batch Logging
Component Type: Feature
Original Purpose: Track arbitrage execution batches with performance metrics
Priority Level: P0-Critical

=== WINDOWS IMPLEMENTATION ===
Runtime Needs: Node.js Service
Data Storage: SQLite Database + File Logs
User Interface: Dashboard Widget
Security Requirements: Log Redaction
Performance Target: Log 2000 events/second, query response < 50ms
```

**AI Response:**
```
✅ FEATURE ANALYSIS COMPLETE

🔍 "What does this FEATURE do?"
→ Tracks arbitrage execution batches with real-time logging and performance metrics

📁 "Which MD file OWNS this FEATURE?"
→ **backend.md** - Core execution logging belongs in the backend engine

🔗 "Which MD files REFERENCE this FEATURE?"
→ **dashboard.md** - Real-time log viewer widget and export controls
→ **config.md** - Log retention settings and file rotation policies
→ **security.md** - Log redaction rules for sensitive data
→ **testing.md** - Performance testing for 2k events/second
→ **docs.md** - Operator guide for log analysis and troubleshooting
```

### **Example 2: Windows Installer**

**Your Input:**
```
APEX WINDOWS FEATURE MAPPING REQUEST

=== COMPONENT ANALYSIS ===
Component Name: One-Click Installer
Component Type: Feature
Original Purpose: Install application with all dependencies automatically
Priority Level: P0-Critical

=== WINDOWS IMPLEMENTATION ===
Runtime Needs: NSIS/Inno Setup
Data Storage: Registry + %AppData%
User Interface: Installation Wizard
Security Requirements: Code Signing
Performance Target: Complete installation in under 3 minutes
```

**AI Response:**
```
✅ FEATURE ANALYSIS COMPLETE

🔍 "What does this FEATURE do?"
→ Provides one-click Windows installation with automatic dependency management

📁 "Which MD file OWNS this FEATURE?"
→ **install-dependencies.md** - Primary installer specification and requirements

🔗 "Which MD files REFERENCE this FEATURE?"
→ **deployment.md** - Packaging pipeline and distribution strategy
→ **security.md** - Code signing certificates and validation
→ **config.md** - Default configuration setup during installation
→ **testing.md** - Silent installation testing and validation
→ **docs.md** - Installation guide for end users
```

### **Example 3: AI Decision Engine**

**Your Input:**
```
APEX WINDOWS FEATURE MAPPING REQUEST

=== COMPONENT ANALYSIS ===
Component Name: Opportunity Detection AI
Component Type: Subsystem
Original Purpose: ML-based arbitrage opportunity identification
Priority Level: P1-High

=== WINDOWS IMPLEMENTATION ===
Runtime Needs: Python Scripts + Node.js Bridge
Data Storage: SQLite Database + Model Files
User Interface: Dashboard Analytics Panel
Security Requirements: Model Protection
Performance Target: Scan opportunities in under 2 seconds
```

**AI Response:**
```
✅ FEATURE ANALYSIS COMPLETE

🔍 "What does this FEATURE do?"
→ Uses machine learning to identify profitable arbitrage opportunities in real-time

📁 "Which MD file OWNS this FEATURE?"
→ **ai-modules.md** - Primary AI/ML system specification and model management

🔗 "Which MD files REFERENCE this FEATURE?"
→ **backend.md** - AI integration points and opportunity data flow
→ **dashboard.md** - AI insights panel and opportunity visualization
→ **config.md** - AI model settings and performance tuning
→ **testing.md** - Model accuracy testing and performance validation
→ **docs.md** - AI system explanation for operators
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

**Copy the "YOUR INPUT" template above, fill in your component details, and submit to any AI assistant. You'll receive clear guidance on exactly which MD files to update with paste-ready specifications.**

**This approach transforms your complex 6,165-file system into manageable Windows desktop features, one component at a time!**