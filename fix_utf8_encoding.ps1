# Fix corrupted UTF-8 characters in all 842 prompts
# Replaces corrupted emoji characters with proper UTF-8 symbols

Write-Host "🚀 Starting UTF-8 encoding fix for all prompts..." -ForegroundColor Green

# Get all prompt files
$promptFiles = Get-ChildItem "generated-prompts" -Filter "prompt-*.md"
if ($promptFiles.Count -eq 0) {
    Write-Host "❌ No prompt files found!" -ForegroundColor Red
    exit 1
}

Write-Host "🔍 Found $($promptFiles.Count) prompt files to process..." -ForegroundColor Yellow

# Create backup directory
$backupDir = "backup_utf8_fix"
if (!(Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir | Out-Null
}

$fixedCount = 0
$totalReplacements = 0

foreach ($file in $promptFiles) {
    try {
        # Read file content
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        $originalContent = $content
        $replacementsMade = 0
        
        # Fix corrupted characters
        # Warning siren emoji
        if ($content -match "ðŸš¨") {
            $count = ($content | Select-String "ðŸš¨" -AllMatches).Matches.Count
            $content = $content -replace "ðŸš¨", "🚨"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'ðŸš¨' → '🚨'" -ForegroundColor Green
        }
        
        # Warning sign emoji
        if ($content -match "âš ï¸") {
            $count = ($content | Select-String "âš ï¸" -AllMatches).Matches.Count
            $content = $content -replace "âš ï¸", "⚠️"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'âš ï¸' → '⚠️'" -ForegroundColor Green
        }
        
        # Arrow symbol
        if ($content -match "â†'") {
            $count = ($content | Select-String "â†'" -AllMatches).Matches.Count
            $content = $content -replace "â†'", "→"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â†'' → '→'" -ForegroundColor Green
        }
        
        # Dash symbols
        if ($content -match "â€"") {
            $count = ($content | Select-String "â€"" -AllMatches).Matches.Count
            $content = $content -replace "â€"", "—"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€"' → '—'" -ForegroundColor Green
        }
        
        if ($content -match "â€"") {
            $count = ($content | Select-String "â€"" -AllMatches).Matches.Count
            $content = $content -replace "â€"", "–"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€"' → '–'" -ForegroundColor Green
        }
        
        # Quote symbols
        if ($content -match "â€™") {
            $count = ($content | Select-String "â€™" -AllMatches).Matches.Count
            $content = $content -replace "â€™", "'"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€™' → '''" -ForegroundColor Green
        }
        
        if ($content -match "â€œ") {
            $count = ($content | Select-String "â€œ" -AllMatches).Matches.Count
            $content = $content -replace "â€œ", '"'
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€œ' → '"'" -ForegroundColor Green
        }
        
        if ($content -match "â€") {
            $count = ($content | Select-String "â€" -AllMatches).Matches.Count
            $content = $content -replace "â€", '"'
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€' → '"'" -ForegroundColor Green
        }
        
        # Bullet and ellipsis
        if ($content -match "â€¢") {
            $count = ($content | Select-String "â€¢" -AllMatches).Matches.Count
            $content = $content -replace "â€¢", "•"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€¢' → '•'" -ForegroundColor Green
        }
        
        if ($content -match "â€¦") {
            $count = ($content | Select-String "â€¦" -AllMatches).Matches.Count
            $content = $content -replace "â€¦", "…"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€¦' → '…'" -ForegroundColor Green
        }
        
        # Dagger symbols
        if ($content -match "â€¡") {
            $count = ($content | Select-String "â€¡" -AllMatches).Matches.Count
            $content = $content -replace "â€¡", "‡"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€¡' → '‡'" -ForegroundColor Green
        }
        
        if ($content -match "â€ ") {
            $count = ($content | Select-String "â€ " -AllMatches).Matches.Count
            $content = $content -replace "â€ ", "†"
            $replacementsMade += $count
            Write-Host "  ✅ $($file.Name): Replaced $count instances of 'â€ ' → '†'" -ForegroundColor Green
        }
        
        # Only write if changes were made
        if ($content -ne $originalContent) {
            # Create backup
            $backupFile = Join-Path $backupDir "$($file.Name).backup"
            Copy-Item $file.FullName $backupFile
            
            # Write fixed content
            $content | Out-File -FilePath $file.FullName -Encoding UTF8 -NoNewline
            
            $fixedCount++
            $totalReplacements += $replacementsMade
            Write-Host "  📝 $($file.Name): $replacementsMade replacements made" -ForegroundColor Cyan
        } else {
            Write-Host "  ⏭️  $($file.Name): No UTF-8 issues found" -ForegroundColor Gray
        }
        
    } catch {
        Write-Host "  ❌ Error processing $($file.Name): $($_.Exception.Message)" -ForegroundColor Red
        continue
    }
}

Write-Host "`n🎉 UTF-8 Fix Complete!" -ForegroundColor Green
Write-Host "📊 Files processed: $($promptFiles.Count)" -ForegroundColor Yellow
Write-Host "📊 Files fixed: $fixedCount" -ForegroundColor Yellow
Write-Host "📊 Total replacements: $totalReplacements" -ForegroundColor Yellow
Write-Host "💾 Backups saved to: $backupDir" -ForegroundColor Yellow
