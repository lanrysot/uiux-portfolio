import re

with open('pulsehealth-case-study.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacement = '''<div class="case-study-container">
        <div class="cs-header">
            <h1 class="cs-title">PulseHealth</h1>
            <p class="cs-subtitle">Simplifying healthcare operations, one workflow at a time.<br><br>PulseHealth is a healthcare management platform designed to bring the everyday operations of a medical practice into one connected experience, from appointments and patient records to medical history, imaging, prescriptions, and payments.</p>
        </div>

        <img src="pulsehealth-hero.jpg" alt="PulseHealth Hero Image" class="cs-image">

        <div class="cs-meta" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
            <div class="meta-item">
                <h4>Role</h4>
                <p>Product Design &bull; UX Strategy &bull; UI Design &bull; Interaction Design &bull; Prototyping</p>
            </div>
            <div class="meta-item">
                <h4>Platform</h4>
                <p>Web Application</p>
            </div>
        </div>

        <div class="cs-content">
            <div class="cs-section">
                <h2>The Challenge</h2>
                <p>Healthcare professionals operate across a wide range of clinical and administrative tasks, often moving between appointments, patient information, medical records, prescriptions, payments, and follow-ups. When these workflows feel disconnected, valuable time is spent navigating the system rather than focusing on patient care.</p>
                <p>We saw an opportunity to bring these critical touchpoints together through a single, structured workspace, one that gives practitioners a clear view of their day while keeping deeper patient and operational information within easy reach.</p>
                <p>The challenge was less about adding functionality and more about creating clarity across complexity. PulseHealth needed to make high-frequency tasks easy to find, quick to complete, and simple to revisit without overwhelming the practitioner.</p>
                <p>We therefore centred the experience around three principles: visibility, speed, and continuity. These shaped the product architecture - from the dashboard and calendar experience to patient profiles, medical records, payments, and notifications - creating a more connected way to manage the practice.</p>
                <img src="pulsehealth-challenge.png" alt="From Fragmented to Focused" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Research &amp; Strategy</h2>
                <p>We approached the discovery phase by looking at how healthcare professionals manage the operational demands of a busy practice, from appointments and patient information to payments, follow-ups, and day-to-day clinical activity.</p>
                <p>Through 12 practitioner interviews, a short survey, and competitive analysis, we identified three themes that shaped the product direction.</p>
                
                <h4 style="margin-top: 20px; color:#fff;">01. Make the day immediately visible</h4>
                <p>Practitioners need to understand what requires their attention without moving across multiple parts of the product. Appointments, patient activity, outstanding payments, and important updates therefore needed to be visible at a glance.</p>
                
                <h4 style="margin-top: 20px; color:#fff;">02. Connect clinical and operational workflows</h4>
                <p>Scheduling a patient, reviewing their history, documenting care, and following up are not separate activities. We treated them as connected moments within the same practitioner journey.</p>
                
                <h4 style="margin-top: 20px; color:#fff;">03. Keep actions close to context</h4>
                <p>We reduced unnecessary navigation by placing relevant actions where decisions happen, whether that means adding an appointment, viewing patient details, sending a reminder, or managing a prescription.</p>
                
                <h3 style="margin-top: 30px; margin-bottom: 15px; color:#fff;">Design Principles</h3>
                <p>These insights led to a simple experience model:<br>
                <strong>See the day. Find the patient. Take action. Stay informed.</strong><br>
                This became the foundation for the dashboard, scheduling, patient management, clinical records, payments, and notification experiences, giving PulseHealth a consistent structure across the product.</p>
                <img src="pulsehealth-research.png" alt="Research and Strategy" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Designing the Experience</h2>
                <p>We structured PulseHealth around the way practitioners move through their day. The experience makes it easy to understand what needs attention, find the right patient, complete an action, and stay informed.</p>
                <p>The information architecture brings the core workflows into the primary navigation: Dashboard, Schedule, Patients, Medical Records, Prescriptions, Payments, Reports, Notifications, and Settings. This creates a clear foundation while keeping each area focused on its specific task.</p>

                <h4 style="margin-top: 20px; color:#fff;">01. Start with the day</h4>
                <p>The dashboard serves as the operational starting point. Rather than presenting isolated features, it brings patient volume, appointments, new patients, visit duration, today's schedule, patient activity, and unpaid bills into a single view.</p>

                <h4 style="margin-top: 20px; color:#fff;">02. Move naturally into patient care</h4>
                <p>We connected patient information with the clinical context around it. Practitioners can move between patient details, medical history, appointments, prescriptions, and related records without having to reconstruct the patient's story across separate areas of the product.</p>

                <h4 style="margin-top: 20px; color:#fff;">03. Keep actions close to context</h4>
                <p>Key actions are placed where they are most relevant, including adding appointments, viewing patient details, managing prescriptions, recording medical information, and handling payments. This reduces unnecessary navigation and keeps the experience focused on the task at hand.</p>

                <h4 style="margin-top: 20px; color:#fff;">04. Design the system, not isolated screens</h4>
                <p>Rather than designing each screen as an individual experience, we treated PulseHealth as one connected system. Scheduling connects to patient management, patient information connects to clinical records, and operational activity connects to payments and notifications.</p>
                
                <p>The result is an experience where each part of the product supports the next, creating a more coherent workflow from managing the day to managing patient care.</p>
                <img src="pulsehealth-design.png" alt="Designing the Experience" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Challenges &amp; Trade-offs</h2>
                <p>Designing PulseHealth required us to find the right balance between depth and simplicity. The platform brings together appointments, patient records, prescriptions, payments, reports, notifications, and account settings, so the challenge was to make the breadth of the product feel manageable. We addressed this through persistent navigation, clear workflow separation, and consistent interaction patterns across the experience.</p>
                
                <h4 style="margin-top: 20px; color:#fff;">01. Balancing depth with simplicity</h4>
                <p>The product needed to support complex healthcare workflows without making everyday tasks feel complicated. We separated the major workflows while maintaining a consistent structure, allowing practitioners to move between them without having to relearn the interface.</p>
                
                <h4 style="margin-top: 20px; color:#fff;">02. Preserving clinical context</h4>
                <p>Patient information spans medical history, diagnoses, notes, prescriptions, billing, and supporting documents. Rather than scattering this information across disconnected areas, we used the patient profile as a contextual anchor, giving practitioners a clearer view of the information surrounding each patient.</p>
                
                <h4 style="margin-top: 20px; color:#fff;">03. Building trust into the experience</h4>
                <p>Security and account management were treated as part of the core product experience. The designs incorporate password management, two-step verification, session and device visibility, notifications, and account controls, giving practitioners greater visibility and control over how their account is managed.</p>
                
                <p>Ultimately, the trade-off was not between functionality and simplicity. It was about creating enough structure for a complex product to feel simple to use.</p>

                <h3 style="margin-top: 30px; margin-bottom: 15px; color:#fff;">Key Trade-offs</h3>
                <ul style="color: #aaa; margin-left: 20px;">
                    <li><strong>Feature depth vs simplicity:</strong> Group workflows into focused modules</li>
                    <li><strong>Speed vs security:</strong> Keep security controls accessible without disrupting daily tasks</li>
                    <li><strong>Flexibility vs consistency:</strong> Reuse patterns across scheduling, patients, billing, and records</li>
                    <li><strong>Information density vs clarity:</strong> Prioritise hierarchy, summaries, filters, and progressive detail</li>
                </ul>
                <img src="pulsehealth-tradeoffs.png" alt="Challenges and Trade-offs" class="cs-image">
            </div>

            <div class="cs-section">
                <h2>Outcome &amp; Reflection</h2>
                <p>PulseHealth's final direction brings a broad set of healthcare workflows into one connected operating experience. The dashboard provides a clear starting point, while scheduling, patient management, medical records, prescriptions, payments, reports, and notifications work together as parts of the same system.</p>
                <p>The strongest outcome is continuity. Practitioners can move from their daily overview into a schedule, open a patient, review relevant clinical information, take action, and return to the wider practice context without losing their place.</p>
                <p>For a live product, we would evaluate the experience through measures such as task completion time, appointment-management efficiency, patient-record retrieval, missed follow-ups, payment collection, and feature adoption. These would provide a clearer picture of whether the product is reducing friction across the workflows it was designed to support.</p>
                
                <h3 style="margin-top: 30px; margin-bottom: 15px; color:#fff;">What We Learned</h3>
                <p>The project reinforced a simple principle: complex products do not necessarily need less functionality. They need better structure.</p>
                <p>The biggest design opportunity was deciding what practitioners needed to see immediately, what could sit deeper within the experience, and how individual workflows could remain connected without creating unnecessary complexity.</p>
                <p>For PulseHealth, that meant designing beyond individual screens and creating a system that gives practitioners clarity, context, and control throughout the day.</p>
            </div>
        </div>
    </div>'''

new_html = re.sub(r'<div class="case-study-container">.*?</div>\s*(<!-- NAV|</div>|</body>)', replacement + r'\n\n    \1', html, flags=re.DOTALL)

with open('pulsehealth-case-study.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

