try {
    $basePath = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot"
    $targetPath = Join-Path $basePath "ai-modules"

    Write-Host "Checking path: $targetPath"

    if (-not (Test-Path $targetPath)) {
        Write-Host "ERROR: Path does not exist: $targetPath"
        exit 1
    }

    $files = Get-ChildItem -Path $targetPath -Recurse -File -Force -ErrorAction Stop
    $folders = Get-ChildItem -Path $targetPath -Recurse -Directory -Force -ErrorAction Stop

    Write-Host "TOTAL FILES FOUND: $($files.Count)"
    Write-Host "TOTAL FOLDERS FOUND: $($folders.Count)"

    Write-Host "--- COMPLETE FOLDER STRUCTURE (ALL $($folders.Count) FOLDERS) ---"
    $folders | Sort-Object FullName | ForEach-Object {
        $relativePath = $_.FullName.Replace($targetPath, "").TrimStart('\')
        Write-Host $relativePath
    }
    Write-Host "--- END OF FOLDER STRUCTURE ---"

    # Check if we need chunking for large folders
    if ($files.Count -gt 500) {
        Write-Host "LARGE FOLDER: $($files.Count) files - Processing in chunks"
    }
    Write-Host "REMINDER: Must list EVERY file - Use CHUNKS if needed"
    Write-Host "--- COMPLETE FILE LIST (ALL $($files.Count) FILES) ---"
    $fileIndex = 1
    $files | Sort-Object FullName | ForEach-Object {
        Write-Host "FILE $fileIndex/$($files.Count): $($_.FullName)"
        $fileIndex++
    }
    Write-Host "--- END OF COMPLETE LIST ---"

} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
    Write-Host "Failed to enumerate files in: $targetPath"
    exit 1
}