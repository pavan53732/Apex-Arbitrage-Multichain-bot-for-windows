# RESET FEATURES - Reset all feature .md files to initial empty state
$featuresPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\features"

Write-Host "`n============================================" -ForegroundColor Yellow
Write-Host "   RESETTING ALL FEATURE FILES TO EMPTY" -ForegroundColor Yellow  
Write-Host "============================================" -ForegroundColor Yellow

# List of feature files to reset (excluding README.md)
$featureFiles = @(
    "ai-modules.md",
    "archive.md",
    "backend.md",
    "config.md",
    "contracts.md",
    "dashboard.md",
    "deployment.md",
    "docs.md",
    "install-dependencies.md",
    "security.md",
    "testing.md"
)

$resetCount = 0

foreach ($file in $featureFiles) {
    $filePath = Join-Path $featuresPath $file
    
    if (Test-Path $filePath) {
        Write-Host "Resetting $file..." -NoNewline
        
        # Create empty file with just the filename as header
        $fileName = [System.IO.Path]::GetFileNameWithoutExtension($file)
        $headerName = $fileName.Replace("-", " ")
        $headerName = (Get-Culture).TextInfo.ToTitleCase($headerName)
        
        # Write minimal content (just a header)
        $content = "# $headerName`n"
        Set-Content -Path $filePath -Value $content -NoNewline
        
        Write-Host " RESET!" -ForegroundColor Green
        $resetCount++
    } else {
        Write-Host "Creating $file..." -NoNewline
        
        # Create the file if it doesn't exist
        $fileName = [System.IO.Path]::GetFileNameWithoutExtension($file)
        $headerName = $fileName.Replace("-", " ")
        $headerName = (Get-Culture).TextInfo.ToTitleCase($headerName)
        
        $content = "# $headerName`n"
        Set-Content -Path $filePath -Value $content -NoNewline
        
        Write-Host " CREATED!" -ForegroundColor Cyan
        $resetCount++
    }
}

# Check and delete progress.md if it exists
$progressPath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\progress.md"
if (Test-Path $progressPath) {
    Write-Host "`nDeleting progress.md..." -NoNewline
    Remove-Item -Path $progressPath -Force
    Write-Host " DELETED!" -ForegroundColor Red
} else {
    Write-Host "`nprogress.md not found (already deleted)" -ForegroundColor Gray
}

Write-Host "`n============================================" -ForegroundColor Green
Write-Host "           RESET COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host "Files reset: $resetCount" -ForegroundColor White

# Show current state
Write-Host "`nCurrent state of features folder:" -ForegroundColor Cyan
$files = Get-ChildItem -Path $featuresPath -Filter "*.md" | Select-Object Name, Length
$files | Format-Table -AutoSize

Write-Host "`nAll feature files are now reset to empty!" -ForegroundColor Green
Write-Host "README.md was preserved (not reset)" -ForegroundColor Yellow
Write-Host "progress.md has been removed" -ForegroundColor Yellow
Write-Host "`nReady for fresh feature documentation!" -ForegroundColor Cyan