# Regenerate All 842 Corrupted Prompt Files
$ErrorActionPreference = "Stop"

$repoRoot = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows"
$templatePath = Join-Path $repoRoot "generated-prompts\TEMPLATE-COMPLETE.md"
$pathLocationsPath = Join-Path $repoRoot "Path-Locations.md"
$outputDir = Join-Path $repoRoot "generated-prompts"

Write-Host "=== Apex Arbitrage Prompt Regeneration ===" -ForegroundColor Cyan
Write-Host "Template: $templatePath"
Write-Host "Path Locations: $pathLocationsPath"
Write-Host "Output Directory: $outputDir"
Write-Host ""

if (-not (Test-Path $templatePath)) {
    Write-Host "ERROR: Template file not found" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $pathLocationsPath)) {
    Write-Host "ERROR: Path-Locations.md not found" -ForegroundColor Red
    exit 1
}

Write-Host "Reading template..." -ForegroundColor Yellow
$template = Get-Content $templatePath -Raw

Write-Host "Reading Path-Locations.md..." -ForegroundColor Yellow
$pathLocationsContent = Get-Content $pathLocationsPath -Raw

$pathPattern = '^\s*(\d+)\.\s+(.+)$'
$paths = @()

foreach ($line in ($pathLocationsContent -split "`n")) {
    if ($line -match $pathPattern) {
        $number = [int]$matches[1]
        $path = $matches[2].Trim()
        $paths += @{Number = $number; Path = $path}
    }
}

Write-Host "Found $($paths.Count) paths" -ForegroundColor Green

if ($paths.Count -eq 0) {
    Write-Host "ERROR: No paths found" -ForegroundColor Red
    exit 1
}

$successCount = 0
$errorCount = 0

foreach ($pathEntry in $paths) {
    $promptNumber = $pathEntry.Number
    $folderPath = $pathEntry.Path
    
    $promptNumberFormatted = $promptNumber.ToString("D3")
    $outputFile = Join-Path $outputDir "prompt-$promptNumberFormatted.md"
    
    Write-Host "[$promptNumberFormatted] $folderPath" -ForegroundColor Cyan
    
    try {
        $promptContent = $template -replace '\{PROMPT_NUMBER\}', $promptNumber
        $promptContent = $promptContent -replace '\{FOLDER_PATH\}', $folderPath
        
        Set-Content -Path $outputFile -Value $promptContent -Encoding UTF8
        
        $successCount++
        Write-Host "  Created" -ForegroundColor Green
        
    } catch {
        $errorCount++
        Write-Host "  ERROR: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "=== Complete ===" -ForegroundColor Cyan
Write-Host "Success: $successCount" -ForegroundColor Green
Write-Host "Errors: $errorCount" -ForegroundColor Red
