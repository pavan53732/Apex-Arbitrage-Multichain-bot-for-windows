# SUPER ENFORCEMENT - Forces AI to list EVERYTHING
$promptsPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

Write-Host "`n============================================" -ForegroundColor Red
Write-Host "   SUPER ENFORCER - NO FILE GETS SKIPPED!" -ForegroundColor Red  
Write-Host "============================================" -ForegroundColor Red

$files = Get-ChildItem -Path $promptsPath -Filter "prompt-*.md" -File
$total = $files.Count
$fixed = 0

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..." -NoNewline
    
    $content = Get-Content $file.FullName -Raw
    $original = $content
    
    # Add SUPER STRONG enforcement header
    if ($content -notmatch "MANDATORY COMPLIANCE") {
        $header = @"

# MANDATORY COMPLIANCE - LIST EVERY FILE

## ZERO TOLERANCE POLICY

**YOU MUST:**
- LIST ALL 5000+ FILES (NO EXCEPTIONS)
- LIST ALL 1000+ FOLDERS (NO EXCEPTIONS)  
- WRITE 20-30 WORDS PER FILE (NO EXCEPTIONS)
- CONTINUE UNTIL 100% COMPLETE (NO EXCEPTIONS)

**FORBIDDEN:**
- Using ... or etc = FAIL
- Using "and more" = FAIL
- Stopping early = FAIL
- Skipping ANY file = FAIL

**ENFORCEMENT:**
If you skip even 1 file out of 5000, YOU HAVE FAILED.
There is NO acceptable reason to not list a file.
CONTINUE LISTING until EVERY file is documented.

---

"@
        $content = $header + $content
    }
    
    # Replace weak language
    $content = $content -replace "should", "MUST"
    $content = $content -replace "recommended", "REQUIRED"
    $content = $content -replace "if possible", "MANDATORY"
    
    # Add chunking reminder
    if ($content -notmatch "CHUNK CONTINUATION") {
        $content = $content -replace "(Write-Host .--- COMPLETE FILE LIST)", @"
Write-Host "REMINDER: Must list EVERY file - Use CHUNKS if needed"
`$1
"@
    }
    
    # Add validation loops
    if ($content -notmatch "VALIDATION LOOP") {
        $validation = @"

### VALIDATION LOOP REQUIREMENT

After EVERY 100 files:
1. COUNT what you listed
2. VERIFY against PowerShell count
3. If mismatch, GO BACK and fix
4. DO NOT proceed until counts match

"@
        $content = $content -replace "(Before writing files, verify)", ($validation + "`$1")
    }
    
    # Add continuation enforcement
    $content = $content -replace "(If ANY element is missing)", @"
`$1

**CONTINUATION PROTOCOL:**
- If interrupted at file 500 of 5000
- IMMEDIATELY continue from file 501
- DO NOT restart from beginning
- COMPLETE the remaining 4500 files
- NO EXCUSES ACCEPTED
"@
    
    if ($content -ne $original) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $fixed++
        Write-Host " ENFORCED!" -ForegroundColor Green
    } else {
        Write-Host " Already enforced" -ForegroundColor Yellow
    }
}

Write-Host "`n============================================" -ForegroundColor Green
Write-Host "         SUPER ENFORCEMENT COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host "Files processed: $total" -ForegroundColor White
Write-Host "Files enforced: $fixed" -ForegroundColor Green

Write-Host "`nKey enforcement added:" -ForegroundColor Cyan
Write-Host "- MANDATORY COMPLIANCE header" -ForegroundColor Yellow
Write-Host "- ZERO TOLERANCE policy" -ForegroundColor Yellow
Write-Host "- CONTINUATION PROTOCOL" -ForegroundColor Yellow
Write-Host "- VALIDATION LOOPS every 100 files" -ForegroundColor Yellow
Write-Host "- Replaced all weak language" -ForegroundColor Yellow

Write-Host "`nNOW AI MUST LIST:" -ForegroundColor Red
Write-Host "- EVERY FILE (even if 5000+)" -ForegroundColor White
Write-Host "- EVERY FOLDER (even if 1000+)" -ForegroundColor White
Write-Host "- FULL DESCRIPTIONS (20-30 words)" -ForegroundColor White
Write-Host "- NO SKIPPING ALLOWED!" -ForegroundColor White