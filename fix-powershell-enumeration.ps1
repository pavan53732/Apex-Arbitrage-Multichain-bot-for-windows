# Fix PowerShell enumeration in all 842 prompts
$promptsDir = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$files = Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | Sort-Object Name

$oldPS = @'
```powershell
$files = Get-ChildItem -Path "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\$folderPath" -Recurse -File -Force
Write-Host "TOTAL FILES FOUND: $($files.Count)"
Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"
if ($files.Count -le 500) {
    $files | ForEach-Object { Write-Host $_.FullName }
} else {
    Write-Host "LARGE FOLDER: $($files.Count) files - listing first 100"
    $files | Select-Object -First 100 | ForEach-Object { Write-Host $_.FullName }
    Write-Host "... and $($files.Count - 100) more files"
}
Write-Host "--- END OF COMPLETE LIST ---"
```
'@

$newPS = @'
```powershell
$folderPath = "FOLDER_NAME_PLACEHOLDER"
$fullPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\$folderPath"

Write-Host "=== ENUMERATING: $folderPath ==="
Write-Host ""

$files = Get-ChildItem -Path $fullPath -Recurse -File -Force -ErrorAction Stop

Write-Host "TOTAL FILES FOUND: $($files.Count)"
Write-Host ""
Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"

foreach ($file in $files) {
    Write-Host $file.FullName
}

Write-Host ""
Write-Host "--- END OF COMPLETE LIST ---"
Write-Host "VERIFICATION: Listed $($files.Count) files above"
```
'@

$fixedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Extract folder name from filename (e.g., prompt-001-ai-modules.md -> ai-modules)
    if ($file.Name -match 'prompt-\d+-(.*?)\.md') {
        $folderName = $matches[1]
        $customPS = $newPS -replace 'FOLDER_NAME_PLACEHOLDER', $folderName
        
        # Replace old PowerShell with new
        $newContent = $content -replace [regex]::Escape($oldPS), $customPS
        
        if ($newContent -ne $content) {
            Set-Content -Path $file.FullName -Value $newContent -NoNewline
            $fixedCount++
        }
    }
}

Write-Host "Fixed PowerShell enumeration in $fixedCount prompts"
