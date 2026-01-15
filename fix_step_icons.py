#!/usr/bin/env python3
"""
Fix icons in all Microneedling RF treatment pages
Each step should have a unique appropriate icon
"""

import os
import re

BASE_DIR = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

# List of pages to update
pages = [
    "fractional-rf-microneedling-face-neck.html",
    "fractional-rf-microneedling-body.html",
    "stretch-mark-resurfacing.html",
    "skin-blur-microneedling.html",
    "brightening-c-microneedling.html",
    "hydra-glow-microneedling.html",
    "firming-peptide-microneedling.html",
    "cellular-boost-exosomes-microneedling.html",
    "scalp-revive-microneedling-exosomes.html",
    "green-peel-bio-microneedling.html",
    "skin-revive-microneedling-biorepeel.html"
]

# Standard icon set for common step types
standard_icons = {
    1: "fa-spa",              # Cleansing/Prep
    2: "fa-location-crosshairs",  # Assessment/Mapping
    3: "fa-bolt",             # Main treatment/Energy
    4: "fa-face-smile",       # Contouring/Focus
    5: "fa-droplet",          # Serums/Hydration
    6: "fa-shield-heart"      # Protection/Finish
}

for page in pages:
    filepath = os.path.join(BASE_DIR, page)
    
    if not os.path.exists(filepath):
        print(f"⚠ Skipping {page} - file not found")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all step cards and replace icons
    step_pattern = r'(<div class="step-number">(\d+)</div>\s*<div class="step-icon">\s*<i class="fas )fa-spa("></i>)'
    
    def replace_icon(match):
        prefix = match.group(1)
        step_num = int(match.group(2))
        suffix = match.group(3)
        
        # Get the appropriate icon for this step
        icon = standard_icons.get(step_num, "fa-spa")
        
        return f'{prefix}{icon}{suffix}'
    
    # Replace all icons
    new_content = re.sub(step_pattern, replace_icon, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated icons in {page}")
    else:
        print(f"⚠ No changes needed for {page}")

print(f"\n✓ All icons updated!")
