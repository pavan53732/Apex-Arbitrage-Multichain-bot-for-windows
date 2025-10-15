# Fix encoding issues - read as UTF-8, fix corrupted text, write as UTF-8 no BOM
$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

for ($i = 1; $i -le 842; $i++) {
    $fileName = "prompt-{0:D3}.md" -f $i
    $filePath = Join-Path $promptsDir $fileName
    
    if (Test-Path $filePath) {
        # Read with UTF-8
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
        
        # Replace ALL variations of corrupted emojis
        $content = $content -replace "ðŸš¨", "🚨"
        $content = $content -replace "âš ï¸", "⚠️"
        $content = $content -replace "â†'", "→"
        $content = $content -replace "â€¦", "…"
        
        # Write with UTF-8 no BOM
        [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
        
        Write-Host "Fixed: $fileName"
    }
}

Write-Host "`nDone! Fixed all 842 files with UTF-8 no BOM encoding"
