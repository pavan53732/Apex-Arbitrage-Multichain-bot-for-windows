# RESTORE - Remove the incorrectly placed header at the beginning
$promptsPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

Write-Host "`n============================================" -ForegroundColor Yellow
Write-Host "   REMOVING INCORRECTLY PLACED HEADERS" -ForegroundColor Yellow  
Write-Host "============================================" -ForegroundColor Yellow

$files = Get-ChildItem -Path $promptsPath -Filter "prompt-*.md" -File
$total = $files.Count
$fixed = 0

foreach ($file in $files) {
    Write-Host "Restoring $($file.Name)..." -NoNewline
    
    $content = Get-Content $file.FullName -Raw
    $original = $content
    
    # Remove the incorrectly placed header at the beginning (lines 1-23)
    if ($content -match "^[\r\n]*# MANDATORY COMPLIANCE - LIST EVERY FILE") {
        # Remove everything from the start up to and including the "---" line before DELEGATION FLOW
        $content = $content -replace "^[\s\S]*?---\r?\n(## 🎯 DELEGATION FLOW: COMPLETE ALL STEPS)", '$1'
    }
    
    if ($content -ne $original) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $fixed++
        Write-Host " RESTORED!" -ForegroundColor Green
    } else {
        Write-Host " No changes needed" -ForegroundColor Yellow
    }
}

Write-Host "`n============================================" -ForegroundColor Green
Write-Host "           RESTORATION COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host "Files processed: $total" -ForegroundColor White
Write-Host "Files restored: $fixed" -ForegroundColor Green
Write-Host "`nPrompts now start correctly with DELEGATION FLOW" -ForegroundColor Cyan