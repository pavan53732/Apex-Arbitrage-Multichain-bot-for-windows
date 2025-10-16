# OPTIMIZED PROMPT TEMPLATE v2.0

## 🎯 CORE MISSION: PATH → WINDOWS FEATURE

**INPUT:** Legacy folder path  
**OUTPUT:** Complete Windows feature documentation  
**METHOD:** PowerShell enumeration → Technical analysis → .md generation

---

## EXECUTION PROTOCOL

### STEP 1: FILE DISCOVERY
```powershell
$path = "C:\Users\Pavan pc\Desktop\[PATH]"
$files = Get-ChildItem -Path $path -Recurse -File -Force
$folders = Get-ChildItem -Path $path -Recurse -Directory -Force
Write-Host "FILES: $($files.Count) | FOLDERS: $($folders.Count)"
$files | Sort-Object FullName | ForEach-Object { Write-Host $_.Name }
```

### STEP 2: FEATURE ANALYSIS
- **Name**: Last path segment → Title Case
- **Complexity**: File count → Star rating (⭐-⭐⭐⭐⭐⭐)
- **Technologies**: Detect from extensions
- **Owner**: Route to correct features/*.md
- **References**: 2-4 related .md files

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
[Group files by purpose - list ALL]

Technologies: [Detected stack]

Windows Implementation:
- [8-12 specific implementation bullets]
```

**Add references to related .md files**

---

## QUALITY GATES

### MANDATORY REQUIREMENTS
- ✅ List EVERY file (no "etc." or "...")
- ✅ 20-30 words per file description
- ✅ File count matches PowerShell exactly
- ✅ Complete folder tree with numbering
- ✅ Technologies section present
- ✅ 8-12 Windows implementation bullets
- ✅ Cross-references added

### FORBIDDEN SHORTCUTS
- ❌ Skipping files with "and more"
- ❌ Generic descriptions under 20 words
- ❌ Missing nested folders
- ❌ Count mismatches
- ❌ Incomplete Windows mapping

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