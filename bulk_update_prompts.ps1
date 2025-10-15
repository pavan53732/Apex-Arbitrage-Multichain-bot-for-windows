# Bulk update script for adding numbering format to all prompt files
$basePath = 'C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts'
$files = Get-ChildItem -Path $basePath -Filter 'prompt-*.md' | Where-Object { $_.Name -ne 'prompt-001.md' } | Sort-Object Name

$newSection = @'
**REQUIRED FORMAT:**

###  MANDATORY NUMBERING FORMAT

**CRITICAL**: Every folder and file MUST be numbered:

**Folder Format:** FOLDER X/Y: foldername/ where X = current, Y = total
**File Format:** FILE X/Y: filename.ext where X = current, Y = total

**Example:**

`
FOLDER 1/11: backend/contracts/
 FOLDER 2/11: docs/
  FILE 1/125: README.md
  FILE 2/125: GOVERNANCE.md
  FILE 3/125: SECURITY.md
 FOLDER 3/11: interfaces/
  FILE 4/125: IAIAgentInterface.sol
  FILE 5/125: IAlphaNFT.sol
`

**FORBIDDEN**: Listing without FOLDER X/Y: or FILE X/Y: prefix

`
Folder Structure:
'@

$totalFiles = $files.Count
$processed = 0

Write-Host "Processing $totalFiles files..."

foreach ($file in $files) {
    $filePath = $file.FullName
    $content = Get-Content -Path $filePath -Raw -Encoding UTF8
    
    # Replace the old content with new content
    $oldString = '**REQUIRED FORMAT:**' + "

" + '`' + "
" + 'Folder Structure:'
    $newContent = $content -replace [regex]::Escape($oldString), $newSection
    
    if ($newContent -ne $content) {
        Set-Content -Path $filePath -Value $newContent -Encoding UTF8
        $processed++
        Write-Host "Updated: $file.Name ($processed/$totalFiles)"
    } else {
        Write-Host "Skipped: $file.Name (no changes needed)"
    }
}

Write-Host "Completed! Processed $processed files."
