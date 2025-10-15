param(
  [string]$Root = (Resolve-Path "$PSScriptRoot\.."),
  [int]$StartIndex = 0,
  [int]$Count = 1000000,
  [int]$ProgressEvery = 200
)

Write-Host "Normalization root: $Root"
$files = Get-ChildItem -Path (Join-Path $Root 'generated-prompts') -Filter 'prompt-*.md' | Sort-Object Name
$slice = $files | Select-Object -Skip $StartIndex -First $Count

if (-not $slice) {
  Write-Host "No files to process."
  exit 0
}

$i = 0
$updated = 0
$replacementLine = '- Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering (folders first, then files) at each level'

foreach ($f in $slice) {
  $i++
  $orig = Get-Content -LiteralPath $f.FullName -Raw

  # Replace any enforcement bullet line (with any preceding symbols) to a clean ASCII-only line
  $content = [System.Text.RegularExpressions.Regex]::Replace(
    $orig,
    '(?m)^[\t ]*[-*] +.*Enforce numbering rules:.*$',
    $replacementLine
  )

  if ($content -ne $orig) {
    # Normalize to LF endings and write UTF-8 without BOM
    $content = $content -replace "\r\n?", "`n"
    [System.IO.File]::WriteAllText($f.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    $updated++
  }

  if ($i % $ProgressEvery -eq 0) {
    Write-Host ("Processed {0}/{1} files... Updated: {2}" -f $i, $slice.Count, $updated)
  }
}

Write-Host ("Normalization complete. Files processed: {0}. Files updated: {1}" -f $slice.Count, $updated)
