"""
Script to create all facial treatment pages based on the documentation
"""

treatments_data = {
    "skin-glow-hydrofacial.html": {
        "title": "Skin Glow: HydroFacial",
        "price": "£99",
        "tagline": "Advanced hydration and glow treatment for radiant skin",
        "about": [
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
            {"name": "Face – 1 Session", "price": "£99", "desc": "Complete HydroFacial treatment with LED therapy."},
            {"name": "Face – 3 Sessions", "price": "£267", "desc": "Package for sustained glow and hydration."},
            {"name": "Face – 4 Sessions", "price": "£336", "desc": "Extended package for optimal results."},
            {"name": "Face – 6 Sessions", "price": "£475", "desc": "Complete course for maximum transformation."}
        ],
        "frequency": "Every 4–6 weeks for maintenance and optimal results",
        "frequency_note": "Can be combined with treatments like peels, masks, or serums for enhanced effects"
    },
    
    "skin-radiance-biorepeel.html": {
        "title": "Skin Radiance: BioRePeel",
        "price": "£99",
        "tagline": "Gentle yet powerful chemical peel for skin rejuvenation",
        "about": [
            "BioRePeel is a gentle yet powerful chemical peel that combines exfoliation with bioactive nutrients to rejuvenate the skin from within. Unlike traditional peels that can be harsh, this advanced treatment works beneath the skin's surface to exfoliate, hydrate, and repair at the same time—making it safe for sensitive skin and ideal for those wanting results without downtime.",
            "Designed to stimulate collagen production, brighten the complexion, and improve overall skin texture, BioRePeel delivers both instant and long-term benefits. Skin appears plumper, fresher, and more radiant immediately after treatment, with an \"event-ready\" glow. With continued treatments, BioRePeel helps reduce pigmentation, breakouts, scarring, and fine lines, leaving the skin smoother, brighter, and more youthful with minimal peeling and minimal disruption to daily life."
        ],
        "badges": ["Cell Renewal", "Brightening", "Collagen Boost", "Minimal Downtime", "All Skin Types"],
        "benefits": [
            {"icon": "fas fa-hand-sparkles", "title": "Improves Skin Texture & Smoothness", "desc": "Removes dead skin cells and stimulates cell turnover, leaving the skin softer, smoother, and more refined."},
            {"icon": "fas fa-sun", "title": "Brightens & Evens Skin Tone", "desc": "Reduces dullness and helps correct uneven pigmentation for a more radiant, balanced complexion."},
            {"icon": "fas fa-clock-rotate-left", "title": "Reduces Fine Lines & Supports Anti-Aging", "desc": "Stimulates collagen and elastin production to improve firmness, elasticity, and skin plumpness."},
            {"icon": "fas fa-face-smile", "title": "Helps with Acne & Post-Acne Marks", "desc": "Deeply exfoliates, clears clogged pores, and helps improve mild scarring and post-inflammatory marks."},
            {"icon": "fas fa-compress", "title": "Minimises the Appearance of Pores", "desc": "Clears congestion and smooths the skin surface, making pores appear smaller and more refined."},
            {"icon": "fas fa-star", "title": "Provides a Radiant Glow with Minimal Downtime", "desc": "Often described as a \"lunchtime peel,\" delivering visible results with little to no recovery time."}
        ],
        "steps": [
            {"icon": "fas fa-user-doctor", "title": "Personalised Skin Consultation", "desc": "Your experience begins with a tailored skin analysis, allowing your practitioner to understand your concerns and customise your Bio RePeel treatment for maximum results."},
            {"icon": "fas fa-soap", "title": "Purifying Cleanse & Skin Prep", "desc": "A deep, refreshing cleanse removes makeup, oil, and impurities while preparing your skin to fully absorb the professional-grade ingredients used in the peel."},
            {"icon": "fas fa-hand-sparkles", "title": "Blackhead & Whitehead Extraction", "desc": "Gentle, targeted extractions clear congested pores, removing blackheads, whiteheads, and buildup to leave your skin smoother, clearer, and perfectly prepped for the peel."},
            {"icon": "fas fa-flask", "title": "Bio RePeel Application", "desc": "The advanced bioactive peel is applied to dissolve dull, dead skin cells, brighten pigmentation, improve texture, and stimulate fresh collagen beneath the surface."},
            {"icon": "fas fa-droplet", "title": "Hyaluronic Acid Deep Hydration Shot", "desc": "A concentrated burst of hyaluronic acid serum is applied to the skin, delivering instant plumping, smoothing, and dewy hydration. This professional infusion locks in moisture, restores softness, and enhances radiance."},
            {"icon": "fas fa-face-smile-relaxed", "title": "Relaxing Facial Massage", "desc": "A soothing massage of the face, neck, and décolletage boosts circulation, encourages lymphatic drainage, and enhances your natural glow, leaving your complexion lifted, refreshed, and luminous."},
            {"icon": "fas fa-shield-heart", "title": "Post-Treatment Glow Shield", "desc": "To finish, a protective layer of recovery serums and professional SPF is applied to lock in moisture, soothe the skin, and preserve your post-treatment glow all day."}
        ],
        "addons": [
            {"icon": "fas fa-lightbulb", "title": "LED Light Therapy – £10", "desc": "Enhances collagen production, calms inflammation, reduces redness, and accelerates skin healing. Perfect for every skin type, this add-on boosts radiance and overall glow."},
            {"icon": "fas fa-mask-face", "title": "Hydrating Jelly Mask – £10", "desc": "A soothing, cooling hydro-jelly mask that locks in hydration, reduces irritation, and leaves your complexion glassy, soft, and visibly radiant."},
            {"icon": "fas fa-dna", "title": "Collagen Peptide Booster – £15", "desc": "A professional peptide infusion that firms, softens fine lines, and supports long-term rejuvenation. Perfect for enhancing elasticity and maintaining a youthful, glowing complexion."},
            {"icon": "fas fa-syringe", "title": "Micro-Needling Add-On – £59", "desc": "A targeted micro-needling treatment that works beneath the surface to supercharge results, improving texture, promoting collagen, and enhancing overall skin vitality."}
        ],
        "pricing": [
            {"name": "Face – 1 Session", "price": "£99", "desc": "Single BioRePeel treatment."},
            {"name": "Face – 3 Sessions", "price": "£267", "desc": "Course for optimal skin renewal."},
            {"name": "Face – 4 Sessions", "price": "£336", "desc": "Extended package for deeper results."},
            {"name": "Face – 6 Sessions", "price": "£475", "desc": "Complete transformation course."},
            {"name": "Face & Neck – 1 Session", "price": "£149", "desc": "BioRePeel for face and neck."},
            {"name": "Face & Neck – 3 Sessions", "price": "£401", "desc": "Course for comprehensive renewal."},
            {"name": "Face & Neck – 4 Sessions", "price": "£506", "desc": "Extended face and neck package."},
            {"name": "Face & Neck – 6 Sessions", "price": "£715", "desc": "Full rejuvenation course."}
        ],
        "frequency": "Once per week for 3–6 consecutive weeks for initial course; every 4–6 weeks for maintenance",
        "frequency_note": "Weekly treatments may be adjusted for sensitive skin; proper home care and sun protection maximize results"
    }
}

print("Treatment data structure created successfully")
print(f"Total treatments defined: {len(treatments_data)}")
