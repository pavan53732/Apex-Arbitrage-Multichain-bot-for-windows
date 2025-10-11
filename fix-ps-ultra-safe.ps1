# Ultra-safe PowerShell fix - only replaces specific lines, preserves everything else
$promptsDir = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$files = Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | Sort-Object Name

$fixedCount = 0

foreach ($file in $files) {
    # Extract folder name from filename
    if ($file.Name -match 'prompt-\d+-(.*?)\.md') {
        $folderName = $matches[1]
        
        $lines = Get-Content -Path $file.FullName
        $modified = $false
        
        # Find line 109 (index 108) - the old $files = Get-ChildItem line
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match '^\$files = Get-ChildItem -Path "C:\\Users\\Pavan pc.*\$folderPath" -Recurse -File -Force$') {
                # Found it! Replace lines 109-119 (indices 108-118)
                $lines[$i] = "`$folderPath = `"$folderName`""
                $lines[$i+1] = '$fullPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\$folderPath"'
                $lines[$i+2] = ''
                $lines[$i+3] = 'Write-Host "=== ENUMERATING: $folderPath ==="'
                $lines[$i+4] = 'Write-Host ""'
                $lines[$i+5] = ''
                $lines[$i+6] = '$files = Get-ChildItem -Path $fullPath -Recurse -File -Force -ErrorAction Stop'
                $lines[$i+7] = ''
                $lines[$i+8] = 'Write-Host "TOTAL FILES FOUND: $($files.Count)"'
                $lines[$i+9] = 'Write-Host ""'
                $lines[$i+10] = 'Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"'
                
                # Keep line i+11 as-is (if statement line)
                # Replace lines i+12 to i+18
                $lines[$i+12] = ''
                $lines[$i+13] = 'foreach ($file in $files) {'
                $lines[$i+14] = '    Write-Host $file.FullName'
                $lines[$i+15] = '}'
                $lines[$i+16] = ''
                $lines[$i+17] = 'Write-Host ""'
                $lines[$i+18] = 'Write-Host "--- END OF COMPLETE LIST ---"'
                $lines[$i+19] = 'Write-Host "VERIFICATION: Listed $($files.Count) files above"'
                
                $modified = $true
                break
            }
        }
        
        if ($modified) {
            Set-Content -Path $file.FullName -Value $lines
            $fixedCount++
        }
    }
}

Write-Host "Fixed $fixedCount prompts (ultra-safe mode)"
