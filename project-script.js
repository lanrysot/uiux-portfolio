(function () {
      "use strict";

      /* ── CASE STUDY DATA ── */
      var PROJECTS = [        {
          cat: "Explainer", client: "Revizze",
          title: "Revizze AI-Powered Project Management Platform",
          tagline: "The video will be used on the homepage, in paid LinkedIn campaigns, and by the sales team during product demos.",
          details: [
            { title: "Project Overview", content: "Create a 90-second product launch video introducing Revizze's AI-powered project management platform. The video will be used on the homepage, in paid LinkedIn campaigns, and by the sales team during product demos." },
            { title: "The Brief", content: "Revizze was preparing for a new product launch targeting operations managers at growing companies. The goal was to clearly communicate the platform's value in under 90 seconds while positioning it as a faster, smarter alternative to manual project management tools. The video needed to work across multiple channels without requiring different edits." },
            { title: "Research", content: "I spent time understanding the product from the perspective of a first-time user, mapping the onboarding flow, key features, and most common pain points. I also reviewed competitor videos from Asana, Monday.com, ClickUp, and Notion to identify common messaging patterns and opportunities to differentiate the narrative." },
            { title: "Creative Strategy", content: "Rather than explaining every feature, I focused the story around one measurable benefit: helping teams save time every week. This became the central message, allowing every animation, transition, and UI sequence to reinforce a single outcome instead of competing for attention." },
            { title: "Script Development", content: "The script followed a simple progression: introduce the problem, highlight the frustrations of manual project management, demonstrate how Revizze solves those challenges through AI automation, and finish with a clear invitation to start a free trial." },
            { title: "Storyboard", content: "Each scene was sketched before animation began, allowing the pacing and visual hierarchy to be reviewed early. This helped validate the narrative flow before investing time in design and motion." },
            { title: "Animatic", content: "Before production, I assembled a timed animatic using storyboard frames and the approved voiceover to validate pacing, scene timing, and narrative flow. This allowed key stakeholders to review the structure and make adjustments before animation began, reducing revisions later in production." },
            { title: "Style Exploration", content: "The visual language combined clean typography, generous spacing, subtle gradients, and minimal interface design. Motion references were inspired by modern SaaS brands, emphasizing clarity over decorative animation." },
            { title: "Asset Design", content: "Product screens were recreated in Figma to ensure consistency and flexibility during animation. Supporting assets including icons, graphs, interface cards, and illustrations were designed as reusable components to maintain visual consistency throughout the project." },
            { title: "Animation", content: "Animation focused on communicating functionality rather than showcasing effects. UI interactions, cursor movements, graph animations, and smooth transitions guided the viewer through the product naturally, keeping attention on the story rather than the motion itself." },
            { title: "Sound Design", content: "Subtle interface sounds, transitions, and a modern background track reinforced the feeling of using a responsive digital product without distracting from the narration." },
            { title: "Review & Iteration", content: "Multiple review rounds refined pacing, typography, and feature prioritization. Small adjustments to timing and visual emphasis significantly improved clarity while keeping the overall runtime concise." },
            { title: "The Outcome", content: "The final video became the company's primary product explainer across marketing and sales. It was featured on the homepage, included in outbound sales presentations, and repurposed for paid social campaigns, giving the product team a consistent asset across every stage of the customer journey." }
          ],
          before: "-",
          after: "-",
          results: [{ n: "1", l: "Primary Asset" }, { n: "90s", l: "Explainer Video" }, { n: "Multi", l: "Channel Usage" }],
          tools: ["Figma", "After Effects", "Premiere Pro", "Audition"],
          video: "https://www.youtube.com/embed/Rk3NoCbwouI?si=J8BgXo0mz7732tSr"
        },
        {
          cat: "Explainer", client: "Revizze",
          title: "SaaS Platform Explainer — Turning a Complex Dashboard Into a 90-Second Story",
          tagline: "Revizze needed their platform's core value communicated clearly for an enterprise audience with zero prior product knowledge. The challenge: explain a 14-feature dashboard in under 90 seconds without dumbing it down.",
                              details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Create a 90-second product launch video introducing Revizze\'s AI-powered project management platform. The video will be used on the homepage, in paid LinkedIn campaigns, and by the sales team during product demos.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Brief', content: 'Revizze was preparing for a new product launch targeting operations managers at growing companies. The goal was to clearly communicate the platform\'s value in under 90 seconds while positioning it as a faster, smarter alternative to manual project management tools. The video needed to work across multiple channels without requiring different edits.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research', content: 'I spent time understanding the product from the perspective of a first-time user, mapping the onboarding flow, key features, and most common pain points. I also reviewed competitor videos from Asana, Monday.com, ClickUp, and Notion to identify common messaging patterns and opportunities to differentiate the narrative.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Creative Strategy', content: 'Rather than explaining every feature, I focused the story around one measurable benefit: helping teams save time every week. This became the central message, allowing every animation, transition, and UI sequence to reinforce a single outcome instead of competing for attention.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Script Development', content: 'The script followed a simple progression: introduce the problem, highlight the frustrations of manual project management, demonstrate how Revizze solves those challenges through AI automation, and finish with a clear invitation to start a free trial.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>', title: 'Storyboard', content: 'Each scene was sketched before animation began, allowing the pacing and visual hierarchy to be reviewed early. This helped validate the narrative flow before investing time in design and motion.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>', title: 'Animatic', content: 'Before production, I assembled a timed animatic using storyboard frames and the approved voiceover to validate pacing, scene timing, and narrative flow. This allowed key stakeholders to review the structure and make adjustments before animation began, reducing revisions later in production.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path></svg>', title: 'Style Exploration', content: 'The visual language combined clean typography, generous spacing, subtle gradients, and minimal interface design. Motion references were inspired by modern SaaS brands, emphasizing clarity over decorative animation.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>', title: 'Asset Design', content: 'Product screens were recreated in Figma to ensure consistency and flexibility during animation. Supporting assets including icons, graphs, interface cards, and illustrations were designed as reusable components to maintain visual consistency throughout the project.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>', title: 'Animation', content: 'Animation focused on communicating functionality rather than showcasing effects. UI interactions, cursor movements, graph animations, and smooth transitions guided the viewer through the product naturally, keeping attention on the story rather than the motion itself.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path></svg>', title: 'Sound Design', content: 'Subtle interface sounds, transitions, and a modern background track reinforced the feeling of using a responsive digital product without distracting from the narration.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path></svg>', title: 'Review & Iteration', content: 'Multiple review rounds refined pacing, typography, and feature prioritization. Small adjustments to timing and visual emphasis significantly improved clarity while keeping the overall runtime concise.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>', title: 'The Outcome', content: 'The final video became the company\'s primary product explainer across marketing and sales. It was featured on the homepage, included in outbound sales presentations, and repurposed for paid social campaigns, giving the product team a consistent asset across every stage of the customer journey.' }
          ],
          before: "Prospects visited the homepage and left without booking a demo — bounce rate was 74%. Sales reps were spending 20 minutes per call explaining the product before any real conversation started.",
          after: "Bounce rate dropped to 48%. Demo requests up 42% in the first 30 days. Sales reps now use the video to pre-educate, cutting call time by an average of 12 minutes.",
          results: [{ n: "42%", l: "More Demo Requests" }, { n: "26pt", l: "Bounce Rate Drop" }, { n: "12min", l: "Saved Per Sales Call" }],
          tools: ["After Effects", "Adobe Illustrator", "Premiere Pro", "Audition"],
          video: "https://www.youtube.com/embed/Rk3NoCbwouI?si=J8BgXo0mz7732tSr"
        },
        {
          cat: "Product Demo", client: "Bankleva",
          title: "Fintech Product Demo — Showing How Payments Work in Under 2 Minutes",
          tagline: "Quickcollect's payment collection tool was seeing high sign-up intent but users were dropping off during onboarding. The product worked well — the problem was clarity, not functionality.",
                              details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Create a 90-second product launch video introducing Revizze\'s AI-powered project management platform. The video will be used on the homepage, in paid LinkedIn campaigns, and by the sales team during product demos.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Brief', content: 'Revizze was preparing for a new product launch targeting operations managers at growing companies. The goal was to clearly communicate the platform\'s value in under 90 seconds while positioning it as a faster, smarter alternative to manual project management tools. The video needed to work across multiple channels without requiring different edits.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research', content: 'I spent time understanding the product from the perspective of a first-time user, mapping the onboarding flow, key features, and most common pain points. I also reviewed competitor videos from Asana, Monday.com, ClickUp, and Notion to identify common messaging patterns and opportunities to differentiate the narrative.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Creative Strategy', content: 'Rather than explaining every feature, I focused the story around one measurable benefit: helping teams save time every week. This became the central message, allowing every animation, transition, and UI sequence to reinforce a single outcome instead of competing for attention.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Script Development', content: 'The script followed a simple progression: introduce the problem, highlight the frustrations of manual project management, demonstrate how Revizze solves those challenges through AI automation, and finish with a clear invitation to start a free trial.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>', title: 'Storyboard', content: 'Each scene was sketched before animation began, allowing the pacing and visual hierarchy to be reviewed early. This helped validate the narrative flow before investing time in design and motion.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>', title: 'Animatic', content: 'Before production, I assembled a timed animatic using storyboard frames and the approved voiceover to validate pacing, scene timing, and narrative flow. This allowed key stakeholders to review the structure and make adjustments before animation began, reducing revisions later in production.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path></svg>', title: 'Style Exploration', content: 'The visual language combined clean typography, generous spacing, subtle gradients, and minimal interface design. Motion references were inspired by modern SaaS brands, emphasizing clarity over decorative animation.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>', title: 'Asset Design', content: 'Product screens were recreated in Figma to ensure consistency and flexibility during animation. Supporting assets including icons, graphs, interface cards, and illustrations were designed as reusable components to maintain visual consistency throughout the project.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>', title: 'Animation', content: 'Animation focused on communicating functionality rather than showcasing effects. UI interactions, cursor movements, graph animations, and smooth transitions guided the viewer through the product naturally, keeping attention on the story rather than the motion itself.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path></svg>', title: 'Sound Design', content: 'Subtle interface sounds, transitions, and a modern background track reinforced the feeling of using a responsive digital product without distracting from the narration.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path></svg>', title: 'Review & Iteration', content: 'Multiple review rounds refined pacing, typography, and feature prioritization. Small adjustments to timing and visual emphasis significantly improved clarity while keeping the overall runtime concise.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>', title: 'The Outcome', content: 'The final video became the company\'s primary product explainer across marketing and sales. It was featured on the homepage, included in outbound sales presentations, and repurposed for paid social campaigns, giving the product team a consistent asset across every stage of the customer journey.' }
          ],
          before: "31% of new sign-ups were abandoning onboarding before completing their first payment setup. Support tickets were high volume and low-complexity — users just didn't know where to start.",
          after: "Onboarding drop-off reduced by 31%. Support ticket volume down 22%. Users who watched the video were 2.4x more likely to complete their first transaction within 24 hours.",
          results: [{ n: "31%", l: "Less Drop-off" }, { n: "2.4x", l: "Faster Activation" }, { n: "22%", l: "Fewer Support Tickets" }],
          tools: ["Blender", "Cinema 4D", "After Effects", "Figma"],
          video: "https://www.youtube.com/embed/74j-l-0pw68?si=E5JVmwmpIw97LW-8"
        },
        {
          cat: "Promotional", client: "Kajota",
          title: "AI Product Launch — A Campaign Video That Made People Stop Scrolling",
          tagline: "Kajota's AI tool was launching into a crowded market. The launch video needed to feel genuinely different — not another tech startup montage with stock footage and buzzwords.",
                              details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Create a 90-second product launch video introducing Revizze\'s AI-powered project management platform. The video will be used on the homepage, in paid LinkedIn campaigns, and by the sales team during product demos.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Brief', content: 'Revizze was preparing for a new product launch targeting operations managers at growing companies. The goal was to clearly communicate the platform\'s value in under 90 seconds while positioning it as a faster, smarter alternative to manual project management tools. The video needed to work across multiple channels without requiring different edits.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research', content: 'I spent time understanding the product from the perspective of a first-time user, mapping the onboarding flow, key features, and most common pain points. I also reviewed competitor videos from Asana, Monday.com, ClickUp, and Notion to identify common messaging patterns and opportunities to differentiate the narrative.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Creative Strategy', content: 'Rather than explaining every feature, I focused the story around one measurable benefit: helping teams save time every week. This became the central message, allowing every animation, transition, and UI sequence to reinforce a single outcome instead of competing for attention.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Script Development', content: 'The script followed a simple progression: introduce the problem, highlight the frustrations of manual project management, demonstrate how Revizze solves those challenges through AI automation, and finish with a clear invitation to start a free trial.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>', title: 'Storyboard', content: 'Each scene was sketched before animation began, allowing the pacing and visual hierarchy to be reviewed early. This helped validate the narrative flow before investing time in design and motion.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>', title: 'Animatic', content: 'Before production, I assembled a timed animatic using storyboard frames and the approved voiceover to validate pacing, scene timing, and narrative flow. This allowed key stakeholders to review the structure and make adjustments before animation began, reducing revisions later in production.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path></svg>', title: 'Style Exploration', content: 'The visual language combined clean typography, generous spacing, subtle gradients, and minimal interface design. Motion references were inspired by modern SaaS brands, emphasizing clarity over decorative animation.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>', title: 'Asset Design', content: 'Product screens were recreated in Figma to ensure consistency and flexibility during animation. Supporting assets including icons, graphs, interface cards, and illustrations were designed as reusable components to maintain visual consistency throughout the project.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>', title: 'Animation', content: 'Animation focused on communicating functionality rather than showcasing effects. UI interactions, cursor movements, graph animations, and smooth transitions guided the viewer through the product naturally, keeping attention on the story rather than the motion itself.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path></svg>', title: 'Sound Design', content: 'Subtle interface sounds, transitions, and a modern background track reinforced the feeling of using a responsive digital product without distracting from the narration.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path></svg>', title: 'Review & Iteration', content: 'Multiple review rounds refined pacing, typography, and feature prioritization. Small adjustments to timing and visual emphasis significantly improved clarity while keeping the overall runtime concise.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>', title: 'The Outcome', content: 'The final video became the company\'s primary product explainer across marketing and sales. It was featured on the homepage, included in outbound sales presentations, and repurposed for paid social campaigns, giving the product team a consistent asset across every stage of the customer journey.' }
          ],
          before: "No visual brand language. Marketing relied on text posts and product screenshots. Engagement rate on social: 1.2%. The brand had no differentiated visual identity to stand on.",
          after: "Launch video hit 2.4M impressions in week one. LinkedIn engagement rate: 8.7%. The brand was cited in 3 design publications. Used in the seed fundraising deck.",
          results: [{ n: "2.4M", l: "Week One Impressions" }, { n: "8.7%", l: "LinkedIn Engagement" }, { n: "3", l: "Design Publications" }],
          tools: ["Blender", "Cinema 4D", "After Effects", "DaVinci Resolve"],
          video: "https://www.youtube.com/embed/gLqxiHWS610?si=y8mJ3jiY7tonVLRv"
        },
        {
          cat: "AI App Builder", client: "Occula",
          title: "Occula — AI App Builder: Think Faster. Build Faster.",
          tagline: "Occula is an AI app builder that helps people turn ideas into digital products through conversation. Bringing prompting, context, skills, and generation into one workspace.",
          details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Occula helps users move from idea to working digital product through conversational AI, uniting code generation, project management, skills, and design guidance.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Challenge', content: 'Make powerful AI app-building capabilities approachable without hiding the controls that give users direction and ownership.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research & Strategy', content: 'Centered around conversational intent as the starting point and contextual control (Skills, Connectors, Style guides) as the supporting layer.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'The Experience Model', content: 'Idea -> Prompt -> Context -> Generate -> Iterate -> Build. Progressive disclosure ensures beginners and advanced users succeed.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'User Flow & Refinement', content: 'An active conversational refinement loop allows users to test generated code, tweak guidelines, and iterate dynamically.' }
          ],
          before: "Traditional workflow: multiple fragmented tools, steep learning curves, slow development cycles.",
          after: "The Occula way: one unified workspace, conversation-led creation, rapid iteration, and direct publishing.",
          results: [{ n: "10x", l: "Faster App Prototyping" }, { n: "1", l: "Unified Workspace" }, { n: "100%", l: "Conversational Creation" }],
          tools: ["Figma", "Design Systems", "Prototyping", "UX Strategy"],
          caseStudyUrl: "occula-case-study.html"
        },
        {
          cat: "Mobility App", client: "Rydar",
          title: "Rydar — Ride-Hailing & Delivery Platform: Clarity from Booking to Drop-Off",
          tagline: "A ride-hailing and delivery platform designed around clarity from booking to drop-off, guiding users through decisions, tracking, and recovery states.",
          details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Rydar is an end-to-end ride-hailing and delivery mobile platform designed to make booking predictable and reassuring for passengers.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Problem', content: 'The ride does not start when the driver arrives — it starts with confidence. Passengers needed clear pricing, vehicle options, and tracking without confusion.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research & Discovery', content: 'Surveyed 120+ respondents and audited competitors to identify uncertainty points across pickup selection, driver waiting, and payment states.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Core Flow', content: 'An 8-stage progression: Set destination -> Confirm pickup -> Choose ride -> Select payment -> Match with driver -> Track ride -> Complete trip -> Review.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Designed for Real Life', content: 'Engineered dedicated, intuitive recovery flows for payment failure, connection drops, driver cancellations, and verification errors.' }
          ],
          before: "Fragmented journey where errors caused drop-offs and users faced uncertainty during driver matching and payment.",
          after: "A connected, predictable experience with live vehicle tracking, clear fare breakdown, and transparent recovery states.",
          results: [{ n: "120+", l: "Survey Participants" }, { n: "8", l: "Core Journey Stages" }, { n: "100%", l: "Recovery State Coverage" }],
          tools: ["Figma", "Design Systems", "Prototyping", "User Research"],
          caseStudyUrl: "rydar-case-study.html"
        },
        {
          cat: "Food Delivery", client: "Dishhh",
          title: "Dishhh — A simpler way to discover, order, and track food",
          tagline: "A food delivery platform designed to help users move from discovering food to receiving their order with less friction.",
          details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Dishhh is a food delivery experience designed to help users move from discovering food to receiving their order with less friction across mobile.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Problem', content: 'Food delivery should feel effortless, not overwhelming. The challenge was creating a flow that helps users find what they want quickly and complete orders without friction.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research & Discovery', content: 'Conducted user interviews, competitive analysis across Glovo, Uber Eats, and Bolt Food, and mapped user personas and end-to-end ordering journeys.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Core Flow', content: 'Structured a clear progression: Discover → Explore → Choose → Order → Checkout → Track → Enjoy, keeping next actions obvious and information accessible.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Validation & Outcome', content: 'Validated the flow across restaurant discovery, menu exploration, customisation, checkout, and live order tracking for complete user confidence.' }
          ],
          before: "Overwhelming choices, unclear delivery estimates, complicated multi-step checkouts, and limited order tracking updates.",
          after: "A connected, intuitive food delivery experience with faster discovery, confident decision-making, simpler checkout, and real-time tracking.",
          results: [{ n: "7", l: "Flow Milestones" }, { n: "4", l: "Core Pillars" }, { n: "100%", l: "End-to-End Tracking" }],
          tools: ["Figma", "Design Systems", "Prototyping", "User Research"],
          caseStudyUrl: "dishhh-case-study.html"
        },
        {
          cat: "Fintech App", client: "Vesta",
          title: "Vesta — Investment & Wealth Management App",
          tagline: "A simpler way to invest and manage your portfolio, turning complex financial actions into a structured, trustworthy mobile experience.",
          details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Vesta is a mobile investment experience designed to make investing easier to understand, start, and manage from signup to portfolio growth.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Problem', content: 'Investing introduces unfamiliar terminology, verification friction, and market anxiety. The challenge was making complex fintech actions feel accessible without losing depth.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research & Discovery', content: 'Audited competitors (Robinhood, Fidelity, eToro), developed proto-personas, and mapped user journeys to uncover friction points during verification and funding.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Core Flow', content: 'Structured a continuous progression: Discover → Sign Up → Verify → Fund → Invest → Track → Manage, ensuring users know what happens next at every step.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Outcomes & Design System', content: 'Delivered guided identity verification, transparent funding with upfront fees, contextual stock insights, and comprehensive portfolio tracking.' }
          ],
          before: "Fragmented financial tools with overwhelming verification steps, hidden fees, and complex market charts causing first-time drop-offs.",
          after: "A structured, trustworthy investment experience with guided verification, transparent funding, and clear portfolio performance monitoring.",
          results: [{ n: "7", l: "Flow Milestones" }, { n: "5", l: "Core Pillars" }, { n: "100%", l: "Verified Continuity" }],
          tools: ["Figma", "Design Systems", "Prototyping", "Fintech UX"],
          caseStudyUrl: "vesta-case-study.html"
        },
        {
          cat: "EdTech App", client: "Learnix Academy",
          title: "Learnix — E-Learning &amp; Skills Development App",
          tagline: "Making learning easier to discover, start, and complete through structured lessons, progress visibility, and learner momentum.",
          details: [
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>', title: 'Project Overview', content: 'Learnix Academy is a mobile learning platform designed to help people discover relevant courses, learn from expert instructors, and manage their learning journey.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>', title: 'The Problem', content: 'Turning an overwhelming course library into a clear learning journey. The challenge was helping learners make confident decisions and move smoothly from discovery to completion.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>', title: 'Research & Discovery', content: 'Audited competitors (Udemy, Coursera, Skillshare, LinkedIn Learning), mapped learner proto-personas, and structured user journeys across all learning touchpoints.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>', title: 'Core Flow', content: 'Structured a continuous progression: Discover → Explore → Evaluate → Enroll → Learn → Track → Return, supporting intentional learning momentum.' },
            { icon: '<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>', title: 'Outcomes & Design', content: 'Delivered intuitive course discovery, high-transparency course details, structured video lessons, real-time progress indicators, and strong retention pathways.' }
          ],
          before: "Overwhelming course catalogs with dense navigation, unclear syllabus outcomes, and high drop-off rates after initial enrollment.",
          after: "A connected, motivating mobile learning experience with clear course evaluation, structured lesson pacing, and visible progress tracking.",
          results: [{ n: "7", l: "Learner Stages" }, { n: "4", l: "Core Pillars" }, { n: "100%", l: "Connected Journey" }],
          tools: ["Figma", "Design Systems", "Prototyping", "EdTech UX"],
          caseStudyUrl: "learnix-case-study.html"
        }
      ];

      

      /* ── PARTICLE CANVAS ── */
      var CV = document.getElementById('bgc'), CTX = CV.getContext('2d'), W, H, PTS = [];
      function rsz() { W = CV.width = window.innerWidth; H = CV.height = window.innerHeight; }
      rsz(); window.addEventListener('resize', function () { rsz(); mkp(); });
      function mkp() { PTS = []; var n = Math.floor(W * H / 14000); for (var i = 0; i < n; i++) PTS.push({ x: Math.random() * W, y: Math.random() * H, r: Math.random() * .8 + .2, vx: (Math.random() - .5) * .22, vy: (Math.random() - .5) * .22, a: Math.random() * .35 + .06 }); }
      mkp();
      function drw() {
        CTX.clearRect(0, 0, W, H);
        CTX.strokeStyle = 'rgba(14,165,233,.022)'; CTX.lineWidth = 1;
        for (var gx = 0; gx <= W; gx += 90) { CTX.beginPath(); CTX.moveTo(gx, 0); CTX.lineTo(gx, H); CTX.stroke(); }
        for (var gy = 0; gy <= H; gy += 90) { CTX.beginPath(); CTX.moveTo(0, gy); CTX.lineTo(W, gy); CTX.stroke(); }
        for (var pi = 0; pi < PTS.length; pi++) {
          var p = PTS[pi]; p.x += p.vx; p.y += p.vy;
          if (p.x < 0) p.x = W; if (p.x > W) p.x = 0; if (p.y < 0) p.y = H; if (p.y > H) p.y = 0;
          CTX.beginPath(); CTX.arc(p.x, p.y, p.r, 0, Math.PI * 2); CTX.fillStyle = 'rgba(14,165,233,' + p.a + ')'; CTX.fill();
        }
        for (var ii = 0; ii < PTS.length; ii++) for (var jj = ii + 1; jj < PTS.length; jj++) {
          var dx = PTS[ii].x - PTS[jj].x, dy = PTS[ii].y - PTS[jj].y, dd = Math.sqrt(dx * dx + dy * dy);
          if (dd < 110) { CTX.beginPath(); CTX.moveTo(PTS[ii].x, PTS[ii].y); CTX.lineTo(PTS[jj].x, PTS[jj].y); CTX.strokeStyle = 'rgba(14,165,233,' + (0.06 * (1 - dd / 110)) + ')'; CTX.lineWidth = .5; CTX.stroke(); }
        }
        requestAnimationFrame(drw);
      }
      drw();

      /* ── SCROLL REVEAL ── */
      var rvEls = document.querySelectorAll('.rv');
      requestAnimationFrame(function () {
        for (var i = 0; i < rvEls.length; i++) rvEls[i].classList.add('hi');
        requestAnimationFrame(function () {
          if (!window.IntersectionObserver) { for (var i = 0; i < rvEls.length; i++) rvEls[i].classList.remove('hi'); return; }
          var obs = new IntersectionObserver(function (entries) {
            for (var i = 0; i < entries.length; i++) if (entries[i].isIntersecting) { entries[i].target.classList.remove('hi'); obs.unobserve(entries[i].target); }
          }, { threshold: .08, rootMargin: '0px 0px -20px 0px' });
          for (var i = 0; i < rvEls.length; i++) obs.observe(rvEls[i]);
        });
      });

      /* ── COUNTERS ── */
      function ctr(el) {
        var to = parseInt(el.getAttribute('data-to'), 10), suf = el.getAttribute('data-suf') || '';
        if (!to || el.getAttribute('data-done')) return;
        el.setAttribute('data-done', '1');
        var dur = 1800, t0 = performance.now();
        (function tk(now) { var p = Math.min((now - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3); el.textContent = Math.floor(e * to) + suf; if (p < 1) requestAnimationFrame(tk); else el.textContent = to + suf; })(performance.now());
      }
      var stEls = document.querySelectorAll('[data-to]');
      for (var si = 0; si < stEls.length; si++) ctr(stEls[si]);

      /* ── FILTER ── */
      var ftags = document.querySelectorAll('.ftag');
      var cards = document.querySelectorAll('.pcard');
      function applyFilter(f) {
        for (var i = 0; i < ftags.length; i++) ftags[i].classList.toggle('on', ftags[i].getAttribute('data-filter') === f);
        var vis = 0;
        for (var j = 0; j < cards.length; j++) {
          var show = (f === 'all' || cards[j].getAttribute('data-cat') === f);
          cards[j].style.display = show ? '' : 'none';
          if (show) vis++;
        }
      }
      for (var fi = 0; fi < ftags.length; fi++) {
        ftags[fi].addEventListener('click', (function (tag) {
          return function () { applyFilter(tag.getAttribute('data-filter')); };
        })(ftags[fi]));
      }

      /* ── MODAL ── */
      var MB = document.getElementById('modal-bg');
      var MC = document.getElementById('modalClose');

      function openModal(id) {
        var d = PROJECTS[id];
        if (!d) return;
        document.getElementById('mCat').textContent = d.cat;
        document.getElementById('mClient').textContent = d.client;
        document.getElementById('mTitle').innerHTML = d.title;
        document.getElementById('mTagline').textContent = d.tagline;
        
        
        var mGrid = document.getElementById("mSections");
        if(mGrid) {
            mGrid.innerHTML = "";
            if (d.details) {
                d.details.forEach(function(det) {
                    var cell = document.createElement("div");
                    cell.className = "m3cell";
                    cell.innerHTML = "<div class=\"m3label\">" + det.icon + det.title + "</div><p class=\"m3val\">" + det.content + "</p>";
                    mGrid.appendChild(cell);
                });
            }
        }
        document.getElementById('mBefore').textContent = d.before;
        document.getElementById('mAfter').textContent = d.after;
        // results
        var rGrid = document.getElementById('mResults'); rGrid.innerHTML = '';
        for (var ri = 0; ri < d.results.length; ri++) {
          var rc = document.createElement('div'); rc.className = 'res-card';
          rc.innerHTML = '<span class="res-num">' + d.results[ri].n + '</span><span class="res-lbl">' + d.results[ri].l + '</span>';
          rGrid.appendChild(rc);
        }
        // tools
        var tRow = document.getElementById('mTools'); tRow.innerHTML = '';
        for (var ti = 0; ti < d.tools.length; ti++) {
          var tc = document.createElement('span'); tc.className = 'tool-chip'; tc.textContent = d.tools[ti];
          tRow.appendChild(tc);
        }
        // video
        document.getElementById('modalVisual').innerHTML = '<iframe width="100%" height="100%" src="' + d.video + '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';
        MB.classList.add('open');
        document.body.style.overflow = 'hidden';
        MB.scrollTop = 0;
      }
      function closeModal() { MB.classList.remove('open'); document.body.style.overflow = ''; document.getElementById('modalVisual').innerHTML = ''; }

      for (var ci = 0; ci < cards.length; ci++) {
        cards[ci].addEventListener('click', (function (card) {
          return function () { openModal(parseInt(card.getAttribute('data-id'), 10)); };
        })(cards[ci]));
      }
      MC.addEventListener('click', closeModal);
      MB.addEventListener('click', function (e) { if (e.target === MB) closeModal(); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeModal(); });

      /* ── MOBILE MENU ── */
      var mobileMenuBtn = document.getElementById('mobileMenuBtn');
      var mobileMenu = document.getElementById('mobileMenu');
      var mobileMenuLinks = document.querySelectorAll('.mobile-nav-ul a');

      function toggleMobileMenu() {
        mobileMenuBtn.classList.toggle('active');
        mobileMenu.classList.toggle('active');
        document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
      }

      function closeMobileMenu() {
        mobileMenuBtn.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      }

      mobileMenuBtn.addEventListener('click', toggleMobileMenu);

      for (var mi = 0; mi < mobileMenuLinks.length; mi++) {
        mobileMenuLinks[mi].addEventListener('click', closeMobileMenu);
      }

      mobileMenu.addEventListener('click', function (e) {
        if (e.target === mobileMenu) closeMobileMenu();
      });

    })();