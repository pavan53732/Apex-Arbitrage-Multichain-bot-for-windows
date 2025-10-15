# Insert blocking checkpoint between STEP 4 and STEP 5 in all prompt files
# Uses UTF-8 encoding without BOM to prevent corruption

$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

$checkpointText = @"

---

## 🚨 MANDATORY CHECKPOINT: NUMBERING FORMAT CONFIRMATION

**⚠️ STOP AND READ - DO NOT PROCEED TO STEP 5 WITHOUT COMPLETING THIS CHECKPOINT**

Before you write ANY folder tree structure in STEP 5, you MUST confirm you understand and will use the mandatory numbering format:

### REQUIRED FORMAT EXAMPLES:
``````
FOLDER 1/3: src/
FOLDER 2/3: tests/
FOLDER 3/3: docs/

FILE 1/5: src/index.js
FILE 2/5: src/config.js
FILE 3/5: tests/unit.test.js
FILE 4/5: tests/integration.test.js
FILE 5/5: docs/README.md
``````

### HIERARCHICAL NUMBERING RULES:
1. **Count ALL folders first** → Use "FOLDER X/Y:" where Y = total folder count
2. **Count ALL files across ALL folders** → Use "FILE X/Y:" where Y = total file count
3. **Number sequentially** → FOLDER 1, 2, 3... then FILE 1, 2, 3...
4. **Never restart numbering** → Files continue from where folders ended
5. **Always show totals** → X/Y format shows progress and validates completeness

### SELF-CHECK BEFORE PROCEEDING:
- [ ] I have counted the total number of folders in this feature
- [ ] I have counted the total number of files across all folders
- [ ] I understand FOLDER numbering: FOLDER 1/Y, FOLDER 2/Y, ... FOLDER Y/Y
- [ ] I understand FILE numbering: FILE 1/Z, FILE 2/Z, ... FILE Z/Z
- [ ] I will use this exact format in STEP 5 folder tree structure

**TYPE "CONFIRMED" BELOW TO PROCEED TO STEP 5:**

[Your confirmation here]

---

"@

Write-Host "Starting checkpoint insertion..." -ForegroundColor Cyan
Write-Host ""

$files = Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | Sort-Object Name
$successCount = 0
$errorCount = 0
$skippedCount = 0

foreach ($file in $files) {
    try {
        # Read with UTF-8 encoding
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        
        # Check if checkpoint already exists
        if ($content -match "MANDATORY CHECKPOINT: NUMBERING FORMAT CONFIRMATION") {
            Write-Host "⏭️  Skipped: $($file.Name) (checkpoint already exists)" -ForegroundColor Yellow
            $skippedCount++
            continue
        }
        
        # Find insertion point (before STEP 5)
        $step5Pattern = "### STEP 5: IMPLEMENTATION GUIDE"
        
        if ($content -match $step5Pattern) {
            # Insert checkpoint before STEP 5
            $newContent = $content -replace "($step5Pattern)", "$checkpointText`$1"
            
            # Write back with UTF-8 no BOM
            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            [System.IO.File]::WriteAllText($file.FullName, $newContent, $utf8NoBom)
            
            $successCount++
            Write-Host "✅ Modified: $($file.Name)" -ForegroundColor Green
        } else {
            Write-Host "⚠️  STEP 5 not found in: $($file.Name)" -ForegroundColor Yellow
            $errorCount++
        }
    } catch {
        Write-Host "❌ Error processing $($file.Name): $_" -ForegroundColor Red
        $errorCount++
    }
}

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "📊 CHECKPOINT INSERTION SUMMARY" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "✅ Successfully modified: $successCount files" -ForegroundColor Green
Write-Host "⏭️  Skipped (already exists): $skippedCount files" -ForegroundColor Yellow
Write-Host "❌ Errors: $errorCount files" -ForegroundColor Red
Write-Host "📁 Total files processed: $($files.Count)" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

if ($successCount -gt 0) {
    Write-Host "🎉 Checkpoint successfully inserted into $successCount prompt files!" -ForegroundColor Green
    Write-Host "✨ Encoding: UTF-8 without BOM (no corruption)" -ForegroundColor Green
}

if ($errorCount -gt 0) {
    Write-Host "⚠️  Warning: $errorCount files had errors. Please review." -ForegroundColor Yellow
}
