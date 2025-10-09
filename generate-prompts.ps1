# Generate Individual Prompts from Path-Locations.md
# This script creates individual prompt files for each path in Path-Locations.md

$promptTemplate = Get-Content -Path "PROMPT.md" -Raw
$pathsFile = "Path-Locations.md"

# Create output directory
$outputDir = "generated-prompts"
if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# Read paths from Path-Locations.md (skip header lines)
$paths = Get-Content $pathsFile | Where-Object { $_ -match "^\d+\. " } | ForEach-Object {
    $_.Substring($_.IndexOf(". ") + 2)
}

# Generate prompt for ALL 842 paths
$counter = 0
$maxPrompts = 842  # Generate ALL prompts
foreach ($path in $paths) {
    if ($counter -ge $maxPrompts) { break }

    $counter++
    $folderPath = $path -replace "Apex Arbitrage Multichain bot/", ""

    # Replace placeholder in template (handle both hyphenated and non-hyphenated versions)
    $customPrompt = $promptTemplate -replace "\[folder-path\]", $folderPath
    $customPrompt = $customPrompt -replace "\[your-folder-path\]", $folderPath

    # Create filename from path (sanitize for filesystem)
    $fileName = $folderPath -replace "/", "-" -replace "\\", "-" -replace ":", "" -replace "<", "" -replace ">", "" -replace '"', "" -replace "\|", "" -replace "\?", "" -replace "\*", ""
    $fileName = "prompt-{0:000}-{1}.md" -f $counter, $fileName

    # Write to file
    $customPrompt | Out-File -FilePath "$outputDir\$fileName" -Encoding UTF8

    Write-Host "Generated prompt $counter for: $path"
}

Write-Host "Generated $counter example prompt files in $outputDir directory"