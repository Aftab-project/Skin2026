import os
from textwrap import dedent

OUTPUT_DIR = r"c:\\Users\\t-aftabkhan\\OneDrive - Microsoft\\Desktop\\MiliSkin&Beauty - Copy (2)\\treatments"

TEMPLATE = dedent('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="facial, skincare, {title}, Mili Skin & Beauty, London">
    <meta property="og:title" content="{title} - Mili Skin & Beauty">
    <meta property="og:description" content="{meta_desc}">
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
    <header class="header">
        <nav class="navbar">
            <div class="container">
                <div class="nav-wrapper">
                    <a href="../index.html#home" class="logo">
                        <span class="logo-text">Mili Skin & Beauty</span>
                    </a>
                    <button class="mobile-menu-toggle" aria-label="Toggle Menu">
                        <span></span><span></span><span></span>
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

    <nav class="treatment-mega-nav">
        <div class="container">
            <div class="mega-nav-wrapper">
                <div class="mega-category">
                    <button class="mega-category-trigger" aria-expanded="false" aria-controls="facials-skincare-mega-menu">
                        <div class="trigger-content">
                            <i class="fas fa-hand-holding-droplet"></i>
                            <span>Facials & Skincare</span>
                        </div>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="mega-menu" id="facials-skincare-mega-menu" aria-hidden="true">
                        <div class="mega-menu-content">
                            <div class="mega-menu-header">
                                <h3>Facials & Skincare</h3>
                                <p>Advanced facials for cleansing, rejuvenation, and skin transformation</p>
                            </div>
                            <div class="mega-menu-grid">
                                <ul class="mega-menu-column">
                                    <li class="column-title">Hydration & Glow</li>
                                    <li><a href="skin-glow-hydrofacial.html">Skin Glow: HydroFacial</a></li>
                                    <li><a href="skin-glass-korean-facial.html">Skin Glass: Korean Facial</a></li>
                                    <li><a href="skin-oxyglow-oxygen-facial.html">Skin OxyGlow: Oxygen Facial</a></li>
                                    <li><a href="skin-illumine-hydrofacial-ultra.html">Skin Illumine: HydroFacial Ultra</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Renewal & Peels</li>
                                    <li><a href="skin-radiance-biorepeel.html">Skin Radiance: BioRePeel</a></li>
                                    <li><a href="green-peel-bio-microneedling.html">Green Peel – Bio Microneedling</a></li>
                                    <li><a href="skin-renewal-chemical-peel.html">Skin Renewal: Chemical Peel</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Advanced Tech</li>
                                    <li><a href="skin-revive-microneedling-biorepeel.html">Skin Revive: Microneedling + BioRePeel</a></li>
                                    <li><a href="skin-luma-lift-rf-facial.html">Skin Luma Lift: RF Facial</a></li>
                                    <li><a href="skin-luxe-satin-ultimate-exfoliation.html">Skin Luxe Satin: Ultimate Exfoliation</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Specialty</li>
                                    <li><a href="skin-balance-bb-glow.html">Skin Balance: BB Glow</a></li>
                                    <li><a href="deep-blackhead-extraction.html">Deep Blackhead Extraction</a></li>
                                    <li class="mega-menu-cta"><a href="../index.html#contact" class="btn btn-sm">Book Treatment</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="mega-category">
                    <button class="mega-category-trigger" aria-expanded="false" aria-controls="hifu-treatments-mega-menu">
                        <div class="trigger-content">
                            <i class="fas fa-heart-pulse"></i>
                            <span>HIFU Treatments</span>
                        </div>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="mega-menu" id="hifu-treatments-mega-menu" aria-hidden="true">
                        <div class="mega-menu-content">
                            <div class="mega-menu-header">
                                <h3>HIFU Treatments</h3>
                                <p>Non-invasive lifting and tightening for face, neck, and body</p>
                            </div>
                            <div class="mega-menu-grid">
                                <ul class="mega-menu-column">
                                    <li class="column-title">Face & Neck</li>
                                    <li><a href="hifu-face.html">HIFU Face</a></li>
                                    <li><a href="hifu-neck.html">HIFU Neck</a></li>
                                    <li><a href="hifu-face-neck.html">HIFU Face + Neck</a></li>
                                    <li><a href="hifu-jawline.html">HIFU Jawline</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Midsection & Arms</li>
                                    <li><a href="hifu-stomach.html">HIFU Stomach</a></li>
                                    <li><a href="hifu-love-handles.html">HIFU Love Handles</a></li>
                                    <li><a href="hifu-stomach-love-handles.html">HIFU Stomach + Love Handles</a></li>
                                    <li><a href="hifu-arms.html">HIFU Arms (Bingo Wings)</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Lift & Curves</li>
                                    <li><a href="hifu-butt-lift.html">HIFU Butt Lift</a></li>
                                    <li><a href="hifu-breast-lift.html">HIFU Breast Lift</a></li>
                                    <li><a href="hifu-banana-rolls.html">HIFU Banana Rolls</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Legs & Thighs</li>
                                    <li><a href="hifu-inner-thighs.html">HIFU Inner Thighs</a></li>
                                    <li><a href="hifu-outer-thighs.html">HIFU Outer Thighs</a></li>
                                    <li><a href="hifu-face.html">Popular: Full Face</a></li>
                                    <li class="mega-menu-cta"><a href="../index.html#contact" class="btn btn-sm">Book Consultation</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="mega-category">
                    <button class="mega-category-trigger" aria-expanded="false" aria-controls="microneedling-rf-mega-menu">
                        <div class="trigger-content">
                            <i class="fas fa-syringe"></i>
                            <span>Microneedling RF</span>
                        </div>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="mega-menu" id="microneedling-rf-mega-menu" aria-hidden="true">
                        <div class="mega-menu-content">
                            <div class="mega-menu-header">
                                <h3>Microneedling RF</h3>
                                <p>Collagen-stimulating microneedling, RF, and resurfacing treatments</p>
                            </div>
                            <div class="mega-menu-grid">
                                <ul class="mega-menu-column">
                                    <li class="column-title">Microneedling & RF</li>
                                    <li><a href="skin-revive-microneedling-biorepeel.html">Microneedling + BioRePeel</a></li>
                                    <li><a href="green-peel-bio-microneedling.html">Green Peel – Bio Microneedling</a></li>
                                    <li><a href="skin-luma-lift-rf-facial.html">Radio Frequency Facial</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Resurfacing & Peels</li>
                                    <li><a href="skin-luxe-satin-ultimate-exfoliation.html">Ultimate Exfoliation</a></li>
                                    <li><a href="skin-renewal-chemical-peel.html">Chemical Peel</a></li>
                                    <li><a href="skin-radiance-biorepeel.html">BioRePeel</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Targeted Care</li>
                                    <li><a href="skin-oxyglow-oxygen-facial.html">Oxygen Facial</a></li>
                                    <li><a href="skin-glass-korean-facial.html">Korean Facial</a></li>
                                    <li><a href="skin-glow-hydrofacial.html">HydroFacial</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="mega-menu-cta"><a href="../index.html#contact" class="btn btn-sm">Book Treatment</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <section class="treatment-hero" style="background-image: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url('../images/hifu-hero.jpg'); background-size: cover; background-position: center;">
        <div class="treatment-container">
            <h1 style="color: #fff; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);">{title}</h1>
            <p class="tagline" style="color: #f0f0f0; text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);">{tagline}</p>
            <div class="hero-cta-buttons">
                <a href="#section-pricing" class="btn btn-primary">Book Now</a>
                <a href="#section-benefits" class="btn btn-secondary" style="background-color: #6B5437; color: #fff; border-color: #6B5437;">See Benefits</a>
            </div>
        </div>
    </section>

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

    <section id="section-about" class="treatment-section">
        <div class="treatment-container">
            <div class="about-layout">
                <div class="about-content">
                    <h3>About This Treatment</h3>
{about_html}
                </div>
                <div class="about-features">
                    <h3>Key Benefits</h3>
                    <div class="about-badges">
{badges_html}                    </div>
                </div>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item"><img src="../images/SkinGlowydrofacial.webp" alt="Treatment in progress" loading="lazy"></div>
                <div class="gallery-item"><img src="../images/Hydrafacial.jpg" alt="Device cleansing skin" loading="lazy"></div>
                <div class="gallery-item"><img src="../images/skinreviewtopuo.png" alt="Glowing result close-up" loading="lazy"></div>
            </div>
        </div>
    </section>

    <section id="section-benefits" class="treatment-section" style="background: var(--neutral-surface);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Benefits and Real Results of This Treatment</h2>
                <p>Discover what makes {title} special</p>
            </div>
            <div class="benefits-results-wrap">
                <div class="benefits-panel">
                    <div class="benefits-grid">
{benefits_html}                    </div>
                </div>
                <div class="results-panel">
                    <div class="results-card">
                        <div class="results-media">
                            <img src="../images/HydraFacial_Before_and_After.webp" alt="Before and after results" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; border: 6px solid #d6ad60; border-radius: 12px; display: block;">
                        </div>
                        <div class="results-body">
                            <h3>Real Results</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="section-steps" class="treatment-section" style="background: linear-gradient(135deg, #f8f6f1 0%, #faf8f3 100%);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Your Step-by-Step Experience</h2>
                <p>{steps_desc}</p>
            </div>
            <div class="experience-grid">
{steps_html}            </div>
{addons_html}
        </div>
    </section>

    <style>
        .experience-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 35px; margin-top: 45px; }
        .experience-card { background: #fff; padding: 35px 25px; border-radius: 10px; box-shadow: 0 4px 12px rgba(214,173,96,0.12); transition: all 0.3s ease; position: relative; text-align: center; }
        .experience-card:hover { box-shadow: 0 8px 20px rgba(214,173,96,0.2); transform: translateY(-5px); }
        .step-number { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); width: 30px; height: 30px; background: linear-gradient(135deg,#d6ad60,#e5bf77); color: #fff; border-radius: 50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:14px; box-shadow: 0 3px 8px rgba(214,173,96,0.3); }
        .step-icon { font-size: 32px; color: #d6ad60; margin: 15px 0 12px 0; }
        .experience-card h3 { font-size: 16px; font-weight: 600; color: #1a1a1a; margin: 10px 0 8px 0; font-family: 'Playfair Display', serif; }
        .experience-card p { font-size: 13px; color: #666; line-height: 1.5; margin: 0; }
        @media (max-width: 768px) { .experience-grid { grid-template-columns: repeat(2, 1fr); gap: 15px; } .experience-card { padding: 20px 15px; } .experience-card h3 { font-size: 14px; } .experience-card p { font-size: 12px; } }
        @media (max-width: 480px) { .experience-grid { grid-template-columns: 1fr; } }
    </style>

    <section id="section-pricing" class="treatment-section">
        <div class="treatment-container">
            <h2>Pricing & Enquiry</h2>
            <div class="pricing-layout">
                <div>
                    <h3>Investment</h3>
                    <div class="pricing-list">
{pricing_html}                    </div>
                    <p style="margin-top: 12px; font-size: 14px; color: #555;"><strong>Recommended frequency:</strong> {frequency_main}. {frequency_note}</p>
                </div>
                <div>
                    <h3>Get in Touch</h3>
                    <form class="enquiry-form" action="contact.php" method="POST">
                        <input type="hidden" name="treatment" value="{title}">
                        <div class="form-group"><label for="name">Full Name *</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">Email Address *</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="phone">Phone Number *</label><input type="tel" id="phone" name="phone" required></div>
                        <div class="form-group"><label for="interested">Interested in *</label>
                            <select id="interested" name="interested" required>
                                <option value="">Select option</option>
{pricing_options_html}                            </select>
                        </div>
                        <div class="form-group"><label for="message">Message or Questions</label><textarea id="message" name="message" placeholder="Any specific questions about the treatment?"></textarea></div>
                        <div class="form-checkbox"><input type="checkbox" id="consent" name="consent" required><label for="consent">I consent to being contacted about my enquiry *</label></div>
                        <button type="submit" class="form-submit">Send Enquiry</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <section id="section-faqs" class="treatment-section" style="background: var(--neutral-surface);">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Frequently Asked Questions</h2>
                <p>Everything you need to know about {title}</p>
            </div>
            <div class="accordion faqs-accordion">
{faqs_html}            </div>
        </div>
    </section>

    <section id="section-related" class="treatment-section">
        <div class="treatment-container">
            <div class="section-header">
                <h2>Complementary Treatments</h2>
                <p>Explore other facials that pair beautifully with {title}</p>
            </div>
            <div class="related-cards-grid">
                <div class="related-card">
                    <div class="related-card-image"><img src="../images/skin glass korean facial treatment.jpg" alt="Skin Glass Korean Facial Treatment" loading="lazy"></div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin Glass: Korean Facial</h4>
                        <p class="related-card-desc">Multi-step Korean facial for luminous, glass-like skin with advanced serums and techniques.</p>
                        <div class="related-card-meta"><span>60 mins</span><span class="related-card-price">From £99</span></div>
                        <a href="skin-glass-korean-facial.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>
                <div class="related-card">
                    <div class="related-card-image"><img src="../images/BIORPEEL.jpg" alt="BioRePeel Treatment" loading="lazy"></div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin Radiance: BioRePeel</h4>
                        <p class="related-card-desc">Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.</p>
                        <div class="related-card-meta"><span>45 mins</span><span class="related-card-price">From £99</span></div>
                        <a href="skin-radiance-biorepeel.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>
                <div class="related-card">
                    <div class="related-card-image"><img src="../images/oxygenNeo.avif" alt="Oxygen Facial Treatment" loading="lazy"></div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin OxyGlow: Oxygen Facial</h4>
                        <p class="related-card-desc">Oxygen infusion facial for instant glow and deep rejuvenation with premium serums.</p>
                        <div class="related-card-meta"><span>45 mins</span><span class="related-card-price">From £99</span></div>
                        <a href="skin-oxyglow-oxygen-facial.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Mili Skin & Beauty</h3>
                    <p>Your trusted partner for advanced skin care treatments in London.</p>
                    <div class="social-links">
                        <a href="https://www.instagram.com/mili.skin.beauty" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="mailto:Militest@gmail.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
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
            <div class="footer-bottom"><p>&copy; 2025 Mili Skin & Beauty. All rights reserved.</p></div>
        </div>
    </footer>

    <a href="https://wa.me/447346001219" target="_blank" rel="noopener noreferrer" class="whatsapp-button" aria-label="Contact us on WhatsApp"><i class="fab fa-whatsapp"></i></a>
    <script src="../script.js"></script>
    <script src="../treatment-components.js"></script>
</body>
</html>
''')


def render_page(cfg: dict) -> str:
    about_html = "\n".join(f"                    <p>{p}</p>" for p in cfg["about"]) + "\n"
    badges_html = "".join(f"                        <div class=\"badge\">{b}</div>\n" for b in cfg["badges"])
    benefits_html = "".join(
        f"                        <div class=\"benefit-card\">\n"
        f"                            <div class=\"icon\"><i class=\"{b['icon']}\"></i></div>\n"
        f"                            <h4>{b['title']}</h4>\n"
        f"                            <p>{b['desc']}</p>\n"
        f"                        </div>\n" for b in cfg["benefits"]
    )
    steps_html = "".join(
        f"                <div class=\"experience-card\">\n"
        f"                    <div class=\"step-number\">{i+1}</div>\n"
        f"                    <div class=\"step-icon\"><i class=\"{s['icon']}\"></i></div>\n"
        f"                    <h3>{s['title']}</h3>\n"
        f"                    <p>{s['desc']}</p>\n"
        f"                </div>\n\n" for i, s in enumerate(cfg["steps"]))
    addons_html = ""
    if cfg.get("addons"):
        addon_cards = "".join(
            f"                    <div class=\"benefit-card\">\n"
            f"                        <div class=\"icon\"><i class=\"{a['icon']}\"></i></div>\n"
            f"                        <h4>{a['title']}</h4>\n"
            f"                        <p>{a['desc']}</p>\n"
            f"                    </div>\n" for a in cfg["addons"])
        addons_html = f"""
            <div class=\"add-ons-section\" style=\"margin-top: 50px;\">\n                <h3 style=\"text-align: center; margin-bottom: 30px; font-family: 'Playfair Display', serif; color: #1a1a1a;\">Optional Add-Ons</h3>\n                <div class=\"benefits-grid\">\n{addon_cards}                </div>\n            </div>"""
    pricing_html = "".join(
        f"                        <div class=\"pricing-item\">\n"
        f"                            <div class=\"pricing-info\">\n"
        f"                                <h4>{p['name']}</h4>\n"
        f"                                <p>{p['desc']}</p>\n"
        f"                            </div>\n"
        f"                            <div class=\"pricing-price\">{p['price']}</div>\n"
        f"                            <a href=\"https://that-time.co.uk/service/196300/book\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"nav-link book-btn\">Book Now</a>\n"
        f"                        </div>\n" for p in cfg["pricing"])
    pricing_options_html = "".join(
        f"                                <option value=\"{p['name']}\">{p['name']} - {p['price']}</option>\n" for p in cfg["pricing"])
    faqs_html = "".join(
        f"                <div class=\"accordion-item\">\n"
        f"                    <div class=\"accordion-header\">\n"
        f"                        <h4>{f['q']}</h4>\n"
        f"                        <i class=\"fas fa-chevron-down accordion-icon\"></i>\n"
        f"                    </div>\n"
        f"                    <div class=\"accordion-content\">\n"
        f"                        <div class=\"accordion-body\">\n"
        f"                            <p>{f['a']}</p>\n"
        f"                        </div>\n"
        f"                    </div>\n"
        f"                </div>\n" for f in cfg["faqs"])
    # Safely substitute placeholders without using str.format to avoid conflicts with CSS/HTML braces
    html = TEMPLATE
    replacements = {
        "meta_desc": cfg["meta_desc"],
        "title": cfg["title"],
        "tagline": cfg["tagline"],
        "about_html": about_html,
        "badges_html": badges_html,
        "benefits_html": benefits_html,
        "steps_desc": cfg["steps_desc"],
        "steps_html": steps_html,
        "addons_html": addons_html,
        "pricing_html": pricing_html,
        "frequency_main": cfg["frequency_main"],
        "frequency_note": cfg["frequency_note"],
        "pricing_options_html": pricing_options_html,
        "faqs_html": faqs_html,
    }
    for key, value in replacements.items():
        html = html.replace("{" + key + "}", value)
    return html


def write_page(slug: str, html: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, slug)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✔ Wrote {path}")


DATA = [
    {
        "slug": "skin-radiance-biorepeel.html",
        "title": "Skin Radiance: BioRePeel",
        "meta_desc": "BioRePeel at Mili Skin & Beauty – gentle, effective peel for brighter, smoother skin with minimal downtime.",
        "tagline": "Gentle bioactive peel for brighter, smoother skin – £99",
        "about": [
            "BioRePeel is a gentle yet powerful chemical peel that combines exfoliation with bioactive nutrients to rejuvenate the skin from within.",
            "Designed to stimulate collagen production, brighten the complexion, and improve overall skin texture, with minimal downtime and minimal peeling."
        ],
        "badges": ["Cell Renewal", "Brightening", "Collagen Boost", "Minimal Downtime", "All Skin Types"],
        "benefits": [
            {"icon":"fas fa-hand-sparkles","title":"Improves Texture & Smoothness","desc":"Removes dead skin cells and stimulates cell turnover for softer, refined skin."},
            {"icon":"fas fa-sun","title":"Brightens & Evens Tone","desc":"Reduces dullness and helps correct uneven pigmentation."},
            {"icon":"fas fa-clock-rotate-left","title":"Reduces Fine Lines","desc":"Stimulates collagen and elastin to improve firmness and plumpness."},
            {"icon":"fas fa-face-smile","title":"Helps with Acne Marks","desc":"Clears clogged pores and helps improve mild scarring and post-inflammatory marks."},
            {"icon":"fas fa-compress","title":"Minimises Pores","desc":"Clears congestion and smooths the surface for refined pores."},
            {"icon":"fas fa-star","title":"Radiant Glow, Minimal Downtime","desc":"Visible results with little to no recovery time."}
        ],
        "steps_desc": "A tailored 7-step renewal and glow journey",
        "steps": [
            {"icon":"fas fa-user-doctor","title":"Personalised Skin Consultation","desc":"Tailored analysis to customise your BioRePeel for maximum results."},
            {"icon":"fas fa-soap","title":"Purifying Cleanse & Skin Prep","desc":"Deep cleanse removes impurities and primes the skin."},
            {"icon":"fas fa-hand-sparkles","title":"Blackhead & Whitehead Extraction","desc":"Gentle extractions clear congestion and prep for the peel."},
            {"icon":"fas fa-flask","title":"Bio RePeel Application","desc":"Dissolves dull cells, brightens pigmentation, and stimulates collagen."},
            {"icon":"fas fa-droplet","title":"Hyaluronic Acid Hydration Shot","desc":"Concentrated HA delivers instant plumping and dewy hydration."},
            {"icon":"fas fa-face-smile-relaxed","title":"Relaxing Facial Massage","desc":"Boosts circulation and lymphatic drainage for a lifted glow."},
            {"icon":"fas fa-shield-heart","title":"Post-Treatment Glow Shield","desc":"Recovery serums and SPF lock in moisture and protect."}
        ],
        "addons": [
            {"icon":"fas fa-lightbulb","title":"LED Light Therapy – £10","desc":"Enhances collagen, calms inflammation, and boosts radiance."},
            {"icon":"fas fa-mask-face","title":"Hydrating Jelly Mask – £10","desc":"Cooling hydro-jelly mask locks in hydration and soothes."},
            {"icon":"fas fa-dna","title":"Collagen Peptide Booster – £15","desc":"Firms skin and softens fine lines for youthful radiance."},
            {"icon":"fas fa-syringe","title":"Micro-Needling Add-On – £59","desc":"Targets texture and collagen for next-level results."}
        ],
        "pricing": [
            {"name":"Face – 1 Session","price":"£99","desc":"Single BioRePeel treatment."},
            {"name":"Face – 3 Sessions","price":"£267","desc":"Course for optimal renewal."},
            {"name":"Face – 4 Sessions","price":"£336","desc":"Extended package for deeper results."},
            {"name":"Face – 6 Sessions","price":"£475","desc":"Complete transformation course."},
            {"name":"Face & Neck – 1 Session","price":"£149","desc":"BioRePeel for face and neck."},
            {"name":"Face & Neck – 3 Sessions","price":"£401","desc":"Comprehensive renewal course."},
            {"name":"Face & Neck – 4 Sessions","price":"£506","desc":"Extended face and neck package."},
            {"name":"Face & Neck – 6 Sessions","price":"£715","desc":"Full rejuvenation course."}
        ],
        "frequency_main":"Initial: once per week for 3–6 weeks; Maintenance: every 4–6 weeks",
        "frequency_note":"Sensitive skin may adjust to every 10–14 days; support with home care and SPF.",
        "faqs": [
            {"q":"Is BioRePeel suitable for sensitive skin?","a":"Yes. It's designed to be gentle with minimal downtime and tailored strength."},
            {"q":"Will I peel a lot?","a":"Peeling is minimal to moderate depending on your skin and course plan."},
            {"q":"How soon can I wear makeup?","a":"Light mineral makeup can be worn after 24 hours; follow aftercare guidance."}
        ]
    },
    {
        "slug":"green-peel-bio-microneedling.html",
        "title":"Green Peel – Bio Microneedling",
        "meta_desc":"Green Peel Bio Microneedling – natural herbal resurfacing to renew, smooth, and brighten skin.",
        "tagline":"Natural herbal resurfacing for renewal and glow",
        "about":[
            "The Green Peel is a natural, herbal-based skin resurfacing treatment that stimulates regeneration using plant-derived ingredients instead of acids.",
            "A specialised herbal blend is massaged into the skin to activate circulation and natural micro-exfoliation, targeting acne, pigmentation, sun damage, and texture."
        ],
        "badges":["Natural & Herbal","Skin Renewal","Texture Smoothing","Pigment Support","Customisable Strength"],
        "benefits":[
            {"icon":"fas fa-leaf","title":"Skin Renewal & Regeneration","desc":"Stimulates cell turnover to reveal fresher, smoother skin."},
            {"icon":"fas fa-gem","title":"Improved Texture & Tone","desc":"Reduces roughness and dullness for radiant softness."},
            {"icon":"fas fa-bacteria","title":"Acne & Blemish Support","desc":"Helps unclog pores and calm breakouts."},
            {"icon":"fas fa-circle-half-stroke","title":"Pigmentation Reduction","desc":"Supports fading of sun damage and uneven tone."},
            {"icon":"fas fa-face-smile","title":"Fine Line Improvement","desc":"Promotes collagen for firmer, youthful-looking skin."},
            {"icon":"fas fa-seedling","title":"Natural & Customisable","desc":"Botanical ingredients; strength tailored to your skin."}
        ],
        "steps_desc":"Personalised herbal resurfacing with bio-microneedling actions",
        "steps":[
            {"icon":"fas fa-user-doctor","title":"Consultation & Skin Assessment","desc":"Choose the right Green Peel strength for your goals."},
            {"icon":"fas fa-soap","title":"Cleansing & Prep","desc":"Gentle cleanse removes impurities and primes the skin."},
            {"icon":"fas fa-seedling","title":"Herbal Blend Application","desc":"Massage activates circulation and natural exfoliation."},
            {"icon":"fas fa-arrows-rotate","title":"Absorption & Activation","desc":"Herbs stimulate cellular renewal and boost vitality."},
            {"icon":"fas fa-mask-face","title":"Removal & Soothing Mask","desc":"Calms, hydrates, and reduces sensitivity."},
            {"icon":"fas fa-vial-circle-check","title":"Healing Serum & Take-Home Care","desc":"Support hydration and regeneration post-peel."},
            {"icon":"fas fa-sparkles","title":"Peeling & Renewal","desc":"Mild to visible peeling reveals brighter, smoother skin."}
        ],
        "addons":[
            {"icon":"fas fa-lemon","title":"Vitamin C Booster – £15","desc":"Targets dullness and pigmentation for a bright finish."},
            {"icon":"fas fa-droplet","title":"Hyaluronic Acid Serum – £5","desc":"Take-home serum to boost moisture and comfort."}
        ],
        "pricing":[
            {"name":"Green Peel Bio Microneedling – Face","price":"£99","desc":"Herbal resurfacing with bioactive microneedling effects."},
            {"name":"Green Peel Bio Microneedling – 3 Sessions","price":"£267","desc":"Course for cumulative renewal and clarity."},
            {"name":"Green Peel Bio Microneedling – 4 Sessions","price":"£336","desc":"Extended course for deeper results."},
            {"name":"Green Peel Bio Microneedling – 6 Sessions","price":"£475","desc":"Comprehensive transformation."},
            {"name":"Green Peel Bio Microneedling – Face & Neck","price":"£149","desc":"Dual-area rejuvenation and firming."},
            {"name":"Green Peel Bio Microneedling – Body Area","price":"£125","desc":"Target texture, scars, and revitalisation on the body."}
        ],
        "frequency_main":"Initial course: 3–6 sessions, 3–4 weeks apart; Maintenance: every 3–6 months",
        "frequency_note":"Use provided take-home serum post-treatment to support healing.",
        "faqs":[
            {"q":"Will I peel?","a":"Expect mild to visible peeling depending on strength used."},
            {"q":"Is it natural?","a":"Yes, the blend uses herbal botanicals instead of chemical acids."}
        ]
    },
    {
        "slug":"skin-illumine-hydrofacial-ultra.html",
        "title":"Skin Illumine: HydroFacial Ultra",
        "meta_desc":"HydroFacial Ultra – multi-technology luxury facial with RF, EMS, ultrasound, micro/hydradermabrasion, and LED.",
        "tagline":"Cutting-edge multi-tech rejuvenation for sculpted radiance – £150",
        "about":[
            "HydroFacial Ultra combines RF, EMS, ultrasound hammer, microdermabrasion, Hydrodermabrasion, and LED with high-performance serums for full-spectrum rejuvenation.",
            "Restores hydration, refines texture, lifts and firms with visible, long-lasting results and minimal downtime."
        ],
        "badges":["Deep Hydration","Refined Texture","Even Tone","Firming & Lift","LED Enhanced","Luxury Booster"],
        "benefits":[
            {"icon":"fas fa-droplet","title":"Deep Hydration & Plumping","desc":"Long-lasting moisture; velvety, supple skin with a lifted look."},
            {"icon":"fas fa-compress","title":"Refined Texture & Pores","desc":"Smooths irregularities and visibly reduces pore size."},
            {"icon":"fas fa-sun","title":"Radiance & Even Tone","desc":"Brightens dullness and corrects uneven pigmentation."},
            {"icon":"fas fa-bolt","title":"Youthful Renewal & Firmness","desc":"Stimulates collagen and elastin; softens lines and lifts."},
            {"icon":"fas fa-microchip","title":"Advanced Technology","desc":"RF, EMS, ultrasound, micro/hydradermabrasion for sculpting and contouring."},
            {"icon":"fas fa-lightbulb","title":"LED-Enhanced Rejuvenation","desc":"Red LED energises collagen; blue LED soothes inflammation."}
        ],
        "steps_desc":"A 10-step multi-technology luxury journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Removes makeup and impurities to prep the skin."},
            {"icon":"fas fa-leaf","title":"Enzyme Peel","desc":"Gentle exfoliation primes for deeper resurfacing."},
            {"icon":"fas fa-wand-magic-sparkles","title":"Ultrasonic Scrubber","desc":"Lifts impurities and unclogs pores."},
            {"icon":"fas fa-hand-sparkles","title":"Precision Extraction","desc":"Comfortable removal of congestion and blackheads."},
            {"icon":"fas fa-spray-can-sparkles","title":"Micro + Hydrodermabrasion","desc":"Smooths texture and deeply infuses hydrating fluids."},
            {"icon":"fas fa-wave-square","title":"RF, EMS & Ultrasound Hammer","desc":"Stimulates collagen, tightens, and contours the face."},
            {"icon":"fas fa-flask","title":"High-Performance Serum Infusion","desc":"Hyaluronic acid, peptides, antioxidants, and brighteners."},
            {"icon":"fas fa-face-smile-relaxed","title":"Mask & Facial Massage","desc":"Seals nutrients and promotes relaxation & drainage."},
            {"icon":"fas fa-lightbulb","title":"LED Light Therapy","desc":"Red for collagen, blue to calm and target blemishes."},
            {"icon":"fas fa-sparkles","title":"Included Booster","desc":"Choose Vitamin C, Collagen Peptide, or Illumine Brightening."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£150","desc":"HydroFacial Ultra with included booster."},
            {"name":"Face – 3 Sessions","price":"£405","desc":"Course for optimal sculpted radiance."},
            {"name":"Face – 4 Sessions","price":"£510","desc":"Extended package for lasting benefits."},
            {"name":"Face – 6 Sessions","price":"£720","desc":"Comprehensive luxury transformation."}
        ],
        "frequency_main":"Maintenance every 4–6 weeks",
        "frequency_note":"Combine with additional serums or masks for a fully customised experience.",
        "faqs":[
            {"q":"Is a booster included?","a":"Yes, choose from Vitamin C, Collagen Peptide, or Illumine Brightening."}
        ]
    },
    {
        "slug":"skin-glass-korean-facial.html",
        "title":"Skin Glass: Korean Facial",
        "meta_desc":"Korean Glass Skin Facial – intense hydration, barrier repair, and glow-enhancing ritual.",
        "tagline":"Hydration layering and glow for translucent, glass-like skin – £99",
        "about":[
            "Inspired by advanced Korean skincare rituals, this facial focuses on intense hydration, barrier repair, and radiant clarity for a dewy, translucent finish.",
            "Perfect for dull, dehydrated, or uneven skin with instant results and no downtime."
        ],
        "badges":["Glass-Skin Glow","Deep Hydration","Refined Texture","Even Tone","Barrier Repair","No Downtime"],
        "benefits":[
            {"icon":"fas fa-gem","title":"Glass-Skin Glow","desc":"Achieves a smooth, dewy, reflective complexion."},
            {"icon":"fas fa-droplet","title":"Deep Hydration & Plumping","desc":"Intensely hydrates for soft, bouncy skin."},
            {"icon":"fas fa-spray-can-sparkles","title":"Refined Texture","desc":"Smooths roughness and enhances clarity."},
            {"icon":"fas fa-sun","title":"Brightened, Even Tone","desc":"Reduces dullness for luminous radiance."},
            {"icon":"fas fa-shield","title":"Skin Barrier Repair","desc":"Strengthens and soothes stressed skin."}
        ],
        "steps_desc":"A glow-boosting 8-step ritual",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Gently removes makeup and impurities."},
            {"icon":"fas fa-flask","title":"Enzyme or Mild Acid Exfoliation","desc":"Smooths texture without irritation."},
            {"icon":"fas fa-spray-can-sparkles","title":"Hydration Tonics","desc":"Toners and essences infuse moisture deeply."},
            {"icon":"fas fa-vial","title":"Serum Layering","desc":"Hyaluronic acid, niacinamide, peptides and botanicals."},
            {"icon":"fas fa-mask","title":"Glass Skin Mask","desc":"Locks in moisture and enhances translucency."},
            {"icon":"fas fa-hand-holding-heart","title":"Facial Massage & Lymphatic Drainage","desc":"Boosts circulation and reduces puffiness."},
            {"icon":"fas fa-lightbulb","title":"LED Light Therapy (Optional)","desc":"Calms, boosts glow, and supports skin health."},
            {"icon":"fas fa-shield-heart","title":"Moisturise & SPF Finish","desc":"Protects and maintains the glass-skin glow."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£99","desc":"Complete Skin Glass ritual."},
            {"name":"Face – 3 Sessions","price":"£267","desc":"Glow-maintenance course."},
            {"name":"Face – 4 Sessions","price":"£336","desc":"Extended glow package."},
            {"name":"Face – 6 Sessions","price":"£475","desc":"Comprehensive radiance program."}
        ],
        "frequency_main":"Every 3–4 weeks",
        "frequency_note":"Ideal 24–72 hours before special occasions for a glass-skin finish.",
        "faqs":[
            {"q":"Can sensitive skin have this treatment?","a":"Yes, the routine is gentle and tailored to your skin type."}
        ]
    },
    {
        "slug":"skin-revive-microneedling-biorepeel.html",
        "title":"Skin Revive: Microneedling + BioRePeel",
        "meta_desc":"Microneedling plus BioRePeel – dual-action renewal for texture, scars, pores, and radiance.",
        "tagline":"Dual-action renewal for texture, scars, and radiance – £175",
        "about":[
            "Combines precise microneedling with BioRePeel to stimulate collagen, refine pores, and resurface uneven texture for a bright, even complexion.",
            "Ideal for acne scars, fine lines, and pigmentation with immediate and cumulative results."
        ],
        "badges":["Texture Smoothing","Scar Softening","Collagen Boost","Pore Refining","Radiant Glow"],
        "benefits":[
            {"icon":"fas fa-spray-can-sparkles","title":"Smooths Texture & Scars","desc":"Reduces acne scars, fine lines, and uneven skin texture."},
            {"icon":"fas fa-dna","title":"Stimulates Collagen","desc":"Encourages natural regeneration for firmer skin."},
            {"icon":"fas fa-sun","title":"Radiance & Glow","desc":"Improves tone and restores a healthy complexion."},
            {"icon":"fas fa-compress","title":"Refines Pores","desc":"Minimises the appearance of enlarged pores."},
            {"icon":"fas fa-layer-group","title":"Dual-Layer Rejuvenation","desc":"Combines microneedling and BioRePeel for maximal results."}
        ],
        "steps_desc":"A 6-step precision renewal journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Removes makeup, oil, and impurities."},
            {"icon":"fas fa-vial","title":"Skin Preparation","desc":"Gentle solution optimises comfort and results."},
            {"icon":"fas fa-syringe","title":"Microneedling","desc":"Creates microchannels to renew and smooth texture."},
            {"icon":"fas fa-flask","title":"BioRePeel Application","desc":"Enhances radiance and evens tone."},
            {"icon":"fas fa-mask","title":"Soothing Mask & Hydration","desc":"Calms and locks in moisture."},
            {"icon":"fas fa-shield-heart","title":"Serums & SPF","desc":"Protect and maintain renewed glow."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£175","desc":"Full treatment: microneedling + BioRePeel."},
            {"name":"Face – 3 Sessions","price":"£525","desc":"Course for cumulative improvements."},
            {"name":"Face – 4 Sessions","price":"£700","desc":"Extended course for deeper results."},
            {"name":"Face – 6 Sessions","price":"£1,050","desc":"Comprehensive transformation."},
            {"name":"Face & Neck – 1 Session","price":"£225","desc":"Dual-area renewal and firming."}
        ],
        "frequency_main":"Every 4–6 weeks",
        "frequency_note":"3–6 treatments recommended for deeper concerns.",
        "faqs":[
            {"q":"Is there downtime?","a":"Mild redness may occur for 24–48 hours; follow aftercare."}
        ]
    },
    {
        "slug":"skin-oxyglow-oxygen-facial.html",
        "title":"Skin OxyGlow: Oxygen Facial",
        "meta_desc":"Oxygen Facial – oxygen infusion with hydrating serums for bright, plump, and refreshed skin.",
        "tagline":"Oxygen infusion and hydration for instant glow – £99",
        "about":[
            "Infuses pure oxygen with targeted serums to nourish, stimulate circulation, and oxygenate skin cells for immediate radiance.",
            "Combines massage and optional LED to leave skin plump, radiant, and refreshed with minimal downtime."
        ],
        "badges":["Deep Hydration","Radiant Glow","Refined Texture","Calming","Circulation Boost","Instant Results"],
        "benefits":[
            {"icon":"fas fa-droplet","title":"Deep Hydration & Plumping","desc":"Long-lasting moisture for luxuriously hydrated skin."},
            {"icon":"fas fa-sun","title":"Radiance & Glow","desc":"Brightens dull skin for a healthy complexion."},
            {"icon":"fas fa-spray-can-sparkles","title":"Refined Texture","desc":"Smooths surface and improves clarity."},
            {"icon":"fas fa-feather","title":"Calms & Soothes","desc":"Reduces puffiness and inflammation."},
            {"icon":"fas fa-heart-pulse","title":"Circulation & Oxygenation","desc":"Boosts microcirculation for revitalised skin."}
        ],
        "steps_desc":"A soothing 7-step oxygen infusion journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Preps the skin for serum absorption."},
            {"icon":"fas fa-flask","title":"Gentle Exfoliation","desc":"Polishes and smooths to boost glow."},
            {"icon":"fas fa-wind","title":"Oxygen Infusion","desc":"Delivers oxygen with serums for immediate radiance."},
            {"icon":"fas fa-vial","title":"Serum Layering & Massage","desc":"Hydrating and brightening serums with a soothing massage."},
            {"icon":"fas fa-lightbulb","title":"LED Light Therapy (Optional)","desc":"Red for collagen; blue to calm and balance."},
            {"icon":"fas fa-mask","title":"Custom Mask","desc":"Seals in moisture and restores the barrier."},
            {"icon":"fas fa-shield-heart","title":"Moisturiser & SPF","desc":"Protects and maintains hydration."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£99","desc":"Oxygen infusion with hydrating serums."},
            {"name":"Face – 3 Sessions","price":"£267","desc":"Course for consistent glow."},
            {"name":"Face – 4 Sessions","price":"£336","desc":"Extended glow package."},
            {"name":"Face – 6 Sessions","price":"£475","desc":"Complete radiance program."}
        ],
        "frequency_main":"Every 2–4 weeks",
        "frequency_note":"Ideal 24–48 hours before events for a red-carpet glow.",
        "faqs":[{"q":"Is there downtime?","a":"No, you can resume normal activities immediately."}]
    },
    {
        "slug":"skin-renewal-chemical-peel.html",
        "title":"Skin Renewal: Chemical Peel",
        "meta_desc":"Chemical Peel – resurface, refine, and brighten for a renewed, luminous complexion.",
        "tagline":"Resurfacing peel for smooth texture and radiant tone – £99",
        "about":[
            "High-performance chemical exfoliants resurface, refine, and brighten the skin for smoother texture and even tone.",
            "Combined with soothing serums and hydration to enhance luminosity with minimal downtime."
        ],
        "badges":["Texture Refining","Brightening","Skin Renewal","Hydrating","Minimal Downtime"],
        "benefits":[
            {"icon":"fas fa-spray-can-sparkles","title":"Smooths Texture","desc":"Reduces roughness and enhances softness."},
            {"icon":"fas fa-sun","title":"Brightens & Evens Tone","desc":"Targets pigmentation and dullness."},
            {"icon":"fas fa-arrows-rotate","title":"Stimulates Renewal","desc":"Promotes natural cell turnover."},
            {"icon":"fas fa-droplet","title":"Hydrates & Soothes","desc":"Restores moisture while calming the skin."}
        ],
        "steps_desc":"A 6-step resurfacing and renewal journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Prepares skin for active ingredients."},
            {"icon":"fas fa-magnifying-glass","title":"Skin Analysis & Prep","desc":"Select ideal peel strength and pre-solution."},
            {"icon":"fas fa-flask","title":"Chemical Peel Application","desc":"Exfoliates, smooths texture, and reduces pigmentation."},
            {"icon":"fas fa-vial","title":"Soothing Serum Infusion","desc":"Nourishes, hydrates, and calms."},
            {"icon":"fas fa-mask","title":"Custom Mask & Massage","desc":"Locks in nutrients and relaxes."},
            {"icon":"fas fa-shield-heart","title":"Post-Treatment Protection","desc":"Moisturiser and SPF to protect results."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£99","desc":"Professional peel with soothing finish."},
            {"name":"Face – 3 Sessions","price":"£267","desc":"Course for visible renewal."},
            {"name":"Face – 4 Sessions","price":"£336","desc":"Extended peel program."},
            {"name":"Face – 6 Sessions","price":"£475","desc":"Comprehensive rejuvenation."}
        ],
        "frequency_main":"Every 4–6 weeks",
        "frequency_note":"3–6 sessions recommended for deeper pigmentation or textural concerns.",
        "faqs":[{"q":"Is there downtime?","a":"Minimal; mild flaking can occur depending on peel strength."}]
    },
    {
        "slug":"skin-luxe-satin-ultimate-exfoliation.html",
        "title":"Skin Luxe Satin: Ultimate Exfoliation",
        "meta_desc":"Ultimate Exfoliation – enzyme peel, microdermabrasion, dermaplaning, and hydration for satin-smooth skin.",
        "tagline":"Comprehensive polishing for soft, luminous, satin-smooth skin – £99",
        "about":[
            "Combines enzyme peel, microdermabrasion, dermaplaning, extractions, and hydrating serums to refine texture and enhance radiance.",
            "Leaves skin ultra-smooth and revitalised with minimal downtime."
        ],
        "badges":["Comprehensive Exfoliation","Pore Refining","Radiance","Silky Finish","Minimal Downtime"],
        "benefits":[
            {"icon":"fas fa-layer-group","title":"Comprehensive Exfoliation","desc":"Removes dead cells and smooths surface texture."},
            {"icon":"fas fa-compress","title":"Refines & Cleanses Pores","desc":"Targeted extractions clear congestion."},
            {"icon":"fas fa-sun","title":"Radiance & Glow","desc":"Hydrating serums brighten dull skin."},
            {"icon":"fas fa-feather","title":"Soft & Silky Skin","desc":"Leaves skin ultra-smooth with a satin finish."}
        ],
        "steps_desc":"An 8-step refinement and glow journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Creates a clean canvas for resurfacing."},
            {"icon":"fas fa-leaf","title":"Exfoliation & Enzyme Peel","desc":"Dissolves dead cells and smooths texture."},
            {"icon":"fas fa-wand-magic-sparkles","title":"Microdermabrasion","desc":"Polishes and refines pores."},
            {"icon":"fas fa-scissors","title":"Dermaplaning","desc":"Removes vellus hair and buildup."},
            {"icon":"fas fa-hand-sparkles","title":"Precision Extractions","desc":"Clears congestion and impurities."},
            {"icon":"fas fa-vial","title":"Hydrating Serum Infusion","desc":"HA and brighteners restore radiance."},
            {"icon":"fas fa-mask","title":"Custom Mask & Massage","desc":"Locks nutrients and rejuvenates."},
            {"icon":"fas fa-shield-heart","title":"SPF Finish","desc":"Protects the fresh glow."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£99","desc":"Full ultimate exfoliation treatment."},
            {"name":"Face – 3 Sessions","price":"£267","desc":"Course for consistent refinement."},
            {"name":"Face – 4 Sessions","price":"£336","desc":"Extended course for deeper results."},
            {"name":"Face – 6 Sessions","price":"£475","desc":"Complete transformation package."}
        ],
        "frequency_main":"Every 3–4 weeks",
        "frequency_note":"Combine with serums or masks for enhanced results.",
        "faqs":[{"q":"Is dermaplaning included?","a":"Yes, to enhance smoothness and product absorption."}]
    },
    {
        "slug":"skin-balance-bb-glow.html",
        "title":"Skin Balance: BB Glow",
        "meta_desc":"BB Glow – semi-permanent brightening via microneedling infusion of BB serums for radiant, even tone.",
        "tagline":"Semi-permanent luminosity and even tone via BB serums – £109",
        "about":[
            "Advanced microneedling infuses nutrient-rich BB serums to brighten, even tone, hydrate, and stimulate collagen for long-lasting glow.",
            "Provides a subtle tint with deeper skin rejuvenation and minimal downtime."
        ],
        "badges":["Even Tone","Deep Hydration","Smooth Texture","Long-Lasting","Glow Boost"],
        "benefits":[
            {"icon":"fas fa-sun","title":"Even Tone & Radiance","desc":"Gradually corrects uneven tone and brightens."},
            {"icon":"fas fa-droplet","title":"Deep Hydration","desc":"Microneedling ensures maximum serum penetration."},
            {"icon":"fas fa-spray-can-sparkles","title":"Soft & Smooth Texture","desc":"Refines surface and stimulates collagen."},
            {"icon":"fas fa-hourglass-half","title":"Long-Lasting Results","desc":"Semi-permanent pigment provides a natural finish."}
        ],
        "steps_desc":"A 6-step brightening infusion journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Preps skin for even application."},
            {"icon":"fas fa-flask","title":"Gentle Exfoliation","desc":"Enhances serum absorption."},
            {"icon":"fas fa-syringe","title":"Microneedling Serum Infusion","desc":"Creates microchannels to infuse BB serums and renew."},
            {"icon":"fas fa-vial","title":"BB Serum Application","desc":"Layers additional serums for glow and nourishment."},
            {"icon":"fas fa-mask","title":"Soothing Mask & Massage","desc":"Locks in nutrients and calms."},
            {"icon":"fas fa-shield-heart","title":"Hydration & SPF","desc":"Seals results and protects."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£109","desc":"BB Glow infusion treatment."},
            {"name":"Face – 3 Sessions","price":"£327","desc":"Course for lasting luminosity."},
            {"name":"Face – 4 Sessions","price":"£436","desc":"Extended course for optimal results."},
            {"name":"Face – 6 Sessions","price":"£654","desc":"Complete glow program."}
        ],
        "frequency_main":"Every 4–6 weeks",
        "frequency_note":"3–5 sessions recommended for optimal, long-lasting results.",
        "faqs":[{"q":"Is it safe for all tones?","a":"Yes, serums are selected to match and enhance your tone."}]
    },
    {
        "slug":"skin-luma-lift-rf-facial.html",
        "title":"Skin Luma Lift: Radio Frequency Facial",
        "meta_desc":"RF Facial – tighten, lift, and rejuvenate by stimulating collagen and elastin.",
        "tagline":"Firming RF energy for lift, elasticity, and glow – £119",
        "about":[
            "RF energy penetrates deep to stimulate collagen and elastin, improve elasticity, and restore a youthful contour with minimal downtime.",
            "Combined with hydrating serums and targeted massage for enhanced firmness and radiance."
        ],
        "badges":["Skin Tightening","Lift & Contour","Hydration","Texture Refining","Minimal Downtime"],
        "benefits":[
            {"icon":"fas fa-up-long","title":"Skin Tightening & Lifting","desc":"Stimulates collagen and elastin for a firmer appearance."},
            {"icon":"fas fa-face-smile","title":"Improved Elasticity & Contour","desc":"Enhances facial structure and softens sagging."},
            {"icon":"fas fa-droplet","title":"Hydration & Glow","desc":"Serums restore moisture and luminosity."},
            {"icon":"fas fa-spray-can-sparkles","title":"Refines Texture","desc":"Smooths fine lines and surface irregularities."}
        ],
        "steps_desc":"A 7-step firming and contouring journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Preps for maximum serum absorption."},
            {"icon":"fas fa-flask","title":"Gentle Exfoliation","desc":"Smooths texture for even RF delivery."},
            {"icon":"fas fa-wave-square","title":"RF Application","desc":"Stimulates collagen, tightens, and firms."},
            {"icon":"fas fa-vial","title":"Serum Infusion","desc":"Hydrating and firming serums nourish skin."},
            {"icon":"fas fa-hand-holding-heart","title":"Targeted Facial Massage","desc":"Boosts circulation and enhances contour."},
            {"icon":"fas fa-mask","title":"Custom Mask & Hydration","desc":"Seals in nutrients and soothes."},
            {"icon":"fas fa-shield-heart","title":"Post-Treatment Protection","desc":"Moisturiser and SPF to maintain results."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£119","desc":"Firming RF facial treatment."},
            {"name":"Face – 3 Sessions","price":"£357","desc":"Course for cumulative lift."},
            {"name":"Face – 4 Sessions","price":"£476","desc":"Extended course for enhanced firmness."},
            {"name":"Face – 6 Sessions","price":"£714","desc":"Comprehensive firming program."}
        ],
        "frequency_main":"Every 4–6 weeks",
        "frequency_note":"3–6 sessions recommended for enhanced, long-lasting results.",
        "faqs":[{"q":"Is it painful?","a":"Most clients feel comfortable warmth during RF energy delivery."}]
    },
    {
        "slug":"deep-blackhead-extraction.html",
        "title":"Deep Blackhead Extraction",
        "meta_desc":"Deep Blackhead Extraction – professional pore decongestion and skin purification treatment.",
        "tagline":"Professional extraction to decongest and refine – £60",
        "about":[
            "Thorough, professional extraction to purify and decongest the skin using advanced techniques and soothing serums.",
            "Clears impurities, refines pores, and restores clarity without irritation or damage."
        ],
        "badges":["Purifies","Refines Pores","Calming","Immediate Clarity","Breakout Prevention"],
        "benefits":[
            {"icon":"fas fa-broom","title":"Deep Purification","desc":"Clears blackheads, clogged pores, and impurities."},
            {"icon":"fas fa-compress","title":"Refines & Smooths Pores","desc":"Skin looks cleaner and smoother."},
            {"icon":"fas fa-feather","title":"Calms & Hydrates","desc":"Soothes irritation and restores hydration."},
            {"icon":"fas fa-star","title":"Instant Results","desc":"Skin feels fresh, polished, and clear immediately."}
        ],
        "steps_desc":"A 6-step professional decongestion journey",
        "steps":[
            {"icon":"fas fa-soap","title":"Double Cleanse","desc":"Removes surface impurities and oils."},
            {"icon":"fas fa-flask","title":"Gentle Exfoliation","desc":"Softens skin and preps pores."},
            {"icon":"fas fa-suction-cup","title":"Deep Extraction","desc":"Targeted, safe extraction clears congestion."},
            {"icon":"fas fa-vial","title":"Soothing Serum Infusion","desc":"Calms redness and strengthens the barrier."},
            {"icon":"fas fa-mask","title":"Custom Mask","desc":"Seals nutrients and soothes."},
            {"icon":"fas fa-shield-heart","title":"Post-Treatment Care","desc":"Moisturiser and SPF to protect and maintain."}
        ],
        "addons":[],
        "pricing":[
            {"name":"Face – 1 Session","price":"£60","desc":"Deep blackhead extraction."},
            {"name":"Face – 3 Sessions","price":"£162","desc":"Course for ongoing clarity."},
            {"name":"Face – 6 Sessions","price":"£306","desc":"Extended program for stubborn congestion."}
        ],
        "frequency_main":"Every 3–4 weeks",
        "frequency_note":"Combine with hydrating facials for long-lasting clarity.",
        "faqs":[{"q":"Will it hurt?","a":"Discomfort is minimal; we use techniques to protect the skin."}]
    }
]

if __name__ == "__main__":
    for cfg in DATA:
        html = render_page(cfg)
        write_page(cfg["slug"], html)
    print("\nAll pages generated.")
