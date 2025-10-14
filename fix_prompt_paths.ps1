# Script to fix the broken PowerShell path construction in all prompt files

$promptsPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

Write-Host "`n🔧 FIXING PATH ISSUES IN ALL PROMPT FILES..." -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# Get all prompt files
$promptFiles = Get-ChildItem -Path $promptsPath -Filter "prompt-*.md" -File
$totalFiles = $promptFiles.Count
$fixedCount = 0

foreach ($file in $promptFiles) {
    Write-Progress -Activity "Fixing prompt files" -Status "Processing $($file.Name)" -PercentComplete (($fixedCount / $totalFiles) * 100)
    
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    
    # Fix 1: Broken PowerShell path construction
    # OLD: $targetPath = Join-Path $basePath "C:\Users\Pavan pc\Desktop\..."
    # This is WRONG because it's joining a base path with a FULL path
    
    # Find and replace the broken path pattern
    $oldPattern = '\$targetPath = Join-Path \$basePath "C:\\Users\\Pavan pc\\Desktop\\Apex Arbitrage Multichain bot for windows\\Apex-Arbitrage-Multichain-bot-for-windows\\Apex Arbitrage Multichain bot\\'
    if ($content -match $oldPattern) {
        $content = $content -replace ($oldPattern + '([^"]+)"'), '$targetPath = Join-Path $basePath "$1"'
    }
    
    # Fix 2: Add proper path validation
    $pathValidation = @'
Write-Host "Checking path: $targetPath"
    if ($targetPath -like "*\*\*") {
        # Fix double path issue
        $targetPath = $targetPath -replace ".*\\Apex Arbitrage Multichain bot\\", "$basePath\"
    }
'@
    $content = $content -replace 'Write-Host "Checking path: \$targetPath"', $pathValidation
    
    # Fix 3: Add file listing continuation enforcement
    $enforcementText = @'
Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"
    Write-Host "MANDATORY: ALL FILES MUST BE LISTED - NO EXCEPTIONS"
'@
    $content = $content -replace 'Write-Host "--- COMPLETE FILE LIST \(ALL \$\(\$files\.Count\) FILES\) ---"', $enforcementText
    
    # Fix 4: Add chunking for large file lists
    $chunkingCode = @'
# Process files in chunks if more than 500
    if ($files.Count -gt 500) {
        Write-Host "LARGE FOLDER DETECTED: Processing in chunks of 500 files"
        $chunkSize = 500
        $totalChunks = [Math]::Ceiling($files.Count / $chunkSize)
        
        for ($chunk = 0; $chunk -lt $totalChunks; $chunk++) {
            $startIdx = $chunk * $chunkSize
            $endIdx = [Math]::Min($startIdx + $chunkSize, $files.Count)
            Write-Host "`nCHUNK $($chunk + 1) OF $totalChunks (Files $($startIdx + 1) to $endIdx):"
            
            $files[$startIdx..($endIdx - 1)] | Sort-Object FullName | ForEach-Object {
                Write-Host "FILE $($startIdx + $files.IndexOf($_) + 1)/$($files.Count): $($_.FullName)"
            }
        }
    } else {
        $files | Sort-Object FullName | ForEach-Object {
'@
    $content = $content -replace '\$files \| Sort-Object FullName \| ForEach-Object \{', $chunkingCode
    
    # Fix 5: Close the else block properly
    $closeBlock = @'
$fileIndex++
        }
    }
    Write-Host "--- END OF COMPLETE LIST ---"
'@
    $content = $content -replace '\$fileIndex\+\+\s*\}\s*Write-Host "--- END OF COMPLETE LIST ---"', $closeBlock
    
    # Fix 6: Add completion enforcement messages
    $enforcementMsg = @'
**🚨 CRITICAL ENFORCEMENT 🚨**
- YOU MUST LIST EVERY SINGLE FILE - NO EXCEPTIONS
- IF INTERRUPTED, YOU MUST CONTINUE FROM WHERE YOU STOPPED
- DO NOT PROCEED UNTIL ALL FILES ARE DOCUMENTED
- VALIDATION WILL FAIL IF ANY FILE IS MISSING

**VALIDATION REQUIRED:
'@
    $content = $content -replace '\*\*VALIDATION REQUIRED:', $enforcementMsg
    
    # Fix 7: Add stronger language for file listing requirements
    $strongerLang = 'list EVERY filename explicitly
- **CONTINUATION REQUIRED**: If output is truncated, IMMEDIATELY continue listing from the last file
- **NO COMPLETION WITHOUT FULL LISTING**: Do not move to next step until ALL files are documented
- **CHUNK MARKERS**: For folders with 500+ files, use "CHUNK X OF Y" markers'
    $content = $content -replace 'list EVERY filename explicitly', $strongerLang
    
    # Fix 8: Add validation loop requirements
    $validationLoop = @'
**If ANY element is missing, your output is INCOMPLETE and MUST be revised.**

**🔄 CONTINUOUS VALIDATION LOOP:**
- After every 100 files listed → Verify count matches PowerShell
- At each folder boundary → Confirm all files in folder are listed
- Before writing .md files → Triple-check ALL files are documented
- If ANY file is missing → STOP and add missing files IMMEDIATELY
'@
    $content = $content -replace '\*\*If ANY element is missing, your output is INCOMPLETE and MUST be revised\.\*\*', $validationLoop
    
    # Check if content was modified
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $fixedCount++
        Write-Host "✅ Fixed: $($file.Name)" -ForegroundColor Green
    } else {
        Write-Host "⏭️ No changes needed: $($file.Name)" -ForegroundColor Yellow
    }
}

Write-Progress -Activity "Fixing prompt files" -Completed

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "PATH FIXING COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "Total files processed: $totalFiles" -ForegroundColor White
Write-Host "Files fixed: $fixedCount" -ForegroundColor Green
Write-Host "`nKey improvements made:" -ForegroundColor Cyan
Write-Host "1. ✅ Fixed broken PowerShell path construction" -ForegroundColor White
Write-Host "2. ✅ Added chunking for large file lists (500+ files)" -ForegroundColor White
Write-Host "3. ✅ Added continuation enforcement for interrupted listings" -ForegroundColor White
Write-Host "4. ✅ Added validation loops at multiple checkpoints" -ForegroundColor White
Write-Host "5. ✅ Enhanced completion requirements with stronger language" -ForegroundColor White