param(
    [string]$Path = "generated-prompts",
    [string]$Pattern = "prompt-*.md",
    [switch]$TestMode
)

# Function to fix encoding corruption in files
function Fix-EncodingCorruption {
    param(
        [string]$FilePath,
        [ref]$TotalReplacements,
        [ref]$FilesProcessed
    )

    try {
        # Read file content with UTF-8 encoding
        $content = Get-Content -Path $FilePath -Encoding UTF8 -Raw

        # Count occurrences of corrupted character before replacement
        $corruptedCount = [regex]::Matches($content, 'â†').Count

        if ($corruptedCount -gt 0) {
            # Replace corrupted character sequence with correct right arrow symbol
            $fixedContent = $content -replace 'â†', '→'

            if (-not $TestMode) {
                # Write back with UTF-8 encoding (without BOM)
                $fixedContent | Out-File -FilePath $FilePath -Encoding UTF8 -NoNewline
            }

            # Update counters
            $TotalReplacements.Value += $corruptedCount
            $FilesProcessed.Value++

            Write-Host "Fixed $corruptedCount corruption(s) in $FilePath"
        } else {
            $FilesProcessed.Value++
            Write-Host "No corruption found in $FilePath"
        }
    }
    catch {
        Write-Warning "Error processing file $FilePath : $($_.Exception.Message)"
    }
}

# Main script logic
try {
    # Get all matching files
    $files = Get-ChildItem -Path $Path -Filter $Pattern -File

    if ($files.Count -eq 0) {
        Write-Host "No files found matching pattern ""$Pattern"" in path ""$Path"""
        exit 0
    }

    Write-Host "Found $($files.Count) files to process"

    # Initialize counters
    $totalReplacements = 0
    $filesProcessed = 0

    # Process each file with progress
    $files | ForEach-Object -Begin {
        $i = 0
        $total = $files.Count
    } -Process {
        $i++
        Write-Progress -Activity "Fixing encoding corruption" -Status "Processing file $($_.Name)" -PercentComplete (($i / $total) * 100)

        Fix-EncodingCorruption -FilePath $_.FullName -TotalReplacements ([ref]$totalReplacements) -FilesProcessed ([ref]$filesProcessed)
    } -End {
        Write-Progress -Activity "Fixing encoding corruption" -Completed
    }

    # Final summary
    Write-Host "`nProcessing complete:"
    Write-Host "Files processed: $filesProcessed"
    Write-Host "Total replacements made: $totalReplacements"

    if ($TestMode) {
        Write-Host "TEST MODE: No files were actually modified"
    }

} catch {
    Write-Error "Script execution failed: $($_.Exception.Message)"
    exit 1
}