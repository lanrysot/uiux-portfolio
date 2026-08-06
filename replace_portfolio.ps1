$c = Get-Content -Path "portfolio.html" -Raw

$c = $c -replace "Motion Graphics Designer \| 2D & 3D Animation", "UI/UX Designer | Product Design"
$c = $c -replace "motion graphics designer helping SaaS", "UI/UX Designer helping SaaS"
$c = $c -replace "Motion Graphics Designer", "UI/UX Designer"
$c = $c -replace "motion graphics designer", "UI/UX designer"
$c = $c -replace "Creative Director · Motion Designer", "UI/UX Designer · Product Designer"
$c = $c -replace "Motion Designer · Creative Director", "UI/UX Designer · Product Designer"
$c = $c -replace "I create motion graphics <br>that convert for brands.", "I design digital products <br>that convert and engage."
$c = $c -replace "2D &amp; 3D animations", "intuitive UI/UX designs"
$c = $c -replace "<span>After Effects</span>\s*<span>Alight Motion</span>", "<span>Figma</span><span>Prototyping</span>"
$c = $c -replace "World-class 2D & 3D animation", "World-class UI/UX design"

Set-Content -Path "portfolio.html" -Value $c -Encoding UTF8
Write-Output "Done"
