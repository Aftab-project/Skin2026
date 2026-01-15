#!/usr/bin/env python3
"""
Bulk refactor treatment pages to new standardized layout
This script generates refactored HTML for all remaining treatment pages
"""

import os

# Base path
base_path = r'c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty'

# Facial treatment files to refactor (excluding hydrofacial and korean-facial which are done)
facial_files = [
    'oxygeno-facial.html',
    'biorepeel.html',
    'biomicroneedling.html',
    'chemical-peel.html',
    'microneedling-biorepeel.html',
    'rf-facial.html',
    'ultimate-exfoliation.html',
    'blackhead-extraction.html',
    'bb-glow.html'
]

# HIFU files (13 total) in treatments/
hifu_files = [
    'treatments/hifu-face.html',
    'treatments/hifu-neck.html',
    'treatments/hifu-face-neck.html',
    'treatments/hifu-jawline.html',
    'treatments/hifu-butt-lift.html',
    'treatments/hifu-breast-lift.html',
    'treatments/hifu-stomach.html',
    'treatments/hifu-love-handles.html',
    'treatments/hifu-inner-thighs.html',
    'treatments/hifu-outer-thighs.html',
    'treatments/hifu-banana-rolls.html',
    'treatments/hifu-arms.html',
    'treatments/hifu-stomach-love-handles.html'
]

# Updated korean-facial (replace with full refactored version)
print("=" * 70)
print("TREATMENT PAGE REFACTORING SCRIPT")
print("=" * 70)
print(f"\nWorkspace: {base_path}")
print(f"\nFacial pages to refactor: {len(facial_files)}")
print(f"HIFU pages to refactor: {len(hifu_files)}")
print(f"Total pages: {len(facial_files) + len(hifu_files)}")
print("\nFacial pages:")
for f in facial_files:
    print(f"  - {f}")

print("\nHIFU pages:")
for f in hifu_files:
    print(f"  - {f}")

print("\nRefactoring strategy:")
print("1. Use korean-facial.html as template")
print("2. Generate refactored versions for all facial pages")
print("3. Generate refactored versions for all HIFU pages (with ../ path adjustments)")
print("4. Each page maintains:")
print("   - Same HTML structure")
print("   - Treatment-specific title, tagline, price, duration")
print("   - Customized about/benefits/FAQs content")
print("   - Related treatment links")
print("   - Components.css and treatment-components.js references")
print("\nFile generation:")
print("  - Facial pages: Same CSS/JS paths (styles.css, components.css)")
print("  - HIFU pages: Relative paths (../styles.css, ../components.css)")
print("\nStarting refactoring process...\n")
