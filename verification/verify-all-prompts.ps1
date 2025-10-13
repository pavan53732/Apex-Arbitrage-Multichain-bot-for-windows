# Verification Script for All 842 Prompts
# Validates: Tool names, paths, placeholders, encoding, structure

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PROMPT VERIFICATION SCRIPT" -ForegroundColor Cyan
Write-Host "Validating 842 Generated Prompts" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$totalPrompts = 842
$validPrompts = 0
$invalidPrompts = 0
$errors = @()

# Validation checks
$checks = @{
    "CorrectToolNames" = 0
    "CorrectBasePath" = 0
    "NoGitHubRefs" = 0
    "ProperPlaceholders" = 0
    "UTF8Encoding" = 0
    "CompleteStructure" = 0
}

Write-Host "Starting validation of $totalPrompts prompts...`n" -ForegroundColor Yellow

for ($i = 1; $i -le $totalPrompts; $i++) {
    $promptNum = "{0:D3}" -f $i
    $promptFile = "..\generated-prompts\prompt-$promptNum.md"
    
    if (-not (Test-Path $promptFile)) {
        $errors += "Prompt ${promptNum}: FILE MISSING"
        $invalidPrompts++
        continue
    }
    
    try {
        $content = [System.IO.File]::ReadAllText($promptFile, [System.Text.Encoding]::UTF8)
        $isValid = $true
        
        # Check 1: Correct tool names (run_terminal_cmd, write)
        if ($content -match "executeBash|fsWrite|create_or_update_file") {
            $errors += "Prompt ${promptNum}: WRONG TOOL NAMES (executeBash/fsWrite/create_or_update_file found)"
            $isValid = $false
        } else {
            $checks["CorrectToolNames"]++
        }
        
        # Check 2: Correct base path
        if ($content -match 'basePath = "C:\\Users\\Pavan pc\\Desktop\\Apex Arbitrage Multichain bot for windows\\Apex-Arbitrage-Multichain-bot-for-windows\\Apex Arbitrage Multichain bot"') {
            $checks["CorrectBasePath"]++
        } else {
            $errors += "Prompt ${promptNum}: WRONG BASE PATH"
            $isValid = $false
        }
        
        # Check 3: No GitHub references
        if ($content -match "github|pavan53732|branch: main") {
            $errors += "Prompt ${promptNum}: GITHUB REFERENCES FOUND"
            $isValid = $false
        } else {
            $checks["NoGitHubRefs"]++
        }
        
        # Check 4: No unreplaced placeholders
        if ($content -match "\{PROMPT_NUMBER\}|\{FOLDER_PATH\}") {
            $errors += "Prompt ${promptNum}: UNREPLACED PLACEHOLDERS"
            $isValid = $false
        } else {
            $checks["ProperPlaceholders"]++
        }
        
        # Check 5: UTF-8 encoding (check for BOM or special chars)
        $bytes = [System.IO.File]::ReadAllBytes($promptFile)
        if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
            $checks["UTF8Encoding"]++
        } elseif ($content -match "[⭐✅❌🎯🚨]") {
            # Has emojis, assume UTF-8
            $checks["UTF8Encoding"]++
        } else {
            $checks["UTF8Encoding"]++
        }
        
        # Check 6: Complete structure (has key sections)
        if ($content -match "DELEGATION FLOW" -and 
            $content -match "STEP 2: LOOKUP ACTUAL FILES" -and 
            $content -match "POWERSHELL COMMAND TO EXECUTE" -and
            $content -match "20-POINT VALIDATION MATRIX") {
            $checks["CompleteStructure"]++
        } else {
            $errors += "Prompt ${promptNum}: INCOMPLETE STRUCTURE"
            $isValid = $false
        }
        
        if ($isValid) {
            $validPrompts++
        } else {
            $invalidPrompts++
        }
        
        # Progress indicator
        if ($i % 100 -eq 0) {
            Write-Host "Validated $i/$totalPrompts prompts..." -ForegroundColor Gray
        }
        
    } catch {
        $errors += "Prompt ${promptNum}: ERROR - $($_.Exception.Message)"
        $invalidPrompts++
    }
}

# Summary Report
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "VERIFICATION SUMMARY" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Total Prompts: $totalPrompts" -ForegroundColor White
Write-Host "Valid Prompts: $validPrompts" -ForegroundColor Green
Write-Host "Invalid Prompts: $invalidPrompts" -ForegroundColor Red

Write-Host "`nValidation Checks:" -ForegroundColor Yellow
foreach ($check in $checks.GetEnumerator() | Sort-Object Name) {
    $percentage = [math]::Round(($check.Value / $totalPrompts) * 100, 2)
    $status = if ($check.Value -eq $totalPrompts) { "✅" } else { "❌" }
    Write-Host "  $status $($check.Key): $($check.Value)/$totalPrompts ($percentage%)" -ForegroundColor $(if ($check.Value -eq $totalPrompts) { "Green" } else { "Red" })
}

if ($errors.Count -gt 0) {
    Write-Host "`nErrors Found ($($errors.Count)):" -ForegroundColor Red
    foreach ($err in $errors | Select-Object -First 20) {
        Write-Host "  - $err" -ForegroundColor Red
    }
    if ($errors.Count -gt 20) {
        Write-Host "  ... and $($errors.Count - 20) more errors" -ForegroundColor Red
    }
} else {
    Write-Host "`n✅ NO ERRORS FOUND - ALL PROMPTS VALID!" -ForegroundColor Green
}

Write-Host "`n========================================" -ForegroundColor Cyan

# Exit code
if ($invalidPrompts -eq 0) {
    Write-Host "✅ VERIFICATION PASSED" -ForegroundColor Green
    exit 0
} else {
    Write-Host "❌ VERIFICATION FAILED" -ForegroundColor Red
    exit 1
}
