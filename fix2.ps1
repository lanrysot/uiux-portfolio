$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $html = Get-Content $file.FullName -Raw -Encoding UTF8
    $html = $html.Replace('â€”', '—')
    $html = $html.Replace('â†’', '→')
    $html = $html.Replace('â€™', "'")
    $html = $html.Replace('â­ ', '⭐')
    $html = $html.Replace('Â·', '·')
    $html = $html.Replace('Â©', '©')
    Set-Content -Path $file.FullName -Value $html -Encoding UTF8
}
git add *.html
git commit -m "Fix mojibake globally (take 3)"
git push origin main
