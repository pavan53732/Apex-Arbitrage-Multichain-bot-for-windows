param(
  [string]$Root = (Resolve-Path "$PSScriptRoot\.."),
  [int]$StartIndex = 0,
  [int]$Count = 1000000,
  [int]$ProgressEvery = 100
)

Write-Host "Normalization root: $Root"
$files = Get-ChildItem -Path (Join-Path $Root 'generated-prompts') -Filter 'prompt-*.md' | Sort-Object Name
$slice = $files | Select-Object -Skip $StartIndex -First $Count

if (-not $slice) {
  Write-Host "No files to process."
  exit 0
}

$replacements = @(
  # Common mojibake for check mark (✓) as seen in UTF-8 mis-decoding
  @{ Pattern = 'âœ…'; Replacement = '- [x]'; Description = 'Replace mojibake checkmark with ASCII checkbox' },
  @{ Pattern = 'âœ”'; Replacement = '- [x]'; Description = 'Replace mojibake heavy check with ASCII checkbox' },
  # Smart quotes and ellipsis
  @{ Pattern = 'â€¦'; Replacement = '...'; Description = 'Normalize ellipsis' },
  @{ Pattern = 'â€œ'; Replacement = '"'; Description = 'Normalize left smart quote' },
  @{ Pattern = 'â€'; Replacement = '"'; Description = 'Normalize right smart quote' },
  @{ Pattern = 'â€™'; Replacement = "'"; Description = 'Normalize apostrophe' },
  @{ Pattern = 'â€“'; Replacement = '-'; Description = 'Normalize en dash' },
  @{ Pattern = 'â€”'; Replacement = '--'; Description = 'Normalize em dash' }
)

$i = 0
$updated = 0
foreach ($f in $slice) {
  $i++
  try {
    $orig = Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8
  } catch {
    # Fallback to default encoding if UTF-8 read fails
    $orig = Get-Content -LiteralPath $f.FullName -Raw
  }

  $content = $orig
  foreach ($r in $replacements) {
    $content = $content -replace [regex]::Escape($r.Pattern), [System.Text.RegularExpressions.Regex]::Escape($r.Replacement) -replace '\\', '\\'
  }

  # Also normalize any lingering Unicode checkmark to ASCII checkbox
  $content = $content -replace '\u2713|\u2714|\u2705', '- [x]'

  if ($content -ne $orig) {
    # Ensure LF line endings for Markdown
    $content = $content -replace '\r\n?', "`n"
    [System.IO.File]::WriteAllText($f.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    $updated++
  }

  if ($i % $ProgressEvery -eq 0) {
    Write-Host ("Processed {0}/{1} files... Updated: {2}" -f $i, $slice.Count, $updated)
  }
}

Write-Host ("Normalization complete. Files processed: {0}. Files updated: {1}" -f $slice.Count, $updated)
