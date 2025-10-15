# Insert MANDATORY PRE-WRITE CHECKPOINT into all 842 prompts
# Preserves UTF-8 encoding without BOM

$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

$checkpoint = @'

## ⛔ MANDATORY PRE-WRITE CHECKPOINT ⛔

**STOP - DO NOT PROCEED TO WRITING FOLDER TREE UNTIL YOU CONFIRM:**

### 🔢 FOLDER TREE NUMBERING - MANDATORY FORMAT

**YOU MUST USE THIS EXACT FORMAT:**

```
FOLDER 1/3: backend/
  FOLDER 1/2: contracts/
    FILE 1/125: README.md
    FILE 2/125: GOVERNANCE.md
    FILE 3/125: SECURITY.md
  FOLDER 2/2: plugins/
    FILE 1/87: adapter-base.js
    FILE 2/87: adapter-factory.js
```

**CRITICAL RULES - ZERO TOLERANCE:**

1. ✅ **FOLDER X/Y:** prefix for ALL folders
   - X = position at THIS level (resets each level)
   - Y = total folders at THIS level
   - Example: FOLDER 1/3, FOLDER 2/3, FOLDER 3/3

2. ✅ **FILE X/Y:** prefix for ALL files
   - X = position in THIS folder
   - Y = total files in THIS folder
   - Example: FILE 1/125, FILE 2/125, ..., FILE 125/125

3. ✅ **Hierarchical numbering** - Each level RESETS
   - ✅ CORRECT: FOLDER 1/3 → FOLDER 1/2 (resets to 1)
   - ❌ WRONG: FOLDER 1/3 → FOLDER 4/5 (doesn't reset)

4. ✅ **List EVERY file** - NO EXCEPTIONS
   - If PowerShell found 125 files → List ALL 125 files
   - FORBIDDEN: "and more files", "etc.", "..."

5. ✅ **20-30 word description per file** - MANDATORY
   - Count words in each description
   - Must explain WHAT, WHY, HOW

**SELF-CHECK BEFORE PROCEEDING:**

- [ ] I will use "FOLDER X/Y:" prefix for every folder
- [ ] I will use "FILE X/Y:" prefix for every file
- [ ] I will reset numbering at each level
- [ ] I will list ALL files (no skipping)
- [ ] I will write 20-30 words per file

**IF YOU ANSWER NO TO ANY: STOP AND RE-READ REQUIREMENTS**

**ONLY AFTER CONFIRMING ALL 5 CHECKS: PROCEED TO WRITING FOLDER TREE**

---

'@

# Find insertion point (after "### STEP 4: MAP TO .MD FILES")
$searchPattern = "### STEP 4: MAP TO .MD FILES"
$nextLinePattern = "- Choose the single owner .md from:"

$processedCount = 0
$errorCount = 0

Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | ForEach-Object {
    $filePath = $_.FullName
    $promptNumber = $_.BaseName -replace 'prompt-', ''
    
    try {
        # Read file with UTF-8 encoding (no BOM)
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # Check if checkpoint already exists
        if ($content -match "MANDATORY PRE-WRITE CHECKPOINT") {
            Write-Host "SKIP: prompt-$promptNumber.md (checkpoint already exists)" -ForegroundColor Yellow
            return
        }
        
        # Find insertion point
        $step4Index = $content.IndexOf($searchPattern)
        if ($step4Index -eq -1) {
            Write-Host "ERROR: prompt-$promptNumber.md (STEP 4 not found)" -ForegroundColor Red
            $script:errorCount++
            return
        }
        
        # Find the end of STEP 4 section (next line after the bullet points)
        $nextLineIndex = $content.IndexOf($nextLinePattern, $step4Index)
        if ($nextLineIndex -eq -1) {
            Write-Host "ERROR: prompt-$promptNumber.md (insertion point not found)" -ForegroundColor Red
            $script:errorCount++
            return
        }
        
        # Find the end of the line containing "Choose 1-4 referencing .md files"
        $insertionPoint = $content.IndexOf("`n", $nextLineIndex + $nextLinePattern.Length)
        if ($insertionPoint -eq -1) {
            $insertionPoint = $content.Length
        }
        
        # Insert checkpoint
        $newContent = $content.Substring(0, $insertionPoint) + $checkpoint + $content.Substring($insertionPoint)
        
        # Write back with UTF-8 encoding (no BOM)
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        [System.IO.File]::WriteAllText($filePath, $newContent, $utf8NoBom)
        
        $script:processedCount++
        Write-Host "SUCCESS: prompt-$promptNumber.md" -ForegroundColor Green
        
    } catch {
        Write-Host "ERROR: prompt-$promptNumber.md - $($_.Exception.Message)" -ForegroundColor Red
        $script:errorCount++
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "SUMMARY:" -ForegroundColor Cyan
Write-Host "Processed: $processedCount files" -ForegroundColor Green
Write-Host "Errors: $errorCount files" -ForegroundColor $(if ($errorCount -eq 0) { "Green" } else { "Red" })
Write-Host "========================================" -ForegroundColor Cyan
