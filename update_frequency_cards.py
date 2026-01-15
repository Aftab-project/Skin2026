#!/usr/bin/env python3
"""
Replace the simple Recommended Course div with the frequency-card structure
"""

import os
import re

BASE_DIR = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

# Mapping of pages to their course and maintenance info
page_info = {
    "fractional-rf-microneedling-face-neck.html": {
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months to sustain skin firmness, smoothness, and rejuvenation.",
        "subtitle": "Optimize lifting, tightening, and long-term skin renewal."
    },
    "fractional-rf-microneedling-body.html": {
        "course": "3–6 sessions spaced 4–6 weeks apart",
        "maintenance": "Every 4–6 months to maintain firmness, smoothness, and skin quality.",
        "subtitle": "Maximize body contouring and skin tightening results."
    },
    "stretch-mark-resurfacing.html": {
        "course": "4–6 sessions spaced 4–6 weeks apart",
        "maintenance": "1–2 sessions per year to maintain skin strength and smoothness.",
        "subtitle": "Progressive improvement of stretch mark appearance and skin texture."
    },
    "skin-blur-microneedling.html": {
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "1–2 sessions per year to maintain smooth, refined skin texture.",
        "subtitle": "Build collagen and refine skin for a naturally polished finish."
    },
    "brightening-c-microneedling.html": {
        "course": "3–6 sessions spaced 4 weeks apart",
        "maintenance": "Every 2–3 months to sustain brightness, firmness, and radiance.",
        "subtitle": "Achieve even tone, glow, and long-lasting radiance."
    },
    "hydra-glow-microneedling.html": {
        "course": "3–6 sessions spaced 4 weeks apart",
        "maintenance": "Every 2–3 months to sustain hydration, firmness, and glow.",
        "subtitle": "Deep hydration and radiance for plump, youthful skin."
    },
    "firming-peptide-microneedling.html": {
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months to sustain lifting, firmness, and collagen production.",
        "subtitle": "Lift, firm, and define for a naturally sculpted appearance."
    },
    "cellular-boost-exosomes-microneedling.html": {
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 4–6 months to sustain results and continue cellular rejuvenation.",
        "subtitle": "Accelerate skin renewal and cellular regeneration."
    },
    "scalp-revive-microneedling-exosomes.html": {
        "course": "3–6 sessions spaced 4–6 weeks apart",
        "maintenance": "Every 3–4 months to sustain hair health and scalp regeneration.",
        "subtitle": "Stimulate follicles and support natural hair growth."
    },
    "green-peel-bio-microneedling.html": {
        "course": "3–6 sessions spaced 3–4 weeks apart",
        "maintenance": "Every 3–6 months depending on skin concerns and desired results.",
        "subtitle": "Natural herbal renewal for radiant, healthy skin."
    },
    "skin-revive-microneedling-biorepeel.html": {
        "course": "3–6 treatments spaced 4–6 weeks apart",
        "maintenance": "Every 4–6 weeks to maintain smooth texture and firmness.",
        "subtitle": "Dual-action renewal for texture, tone, and radiance."
    }
}

def create_frequency_card(course, maintenance, subtitle):
    return f'''                    <div class="frequency-card">
                        <div class="frequency-header">
                            <div class="frequency-icon"><i class="fas fa-clock"></i></div>
                            <div>
                                <p class="frequency-title">Recommended Frequency</p>
                                <p class="frequency-sub">{subtitle}</p>
                            </div>
                        </div>
                        <div class="frequency-rows">
                            <div class="frequency-row">
                                <div class="frequency-bullet"></div>
                                <div>
                                    <p class="frequency-label">Initial Course</p>
                                    <p class="frequency-copy">{course}</p>
                                </div>
                            </div>
                            <div class="frequency-row">
                                <div class="frequency-bullet"></div>
                                <div>
                                    <p class="frequency-label">Maintenance</p>
                                    <p class="frequency-copy">{maintenance}</p>
                                </div>
                            </div>
                        </div>
                    </div>'''

for page, info in page_info.items():
    filepath = os.path.join(BASE_DIR, page)
    
    if not os.path.exists(filepath):
        print(f"⚠ Skipping {page} - file not found")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the old simple div structure
    old_pattern = r'<div style="margin-top: 30px; padding: 20px; background: #f9f7f3; border-left: 4px solid #d6ad60; border-radius: 8px;">.*?</div>\s*</div>'
    
    # Find and replace the old structure
    if re.search(old_pattern, content, re.DOTALL):
        # Create the new frequency card
        new_card = create_frequency_card(info['course'], info['maintenance'], info['subtitle'])
        
        # Replace the old div with new frequency card, keeping the closing </div> for pricing column
        content = re.sub(
            old_pattern,
            new_card + '\n                </div>',
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {page}")
    else:
        print(f"⚠ Pattern not found in {page}")

print(f"\n✓ All Recommended Course sections updated to frequency-card design!")
