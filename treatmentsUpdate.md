
Goal: Refactor ALL treatment info pages (every page linked under the site’s subheader dropdown) to a consistent layout and component structure, keeping the brand aesthetic. You MAY add new colors if they harmonize with the site and maintain logical combinations and WCAG AA contrast.

Scope:
- Include all treatment detail pages (e.g., hydrafacial, facials, massage, RF, microcurrent, etc.).
- Do not change routes/slugs; keep SEO metadata and content sources intact.

Global style rules:
- Keep existing typography scale, spacing rhythm, button radii, shadows, animations.
- Colors:
  - Prefer existing CSS variables/design tokens (e.g., --brand-*, Tailwind theme).
  - You MAY extend the palette minimally: up to 2 accents + 1 neutral surface tone that fits the aesthetic.
  - Maintain AA contrast for text and interactive elements.
- Fully responsive (mobile‑first), accessible (semantic HTML, ARIA, heading hierarchy), and SEO-friendly (meta/OG tags, alt text).
- Reuse existing components/utilities (Button, Container, Grid, Accordion, Tabs, Carousel). If missing, create minimal reusable ones.

Target layout (top → bottom) for every treatment page:
1) HERO
   - Full‑width background image/video for that treatment.
   - H1 (treatment name) + short tagline.
   - Two pill CTAs: primary “Book now”, secondary “See benefits” with smooth scroll.

2) STICKY SUBNAV (tabs/anchors)
   - Anchors: About • Benefits • Gallery • Results • Step‑by‑step • Pricing • FAQs • Related
   - Sticky on scroll; smooth scroll; highlight active section while scrolling.

3) ABOUT THE SERVICE
   - Two‑column (stacks on mobile).
   - Left: section title + 2–3 concise paragraphs sourced from the page’s content.
   - Right: key points/badges (e.g., “No downtime”, “Glowing complexion”).
   - Below: responsive 3‑image inline gallery.

4) BENEFITS GRID
   - 2×2 or 3×2 responsive cards.
   - Each card: small icon/bullet, short title, 1–2 line description.

5) RESULTS (BEFORE/AFTER)
   - Carousel/slider with captions; arrows/dots; swipe on mobile.

6) STEP‑BY‑STEP (ACCORDION)
   - Items: (1) Consultation, (2) Before Treatment, (3) During Treatment, (4) Aftercare.
   - Expandable accordion items with rich text.

7) PRICING + CONTACT
   - Two‑column:
     - Left: pricing list (sessions + add‑ons) with durations/prices.
     - Right: compact enquiry form (Name, Contact method, Phone/Email, Message, Consent).
   - Submit via existing form handler/component.

8) FAQS (ACCORDION)
   - Two‑column on desktop; single column on mobile.
   - Use existing FAQ data where available. Accessible controls.

9) RELATED TREATMENTS
   - Horizontal cards: image, title, short blurb, duration, from‑price, “Learn more” link.
   - Reuse Card component if available.

Implementation notes (apply to all pages):
- Section IDs: #about #benefits #gallery #results #steps #pricing #faqs #related
- Headings: H1 (page) → H2 (sections) → H3 (items).
- Lazy‑load images; use srcset or framework <Image>.
- Keep strings translatable if i18n is configured.
- Preserve routes/slugs and SEO metadata (canonical, OG tags).
- If a component doesn’t exist, build a minimal reusable one consistent with design system.

Content/data guidance:
- Pull copy, prices, durations, and images from each page’s existing data source (CMS/JSON/MDX).
- Create a normalized data model per treatment:
  {
    "title": "Treatment Name",
    "tagline": "Short benefit statement",
    "hero": { "image": "...", "primaryCta": "#pricing", "secondaryCta": "#benefits" },
    "about": { "intro": "...", "details": ["...", "..."], "badges": ["..."], "gallery": ["...","...","..."] },
    "benefits": [{ "title": "...", "text": "..." }],
    "results": [{ "before": "...", "after": "...", "caption": "..." }],
    "steps": [{ "title": "Consultation", "content": "..." }, { "title": "Before Treatment", "content": "..." }, { "title": "During Treatment", "content": "..." }, { "title": "Aftercare", "content": "..." }],
    "pricing": { "sessions": [{ "name": "...", "price": ... }], "addons": [{ "name": "...", "price": ... }] },
    "faqs": [{ "q": "...", "a": "..." }],
    "related": [{ "title": "...", "from": ..., "duration": "...", "image": "...", "href": "/treatments/..." }]
  }

Palette extension guidance (allowed):
- Use one **primary**, one **secondary**, one **neutral surface**, and up to **two accents**.
- Hover/active states: ~8–12% lighter/darker than base.
- Apply accents sparingly to active tabs, badges, focus rings, and subtle borders.
- Ensure WCAG AA contrast for text and interactive elements.

Acceptance criteria (for every page):
- Layout matches the section order above.
- Colors remain consistent and tasteful; contrast meets AA.
- Sticky tabs work with smooth scroll + active highlighting.
- Lighthouse mobile + accessibility ≥ 90.
- Form posts to the existing handler without regressions.
- No breaking changes to routes or SEO metadata.

Action:
Implement this refactor across ALL treatment pages listed in the subheader dropdown. Create or update shared components as needed. Keep code clean, modular, and commented.
