import os
import json

# Define all treatments to create based on the Microneedling RF.md file
treatments = {
    "fractional-rf-microneedling-body": {
        "title": "Fractional RF + Microneedling Body Treatments",
        "tagline": "Advanced skin tightening and body contouring with Fractional RF + Microneedling",
        "about": "Take your body sculpting to the next level with our Fractional RF + Microneedling combination, designed to tighten, lift, and remodel skin while targeting stretch marks, sagging, and uneven texture. This dual-action treatment combines Fractional Radio Frequency (RF) and Microneedling to maximize skin regeneration, improve elasticity, and smooth stretch marks, delivering visible lifting and contouring results on arms, thighs, stomach, back, and other areas.",
        "areas": ["Arms", "Back", "Thighs", "Stomach", "Other Areas", "Stretch Marks"],
        "pricing": {"Arms": 175, "Back": 175, "Thighs": 175, "Stomach": 175, "Other Areas": 175, "Stretch Marks": 175},
        "course": "3–6 sessions spaced 4–6 weeks apart",
        "maintenance": "Every 4–6 months"
    },
    "stretch-mark-resurfacing": {
        "title": "Stretch Mark Resurfacing",
        "tagline": "Advanced corrective treatment with Fractional RF + Microneedling",
        "about": "Stretch Mark Resurfacing with Fractional RF + Microneedling is an advanced corrective treatment designed to visibly improve the appearance of stretch marks by repairing weakened skin structure, tightening tissue, and smoothing texture.",
        "areas": ["Body Area"],
        "pricing": {"1 Session": 175, "3 Sessions": 473, "6 Sessions": 893},
        "course": "4–6 sessions spaced 4–6 weeks apart",
        "maintenance": "1–2 sessions per year"
    },
    "skin-blur-microneedling": {
        "title": "Skin Blur Microneedling",
        "tagline": "Non-surgical skin rejuvenation for smoothness and radiance",
        "about": "Our Skin Blur Microneedling treatment is a non-surgical skin rejuvenation solution that smooths fine lines, diminishes scarring, and refines uneven texture for a brighter, more even complexion. Skin Blur works like a subtle blur filter for your skin — softening imperfections, minimizing pores, and smoothing texture.",
        "areas": ["Face", "Face & Neck", "Body Area"],
        "pricing": {"Face": 125, "Face & Neck": 175, "Body Area": 149},
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "1–2 sessions per year"
    },
    "brightening-c-microneedling": {
        "title": "Brightening C Microneedling",
        "tagline": "Even skin tone and boost radiance with Vitamin C infusion",
        "about": "Take your skin glow to the next level with our Brightening C Microneedling, a dual-action treatment designed to even skin tone, reduce pigmentation, boost radiance, and improve skin texture and firmness. This premium treatment combines microneedling with Vitamin C infusion.",
        "areas": ["Face", "Face & Neck", "Body Area"],
        "pricing": {"Face": 175, "Face & Neck": 249, "Body Area": 175},
        "course": "3–6 sessions spaced 4 weeks apart",
        "maintenance": "Every 2–3 months"
    },
    "hydra-glow-microneedling": {
        "title": "Hydra-Glow Microneedling",
        "tagline": "Luxurious hydration and radiance with mini-hydrofacial fusion",
        "about": "Elevate your skin's hydration and radiance with Hydra-Glow Microneedling, a luxurious dual-action treatment that fuses microneedling with a mini-hydrofacial. This advanced treatment deeply hydrates, smooths, and rejuvenates the skin while stimulating natural collagen and elastin production.",
        "areas": ["Face", "Face & Neck", "Body Area"],
        "pricing": {"Face": 175, "Face & Neck": 249, "Body Area": 175},
        "course": "3–6 sessions spaced 4 weeks apart",
        "maintenance": "Every 2–3 months"
    },
    "firming-peptide-microneedling": {
        "title": "Firming Peptide Microneedling",
        "tagline": "Restore firmness and define your natural contours",
        "about": "Restore firmness, lift sagging areas, and define your natural contours with Firming Peptide Microneedling. This advanced treatment combines precision microneedling with targeted peptide serums designed to stimulate collagen and elastin production.",
        "areas": ["Face", "Face & Neck", "Body Area"],
        "pricing": {"Face": 175, "Face & Neck": 249, "Body Area": 175},
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months"
    },
    "cellular-boost-exosomes-microneedling": {
        "title": "Cellular Boost: Exosomes + Microneedling",
        "tagline": "Next-generation treatment with cellular messengers",
        "about": "Revolutionize your skin with Cellular Boost: Microneedling + Exosomes, a next-generation treatment that combines precision microneedling with advanced exosome therapy. Exosomes — naturally derived cellular messengers — accelerate repair, stimulate collagen and elastin, and boost cellular turnover.",
        "areas": ["Face", "Face & Neck", "Body Area"],
        "pricing": {"Face": 175, "Face & Neck": 249, "Body Area": 175},
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months"
    },
    "scalp-revive-microneedling-exosomes": {
        "title": "Scalp Revive: Microneedling + Exosomes",
        "tagline": "Revitalize hair follicles and support natural hair growth",
        "about": "Bring your scalp back to life with Scalp Revive, a cutting-edge treatment combining precision microneedling with regenerative exosomes. This dual-action therapy stimulates blood flow, revitalizes hair follicles, and supports natural hair growth.",
        "areas": ["Scalp"],
        "pricing": {"Scalp - 1 Session": 175, "Scalp - 3 Sessions": 420, "Scalp - 6 Sessions": 735},
        "course": "3–6 sessions spaced 4–6 weeks apart",
        "maintenance": "Every 3–4 months"
    },
    "green-peel-bio-microneedling": {
        "title": "Green Peel – Bio Microneedling",
        "tagline": "Natural herbal-based skin resurfacing",
        "about": "The Green Peel is a natural, herbal-based skin resurfacing treatment that stimulates the skin's regeneration using plant-derived ingredients. Suitable for face, neck, décolleté, and body areas, it boosts circulation, accelerates cell turnover, and strengthens the skin from within.",
        "areas": ["Face", "Face & Neck", "Body Area"],
        "pricing": {"Face": 99, "Face & Neck": 149, "Body Area": 125},
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 3–6 months"
    },
    "skin-revive-microneedling-biorepeel": {
        "title": "Skin Revive: Microneedling + BioRePeel",
        "tagline": "Transformative dual-action skin renewal",
        "about": "Rejuvenate and restore your complexion with Skin Revive, a transformative treatment combining precise microneedling with the powerful BioRePeel. Designed to smooth texture, reduce acne scars, refine pores, and restore firmness, this dual-action treatment stimulates collagen production and promotes deep skin renewal.",
        "areas": ["Face", "Face & Neck"],
        "pricing": {"Face": 175, "Face & Neck": 225},
        "course": "3–6 treatments",
        "maintenance": "Every 4–6 weeks"
    }
}

print(json.dumps(treatments, indent=2))
print("\n✓ Treatment data defined successfully!")
print(f"Total treatments to create: {len(treatments)}")
