$files = Get-ChildItem "generated-prompts\prompt-*.md"
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    $newContent = $content -replace '(?m)^.*Write-Host.*You are an expert Windows software architect.*$', '$files | ForEach-Object { Write-Host $_.FullName }'
    Set-Content $file.FullName $newContent
}