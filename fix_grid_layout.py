#!/usr/bin/env python3
"""
Update all Microneedling RF pages to match HIFU styling
- Fix grid to be 3x3 layout
- Ensure consistent colors
"""

import os
import re

BASE_DIR = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

# List of new Microneedling RF pages to update
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

# Old grid style (auto-fit)
old_grid_style = """        .experience-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 35px;
            margin-top: 45px;
        }"""

# New grid style (3 columns like HIFU)
new_grid_style = """        .experience-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(240px, 1fr));
            gap: 28px;
            margin-top: 45px;
        }"""

for page in pages:
    filepath = os.path.join(BASE_DIR, page)
    
    if not os.path.exists(filepath):
        print(f"⚠ Skipping {page} - file not found")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the grid style
    if old_grid_style in content:
        content = content.replace(old_grid_style, new_grid_style)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {page}")
    else:
        print(f"⚠ Grid style not found in {page}")

print(f"\n✓ Grid layout updated to 3-column layout for all pages!")
