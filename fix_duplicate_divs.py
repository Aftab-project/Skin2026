import os
import re

# Fix the duplicate closing divs that were introduced
def fix_duplicate_divs(filepath):
    """Remove the duplicate closing divs"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find and fix the duplicate closing divs
    # Look for: </div>\n                    </div>\n                </div> after benefits-grid
    pattern = r'(</div>\s*<!--\s*closing benefits-grid\s*-->\s*</div>\s*</div>)'
    
    # Actually, let's use a simpler pattern based on what we see
    # We need to remove one extra </div> that appears after the benefits-grid closes
    pattern = r'(</div>\s*</div>\s*</div>\s*<div class="results-panel">)'
    
    # This should become: </div>\n                </div>\n\n                <div class="results-panel">
    replacement = r'</div>\n                </div>\n\n                <div class="results-panel">'
    
    # But first check if the pattern matches
    if re.search(r'</div>\s*</div>\s*</div>\s*<div class="results-panel">', content):
        # Check the actual structure
        match = re.search(r'(</div>)\s*(</div>)\s*(</div>)\s*(<div class="results-panel">)', content)
        if match:
            # There's an extra </div> - remove it
            new_content = re.sub(
                r'(</div>)\s*(</div>)\s*(</div>)\s*(<div class="results-panel">)',
                r'\1\n                \2\n\n                \4',
                content
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed duplicate divs in {os.path.basename(filepath)}")
            return True
    
    return False

# Main execution
treatments_dir = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

pages_to_fix = [
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

fixed_count = 0
for filename in pages_to_fix:
    filepath = os.path.join(treatments_dir, filename)
    if os.path.exists(filepath):
        if fix_duplicate_divs(filepath):
            fixed_count += 1
    else:
        print(f"✗ File not found: {filename}")

if fixed_count == 0:
    print("No duplicate divs found to fix, or they don't exist in the expected pattern")
else:
    print(f"\n✓ Fixed {fixed_count} files")
