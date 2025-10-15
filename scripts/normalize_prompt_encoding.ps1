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

# Helper: try to decode mojibake where UTF-8 was misread as Windows-1252/Latin1
function Convert-FromMojibakeUtf8([string]$text) {
  try {
    $bytes1252 = [System.Text.Encoding]::GetEncoding(1252).GetBytes($text)
    $decoded = [System.Text.Encoding]::UTF8.GetString($bytes1252)
    return $decoded
  } catch {
    return $text
  }
}

foreach ($f in $slice) {
  $i++
  try {
    $orig = Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8
  } catch {
    $orig = Get-Content -LiteralPath $f.FullName -Raw
  }

  $content = $orig
  # First pass: attempt mojibake auto-fix (UTF-8 bytes misread as cp1252)
  $content = Convert-FromMojibakeUtf8 $content

  # Replace any enforcement bullet line (with any preceding symbols) to a clean ASCII-only line
  $content = [System.Text.RegularExpressions.Regex]::Replace(
    $content,
    '(?m)^[\t ]*[-*] +.*Enforce numbering rules:.*$',
    $replacementLine
  )

  # Replace ellipsis mojibake: UTF-8 bytes E2 80 A6 mis-decoded as U+00E2 U+20AC U+00A6
  # Build the three-character mojibake sequence via code points to avoid parser/encoding issues
  $ellipsisMojibake = ([char]0x00E2).ToString() + ([char]0x20AC).ToString() + ([char]0x00A6).ToString()
  $content = $content.Replace($ellipsisMojibake, "...")

  # Normalize common punctuation to ASCII to harden prompts
  $content = $content -replace "[\u2018\u2019]", "'"  # curly single quotes to straight
  $content = $content -replace "[\u201C\u201D]", '"'   # curly double quotes to straight
  $content = $content -replace "\u2014", "--"          # em dash to double hyphen
  $content = $content -replace "\u2013", "-"           # en dash to hyphen
  $content = $content -replace "\u00D7", "x"           # multiplication sign to 'x'
  $content = $content -replace "\u00A0", " "           # non-breaking space to normal space

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
