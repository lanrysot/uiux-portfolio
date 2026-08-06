$c = Get-Content -Path "index.html" -Raw

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
$c = $c -replace "2025 Motion<br>Design Showreel", "Featured Case Study<br>Quicken"
$c = $c -replace "Three minutes\. Every style\. This is what 60\+ projects of\s*relentless\s*craft looks like distilled into a single reel\.", "A modern financial management platform that simplifies personal and business finance."
$c = $c -replace "Watch Showreel", "View Case Study"
$c = $c -replace "Showreel", "Case Studies"
$c = $c -replace "Every type of video<br>your brand needs\.", "Every type of digital product<br>your brand needs."

$video = '(?s)<script src="https://fast\.wistia\.com/player\.js".*?<wistia-player[^>]*></wistia-player>'
$caseStudy = '<a href="quicken-case-study.html" style="display: block; width: 100%; aspect-ratio: 16/9; border-radius: 20px; overflow: hidden; position: relative;"><img src="quicken-preview.jpg" alt="Quicken Case Study" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"><div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 30px; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: white;"><h3 style="font-size: 24px; font-weight: 600; margin-bottom: 8px;">Quicken Financial Platform</h3><p style="font-size: 16px; opacity: 0.8;">Click to view full case study</p></div></a>'
$c = $c -replace $video, $caseStudy

Set-Content -Path "index.html" -Value $c -Encoding UTF8
Write-Output "Done"
