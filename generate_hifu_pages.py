#!/usr/bin/env python3
"""
Generate 13 HIFU treatment pages based on hydrofacial.html template structure
with customized titles, taglines, and pricing.
"""

import os

# HIFU treatments with pricing
HIFU_TREATMENTS = [
    {
        "filename": "hifu-face.html",
        "title": "HIFU Face Lift",
        "tagline": "Advanced non-invasive skin lifting and tightening for a youthful complexion",
        "single": "£199",
        "triple": "£549",
        "six": "£999",
        "description": "The HIFU Face Lift treatment uses advanced ultrasound technology to safely lift and tighten facial skin. This non-invasive procedure stimulates collagen production deep within the skin, resulting in a naturally lifted appearance without surgery or downtime. Perfect for restoring youthful contours and improving skin elasticity.",
        "description_extended": "HIFU (High-Intensity Focused Ultrasound) delivers focused energy precisely to the target areas, encouraging the skin's natural regeneration process. The Face Lift treatment addresses sagging skin, loss of definition, and fine lines, providing dramatic lifting results that improve over time.",
        "benefits": ["Visible lifting effect", "No surgery required", "Collagen remodeling", "Natural results", "Long-lasting", "All skin types"]
    },
    {
        "filename": "hifu-neck.html",
        "title": "HIFU Neck Lift",
        "tagline": "Tighten and tone your neck with advanced ultrasound technology",
        "single": "£149",
        "triple": "£399",
        "six": "£749",
        "description": "The HIFU Neck Lift targets the delicate neck area, which often shows signs of ageing first. This treatment tightens loose skin, reduces crepey texture, and restores definition to the jawline and neck contour. Non-invasive and painless, it's an excellent alternative to surgical neck lift procedures.",
        "description_extended": "The neck is one of the most neglected areas in skincare routines, yet it's highly visible and prone to showing signs of age. This HIFU treatment specifically targets the neck and décolletage to lift, tighten, and rejuvenate the area.",
        "benefits": ["Tightens loose skin", "Improves jawline definition", "Reduces crepey texture", "No downtime", "Painless procedure", "Immediate visible results"]
    },
    {
        "filename": "hifu-face-neck.html",
        "title": "HIFU Face & Neck",
        "tagline": "Complete facial and neck lifting and tightening in one transformative treatment",
        "single": "£299",
        "triple": "£799",
        "six": "£1499",
        "description": "Combine the benefits of facial lifting with neck tightening in this comprehensive treatment. The HIFU Face & Neck package addresses the entire face and neck area, creating a harmonious lift and rejuvenation from jawline to décolletage. This full-face approach provides cohesive, natural-looking results.",
        "description_extended": "Treating the face and neck together ensures a seamless, integrated result. This comprehensive approach lifts the entire face while simultaneously tightening the neck area, creating a more youthful, balanced appearance. Ideal for those seeking complete facial rejuvenation.",
        "benefits": ["Full face and neck coverage", "Harmonious lifting effect", "Improved jaw definition", "Tightened neck area", "Comprehensive rejuvenation", "Professional results"]
    },
    {
        "filename": "hifu-jawline.html",
        "title": "HIFU Jawline Definition",
        "tagline": "Sculpt and define your jawline with precision ultrasound technology",
        "single": "£179",
        "triple": "£479",
        "six": "£899",
        "description": "The HIFU Jawline Definition treatment is specifically designed to enhance and define the lower face. By tightening loose skin and lifting the jawline, this treatment creates sharper definition, reduces jowls, and restores youthful facial contours. It's an excellent non-surgical alternative to chin and jawline enhancement procedures.",
        "description_extended": "A well-defined jawline is often associated with youth and vitality. This targeted HIFU treatment precisely focuses on the jawline area to remove sagging skin, lift the jowls, and create crisp definition. The results are subtle yet dramatic, enhancing your natural features.",
        "benefits": ["Sharp jawline definition", "Reduces jowling", "Lifts lower face", "Non-invasive sculpting", "Natural enhancement", "Long-lasting results"]
    },
    {
        "filename": "hifu-butt-lift.html",
        "title": "HIFU Butt Lift",
        "tagline": "Non-invasive lifting and tightening for a more lifted, youthful appearance",
        "single": "£299",
        "triple": "£799",
        "six": "£1499",
        "description": "The HIFU Butt Lift treatment uses advanced ultrasound technology to lift and tighten the gluteal area without surgery. This non-invasive procedure tightens loose skin, improves shape, and enhances firmness. Perfect for those seeking a more lifted, youthful appearance without the risks and recovery time of surgical procedures.",
        "description_extended": "HIFU technology stimulates collagen production deep within the buttock tissues, encouraging natural skin tightening and lifting. This treatment is ideal for addressing sagging skin, loss of firmness, and improving overall contour in the buttock area.",
        "benefits": ["Lifted appearance", "Improved firmness", "No surgical risks", "No downtime", "Skin tightening", "Long-lasting lift"]
    },
    {
        "filename": "hifu-breast-lift.html",
        "title": "HIFU Breast Lift",
        "tagline": "Achieve natural breast lifting without surgery using advanced ultrasound technology",
        "single": "£349",
        "triple": "£949",
        "six": "£1799",
        "description": "The HIFU Breast Lift is a non-surgical solution for breast sagging and loss of firmness. This innovative treatment uses focused ultrasound energy to tighten skin, improve shape, and enhance lift in the breast area. It's an excellent alternative for those seeking natural enhancement without implants or surgery.",
        "description_extended": "As skin loses elasticity over time, breast tissue can lose firmness and lift. This HIFU treatment specifically targets the breast area to stimulate collagen remodeling and skin tightening, resulting in a naturally lifted appearance that improves progressively.",
        "benefits": ["Natural lift effect", "Improved firmness", "Non-surgical option", "No implants needed", "Gradual improvement", "Safe and effective"]
    },
    {
        "filename": "hifu-stomach.html",
        "title": "HIFU Stomach Tightening",
        "tagline": "Tighten and tone your abdominal area for a smoother, more defined contour",
        "single": "£279",
        "triple": "£749",
        "six": "£1399",
        "description": "The HIFU Stomach Tightening treatment targets loose skin and loss of elasticity in the abdominal area. Using advanced ultrasound technology, this non-invasive procedure tightens skin, improves definition, and enhances overall abdominal contour without surgery. Ideal for post-pregnancy skin tightening or general abdominal contouring.",
        "description_extended": "The stomach area is prone to sagging skin due to weight fluctuations, pregnancy, or natural ageing. This HIFU treatment stimulates collagen production and skin tightening, resulting in improved texture, firmness, and a smoother abdominal appearance.",
        "benefits": ["Skin tightening", "Improved definition", "No surgery required", "Post-pregnancy friendly", "Smooth contour", "Progressive improvement"]
    },
    {
        "filename": "hifu-love-handles.html",
        "title": "HIFU Love Handles",
        "tagline": "Target and tighten the flanks with precision ultrasound technology",
        "single": "£199",
        "triple": "£549",
        "six": "£999",
        "description": "The HIFU Love Handles treatment specifically targets the side abdominal area, reducing sagging skin and improving definition around the flanks. This non-invasive procedure tightens loose skin, enhances body contouring, and creates a smoother silhouette. Perfect for those seeking to improve waistline definition.",
        "description_extended": "Love handles can be stubborn areas of loose skin and loss of firmness. This targeted HIFU treatment focuses energy precisely on the flank area to tighten skin and improve the overall waistline appearance, complementing abdominal treatments perfectly.",
        "benefits": ["Targeted flank tightening", "Improved waistline", "Skin firming", "Enhanced definition", "Non-invasive", "Visible results"]
    },
    {
        "filename": "hifu-inner-thighs.html",
        "title": "HIFU Inner Thighs",
        "tagline": "Lift and tighten inner thigh skin for improved appearance and confidence",
        "single": "£249",
        "triple": "£649",
        "six": "£1199",
        "description": "The HIFU Inner Thighs treatment addresses sagging skin and loss of elasticity in this delicate area. Using focused ultrasound energy, this non-invasive procedure tightens and lifts the inner thigh skin, improving texture and creating a more youthful appearance. No surgery, no downtime.",
        "description_extended": "The inner thigh area is often affected by loose skin due to weight loss, ageing, or pregnancy. This HIFU treatment specifically targets this area to stimulate collagen production and skin tightening, resulting in smoother, firmer-looking thighs.",
        "benefits": ["Thigh skin tightening", "Improved firmness", "Lifted appearance", "No surgery needed", "Smooth texture", "Enhanced confidence"]
    },
    {
        "filename": "hifu-outer-thighs.html",
        "title": "HIFU Outer Thighs",
        "tagline": "Tighten and tone your outer thighs for a sleeker, more defined leg contour",
        "single": "£249",
        "triple": "£649",
        "six": "£1199",
        "description": "The HIFU Outer Thighs treatment targets the lateral thigh area, addressing cellulite appearance and improving skin texture and firmness. This non-invasive ultrasound treatment tightens loose skin and enhances leg contour, creating a smoother, more toned appearance.",
        "description_extended": "The outer thigh is a common area for cellulite and loose skin. This HIFU treatment uses advanced ultrasound technology to tighten the skin, improve texture, and enhance the overall appearance of the thighs for a sleeker silhouette.",
        "benefits": ["Cellulite appearance reduction", "Skin tightening", "Improved texture", "Enhanced leg contour", "Non-invasive", "Gradual improvement"]
    },
    {
        "filename": "hifu-banana-rolls.html",
        "title": "HIFU Banana Rolls",
        "tagline": "Target the under-buttock area with precision ultrasound lifting and tightening",
        "single": "£199",
        "triple": "£549",
        "six": "£999",
        "description": "The HIFU Banana Rolls treatment specifically targets the crease area beneath the buttocks, improving lift and tightness. This non-invasive procedure tightens loose skin and enhances the transition between the buttocks and thighs, creating a more youthful and defined appearance.",
        "description_extended": "The banana roll area can develop loose skin and loss of definition. This targeted HIFU treatment focuses ultrasound energy on this specific region to tighten skin and improve lift, creating a more seamless, youthful contour.",
        "benefits": ["Targets under-buttock area", "Improves lift", "Tightens loose skin", "Enhanced definition", "Non-invasive", "Noticeable results"]
    },
    {
        "filename": "hifu-arms.html",
        "title": "HIFU Arms",
        "tagline": "Tighten and tone sagging arm skin for sleeker, more defined arms",
        "single": "£199",
        "triple": "£549",
        "six": "£999",
        "description": "The HIFU Arms treatment addresses sagging skin and loss of firmness in the upper arm area. Using advanced ultrasound technology, this non-invasive procedure tightens arm skin, improves definition, and creates a more sculpted appearance. Perfect for those seeking arm contouring without surgery.",
        "description_extended": "Arm skin can lose elasticity and sag with age or weight changes. This HIFU treatment stimulates collagen production and skin tightening in the arm area, resulting in firmer, more toned-looking arms without surgery or downtime.",
        "benefits": ["Arm skin tightening", "Improved firmness", "Enhanced definition", "Sculpted appearance", "No surgery needed", "Sleeker arms"]
    },
    {
        "filename": "hifu-stomach-love-handles.html",
        "title": "HIFU Stomach + Love Handles Bundle",
        "tagline": "Complete abdominal and flank contouring with our premium bundle treatment",
        "single": "£449",
        "triple": "£1199",
        "six": "£2299",
        "description": "The HIFU Stomach + Love Handles Bundle combines two treatments in one comprehensive package for maximum abdominal and flank contouring. This complete body tightening solution addresses the entire midsection, tightening loose skin, improving definition, and creating a smoother, more sculpted silhouette.",
        "description_extended": "Treating the stomach and love handles together ensures cohesive results across the entire midsection. This premium bundle package allows for comprehensive contouring with the ultrasound energy precisely distributed to both areas for maximum impact and efficiency.",
        "benefits": ["Complete midsection coverage", "Comprehensive contouring", "Better value than separate", "Integrated results", "Full abdominal tightening", "Professional sculpting"]
    }
]

# HTML Template
def generate_hifu_page(treatment):
    """Generate HTML for a HIFU treatment page"""
    
    single_price = treatment['single']
    triple_price = treatment['triple']
    six_price = treatment['six']
    title = treatment['title']
    tagline = treatment['tagline']
    desc = treatment['description']
    desc_ext = treatment['description_extended']
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} treatment at Mili Skin & Beauty - {tagline} Book your treatment in 13b Edinburgh Cl, London E2 9NY.">
    <meta name="keywords" content="HIFU, {title}, skin tightening, body contouring, 13b Edinburgh Cl, London E2 9NY">
    <meta property="og:title" content="{title} - Mili Skin & Beauty">
    <meta property="og:description" content="{tagline}">
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
                        <li><a href="https://that-time.co.uk/mili-skinbeauty" target="_blank" rel="noopener noreferrer" class="nav-link book-btn">Book Now</a></li>
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

    <!-- Premium Treatment Categories Navigation -->
    <nav class="treatment-mega-nav">
        <div class="container">
            <div class="mega-nav-wrapper">
                
                <!-- HIFU Category -->
                <div class="mega-category">
                    <button class="mega-category-trigger" aria-expanded="false" aria-controls="hifu-mega-menu">
                        <div class="trigger-content">
                            <i class="fas fa-heartbeat"></i>
                            <span>HIFU Treatments</span>
                        </div>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="mega-menu" id="hifu-mega-menu" aria-hidden="true">
                        <div class="mega-menu-content">
                            <div class="mega-menu-header">
                                <h3>HIFU – Advanced Skin Tightening</h3>
                                <p>Non-invasive lifting and tightening for face, neck, and body</p>
                            </div>
                            <div class="mega-menu-grid">
                                <ul class="mega-menu-column">
                                    <li class="column-title">Face & Neck</li>
                                    <li><a href="hifu-face.html">HIFU Face</a></li>
                                    <li><a href="hifu-neck.html">HIFU Neck</a></li>
                                    <li><a href="hifu-face-neck.html">HIFU Face and Neck</a></li>
                                    <li><a href="hifu-jawline.html">HIFU Jawline Definition</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Body Treatments</li>
                                    <li><a href="hifu-butt-lift.html">HIFU Butt Lift</a></li>
                                    <li><a href="hifu-breast-lift.html">HIFU Breast Lift</a></li>
                                    <li><a href="hifu-stomach.html">HIFU Stomach Tightening</a></li>
                                    <li><a href="hifu-love-handles.html">HIFU Love Handles</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Legs & Areas</li>
                                    <li><a href="hifu-inner-thighs.html">HIFU Inner Thighs</a></li>
                                    <li><a href="hifu-outer-thighs.html">HIFU Outer Thighs</a></li>
                                    <li><a href="hifu-banana-rolls.html">HIFU Banana Rolls</a></li>
                                    <li><a href="hifu-arms.html">HIFU Arms</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Bundles</li>
                                    <li><a href="hifu-stomach-love-handles.html">Stomach + Love Handles</a></li>
                                    <li><a href="hifu-face.html">Popular: Full Face</a></li>
                                    <li class="mega-menu-cta"><a href="../index.html#contact" class="btn btn-sm">Book Consultation</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Facial Treatments Category -->
                <div class="mega-category">
                    <button class="mega-category-trigger" aria-expanded="false" aria-controls="facial-mega-menu">
                        <div class="trigger-content">
                            <i class="fas fa-spa"></i>
                            <span>Facial Treatments</span>
                        </div>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="mega-menu" id="facial-mega-menu" aria-hidden="true">
                        <div class="mega-menu-content">
                            <div class="mega-menu-header">
                                <h3>Facial Treatments</h3>
                                <p>Advanced facials for cleansing, rejuvenation, and skin transformation</p>
                            </div>
                            <div class="mega-menu-grid">
                                <ul class="mega-menu-column">
                                    <li class="column-title">Hydration & Glow</li>
                                    <li><a href="../hydrofacial.html">Skin Glow: Hydrofacial</a></li>
                                    <li><a href="../korean-facial.html">Skin Glass: Korean Facial</a></li>
                                    <li><a href="../oxygeno-facial.html">Skin Oxyglow: OxygenO Facial</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Renewal & Peels</li>
                                    <li><a href="../biorepeel.html">Skin Radiance: BioRePeel</a></li>
                                    <li><a href="../biomicroneedling.html">Green Peel – BioMicroneedling</a></li>
                                    <li><a href="../chemical-peel.html">Skin Renewal: Chemical Peel</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Advanced Tech</li>
                                    <li><a href="../microneedling-biorepeel.html">Skin Revive: Microneedling + BioRePeel</a></li>
                                    <li><a href="../rf-facial.html">Skin LumaLift: Radio Frequency Facial</a></li>
                                    <li><a href="../ultimate-exfoliation.html">Skin Luxe Satin: Ultimate Exfoliation</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Specialty</li>
                                    <li><a href="../bb-glow.html">Skin Balance: BB Glow</a></li>
                                    <li><a href="../blackhead-extraction.html">Deep Blackhead Extraction</a></li>
                                    <li class="mega-menu-cta"><a href="../index.html#contact" class="btn btn-sm">Book Treatment</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </nav>

    <!-- ============================================
         SECTION 1: HERO
         ============================================ -->
    <section class="treatment-hero" style="background-image: url('../images/hifu-hero.jpg');">
        <div class="treatment-container">
            <h1>{title}</h1>
            <p class="tagline">{tagline}</p>
            
            <div class="hero-cta-buttons">
                <a href="#section-pricing" class="btn btn-primary">Book Now</a>
                <a href="#section-benefits" class="btn btn-secondary">See Benefits</a>
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
                <li class="subnav-item"><a href="#section-results" class="subnav-link">Results</a></li>
                <li class="subnav-item"><a href="#section-steps" class="subnav-link">How It Works</a></li>
                <li class="subnav-item"><a href="#section-pricing" class="subnav-link">Pricing</a></li>
                <li class="subnav-item"><a href="#section-faqs" class="subnav-link">FAQs</a></li>
                <li class="subnav-item"><a href="#section-related" class="subnav-link">Related</a></li>
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
                    <p>{desc}</p>
                    <p>{desc_ext}</p>
                    <p>The treatment works by delivering focused ultrasound energy to the precise depths within the skin and underlying tissues, stimulating the production of new collagen and elastin. This natural biological response results in progressive skin tightening, lifting, and improved texture over several weeks.</p>
                </div>
                
                <div class="about-features">
                    <h3>Key Benefits</h3>
                    <div class="about-badges">
"""
    
    # Add benefits as badges
    for benefit in treatment['benefits']:
        html += f'                        <div class="badge">{benefit}</div>\n'
    
    html += """                    </div>
                </div>
            </div>

            <!-- Inline Gallery (3 images) -->
            <div class="gallery-grid">
                <div class="gallery-item">
                    <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 3: BENEFITS GRID
         ============================================ -->
    <section id="section-benefits" class="treatment-section" style="background: var(--neutral-surface);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Benefits of This Treatment</h2>
                <p>Discover what makes HIFU special</p>
            </div>
            
            <div class="benefits-grid">
                <div class="benefit-card">
                    <div class="icon"><i class="fas fa-bolt"></i></div>
                    <h4>Visible Lifting</h4>
                    <p>See progressive lifting and tightening results that improve over several weeks.</p>
                </div>
                
                <div class="benefit-card">
                    <div class="icon"><i class="fas fa-clock"></i></div>
                    <h4>No Downtime</h4>
                    <p>Return to daily activities immediately with no recovery period required.</p>
                </div>
                
                <div class="benefit-card">
                    <div class="icon"><i class="fas fa-heart"></i></div>
                    <h4>Non-Invasive</h4>
                    <p>Advanced ultrasound technology delivers results without surgery or needles.</p>
                </div>
                
                <div class="benefit-card">
                    <div class="icon"><i class="fas fa-droplet"></i></div>
                    <h4>Natural Results</h4>
                    <p>Achieve a naturally lifted appearance that enhances your existing features.</p>
                </div>

                <div class="benefit-card">
                    <div class="icon"><i class="fas fa-gem"></i></div>
                    <h4>Collagen Stimulation</h4>
                    <p>Triggers your body's natural collagen production for long-lasting improvement.</p>
                </div>

                <div class="benefit-card">
                    <div class="icon"><i class="fas fa-check-circle"></i></div>
                    <h4>Long-Lasting</h4>
                    <p>Results continue to improve and last up to 12 months with proper maintenance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 4: RESULTS (Before/After Carousel)
         ============================================ -->
    <section id="section-results" class="treatment-section">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Real Results</h2>
                <p>See the transformation for yourself</p>
            </div>

            <div class="results-carousel">
                <div class="carousel-container">
                    <div class="carousel-slide active">
                        <div class="gallery-placeholder" style="background: linear-gradient(135deg, #f9f7f3 0%, #f5f1e8 100%);"><i class="fas fa-image"></i></div>
                        <div class="carousel-content">
                            <p>Client result: Visible lifting and tightening with improved contour</p>
                        </div>
                    </div>
                    
                    <div class="carousel-slide">
                        <div class="gallery-placeholder" style="background: linear-gradient(135deg, #f9f7f3 0%, #f5f1e8 100%);"><i class="fas fa-image"></i></div>
                        <div class="carousel-content">
                            <p>Progressive improvement in skin firmness and definition over time</p>
                        </div>
                    </div>
                    
                    <div class="carousel-slide">
                        <div class="gallery-placeholder" style="background: linear-gradient(135deg, #f9f7f3 0%, #f5f1e8 100%);"><i class="fas fa-image"></i></div>
                        <div class="carousel-content">
                            <p>Enhanced natural contour with lifted, rejuvenated appearance</p>
                        </div>
                    </div>
                </div>

                <div class="carousel-controls">
                    <button class="carousel-button" data-carousel-prev aria-label="Previous result">
                        <i class="fas fa-chevron-left"></i>
                    </button>
                    <div class="carousel-dots">
                        <div class="dot active"></div>
                        <div class="dot"></div>
                        <div class="dot"></div>
                    </div>
                    <button class="carousel-button" data-carousel-next aria-label="Next result">
                        <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 5: STEP-BY-STEP (Accordion)
         ============================================ -->
    <section id="section-steps" class="treatment-section" style="background: var(--neutral-surface);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>How the Treatment Works</h2>
                <p>Step-by-step breakdown of your treatment journey</p>
            </div>

            <div class="accordion steps-accordion">
                <div class="accordion-item open">
                    <div class="accordion-header">
                        <h4>1. Consultation & Assessment</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>We begin with a thorough consultation where we understand your goals, assess your skin condition, and determine if HIFU is suitable for you. Our specialists will discuss expected results and create a personalized treatment plan.</p>
                            <p><strong>Duration:</strong> 15-20 minutes</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>2. Pre-Treatment Preparation</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>The treatment area is cleansed and prepared. A coupling gel is applied to facilitate ultrasound transmission and ensure optimal energy delivery to the target tissues.</p>
                            <p><strong>Duration:</strong> 5-10 minutes</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>3. Treatment Application</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>The HIFU device delivers focused ultrasound energy to the targeted areas. You may feel gentle warmth and slight vibration sensations. The procedure is well-tolerated and requires no anesthesia.</p>
                            <p><strong>Duration:</strong> 30-45 minutes depending on treatment area</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>4. Aftercare & Follow-Up Guidance</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>After treatment, we provide comprehensive aftercare instructions to maximize your results. The area may feel slightly warm or tender, which is normal and subsides quickly.</p>
                            <ul>
                                <li>Avoid heat exposure for 24 hours (saunas, hot baths)</li>
                                <li>Apply ice or cool compress if needed for comfort</li>
                                <li>Stay hydrated to support the healing process</li>
                                <li>Use gentle skincare products for 48 hours</li>
                                <li>Avoid strenuous exercise for 48 hours</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

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
                        <div class="pricing-item">
                            <div class="pricing-info">
                                <h4>Single Session</h4>
                                <p>Complete treatment</p>
                            </div>
                            <div class="pricing-price">{single_price}</div>
                        </div>

                        <div class="pricing-item">
                            <div class="pricing-info">
                                <h4>3-Session Course</h4>
                                <p>Best for results</p>
                            </div>
                            <div class="pricing-price">{triple_price}</div>
                        </div>

                        <div class="pricing-item">
                            <div class="pricing-info">
                                <h4>6-Session Course</h4>
                                <p>Maximum benefits</p>
                            </div>
                            <div class="pricing-price">{six_price}</div>
                        </div>

                        <div class="pricing-item">
                            <div class="pricing-info">
                                <h4>Maintenance Session</h4>
                                <p>6-12 months after course</p>
                            </div>
                            <div class="pricing-price">{single_price}</div>
                        </div>
                    </div>
                </div>

                <!-- Enquiry Form Column -->
                <div>
                    <h3>Get in Touch</h3>
                    <form class="enquiry-form" action="../contact.php" method="POST">
                        <input type="hidden" name="treatment" value="{title}">

                        <div class="form-group">
                            <label for="name">Full Name *</label>
                            <input type="text" id="name" name="name" required>
                        </div>

                        <div class="form-group">
                            <label for="email">Email Address *</label>
                            <input type="email" id="email" name="email" required>
                        </div>

                        <div class="form-group">
                            <label for="phone">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required>
                        </div>

                        <div class="form-group">
                            <label for="interested">Interested in *</label>
                            <select id="interested" name="interested" required>
                                <option value="">Select option</option>
                                <option value="Single Session">Single Session - {single_price}</option>
                                <option value="3-Session Course">3-Session Course - {triple_price}</option>
                                <option value="6-Session Course">6-Session Course - {six_price}</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="message">Message or Questions</label>
                            <textarea id="message" name="message" placeholder="Any specific questions about the treatment?"></textarea>
                        </div>

                        <div class="form-checkbox">
                            <input type="checkbox" id="consent" name="consent" required>
                            <label for="consent">I consent to being contacted about my enquiry *</label>
                        </div>

                        <button type="submit" class="form-submit">Send Enquiry</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 7: FAQs (Accordion)
         ============================================ -->
    <section id="section-faqs" class="treatment-section" style="background: var(--neutral-surface);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Frequently Asked Questions</h2>
                <p>Everything you need to know about HIFU treatment</p>
            </div>

            <div class="accordion faqs-accordion">
                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>Is HIFU treatment painful?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Most clients experience minimal discomfort. You may feel gentle warmth and slight vibration, which is completely normal. The sensation is well-tolerated and there is no need for anesthesia or numbing cream.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>How long does the treatment take?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>The treatment typically takes 30-60 minutes depending on the area being treated. Including consultation, the entire appointment is usually 60-90 minutes.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>When will I see results?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Some clients notice immediate mild improvements. However, optimal results develop progressively over 2-3 months as collagen remodeling occurs. Results continue to improve with a series of treatments.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>Is there any downtime?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>No downtime is required. You can return to normal activities immediately after treatment. Mild redness or temporary swelling may occur but typically subsides within a few hours.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>How long do the results last?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Results can last 6-12 months depending on individual factors and lifestyle. Many clients benefit from maintenance treatments every 6-12 months to sustain their results.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>Is HIFU safe?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Yes, HIFU is a FDA-approved and clinically proven treatment with an excellent safety record. It uses non-ionizing ultrasound energy and has been safely used for decades in medical applications.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>Who is suitable for HIFU treatment?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>HIFU is suitable for most adults seeking non-invasive skin tightening and lifting. However, we recommend consultation with our specialists to determine if you're an ideal candidate.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         SECTION 8: RELATED TREATMENTS
         ============================================ -->
    <section id="section-related" class="treatment-section">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Complementary Treatments</h2>
                <p>Explore other HIFU treatments that pair beautifully together</p>
            </div>

            <div class="related-cards-grid">
                <div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">HIFU Face Lift</h4>
                        <p class="related-card-desc">Advanced non-invasive skin lifting and tightening for a youthful complexion.</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">From £199</span>
                        </div>
                        <a href="hifu-face.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>

                <div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">HIFU Neck Lift</h4>
                        <p class="related-card-desc">Tighten and tone your neck with advanced ultrasound technology.</p>
                        <div class="related-card-meta">
                            <span>30 mins</span>
                            <span class="related-card-price">From £149</span>
                        </div>
                        <a href="hifu-neck.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>

                <div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin Glow: Hydrofacial</h4>
                        <p class="related-card-desc">Deep cleansing, hydration, and instant radiance with professional technology.</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">From £99</span>
                        </div>
                        <a href="../hydrofacial.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Mili Skin & Beauty</h3>
                    <p>Your trusted partner for advanced skin care treatments in London.</p>
                    <div class="social-links">
                        <a href="https://www.instagram.com/mili.skin.beauty" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                        <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
                            <i class="fab fa-facebook"></i>
                        </a>
                        <a href="mailto:Militest@gmail.com" aria-label="Email">
                            <i class="fas fa-envelope"></i>
                        </a>
                    </div>
                </div>

                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="../index.html#home">Home</a></li>
                        <li><a href="../index.html#about">About</a></li>
                        <li><a href="../index.html#services">Services</a></li>
                        <li><a href="../index.html#price-list">Price List</a></li>
                        <li><a href="../index.html#contact">Contact</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Contact Info</h4>
                    <ul class="footer-contact">
                        <li><i class="fas fa-map-marker-alt"></i> <a href="https://www.google.com/maps/search/13b+Edinburgh+Cl,+London+E2+9NY" target="_blank" rel="noopener noreferrer">13b Edinburgh Cl, London E2 9NY</a></li>
                        <li><i class="fas fa-phone"></i> <a href="tel:+447346001219">07346 001219</a></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:Militest@gmail.com">Militest@gmail.com</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Opening Hours</h4>
                    <ul class="footer-hours">
                        <li>Tue - Fri: 9:00 AM - 7:00 PM</li>
                        <li>Saturday: 10:00 AM - 6:00 PM</li>
                        <li>Sunday & Monday: Closed</li>
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
    <script src="../treatment-components.js"></script>
</body>
</html>
"""
    return html


def main():
    """Generate all HIFU pages"""
    treatments_dir = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty\treatments"
    
    # Ensure treatments directory exists
    os.makedirs(treatments_dir, exist_ok=True)
    
    generated_count = 0
    
    for treatment in HIFU_TREATMENTS:
        filepath = os.path.join(treatments_dir, treatment['filename'])
        html_content = generate_hifu_page(treatment)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        generated_count += 1
        print(f"✓ Generated: {treatment['filename']}")
    
    print(f"\n✅ Successfully generated {generated_count} HIFU treatment pages!")
    print(f"📁 Location: {treatments_dir}")


if __name__ == "__main__":
    main()
