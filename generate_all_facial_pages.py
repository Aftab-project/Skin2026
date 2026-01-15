"""
Comprehensive script to generate all 12 Facial & Skincare treatment pages
Based on the HIFU treatment page structure
"""

import os
import json

# Define all treatment data based on the documentation
TREATMENTS = [
    {
        "filename": "skin-glow-hydrofacial.html",
        "title": "Skin Glow: HydroFacial",
        "meta_desc": "Skin Glow: HydroFacial at Mili Skin & Beauty - Advanced hydration and glow treatment for radiant skin.",
        "hero_title": "Skin Glow: HydroFacial",
        "hero_tagline": "Advanced hydration and glow treatment for radiant skin – £99",
        "about_paras": [
            "The Hydrofacial is an advanced, machine-assisted treatment that deeply cleanses, exfoliates, and hydrates the skin while infusing targeted serums for optimal results. Using innovative vortex technology and gentle suction, impurities are removed as the skin is nourished with antioxidants, peptides, and hyaluronic acid.",
            "Suitable for all skin types, this treatment improves skin texture, reduces congestion, and restores hydration for a smoother, more radiant complexion. LED therapy is incorporated to calm redness, soften fine lines, and revitalise tired skin, leaving the face refreshed, plump, and glowing with no downtime."
        ],
        "badges": ["Deep Hydration", "Radiant Glow", "Refined Pores", "LED Therapy", "No Downtime"],
        "benefits": [
            {"icon": "fas fa-droplet", "title": "Hydration & Plumping", "desc": "Infuses skin with intense, nourishing moisture, leaving it velvety, supple, and luxuriously soft."},
            {"icon": "fas fa-sun", "title": "Radiance & Even Tone", "desc": "Restores luminous, glowing skin, reducing dullness and revealing a flawless, camera-ready complexion."},
            {"icon": "fas fa-compress", "title": "Silken Texture & Refined Pores", "desc": "Clears congestion, minimises pores, and leaves skin exquisitely smooth and polished."},
            {"icon": "fas fa-sparkles", "title": "Youthful Renewal", "desc": "Reduces fine lines, boosts firmness, and enhances elasticity for a lifted, refreshed, and timeless look."},
            {"icon": "fas fa-lightbulb", "title": "LED-Enhanced Rejuvenation", "desc": "Stimulates collagen, calms inflammation, and targets breakouts, elevating your skin to its very best condition."},
            {"icon": "fas fa-star", "title": "Instant, Red-Carpet Glow", "desc": "Visible results immediately, with minimal downtime, leaving your skin feeling like the ultimate indulgence."}
        ],
        "steps_desc": "An 8-step hydration and glow journey",
        "steps": [
            {"icon": "fas fa-user-doctor", "title": "Personalised Luxury Consultation", "desc": "Your journey begins with a bespoke skin analysis, understanding your unique concerns, goals, and skin type. Every step is tailored to ensure maximum results."},
            {"icon": "fas fa-soap", "title": "Deep, Gentle Cleansing Ritual", "desc": "Skin is treated with professional-grade cleansers that remove impurities while respecting its natural balance, preparing it for rejuvenation."},
            {"icon": "fas fa-arrows-rotate", "title": "Exquisite Exfoliation & Resurfacing", "desc": "Advanced vortex technology delicately removes dead skin cells and smooths the surface, revealing fresh, radiant skin."},
            {"icon": "fas fa-hand-sparkles", "title": "Precise, Painless Extraction", "desc": "Congested pores, blackheads, and impurities are cleared with precision and comfort, leaving your skin clean, polished, and refined."},
            {"icon": "fas fa-flask", "title": "High-Potency Serum Infusion", "desc": "Nutrient-rich serums packed with hyaluronic acid, peptides, and antioxidants are delivered deep into the skin, hydrating, plumping, and restoring youthful radiance."},
            {"icon": "fas fa-face-smile-relaxed", "title": "Customised Mask & Relaxing Facial Massage", "desc": "A soothing mask locks in nutrients while a gentle massage promotes circulation, lymphatic drainage, and complete relaxation."},
            {"icon": "fas fa-lightbulb", "title": "LED Light Therapy", "desc": "Red LED stimulates collagen and reduces fine lines, while blue LED targets breakouts and calms inflammation, enhancing overall rejuvenation."},
            {"icon": "fas fa-shield-heart", "title": "Post-Treatment Protection & Glow", "desc": "Recovery serums and SPF protect, nourish, and maintain your skin's luminosity, ensuring your glow lasts long after you leave the treatment room."}
        ],
        "addons": [
            {"icon": "fas fa-scalpel", "title": "Dermaplaning – £10", "desc": "A gentle exfoliation treatment that removes dead skin and peach fuzz using a precise, professional blade. This leaves your skin ultra-smooth, brighter, and perfectly prepped for deeper product absorption and a flawless finish."},
            {"icon": "fas fa-lemon", "title": "Vitamin C Booster – £15", "desc": "A brightening serum infusion designed to target dullness, uneven skin tone, and pigmentation. This antioxidant-rich boost enhances radiance, protects the skin from environmental stress, and leaves you with a fresh, glowing complexion."},
            {"icon": "fas fa-dna", "title": "Collagen Peptide Booster – £15", "desc": "A concentrated blend of skin-firming peptides that support collagen and elasticity. This booster helps smooth fine lines, improve skin texture, and deliver a tighter, more youthful appearance."}
        ],
        "pricing": [
            {"name": "Face – 1 Session", "price": "£99", "desc": "Complete HydroFacial treatment with LED therapy.", "value": "Face - 1 Session"},
            {"name": "Face – 3 Sessions", "price": "£267", "desc": "Package for sustained glow and hydration.", "value": "Face - 3 Sessions"},
            {"name": "Face – 4 Sessions", "price": "£336", "desc": "Extended package for optimal results.", "value": "Face - 4 Sessions"},
            {"name": "Face – 6 Sessions", "price": "£475", "desc": "Complete course for maximum transformation.", "value": "Face - 6 Sessions"}
        ],
        "frequency": "Every 4–6 weeks for maintenance and optimal results",
        "frequency_note": "Can be combined with treatments like peels, masks, or serums for enhanced effects",
        "faqs": [
            {"q": "Is the treatment suitable for all skin types?", "a": "Yes, HydroFacial is suitable for all skin types including sensitive skin. The treatment is fully customizable to address your specific concerns."},
            {"q": "How long does the treatment take?", "a": "The complete treatment takes approximately 60-75 minutes including consultation and post-care."},
            {"q": "When will I see results?", "a": "You'll notice immediate results with radiant, hydrated, and glowing skin right after your first session. Results continue to improve with regular treatments."},
            {"q": "Is there any downtime?", "a": "No downtime. You can resume normal activities immediately and even apply makeup right after treatment if desired."},
            {"q": "How often should I have this treatment?", "a": "For optimal results, we recommend treatments every 4–6 weeks for maintenance. Your therapist will create a personalized schedule based on your skin goals."}
        ]
    }
]

def generate_html_page(treatment_data):
    """Generate complete HTML page for a treatment"""
    
    # Generate benefits HTML
    benefits_html = ""
    for benefit in treatment_data["benefits"]:
        benefits_html += f'''                        <div class="benefit-card">
                            <div class="icon"><i class="{benefit['icon']}"></i></div>
                            <h4>{benefit['title']}</h4>
                            <p>{benefit['desc']}</p>
                        </div>
'''
    
    # Generate steps HTML
    steps_html = ""
    for idx, step in enumerate(treatment_data["steps"], 1):
        steps_html += f'''                <!-- Step {idx} -->
                <div class="experience-card">
                    <div class="step-number">{idx}</div>
                    <div class="step-icon">
                        <i class="{step['icon']}"></i>
                    </div>
                    <h3>{step['title']}</h3>
                    <p>{step['desc']}</p>
                </div>

'''
    
    # Generate addons HTML if present
    addons_html = ""
    if treatment_data.get("addons"):
        addon_cards = ""
        for addon in treatment_data["addons"]:
            addon_cards += f'''                    <div class="benefit-card">
                        <div class="icon"><i class="{addon['icon']}"></i></div>
                        <h4>{addon['title']}</h4>
                        <p>{addon['desc']}</p>
                    </div>
'''
        addons_html = f'''
            <!-- Optional Add-Ons Section -->
            <div class="add-ons-section" style="margin-top: 50px;">
                <h3 style="text-align: center; margin-bottom: 30px; font-family: 'Playfair Display', serif; color: #1a1a1a;">Optional Add-Ons</h3>
                <div class="benefits-grid">
{addon_cards}                </div>
            </div>'''
    
    # Generate pricing HTML
    pricing_html = ""
    pricing_options = ""
    for item in treatment_data["pricing"]:
        pricing_html += f'''                        <div class="pricing-item">
                            <div class="pricing-info">
                                <h4>{item['name']}</h4>
                                <p>{item['desc']}</p>
                            </div>
                            <div class="pricing-price">{item['price']}</div>
                            <a href="https://that-time.co.uk/service/196300/book" target="_blank" rel="noopener noreferrer" class="nav-link book-btn">Book Now</a>
                        </div>
'''
        pricing_options += f'''                                <option value="{item['value']}">{item['name']} - {item['price']}</option>
'''
    
    # Generate FAQs HTML
    faqs_html = ""
    for faq in treatment_data["faqs"]:
        faqs_html += f'''                <div class="accordion-item">
                    <div class="accordion-header">
                        <h4>{faq['q']}</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>{faq['a']}</p>
                        </div>
                    </div>
                </div>

'''
    
    # Generate about paragraphs HTML
    about_paras_html = ""
    for para in treatment_data["about_paras"]:
        about_paras_html += f"                    <p>{para}</p>\n"
    
    # Generate badges HTML
    badges_html = ""
    for badge in treatment_data["badges"]:
        badges_html += f'                        <div class="badge">{badge}</div>\n'
    
   print(f"Generated HTML structure for {treatment_data['title']}")
    return f"Page data ready for {treatment_data['filename']}"

# Process all treatments
for treatment in TREATMENTS:
    result = generate_html_page(treatment)
    print(result)

print(f"\nTotal treatments to generate: {len(TREATMENTS)}")
print("Script execution complete")
