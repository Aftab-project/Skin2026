#!/usr/bin/env python3
"""
Refactor all treatment pages to new layout
Creates refactored HTML based on template and treatment data
"""

treatment_data = {
    "korean-facial.html": {
        "title": "Skin Glass: Korean Facial",
        "tagline": "Multi-step Korean beauty ritual for luminous, glass-like skin",
        "price": "£99",
        "duration": "60 minutes"
    },
    "oxygeno-facial.html": {
        "title": "Skin Oxyglow: OxygenO Facial",
        "tagline": "Oxygen infusion for instant glow and deep cellular rejuvenation",
        "price": "£89",
        "duration": "45 minutes"
    },
    "biorepeel.html": {
        "title": "Skin Radiance: BioRePeel",
        "tagline": "Advanced biochemical peel for renewal and radiant transformation",
        "price": "£99",
        "duration": "45 minutes"
    },
    "biomicroneedling.html": {
        "title": "Green Peel – BioMicroneedling",
        "tagline": "Herbal microneedling for natural skin renewal and rejuvenation",
        "price": "£89",
        "duration": "45 minutes"
    },
    "chemical-peel.html": {
        "title": "Skin Renewal: Chemical Peel",
        "tagline": "Professional chemical peel for dramatic skin transformation",
        "price": "£99",
        "duration": "45 minutes"
    },
    "microneedling-biorepeel.html": {
        "title": "Skin Revive: Microneedling + BioRePeel",
        "tagline": "Dual-action treatment for maximum skin transformation",
        "price": "£149",
        "duration": "60 minutes"
    },
    "rf-facial.html": {
        "title": "Skin LumaLift: Radio Frequency Facial",
        "tagline": "Advanced RF technology for non-invasive skin tightening",
        "price": "£129",
        "duration": "60 minutes"
    },
    "ultimate-exfoliation.html": {
        "title": "Skin Luxe Satin: Ultimate Exfoliation",
        "tagline": "Triple-exfoliation facial for ultimate smoothness and radiance",
        "price": "£99",
        "duration": "45 minutes"
    },
    "blackhead-extraction.html": {
        "title": "Deep Blackhead Extraction",
        "tagline": "Professional deep-pore extraction for clear, refined skin",
        "price": "£79",
        "duration": "45 minutes"
    },
    "bb-glow.html": {
        "title": "Skin Balance: BB Glow",
        "tagline": "Semi-permanent tinted coverage with skincare benefits",
        "price": "£125",
        "duration": "60 minutes"
    }
}

# HIFU treatments
hifu_treatments = {
    "hifu-face.html": {"title": "HIFU Face", "tagline": "Non-invasive facial lifting and tightening", "price": "£199", "duration": "60 minutes"},
    "hifu-neck.html": {"title": "HIFU Neck", "tagline": "Professional neck and jawline tightening", "price": "£149", "duration": "45 minutes"},
    "hifu-face-neck.html": {"title": "HIFU Face and Neck", "tagline": "Complete facial and neck rejuvenation", "price": "£299", "duration": "90 minutes"},
    "hifu-jawline.html": {"title": "HIFU Jawline Definition", "tagline": "Enhanced jawline definition and contour", "price": "£179", "duration": "60 minutes"},
    "hifu-butt-lift.html": {"title": "HIFU Butt Lift", "tagline": "Non-invasive buttock lifting and tightening", "price": "£299", "duration": "60 minutes"},
    "hifu-breast-lift.html": {"title": "HIFU Breast Lift", "tagline": "Non-invasive breast lift and firmness", "price": "£349", "duration": "75 minutes"},
    "hifu-stomach.html": {"title": "HIFU Stomach Tightening", "tagline": "Abdominal tightening and contouring", "price": "£279", "duration": "60 minutes"},
    "hifu-love-handles.html": {"title": "HIFU Love Handles", "tagline": "Targeted love handles and side tightening", "price": "£199", "duration": "45 minutes"},
    "hifu-inner-thighs.html": {"title": "HIFU Inner Thighs", "tagline": "Inner thigh tightening and lifting", "price": "£249", "duration": "60 minutes"},
    "hifu-outer-thighs.html": {"title": "HIFU Outer Thighs", "tagline": "Outer thigh firming and definition", "price": "£249", "duration": "60 minutes"},
    "hifu-banana-rolls.html": {"title": "HIFU Banana Rolls", "tagline": "Under-buttock tightening and lifting", "price": "£199", "duration": "45 minutes"},
    "hifu-arms.html": {"title": "HIFU Arms", "tagline": "Arm tightening and definition", "price": "£199", "duration": "45 minutes"},
    "hifu-stomach-love-handles.html": {"title": "Stomach + Love Handles Bundle", "tagline": "Combined stomach and love handles treatment", "price": "£449", "duration": "90 minutes"}
}

print(f"Total treatments to refactor: {len(treatment_data) + len(hifu_treatments)}")
print("\nFacial treatments: " + ", ".join(treatment_data.keys())[:80] + "...")
print("HIFU treatments: " + str(len(hifu_treatments)) + " pages")
