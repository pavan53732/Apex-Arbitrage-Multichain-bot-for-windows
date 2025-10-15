# Add MANDATORY FORMAT CONFIRMATION checkpoint before STEP 5
# UTF-8 encoding without BOM

$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

$checkpoint = @'

## ⛔ STOP - MANDATORY FORMAT CONFIRMATION ⛔

**BEFORE YOU WRITE FOLDER TREE, YOU MUST CONFIRM:**

**REQUIRED FORMAT:**

✅ **FOLDER X/Y: foldername/** where X = current position at this level, Y = total folders at this level
✅ **FILE X/Y: filename.ext** where X = current position in folder, Y = total files in folder
✅ **Hierarchical numbering** - Each level RESETS (FOLDER 1/3 → FOLDER 1/2, NOT FOLDER 1/3 → FOLDER 4/5)
✅ **List EVERY file** with 20-30 word description
✅ **NO shortcuts** - FORBIDDEN: "and more files", "etc.", "..."

**EXAMPLE:**
```
FOLDER 1/3: backend/
  FOLDER 1/2: contracts/
    FILE 1/125: README.md
    FILE 2/125: GOVERNANCE.md
  FOLDER 2/2: plugins/
    FILE 1/87: adapter-base.js
```

**SELF-CHECK:**
- [ ] I will use FOLDER X/Y: prefix for every folder
- [ ] I will use FILE X/Y: prefix for every file
- [ ] I will reset numbering at each level
- [ ] I will list ALL files with 20-30 word descriptions
- [ ] I will NOT use "and more files" or "etc."

**ONLY AFTER CONFIRMING ALL 5 CHECKS: PROCEED TO STEP 5**

---

'@

$searchPattern = "### STEP 4: MAP TO .MD FILES"
$insertAfterPattern = "- Choose 1-4 referencing .md files based on real integration needs"

$processedCount = 0
$errorCount = 0
$skippedCount = 0

Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | ForEach-Object {
    $filePath = $_.FullName
    $promptNumber = $_.BaseName -replace 'prompt-', ''
    
    try {
        # Read with UTF-8 no BOM
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.UTF8Encoding]::new($false))
        
        # Check if checkpoint already exists
        if ($content -match "STOP - MANDATORY FORMAT CONFIRMATION") {
            Write-Host "SKIP: prompt-$promptNumber.md (checkpoint exists)" -ForegroundColor Yellow
            $script:skippedCount++
            return
        }
        
        # Find STEP 4
        $step4Index = $content.IndexOf($searchPattern)
        if ($step4Index -eq -1) {
            Write-Host "ERROR: prompt-$promptNumber.md (STEP 4 not found)" -ForegroundColor Red
            $script:errorCount++
            return
        }
        
        # Find insertion point after "Choose 1-4 referencing"
        $insertIndex = $content.IndexOf($insertAfterPattern, $step4Index)
        if ($insertIndex -eq -1) {
            Write-Host "ERROR: prompt-$promptNumber.md (insertion point not found)" -ForegroundColor Red
            $script:errorCount++
            return
        }
        
        # Find end of that line
        $lineEnd = $content.IndexOf("`n", $insertIndex)
        if ($lineEnd -eq -1) { $lineEnd = $content.Length }
        
        # Insert checkpoint
        $newContent = $content.Substring(0, $lineEnd) + $checkpoint + $content.Substring($lineEnd)
        
        # Write with UTF-8 no BOM
        [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.UTF8Encoding]::new($false))
        
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
Write-Host "Skipped: $skippedCount files" -ForegroundColor Yellow
Write-Host "Errors: $errorCount files" -ForegroundColor $(if ($errorCount -eq 0) { "Green" } else { "Red" })
Write-Host "========================================" -ForegroundColor Cyan
