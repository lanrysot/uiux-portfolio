$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    $content = $content.Replace('â†’', '→')
    $content = $content.Replace('â€”', '—')
    $content = $content.Replace('â€™', "'")
    $content = $content.Replace('â­ ', '⭐')
    $content = $content.Replace('â€"', '–')
    $content = $content.Replace('Â·', '·')
    
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}
git add *.html
git commit -m "Fix mojibake encoding issues"
git push origin main
