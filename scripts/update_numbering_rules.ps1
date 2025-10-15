param(
  [string]$Root = "C:\\Users\\Pavan pc\\Desktop\\Apex Arbitrage Multichain bot for windows\\Apex-Arbitrage-Multichain-bot-for-windows\\generated-prompts",
  [int]$StartIndex = 0,
  [int]$Count = -1,
  [int]$ProgressEvery = 50
)

$ErrorActionPreference = 'Stop'

$rulesBlock = @"
**Numbering Rules (STRICT):**
- Per-level reset: Each folder level restarts numbering at 1 for its immediate children (e.g., 1/3, 2/3, 3/3). Do NOT carry numbers across different parent folders.
- Separate sequences: Folder numbering and file numbering are independent. Do NOT interleave or share counters between folders and files.
- Folder totals (Y): Count ONLY sibling folders at that level (exclude files). Example: If a folder has 3 subfolders and 5 files, folder Y = 3.
- File totals (Y): Count ONLY files within that single folder (exclude subfolders). Example: If a folder has 7 files and 2 subfolders, file Y = 7.
- Sequential within scope: Files in a folder must be numbered FILE 1/Y, 2/Y, …, Y/Y; subfolders at a level must be FOLDER 1/Y, 2/Y, …, Y/Y.
- Example clarity: Use 1/3 then 1/2 for a child level, NOT 1/3 then 4/5. Each level resets.
- Deterministic ordering: At every folder level, list all subfolders first (sorted A->Z), then list all files (sorted A->Z) before descending into deeper levels.
- Exact counts: Compute Y from actual discovered items at that level; never guess or reuse counts from other levels.
"@

$updated = 0
$allFiles = Get-ChildItem -Path $Root -Filter 'prompt-*.md' -File -Recurse | Sort-Object FullName
$total = $allFiles.Count
if ($Count -lt 0) { $Count = [Math]::Max(0, $total - $StartIndex) }
$files = $allFiles | Select-Object -Skip $StartIndex -First $Count
Write-Host "Processing prompts $StartIndex to $([Math]::Min($StartIndex+$Count-1,$total-1)) of $total..."
$i = 0

foreach ($f in $files) {
  $i++
  $content = Get-Content -Raw -Encoding UTF8 -Path $f.FullName
  $original = $content

  # Insert strict rules after File Format -> before **Example:** if not present
  if ($content -notmatch '\*\*Numbering Rules \(STRICT\):\*\*') {
    $pattern1 = '(?s)(\*\*File Format:\*\* `FILE X/Y: filename\.ext` where X = current, Y = total\s*)(\r?\n)(\s*)(\r?\n)?(\*\*Example:\*\*)'
    $replacement1 = "$1`r`n$rulesBlock`r`n`r`n$5"
    $newContent = [regex]::Replace($content, $pattern1, $replacement1, 1)
    if ($newContent -ne $content) { $content = $newContent }

    # Secondary anchor: inject after NUMBERING EXAMPLES code block if present
    if ($content -notmatch '\\*\\*Numbering Rules \\(STRICT\\):\\*\\*') {
      $pattern1b = '(?ms)(^\s*####\s*NUMBERING EXAMPLES\s*\r?\n[\s\S]*?^\s*`\s*\r?\n)([\s\S]*?)(?=^\s*####\s*CRITICAL REQUIREMENTS)'
      $replacement1b = "$1$rulesBlock`r`n"
      $newContent = [regex]::Replace($content, $pattern1b, $replacement1b, 1)
      if ($newContent -ne $content) { $content = $newContent }
    }
  }

  # Fallback: If a '####  NUMBERING RULES' subsection exists, replace its bullets with strict ones
  if ($content -notmatch 'Per-level reset: Each folder level restarts numbering at 1 for its immediate children') {
    $patternNR = '(?ms)(^\s*####\s*NUMBERING RULES\s*\r?\n)(.*?)(?=^\s*####\s|^\s*\*\*ULTRA-MANDATORY RULES:\*\*|\Z)'
    $replacementNR = "$1- Per-level reset: Each folder level restarts numbering at 1 for its immediate children (e.g., 1/3, 2/3, 3/3). Do NOT carry numbers across different parent folders.`r`n- Separate sequences: Folder numbering and file numbering are independent. Do NOT interleave or share counters between folders and files.`r`n- Folder totals (Y): Count ONLY sibling folders at that level (exclude files). Example: If a folder has 3 subfolders and 5 files, folder Y = 3.`r`n- File totals (Y): Count ONLY files within that single folder (exclude subfolders). Example: If a folder has 7 files and 2 subfolders, file Y = 7.`r`n- Sequential within scope: Files in a folder must be numbered FILE 1/Y, 2/Y, …, Y/Y; subfolders at a level must be FOLDER 1/Y, 2/Y, …, Y/Y.`r`n- Example clarity: Use 1/3 then 1/2 for a child level, NOT 1/3 then 4/5. Each level resets.`r`n- Deterministic ordering: At every folder level, list all subfolders first (sorted A->Z), then list all files (sorted A->Z) before descending into deeper levels.`r`n- Exact counts: Compute Y from actual discovered items at that level; never guess or reuse counts from other levels.`r`n"
    $newContent = [regex]::Replace($content, $patternNR, $replacementNR, 1)
    if ($newContent -ne $content) { $content = $newContent }
  }

  # Add enforcement bullet under ULTRA-MANDATORY RULES if missing (with header fallback)
  if ($content -notmatch 'Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering \(folders first, then files\) at each level') {
    $pattern2 = '(?m)^-\s*✅\s*If PowerShell shows 54 files, your tree MUST show all 54 files\s*$'
    $replacement2 = "$0`r`n- ✅ Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering (folders first, then files) at each level"
    $newContent = [regex]::Replace($content, $pattern2, $replacement2, 1)
    if ($newContent -ne $content) {
      $content = $newContent
    } else {
      $pattern2b = '(?m)(^\*\*ULTRA-MANDATORY RULES:\*\*\s*$)'
      $replacement2b = "$1`r`n- ✅ Enforce numbering rules: per-level reset, separate folder/file counters, and deterministic A->Z ordering (folders first, then files) at each level"
      $newContent = [regex]::Replace($content, $pattern2b, $replacement2b, 1)
      if ($newContent -ne $content) { $content = $newContent }
    }
  }

  # Strengthen QUALITY STANDARDS item 9
  $pattern3 = '(?m)^9\. \*\*Complete Folder Structure\*\*: .*'
  $replacement3 = "9. **Complete Folder Structure**: Use numbered format 'FOLDER X/Y: foldername/' and 'FILE X/Y: filename.ext' for ALL folders and files; numbering resets per level, folder/file counters are separate, and ordering is folders-first then files (A->Z) at each level"
  $newContent = [regex]::Replace($content, $pattern3, $replacement3, 1)
  if ($newContent -ne $content) { $content = $newContent }

  if ($content -ne $original) {
    Set-Content -Path $f.FullName -Value $content -Encoding UTF8
    $updated++
  }

  if (($i % $ProgressEvery) -eq 0) {
    Write-Host "...processed $i / $($files.Count) in this batch; updated so far: $updated"
  }
}

Write-Host "Batch complete. Updated files in batch: $updated of $($files.Count). Total files available: $total"