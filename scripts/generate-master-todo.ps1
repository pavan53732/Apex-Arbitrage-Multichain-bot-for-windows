$ErrorActionPreference = 'Stop'

# Determine repo root from this script's location
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir '..')
$PromptsDir = Join-Path $RepoRoot 'generated-prompts'

if (-not (Test-Path -Path $PromptsDir)) {
    throw "Prompts directory not found: $PromptsDir"
}

# Enumerate all prompt files
$items = Get-ChildItem -Path $PromptsDir -Filter 'prompt-*.md' -File

# Parse entries: extract numeric ID and title from filename
$entries = foreach ($it in $items) {
    $m = [regex]::Match($it.Name, '^prompt-(\d{3})-(.+)\.md$')
    if ($m.Success) {
        [PSCustomObject]@{
            Id    = [int]$m.Groups[1].Value
            Title = $m.Groups[2].Value
        }
    }
}

# Sort by numeric Id then Title
$sorted = $entries | Sort-Object Id, Title
$n = $sorted.Count

# Unicode punctuation
$ndash = [char]0x2013
$mdash = [char]0x2014

# Build output lines
$lines = New-Object System.Collections.Generic.List[string]
if ($n -ne 842) {
    $lines.Add(("WARNING: Found {0} prompts, expected 842" -f $n))
}
$lines.Add(('# Master TODO {0} 842 Prompts' -f $ndash))
$lines.Add(("Total: {0} (expected 842)" -f $n))

foreach ($e in $sorted) {
    $idStr = ('{0:000}' -f $e.Id)
    $line = '- [ ] Prompt ' + $idStr + ' ' + $mdash + ' ' + $e.Title + ' ' + $mdash + ' target: features/<TBD>.md'
    $lines.Add($line)
}

$outFile = Join-Path $PromptsDir 'todo-all-prompts.md'
$lines | Set-Content -Path $outFile -Encoding UTF8

Write-Host ("Wrote {0} TODO entries to {1}" -f $n, $outFile)
