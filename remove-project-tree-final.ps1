# Remove PROJECT TREE references - Final version
$promptsFolder = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$promptFiles = Get-ChildItem -Path $promptsFolder -Filter "prompt-*.md"

foreach ($file in $promptFiles) {
    $lines = Get-Content -Path $file.FullName
    $newLines = @()
    $skipMode = $false
    
    foreach ($line in $lines) {
        # Start skipping when we hit PROJECT TREE section
        if ($line -match '^\s*-\s+\*\*PROJECT TREE COMPLETE STRUCTURE') {
            $skipMode = $true
            continue
        }
        
        # Stop skipping when we hit Path-Locations section
        if ($line -match '^\s*-\s+\*\*Path-Locations') {
            $skipMode = $false
        }
        
        # Skip "Then cross-reference with PROJECT TREE:" line
        if ($line -match 'Then cross-reference with PROJECT TREE:') {
            continue
        }
        
        # Add line if not in skip mode
        if (-not $skipMode) {
            $newLines += $line
        }
    }
    
    # Write back
    $newLines | Set-Content -Path $file.FullName
    Write-Host "Updated: $($file.Name)"
}

Write-Host "`nCompleted!"
