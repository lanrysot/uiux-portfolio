import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will find the whole .srv-grid block and replace it entirely with the corrected one.
# It starts at <div class="srv-grid"> and ends before </div>\n            </div>\n        </div>\n    </section>\n\n    <!-- -- HOW I WORK
pattern = re.compile(r'<div class="srv-grid">.*?</div>\n            </div>\n        </div>\n    </section>\n\n    <!-- -- HOW I WORK', re.DOTALL)

# Let's verify we found it
match = pattern.search(html)
if match:
    pass
else:
    print("Could not find srv-grid block")

new_srv_grid = '''<div class="srv-grid">
                    <a href="./technology.html" class="sc rv d1" style="text-decoration: none; color: inherit; display: block;">
                        <span class="snum">01</span>
                        <div class="sc-thumb" style="background-image: url('./centa-hero-mockup.png'); background-size: cover; background-position: center;">
                            <div class="sc-overlay">
                                <div class="sc-view-btn">CLICK TO SEE MORE PROJECT <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
                            </div>
                        </div>
                        <p class="sn">Technology &amp; Digital</p>
                        <p class="sd">Explore case studies and innovative design solutions for the technology and digital sector.</p>
                    </a>
                    
                    <a href="./business.html" class="sc rv d2" style="text-decoration: none; color: inherit; display: block;">
                        <span class="snum">02</span>
                        <div class="sc-thumb" style="background-image: url('./cs-imac-mockup.png'); background-size: cover; background-position: center;">
                            <div class="sc-overlay">
                                <div class="sc-view-btn">CLICK TO SEE MORE PROJECT <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
                            </div>
                        </div>
                        <p class="sn">Business &amp; Enterprise</p>
                        <p class="sd">View comprehensive enterprise platforms and B2B solutions designed for scale.</p>
                    </a>
                    
                    <a href="./finance.html" class="sc rv d3" style="text-decoration: none; color: inherit; display: block;">
                        <span class="snum">03</span>
                        <div class="sc-thumb" style="background-image: url('./quicken-preview-v2.jpg'); background-size: cover; background-position: center;">
                            <div class="sc-overlay">
                                <div class="sc-view-btn">CLICK TO SEE MORE PROJECT <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
                            </div>
                        </div>
                        <p class="sn">Financial Services</p>
                        <p class="sd">Discover secure, intuitive, and modern interfaces for fintech and banking products.</p>
                    </a>
                    
                    <a href="./healthcare.html" class="sc rv d4" style="text-decoration: none; color: inherit; display: block;">
                        <span class="snum">04</span>
                        <div class="sc-thumb" style="background-image: url('./cs-before-after.png'); background-size: cover; background-position: center;">
                            <div class="sc-overlay">
                                <div class="sc-view-btn">CLICK TO SEE MORE PROJECT <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
                            </div>
                        </div>
                        <p class="sn">Healthcare</p>
                        <p class="sd">Explore accessible and user-friendly digital experiences crafted for healthcare providers.</p>
                    </a>
                    
                    <a href="./security.html" class="sc rv d5" style="text-decoration: none; color: inherit; display: block;">
                        <span class="snum">05</span>
                        <div class="sc-thumb" style="background-image: url('./centa-design-system.png'); background-size: cover; background-position: center;">
                            <div class="sc-overlay">
                                <div class="sc-view-btn">CLICK TO SEE MORE PROJECT <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
                            </div>
                        </div>
                        <p class="sn">Security &amp; Infrastructure</p>
                        <p class="sd">View complex infrastructure systems translated into clear, actionable dashboards.</p>
                    </a>
                    
                    <a href="./commerce.html" class="sc rv d6" style="text-decoration: none; color: inherit; display: block;">
                        <span class="snum">06</span>
                        <div class="sc-thumb" style="background-image: url('./cs-research-insights.png'); background-size: cover; background-position: center;">
                            <div class="sc-overlay">
                                <div class="sc-view-btn">CLICK TO SEE MORE PROJECT <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7" /></svg></div>
                            </div>
                        </div>
                        <p class="sn">Commerce &amp; Consumer</p>
                        <p class="sd">Discover engaging e-commerce platforms and consumer apps optimized for conversion.</p>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- -- HOW I WORK'''

html = pattern.sub(new_srv_grid, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html categories.")
