"""
Generate Fractional RF + Microneedling Body, Stretch Mark Resurfacing, and Green Peel treatment pages.
Based on the body treatments documentation.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TREATMENT_DIR = os.path.join(BASE_DIR, 'treatments')

# Read template from HIFU butt lift
with open(os.path.join(TREATMENT_DIR, 'hifu-butt-lift.html'), 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()


def create_fractional_rf_body_page():
    """Create the Fractional RF + Microneedling Body page."""
    
    config = {
        'page_title': 'Fractional RF + Microneedling Body',
        'tagline': 'Advanced body tightening, lifting, and stretch mark reduction',
        'meta_description': 'Fractional RF + Microneedling Body at Mili Skin & Beauty - Advanced body sculpting and stretch mark treatment.',
        'meta_keywords': 'Fractional RF Body, Microneedling Body, stretch marks, body tightening, London',
        'about_content': '''<p>Take your body sculpting to the next level with our Fractional RF + Microneedling combination, designed to tighten, lift, and remodel skin while targeting stretch marks, sagging, and uneven texture.</p>
                    <p>This dual-action treatment combines <strong>Fractional Radio Frequency (RF)</strong> that penetrates deep into the dermis to stimulate collagen and elastin, tightening and firming the skin, with <strong>Microneedling</strong> that creates micro-channels to enhance serum absorption, remodel tissue, and improve texture.</p>
                    <p>Together, this combo maximises skin regeneration, improves elasticity, and smooths stretch marks, delivering visible lifting and contouring results on arms, thighs, stomach, back, and other areas.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Advanced Skin Tightening &amp; Firming', 'Lifts and tones sagging areas'),
            ('fa-chart-line', 'Stretch Mark Reduction', 'Improves texture, smooths scars, and restores elasticity'),
            ('fa-spa', 'Body Contouring &amp; Definition', 'Enhances natural curves and smooths uneven areas'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Encourages long-term tissue regeneration'),
            ('fa-sparkles', 'Texture Refinement', 'Smooths rough, crepey, or dimpled skin'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Dramatic results without invasive procedures')
        ],
        'steps': [
            ('fa-spa', 'Skin Prep &amp; Activation', 'The treatment area is cleansed and prepped for optimal penetration of RF and microneedling energy.'),
            ('fa-location-crosshairs', 'Precision Mapping', 'Sagging, texture concerns, and stretch marks are assessed to customise treatment zones.'),
            ('fa-bolt', 'Fractional RF + Microneedling Delivery', 'Microneedles create micro-channels while RF energy penetrates deeper layers, stimulating collagen, firming tissue, and smoothing skin simultaneously.'),
            ('fa-arrow-up', 'Targeted Body Contouring &amp; Lifting', 'Energy is focused on enhancing definition, lifting sagging areas, and smoothing texture.'),
            ('fa-droplet', 'Active Serum Infusion', 'Hydrating and healing serums are applied to boost results, support tissue repair, and enhance elasticity.'),
            ('fa-shield-heart', 'Barrier Protection &amp; Finish', 'A protective layer and SPF are applied to lock in results, support recovery, and maintain skin health.')
        ],
        'pricing_table': [
            ('Arms', '£175', 'N/A', 'N/A'),
            ('Back', '£175', 'N/A', 'N/A'),
            ('Thighs', '£175', 'N/A', 'N/A'),
            ('Stomach', '£175', 'N/A', 'N/A'),
            ('Other Areas', '£175', 'N/A', 'N/A'),
            ('Stretch Marks', '£175', 'N/A', 'N/A')
        ],
        'frequency': [
            ('Initial Course', '3–6 sessions spaced 4–6 weeks apart.'),
            ('Maintenance', 'Every 4–6 months to maintain firmness, smoothness, and skin quality.')
        ],
        'form_options': [
            'Arms - £175',
            'Back - £175',
            'Thighs - £175',
            'Stomach - £175',
            'Other Areas - £175',
            'Stretch Marks - £175'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild discomfort may occur; numbing cream is available to enhance comfort.'),
            ('How long does the treatment take?', 'Plan for 45–60 minutes depending on the treatment area.'),
            ('When will I see results?', 'You may notice improved texture immediately; full results develop over 4–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime with possible mild redness for 24–48 hours. Normal activities can resume quickly.'),
            ('How long do the results last?', 'Results improve over time; maintenance every 4–6 months recommended.')
        ],
        'addons': '''<h4>Optional Take-Home Add-Ons</h4>
                    <p>Enhance and prolong your results with professional-grade serums for home use:</p>
                    <ul style="list-style: none; padding-left: 0; margin-top: 15px;">
                        <li style="padding: 8px 0; border-bottom: 1px solid rgba(214, 173, 96, 0.2);"><strong>Skin Healing Lotion – £12</strong><br>Soothes sensitivity, supports repair, and reduces post-treatment redness.</li>
                        <li style="padding: 8px 0; border-bottom: 1px solid rgba(214, 173, 96, 0.2);"><strong>DDS Skin Healing Serum – £10</strong><br>Accelerates healing, strengthens skin, and enhances treatment results.</li>
                        <li style="padding: 8px 0;"><strong>HA (Hyaluronic Acid) Serum – £6</strong><br>Boosts hydration, plumps the skin, and maintains a smooth, radiant finish.</li>
                    </ul>'''
    }
    
    return generate_page(config, 'fractional-rf-microneedling-body.html')


def create_stretch_mark_page():
    """Create the Stretch Mark Resurfacing page."""
    
    config = {
        'page_title': 'Stretch Mark Resurfacing',
        'tagline': 'Advanced stretch mark correction and skin repair',
        'meta_description': 'Stretch Mark Resurfacing at Mili Skin & Beauty - Reduce stretch marks with Fractional RF + Microneedling.',
        'meta_keywords': 'Stretch Mark Resurfacing, stretch mark treatment, skin resurfacing, London',
        'about_content': '''<p>Stretch Mark Resurfacing with Fractional RF + Microneedling is an advanced corrective treatment designed to visibly improve the appearance of stretch marks by repairing weakened skin structure, tightening tissue, and smoothing texture.</p>
                    <p>This powerful dual-technology approach combines precision microneedling with fractional radiofrequency energy to target stretch marks at multiple skin depths. Microneedling creates controlled micro-channels that stimulate natural collagen and elastin production while preparing the skin for deeper repair. Fractional RF then delivers heat into the dermis to remodel damaged fibres, strengthen skin density, and tighten stretched tissue.</p>
                    <p>Together, they correct texture irregularities, soften visible lines, and help stretch marks blend seamlessly with surrounding skin. Suitable for stomach, hips, thighs, buttocks, breasts, arms, and lower back, and effective on both newer red stretch marks and older white or textured marks.</p>''',
        'benefits': [
            ('fa-chart-line', 'Stretch Mark Reduction', 'Visibly improves appearance and texture of stretch marks'),
            ('fa-link', 'Skin Structure Repair', 'Repairs weakened skin fibres and strengthens density'),
            ('fa-arrow-up', 'Tissue Tightening', 'Tightens stretched skin for improved firmness'),
            ('fa-heart-pulse', 'Collagen Remodeling', 'Stimulates natural collagen and elastin production'),
            ('fa-sparkles', 'Texture Smoothing', 'Softens visible lines and evens out skin texture'),
            ('fa-shield-heart', 'Non-Surgical &amp; Effective', 'Advanced correction without invasive procedures')
        ],
        'steps': [
            ('fa-search', 'Skin Assessment &amp; Treatment Planning', 'Stretch marks are assessed for depth, texture, and skin laxity to customise treatment intensity.'),
            ('fa-spa', 'Skin Preparation', 'The area is cleansed and prepped to optimise microneedling penetration and RF energy delivery.'),
            ('fa-syringe', 'Microneedling Skin Correction', 'Precision microneedling creates micro-channels to stimulate collagen, improve skin texture, and initiate repair.'),
            ('fa-bolt', 'Fractional RF Remodeling', 'Fractional RF energy is delivered through the skin to heat deeper layers, tightening tissue and rebuilding weakened skin fibres.'),
            ('fa-shield-heart', 'Soothing Recovery &amp; Barrier Support', 'Calming, restorative products are applied to reduce sensitivity and support healing.')
        ],
        'pricing_table': [
            ('Stretch Mark Resurfacing', '£175', 'N/A', 'N/A')
        ],
        'frequency': [
            ('Initial Course', '3–6 sessions spaced 4–6 weeks apart for optimal correction.'),
            ('Maintenance', 'Every 4–6 months to maintain texture improvement and skin quality.')
        ],
        'form_options': [
            'Stretch Mark Resurfacing - £175'
        ],
        'faqs': [
            ('Does it work on old stretch marks?', 'Yes, effective on both new and old stretch marks of various colors and textures.'),
            ('Is the treatment painful?', 'Mild discomfort may occur; numbing cream is available for sensitive areas.'),
            ('How long does each session take?', 'Plan for 45–60 minutes depending on the treatment area size.'),
            ('When will I see results?', 'Initial improvements in texture within 2–4 weeks; full results develop over 3–6 months.'),
            ('How many sessions do I need?', '3–6 sessions recommended for optimal stretch mark correction.')
        ],
        'addons': ''
    }
    
    return generate_page(config, 'stretch-mark-resurfacing.html')


def create_green_peel_page():
    """Create the Green Peel Bio Microneedling page."""
    
    config = {
        'page_title': 'Green Peel – Bio Microneedling',
        'tagline': 'Natural herbal skin resurfacing and regeneration',
        'meta_description': 'Green Peel Bio Microneedling at Mili Skin & Beauty - Natural herbal skin resurfacing for face, neck, and body.',
        'meta_keywords': 'Green Peel, Bio Microneedling, herbal peel, skin regeneration, London',
        'about_content': '''<p>The Green Peel is a natural, herbal-based skin resurfacing treatment that stimulates the skin's regeneration using plant-derived ingredients instead of chemical acids. Suitable for face, neck, décolleté, and body areas, it boosts circulation, accelerates cell turnover, and strengthens the skin from within.</p>
                    <p>A specialised herbal blend is massaged into the skin, acting as a natural micro-exfoliator to target acne, pigmentation, sun damage, uneven texture, and enlarged pores. Depending on the strength chosen, mild to visible peeling may occur over the following days, revealing smoother, brighter, and more refined skin.</p>
                    <p>A soothing mask and healing serum are applied during the session, with take-home serum to maintain hydration and support optimal skin regeneration throughout the peeling and renewal phase.</p>''',
        'benefits': [
            ('fa-leaf', 'Skin Renewal &amp; Regeneration', 'Stimulates cell turnover to reveal fresher, smoother, and healthier-looking skin'),
            ('fa-sparkles', 'Improved Texture &amp; Tone', 'Reduces roughness, uneven texture, and dullness'),
            ('fa-shield', 'Acne &amp; Blemish Support', 'Helps minimise breakouts, unclog pores, and reduce inflammation'),
            ('fa-sun', 'Pigmentation Reduction', 'Supports fading of sun damage, age spots, and uneven pigmentation'),
            ('fa-heart-pulse', 'Natural &amp; Herbal-Based', 'Uses botanical ingredients instead of harsh chemical acids'),
            ('fa-sliders', 'Customisable Strength', 'Can be tailored to your skin type and desired results')
        ],
        'steps': [
            ('fa-comments', 'Consultation &amp; Skin Assessment', 'Personalized evaluation to choose the right Green Peel strength for face, neck, décolleté, or body.'),
            ('fa-spa', 'Cleansing &amp; Prep', 'Gentle cleanse to remove impurities and prep the skin for maximum absorption.'),
            ('fa-hand-sparkles', 'Herbal Blend Application', 'Massage the herbal mixture into the skin, activating circulation and natural exfoliation.'),
            ('fa-clock', 'Absorption &amp; Activation', 'Allow the herbs to stimulate cellular renewal and boost circulation.'),
            ('fa-mask', 'Removal &amp; Soothing Mask', 'Herbs are removed, and a calming mask is applied to hydrate and reduce sensitivity.'),
            ('fa-droplet', 'Skin Healing Serum &amp; Take-Home Care', 'Apply a healing serum in-clinic and provide take-home serum to maintain hydration and support regeneration.'),
            ('fa-recycle', 'Peeling &amp; Renewal', 'Over the next few days, mild to visible peeling reveals smoother, brighter, and rejuvenated skin.')
        ],
        'pricing_table': [
            ('Green Peel – Face', '£99', '£267 (3 sessions)', '£336 (4 sessions)'),
            ('Green Peel – Face &amp; Neck', '£149', '£401 (3 sessions)', '£506 (4 sessions)'),
            ('Green Peel – Body Area', '£125', '£337.50 (3 sessions)', '£425 (4 sessions)')
        ],
        'frequency': [
            ('Initial Course', '3–6 sessions, spaced 3–4 weeks apart.'),
            ('Maintenance', 'Every 3–6 months, depending on skin concerns and results desired.')
        ],
        'form_options': [
            'Green Peel Face - £99',
            'Green Peel Face & Neck - £149',
            'Green Peel Body Area - £125'
        ],
        'faqs': [
            ('Is Green Peel suitable for sensitive skin?', 'Yes, the strength can be customized for sensitive skin types.'),
            ('Will my skin peel visibly?', 'Depending on the strength chosen, you may experience mild to moderate peeling over 3–5 days.'),
            ('Can I use it on my body?', 'Yes, Green Peel is effective on face, neck, décolleté, and body areas.'),
            ('How long does the treatment take?', 'Plan for 45–60 minutes including consultation and aftercare.'),
            ('What should I avoid after treatment?', 'Avoid direct sun exposure, harsh products, and picking at peeling skin. Use SPF and gentle moisturizers.')
        ],
        'addons': '''<h4>Recommended Post-Treatment Products</h4>
                    <ul style="list-style: none; padding-left: 0; margin-top: 15px;">
                        <li style="padding: 8px 0; border-bottom: 1px solid rgba(214, 173, 96, 0.2);"><strong>Skin Healing Lotion – £12</strong><br>Soothes sensitivity and supports skin repair.</li>
                        <li style="padding: 8px 0;"><strong>DDS Skin Healing Serum – £10</strong><br>Accelerates healing, strengthens skin barrier, and enhances results.</li>
                    </ul>'''
    }
    
    return generate_page(config, 'green-peel-bio-microneedling.html')


def generate_page(config, filename):
    """Generate a treatment page from config."""
    
    html = TEMPLATE
    
    # Replace page-specific content
    html = html.replace('HIFU Butt &amp; Breast Treatments', config['page_title'])
    html = html.replace('HIFU Butt & Breast Treatments', config['page_title'])
    html = html.replace('Lift, sculpt, and firm the buttocks', config['tagline'])
    
    # Replace meta tags
    html = html.replace(
        'HIFU Butt & Breast Treatments at Mili Skin & Beauty - Lift and firm buttocks and breasts without surgery.',
        config['meta_description']
    )
    html = html.replace(
        'HIFU Butt & Breast Treatments, body treatment, skincare, Mili Skin & Beauty, London',
        config['meta_keywords']
    )
    
    # Replace About section
    old_about = '''<p>Achieve a lifted, sculpted, and firm silhouette with our HIFU Butt & Breast treatments, designed
to tighten, contour, and enhance volume. Using the latest combination of four advanced
technologies — HIFU, MPT, MFU, and EMS — in one treatment, these sessions deliver one of
the best non-surgical lifting and firming results available.</p>
                    <p>These treatments stimulate collagen, remodel tissue, and restore firmness, creating a more lifted,
toned, and youthful appearance for both the buttocks and breasts. Ideal for clients seeking natural
contouring, anti-sagging, and enhanced shape without surgery.</p>'''
    html = html.replace(old_about, config['about_content'])
    
    # Generate and replace benefits
    benefits_html = ''
    for icon, title, desc in config['benefits']:
        benefits_html += f'''<div class="benefit-card">
                            <div class="icon"><i class="fas {icon}"></i></div>
                            <h4>{title}</h4>
                            <p>{desc}</p>
                        </div>
                        '''
    
    # Find and replace benefits section
    benefits_start = html.find('<div class="benefits-grid">')
    if benefits_start != -1:
        benefits_start += len('<div class="benefits-grid">')
        depth = 1
        i = benefits_start
        while depth > 0 and i < len(html):
            if html[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    benefits_end = i
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html = html[:benefits_start] + '\n                        ' + benefits_html + '\n                    ' + html[benefits_end:]
    
    # Generate and replace steps
    steps_html = ''
    for idx, (icon, title, desc) in enumerate(config['steps'], 1):
        steps_html += f'''<div class="experience-card">
                    <div class="step-number">{idx}</div>
                    <div class="step-icon">
                        <i class="fas {icon}"></i>
                    </div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>

                '''
    
    # Replace step count description
    step_count = len(config['steps'])
    html = html.replace('A 6-step lifting and contouring journey', f'A {step_count}-step treatment journey')
    
    # Find and replace steps section
    steps_start = html.find('<div class="experience-grid">')
    if steps_start != -1:
        steps_start += len('<div class="experience-grid">')
        depth = 1
        i = steps_start
        while depth > 0 and i < len(html):
            if html[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    steps_end = i
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html = html[:steps_start] + '\n                ' + steps_html + '            ' + html[steps_end:]
    
    # Generate and replace pricing table
    rows = ''
    for pricing_row in config['pricing_table']:
        if len(pricing_row) == 4:
            area, price1, price2, price4 = pricing_row
            rows += f'''<tr style="border-bottom: 1px solid rgba(214, 173, 96, 0.2);">
                                    <td style="padding: 12px; font-weight: 600; color: #1a1a1a;">{area}</td>
                                    <td style="padding: 12px; text-align: center; color: #555;">{price1}</td>
                                    <td style="padding: 12px; text-align: center; color: #555;">{price2}</td>
                                    <td style="padding: 12px; text-align: center; color: #555;">{price4}</td>
                                </tr>
                                '''
    
    pricing_html = f'''<h3>Treatment Areas &amp; Pricing</h3>
                    <div style="overflow-x: auto; margin-bottom: 20px;">
                        <table style="width: 100%; border-collapse: collapse; background: linear-gradient(135deg, #fffdf8 0%, #fffaf2 100%); border: 1px solid rgba(214, 173, 96, 0.3); border-radius: 8px; overflow: hidden;">
                            <thead>
                                <tr style="background: linear-gradient(135deg, #d6ad60, #e5bf77); color: #fff;">
                                    <th style="padding: 12px; text-align: left; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">Area</th>
                                    <th style="padding: 12px; text-align: center; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">Price</th>
                                    <th style="padding: 12px; text-align: center; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">3 Sessions</th>
                                    <th style="padding: 12px; text-align: center; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">4+ Sessions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {rows}
                            </tbody>
                        </table>
                    </div>
                    {config.get('addons', '')}'''
    
    # Find and replace pricing section
    pricing_start = html.find('<h3>Choose Your Area</h3>')
    if pricing_start != -1:
        pricing_end = html.find('</div>', html.find('</table>', pricing_start))
        if pricing_end != -1:
            pricing_end += len('</div>')
            html = html[:pricing_start] + pricing_html + html[pricing_end:]
    
    # Generate and replace frequency
    freq_rows = ''
    for label, copy in config['frequency']:
        freq_rows += f'''<div class="frequency-row">
                                <div class="frequency-bullet"></div>
                                <div>
                                    <p class="frequency-label">{label}</p>
                                    <p class="frequency-copy">{copy}</p>
                                </div>
                            </div>
                            '''
    
    freq_html = f'''<div class="frequency-card">
                        <div class="frequency-header">
                            <div class="frequency-icon"><i class="fas fa-clock"></i></div>
                            <div>
                                <p class="frequency-title">Recommended Frequency</p>
                                <p class="frequency-sub">Optimize your results with proper scheduling.</p>
                            </div>
                        </div>
                        <div class="frequency-rows">
                            {freq_rows}
                        </div>
                    </div>'''
    
    # Find and replace frequency card
    freq_start = html.find('<div class="frequency-card">')
    if freq_start != -1:
        depth = 1
        i = freq_start + len('<div class="frequency-card">')
        while depth > 0 and i < len(html):
            if html[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    freq_end = i + 6
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html = html[:freq_start] + freq_html + html[freq_end:]
    
    # Generate and replace form options
    options_html = '<option value="">Select option</option>\n'
    for option in config['form_options']:
        options_html += f'                                <option value="{option}">{option}</option>\n'
    
    form_html = f'''<div class="form-group">
                            <label for="interested">Interested in *</label>
                            <select id="interested" name="interested" required>
                                {options_html}                            </select>
                        </div>'''
    
    # Find and replace form options
    form_start = html.find('<div class="form-group">\n                            <label for="interested">Interested in *</label>')
    if form_start != -1:
        form_end = html.find('</div>', form_start) + len('</div>')
        html = html[:form_start] + form_html + html[form_end:]
    
    # Generate and replace FAQs
    faqs_html = ''
    for question, answer in config['faqs']:
        faqs_html += f'''<div class="accordion-item">
                    <div class="accordion-header">
                        <h4>{question}</h4>
                        <i class="fas fa-chevron-down accordion-icon"></i>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-body">
                            <p>{answer}</p>
                        </div>
                    </div>
                </div>

                '''
    
    # Find and replace FAQs
    faqs_start = html.find('<div class="accordion faqs-accordion">')
    if faqs_start != -1:
        faqs_start += len('<div class="accordion faqs-accordion">')
        depth = 1
        i = faqs_start
        while depth > 0 and i < len(html):
            if html[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    faqs_end = i
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html = html[:faqs_start] + '\n                ' + faqs_html + '            ' + html[faqs_end:]
    
    # Write the file
    file_path = os.path.join(TREATMENT_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Created: {filename}")
    return True


# Main execution
print("Creating RF and Peel treatment pages...")
print("="*60)

create_fractional_rf_body_page()
create_stretch_mark_page()
create_green_peel_page()

print("="*60)
print("All RF and Peel treatment pages have been created successfully!")
