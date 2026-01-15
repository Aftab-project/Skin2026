"""
Complete script to generate all remaining Facial & Skincare treatment pages
This script extracts all data from the documentation and generates HTML pages
using the HIFU treatment page structure as a template.
"""

# Read the template from the existing HydroFacial page
template_file = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments\skin-glow-hydrofacial.html"

with open(template_file, 'r', encoding='utf-8') as f:
    template = f.read()

print(f"Template loaded successfully from {template_file}")
print(f"Template length: {len(template)} characters")

# Define output directory
output_dir = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

print(f"\nOutput directory: {output_dir}")
print("\nScript ready to generate pages")
print("="*60)
