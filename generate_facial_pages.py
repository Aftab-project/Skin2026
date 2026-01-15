#!/usr/bin/env python3
"""
Refactor all 9 facial pages to new standardized template
This script generates the HTML content for each page
"""

def generate_facial_page(title, tagline, price_single, price_3pack, price_6pack, 
                         about_p1, about_p2, about_p3, 
                         benefit_titles, benefit_descs, benefit_icons,
                         related_files):
    """Generate complete refactored facial page HTML"""
    
    benefits_html = ""
    for i, (title, desc, icon) in enumerate(zip(benefit_titles, benefit_descs, benefit_icons)):
        benefits_html += f"""                <div class="benefit-card">
                    <div class="icon"><i class="fas {icon}"></i></div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
"""

    related_cards = ""
    related_titles = {
        'hydrofacial.html': ('Skin Glow: Hydrofacial', 'Deep cleansing and hydration for instant radiance.', '45 mins', '£99'),
        'korean-facial.html': ('Skin Glass: Korean Facial', 'Luxurious multi-step K-beauty ritual for glass skin.', '60 mins', '£99'),
        'oxygeno-facial.html': ('Skin Oxyglow: OxygenO Facial', 'Oxygen infusion for instant glow and hydration.', '45 mins', '£89'),
        'biorepeel.html': ('Skin Radiance: BioRePeel', 'Advanced chemical peel for cell renewal.', '45 mins', '£99'),
        'biomicroneedling.html': ('Green Peel – BioMicroneedling', 'Herbal microneedling for collagen boost.', '45 mins', '£89'),
        'chemical-peel.html': ('Skin Renewal: Chemical Peel', 'Professional exfoliation for transformation.', '45 mins', '£99'),
        'microneedling-biorepeel.html': ('Skin Revive: Microneedling + BioRePeel', 'Dual-action for maximum results.', '60 mins', '£149'),
        'rf-facial.html': ('Skin LumaLift: Radio Frequency Facial', 'RF technology for lifting and tightening.', '60 mins', '£129'),
        'ultimate-exfoliation.html': ('Skin Luxe Satin: Ultimate Exfoliation', 'Triple exfoliation for smoothness and glow.', '45 mins', '£99'),
        'blackhead-extraction.html': ('Deep Blackhead Extraction', 'Professional pore cleansing and extraction.', '45 mins', '£79'),
        'bb-glow.html': ('Skin Balance: BB Glow', 'Semi-permanent tinted skincare infusion.', '60 mins', '£125'),
    }
    
    for related_file in related_files:
        if related_file in related_titles:
            name, desc, time, price = related_titles[related_file]
            related_cards += f"""                <div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">{name}</h4>
                        <p class="related-card-desc">{desc}</p>
                        <div class="related-card-meta">
                            <span>{time}</span>
                            <span class="related-card-price">From {price}</span>
                        </div>
                        <a href="{related_file}" class="related-card-cta">Learn More</a>
                    </div>
                </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} at Mili Skin & Beauty - {tagline.split('.')[0]}. Book in London E2 9NY.">
    <meta name="keywords" content="facial treatment, skincare, {title.lower()}, London">
    <meta property="og:title" content="{title} - Mili Skin & Beauty">
    <meta property="og:description" content="{tagline}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="./images/facial-hero.jpg">
    <title>{title} - Mili Skin & Beauty</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="components.css">
</head>
<body>
    
    <!-- Header & Navigation -->
    <header class="header">
        <nav class="navbar">
            <div class="container">
                <div class="nav-wrapper">
                    <a href="index.html#home" class="logo">
                        <span class="logo-text">Mili Skin & Beauty</span>
                    </a>
                    
                    <button class="mobile-menu-toggle" aria-label="Toggle Menu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                    
                    <ul class="nav-links">
                        <li><a href="index.html#home" class="nav-link">Home</a></li>
                        <li><a href="index.html#about" class="nav-link">About</a></li>
                        <li><a href="index.html#services" class="nav-link">Services</a></li>
                        <li><a href="index.html#contact" class="nav-link">Contact</a></li>
                        <li><a href="faq.html" class="nav-link">FAQ</a></li>
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

    <!-- Treatment Categories Navigation -->
    <nav class="treatment-mega-nav">
        <div class="container">
            <div class="mega-nav-wrapper">
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
                                    <li><a href="hydrofacial.html">Skin Glow: Hydrofacial</a></li>
                                    <li><a href="korean-facial.html">Skin Glass: Korean Facial</a></li>
                                    <li><a href="oxygeno-facial.html">Skin Oxyglow: OxygenO Facial</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Renewal & Peels</li>
                                    <li><a href="biorepeel.html">Skin Radiance: BioRePeel</a></li>
                                    <li><a href="biomicroneedling.html">Green Peel – BioMicroneedling</a></li>
                                    <li><a href="chemical-peel.html">Skin Renewal: Chemical Peel</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Advanced Tech</li>
                                    <li><a href="microneedling-biorepeel.html">Skin Revive: Microneedling + BioRePeel</a></li>
                                    <li><a href="rf-facial.html">Skin LumaLift: Radio Frequency Facial</a></li>
                                    <li><a href="ultimate-exfoliation.html">Skin Luxe Satin: Ultimate Exfoliation</a></li>
                                </ul>
                                <ul class="mega-menu-column">
                                    <li class="column-title">Specialty</li>
                                    <li><a href="bb-glow.html">Skin Balance: BB Glow</a></li>
                                    <li><a href="blackhead-extraction.html">Deep Blackhead Extraction</a></li>
                                    <li class="mega-menu-cta"><a href="index.html#contact" class="btn btn-sm">Book Treatment</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="treatment-hero" style="background-image: url('./images/facial-hero.jpg');">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>{title}</h1>
            <p class="tagline">{tagline}</p>
            <div class="hero-ctas">
                <a href="#section-pricing" class="btn btn-primary">Book Treatment</a>
                <a href="#section-about" class="btn btn-secondary">Learn More</a>
            </div>
        </div>
    </section>

    <!-- Sticky Subnav -->
    <nav class="sticky-subnav">
        <div class="container">
            <ul class="subnav-list">
                <li><a href="#section-about" class="subnav-link active">About</a></li>
                <li><a href="#section-benefits" class="subnav-link">Benefits</a></li>
                <li><a href="#section-results" class="subnav-link">Results</a></li>
                <li><a href="#section-steps" class="subnav-link">How It Works</a></li>
                <li><a href="#section-pricing" class="subnav-link">Pricing</a></li>
                <li><a href="#section-faqs" class="subnav-link">FAQs</a></li>
                <li><a href="#section-related" class="subnav-link">Related</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container">

        <!-- About Section -->
        <section id="section-about" class="treatment-section">
            <h2>About This Treatment</h2>
            <div class="about-layout">
                <div class="about-text">
                    <p>{about_p1}</p>
                    <p>{about_p2}</p>
                    <p>{about_p3}</p>
                </div>
                <div class="about-badges">
                    <span class="badge">Professional Grade</span>
                    <span class="badge">Non-invasive</span>
                    <span class="badge">Visible Results</span>
                    <span class="badge">All Skin Types</span>
                    <span class="badge">No Downtime</span>
                </div>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item">
                    <div class="gallery-placeholder">
                        <i class="fas fa-image"></i>
                        <p>Before Treatment</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">
                        <i class="fas fa-image"></i>
                        <p>During Treatment</p>
                    </div>
                </div>
                <div class="gallery-item">
                    <div class="gallery-placeholder">
                        <i class="fas fa-image"></i>
                        <p>After Treatment</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Benefits Section -->
        <section id="section-benefits" class="treatment-section">
            <h2>Benefits of This Treatment</h2>
            <p>Discover what makes this treatment special.</p>
            <div class="benefits-grid">
{benefits_html}            </div>
        </section>

        <!-- Results Carousel Section -->
        <section id="section-results" class="treatment-section">
            <h2>Real Results</h2>
            <p>See the transformation for yourself.</p>
            <div class="carousel-container">
                <div class="carousel-slide active">
                    <div class="gallery-placeholder" style="min-height: 400px;">
                        <i class="fas fa-image"></i>
                    </div>
                    <p class="carousel-caption">Professional result showing visible improvement</p>
                </div>
                <div class="carousel-slide">
                    <div class="gallery-placeholder" style="min-height: 400px;">
                        <i class="fas fa-image"></i>
                    </div>
                    <p class="carousel-caption">Enhanced complexion with refined texture</p>
                </div>
                <div class="carousel-slide">
                    <div class="gallery-placeholder" style="min-height: 400px;">
                        <i class="fas fa-image"></i>
                    </div>
                    <p class="carousel-caption">Glowing skin with improved tone and clarity</p>
                </div>
                <div class="carousel-controls">
                    <button class="carousel-btn carousel-prev" aria-label="Previous slide"><i class="fas fa-chevron-left"></i></button>
                    <button class="carousel-btn carousel-next" aria-label="Next slide"><i class="fas fa-chevron-right"></i></button>
                </div>
                <div class="carousel-dots">
                    <button class="carousel-dot active" aria-label="Go to slide 1"></button>
                    <button class="carousel-dot" aria-label="Go to slide 2"></button>
                    <button class="carousel-dot" aria-label="Go to slide 3"></button>
                </div>
            </div>
        </section>

        <!-- How It Works Section -->
        <section id="section-steps" class="treatment-section">
            <h2>How the Treatment Works</h2>
            <div class="accordion steps-accordion">
                <div class="accordion-item open">
                    <div class="accordion-header">
                        <h4>1. Consultation & Assessment</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Your therapist assesses your skin type, concerns, and goals to customize the treatment for optimal results.</p>
                            <p><strong>Duration:</strong> 10-15 minutes</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>2. Cleansing & Preparation</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Skin is thoroughly cleansed and prepared to maximize treatment effectiveness and comfort.</p>
                            <p><strong>Duration:</strong> 10 minutes</p>
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
                            <p>The main treatment is applied according to your customized plan. You'll experience relaxation and visible improvements.</p>
                            <p><strong>Duration:</strong> 20-30 minutes</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>4. Aftercare & Guidance</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>We provide comprehensive aftercare instructions to maximize and maintain your treatment results.</p>
                            <p><strong>Total Duration:</strong> 45-60 minutes</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Pricing & Enquiry Section -->
        <section id="section-pricing" class="treatment-section">
            <h2>Pricing & Enquiry</h2>
            <div class="pricing-layout">
                <div class="pricing-info">
                    <h3>Investment</h3>
                    <div class="pricing-list">
                        <div class="pricing-item">
                            <div class="pricing-info-text">
                                <h4>Single Session</h4>
                                <p>Complete treatment</p>
                            </div>
                            <div class="pricing-price">{price_single}</div>
                        </div>
                        <div class="pricing-item">
                            <div class="pricing-info-text">
                                <h4>3-Pack Course</h4>
                                <p>Best for results</p>
                            </div>
                            <div class="pricing-price">{price_3pack}</div>
                        </div>
                        <div class="pricing-item">
                            <div class="pricing-info-text">
                                <h4>6-Pack Course</h4>
                                <p>Maximum benefits</p>
                            </div>
                            <div class="pricing-price">{price_6pack}</div>
                        </div>
                        <div class="pricing-item">
                            <div class="pricing-info-text">
                                <h4>Add-on Treatment</h4>
                                <p>Enhancement option</p>
                            </div>
                            <div class="pricing-price">£25-£50</div>
                        </div>
                    </div>
                </div>
                <div class="enquiry-form-wrapper">
                    <h3>Get in Touch</h3>
                    <form class="enquiry-form" action="contact.php" method="POST">
                        <input type="hidden" name="treatment" value="{title}">
                        <div class="form-group">
                            <label for="name">Full Name</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email Address</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" id="phone" name="phone" required>
                        </div>
                        <div class="form-group">
                            <label for="service">Service Interest</label>
                            <select id="service" name="service" required>
                                <option value="">Select an option</option>
                                <option value="single">Single Session</option>
                                <option value="3-pack">3-Pack Course</option>
                                <option value="6-pack">6-Pack Course</option>
                                <option value="inquiry">General Inquiry</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" rows="4" placeholder="Tell us about your skin goals..."></textarea>
                        </div>
                        <div class="form-group checkbox">
                            <input type="checkbox" id="consent" name="consent" required>
                            <label for="consent">I agree to be contacted about my enquiry</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Send Enquiry</button>
                    </form>
                </div>
            </div>
        </section>

        <!-- FAQs Section -->
        <section id="section-faqs" class="treatment-section">
            <h2>Frequently Asked Questions</h2>
            <div class="accordion faqs-accordion">
                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>How often should I get this treatment?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>For best results, we recommend monthly maintenance treatments. A course of 3-6 treatments spaced 4 weeks apart delivers the most dramatic results.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>Is this suitable for sensitive skin?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Yes, this treatment can be customized for sensitive skin. Let your therapist know about any sensitivities during consultation so they can adjust accordingly.</p>
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
                            <p>Most clients see immediate visible improvements. Optimal results develop over 2-4 weeks as the skin continues to improve with proper aftercare.</p>
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
                            <p>Most of our treatments have minimal to no downtime. You can return to normal activities immediately, though we recommend avoiding intense exercise for 24 hours.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>How long do results last?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Results typically last 4-6 weeks. Regular maintenance treatments help sustain the benefits longer. Results can be cumulative with repeated treatments.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>Can I combine this with other treatments?</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>Yes, many treatments pair beautifully together. We recommend spacing them 2 weeks apart. Discuss your goals with us and we'll create a customized plan.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Related Treatments Section -->
        <section id="section-related" class="treatment-section">
            <h2>Complementary Treatments</h2>
            <p>Explore other facials that pair beautifully with this treatment.</p>
            <div class="related-cards-grid">
{related_cards}            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Mili Skin & Beauty</h3>
                    <p>Premium skincare and beauty treatments in London.</p>
                    <p><strong>Address:</strong> 13b Edinburgh Cl, London E2 9NY</p>
                    <p><strong>Phone:</strong> Available on booking platform</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html#home">Home</a></li>
                        <li><a href="index.html#about">About Us</a></li>
                        <li><a href="index.html#services">Services</a></li>
                        <li><a href="faq.html">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Contact Info</h4>
                    <ul>
                        <li><i class="fas fa-map-marker-alt"></i> <a href="https://www.google.com/maps/search/13b+Edinburgh+Cl,+London+E2+9NY" target="_blank">London E2 9NY</a></li>
                        <li><i class="fas fa-phone"></i> <a href="tel:+447346001219">07346 001219</a></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:Militest@gmail.com">Militest@gmail.com</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Follow Us</h4>
                    <div class="social-links">
                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="#" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Mili Skin & Beauty. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script src="treatment-components.js"></script>
</body>
</html>
"""
    return html

# Generate content for each page
pages = {
    'oxygeno-facial.html': ('Skin Oxyglow: OxygenO Facial', 'Advanced oxygen infusion for instant radiance, deep hydration, and cellular renewal',
        '£89', '£240', '£425',
        'The OxygenO Facial harnesses the power of advanced oxygen infusion technology to deliver transformative results. This revolutionary treatment infuses oxygen and active serums directly into the skin, promoting cellular renewal and vitality.',
        'Oxygen naturally enhances blood circulation, boosts collagen production, and accelerates cellular regeneration. This makes it an excellent choice for those seeking immediate, visible radiance and long-term skin improvement.',
        'Whether you\'re preparing for a special event or investing in your skin\'s long-term health, the OxygenO Facial offers unparalleled comfort and visible results that speak for themselves.',
        ['Instant Radiance', 'Deep Hydration', 'Cellular Renewal', 'Brightening Effect', 'Suitable for All', 'No Downtime'],
        ['Visible glow and brightness appear immediately after treatment, perfect for special events.', 'Oxygen infusion deeply hydrates skin, improving texture and reducing fine lines.', 'Boosts oxygen levels to promote collagen production and skin regeneration.', 'Reduces dullness, dark spots, and uneven skin tone for a luminous complexion.', 'Gentle enough for sensitive skin, effective for all skin types and conditions.', 'Resume activities immediately. Perfect for busy lifestyles—no recovery needed.'],
        ['fa-bolt', 'fa-water', 'fa-leaf', 'fa-sun', 'fa-check-circle', 'fa-clock'],
        ['hydrofacial.html', 'biorepeel.html', 'korean-facial.html']
    ),
}

if __name__ == '__main__':
    print("Template generator ready for facial page refactoring")
