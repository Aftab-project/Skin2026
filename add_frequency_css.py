#!/usr/bin/env python3
"""
Update all Microneedling RF pages to use the proper frequency-card design
matching the HIFU pages
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

# CSS to add before the closing </style> tag
frequency_card_css = """
        .frequency-card {
            margin-top: 18px;
            padding: 18px 16px;
            border: 1px solid rgba(214, 173, 96, 0.3);
            border-radius: 12px;
            background: linear-gradient(135deg, #fffdf8 0%, #fffaf2 100%);
            box-shadow: 0 6px 18px rgba(214, 173, 96, 0.12);
        }

        .frequency-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }

        .frequency-icon {
            width: 42px;
            height: 42px;
            border-radius: 10px;
            background: linear-gradient(135deg, #d6ad60, #e9c67d);
            color: #fff;
            display: grid;
            place-items: center;
            font-size: 18px;
            box-shadow: 0 4px 10px rgba(214, 173, 96, 0.35);
        }

        .frequency-title {
            margin: 0;
            font-size: 15px;
            font-weight: 700;
            color: #1b1b1b;
        }

        .frequency-sub {
            margin: 2px 0 0 0;
            font-size: 13px;
            color: #666;
        }

        .frequency-rows {
            display: grid;
            gap: 10px;
        }

        .frequency-row {
            display: grid;
            grid-template-columns: auto 1fr;
            align-items: flex-start;
            gap: 10px;
            padding: 10px 0;
            border-top: 1px dashed rgba(214, 173, 96, 0.35);
        }

        .frequency-row:first-child {
            border-top: none;
            padding-top: 0;
        }

        .frequency-bullet {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: linear-gradient(135deg, #d6ad60, #e9c67d);
            box-shadow: 0 0 0 4px rgba(214, 173, 96, 0.15);
            margin-top: 4px;
        }

        .frequency-label {
            margin: 0;
            font-weight: 700;
            color: #1b1b1b;
            font-size: 14px;
        }

        .frequency-copy {
            margin: 4px 0 0 0;
            font-size: 13px;
            color: #555;
            line-height: 1.55;
        }
"""

for page in pages:
    filepath = os.path.join(BASE_DIR, page)
    
    if not os.path.exists(filepath):
        print(f"⚠ Skipping {page} - file not found")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add the frequency card CSS before </style> if not already present
    if '.frequency-card' not in content:
        content = content.replace('    </style>', frequency_card_css + '    </style>')
        print(f"✓ Added frequency-card CSS to {page}")
    else:
        print(f"⚠ CSS already exists in {page}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"\n✓ All pages updated with frequency-card styling!")
