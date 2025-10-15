# Fix encoding issues in checkpoint section (lines 722-724)
$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$encoding = New-Object System.Text.UTF8Encoding $false

$fixedCount = 0

for ($i = 1; $i -le 842; $i++) {
    $fileName = "prompt-{0:D3}.md" -f $i
    $filePath = Join-Path $promptsDir $fileName
    
    if (Test-Path $filePath) {
        $content = [System.IO.File]::ReadAllText($filePath, $encoding)
        
        # Fix the corrupted checkpoint header and warning line
        $content = $content -replace "## ðŸš¨ MANDATORY CHECKPOINT: NUMBERING FORMAT CONFIRMATION", "## 🚨 MANDATORY CHECKPOINT: NUMBERING FORMAT CONFIRMATION"
        $content = $content -replace "\*\*âš ï¸ STOP AND READ - DO NOT PROCEED TO STEP 5 WITHOUT COMPLETING THIS CHECKPOINT\*\*", "**⚠️ STOP AND READ - DO NOT PROCEED TO STEP 5 WITHOUT COMPLETING THIS CHECKPOINT**"
        
        # Write back with UTF-8 no BOM
        [System.IO.File]::WriteAllText($filePath, $content, $encoding)
        
        Write-Host "✅ Fixed: $fileName" -ForegroundColor Green
        $fixedCount++
    }
}

Write-Host "`n🎉 Encoding issues fixed in $fixedCount prompt files!" -ForegroundColor Cyan
Write-Host "✨ All files use proper UTF-8 encoding (no BOM)" -ForegroundColor Yellow
