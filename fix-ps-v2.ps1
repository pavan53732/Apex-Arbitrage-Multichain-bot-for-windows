# Fix PowerShell enumeration - version 2
$promptsDir = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$files = Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | Sort-Object Name

$fixedCount = 0

foreach ($file in $files) {
    $lines = Get-Content -Path $file.FullName
    $modified = $false
    
    # Extract folder name from filename
    if ($file.Name -match 'prompt-\d+-(.*?)\.md') {
        $folderName = $matches[1]
        
        # Find and replace PowerShell block (lines 108-120)
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match '^```powershell$' -and $i -lt ($lines.Count - 15)) {
                # Check if next line is the old command
                if ($lines[$i+1] -match '^\$files = Get-ChildItem -Path') {
                    # Replace entire block
                    $lines[$i] = '```powershell'
                    $lines[$i+1] = "`$folderPath = `"$folderName`""
                    $lines[$i+2] = '$fullPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\$folderPath"'
                    $lines[$i+3] = ''
                    $lines[$i+4] = 'Write-Host "=== ENUMERATING: $folderPath ==="'
                    $lines[$i+5] = 'Write-Host ""'
                    $lines[$i+6] = ''
                    $lines[$i+7] = '$files = Get-ChildItem -Path $fullPath -Recurse -File -Force -ErrorAction Stop'
                    $lines[$i+8] = ''
                    $lines[$i+9] = 'Write-Host "TOTAL FILES FOUND: $($files.Count)"'
                    $lines[$i+10] = 'Write-Host ""'
                    $lines[$i+11] = 'Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"'
                    $lines[$i+12] = ''
                    $lines[$i+13] = 'foreach ($file in $files) {'
                    $lines[$i+14] = '    Write-Host $file.FullName'
                    $lines[$i+15] = '}'
                    $lines[$i+16] = ''
                    $lines[$i+17] = 'Write-Host ""'
                    $lines[$i+18] = 'Write-Host "--- END OF COMPLETE LIST ---"'
                    $lines[$i+19] = 'Write-Host "VERIFICATION: Listed $($files.Count) files above"'
                    $lines[$i+20] = '```'
                    
                    # Remove old lines (21-32)
                    for ($j = $i+21; $j -le $i+32; $j++) {
                        if ($j -lt $lines.Count) {
                            $lines[$j] = $null
                        }
                    }
                    
                    $modified = $true
                    break
                }
            }
        }
    }
    
    if ($modified) {
        $lines = $lines | Where-Object { $_ -ne $null }
        Set-Content -Path $file.FullName -Value $lines
        $fixedCount++
    }
}

Write-Host "Fixed $fixedCount prompts"
