import os
import re

# Define benefit details for each treatment
benefits_data = {
    "fractional-rf-microneedling-face-neck.html": [
        ("Tightens Sagging Skin", "Restores firmness and youthful definition", "fas fa-arrow-up"),
        ("Lifts Face and Neck", "Enhances contour and reduces laxity", "fas fa-face-smile"),
        ("Smooths Wrinkles & Fine Lines", "Diminishes signs of aging", "fas fa-wand-magic-sparkles"),
        ("Improves Skin Texture", "Refines and smooths surface", "fas fa-spa"),
        ("Boosts Collagen & Elastin", "Stimulates natural skin regeneration", "fas fa-heart-pulse"),
        ("Non-Surgical Minimal Downtime", "High-impact results without surgery", "fas fa-thumbs-up")
    ],
    "fractional-rf-microneedling-body.html": [
        ("Firms Loose Body Skin", "Tightens and tones sagging areas", "fas fa-arrow-up"),
        ("Improves Stretch Marks", "Reduces texture irregularities", "fas fa-sparkles"),
        ("Smooths Uneven Texture", "Refines crepey or dimpled skin", "fas fa-spa"),
        ("Enhances Body Contour", "Improves definition and curves", "fas fa-person"),
        ("Stimulates Collagen Renewal", "Triggers deep tissue regeneration", "fas fa-heart-pulse"),
        ("Minimal Downtime Non-Invasive", "Results without extended recovery", "fas fa-thumbs-up")
    ],
    "stretch-mark-resurfacing.html": [
        ("Reduces Visible Stretch Marks", "Targets depth and texture", "fas fa-circle-check"),
        ("Repairs Damaged Skin Fibres", "Rebuilds collagen structure", "fas fa-tools"),
        ("Smooths Indented Texture", "Blends marks with surrounding skin", "fas fa-spa"),
        ("Tightens Stretched Skin", "Improves elasticity", "fas fa-arrow-up"),
        ("Improves Skin Density", "Strengthens and thickens skin", "fas fa-shield-heart"),
        ("Works on Old & New Marks", "Effective on all stretch mark types", "fas fa-clock")
    ],
    "skin-blur-microneedling.html": [
        ("Smooths Skin Texture", "Refines and polishes surface", "fas fa-spa"),
        ("Minimises Pores", "Reduces pore appearance", "fas fa-circle-dot"),
        ("Reduces Acne Scars", "Improves scar appearance", "fas fa-circle-check"),
        ("Softens Fine Lines", "Smooths and rejuvenates", "fas fa-wand-magic-sparkles"),
        ("Boosts Natural Radiance", "Restores glow and luminosity", "fas fa-sun"),
        ("Improves Overall Skin Tone", "Evens and brightens complexion", "fas fa-face-smile")
    ],
    "brightening-c-microneedling.html": [
        ("Brightens Dull Skin", "Restores natural glow", "fas fa-sun"),
        ("Reduces Pigmentation", "Fades dark spots and discoloration", "fas fa-circle-check"),
        ("Evens Skin Tone", "Balances complexion", "fas fa-face-smile"),
        ("Boosts Collagen Production", "Stimulates natural renewal", "fas fa-heart-pulse"),
        ("Improves Skin Texture", "Refines and smooths", "fas fa-spa"),
        ("Enhances Long-Lasting Glow", "Prolongs radiance results", "fas fa-sparkles")
    ],
    "hydra-glow-microneedling.html": [
        ("Deeply Hydrates Skin", "Infuses intensive moisture", "fas fa-droplet"),
        ("Restores Instant Glow", "Revives luminosity immediately", "fas fa-sun"),
        ("Smooths Fine Lines", "Diminishes wrinkles", "fas fa-wand-magic-sparkles"),
        ("Improves Skin Elasticity", "Enhances firmness and bounce", "fas fa-arrow-up"),
        ("Refines Texture", "Creates smooth surface", "fas fa-spa"),
        ("Leaves Skin Plump & Dewy", "Delivers dewy, youthful finish", "fas fa-face-smile")
    ],
    "firming-peptide-microneedling.html": [
        ("Firms and Lifts Skin", "Tightens sagging areas", "fas fa-arrow-up"),
        ("Improves Elasticity", "Restores skin resilience", "fas fa-heart-pulse"),
        ("Defines Facial Contours", "Enhances natural definition", "fas fa-face-smile"),
        ("Reduces Early Aging Signs", "Targets fine lines and loss of firmness", "fas fa-wand-magic-sparkles"),
        ("Strengthens Skin Barrier", "Improves skin health", "fas fa-shield-heart"),
        ("Boosts Collagen Support", "Stimulates natural regeneration", "fas fa-sparkles")
    ],
    "cellular-boost-exosomes-microneedling.html": [
        ("Accelerates Skin Repair", "Speeds up healing process", "fas fa-bolt"),
        ("Boosts Collagen & Elastin", "Stimulates deep regeneration", "fas fa-heart-pulse"),
        ("Improves Skin Firmness", "Tightens and tones", "fas fa-arrow-up"),
        ("Smooths Texture & Tone", "Refines and evens", "fas fa-spa"),
        ("Enhances Cellular Renewal", "Triggers cellular regeneration", "fas fa-circle-check"),
        ("Strengthens Skin Barrier", "Improves protection and resilience", "fas fa-shield-heart")
    ],
    "scalp-revive-microneedling-exosomes.html": [
        ("Stimulates Hair Follicles", "Activates dormant growth", "fas fa-sprout"),
        ("Supports Hair Regrowth", "Encourages natural hair growth", "fas fa-leaf"),
        ("Improves Scalp Circulation", "Enhances blood flow", "fas fa-heart-pulse"),
        ("Strengthens Hair Roots", "Reduces breakage and shedding", "fas fa-shield-heart"),
        ("Enhances Scalp Health", "Improves overall scalp wellness", "fas fa-spa"),
        ("Reduces Thinning & Shedding", "Supports fuller, stronger hair", "fas fa-circle-check")
    ],
    "green-peel-bio-microneedling.html": [
        ("Boosts Skin Renewal", "Stimulates cell turnover", "fas fa-circle-check"),
        ("Improves Texture & Tone", "Refines and evens", "fas fa-spa"),
        ("Reduces Acne & Congestion", "Clears and purifies", "fas fa-face-smile"),
        ("Fades Pigmentation", "Reduces dark spots and discoloration", "fas fa-sun"),
        ("Enhances Circulation", "Increases blood flow and vitality", "fas fa-heart-pulse"),
        ("Promotes Natural Glow", "Restores radiance naturally", "fas fa-sparkles")
    ],
    "skin-revive-microneedling-biorepeel.html": [
        ("Smooths Scars & Texture", "Improves surface irregularities", "fas fa-spa"),
        ("Brightens Skin Tone", "Restores luminosity", "fas fa-sun"),
        ("Boosts Collagen Production", "Stimulates deep regeneration", "fas fa-heart-pulse"),
        ("Refines Pores", "Minimizes pore appearance", "fas fa-circle-dot"),
        ("Improves Firmness", "Tightens and lifts", "fas fa-arrow-up"),
        ("Delivers Visible Rejuvenation", "Noticeable improvement in appearance", "fas fa-wand-magic-sparkles")
    ]
}

def create_benefit_cards(benefits):
    """Create HTML for benefit cards"""
    cards_html = ""
    for title, description, icon in benefits:
        cards_html += f'''                        <div class="benefit-card">
                            <div class="icon"><i class="{icon}"></i></div>
                            <h4>{title}</h4>
                            <p>{description}</p>
                        </div>
'''
    return cards_html

def update_benefit_cards(filepath, benefits):
    """Update benefit cards in a treatment file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the benefits-grid section
    pattern = r'(<div class="benefits-grid">)(.*?)(</div>\s*</div>\s*</div>\s*<div class="results-panel">)'
    
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # Create new cards
        new_cards = create_benefit_cards(benefits)
        
        # Replace the old cards with new ones
        new_content = re.sub(
            pattern,
            rf'\1\n{new_cards}                    \3',
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated benefit cards in {os.path.basename(filepath)}")
    else:
        print(f"⚠ Could not find benefits-grid pattern in {os.path.basename(filepath)}")

# Main execution
treatments_dir = r"c:\Users\t-aftabkhan\OneDrive - Microsoft\Desktop\MiliSkin&Beauty - Copy (2)\treatments"

for filename, benefits in benefits_data.items():
    filepath = os.path.join(treatments_dir, filename)
    if os.path.exists(filepath):
        update_benefit_cards(filepath, benefits)
    else:
        print(f"✗ File not found: {filename}")
