# PROPER ENFORCEMENT - Adds enforcement in the RIGHT places
$promptsPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "   PROPER ENFORCEMENT - CORRECT PLACEMENT" -ForegroundColor Cyan  
Write-Host "============================================" -ForegroundColor Cyan

$files = Get-ChildItem -Path $promptsPath -Filter "prompt-*.md" -File
$total = $files.Count
$fixed = 0

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..." -NoNewline
    
    $content = Get-Content $file.FullName -Raw
    $original = $content
    
    # Find the CRITICAL STOP-CHECK section and enhance it
    if ($content -match "## ⚠️ CRITICAL STOP-CHECK BEFORE EXECUTION ⚠️") {
        
        # Add MANDATORY COMPLIANCE right AFTER the CRITICAL STOP-CHECK section
        if ($content -notmatch "### MANDATORY COMPLIANCE - ZERO TOLERANCE POLICY") {
            $content = $content -replace "(## ⚠️ CRITICAL STOP-CHECK BEFORE EXECUTION ⚠️\r?\n\r?\n\*\*READ THIS FIRST - DO NOT SKIP:\*\*\r?\n)", @"
`$1
Before you begin, understand that this prompt has **MANDATORY REQUIREMENTS** that CANNOT be skipped or simplified:

### MANDATORY COMPLIANCE - ZERO TOLERANCE POLICY

**ABSOLUTE REQUIREMENTS:**
- LIST ALL 5000+ FILES (NO EXCEPTIONS)
- LIST ALL 1000+ FOLDERS (NO EXCEPTIONS)  
- WRITE 20-30 WORDS PER FILE (NO EXCEPTIONS)
- CONTINUE UNTIL 100% COMPLETE (NO EXCEPTIONS)

**INSTANT FAILURE CONDITIONS:**
- Using ... or etc = IMMEDIATE FAIL
- Using "and more" = IMMEDIATE FAIL
- Stopping early = IMMEDIATE FAIL
- Skipping ANY file = IMMEDIATE FAIL

**ENFORCEMENT:**
If you skip even 1 file out of 5000, YOU HAVE FAILED.
There is NO acceptable reason to not list a file.
CONTINUE LISTING until EVERY file is documented.

"@
        }
    }
    
    # Enhance the MANDATORY: HANDLE 3000+ FILES section
    if ($content -match "### 🚨 MANDATORY: HANDLE 3000\+ FILES WITHOUT SKIPPING 🚨") {
        # Add validation loop requirement after this section
        if ($content -notmatch "### VALIDATION LOOP REQUIREMENT") {
            $content = $content -replace "(### 🚨 MANDATORY: HANDLE 3000\+ FILES WITHOUT SKIPPING 🚨[\s\S]*?\*\*IF YOU SKIP EVEN ONE FILE, THE OUTPUT IS REJECTED\.\*\*\r?\n)", @"
`$1

### VALIDATION LOOP REQUIREMENT

**After EVERY 100 files:**
1. COUNT what you listed
2. VERIFY against PowerShell count  
3. If mismatch, GO BACK and fix
4. DO NOT proceed until counts match

**CONTINUATION PROTOCOL:**
- If interrupted at file 500 of 5000
- IMMEDIATELY continue from file 501
- DO NOT restart from beginning
- COMPLETE the remaining 4500 files
- NO EXCUSES ACCEPTED

"@
        }
    }
    
    # Enhance the EXAMPLES section with stronger enforcement
    if ($content -match "✅ CORRECT \(3000 files\):") {
        $content = $content -replace "(\.\.\. \(LIST ALL \d+ FILES - NO SKIPPING\))", @"
`$1

**MANDATORY: Every single file MUST have:**
- Full filename with extension
- Arrow separator (→)
- 20-30 word technical description
- NO shortcuts, NO summaries, NO grouping
"@
    }
    
    # Replace weak language throughout
    $content = $content -replace "\bshould\b", "MUST"
    $content = $content -replace "\brecommended\b", "REQUIRED"
    $content = $content -replace "\bif possible\b", "MANDATORY"
    $content = $content -replace "\boptional\b", "REQUIRED"
    $content = $content -replace "\bcan skip\b", "MUST NOT skip"
    $content = $content -replace "\bmay\b(?! not)", "MUST"
    
    # Add chunking reminder in the VALIDATION BEFORE WRITING section
    if ($content -match "VALIDATION BEFORE WRITING:" -and $content -notmatch "CHUNKING STRATEGY") {
        $content = $content -replace "(VALIDATION BEFORE WRITING:)", @"
`$1

**CHUNKING STRATEGY FOR MASSIVE LISTS:**
- If output exceeds response limit, use CHUNKS
- Chunk 1: Files 1-500 with marker [CONTINUING IN NEXT RESPONSE]
- Chunk 2: Files 501-1000 with marker [CONTINUING FROM PREVIOUS]
- Continue until ALL files are listed
- NEVER skip files between chunks

"@
    }
    
    # Strengthen the SELF-CHECK section
    if ($content -match "### SELF-CHECK BEFORE WRITING:") {
        $content = $content -replace "(Ask yourself:)", @"
`$1

**MANDATORY VALIDATION - ALL MUST BE YES:**
"@
        $content = $content -replace "(\*\*If you answer NO to ANY question above, DO NOT PROCEED\. Go back and complete it\.\*\*)", @"
`$1

**FAILURE TO COMPLETE = TASK REJECTION**
Every checkbox MUST be checked. No exceptions.
"@
    }
    
    if ($content -ne $original) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $fixed++
        Write-Host " PROPERLY ENFORCED!" -ForegroundColor Green
    } else {
        Write-Host " Already enforced" -ForegroundColor Yellow
    }
}

Write-Host "`n============================================" -ForegroundColor Green
Write-Host "        PROPER ENFORCEMENT COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host "Files processed: $total" -ForegroundColor White
Write-Host "Files properly enforced: $fixed" -ForegroundColor Green

Write-Host "`nEnforcement added in CORRECT locations:" -ForegroundColor Cyan
Write-Host "- After CRITICAL STOP-CHECK section" -ForegroundColor Yellow
Write-Host "- Enhanced 3000+ FILES section" -ForegroundColor Yellow
Write-Host "- Added VALIDATION LOOPS" -ForegroundColor Yellow
Write-Host "- Added CHUNKING STRATEGY" -ForegroundColor Yellow
Write-Host "- Strengthened SELF-CHECK section" -ForegroundColor Yellow
Write-Host "- Replaced all weak language" -ForegroundColor Yellow

Write-Host "`nPrompts now maintain proper structure:" -ForegroundColor Green
Write-Host "- Still starts with DELEGATION FLOW" -ForegroundColor White
Write-Host "- Enforcement integrated into existing sections" -ForegroundColor White
Write-Host "- No disruption to prompt flow" -ForegroundColor White
Write-Host "- Maximum enforcement without breaking structure" -ForegroundColor White
