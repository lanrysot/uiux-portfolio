import os

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "Motion Graphics Designer | 2D & 3D Animation": "UI/UX Designer | Product Design",
    'content=" motion graphics designer helping SaaS, Fintech and AI brands with 2D & 3D animation, explainer videos and brand motion across Nigeria and Africa."': 'content="UI/UX Designer helping SaaS, Fintech and AI brands with intuitive product design and engaging user experiences across Nigeria and Africa."',
    'content="motion graphics designer, motion graphics designer Nigeria, motion graphics designer Africa, 2D animation, 3D animation, explainer videos, brand motion design, SaaS animation, Fintech animation, AI animation"': 'content="UI/UX designer, product designer, UX research, UI design, Figma, SaaS design, Fintech design, AI product design"',
    "Motion Graphics Designer": "UI/UX Designer",
    "Motion graphics designer": "UI/UX designer",
    "Motion Graphics Designer & Creative Director": "UI/UX Designer & Product Designer",
    "Creative Director · Motion Designer": "UI/UX Designer · Product Designer",
    "Motion Designer · Creative Director": "UI/UX Designer · Product Designer",
    "I create motion graphics <br>that convert for brands.": "I design digital products <br>that convert and engage.",
    "I specialize in creating <strong>2D &amp; 3D animations</strong>": "I specialize in creating <strong>intuitive UI/UX designs</strong>",
    "<span>After Effects</span>\n                            <span>Alight Motion</span>": "<span>Figma</span>\n                            <span>Prototyping</span>",
    "World-class 2D & 3D animation": "World-class UI/UX design",
    "A  motion graphics business creating 2D & 3D animation, explainer videos, and brand motion": "A UI/UX design business creating digital products, web apps, and mobile experiences",
    "2025 Motion<br>Design Showreel": "Featured Case Study<br>Quicken",
    "Three minutes. Every style. This is what 60+ projects of\n                relentless\n                craft looks like distilled into a single reel.": "A modern financial management platform that simplifies personal and business finance.",
    "Watch Showreel": "View Case Study",
    "Showreel": "Case Studies",
    "Every type of video<br>your brand needs.": "Every type of digital product<br>your brand needs.",
    "What I Do": "My Expertise",
    "From first concept to final frame, I handle everything. No chasing, no confusion, just clean, strategic animation that does exactly what you need it to do.": "From research to high-fidelity prototypes, I handle everything. No chasing, no confusion, just clean, strategic design that solves user problems.",
    "Explainer Videos": "User Research",
    "Got a product that's hard to explain? I break it down into a clear, visual story your audience gets immediately — and actually remembers.": "Understanding user behaviors, needs, and motivations through observation techniques, task analysis, and other feedback methodologies.",
    "Product Demos": "Wireframing",
    "Show your product in its best light. Animated demos that highlight the value, guide the eye, and make buying feel obvious.": "Creating structural blueprints that outline the skeleton of your digital product, focusing on space allocation and content prioritization.",
    "UI/UX Animations": "High-Fidelity Prototyping",
    "Bring your app's interface to life. Smooth, purposeful micro-animations that make your product feel premium and completely intuitive.": "Building interactive, clickable prototypes in Figma that look and function exactly like the final product for testing and developer handoff.",
    "Promotional Videos": "Design Systems",
    "Launch campaigns, product announcements, brand stories — crafted to stop thumbs mid-scroll and turn viewers into paying customers.": "Creating robust, scalable component libraries and documentation to ensure visual consistency across all touchpoints.",
    "2D &amp; 3D Animation": "Web Application Design",
    "Whether flat and punchy or dimensional and cinematic, I work in both worlds — and know exactly which style fits your message best.": "Designing complex, data-heavy dashboards and SaaS applications with a focus on simplicity and ease of use.",
    "Brand Motion Design": "Mobile App Design",
    "Logos, intros, lower thirds, branded assets — the visual language that makes your brand feel cohesive and polished everywhere it shows up.": "Crafting intuitive, platform-specific mobile experiences for iOS and Android that users love to engage with.",
    "Visual Language": "Design Approach",
    "Popular SAAS<br>Animation Style": "Modern Product<br>Design Styles"
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Let's handle the video embed replacement separately
video_html = """<script src="https://fast.wistia.com/player.js" async=""></script>
                    <script src="https://fast.wistia.com/embed/v8chvf17mi.js" async="" type="module"></script>
                    <style>
                        wistia-player[media-id='v8chvf17mi']:not(:defined) {
                            background: center / contain no-repeat url('https://fast.wistia.com/embed/medias/v8chvf17mi/swatch');
                            display: block;
                            filter: blur(5px);
                            padding-top: 56.25%;
                        }
                    </style>
                    <wistia-player media-id="v8chvf17mi" aspect="1.7777777777777777"
                        unique-id="wistia-v8chvf17mi-16"></wistia-player>"""

case_study_html = """<a href="quicken-case-study.html" style="display: block; width: 100%; aspect-ratio: 16/9; border-radius: 20px; overflow: hidden; position: relative;">
                        <img src="quicken-preview.jpg" alt="Quicken Case Study" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 30px; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: white;">
                            <h3 style="font-size: 24px; font-weight: 600; margin-bottom: 8px;">Quicken Financial Platform</h3>
                            <p style="font-size: 16px; opacity: 0.8;">Click to view full case study</p>
                        </div>
                    </a>"""

content = content.replace(video_html, case_study_html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Replacement complete.")
