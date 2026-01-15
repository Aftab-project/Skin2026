# Quick Start: Refactor Remaining Treatment Pages

## Overview
You have **23 pages** to refactor. Each takes ~15-20 minutes using the template approach.

---

## The Easy Way: Copy-Paste Method

### Step 1: Open Template
Open `hydrofacial.html` or `korean-facial.html` as your template.

### Step 2: Replace Treatment-Specific Content

In each section, update ONLY these parts:

```
SECTION 1 - HERO
├─ <h1>[TREATMENT TITLE]</h1>
├─ <p class="tagline">[TAGLINE]</p>
└─ style="background-image: url('./images/[TREATMENT]-hero.jpg');"

SECTION 2 - ABOUT
├─ <h3>About This Treatment</h3>
├─ 3x <p>paragraphs with treatment description
├─ 5-6x <div class="badge">benefit badges
└─ 3x <div class="gallery-item">gallery images

SECTION 3 - BENEFITS
├─ <h2>Benefits of [TREATMENT]</h2>
├─ <p>Subtitle (optional)</p>
└─ 6x <div class="benefit-card">
    ├─ <i class="fas fa-[ICON]"></i>
    ├─ <h4>[Benefit Title]</h4>
    └─ <p>[Benefit Description]</p>

SECTION 4 - RESULTS
├─ <h2>Real Results</h2>
├─ 3x <div class="carousel-slide">
│  ├─ <img> or <div class="gallery-placeholder">
│  └─ <p>[Result caption]</p>
└─ 3x <div class="dot">

SECTION 5 - HOW IT WORKS
├─ <h2>How the Treatment Works</h2>
├─ 4x <div class="accordion-item">
│  ├─ <h4>[Step Title]</h4>
│  └─ <p>[Step Description]</p>
└─ Duration info in accordion body

SECTION 6 - PRICING
├─ <h2>Pricing & Enquiry</h2>
├─ Left column: <h3>Investment</h3>
│  └─ 3-4x <div class="pricing-item">
│     ├─ <h4>[Option Name]</h4>
│     └─ <div class="pricing-price">[PRICE]</div>
├─ Right column: <h3>Get in Touch</h3>
└─ <form> with input fields

SECTION 7 - FAQs
├─ <h2>Frequently Asked Questions</h2>
├─ 6-8x <div class="accordion-item">
│  ├─ <h4>[Question]</h4>
│  └─ <p>[Answer]</p>
└─ All same accordion structure

SECTION 8 - RELATED
├─ <h2>Complementary Treatments</h2>
└─ 3x <div class="related-card">
   ├─ <h4 class="related-card-title">[Treatment Name]</h4>
   ├─ <p class="related-card-desc">[Short description]</p>
   ├─ <div class="related-card-meta">
   │  ├─ <span>[Duration]</span>
   │  └─ <span class="related-card-price">From £[PRICE]</span>
   └─ <a href="[LINK]" class="related-card-cta">Learn More</a>
```

---

## Content Template Examples

### Benefit Cards (6 examples)
Use FontAwesome icons from: https://fontawesome.com/icons

```html
<div class="benefit-card">
    <div class="icon"><i class="fas fa-sparkles"></i></div>
    <h4>Instant Glow</h4>
    <p>Visible radiance and brightness immediately after treatment.</p>
</div>
```

Common icons for facials:
- `fas fa-sparkles` - Glow/radiance
- `fas fa-droplet` - Hydration/moisture
- `fas fa-shield-alt` - Protection
- `fas fa-bolt` - Fast/instant results
- `fas fa-clock` - No downtime
- `fas fa-check-circle` - Proven results
- `fas fa-leaf` - Natural/organic
- `fas fa-dumbbell` - Strength/firmness
- `fas fa-arrow-up` - Lifting
- `fas fa-water` - Water/hydration
- `fas fa-sun` - Brightness
- `fas fa-heart` - Love/comfort

### Accordion Items (Step-by-step)

```html
<div class="accordion-item open">
    <div class="accordion-header">
        <h4>1. Consultation & Assessment</h4>
        <i class="fas fa-chevron-down accordion-icon"></i>
    </div>
    <div class="accordion-content">
        <div class="accordion-body">
            <p>Description of step (2-3 sentences)</p>
            <p><strong>Duration:</strong> XX minutes</p>
        </div>
    </div>
</div>
```

### FAQ Accordion Item

```html
<div class="accordion-item">
    <div class="accordion-header">
        <h4>Is the treatment painful?</h4>
        <i class="fas fa-chevron-down accordion-icon"></i>
    </div>
    <div class="accordion-content">
        <div class="accordion-body">
            <p>Answer to the question (2-3 sentences)</p>
        </div>
    </div>
</div>
```

---

## Quick Checklist for Each Page

```
[ ] Update <title> tag with treatment name
[ ] Update meta description with treatment benefit
[ ] Update og:title and og:description
[ ] Update og:image path if image exists
[ ] Update hero section h1, tagline
[ ] Update hero background-image path
[ ] Update about paragraphs (3x)
[ ] Update about badges (5-6x)
[ ] Update benefits section title
[ ] Update 6 benefit cards with icons, titles, descriptions
[ ] Update carousel captions (3x)
[ ] Update accordion steps (4 items with times)
[ ] Update pricing section with prices and options
[ ] Update form hidden field treatment name
[ ] Update FAQs (6-8 items)
[ ] Update related treatments section (3 cards with links)
[ ] Verify all links are correct
[ ] Test on mobile view
```

---

## Pricing Template

Always use these same tiers (customize amounts):
```html
<div class="pricing-item">
    <div class="pricing-info">
        <h4>Single Session</h4>
        <p>Complete treatment</p>
    </div>
    <div class="pricing-price">£[PRICE]</div>
</div>

<div class="pricing-item">
    <div class="pricing-info">
        <h4>3-Pack Course</h4>
        <p>Best for results</p>
    </div>
    <div class="pricing-price">£[PRICE]</div>
</div>

<div class="pricing-item">
    <div class="pricing-info">
        <h4>6-Pack Course</h4>
        <p>Maximum benefits</p>
    </div>
    <div class="pricing-price">£[PRICE]</div>
</div>

<div class="pricing-item">
    <div class="pricing-info">
        <h4>Add-on [Option]</h4>
        <p>[Description]</p>
    </div>
    <div class="pricing-price">£[PRICE]</div>
</div>
```

---

## Form Template (No Changes Needed)

```html
<form class="enquiry-form" action="contact.php" method="POST">
    <input type="hidden" name="treatment" value="[TREATMENT NAME]">
    <!-- rest of form is identical -->
</form>
```

Just update the treatment name in the hidden field!

---

## Facial Pages List (9 total)

1. **oxygeno-facial.html**
   - Title: Skin Oxyglow: OxygenO Facial
   - Price: £89 | Duration: 45 min
   - Focus: Oxygen infusion, instant glow, hydration

2. **biorepeel.html**
   - Title: Skin Radiance: BioRePeel
   - Price: £99 | Duration: 45 min
   - Focus: Chemical peel, cell renewal, brightening

3. **biomicroneedling.html**
   - Title: Green Peel – BioMicroneedling
   - Price: £89 | Duration: 45 min
   - Focus: Herbal microneedling, collagen, natural renewal

4. **chemical-peel.html**
   - Title: Skin Renewal: Chemical Peel
   - Price: £99 | Duration: 45 min
   - Focus: Professional exfoliation, transformation

5. **microneedling-biorepeel.html**
   - Title: Skin Revive: Microneedling + BioRePeel
   - Price: £149 | Duration: 60 min
   - Focus: Dual-action, maximum results

6. **rf-facial.html**
   - Title: Skin LumaLift: Radio Frequency Facial
   - Price: £129 | Duration: 60 min
   - Focus: RF technology, lifting, tightening

7. **ultimate-exfoliation.html**
   - Title: Skin Luxe Satin: Ultimate Exfoliation
   - Price: £99 | Duration: 45 min
   - Focus: Triple exfoliation, smoothness, glow

8. **blackhead-extraction.html**
   - Title: Deep Blackhead Extraction
   - Price: £79 | Duration: 45 min
   - Focus: Pore cleaning, professional extraction

9. **bb-glow.html**
   - Title: Skin Balance: BB Glow
   - Price: £125 | Duration: 60 min
   - Focus: Semi-permanent, tinted, skincare benefits

---

## HIFU Pages List (13 total)

All in `/treatments/` folder. Remember to use `../` for CSS/JS paths!

**Face & Neck:**
1. hifu-face.html - £199, 60 min
2. hifu-neck.html - £149, 45 min
3. hifu-face-neck.html - £299, 90 min
4. hifu-jawline.html - £179, 60 min

**Body:**
5. hifu-butt-lift.html - £299, 60 min
6. hifu-breast-lift.html - £349, 75 min
7. hifu-stomach.html - £279, 60 min
8. hifu-love-handles.html - £199, 45 min

**Legs:**
9. hifu-inner-thighs.html - £249, 60 min
10. hifu-outer-thighs.html - £249, 60 min
11. hifu-banana-rolls.html - £199, 45 min
12. hifu-arms.html - £199, 45 min

**Bundles:**
13. hifu-stomach-love-handles.html - £449, 90 min

---

## Time Estimate

- **Per page:** 15-20 minutes (copy-paste + customize)
- **9 facial pages:** ~2.5-3 hours
- **13 HIFU pages:** ~3-4 hours
- **Total remaining:** ~5.5-7 hours

**With parallel work:** Could be done in 1-2 days

---

## Tips for Speed

1. **Use Find & Replace** in VS Code
   - Find: `.treatment-container`
   - Replace: (leave same, just navigate to sections)

2. **Copy entire sections** from template and just update the inner content

3. **Batch similar pages** - Do all facial exfoliation pages first, then HIFU face pages, etc.

4. **Keep template open** in split view while editing new page

5. **Use Emmet** in VS Code for faster HTML generation
   - Type `.accordion-item>div.accordion-header` and press Tab

---

## Success Criteria for Each Page

- [ ] Page loads without errors
- [ ] Sticky nav works (scrolls smooth, active link highlights)
- [ ] All CTAs point to correct sections
- [ ] Form submits without errors
- [ ] Carousel works (prev/next, dots, auto-play)
- [ ] Accordions expand/collapse smoothly
- [ ] Mobile view is responsive
- [ ] No console JavaScript errors
- [ ] All relative links are correct

---

**Total Effort:** ~6-8 hours for all 23 remaining pages  
**Tools Needed:** VS Code, Find & Replace, template files  
**Resources:** hydrofacial.html, korean-facial.html, components.css, treatment-components.js

Ready to start refactoring! 🚀
