# Remove PROJECT TREE references from all prompts - Version 2
$promptsFolder = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$promptFiles = Get-ChildItem -Path $promptsFolder -Filter "prompt-*.md"

foreach ($file in $promptFiles) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Remove the entire PROJECT TREE COMPLETE STRUCTURE.md section from DATA SOURCES
    $content = $content -replace '- \*\*PROJECT TREE COMPLETE STRUCTURE\.md\*\*:.*?(?=- \*\*Path-Locations\.md\*\*:)', '', 'Singleline'
    
    # Remove "Then cross-reference with PROJECT TREE:" line
    $content = $content -replace 'Then cross-reference with PROJECT TREE:', ''
    
    # Save updated content
    Set-Content -Path $file.FullName -Value $content -NoNewline
    Write-Host "Updated: $($file.Name)"
}

Write-Host "`nCompleted updating all prompt files"
