# Update all 842 prompts to use PowerShell for folder scanning
$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

$oldStep2 = '### STEP 2: LOOKUP ACTUAL FILES (MANDATORY COMPLETE ENUMERATION)

- Search PROJECT TREE COMPLETE STRUCTURE.md for the exact [folder-path]'

$newStep2 = '### STEP 2: SCAN ACTUAL FOLDER WITH POWERSHELL (MANDATORY COMPLETE ENUMERATION)

- Execute PowerShell command to scan the ACTUAL folder:
  ```powershell
  Get-ChildItem -Path "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex Arbitrage Multichain bot\[folder-path]" -Recurse
  ```
- Count files per subfolder accurately
- Preserve exact folder hierarchy'

Get-ChildItem "$promptsDir\prompt-*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    $content = $content -replace [regex]::Escape($oldStep2), $newStep2
    Set-Content -Path $_.FullName -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Updated $($_.Name)" -ForegroundColor Green
}

Write-Host "Done!" -ForegroundColor Cyan
