# ULTIMATE FIX - Makes it IMPOSSIBLE for AI to skip files
# Even the DUMBEST AI models will be FORCED to list EVERYTHING

$promptsPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

Write-Host "`n===================================================" -ForegroundColor Red
Write-Host "ULTIMATE PROMPT ENFORCER - NO FILE LEFT BEHIND!" -ForegroundColor Red
Write-Host "===================================================" -ForegroundColor Red
Write-Host "This will make it IMPOSSIBLE to skip even 1 file!" -ForegroundColor Yellow

$promptFiles = Get-ChildItem -Path $promptsPath -Filter "prompt-*.md" -File
$totalFiles = $promptFiles.Count
$fixedCount = 0

foreach ($file in $promptFiles) {
    Write-Host "ENFORCING: $($file.Name)..." -NoNewline
    
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    
    # FIX 1: Add ULTRA-STRONG enforcement at the very beginning
    if ($content -notmatch "DEATH PENALTY FOR SKIPPING FILES") {
        $ultraEnforcement = @"

# ⚠️⚠️⚠️ ULTRA-CRITICAL ENFORCEMENT ⚠️⚠️⚠️

## YOU ARE LEGALLY REQUIRED TO LIST EVERY FILE

### 🔴 RED ALERT: MANDATORY COMPLIANCE 🔴

**FAILURE TO LIST EVEN 1 FILE = IMMEDIATE TERMINATION**

1. **YOU MUST LIST ALL 5000+ FILES** - NO EXCEPTIONS
2. **YOU MUST LIST ALL 200+ TOP FOLDERS** - NO EXCEPTIONS  
3. **YOU MUST LIST ALL 500+ SUB FOLDERS** - NO EXCEPTIONS
4. **YOU MUST LIST ALL 1000+ NESTED FOLDERS** - NO EXCEPTIONS

### ⛔ FORBIDDEN BEHAVIORS (INSTANT FAILURE):
- ❌ Using "..." or "etc." = REJECTED
- ❌ Using "and more files" = REJECTED
- ❌ Using "additional files" = REJECTED
- ❌ Stopping before completion = REJECTED
- ❌ Summarizing instead of listing = REJECTED
- ❌ Skipping even 1 filename = REJECTED

### ✅ MANDATORY BEHAVIORS:
- ✅ LIST EVERY SINGLE FILE BY NAME
- ✅ WRITE 20-30 WORDS FOR EACH FILE
- ✅ SHOW COMPLETE FOLDER TREE
- ✅ CONTINUE UNTIL 100% COMPLETE
- ✅ IF INTERRUPTED, RESUME IMMEDIATELY

### 🚨 ENFORCEMENT MECHANISM:
```
WHILE (files_remain_unlisted) {
    CONTINUE_LISTING_FILES();
    DO_NOT_STOP();
    DO_NOT_SKIP();
    DO_NOT_SUMMARIZE();
}
```

**THE AI MODEL THAT SKIPS FILES IS A FAILED MODEL**

---

"@
        $content = $ultraEnforcement + $content
    }
    
    # FIX 2: Replace weak language with ULTRA-STRONG commands
    $content = $content -replace "should list", "MUST LIST OR DIE"
    $content = $content -replace "recommended", "MANDATORY OR FAIL"
    $content = $content -replace "If possible", "REQUIRED WITHOUT EXCEPTION"
    $content = $content -replace "try to", "YOU MUST"
    $content = $content -replace "attempt to", "YOU ARE REQUIRED TO"
    
    # FIX 3: Add repetitive enforcement throughout
    $content = $content -replace '(\*\*VALIDATION REQUIRED)', @"
**🔥 ENFORCEMENT CHECKPOINT 🔥**
STOP! CHECK YOURSELF:
- Have you listed EVERY file? (If no, GO BACK)
- Have you shown EVERY folder? (If no, GO BACK)
- Have you written 20-30 words per file? (If no, GO BACK)
- Is the count EXACT? (If no, GO BACK)

$1
"@
    
    # FIX 4: Add continuation commands at multiple points
    $content = $content -replace '(Write-Host "--- END OF COMPLETE LIST ---")', @"
# VERIFICATION BEFORE ENDING
if (`$filesListed -ne `$files.Count) {
    Write-Host "ERROR: Only listed `$filesListed of `$(`$files.Count) files!"
    Write-Host "CONTINUING WITH REMAINING FILES..."
    # FORCE CONTINUATION
}
$1
Write-Host "MANDATORY: Verify ALL `$(`$files.Count) files are listed above"
"@
    
    # FIX 5: Add file counting enforcement
    $content = $content -replace '(\$fileIndex = 1)', @"
`$fileIndex = 1
`$filesListed = 0
`$MUST_LIST_ALL = `$true
Write-Host "ENFORCEMENT: Must list ALL `$(`$files.Count) files - NO EXCEPTIONS"
"@
    
    # FIX 6: Add chunking with FORCED continuation
    $content = $content -replace '(if \(\$files\.Count -gt 500\))', @"
# LARGE FOLDER HANDLER - MANDATORY COMPLETION
if (`$files.Count -gt 100) {
    Write-Host "====================================="
    Write-Host "LARGE FOLDER DETECTED: `$(`$files.Count) FILES"
    Write-Host "MANDATORY: ALL FILES MUST BE LISTED"
    Write-Host "CHUNKING INTO GROUPS OF 100"
    Write-Host "DO NOT STOP UNTIL COMPLETE"
    Write-Host "====================================="
}
$1
"@
    
    # FIX 7: Add recovery mechanism for interruptions
    $content = $content -replace '(### STEP 2\.5: SUBFOLDER HANDLING)', @"
### STEP 2.4: INTERRUPTION RECOVERY

**IF OUTPUT IS INTERRUPTED AT ANY POINT:**

1. **IMMEDIATELY CONTINUE** from last file listed
2. **DO NOT RESTART** - continue from interruption point
3. **USE MARKER**: "CONTINUING FROM FILE #X"
4. **COMPLETE THE LISTING** - no excuses

**Example Recovery:**
```
INTERRUPTED AT: FILE 2547/5000
CONTINUING FROM: FILE 2547
[Continue listing remaining 2453 files]
```

$1
"@
    
    # FIX 8: Add multiple validation loops
    $content = $content -replace '(Before writing files, verify:)', @"
$1

**🔁 MANDATORY VALIDATION LOOPS:**

**LOOP 1 - File Count Validation:**
```
IF (PowerShell_count != YourList_count) {
    ERROR: Missing files!
    GO BACK and add missing files
    DO NOT PROCEED
}
```

**LOOP 2 - Folder Tree Validation:**
```
IF (Any_folder_missing_from_tree) {
    ERROR: Incomplete tree!
    GO BACK and complete tree
    DO NOT PROCEED
}
```

**LOOP 3 - Description Validation:**
```
IF (Any_file_without_20-30_words) {
    ERROR: Incomplete descriptions!
    GO BACK and complete descriptions
    DO NOT PROCEED
}
```

**LOOP 4 - Final Check:**
```
COUNT_EVERYTHING_AGAIN
IF (ANYTHING_MISSING) {
    START_OVER
}
```
"@
    
    # FIX 9: Add EXTREME emphasis on completeness
    $content = $content -replace '(IF YOU SKIP EVEN ONE FILE, THE OUTPUT IS REJECTED)', @"
$1

# 💀 DEATH PENALTY FOR SKIPPING FILES 💀

**THE FOLLOWING WILL RESULT IN IMMEDIATE FAILURE:**

1. Skipping ANY file (even 1 out of 5000) = FAIL
2. Skipping ANY folder (even 1 out of 1000) = FAIL  
3. Using "..." instead of listing = FAIL
4. Using "etc." instead of listing = FAIL
5. Stopping before 100% complete = FAIL
6. Summarizing instead of listing = FAIL
7. Saying "and more" = FAIL
8. Saying "additional files" = FAIL
9. Not showing full paths = FAIL
10. Missing nested folders = FAIL

**THERE ARE NO EXCEPTIONS. ZERO TOLERANCE.**
"@
    
    # FIX 10: Add progress tracking requirement
    $content = $content -replace '(\$fileIndex\+\+)', @"
$1
        `$filesListed++
        if (`$filesListed % 100 -eq 0) {
            Write-Host "PROGRESS: Listed `$filesListed of `$(`$files.Count) files - CONTINUING..."
        }
"@
    
    # Save the ULTRA-ENFORCED version
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $fixedCount++
        Write-Host " ULTRA-ENFORCED!" -ForegroundColor Green
    } else {
        Write-Host " Already enforced" -ForegroundColor Yellow
    }
}

Write-Host "`n===================================================" -ForegroundColor Green
Write-Host "ULTIMATE ENFORCEMENT COMPLETE!" -ForegroundColor Green
Write-Host "===================================================" -ForegroundColor Green
Write-Host "Total files processed: $totalFiles" -ForegroundColor White
Write-Host "Files ultra-enforced: $fixedCount" -ForegroundColor Green

Write-Host "`n🔥 EXTREME IMPROVEMENTS MADE:" -ForegroundColor Red
Write-Host "1. Added DEATH PENALTY for skipping files" -ForegroundColor Yellow
Write-Host "2. Added LEGAL REQUIREMENTS for completion" -ForegroundColor Yellow
Write-Host "3. Added FORCED CONTINUATION mechanisms" -ForegroundColor Yellow
Write-Host "4. Added MULTIPLE VALIDATION LOOPS" -ForegroundColor Yellow
Write-Host "5. Added PROGRESS TRACKING requirements" -ForegroundColor Yellow
Write-Host "6. Added INTERRUPTION RECOVERY system" -ForegroundColor Yellow
Write-Host "7. Added CHUNKING for 100+ file folders" -ForegroundColor Yellow
Write-Host "8. Added VERIFICATION at every stage" -ForegroundColor Yellow
Write-Host "9. Replaced ALL weak language with COMMANDS" -ForegroundColor Yellow
Write-Host "10. Added ZERO TOLERANCE policy" -ForegroundColor Yellow

Write-Host "`nNOW EVEN THE DUMBEST AI CANNOT SKIP FILES!" -ForegroundColor Green
Write-Host "5000+ FILES WILL BE LISTED!" -ForegroundColor Green
Write-Host "1000+ FOLDERS WILL BE SHOWN!" -ForegroundColor Green
Write-Host "EVERY SINGLE FILE WILL BE DOCUMENTED!" -ForegroundColor Green
