$root = 'C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot\Apex Arbitrage Multichain bot'
$items = @('.devcontainer','.github','.husky','.vscode','ai-modules','archive','backend','benchmarks','ci','config','dashboard','data','deploy','docs','examples','logs','manifest','migrations','overlays','presets','public','research','scripts','storage','tests','third-party','types','utils','vendor','wall-of-fame','watchdog')

Write-Output "=== COMPLETE RECURSIVE ANALYSIS (INCLUDING ALL FOLDERS) ==="
Write-Output ""

$totalFolders = 0
$totalFiles = 0

foreach ($i in $items) {
  $p = Join-Path $root $i
  if (Test-Path -LiteralPath $p) {
    # Count the top-level folder itself
    $folderCount = 1
    
    # Count all nested folders and files
    $allFolders = @(Get-ChildItem -LiteralPath $p -Directory -Recurse -Force -ErrorAction SilentlyContinue)
    $allFiles = @(Get-ChildItem -LiteralPath $p -File -Recurse -Force -ErrorAction SilentlyContinue)
    
    $folderCount += $allFolders.Count
    $fileCount = $allFiles.Count
    
    # Calculate maximum nesting depth
    $maxDepth = 0
    if ($allFolders.Count -gt 0) {
      foreach ($folder in $allFolders) {
        $relativePath = $folder.FullName.Substring($p.Length)
        $depth = ($relativePath.Split('\') | Where-Object { $_ -ne '' }).Count
        if ($depth -gt $maxDepth) { $maxDepth = $depth }
      }
    }
    
    $totalFolders += $folderCount
    $totalFiles += $fileCount
    
    Write-Output ("- {0}/------{1} FOLDERS - {2} FILES (Max Depth: {3})" -f $i, $folderCount, $fileCount, $maxDepth)
  } else {
    # Silently skip missing folders
  }
}

Write-Output ""
Write-Output "=== PROJECT TOTALS ==="
Write-Output ("TOTAL FOLDERS: {0}" -f $totalFolders)
Write-Output ("TOTAL FILES: {0}" -f $totalFiles)
Write-Output ("GRAND TOTAL: {0}" -f ($totalFolders + $totalFiles))
