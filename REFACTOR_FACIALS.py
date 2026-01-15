#!/usr/bin/env python3
"""
Batch refactor all 9 remaining facial treatment pages
Run from workspace root
"""

import os
from pathlib import Path

# Define all 9 facial pages with their customization data
facials = {
    'oxygeno-facial.html': {
        'title': 'Skin Oxyglow: OxygenO Facial',
        'tagline': 'Advanced oxygen infusion for instant radiance, deep hydration, and cellular renewal',
        'price_single': '£89',
        'price_3pack': '£240',
        'price_6pack': '£425',
        'duration': '45 minutes',
        'icon_benefits': ['fa-bolt', 'fa-water', 'fa-leaf', 'fa-sun', 'fa-check-circle', 'fa-clock'],
        'about_p1': 'The OxygenO Facial harnesses the power of advanced oxygen infusion technology to deliver transformative results. This revolutionary treatment infuses oxygen and active serums directly into the skin, promoting cellular renewal and vitality.',
        'about_p2': 'Oxygen naturally enhances blood circulation, boosts collagen production, and accelerates cellular regeneration. This makes it an excellent choice for those seeking immediate, visible radiance and long-term skin improvement.',
        'about_p3': 'Whether you\'re preparing for a special event or investing in your skin\'s long-term health, the OxygenO Facial offers unparalleled comfort and visible results that speak for themselves.',
        'benefit_titles': ['Instant Radiance', 'Deep Hydration', 'Cellular Renewal', 'Brightening Effect', 'Suitable for All', 'No Downtime'],
        'benefit_descs': [
            'Visible glow and brightness appear immediately after treatment, perfect for special events.',
            'Oxygen infusion deeply hydrates skin, improving texture and reducing fine lines.',
            'Boosts oxygen levels to promote collagen production and skin regeneration.',
            'Reduces dullness, dark spots, and uneven skin tone for a luminous complexion.',
            'Gentle enough for sensitive skin, effective for all skin types and conditions.',
            'Resume activities immediately. Perfect for busy lifestyles—no recovery needed.'
        ],
        'related': ['hydrofacial.html', 'biorepeel.html', 'korean-facial.html'],
    },
    
    'biorepeel.html': {
        'title': 'Skin Radiance: BioRePeel',
        'tagline': 'Advanced chemical peel for professional cell renewal, brightening, and dramatic skin transformation',
        'price_single': '£99',
        'price_3pack': '£279',
        'price_6pack': '£519',
        'duration': '45 minutes',
        'icon_benefits': ['fa-sparkles', 'fa-sun', 'fa-shield-alt', 'fa-dumbbell', 'fa-droplet', 'fa-clock'],
        'about_p1': 'BioRePeel is an advanced chemical peel that delivers professional-grade results without harsh downtime. Using a proprietary blend of natural acids and botanicals, this treatment gently exfoliates dead skin cells while stimulating collagen production.',
        'about_p2': 'The peel works on multiple skin layers to reveal fresher, brighter, more youthful-looking skin. It\'s specifically designed to address dullness, fine lines, acne scars, and uneven skin tone with precision and safety.',
        'about_p3': 'BioRePeel is suitable for all skin types and can be customized in strength to match your skin\'s needs. Results are visible from the first treatment, with ongoing improvements as collagen production increases.',
        'benefit_titles': ['Radiant Renewal', 'Brightening Boost', 'Collagen Stimulation', 'Scar Improvement', 'Hydration Boost', 'No Downtime'],
        'benefit_descs': [
            'Removes dull, damaged outer skin layers to reveal fresh, radiant complexion beneath.',
            'Increases skin brightness and luminosity while evening out skin tone and discoloration.',
            'Stimulates collagen and elastin production for improved texture and firmness over time.',
            'Reduces the appearance of acne scars and surface imperfections with regular treatments.',
            'BioRePeel hydrates while exfoliating, leaving skin soft, supple, and moisturized.',
            'Minimal to no downtime. Return to daily activities with glowing skin immediately.'
        ],
        'related': ['hydrofacial.html', 'chemical-peel.html', 'oxygeno-facial.html'],
    },
    
    'biomicroneedling.html': {
        'title': 'Green Peel – BioMicroneedling',
        'tagline': 'Herbal microneedling for natural collagen induction, renewal, and visible skin improvement',
        'price_single': '£89',
        'price_3pack': '£240',
        'price_6pack': '£425',
        'duration': '45 minutes',
        'icon_benefits': ['fa-leaf', 'fa-shield-alt', 'fa-arrow-up', 'fa-heart', 'fa-droplet', 'fa-bolt'],
        'about_p1': 'Green Peel BioMicroneedling combines the power of microneedling with herbal botanicals for natural, visible skin renewal. Using ultra-fine needles and organic serums, this treatment stimulates collagen production while maintaining skin health.',
        'about_p2': 'The herbal infusion during treatment harnesses the healing power of nature. This method is gentler than traditional microneedling but equally effective, making it ideal for those seeking results with minimal irritation.',
        'about_p3': 'Perfect for fine lines, texture issues, enlarged pores, and overall skin renewal. The natural approach means beautiful results without harsh chemicals or extensive recovery time.',
        'benefit_titles': ['Natural Collagen Boost', 'Herbal Infusion', 'Minimal Irritation', 'Improved Texture', 'Skin Renewal', 'Visible Results'],
        'benefit_descs': [
            'Stimulates your body\'s natural collagen production for improved skin texture and firmness.',
            'Herbal serums are infused during treatment for enhanced healing and nourishment.',
            'More gentle than traditional microneedling while still delivering powerful results.',
            'Reduces pore size, smooths fine lines, and improves overall skin texture.',
            'Supports natural skin renewal processes for healthy, youthful-looking complexion.',
            'See improvement after one session; best results develop over a 6-session course.'
        ],
        'related': ['chemical-peel.html', 'biorepeel.html', 'rf-facial.html'],
    },
    
    'chemical-peel.html': {
        'title': 'Skin Renewal: Chemical Peel',
        'tagline': 'Professional chemical exfoliation for deep skin transformation, brightness, and youthful renewal',
        'price_single': '£99',
        'price_3pack': '£279',
        'price_6pack': '£519',
        'duration': '45 minutes',
        'icon_benefits': ['fa-sparkles', 'fa-sun', 'fa-leaf', 'fa-shield-alt', 'fa-dumbbell', 'fa-clock'],
        'about_p1': 'Chemical peels are one of the most effective professional treatments for addressing multiple skin concerns simultaneously. Our peels use medical-grade formulas to exfoliate, renew, and transform your skin safely and effectively.',
        'about_p2': 'By removing damaged outer skin layers, chemical peels reveal the fresh, healthy skin beneath. They\'re highly customizable in strength, making them suitable for all skin types from sensitive to resilient.',
        'about_p3': 'Results are dramatic and long-lasting. A course of treatments addresses deep concerns like acne, hyperpigmentation, scarring, and aging. Single treatments provide immediate improvement; multiple treatments create transformation.',
        'benefit_titles': ['Deep Exfoliation', 'Brightness Boost', 'Anti-Aging Benefits', 'Acne Control', 'Even Tone', 'Professional Results'],
        'benefit_descs': [
            'Removes multiple skin layers to deeply exfoliate and reveal fresh, new skin.',
            'Increases radiance and luminosity while removing dark spots and dullness.',
            'Stimulates collagen production to reduce fine lines, wrinkles, and improve elasticity.',
            'Effective for acne-prone skin, reduces bacteria, oil, and breakout frequency.',
            'Reduces hyperpigmentation and discoloration for even, uniform skin tone.',
            'Professional-grade results that dramatically improve skin appearance and health.'
        ],
        'related': ['biorepeel.html', 'ultimate-exfoliation.html', 'hydrofacial.html'],
    },
    
    'microneedling-biorepeel.html': {
        'title': 'Skin Revive: Microneedling + BioRePeel',
        'tagline': 'Dual-action treatment combining microneedling and chemical peel for maximum results and transformation',
        'price_single': '£149',
        'price_3pack': '£399',
        'price_6pack': '£749',
        'duration': '60 minutes',
        'icon_benefits': ['fa-bolt', 'fa-arrow-up', 'fa-shield-alt', 'fa-droplet', 'fa-star', 'fa-heart'],
        'about_p1': 'This advanced combination treatment merges two powerful technologies: microneedling and BioRePeel. Together, they create a synergistic effect that delivers superior results compared to either treatment alone.',
        'about_p2': 'Microneedling creates channels for serum penetration while BioRePeel exfoliates and renews. The combination accelerates collagen production, improves texture, brightens tone, and addresses multiple skin concerns in one session.',
        'about_p3': 'This is our most transformative facial treatment, ideal for those serious about skin improvement. Results are visible immediately and improve dramatically over a 6-session course. Professional-level results without surgery.',
        'benefit_titles': ['Maximum Results', 'Dual Action', 'Accelerated Collagen', 'Dramatic Improvement', 'Multiple Benefits', 'Professional Grade'],
        'benefit_descs': [
            'Combines two powerful treatments for superior results than either alone.',
            'Microneedling + peeling work synergistically for accelerated skin transformation.',
            'Stimulates intense collagen production for improved texture, firmness, and elasticity.',
            'Addresses multiple concerns: wrinkles, scars, tone, texture, brightness in one treatment.',
            'Improves appearance of acne scars, hyperpigmentation, fine lines, and large pores.',
            'Professional medical-grade results with visible dramatic improvement after course.'
        ],
        'related': ['rf-facial.html', 'biomicroneedling.html', 'biorepeel.html'],
    },
    
    'rf-facial.html': {
        'title': 'Skin LumaLift: Radio Frequency Facial',
        'tagline': 'Advanced RF technology for lifting, tightening, and rejuvenation without surgery',
        'price_single': '£129',
        'price_3pack': '£349',
        'price_6pack': '£649',
        'duration': '60 minutes',
        'icon_benefits': ['fa-bolt', 'fa-arrow-up', 'fa-dumbbell', 'fa-sparkles', 'fa-shield-alt', 'fa-clock'],
        'about_p1': 'Radio Frequency (RF) facial technology delivers heat energy deep into skin layers, stimulating collagen production and tightening skin structure. This non-invasive treatment provides lifting and rejuvenation without surgery or downtime.',
        'about_p2': 'The RF energy heats dermal layers to create controlled thermal injury, triggering your body\'s natural healing response and collagen regeneration. Results include lifted, tighter, more youthful skin with improved elasticity.',
        'about_p3': 'Perfect for those seeking lifting and tightening benefits without invasive procedures. Results develop progressively over weeks as collagen remodels. Maintenance treatments every 3-6 months sustain your lifted appearance.',
        'benefit_titles': ['Skin Lifting', 'Tightening & Firming', 'Collagen Boost', 'No Surgery', 'Visible Lifting', 'Long-lasting'],
        'benefit_descs': [
            'RF energy lifts and tones sagging skin for a more youthful, defined appearance.',
            'Tightens and firms skin structure, improving texture and reducing loose, crepey skin.',
            'Stimulates deep collagen production for improved elasticity and skin thickness.',
            'Non-invasive alternative to surgery with no incisions, scars, or recovery time.',
            'Visible lifting appears immediately; progressive improvement over 2-3 months.',
            'Results last 6-12 months; maintenance treatments every 6 months sustain benefits.'
        ],
        'related': ['microneedling-biorepeel.html', 'ultimate-exfoliation.html', 'hydrofacial.html'],
    },
    
    'ultimate-exfoliation.html': {
        'title': 'Skin Luxe Satin: Ultimate Exfoliation',
        'tagline': 'Triple exfoliation for extraordinary smoothness, brightness, and skin perfection',
        'price_single': '£99',
        'price_3pack': '£279',
        'price_6pack': '£519',
        'duration': '45 minutes',
        'icon_benefits': ['fa-sparkles', 'fa-water', 'fa-sun', 'fa-shield-alt', 'fa-droplet', 'fa-heart'],
        'about_p1': 'Ultimate Exfoliation combines three complementary exfoliation methods for complete skin renewal. This multi-layered approach removes all dead skin while revealing the smoothest, most radiant skin possible.',
        'about_p2': 'The triple exfoliation includes mechanical, enzymatic, and chemical methods customized to your skin. This comprehensive approach addresses texture, tone, brightness, and overall skin health simultaneously.',
        'about_p3': 'The result is luminous, silky-smooth skin that looks professionally finished. This treatment is perfect for preparing for special events or beginning a serious skincare routine.',
        'benefit_titles': ['Supreme Smoothness', 'Triple Brightness', 'Satin Texture', 'Radiant Glow', 'All-in-One', 'Immediate Impact'],
        'benefit_descs': [
            'Triple exfoliation creates exceptionally smooth, luxurious skin texture.',
            'Addresses dullness, discoloration, and tone from multiple angles for maximum brightness.',
            'Leaves skin feeling silky and refined with luxurious, satin-like finish.',
            'Reveals radiant, glowing skin immediately after treatment.',
            'Complete exfoliation and renewal in one comprehensive treatment.',
            'Perfect for special events or starting a renewed skincare routine.'
        ],
        'related': ['chemical-peel.html', 'biorepeel.html', 'hydrofacial.html'],
    },
    
    'blackhead-extraction.html': {
        'title': 'Deep Blackhead Extraction',
        'tagline': 'Professional-grade pore cleansing and extraction for clear, refined skin',
        'price_single': '£79',
        'price_3pack': '£210',
        'price_6pack': '£390',
        'duration': '45 minutes',
        'icon_benefits': ['fa-shield-alt', 'fa-droplet', 'fa-sun', 'fa-check-circle', 'fa-sparkles', 'fa-clock'],
        'about_p1': 'Deep blackhead extraction is a specialized facial treatment that thoroughly cleans pores and removes blackheads, congestion, and buildup. Our trained professionals use professional-grade techniques to safely extract impurities without damaging skin.',
        'about_p2': 'This treatment is ideal for those with congested, oily, or acne-prone skin. We use hydration and calming serums alongside extraction to ensure your skin remains healthy and happy.',
        'about_p3': 'Results are immediately visible: clearer, refined pores and smooth texture. Regular maintenance treatments every 4 weeks keep pores clear and prevent buildup.',
        'benefit_titles': ['Clear Pores', 'Refined Texture', 'Congestion Relief', 'Acne Prevention', 'Brightening Effect', 'Professional Results'],
        'benefit_descs': [
            'Professional extraction removes blackheads and congestion safely and effectively.',
            'Refines pore appearance and improves overall skin texture.',
            'Relieves pore congestion, buildup, and surface impurities.',
            'Reduces acne formation by keeping pores clear and uncongested.',
            'Reveals brighter, clearer skin after removal of congestion.',
            'Professional techniques ensure safe, effective results without skin damage.'
        ],
        'related': ['hydrofacial.html', 'biorepeel.html', 'biomicroneedling.html'],
    },
    
    'bb-glow.html': {
        'title': 'Skin Balance: BB Glow',
        'tagline': 'Semi-permanent tinted skincare infusion for glowing, flawless-looking complexion',
        'price_single': '£125',
        'price_3pack': '£349',
        'price_6pack': '£649',
        'duration': '60 minutes',
        'icon_benefits': ['fa-sparkles', 'fa-heart', 'fa-droplet', 'fa-shield-alt', 'fa-sun', 'fa-clock'],
        'about_p1': 'BB Glow is a revolutionary semi-permanent tinted skincare treatment that combines beauty benefits with skincare benefits. A special tinted serum is infused into skin using microneedling, creating a natural, flawless-looking glow that lasts 2-3 weeks.',
        'about_p2': 'The treatment provides skincare benefits (hydration, brightening, nourishing) combined with light coverage that evens tone and adds luminosity. It\'s like a skincare treatment and light makeup combined into one innovative service.',
        'about_p3': 'Perfect for those seeking a subtle, natural glow without heavy makeup. The tint fades gradually over 2-3 weeks, and treatments can be repeated for continuous results. Semi-permanent, so no commitment required.',
        'benefit_titles': ['Natural Glow', 'Skincare + Beauty', 'Flawless Tone', 'Semi-Permanent', 'Skincare Benefits', 'No Downtime'],
        'benefit_descs': [
            'Creates natural, luminous glow that looks like healthy skin, not makeup.',
            'Combines skincare benefits (hydration, nourishment) with light coverage.',
            'Evens out skin tone and adds radiance for flawless-looking complexion.',
            'Fades gradually over 2-3 weeks; treatments can be repeated as desired.',
            'Infuses hydrating, brightening, nourishing serums as tint is applied.',
            'No downtime. Return to activities immediately with beautiful glowing skin.'
        ],
        'related': ['hydrofacial.html', 'korean-facial.html', 'oxygeno-facial.html'],
    },
}

print("✓ Refactoring data configured for 9 facial pages")
print("Ready to refactor:")
for filename in facials.keys():
    print(f"  - {filename}")
