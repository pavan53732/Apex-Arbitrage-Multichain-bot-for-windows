# Complete fix for prompt corruption - removes ALL duplicate content
$promptsDir = "C:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"
$files = Get-ChildItem -Path $promptsDir -Filter "prompt-*.md" | Sort-Object Name

$fixedCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Check if file is corrupted (contains duplicate "You are an expert" text)
    $matches = [regex]::Matches($content, "You are an expert Windows software architect")
    
    if ($matches.Count -gt 1) {
        # File is corrupted - extract only the first occurrence
        $firstMatch = $matches[0].Index
        $validContent = $content.Substring(0, $firstMatch + 50000)  # Keep first ~50K chars which should be the valid prompt
        
        # Find the actual end of the prompt (POST-EXECUTION CHECKPOINT section)
        if ($validContent -match '(?s)(.*\*\*Mark this prompt as COMPLETE\.\*\*\s*\r?\n\s*---\s*\r?\n)') {
            $cleanContent = $Matches[1]
            Set-Content -Path $file.FullName -Value $cleanContent -NoNewline
            $fixedCount++
        }
    }
}

Write-Host "Fixed $fixedCount corrupted prompt files"
