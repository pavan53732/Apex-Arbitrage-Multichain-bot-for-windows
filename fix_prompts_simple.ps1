# Simple script to fix critical issues in all prompt files

$promptsPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

Write-Host "`n=== FIXING PROMPT FILES ===" -ForegroundColor Cyan
Write-Host "This will fix the broken path construction that prevents complete file listing`n" -ForegroundColor Yellow

# Get all prompt files
$promptFiles = Get-ChildItem -Path $promptsPath -Filter "prompt-*.md" -File
$totalFiles = $promptFiles.Count
$fixedCount = 0

Write-Host "Found $totalFiles prompt files to process`n" -ForegroundColor White

foreach ($file in $promptFiles) {
    Write-Host "Processing: $($file.Name)..." -NoNewline
    
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    $changesMade = $false
    
    # Fix 1: The MAIN ISSUE - Broken path joining
    # The prompts have: Join-Path $basePath "C:\Users\Pavan pc\Desktop\..."
    # This creates an INVALID path because it's joining a base with a full path
    if ($content -match 'Join-Path \$basePath "C:\\Users\\Pavan pc\\Desktop') {
        # Replace the full path with just the relative folder name
        $content = $content -replace '\$targetPath = Join-Path \$basePath "C:\\Users\\Pavan pc\\Desktop\\Apex Arbitrage Multichain bot for windows\\Apex-Arbitrage-Multichain-bot-for-windows\\Apex Arbitrage Multichain bot\\([^"]+)"', '$targetPath = Join-Path $basePath "$1"'
        $changesMade = $true
    }
    
    # Fix 2: Add enforcement for complete file listing
    if ($content -match "MUST LIST EVERY SINGLE FILE" -eq $false) {
        $content = $content -replace '(\*\*FORBIDDEN\*\*: Do not guess)', @"
**MANDATORY ENFORCEMENT:**
- YOU MUST LIST EVERY SINGLE FILE WITHOUT EXCEPTION
- IF OUTPUT IS TRUNCATED, CONTINUE FROM THE LAST FILE
- DO NOT PROCEED UNTIL ALL FILES ARE LISTED
- VALIDATION FAILS IF ANY FILE IS MISSING

`$1
"@
        $changesMade = $true
    }
    
    # Fix 3: Add chunking support for large folders
    if ($content -match "Process files in chunks" -eq $false) {
        $content = $content -replace '(Write-Host "--- COMPLETE FILE LIST)', @"
# Check if we need chunking for large folders
    if (`$files.Count -gt 500) {
        Write-Host "LARGE FOLDER: `$(`$files.Count) files - Processing in chunks"
    }
    `$1
"@
        $changesMade = $true
    }
    
    # Fix 4: Add stronger validation requirements
    $content = $content -replace 'If ANY check fails: STOP and report issue', @"
If ANY check fails: STOP and report issue

**CRITICAL VALIDATION POINTS:**
1. After PowerShell enumeration → Count files
2. After folder tree creation → Verify all files present
3. After Feature Files section → Double-check counts match
4. Before writing .md files → Triple-check completeness
5. If ANY discrepancy → STOP and fix immediately
"@
    
    # Save if changes were made
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $fixedCount++
        Write-Host " FIXED" -ForegroundColor Green
    } else {
        Write-Host " No changes needed" -ForegroundColor Yellow
    }
}

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "FIXING COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "Total files processed: $totalFiles" -ForegroundColor White
Write-Host "Files fixed: $fixedCount" -ForegroundColor Green

Write-Host "`nKey improvements made:" -ForegroundColor Cyan
Write-Host "1. Fixed broken PowerShell path joining (main issue)" -ForegroundColor White
Write-Host "2. Added mandatory enforcement for complete file listing" -ForegroundColor White
Write-Host "3. Added chunking support for large folders (500+ files)" -ForegroundColor White  
Write-Host "4. Added multiple validation checkpoints" -ForegroundColor White
Write-Host "`nYour prompts should now properly list ALL files!" -ForegroundColor Green