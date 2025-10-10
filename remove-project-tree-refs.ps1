# Remove PROJECT TREE COMPLETE STRUCTURE.md references from all prompts
$promptsFolder = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$promptFiles = Get-ChildItem -Path $promptsFolder -Filter "prompt-*.md"

foreach ($file in $promptFiles) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Remove MANDATORY DOCUMENTATION PROTOCOL section (entire block)
    $content = $content -replace '(?s)## MANDATORY DOCUMENTATION PROTOCOL.*?(?=##\s+\w)', ''
    
    # Remove "Search PROJECT TREE COMPLETE STRUCTURE.md" line from STEP 2
    $content = $content -replace '\s*-\s*Search PROJECT TREE COMPLETE STRUCTURE\.md for the exact.*?\r?\n', ''
    
    # Save updated content
    Set-Content -Path $file.FullName -Value $content -NoNewline
    Write-Host "Updated: $($file.Name)"
}

Write-Host "`nCompleted updating all prompt files"
