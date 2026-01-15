#!/usr/bin/env python3
"""
Generate 9 refactored facial treatment HTML pages based on hydrofacial.html template.
Customizes: title, tagline, meta description, og:title/og:description, pricing, 
form treatment name, and related treatments links.
"""

from importlib.machinery import SourceFileLoader
import os

# Read the hydrofacial.html template
template_path = os.path.join(os.path.dirname(__file__), 'hydrofacial.html')
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Load richer content (about paragraphs, benefits, related) from refactor_config
config_path = os.path.join(os.path.dirname(__file__), 'refactor_config.json')
config_module = SourceFileLoader("refactor_config", config_path).load_module()
rich_content = getattr(config_module, "treatments", {})

# Define treatment data
treatments = [
    {
        'filename': 'oxygeno-facial.html',
        'subdir': '',
        'title': 'Skin Oxyglow: OxygenO Facial',
        'tagline': 'Oxygen infusion for instant glow and deep rejuvenation',
        'meta_description': 'Skin Oxyglow OxygenO Facial at Mili Skin & Beauty - Oxygen-infused facial for instant glow and deep rejuvenation with premium serums. Book your OxygenO Facial treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Oxygen-infused facial for instant glow and deep rejuvenation with premium serums.',
        'single_price': '£89',
        'single_value': '£89',
        '3pack_price': '£240',
        '3pack_value': '£240',
        '6pack_price': '£425',
        '6pack_value': '£425',
        'treatment_form_value': 'Skin Oxyglow: OxygenO Facial',
        'related_1': 'korean-facial.html',
        'related_1_title': 'Skin Glass: Korean Facial',
        'related_1_desc': 'Multi-step Korean facial for luminous, glass-like skin with advanced serums and techniques.',
        'related_1_price': 'From £99',
        'related_2': 'biorepeel.html',
        'related_2_title': 'Skin Radiance: BioRePeel',
        'related_2_desc': 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.',
        'related_2_price': 'From £99',
        'related_3': 'hydrofacial.html',
        'related_3_title': 'Skin Glow: Hydrofacial',
        'related_3_desc': 'Deep cleansing, hydration, and instant radiance with our professional Hydrofacial treatment.',
        'related_3_price': 'From £99',
    },
    {
        'filename': 'bb-glow.html',
        'subdir': '',
        'title': 'Skin Balance: BB Glow',
        'tagline': 'Semi-permanent tinted coverage for natural radiant skin',
        'meta_description': 'Skin Balance BB Glow at Mili Skin & Beauty - Semi-permanent tinted coverage treatment for natural, radiant skin appearance. Book your BB Glow treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Semi-permanent tinted coverage treatment for natural, radiant skin appearance.',
        'single_price': '£125',
        'single_value': '£125',
        '3pack_price': '£349',
        '3pack_value': '£349',
        '6pack_price': '£649',
        '6pack_value': '£649',
        'treatment_form_value': 'Skin Balance: BB Glow',
        'related_1': 'blackhead-extraction.html',
        'related_1_title': 'Deep Blackhead Extraction',
        'related_1_desc': 'Professional extraction treatment for clear, blemish-free skin.',
        'related_1_price': 'From £79',
        'related_2': 'oxygeno-facial.html',
        'related_2_title': 'Skin Oxyglow: OxygenO Facial',
        'related_2_desc': 'Oxygen infusion facial for instant glow and deep rejuvenation with premium serums.',
        'related_2_price': 'From £89',
        'related_3': 'hydrofacial.html',
        'related_3_title': 'Skin Glow: Hydrofacial',
        'related_3_desc': 'Deep cleansing, hydration, and instant radiance with our professional Hydrofacial treatment.',
        'related_3_price': 'From £99',
    },
    {
        'filename': 'biorepeel.html',
        'title': 'Skin Radiance: BioRePeel',
        'tagline': 'Advanced chemical peel for cell renewal and radiant skin',
        'meta_description': 'Skin Radiance BioRePeel at Mili Skin & Beauty - Advanced chemical peel for cell renewal and radiant, rejuvenated complexion. Book your BioRePeel treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.',
        'single_price': '£99',
        'single_value': '£99',
        '3pack_price': '£279',
        '3pack_value': '£279',
        '6pack_price': '£519',
        '6pack_value': '£519',
        'treatment_form_value': 'Skin Radiance: BioRePeel',
        'related_1': 'chemical-peel.html',
        'related_1_title': 'Skin Renewal: Chemical Peel',
        'related_1_desc': 'Professional chemical exfoliation for smoother, brighter, more youthful-looking skin.',
        'related_1_price': 'From £99',
        'related_2': 'biomicroneedling.html',
        'related_2_title': 'Green Peel – BioMicroneedling',
        'related_2_desc': 'Combines microneedling with natural herbal Green Peel for superior skin renewal.',
        'related_2_price': 'From £89',
        'related_3': 'microneedling-biorepeel.html',
        'related_3_title': 'Skin Revive: Microneedling + BioRePeel',
        'related_3_desc': 'Dual-action treatment combining microneedling and BioRePeel for maximum rejuvenation.',
        'related_3_price': 'From £149',
    },
    {
        'subdir': '',
        'filename': 'biomicroneedling.html',
        'title': 'Green Peel – BioMicroneedling',
        'tagline': 'Microneedling with natural herbal treatment for superior renewal',
        'meta_description': 'Green Peel BioMicroneedling at Mili Skin & Beauty - Combines microneedling with natural herbal Green Peel for superior skin renewal. Book your BioMicroneedling treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Combines microneedling with natural herbal Green Peel for superior skin renewal.',
        'single_price': '£89',
        'single_value': '£89',
        '3pack_price': '£240',
        '3pack_value': '£240',
        '6pack_price': '£425',
        '6pack_value': '£425',
        'treatment_form_value': 'Green Peel – BioMicroneedling',
        'related_1': 'biorepeel.html',
        'related_1_title': 'Skin Radiance: BioRePeel',
        'related_1_desc': 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.',
        'related_1_price': 'From £99',
        'related_2': 'chemical-peel.html',
        'related_2_title': 'Skin Renewal: Chemical Peel',
        'related_2_desc': 'Professional chemical exfoliation for smoother, brighter, more youthful-looking skin.',
        'related_2_price': 'From £99',
        'related_3': 'rf-facial.html',
        'related_3_title': 'Skin LumaLift: Radio Frequency Facial',
        'related_3_desc': 'Advanced RF technology for skin tightening, lifting, and rejuvenation.',
        'related_3_price': 'From £129',
    },
    {
        'filename': 'chemical-peel.html',
        'title': 'Skin Renewal: Chemical Peel',
        'tagline': 'Professional chemical exfoliation for smoother, brighter skin',
        'meta_description': 'Skin Renewal Chemical Peel at Mili Skin & Beauty - Professional chemical exfoliation for smoother, brighter, more youthful-looking skin. Book your Chemical Peel treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Professional chemical exfoliation for smoother, brighter, more youthful-looking skin.',
        'single_price': '£99',
        'single_value': '£99',
        '3pack_price': '£279',
        '3pack_value': '£279',
        '6pack_price': '£519',
        '6pack_value': '£519',
        'treatment_form_value': 'Skin Renewal: Chemical Peel',
        'related_1': 'biorepeel.html',
        'related_1_title': 'Skin Radiance: BioRePeel',
        'related_1_desc': 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.',
        'related_1_price': 'From £99',
        'related_2': 'biomicroneedling.html',
        'related_2_title': 'Green Peel – BioMicroneedling',
        'related_2_desc': 'Combines microneedling with natural herbal Green Peel for superior skin renewal.',
        'related_2_price': 'From £89',
        'related_3': 'ultimate-exfoliation.html',
        'related_3_title': 'Skin Luxe Satin: Ultimate Exfoliation',
        'related_3_desc': 'Multi-method exfoliation combining chemical, physical, and enzymatic techniques for ultimate renewal.',
        'related_3_price': 'From £99',
    },
    {
        'filename': 'microneedling-biorepeel.html',
        'title': 'Skin Revive: Microneedling + BioRePeel',
        'tagline': 'Dual-action treatment for maximum skin rejuvenation',
        'meta_description': 'Skin Revive Microneedling + BioRePeel at Mili Skin & Beauty - Dual-action treatment combining microneedling and BioRePeel for maximum rejuvenation. Book your combo treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Dual-action treatment combining microneedling and BioRePeel for maximum rejuvenation.',
        'single_price': '£149',
        'single_value': '£149',
        '3pack_price': '£399',
        '3pack_value': '£399',
        '6pack_price': '£749',
        '6pack_value': '£749',
        'treatment_form_value': 'Skin Revive: Microneedling + BioRePeel',
        'related_1': 'biomicroneedling.html',
        'related_1_title': 'Green Peel – BioMicroneedling',
        'related_1_desc': 'Combines microneedling with natural herbal Green Peel for superior skin renewal.',
        'related_1_price': 'From £89',
        'related_2': 'biorepeel.html',
        'related_2_title': 'Skin Radiance: BioRePeel',
        'related_2_desc': 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.',
        'related_2_price': 'From £99',
        'related_3': 'rf-facial.html',
        'related_3_title': 'Skin LumaLift: Radio Frequency Facial',
        'related_3_desc': 'Advanced RF technology for skin tightening, lifting, and rejuvenation.',
        'related_3_price': 'From £129',
    },
    {
        'filename': 'rf-facial.html',
        'title': 'Skin LumaLift: Radio Frequency Facial',
        'tagline': 'Advanced RF technology for skin tightening and rejuvenation',
        'meta_description': 'Skin LumaLift Radio Frequency Facial at Mili Skin & Beauty - Advanced RF technology for skin tightening, lifting, and rejuvenation. Book your RF Facial treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Advanced RF technology for skin tightening, lifting, and rejuvenation.',
        'single_price': '£129',
        'single_value': '£129',
        '3pack_price': '£349',
        '3pack_value': '£349',
        '6pack_price': '£649',
        '6pack_value': '£649',
        'treatment_form_value': 'Skin LumaLift: Radio Frequency Facial',
        'related_1': 'microneedling-biorepeel.html',
        'related_1_title': 'Skin Revive: Microneedling + BioRePeel',
        'related_1_desc': 'Dual-action treatment combining microneedling and BioRePeel for maximum rejuvenation.',
        'related_1_price': 'From £149',
        'related_2': 'biomicroneedling.html',
        'related_2_title': 'Green Peel – BioMicroneedling',
        'related_2_desc': 'Combines microneedling with natural herbal Green Peel for superior skin renewal.',
        'related_2_price': 'From £89',
        'related_3': 'ultimate-exfoliation.html',
        'related_3_title': 'Skin Luxe Satin: Ultimate Exfoliation',
        'related_3_desc': 'Multi-method exfoliation combining chemical, physical, and enzymatic techniques for ultimate renewal.',
        'related_3_price': 'From £99',
    },
    {
        'filename': 'ultimate-exfoliation.html',
        'title': 'Skin Luxe Satin: Ultimate Exfoliation',
        'tagline': 'Multi-method exfoliation for ultimate skin renewal',
        'meta_description': 'Skin Luxe Satin Ultimate Exfoliation at Mili Skin & Beauty - Multi-method exfoliation combining chemical, physical, and enzymatic techniques for ultimate renewal. Book your Ultimate Exfoliation treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Multi-method exfoliation combining chemical, physical, and enzymatic techniques for ultimate renewal.',
        'single_price': '£99',
        'single_value': '£99',
        '3pack_price': '£279',
        '3pack_value': '£279',
        '6pack_price': '£519',
        '6pack_value': '£519',
        'treatment_form_value': 'Skin Luxe Satin: Ultimate Exfoliation',
        'related_1': 'chemical-peel.html',
        'related_1_title': 'Skin Renewal: Chemical Peel',
        'related_1_desc': 'Professional chemical exfoliation for smoother, brighter, more youthful-looking skin.',
        'related_1_price': 'From £99',
        'related_2': 'biorepeel.html',
        'related_2_title': 'Skin Radiance: BioRePeel',
        'related_2_desc': 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.',
        'related_2_price': 'From £99',
        'related_3': 'biomicroneedling.html',
        'related_3_title': 'Green Peel – BioMicroneedling',
        'related_3_desc': 'Combines microneedling with natural herbal Green Peel for superior skin renewal.',
        'related_3_price': 'From £89',
    },
    {
        'filename': 'blackhead-extraction.html',
        'title': 'Deep Blackhead Extraction',
        'tagline': 'Professional extraction for clear, blemish-free skin',
        'meta_description': 'Deep Blackhead Extraction at Mili Skin & Beauty - Professional extraction treatment for clear, blemish-free skin. Book your blackhead extraction treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Professional extraction treatment for clear, blemish-free skin.',
        'single_price': '£79',
        'single_value': '£79',
        '3pack_price': '£210',
        '3pack_value': '£210',
        '6pack_price': '£390',
        '6pack_value': '£390',
        'treatment_form_value': 'Deep Blackhead Extraction',
        'related_1': 'hydrofacial.html',
        'related_1_title': 'Skin Glow: Hydrofacial',
        'related_1_desc': 'Deep cleansing, hydration, and instant radiance with our professional Hydrofacial treatment.',
        'related_1_price': 'From £99',
        'related_2': 'oxygeno-facial.html',
        'related_2_title': 'Skin Oxyglow: OxygenO Facial',
        'related_2_desc': 'Oxygen infusion facial for instant glow and deep rejuvenation with premium serums.',
        'related_2_price': 'From £89',
        'related_3': 'bb-glow.html',
        'related_3_title': 'Skin Balance: BB Glow',
        'related_3_desc': 'Semi-permanent tinted coverage treatment for natural, radiant skin appearance.',
        'title': 'Skin Balance: BB Glow',
        'tagline': 'Semi-permanent tinted coverage for natural radiant skin',
        'meta_description': 'Skin Balance BB Glow at Mili Skin & Beauty - Semi-permanent tinted coverage treatment for natural, radiant skin appearance. Book your BB Glow treatment in 13b Edinburgh Cl, London E2 9NY.',
        'og_description': 'Semi-permanent tinted coverage treatment for natural, radiant skin appearance.',
        'single_price': '£125',
        'single_value': '£125',
        '3pack_price': '£349',
        '3pack_value': '£349',
        '6pack_price': '£649',
        '6pack_value': '£649',
        'treatment_form_value': 'Skin Balance: BB Glow',
        'related_1': 'blackhead-extraction.html',
        'related_1_title': 'Deep Blackhead Extraction',
        'related_1_desc': 'Professional extraction treatment for clear, blemish-free skin.',
        'related_1_price': 'From £79',
        'related_2': 'oxygeno-facial.html',
        'related_2_title': 'Skin Oxyglow: OxygenO Facial',
        'related_2_desc': 'Oxygen infusion facial for instant glow and deep rejuvenation with premium serums.',
        'related_2_price': 'From £89',
        'related_3': 'hydrofacial.html',
        'related_3_title': 'Skin Glow: Hydrofacial',
        'related_3_desc': 'Deep cleansing, hydration, and instant radiance with our professional Hydrofacial treatment.',
        'related_3_price': 'From £99',
    },
]

# Default HIFU content for layout reuse
default_hifu_about = [
    "HIFU (High-Intensity Focused Ultrasound) uses targeted energy to lift and tighten skin by stimulating deep collagen production without surgery.",
    "The treatment focuses energy at precise depths to trigger a natural healing response, improving firmness, contour, and overall definition.",
    "Results develop over weeks as new collagen forms, offering a lifted, rejuvenated look with minimal downtime and long-lasting benefits."
]

default_hifu_benefits = [
    {"icon": "fas fa-arrow-up", "title": "Non-Surgical Lift", "desc": "Noticeable lift and tightening without incisions."},
    {"icon": "fas fa-wave-square", "title": "Collagen Boost", "desc": "Stimulates deep collagen remodeling for firmness."},
    {"icon": "fas fa-face-smile", "title": "Contours & Definition", "desc": "Sculpts jawline, cheeks, and neck areas."},
    {"icon": "fas fa-clock", "title": "Minimal Downtime", "desc": "Return to daily life immediately after treatment."},
    {"icon": "fas fa-lines-leaning", "title": "Softens Lines", "desc": "Reduces appearance of fine lines and wrinkles."},
    {"icon": "fas fa-bolt", "title": "Long-Lasting", "desc": "Continued improvement for months as collagen matures."}
]

hifu_treatments = [
    {
        'filename': 'hifu-face.html',
        'subdir': 'treatments',
        'title': 'HIFU Face',
        'tagline': 'Non-invasive facial lifting and tightening',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Face',
        'meta_description': 'HIFU Face at Mili Skin & Beauty - Non-invasive lifting and tightening for a sculpted, youthful look.',
        'og_description': 'Non-invasive lifting and tightening for a sculpted, youthful look.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-neck.html',
        'subdir': 'treatments',
        'title': 'HIFU Neck',
        'tagline': 'Professional neck and jawline tightening',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Neck',
        'meta_description': 'HIFU Neck at Mili Skin & Beauty - Targeted tightening to smooth and define the neck and jawline.',
        'og_description': 'Targeted tightening to smooth and define the neck and jawline.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-face-neck.html',
        'subdir': 'treatments',
        'title': 'HIFU Face and Neck',
        'tagline': 'Complete facial and neck rejuvenation',
        'single_price': '£399',
        'single_value': '£399',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Face and Neck',
        'meta_description': 'HIFU Face and Neck at Mili Skin & Beauty - Comprehensive lift and contour for lower face and neck.',
        'og_description': 'Comprehensive lift and contour for lower face and neck.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-jawline.html',
        'subdir': 'treatments',
        'title': 'HIFU Jawline Definition',
        'tagline': 'Enhanced jawline definition and contour',
        'single_price': '£149',
        'single_value': '£149',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Jawline Definition',
        'meta_description': 'HIFU Jawline at Mili Skin & Beauty - Sculpted jawline with focused ultrasound tightening.',
        'og_description': 'Sculpted jawline with focused ultrasound tightening.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-butt-lift.html',
        'subdir': 'treatments',
        'title': 'HIFU Butt Lift',
        'tagline': 'Non-invasive buttock lifting and tightening',
        'single_price': '£299',
        'single_value': '£299',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Butt Lift',
        'meta_description': 'HIFU Butt Lift at Mili Skin & Beauty - Lift and firm buttocks without surgery.',
        'og_description': 'Lift and firm buttocks without surgery.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-breast-lift.html',
        'subdir': 'treatments',
        'title': 'HIFU Breast Lift',
        'tagline': 'Non-invasive breast lift and firmness',
        'single_price': '£299',
        'single_value': '£299',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Breast Lift',
        'meta_description': 'HIFU Breast Lift at Mili Skin & Beauty - Improve lift and firmness without downtime.',
        'og_description': 'Improve lift and firmness without downtime.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-stomach.html',
        'subdir': 'treatments',
        'title': 'HIFU Stomach Tightening',
        'tagline': 'Abdominal tightening and contouring',
        'single_price': '£299',
        'single_value': '£299',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Stomach Tightening',
        'meta_description': 'HIFU Stomach at Mili Skin & Beauty - Tighten and contour the abdomen with focused ultrasound.',
        'og_description': 'Tighten and contour the abdomen with focused ultrasound.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-love-handles.html',
        'subdir': 'treatments',
        'title': 'HIFU Love Handles',
        'tagline': 'Targeted love handles and side tightening',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Love Handles',
        'meta_description': 'HIFU Love Handles at Mili Skin & Beauty - Tighten and contour the waistline.',
        'og_description': 'Tighten and contour the waistline.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-inner-thighs.html',
        'subdir': 'treatments',
        'title': 'HIFU Inner Thighs',
        'tagline': 'Inner thigh tightening and lifting',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Inner Thighs',
        'meta_description': 'HIFU Inner Thighs at Mili Skin & Beauty - Smooth and firm inner thigh skin.',
        'og_description': 'Smooth and firm inner thigh skin.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-outer-thighs.html',
        'subdir': 'treatments',
        'title': 'HIFU Outer Thighs',
        'tagline': 'Outer thigh firming and definition',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Outer Thighs',
        'meta_description': 'HIFU Outer Thighs at Mili Skin & Beauty - Firm and smooth outer thigh skin.',
        'og_description': 'Firm and smooth outer thigh skin.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-banana-rolls.html',
        'subdir': 'treatments',
        'title': 'HIFU Banana Rolls',
        'tagline': 'Under-buttock tightening and lifting',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Banana Rolls',
        'meta_description': 'HIFU Banana Rolls at Mili Skin & Beauty - Lift and tighten under-buttock area.',
        'og_description': 'Lift and tighten under-buttock area.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-arms.html',
        'subdir': 'treatments',
        'title': 'HIFU Arms',
        'tagline': 'Arm tightening and definition',
        'single_price': '£199',
        'single_value': '£199',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'HIFU Arms',
        'meta_description': 'HIFU Arms at Mili Skin & Beauty - Firm and define upper arms.',
        'og_description': 'Firm and define upper arms.',
        'hero_image': '../images/hifu-hero.jpg',
    },
    {
        'filename': 'hifu-stomach-love-handles.html',
        'subdir': 'treatments',
        'title': 'Stomach + Love Handles Bundle',
        'tagline': 'Combined stomach and love handles treatment',
        'single_price': '£399',
        'single_value': '£399',
        '3pack_price': 'Package Quote',
        '3pack_value': 'Package Quote',
        '6pack_price': 'Package Quote',
        '6pack_value': 'Package Quote',
        'treatment_form_value': 'Stomach + Love Handles Bundle',
        'meta_description': 'HIFU Stomach + Love Handles at Mili Skin & Beauty - Comprehensive waist contouring with focused ultrasound.',
        'og_description': 'Comprehensive waist contouring with focused ultrasound.',
        'hero_image': '../images/hifu-hero.jpg',
    },
]

def adjust_paths_for_subdir(content: str, subdir: str) -> str:
    """Adjust asset and navigation paths when writing into a subdirectory."""
    if subdir != 'treatments':
        return content

    replacements = {
        'href="index.html': 'href="../index.html',
        'href="faq.html': 'href="../faq.html',
        'href="contact.php': 'href="../contact.php',
        'href="styles.css"': 'href="../styles.css"',
        'href="components.css"': 'href="../components.css"',
        'href="script.js"': 'href="../script.js"',
        'href="hydrofacial.html': 'href="../hydrofacial.html',
        'href="korean-facial.html': 'href="../korean-facial.html',
        'href="oxygeno-facial.html': 'href="../oxygeno-facial.html',
        'href="biorepeel.html': 'href="../biorepeel.html',
        'href="biomicroneedling.html': 'href="../biomicroneedling.html',
        'href="chemical-peel.html': 'href="../chemical-peel.html',
        'href="microneedling-biorepeel.html': 'href="../microneedling-biorepeel.html',
        'href="rf-facial.html': 'href="../rf-facial.html',
        'href="ultimate-exfoliation.html': 'href="../ultimate-exfoliation.html',
        'href="bb-glow.html': 'href="../bb-glow.html',
        'href="blackhead-extraction.html': 'href="../blackhead-extraction.html',
        'href="treatments/': 'href="../treatments/',
        'url(\'./images/': "url('../images/",
        'src="./images/': 'src="../images/',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)
    return content


def generate_files(treatments, template):
    """Generate all refactored facial treatment HTML files."""
    output_dir = os.path.dirname(__file__)
    success_count = 0
    error_count = 0
    
    for treatment in treatments:
        try:
            # Merge rich content
            content_data = rich_content.get(treatment['filename'], {})
            title = content_data.get('title', treatment['title'])
            tagline = content_data.get('tagline', treatment['tagline'])
            meta_description = treatment.get('meta_description') or content_data.get('meta_description')
            if not meta_description:
                desc = content_data.get('description', '')
                meta_description = f"{title} at Mili Skin & Beauty — {desc}" if desc else f"{title} at Mili Skin & Beauty"

            about_paragraphs = content_data.get('about_paragraphs', [])
            benefits = content_data.get('benefits', [])

            content = template

            # Provide fallback related links for pages without explicit related_* fields
            if 'related_1' not in treatment:
                treatment['related_1'] = 'hydrofacial.html'
                treatment['related_1_title'] = 'Skin Glow: Hydrofacial'
                treatment['related_1_desc'] = 'Deep cleansing, hydration, and instant radiance with our professional Hydrofacial treatment.'
                treatment['related_1_price'] = 'From £99'
            if 'related_2' not in treatment:
                treatment['related_2'] = 'korean-facial.html'
                treatment['related_2_title'] = 'Skin Glass: Korean Facial'
                treatment['related_2_desc'] = 'Multi-step Korean facial for luminous, glass-like skin with advanced serums and techniques.'
                treatment['related_2_price'] = 'From £99'
            if 'related_3' not in treatment:
                treatment['related_3'] = 'biorepeel.html'
                treatment['related_3_title'] = 'Skin Radiance: BioRePeel'
                treatment['related_3_desc'] = 'Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.'
                treatment['related_3_price'] = 'From £99'

            # Replace document title
            content = content.replace(
                '<title>Skin Glow: Hydrofacial Treatment - Mili Skin & Beauty</title>',
                f'<title>{title} - Mili Skin & Beauty</title>'
            )

            # Replace keywords to align with the treatment
            content = content.replace(
                '<meta name="keywords" content="hydrofacial, facial treatment, skin glow, deep cleansing, 13b Edinburgh Cl, London E2 9NY">',
                f'<meta name="keywords" content="{title}, facial treatment, skincare, Mili Skin & Beauty, London">'
            )

            # Replace meta description and og:title/og:description
            content = content.replace(
                '<meta name="description" content="Skin Glow Hydrofacial at Mili Skin & Beauty - Deep cleansing, hydration, and instant radiance. Book your Hydrofacial treatment in 13b Edinburgh Cl, London E2 9NY.">',
                f'<meta name="description" content="{meta_description}">'
            )
            content = content.replace(
                '<meta property="og:title" content="Skin Glow: Hydrofacial Treatment - Mili Skin & Beauty">',
                f'<meta property="og:title" content="{title} - Mili Skin & Beauty">'
            )
            content = content.replace(
                '<meta property="og:description" content="Deep cleansing, hydration, and instant radiance with our professional Hydrofacial treatment.">',
                f'<meta property="og:description" content="{meta_description}">'
            )

            # Replace hero headline and tagline (keep inline styles intact)
            content = content.replace(
                '>Skin Glow: Hydrofacial</h1>',
                f'>{title}</h1>'
            )
            content = content.replace(
                '>Deep cleansing, hydration, and instant radiance</p>',
                f'>{tagline}</p>'
            )

            # Replace hero image and og:image if provided (helps HIFU pages inherit correct artwork)
            hero_image = content_data.get('hero_image') or treatment.get('hero_image')
            if hero_image:
                content = content.replace(
                    "url('./images/SkinGlowydrofacial.webp')",
                    f"url('{hero_image}')"
                )

            og_image = hero_image or './images/hydrofacial-hero.jpg'
            if treatment.get('subdir') == 'treatments' and og_image.startswith('./'):
                og_image = og_image.replace('./', '../', 1)
            content = content.replace(
                '<meta property="og:image" content="./images/hydrofacial-hero.jpg">',
                f'<meta property="og:image" content="{og_image}">' 
            )

            # Update benefits header line for specificity
            content = content.replace(
                'Discover what makes Hydrofacial special',
                f'Discover what makes {title} special'
            )

            # Replace About paragraphs if richer content exists (HIFU falls back to defaults)
            if not about_paragraphs and treatment.get('subdir') == 'treatments':
                about_paragraphs = default_hifu_about

            if about_paragraphs:
                old_about = (
                    '<p>The Hydrofacial is an advanced, machine-assisted treatment that deeply cleanses, exfoliates, and hydrates the skin while infusing targeted serums for optimal results. Using innovative vortex technology and gentle suction, impurities are removed as the skin is nourished with antioxidants, peptides, and hyaluronic acid.</p>\n'
                    '                    <p>Suitable for all skin types, this treatment improves skin texture, reduces congestion, and restores hydration for a smoother, more radiant complexion. LED therapy is incorporated to calm redness, soften fine lines, and revitalise tired skin, leaving the face refreshed, plump, and glowing with no downtime.</p>'
                )
                new_about = '\n'.join([f'                    <p>{para}</p>' for para in about_paragraphs])
                content = content.replace(old_about, new_about)

            # Replace benefits grid with tailored items (HIFU falls back to defaults)
            if not benefits and treatment.get('subdir') == 'treatments':
                benefits = default_hifu_benefits

            if benefits:
                old_benefits = '''<div class="benefits-grid">
                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-droplet"></i></div>
                            <h4>Hydration & Plumping</h4>
                            <p>Deeply hydrates the skin, leaving it soft, smooth, and plumped.</p>
                        </div>
                        
                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-sun"></i></div>
                            <h4>Radiance & Even Tone</h4>
                            <p>Brightens dull skin and promotes a more even, glowing complexion.</p>
                        </div>
                        
                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-gem"></i></div>
                            <h4>Silken Texture & Refined Pores</h4>
                            <p>Clears congestion, refines pores, and smooths skin texture.</p>
                        </div>
                        
                        <div class="benefit-card">
                            <div class="icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                            <h4>Youthful Renewal</h4>
                            <p>Softens fine lines and improves firmness and elasticity.</p>
                        </div>

                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-lightbulb"></i></div>
                            <h4>LED-Enhanced Rejuvenation</h4>
                            <p>Stimulates collagen, calms inflammation, and supports clearer skin.</p>
                        </div>

                        <div class="benefit-card">
                            <div class="icon"><i class="fas fa-star"></i></div>
                            <h4>Instant Red-Carpet Glow</h4>
                            <p>Immediate visible results with minimal downtime.</p>
                        </div>
                    </div>'''

                benefit_cards = []
                for b in benefits:
                    icon = b.get('icon', 'fas fa-sparkles')
                    benefit_cards.append(
                        f'''                        <div class="benefit-card">
                            <div class="icon"><i class="{icon}"></i></div>
                            <h4>{b.get('title')}</h4>
                            <p>{b.get('desc')}</p>
                        </div>'''
                    )
                new_benefits = '<div class="benefits-grid">\n' + '\n'.join(benefit_cards) + '\n                    </div>'
                content = content.replace(old_benefits, new_benefits)
            
            # Normalize stray encoding so pound symbols match replacement strings
            content = content.replace('Â£', '£')

            # Replace pricing in single session
            content = content.replace(
                '<div class="pricing-price">£99</div>',
                f'<div class="pricing-price">{treatment["single_price"]}</div>',
                1  # Only first occurrence
            )
            
            # Replace pricing in 3-pack
            content = content.replace(
                '<div class="pricing-price">£249</div>',
                f'<div class="pricing-price">{treatment["3pack_price"]}</div>'
            )
            
            # Replace pricing in 6-pack
            content = content.replace(
                '<div class="pricing-price">£459</div>',
                f'<div class="pricing-price">{treatment["6pack_price"]}</div>'
            )
            
            # Replace form options
            content = content.replace(
                '<option value="Single Session">Single Session - £99</option>',
                f'<option value="Single Session">Single Session - {treatment["single_value"]}</option>'
            )
            content = content.replace(
                '<option value="3-Pack Course">3-Pack Course - £249</option>',
                f'<option value="3-Pack Course">3-Pack Course - {treatment["3pack_value"]}</option>'
            )
            content = content.replace(
                '<option value="6-Pack Course">6-Pack Course - £459</option>',
                f'<option value="6-Pack Course">6-Pack Course - {treatment["6pack_value"]}</option>'
            )
            
            # Replace hidden form treatment name
            content = content.replace(
                '<input type="hidden" name="treatment" value="Skin Glow: Hydrofacial">',
                f'<input type="hidden" name="treatment" value="{treatment["treatment_form_value"]}">'
            )
            
            # Replace related treatments links at bottom
            # First related card (Korean Facial / Chemical Peel / etc)
            old_related_1 = '''<div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin Glass: Korean Facial</h4>
                        <p class="related-card-desc">Multi-step Korean facial for luminous, glass-like skin with advanced serums and techniques.</p>
                        <div class="related-card-meta">
                            <span>60 mins</span>
                            <span class="related-card-price">From £99</span>
                        </div>
                        <a href="korean-facial.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>'''
            
            new_related_1 = f'''<div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">{treatment["related_1_title"]}</h4>
                        <p class="related-card-desc">{treatment["related_1_desc"]}</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">{treatment["related_1_price"]}</span>
                        </div>
                        <a href="{treatment["related_1"]}" class="related-card-cta">Learn More</a>
                    </div>
                </div>'''
            
            content = content.replace(old_related_1, new_related_1)
            
            # Second related card (BioRePeel)
            old_related_2 = '''<div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin Radiance: BioRePeel</h4>
                        <p class="related-card-desc">Advanced chemical peel for cell renewal and radiant, rejuvenated complexion.</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">From £99</span>
                        </div>
                        <a href="biorepeel.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>'''
            
            new_related_2 = f'''<div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">{treatment["related_2_title"]}</h4>
                        <p class="related-card-desc">{treatment["related_2_desc"]}</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">{treatment["related_2_price"]}</span>
                        </div>
                        <a href="{treatment["related_2"]}" class="related-card-cta">Learn More</a>
                    </div>
                </div>'''
            
            content = content.replace(old_related_2, new_related_2)
            
            # Third related card (OxygenO Facial)
            old_related_3 = '''<div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">Skin Oxyglow: OxygenO Facial</h4>
                        <p class="related-card-desc">Oxygen infusion facial for instant glow and deep rejuvenation with premium serums.</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">From £89</span>
                        </div>
                        <a href="oxygeno-facial.html" class="related-card-cta">Learn More</a>
                    </div>
                </div>'''
            
            new_related_3 = f'''<div class="related-card">
                    <div class="related-card-image">
                        <div class="gallery-placeholder"><i class="fas fa-image"></i></div>
                    </div>
                    <div class="related-card-content">
                        <h4 class="related-card-title">{treatment["related_3_title"]}</h4>
                        <p class="related-card-desc">{treatment["related_3_desc"]}</p>
                        <div class="related-card-meta">
                            <span>45 mins</span>
                            <span class="related-card-price">{treatment["related_3_price"]}</span>
                        </div>
                        <a href="{treatment["related_3"]}" class="related-card-cta">Learn More</a>
                    </div>
                </div>'''
            
            content = content.replace(old_related_3, new_related_3)
            
            # Also update the FAQ section header
            old_faq = '<p>Everything you need to know about Hydrofacial</p>'
            new_faq = f'<p>Everything you need to know about {treatment["title"]}</p>'
            content = content.replace(old_faq, new_faq)
            
            # Adjust paths for subdirectories
            content = adjust_paths_for_subdir(content, treatment.get('subdir', ''))

            # Write the file
            output_path = os.path.join(output_dir, treatment.get('subdir', ''), treatment['filename'])
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f'✓ {treatment["filename"]}')
            success_count += 1
            
        except Exception as e:
            print(f'✗ {treatment["filename"]}: {e}')
            error_count += 1
    
    # Summary
    print(f'\n{"="*50}')
    print(f'Summary: {success_count} files generated successfully')
    if error_count > 0:
        print(f'Errors: {error_count} file(s) failed')
    print(f'{"="*50}')

if __name__ == '__main__':
    all_treatments = treatments + hifu_treatments
    generate_files(all_treatments, template)
