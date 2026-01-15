#!/usr/bin/env python3
"""
Generate all Microneedling RF treatment pages from template
"""

import os
import re

BASE_DIR = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

# Template data for each treatment
TREATMENTS = {
    "stretch-mark-resurfacing": {
        "title": "Stretch Mark Resurfacing",
        "heading": "Stretch Mark Resurfacing with Fractional RF + Microneedling",
        "tagline": "Advanced corrective treatment designed to visibly improve stretch marks",
        "about_intro": "Stretch Mark Resurfacing with Fractional RF + Microneedling is an advanced corrective treatment designed to visibly improve the appearance of stretch marks by repairing weakened skin structure, tightening tissue, and smoothing texture.",
        "about_detail": "Microneedling creates controlled micro-channels that stimulate natural collagen and elastin production while preparing the skin for deeper repair. Fractional RF then delivers heat into the dermis to remodel damaged fibres, strengthen skin density, and tighten stretched tissue. Suitable for stomach, hips, thighs, buttocks, breasts, arms, and lower back.",
        "badges": ["Stretch Mark Correction", "Skin Tightening", "Texture Smooth", "Collagen Boost", "Non-Surgical"],
        "steps": [
            ("Skin Assessment & Treatment Planning", "Stretch marks are assessed for depth, texture, and skin laxity to customise treatment intensity."),
            ("Skin Preparation", "The area is cleansed and prepped to optimise microneedling penetration and RF energy delivery."),
            ("Microneedling Skin Correction", "Precision microneedling creates micro-channels to stimulate collagen and improve skin texture."),
            ("Fractional RF Remodeling", "Fractional RF energy is delivered to heat deeper layers, tightening tissue and rebuilding weakened skin fibres."),
            ("Soothing Recovery & Barrier Support", "Calming, restorative products are applied to reduce sensitivity and support healing.")
        ],
        "pricing_items": [
            ("Body Area - 1 Session", "£175"),
            ("Body Area - 3 Sessions", "£473"),
            ("Body Area - 6 Sessions", "£893")
        ],
        "course": "4–6 sessions spaced 4–6 weeks apart",
        "maintenance": "1–2 sessions per year"
    },
    
    "skin-blur-microneedling": {
        "title": "Skin Blur Microneedling",
        "heading": "Skin Blur Microneedling",
        "tagline": "Non-surgical skin rejuvenation for smoothness and refined texture",
        "about_intro": "Our Skin Blur Microneedling treatment is a non-surgical skin rejuvenation solution that smooths fine lines, diminishes scarring, and refines uneven texture for a brighter, more even complexion.",
        "about_detail": "Skin Blur works like a subtle blur filter for your skin — softening imperfections, minimizing pores, and smoothing texture to give a polished, flawless appearance. Perfect for the face, neck, and body, ideal for anyone looking to improve skin texture and minimize pores.",
        "badges": ["Texture Refinement", "Fine Lines Reduction", "Pore Minimizing", "Collagen Boost", "Non-Surgical"],
        "steps": [
            ("Skin Prep & Cleansing", "Deep cleanse to remove makeup, oil, and impurities ensuring maximum penetration."),
            ("Precision Skin Assessment", "Assess skin to identify fine lines, scars, texture irregularities, and areas of concern."),
            ("Microneedling Treatment", "Micro-channels are created in the skin, triggering natural healing and collagen production."),
            ("Targeted Contouring & Refinement", "Focus on problem areas like the jawline, cheeks, and neck for improved definition."),
            ("Active Serum Infusion", "Hydrating and reparative serums are applied to enhance recovery and boost results."),
            ("Barrier Protection & Finish", "Protective layer and SPF are applied to reduce sensitivity and support healing.")
        ],
        "pricing_items": [
            ("Face", "£125"),
            ("Face & Neck", "£175"),
            ("Body Area", "£149")
        ],
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "1–2 sessions per year"
    },

    "brightening-c-microneedling": {
        "title": "Brightening C Microneedling",
        "heading": "Brightening C Microneedling",
        "tagline": "Even skin tone and boost radiance with Vitamin C infusion",
        "about_intro": "Take your skin glow to the next level with our Brightening C Microneedling, a dual-action treatment designed to even skin tone, reduce pigmentation, boost radiance, and improve skin texture.",
        "about_detail": "This premium treatment combines microneedling with professional serums and Vitamin C infusion, both in-clinic and as take-home serums. Microneedling creates micro-channels in the skin to stimulate collagen and elastin production, while Vitamin C boosts radiance and reduces dark spots.",
        "badges": ["Radiance Boost", "Even Tone", "Pigmentation Reduction", "Firming", "Vitamin C Infusion"],
        "steps": [
            ("Skin Prep & Activation", "Treatment area is cleansed and prepared to optimise microneedling efficacy."),
            ("Precision Assessment & Mapping", "Individual pigmentation and texture concerns are assessed and mapped."),
            ("Microneedling + Professional Serum Infusion", "Micro-channels are created while hydrating serums are applied, stimulating collagen."),
            ("Vitamin C Post-Treatment Infusion", "Vitamin C serum is applied in-clinic to boost radiance and even skin tone."),
            ("Vitamin C Take-Home Serum", "Professional-grade Vitamin C serum is provided for home use starting day 3."),
            ("Barrier Protection & Finish", "Protective layer and SPF are applied to safeguard skin and lock in results.")
        ],
        "pricing_items": [
            ("Face", "£175"),
            ("Face & Neck", "£249"),
            ("Body Area", "£175")
        ],
        "course": "3–6 sessions spaced 4 weeks apart",
        "maintenance": "Every 2–3 months"
    },

    "hydra-glow-microneedling": {
        "title": "Hydra-Glow Microneedling",
        "heading": "Hydra-Glow Microneedling",
        "tagline": "Luxurious hydration and radiance with mini-hydrofacial fusion",
        "about_intro": "Elevate your skin's hydration and radiance with Hydra-Glow Microneedling, a luxurious dual-action treatment that fuses microneedling with a mini-hydrofacial.",
        "about_detail": "This advanced treatment deeply hydrates, smooths, and rejuvenates the skin while stimulating natural collagen and elastin production, leaving your complexion radiant, plump, and refreshed. Hydra-Glow works beneath the surface to refine texture, reduce fine lines, and restore youthful elasticity.",
        "badges": ["Deep Hydration", "Radiance Boost", "Fine Lines Reduction", "Collagen Boost", "Plumping"],
        "steps": [
            ("Light Exfoliation", "Gently slough away dead skin cells to smooth surface and prep the skin."),
            ("Extractions", "Clear clogged pores and impurities for a clean, refreshed base."),
            ("Precision Assessment", "Map target areas for hydration, fine lines, and texture improvement."),
            ("Microneedling + Serum Infusion", "Micro-channels are created while hydrating and repairing serums penetrate deeply."),
            ("Hydration & Glow Infusion", "Glow-boosting, hydrating serums are applied for plump, radiant, dewy skin."),
            ("LED Light Therapy & Barrier Protection", "Red LED accelerates healing, then protective layer and SPF are applied.")
        ],
        "pricing_items": [
            ("Face", "£175"),
            ("Face & Neck", "£249"),
            ("Body Area", "£175")
        ],
        "course": "3–6 sessions spaced 4 weeks apart",
        "maintenance": "Every 2–3 months"
    },

    "firming-peptide-microneedling": {
        "title": "Firming Peptide Microneedling",
        "heading": "Firming Peptide Microneedling",
        "tagline": "Restore firmness and define your natural contours",
        "about_intro": "Restore firmness, lift sagging areas, and define your natural contours with Firming Peptide Microneedling. This advanced treatment combines precision microneedling with targeted peptide serums.",
        "about_detail": "Designed to stimulate collagen and elastin production, improving elasticity, lifting the skin, and strengthening the skin barrier. Ideal for anyone looking to combat early signs of aging, sagging, or loss of firmness, delivering a naturally lifted, sculpted, and rejuvenated appearance.",
        "badges": ["Lifting & Firming", "Contour Sculpting", "Elasticity Boost", "Sagging Reduction", "Anti-Aging"],
        "steps": [
            ("Skin Prep & Activation", "Skin is thoroughly cleansed and prepped to enhance penetration of peptide serums."),
            ("Firming Assessment & Mapping", "Key areas of sagging and fine lines are identified, with focus on jawline and cheeks."),
            ("Microneedling + Peptide Serum Infusion", "Micro-channels are created while potent peptide serums penetrate deeply."),
            ("Targeted Contour & Sculpting", "Peptide application and gentle massage focus on areas needing definition."),
            ("Hydration & Radiance Boost", "Hydrating serums are applied to plump skin and enhance radiance."),
            ("Barrier Protection & Finish", "Protective layer and SPF are applied to lock in results and support recovery.")
        ],
        "pricing_items": [
            ("Face", "£175"),
            ("Face & Neck", "£249"),
            ("Body Area", "£175")
        ],
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months"
    },

    "cellular-boost-exosomes-microneedling": {
        "title": "Cellular Boost: Exosomes + Microneedling",
        "heading": "Cellular Boost: Exosomes + Microneedling",
        "tagline": "Next-generation cellular renewal with advanced exosome therapy",
        "about_intro": "Revolutionize your skin with Cellular Boost: Microneedling + Exosomes, a next-generation treatment combining precision microneedling with advanced exosome therapy.",
        "about_detail": "Exosomes — naturally derived cellular messengers — accelerate repair, stimulate collagen and elastin, and boost cellular turnover, leaving skin firmer, smoother, and radiantly youthful. This cutting-edge combination promotes cellular regeneration and deep skin rejuvenation.",
        "badges": ["Cellular Renewal", "Accelerated Healing", "Collagen Boost", "Cellular Turnover", "Advanced Tech"],
        "steps": [
            ("Skin Analysis & Activation", "Assess skin to identify early aging, texture concerns, and cellular fatigue."),
            ("Gentle Enzyme Prep", "Light enzyme treatment softens skin and primes it for maximum absorption."),
            ("Microneedling with Exosome Infusion", "Precision microneedling creates micro-channels, exosomes delivered directly to dermis."),
            ("Hydration & Radiance Boost", "Hydrating serums applied to plump, nourish, and enhance skin glow."),
            ("LED Regeneration Therapy", "Red LED light accelerates healing, calms inflammation, and boosts collagen."),
            ("Barrier Protection & Finish", "Protective layer and SPF applied to lock in results and strengthen barrier.")
        ],
        "pricing_items": [
            ("Face", "£175"),
            ("Face & Neck", "£249"),
            ("Body Area", "£175")
        ],
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months"
    },

    "scalp-revive-microneedling-exosomes": {
        "title": "Scalp Revive: Microneedling + Exosomes",
        "heading": "Scalp Revive: Microneedling + Exosomes",
        "tagline": "Revitalize hair follicles and support natural hair growth",
        "about_intro": "Bring your scalp back to life with Scalp Revive, a cutting-edge treatment combining precision microneedling with regenerative exosomes.",
        "about_detail": "This dual-action therapy stimulates blood flow, revitalizes hair follicles, and supports natural hair growth while improving overall scalp health. Perfect for thinning hair, weakened follicles, or early signs of hair loss.",
        "badges": ["Hair Follicle Stimulation", "Blood Flow Boost", "Hair Growth Support", "Scalp Health", "Hair Thinning"],
        "steps": [
            ("Scalp Analysis & Activation", "Assess hair density, follicle health, and scalp condition for customized treatment."),
            ("Cleansing & Prep", "Gently cleanse scalp to remove impurities and optimize absorption."),
            ("Microneedling with Exosome Infusion", "Precision microneedling creates micro-channels, exosomes penetrate directly."),
            ("Targeted Follicle Boost", "Focus on areas of thinning with additional exosome infusion for follicle repair."),
            ("Hydration & Nourishing Serum", "Infuse scalp with hydrating and nutrient-rich serums."),
            ("Barrier Protection & Finish", "Protective layer applied to reduce sensitivity and enhance recovery.")
        ],
        "pricing_items": [
            ("Scalp - 1 Session", "£175"),
            ("Scalp - 3 Sessions", "£420"),
            ("Scalp - 6 Sessions", "£735")
        ],
        "course": "3–6 sessions spaced 4–6 weeks apart",
        "maintenance": "Every 3–4 months"
    },

    "green-peel-bio-microneedling": {
        "title": "Green Peel – Bio Microneedling",
        "heading": "Green Peel – Bio Microneedling",
        "tagline": "Natural herbal-based skin resurfacing and renewal",
        "about_intro": "The Green Peel is a natural, herbal-based skin resurfacing treatment that stimulates the skin's regeneration using plant-derived ingredients instead of chemical acids.",
        "about_detail": "Suitable for face, neck, décolleté, and body areas, it boosts circulation, accelerates cell turnover, and strengthens the skin from within. A specialized herbal blend is massaged into the skin, acting as a natural micro-exfoliator.",
        "badges": ["Natural Herbs", "Cell Turnover", "Circulation Boost", "Chemical-Free", "Peeling"],
        "steps": [
            ("Consultation & Skin Assessment", "Personalized evaluation to choose right Green Peel strength."),
            ("Cleansing & Prep", "Gentle cleanse to remove impurities and prep skin."),
            ("Herbal Blend Application", "Massage herbal mixture into skin, activating circulation."),
            ("Absorption & Activation", "Herbs stimulate cellular renewal and boost circulation."),
            ("Removal & Soothing Mask", "Herbs removed, calming mask applied to hydrate and reduce sensitivity."),
            ("Skin Healing Serum & Take-Home Care", "Healing serum applied in-clinic, take-home serum for regeneration support.")
        ],
        "pricing_items": [
            ("Face", "£99"),
            ("Face & Neck", "£149"),
            ("Body Area", "£125")
        ],
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 3–6 months"
    },

    "skin-revive-microneedling-biorepeel": {
        "title": "Skin Revive: Microneedling + BioRePeel",
        "heading": "Skin Revive: Microneedling + BioRePeel",
        "tagline": "Transformative dual-action skin renewal and resurfacing",
        "about_intro": "Rejuvenate and restore your complexion with Skin Revive, a transformative treatment combining precise microneedling with the powerful BioRePeel.",
        "about_detail": "Designed to smooth texture, reduce acne scars, refine pores, and restore firmness, this dual-action treatment stimulates collagen production and promotes deep skin renewal. The combination of microneedling and BioRePeel ensures both immediate and long-term benefits.",
        "badges": ["Scar Reduction", "Pore Refinement", "Texture Smoothing", "Dual-Action", "Skin Renewal"],
        "steps": [
            ("Double Cleanse", "Remove makeup, oil, and impurities, creating a clean canvas."),
            ("Skin Preparation", "Gentle solution preps skin, enhancing comfort and results."),
            ("Microneedling", "Precision micro-needles create microchannels to stimulate collagen."),
            ("BioRePeel Application", "Nutrient-rich chemical peel resurfaces skin and enhances radiance."),
            ("Soothing Mask & Hydration", "Calms redness, locks in moisture, and supports recovery."),
            ("Targeted Serums & Protection", "Infuse with bespoke serums and finish with SPF protection.")
        ],
        "pricing_items": [
            ("Face", "£175"),
            ("Face & Neck", "£225")
        ],
        "course": "3–6 treatments",
        "maintenance": "Every 4–6 weeks"
    }
}

def generate_html(filename, config):
    """Generate HTML page for a treatment"""
    
    title = config["title"]
    heading = config["heading"]
    tagline = config["tagline"]
    about_intro = config["about_intro"]
    about_detail = config["about_detail"]
    badges = config["badges"]
    steps = config["steps"]
    pricing_items = config["pricing_items"]
    course = config["course"]
    maintenance = config["maintenance"]
    
    # Generate steps HTML
    steps_html = ""
    for i, (step_title, step_desc) in enumerate(steps, 1):
        steps_html += f'''
                <div class="experience-card">
                    <div class="step-number">{i}</div>
                    <div class="step-icon">
                        <i class="fas fa-spa"></i>
                    </div>
                    <h3>{step_title}</h3>
                    <p>{step_desc}</p>
                </div>
'''
    
    # Generate badges
    badges_html = "\n".join([f'                        <div class="badge">{badge}</div>' for badge in badges])
    
    # Generate pricing items
    pricing_html = ""
    for item_name, item_price in pricing_items:
        pricing_html += f'''
                        <div class="pricing-item">
                            <div class="pricing-info">
                                <h4>{item_name}</h4>
                                <p>Premium treatment for optimal results.</p>
                            </div>
                            <div class="pricing-price">{item_price}</div>
                            <a href="https://that-time.co.uk/service/196300/book" target="_blank" rel="noopener noreferrer" class="nav-link book-btn">Book Now</a>
                        </div>
'''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} at Mili Skin & Beauty - Premium skincare treatment.">
    <meta name="keywords" content="{title}, microneedling, skincare, Mili Skin & Beauty, London">
    <meta property="og:title" content="{title} - Mili Skin & Beauty">
    <meta property="og:description" content="{title} at Mili Skin & Beauty - {tagline}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="../images/hifu-hero.jpg">
    <title>{title} - Mili Skin & Beauty</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../components.css">
</head>
<body>
    
    <!-- Header & Navigation -->
    <header class="header">
        <nav class="navbar">
            <div class="container">
                <div class="nav-wrapper">
                    <a href="../index.html#home" class="logo">
                        <span class="logo-text">Mili Skin & Beauty</span>
                    </a>
                    
                    <button class="mobile-menu-toggle" aria-label="Toggle Menu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                    
                    <ul class="nav-links">
                        <li><a href="../index.html#home" class="nav-link">Home</a></li>
                        <li><a href="../index.html#about" class="nav-link">About</a></li>
                        <li><a href="../index.html#services" class="nav-link">Services</a></li>
                        <li><a href="../index.html#contact" class="nav-link">Contact</a></li>
                        <li><a href="../faq.html" class="nav-link">FAQ</a></li>
                        <li><a href="https://that-time.co.uk/service/196300/book" target="_blank" rel="noopener noreferrer" class="nav-link book-btn">Book Now</a></li>
                    </ul>

                    <div class="nav-actions">
                        <button class="search-toggle" aria-label="Open search" aria-expanded="false" aria-controls="nav-search-panel">
                            <i class="fas fa-search"></i>
                        </button>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <!-- ============================================
         SECTION 1: HERO
         ============================================ -->
    <section class="treatment-hero" style="background-image: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url('../images/hifu-hero.jpg'); background-size: cover; background-position: center;">
        <div class="treatment-container">
            <h1 style="color: #fff; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);">{heading}</h1>
            <p class="tagline" style="color: #f0f0f0; text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);">{tagline}</p>
            
            <div class="hero-cta-buttons">
                <a href="#section-pricing" class="btn btn-primary">Book Now</a>
                <a href="#section-benefits" class="btn btn-secondary" style="background-color: #6B5437; color: #fff; border-color: #6B5437;">See Benefits</a>
            </div>
        </div>
    </section>

    <!-- ============================================
         STICKY SUBNAV (Tabs/Anchors)
         ============================================ -->
    <nav class="sticky-subnav">
        <div class="subnav-container">
            <ul class="subnav-list">
                <li class="subnav-item"><a href="#section-about" class="subnav-link active">About</a></li>
                <li class="subnav-item"><a href="#section-benefits" class="subnav-link">Benefits</a></li>
                <li class="subnav-item"><a href="#section-steps" class="subnav-link">How It Works</a></li>
                <li class="subnav-item"><a href="#section-pricing" class="subnav-link">Pricing</a></li>
            </ul>
        </div>
    </nav>

    <!-- ============================================
         SECTION 2: ABOUT THE SERVICE
         ============================================ -->
    <section id="section-about" class="treatment-section">
        <div class="treatment-container">
            <div class="about-layout">
                <div class="about-content">
                    <h3>About This Treatment</h3>
                    <p>{about_intro}</p>
                    <p>{about_detail}</p>
                </div>
                
                <div class="about-features">
                    <h3>Key Features</h3>
                    <div class="about-badges">
{badges_html}
                    </div>
                </div>
            </div>

            <!-- Inline Gallery (3 images) -->
            <div class="gallery-grid">
                <div class="gallery-item">
                    <img src="../images/SkinGlowydrofacial.webp" alt="{title} treatment" loading="lazy">
                </div>
                <div class="gallery-item">
                    <img src="../images/Hydrafacial.jpg" alt="{title} results" loading="lazy">
                </div>
                <div class="gallery-item">
                    <img src="../images/skinreviewtopuo.png" alt="{title} skin improvement" loading="lazy">
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 3: BENEFITS + REAL RESULTS
         ============================================ -->
    <section id="section-benefits" class="treatment-section" style="background: var(--neutral-surface);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Benefits and Real Results</h2>
                <p>Discover what makes this treatment special</p>
            </div>

            <div class="benefits-results-wrap">
                <div class="benefits-panel">
                    <div class="benefits-grid">
                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-heart-pulse"></i></div>
                            <h4>Collagen & Elastin Stimulation</h4>
                            <p>Triggers natural skin regeneration and long-term rejuvenation</p>
                        </div>
                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-face-smile"></i></div>
                            <h4>Skin Refinement</h4>
                            <p>Improves texture and refines overall skin quality</p>
                        </div>
                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-wand-magic-sparkles"></i></div>
                            <h4>Non-Surgical, Minimal Downtime</h4>
                            <p>High-impact results without surgery or extended recovery</p>
                        </div>
                    </div>
                </div>

                <div class="results-panel">
                    <div class="results-card">
                        <div class="results-media">
                            <img src="../images/HydraFacial_Before_and_After.webp" alt="Treatment before and after results" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; border: 6px solid #d6ad60; border-radius: 12px; display: block;">
                        </div>
                        <div class="results-body">
                            <h3>Real Results</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 5: STEP-BY-STEP EXPERIENCE
         ============================================ -->
    <section id="section-steps" class="treatment-section" style="background: linear-gradient(135deg, #f8f6f1 0%, #faf8f3 100%);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Your Step-by-Step Experience</h2>
                <p>A comprehensive treatment journey</p>
            </div>

            <div class="experience-grid">
{steps_html}
            </div>
        </div>
    </section>

    <style>
        .experience-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 35px;
            margin-top: 45px;
        }}

        .experience-card {{
            background: #fff;
            padding: 35px 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(214, 173, 96, 0.12);
            transition: all 0.3s ease;
            position: relative;
            text-align: center;
        }}

        .experience-card:hover {{
            box-shadow: 0 8px 20px rgba(214, 173, 96, 0.2);
            transform: translateY(-5px);
        }}

        .step-number {{
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, #d6ad60, #e5bf77);
            color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 14px;
            box-shadow: 0 3px 8px rgba(214, 173, 96, 0.3);
        }}

        .step-icon {{
            font-size: 32px;
            color: #d6ad60;
            margin: 15px 0 12px 0;
        }}

        .experience-card h3 {{
            font-size: 16px;
            font-weight: 600;
            color: #1a1a1a;
            margin: 10px 0 8px 0;
            font-family: 'Playfair Display', serif;
        }}

        .experience-card p {{
            font-size: 13px;
            color: #666;
            line-height: 1.5;
            margin: 0;
        }}

        @media (max-width: 768px) {{
            .experience-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 15px;
            }}

            .experience-card {{
                padding: 20px 15px;
            }}

            .experience-card h3 {{
                font-size: 14px;
            }}

            .experience-card p {{
                font-size: 12px;
            }}
        }}

        @media (max-width: 480px) {{
            .experience-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>

    <!-- ============================================
         SECTION 6: PRICING & CONTACT
         ============================================ -->
    <section id="section-pricing" class="treatment-section">
        <div class="treatment-container">
            <h2>Pricing & Enquiry</h2>
            
            <div class="pricing-layout">
                <!-- Pricing Column -->
                <div>
                    <h3>Investment</h3>
                    <div class="pricing-list">
{pricing_html}
                    </div>

                    <div style="margin-top: 30px; padding: 20px; background: #f9f7f3; border-left: 4px solid #d6ad60; border-radius: 8px;">
                        <h4>Recommended Course</h4>
                        <p><strong>{course}</strong></p>
                        <p style="margin-top: 10px; color: #666;"><strong>Maintenance:</strong> {maintenance}</p>
                    </div>
                </div>

                <!-- Contact Column -->
                <div>
                    <h3>Ready to Book?</h3>
                    <p>Contact us for a consultation to determine the best treatment plan for your needs.</p>
                    
                    <form id="treatment-contact-form" style="margin-top: 25px; display: flex; flex-direction: column; gap: 15px;">
                        <div>
                            <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Lato', sans-serif;">
                        </div>
                        <div>
                            <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Lato', sans-serif;">
                        </div>
                        <div>
                            <input type="tel" name="phone" placeholder="Your Phone" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Lato', sans-serif;">
                        </div>
                        <div>
                            <textarea name="message" placeholder="Tell us about your goals..." rows="5" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Lato', sans-serif;"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Send Inquiry</button>
                    </form>

                    <p style="margin-top: 20px; color: #999; font-size: 12px;">Or call us directly at your preferred time.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         FOOTER
         ============================================ -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Mili Skin & Beauty</h4>
                    <p>Premium skincare and beauty treatments in London</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../index.html#services">Services</a></li>
                        <li><a href="../faq.html">FAQ</a></li>
                        <li><a href="../index.html#contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Follow Us</h4>
                    <ul>
                        <li><a href="#">Instagram</a></li>
                        <li><a href="#">Facebook</a></li>
                        <li><a href="#">TikTok</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Mili Skin & Beauty. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="../script.js"></script>
</body>
</html>
'''
    
    return html_content

# Generate all pages
if __name__ == "__main__":
    for filename, config in TREATMENTS.items():
        html = generate_html(filename, config)
        filepath = os.path.join(BASE_DIR, f"{filename}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Created: {filename}.html")
    
    print(f"\n✓ Successfully created {len(TREATMENTS)} treatment pages!")
