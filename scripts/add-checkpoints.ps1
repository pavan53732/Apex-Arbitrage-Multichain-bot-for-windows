# Add progress checkpoints to all 842 prompts
$promptsDir = "c:\Users\Pavan pc\Desktop\Apex Arbitrage Multichain bot for windows\Apex-Arbitrage-Multichain-bot-for-windows\generated-prompts"

$topCheckpoint = @'

---
## PRE-EXECUTION CHECKPOINT

**Before proceeding, check progress tracking:**

1. Read `generated-prompts/progress.md`
2. Search for "Prompt {0}: Executed" in the Execution Log
3. **If found**: STOP - This prompt already completed. Move to next prompt.
4. **If not found**: Proceed with execution below.

---

'@

$bottomCheckpoint = @'

---
## POST-EXECUTION CHECKPOINT

**After completing all tasks above, update progress tracking:**

1. Open `generated-prompts/progress.md`
2. Increment "Completed" counter (X/842 -> X+1/842)
3. Update "Last Updated" to today's date
4. Update "Recent Completions" to: Prompt {0} (Feature: [Feature Name])
5. Append to Execution Log:
   ```
   Prompt {0}: Executed - Added 'Feature: [Feature Name]' to features/[owner].md
   ```
6. Save progress.md before moving to next prompt

**Mark this prompt as COMPLETE.**

---
'@

Get-ChildItem "$promptsDir\prompt-*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    
    if ($_.Name -match 'prompt-(\d+)') {
        $promptNum = $1
        
        if ($content -notmatch "PRE-EXECUTION CHECKPOINT" -and $content -notmatch "POST-EXECUTION CHECKPOINT") {
            
            $topInsert = $topCheckpoint -f $promptNum
            $content = $content -replace '(\*\*FAILURE TO FOLLOW THIS PROTOCOL IS FORBIDDEN\*\*: Never create documentation without reading source files first\.)', "`$1$topInsert"
            
            $bottomInsert = $bottomCheckpoint -f $promptNum, $promptNum
            $content = $content.TrimEnd() + "`r`n$bottomInsert"
            
            Set-Content -Path $_.FullName -Value $content -Encoding UTF8 -NoNewline
            Write-Host "Updated $($_.Name)" -ForegroundColor Green
        } else {
            Write-Host "Skipped $($_.Name)" -ForegroundColor Yellow
        }
    }
}

Write-Host "Done!" -ForegroundColor Cyan
