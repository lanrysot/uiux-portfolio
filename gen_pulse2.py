# -*- coding: utf-8 -*-
import re

with open('pulsehealth-case-study.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace title
html = html.replace('<title>Centa - CRM Sales Dashboard | Case Study</title>', '<title>PulseHealth - Healthcare Management Platform | Case Study</title>')

replacement = '''<h1 class="cs-title">PulseHealth</h1>
        <p class="cs-subtitle">Simplifying healthcare operations, one workflow at a time. A single connected workspace for appointments, records, imaging, and prescriptions.</p>

        <div class="cs-meta">
            <div class="meta-item">
                <h4>Role</h4>
                <p>Product Designer (UX/UI)</p>
            </div>
            <div class="meta-item">
                <h4>Timeline</h4>
                <p>8 Weeks</p>
            </div>
            <div class="meta-item">
                <h4>Tools</h4>
                <p>Figma, FigJam, Notion</p>
            </div>
            <div class="meta-item">
                <h4>Platform</h4>
                <p>Web Application (Responsive)</p>
            </div>
        </div>

        <img src="pulsehealth-hero.jpg" alt="PulseHealth Hero Image" class="cs-image">

        <div class="cs-content">
            <div class="cs-section">
                <h2>The Challenge</h2>
                <p>Healthcare professionals spend too much time navigating scattered tools and disconnected workflows. This leads to more time on admin tasks, higher no-shows, missed follow-ups, and lost revenue.</p>
                <img src="pulsehealth-challenge.png" alt="From Fragmented to Focused" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Research &amp; Strategy</h2>
                <p>To understand the core needs, I conducted user interviews with doctors and clinic staff. The consensus was clear: visibility drives confidence, workflows must be connected, and context is critical. The design principle became: See the day, Find the patient, Take action, and Stay informed.</p>
                <img src="pulsehealth-research.png" alt="Research and Strategy" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Designing the Experience</h2>
                <p>The experience was built around how healthcare professionals move through their day. From starting with the dashboard, to moving naturally into patient care, keeping actions close to context, and designing the system as connected workflows rather than isolated screens.</p>
                <img src="pulsehealth-design.png" alt="Designing the Experience" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Challenges &amp; Trade-offs</h2>
                <p>Balancing depth with simplicity, speed with security, and flexibility with consistency to deliver a platform that helps healthcare professionals focus on what matters most - patient care.</p>
                <img src="pulsehealth-tradeoffs.png" alt="Challenges and Trade-offs" class="cs-image">
            </div>

        </div>
</div>
'''

html = re.sub(r'<h1 class="cs-title">.*?</div>\s*</div>\s*(?=</section>|<footer)', replacement, html, flags=re.DOTALL)

with open('pulsehealth-case-study.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pulsehealth-case-study.html")
