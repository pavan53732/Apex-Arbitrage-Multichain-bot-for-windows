# Fix by replacing exact corrupted byte sequences
$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

for ($i = 1; $i -le 842; $i++) {
    $fileName = "prompt-{0:D3}.md" -f $i
    $filePath = Join-Path $promptsDir $fileName
    
    if (Test-Path $filePath) {
        # Read as raw bytes
        $bytes = [System.IO.File]::ReadAllBytes($filePath)
        $content = [System.Text.Encoding]::UTF8.GetString($bytes)
        
        # Replace the exact corrupted patterns we see
        $content = $content -replace "## ðŸš¨ MANDATORY CHECKPOINT", "## 🚨 MANDATORY CHECKPOINT"
        $content = $content -replace "## dYs`" MANDATORY CHECKPOINT", "## 🚨 MANDATORY CHECKPOINT"
        $content = $content -replace "\*\*âš ï¸ STOP AND READ", "**⚠️ STOP AND READ"
        $content = $content -replace "â†'", "→"
        $content = $content -replace "â€¦", "…"
        
        # Write back as UTF-8 without BOM
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
        
        Write-Host "Fixed: $fileName"
    }
}

Write-Host "`nCompleted fixing all 842 files"
