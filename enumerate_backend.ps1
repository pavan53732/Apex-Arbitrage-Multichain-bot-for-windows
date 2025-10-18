try {
    $path = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\Apex Arbitrage Multichain bot\backend"
    if (-not (Test-Path $path)) { Write-Host "ERROR: Path not found"; exit 1 }

$files = Get-ChildItem -Path $path -Recurse -File -Force
$folders = Get-ChildItem -Path $path -Recurse -Directory -Force

    Write-Host "TOTAL FILES: $($files.Count) | TOTAL FOLDERS: $($folders.Count)"

    if ($files.Count -gt 200) { Write-Host "LARGE FOLDER: $($files.Count) files detected" }
    if ($files.Count -gt 500) { Write-Host "ULTRA-MASSIVE FOLDER: Will use intensive micro-chunking" }

    # Dynamic validation based on complexity
    $extensions = $files | ForEach-Object { [System.IO.Path]::GetExtension($_) } | Select-Object -Unique
    $complexity = if ($extensions.Count -le 2) { "Simple" }
                  elseif ($extensions.Count -le 5) { "Mixed" }
                  elseif ($extensions.Count -le 8) { "Complex" }
                  else { "Critical" }

    switch ($complexity) {
        "Simple" { $validationInterval = 50 }    # Homogeneous file types
        "Mixed" { $validationInterval = 25 }     # Multiple content types
        "Complex" { $validationInterval = 15 }   # High diversity, mixed purposes
        "Critical" { $validationInterval = 10 }  # Smart contracts, security files
    }

    Write-Host "COMPLEXITY: $complexity | VALIDATION EVERY: $validationInterval files"

    # MANDATORY: List EVERY SINGLE FILE - NO EXCEPTIONS
    Write-Host "=== COMPLETE FILE ENUMERATION ==="
    $files | Sort-Object FullName | ForEach-Object -Begin {$i=1} -Process {
    Write-Host "FILE $i/$($files.Count): $($_.FullName)"
    $i++
    }
    Write-Host "=== ENUMERATION COMPLETE: $($files.Count) files listed ==="

    # MANDATORY: List EVERY SINGLE FOLDER - NO EXCEPTIONS
    Write-Host "=== COMPLETE FOLDER ENUMERATION ==="
    $folders | Sort-Object FullName | ForEach-Object -Begin {$i=1} -Process {
    Write-Host "FOLDER $i/$($folders.Count): $($_.FullName)"
    $i++
    }
    Write-Host "=== ENUMERATION COMPLETE: $($folders.Count) folders listed ==="
} catch { Write-Host "ERROR: $($_.Exception.Message)" }