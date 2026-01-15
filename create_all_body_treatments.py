"""
Generate ALL body treatment pages based on the body treatments documentation.
Creates comprehensive treatment pages for each body treatment mentioned in the doc.
"""

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TREATMENT_DIR = os.path.join(BASE_DIR, 'treatments')

# Ensure treatments directory exists
os.makedirs(TREATMENT_DIR, exist_ok=True)


def generate_treatment_config():
    """Return all treatment configurations based on the documentation."""
    
    configs = {}
    
    # 1. HIFU Breast Lift
    configs['hifu-breast-lift.html'] = {
        'page_title': 'HIFU Breast Lift',
        'tagline': 'Lift, sculpt, and firm the breast area',
        'meta_description': 'HIFU Breast Lift at Mili Skin & Beauty - Lift and firm breasts without surgery using advanced HIFU technology.',
        'meta_keywords': 'HIFU Breast Lift, body treatment, breast lift, London',
        'about_content': '''<p>Achieve a lifted, sculpted, and firm silhouette with our HIFU Breast Lift treatment, designed to tighten, contour, and enhance volume. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, these sessions deliver one of the best non-surgical lifting and firming results available.</p>
                    <p>This treatment stimulates collagen, remodels tissue, and restores firmness, creating a more lifted, toned, and youthful appearance for the breasts. Ideal for clients seeking natural contouring, anti-sagging, and enhanced shape without surgery.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Lifted &amp; Sculpted Breasts', 'Enhances shape, contour, and firmness'),
            ('fa-link', 'Anti-Sagging &amp; Firming', 'Tightens loose skin for a more youthful profile'),
            ('fa-heart-pulse', 'Collagen Stimulation', 'Boosts natural collagen and elastin for long-term firmness'),
            ('fa-circle-plus', 'Volume Restoration', 'Rejuvenates curves without surgery'),
            ('fa-droplet', 'Smoothness &amp; Radiance', 'Hydrates and nourishes skin for soft, glowing results'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Achieve dramatic lift and contour without invasive procedures')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'The treatment area is cleansed to remove impurities and prepare the skin for optimal results.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'The breast area is assessed and marked for targeted energy delivery, ensuring even lifting and contouring.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS', '<strong>HIFU:</strong> Lifts and remodels deep tissue layers. <strong>MPT:</strong> Firms surface skin. <strong>MFU:</strong> Stimulates collagen. <strong>EMS:</strong> Tones muscles for lifted, firm appearance.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy is applied strategically to enhance shape, volume, and firmness, creating naturally lifted and sculpted curves.'),
            ('fa-droplet', 'Hydrating Serum Infusion &amp; Massage', 'High-performance serums hydrate and plump while a gentle massage improves circulation and promotes relaxation.'),
            ('fa-shield-heart', 'Post-Treatment Protection &amp; Radiance', 'Recovery serums protect the skin and maintain lift, leaving the treated area smooth, firm, and visibly lifted.')
        ],
        'pricing_table': [
            ('Breast', '£299', '£538', '£957')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for maximum lift and collagen remodeling.'),
            ('Maintenance', 'Every 4–6 months to preserve firmness, contour, and shape.')
        ],
        'form_options': [
            'Breast - £299'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 45–60 minutes including consultation, mapping, treatment, and aftercare.'),
            ('When will I see results?', 'You may feel an immediate lift; contour and firmness build over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine; avoid intense heat or vigorous exercise for 24 hours.'),
            ('How long do the results last?', 'With 2–3 sessions spaced 6–8 weeks apart, results last months; maintain every 4–6 months.')
        ]
    }
    
    # 2. HIFU Arms (Bingo Wings)
    configs['hifu-arms.html'] = {
        'page_title': 'HIFU Arms – Bingo Wings Reduction',
        'tagline': 'Tone, lift, and reduce bingo wings',
        'meta_description': 'HIFU Arms treatment at Mili Skin & Beauty - Reduce bingo wings and tone upper arms with advanced HIFU technology.',
        'meta_keywords': 'HIFU Arms, Bingo Wings Reduction, arm toning, London',
        'about_content': '''<p>Say goodbye to sagging upper arms and bingo wings with our HIFU Arms treatment, designed to tighten, lift, and sculpt the arms. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this procedure delivers one of the best non-surgical arm lifting and toning results available.</p>
                    <p>This treatment stimulates collagen, firms tissue, and tones muscles, leaving arms sleeker, lifted, and sculpted. Perfect for clients looking to reduce bingo wings, improve arm definition, and smooth loose skin without surgery.</p>''',
        'benefits': [
            ('fa-arrow-down', 'Bingo Wing Reduction', 'Targets sagging skin under the arms for smoother, tighter contours'),
            ('fa-dumbbell', 'Arm Lift &amp; Tone', 'Firms and lifts the upper arms'),
            ('fa-chart-line', 'Arm Contouring &amp; Definition', 'Improves shape and creates sleeker lines'),
            ('fa-link', 'Anti-Sagging', 'Smooths loose tissue for a youthful appearance'),
            ('fa-heart-pulse', 'Collagen Stimulation', 'Boosts natural collagen and elastin for long-term firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Dramatic lift and contour without invasive procedures')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the arm area to remove impurities and prep skin for maximum treatment effectiveness.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Upper arms are assessed and treatment zones mapped to target sagging tissue and bingo wings.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS Energy Delivery', '<strong>HIFU:</strong> Lifts and remodels deep tissue. <strong>MPT:</strong> Firms surface skin. <strong>MFU:</strong> Stimulates collagen. <strong>EMS:</strong> Tones underlying arm muscles.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy is applied strategically to enhance upper arm definition and firmness, creating sleek, youthful contours.'),
            ('fa-droplet', 'Hydrating Serum Infusion &amp; Massage', 'High-performance serums are infused to hydrate, plump, and restore elasticity.'),
            ('fa-shield-heart', 'Post-Treatment Protection &amp; Radiance', 'Recovery serums maintain firmness and smoothness, leaving arms lifted, toned, and visibly sculpted.')
        ],
        'pricing_table': [
            ('Arms (Bingo Wings Reduction)', '£199', '£358', '£637')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal lift and collagen remodeling.'),
            ('Maintenance', 'Every 4–6 months to preserve arm firmness and contour.')
        ],
        'form_options': [
            'Arms (Bingo Wings) - £199'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 30–45 minutes including consultation, mapping, treatment, and aftercare.'),
            ('When will I see results?', 'You may feel an immediate lift; tone and firmness build over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine; avoid intense heat or vigorous exercise for 24 hours.'),
            ('How long do the results last?', 'With 2–3 sessions spaced 6–8 weeks apart, results last months; maintain every 4–6 months.')
        ]
    }
    
    # 3. HIFU Stomach
    configs['hifu-stomach.html'] = {
        'page_title': 'HIFU Stomach Tightening',
        'tagline': 'Tighten, firm, and contour your midsection',
        'meta_description': 'HIFU Stomach treatment at Mili Skin & Beauty - Tighten and firm abdominal skin with advanced HIFU technology.',
        'meta_keywords': 'HIFU Stomach, abdomen tightening, body contouring, London',
        'about_content': '''<p>Achieve a firmer, sculpted, and toned midsection with our HIFU Stomach treatment. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this session delivers one of the best non-surgical body contouring results available.</p>
                    <p>This treatment tightens loose abdominal skin, reduces stubborn fat, and remodels tissue, leaving the stomach smoother, firmer, and more sculpted. Ideal for clients seeking abdominal contouring and skin tightening without surgery.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Abdominal Lift &amp; Tightening', 'Firms loose skin for a flatter, more toned stomach'),
            ('fa-chart-line', 'Body Contouring &amp; Definition', 'Sculpt and shape the midsection for a smooth silhouette'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Boosts natural collagen for long-lasting skin firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Achieve dramatic contouring without surgery'),
            ('fa-droplet', 'Smoothness &amp; Radiance', 'Hydrates and nourishes skin for soft, glowing results'),
            ('fa-clock', 'Long-Lasting Results', 'Results improve over time with proper maintenance')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the stomach area to remove impurities and prep the skin for maximum effectiveness.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Treatment zones are carefully marked to target sagging skin and stubborn fat.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS Energy Delivery', '<strong>HIFU:</strong> Penetrates deep tissue to lift and tighten. <strong>MPT:</strong> Firms surface skin. <strong>MFU:</strong> Stimulates collagen. <strong>EMS:</strong> Tones abdominal muscles.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy is delivered strategically to enhance abdominal firmness and definition.'),
            ('fa-droplet', 'Hydrating Serum Infusion &amp; Massage', 'High-performance serums are applied to nourish, hydrate, and improve elasticity.'),
            ('fa-shield-heart', 'Post-Treatment Protection &amp; Radiance', 'Recovery serums maintain lift and firmness, leaving the stomach tightened and sculpted.')
        ],
        'pricing_table': [
            ('Stomach', '£299', '£538', '£957')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal lifting and tightening.'),
            ('Maintenance', 'Every 4–6 months to preserve midsection firmness and contour.')
        ],
        'form_options': [
            'Stomach - £299'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 45–60 minutes including consultation, mapping, treatment, and aftercare.'),
            ('When will I see results?', 'You may notice immediate firmness; full results develop over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine; avoid intense heat or vigorous exercise for 24 hours.'),
            ('How long do the results last?', 'With 2–3 sessions spaced 6–8 weeks apart, results last months; maintain every 4–6 months.')
        ]
    }
    
    # 4. HIFU Love Handles
    configs['hifu-love-handles.html'] = {
        'page_title': 'HIFU Love Handles',
        'tagline': 'Sculpt and contour your waistline',
        'meta_description': 'HIFU Love Handles treatment at Mili Skin & Beauty - Reduce love handles and refine waistline with advanced HIFU technology.',
        'meta_keywords': 'HIFU Love Handles, waist contouring, body sculpting, London',
        'about_content': '''<p>Achieve a firmer, sculpted waistline with our HIFU Love Handles treatment. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this session delivers one of the best non-surgical body contouring results available.</p>
                    <p>This treatment targets stubborn side fat, tightens tissue, and remodels the waistline, leaving it smoother, firmer, and more sculpted. Ideal for clients seeking love handle reduction and waistline definition without surgery.</p>''',
        'benefits': [
            ('fa-chart-line', 'Love Handle Reduction', 'Targets stubborn side fat to refine waistline contours'),
            ('fa-arrow-up', 'Body Contouring &amp; Definition', 'Enhances waist definition for a smooth silhouette'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Boosts natural collagen for long-lasting firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Achieve dramatic contouring without surgery'),
            ('fa-droplet', 'Smoothness &amp; Radiance', 'Hydrates and nourishes skin for soft results'),
            ('fa-clock', 'Long-Lasting Results', 'Results improve over time with proper maintenance')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the waist area to remove impurities and prep the skin.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Treatment zones are marked to target love handles for optimal contouring.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS Energy Delivery', '<strong>HIFU:</strong> Penetrates deep tissue. <strong>MPT:</strong> Firms surface skin. <strong>MFU:</strong> Stimulates collagen. <strong>EMS:</strong> Tones muscles.'),
            ('fa-arrow-up', 'Targeted Contouring', 'Energy is delivered to enhance waist definition and love handle reduction.'),
            ('fa-droplet', 'Hydrating Serum Infusion &amp; Massage', 'High-performance serums are applied to nourish and hydrate.'),
            ('fa-shield-heart', 'Post-Treatment Protection', 'Recovery serums maintain firmness and contour.')
        ],
        'pricing_table': [
            ('Love Handles', '£199', '£358', '£637')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal contouring.'),
            ('Maintenance', 'Every 4–6 months to preserve waistline definition.')
        ],
        'form_options': [
            'Love Handles - £199'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 30–45 minutes including consultation and treatment.'),
            ('When will I see results?', 'You may notice immediate firmness; full results develop over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine; avoid intense exercise for 24 hours.'),
            ('How long do the results last?', 'Results last months; maintain every 4–6 months.')
        ]
    }
    
    # 5. HIFU Stomach + Love Handles
    configs['hifu-stomach-love-handles.html'] = {
        'page_title': 'HIFU Stomach &amp; Love Handles',
        'tagline': 'Complete midsection transformation',
        'meta_description': 'HIFU Stomach & Love Handles treatment at Mili Skin & Beauty - Comprehensive midsection contouring with advanced HIFU technology.',
        'meta_keywords': 'HIFU Stomach Love Handles, waist contouring, abdomen treatment, London',
        'about_content': '''<p>Achieve a firmer, sculpted, and toned midsection with our HIFU Stomach & Love Handles combined treatment. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this session delivers one of the best non-surgical body contouring results available.</p>
                    <p>This comprehensive treatment tightens loose abdominal skin, reduces stubborn fat, and remodels tissue, leaving the stomach and waistline smoother, firmer, and more sculpted. Ideal for clients seeking complete midsection transformation without surgery.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Abdominal Lift &amp; Tightening', 'Firms loose skin for a flatter, more toned stomach'),
            ('fa-chart-line', 'Love Handle Reduction', 'Targets stubborn side fat to refine waistline contours'),
            ('fa-spa', 'Complete Midsection Contouring', 'Sculpts and shapes for a smooth silhouette'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Boosts natural collagen for long-lasting skin firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Achieve dramatic contouring without surgery'),
            ('fa-droplet', 'Smoothness &amp; Radiance', 'Hydrates and nourishes skin for soft, glowing results')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the stomach and waist area.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Treatment zones marked for comprehensive contouring.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS', 'Four technologies work together for maximum results.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy delivered to enhance definition and firmness.'),
            ('fa-droplet', 'Hydrating Serum Infusion', 'Serums nourish and hydrate the treated area.'),
            ('fa-shield-heart', 'Post-Treatment Protection', 'Recovery serums maintain lift and firmness.')
        ],
        'pricing_table': [
            ('Stomach &amp; Love Handles', '£399', '£718', '£1,277')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal lifting, tightening, and fat reduction.'),
            ('Maintenance', 'Every 4–6 months to preserve midsection firmness and contour.')
        ],
        'form_options': [
            'Stomach & Love Handles - £399'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 60–75 minutes for the combined treatment.'),
            ('When will I see results?', 'You may notice immediate firmness; full results develop over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine; avoid intense exercise for 24 hours.'),
            ('How long do the results last?', 'Results last months; maintain every 4–6 months.')
        ]
    }
    
    # 6. HIFU Inner Thighs
    configs['hifu-inner-thighs.html'] = {
        'page_title': 'HIFU Inner Thighs',
        'tagline': 'Tighten and tone inner thigh area',
        'meta_description': 'HIFU Inner Thighs treatment at Mili Skin & Beauty - Tighten sagging inner thigh skin with advanced HIFU technology.',
        'meta_keywords': 'HIFU Inner Thighs, thigh tightening, leg contouring, London',
        'about_content': '''<p>Sculpt, lift, and tone your legs with our HIFU Inner Thighs treatment, designed to tighten sagging skin, reduce cellulite, and enhance thigh contours. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this approach delivers one of the best non-surgical thigh lifting and contouring results available.</p>
                    <p>This treatment stimulates collagen, firms tissue, and tones underlying muscles, leaving inner thighs smoother, lifted, and contoured. Ideal for clients seeking inner thigh tightening without surgery.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Thigh Lift &amp; Tone', 'Firms sagging skin for smoother, sculpted legs'),
            ('fa-chart-line', 'Inner Thigh Contouring', 'Enhances thigh definition and overall shape'),
            ('fa-spa', 'Cellulite Reduction', 'Targets uneven texture and improves skin elasticity'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Boosts natural collagen for long-lasting firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Dramatic lift and contour without surgery'),
            ('fa-droplet', 'Hydration &amp; Smoothness', 'Nourishes skin for soft, supple results')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the thigh area to prep skin for maximum results.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Treatment zones marked to target sagging skin and cellulite.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS', 'Four technologies lift, tone, and sculpt thighs.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy enhances inner thigh definition and firmness.'),
            ('fa-droplet', 'Hydrating Serum Infusion', 'Serums hydrate and restore elasticity.'),
            ('fa-shield-heart', 'Post-Treatment Protection', 'Recovery serums maintain lift and firmness.')
        ],
        'pricing_table': [
            ('Inner Thighs', '£199', '£358', '£637')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal thigh lift and tone.'),
            ('Maintenance', 'Every 4–6 months to preserve firmness and smoothness.')
        ],
        'form_options': [
            'Inner Thighs - £199'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 30–45 minutes including consultation and treatment.'),
            ('When will I see results?', 'You may notice immediate firmness; full results develop over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine.'),
            ('How long do the results last?', 'Results last months; maintain every 4–6 months.')
        ]
    }
    
    # 7. HIFU Outer Thighs
    configs['hifu-outer-thighs.html'] = {
        'page_title': 'HIFU Outer Thighs',
        'tagline': 'Contour and smooth outer thigh area',
        'meta_description': 'HIFU Outer Thighs treatment at Mili Skin & Beauty - Contour and smooth outer thighs with advanced HIFU technology.',
        'meta_keywords': 'HIFU Outer Thighs, thigh contouring, leg sculpting, London',
        'about_content': '''<p>Sculpt, lift, and tone your legs with our HIFU Outer Thighs treatment, designed to tighten sagging skin, reduce cellulite, and enhance thigh contours. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this approach delivers one of the best non-surgical thigh lifting and contouring results available.</p>
                    <p>This treatment stimulates collagen, firms tissue, and tones underlying muscles, leaving outer thighs smoother, lifted, and contoured. Ideal for clients seeking outer thigh contouring without surgery.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Thigh Lift &amp; Tone', 'Firms sagging skin for smoother, sculpted legs'),
            ('fa-chart-line', 'Outer Thigh Contouring', 'Enhances thigh definition and overall shape'),
            ('fa-spa', 'Cellulite Reduction', 'Targets uneven texture and improves skin elasticity'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Boosts natural collagen for long-lasting firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Dramatic lift and contour without surgery'),
            ('fa-droplet', 'Hydration &amp; Smoothness', 'Nourishes skin for soft, supple results')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the thigh area to prep skin for maximum results.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Treatment zones marked to target sagging skin and uneven tissue.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS', 'Four technologies lift, tone, and sculpt thighs.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy enhances outer thigh definition and firmness.'),
            ('fa-droplet', 'Hydrating Serum Infusion', 'Serums hydrate and restore elasticity.'),
            ('fa-shield-heart', 'Post-Treatment Protection', 'Recovery serums maintain lift and firmness.')
        ],
        'pricing_table': [
            ('Outer Thighs', '£199', '£358', '£637')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal thigh lift and tone.'),
            ('Maintenance', 'Every 4–6 months to preserve firmness and smoothness.')
        ],
        'form_options': [
            'Outer Thighs - £199'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 30–45 minutes including consultation and treatment.'),
            ('When will I see results?', 'You may notice immediate firmness; full results develop over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine.'),
            ('How long do the results last?', 'Results last months; maintain every 4–6 months.')
        ]
    }
    
    # 8. HIFU Thighs (Combined Inner + Outer)
    configs['hifu-thighs.html'] = {
        'page_title': 'HIFU Thighs (Inner &amp; Outer)',
        'tagline': 'Complete thigh transformation',
        'meta_description': 'HIFU Thighs treatment at Mili Skin & Beauty - Comprehensive inner and outer thigh contouring with advanced HIFU technology.',
        'meta_keywords': 'HIFU Thighs, thigh tightening, leg contouring, London',
        'about_content': '''<p>Sculpt, lift, and tone your legs with our comprehensive HIFU Thighs treatment, designed to tighten sagging skin, reduce cellulite, and enhance thigh contours. Using the latest combination of four advanced technologies — HIFU, MPT, MFU, and EMS — in one treatment, this approach delivers one of the best non-surgical thigh lifting and contouring results available.</p>
                    <p>This treatment stimulates collagen, firms tissue, and tones underlying muscles, leaving thighs smoother, lifted, and contoured. Ideal for clients seeking comprehensive inner and outer thigh tightening and cellulite reduction without surgery.</p>''',
        'benefits': [
            ('fa-arrow-up', 'Thigh Lift &amp; Tone', 'Firms sagging skin for smoother, sculpted legs'),
            ('fa-chart-line', 'Inner &amp; Outer Thigh Contouring', 'Enhances thigh definition and overall shape'),
            ('fa-spa', 'Cellulite Reduction', 'Targets uneven texture and improves skin elasticity'),
            ('fa-heart-pulse', 'Collagen &amp; Elastin Stimulation', 'Boosts natural collagen for long-lasting firmness'),
            ('fa-shield-heart', 'Non-Surgical &amp; Minimal Downtime', 'Dramatic lift and contour without surgery'),
            ('fa-droplet', 'Hydration &amp; Smoothness', 'Nourishes skin for soft, supple results')
        ],
        'steps': [
            ('fa-spa', 'Double Cleanse &amp; Preparation', 'Cleanses the thigh area to prep skin for maximum results.'),
            ('fa-location-crosshairs', 'Precise Mapping &amp; Analysis', 'Treatment zones marked for comprehensive thigh contouring.'),
            ('fa-bolt', 'Advanced HIFU + MPT + MFU + EMS', 'Four technologies lift, tone, and sculpt thighs.'),
            ('fa-arrow-up', 'Targeted Lifting &amp; Contouring', 'Energy enhances complete thigh definition and firmness.'),
            ('fa-droplet', 'Hydrating Serum Infusion', 'Serums hydrate and restore elasticity.'),
            ('fa-shield-heart', 'Post-Treatment Protection', 'Recovery serums maintain lift and firmness.')
        ],
        'pricing_table': [
            ('Inner &amp; Outer Thighs', '£299', '£538', '£957')
        ],
        'frequency': [
            ('Initial Course', '2–3 sessions spaced 6–8 weeks apart for optimal thigh lift, tone, and contour.'),
            ('Maintenance', 'Every 4–6 months to preserve firmness and smoothness.')
        ],
        'form_options': [
            'Inner & Outer Thighs - £299'
        ],
        'faqs': [
            ('Is the treatment painful?', 'Mild warmth or tingling can occur; settings are adjusted to keep you comfortable.'),
            ('How long does the treatment take?', 'Plan for 45–60 minutes for the combined treatment.'),
            ('When will I see results?', 'You may notice immediate firmness; full results develop over 6–12 weeks.'),
            ('Is there any downtime?', 'Minimal downtime. Normal activities are fine.'),
            ('How long do the results last?', 'Results last months; maintain every 4–6 months.')
        ]
    }
    
    return configs


def generate_benefit_cards(benefits):
    """Generate benefit cards HTML."""
    html = ''
    for icon, title, desc in benefits:
        html += f'''<div class="benefit-card">
                            <div class="icon"><i class="fas {icon}"></i></div>
                            <h4>{title}</h4>
                            <p>{desc}</p>
                        </div>
                        '''
    return html


def generate_steps(steps):
    """Generate step cards HTML."""
    html = ''
    for idx, (icon, title, desc) in enumerate(steps, 1):
        html += f'''<div class="experience-card">
                    <div class="step-number">{idx}</div>
                    <div class="step-icon">
                        <i class="fas {icon}"></i>
                    </div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>

                '''
    return html


def generate_pricing_table(pricing_data):
    """Generate pricing table HTML."""
    rows = ''
    for area, price1, price2, price4 in pricing_data:
        rows += f'''<tr style="border-bottom: 1px solid rgba(214, 173, 96, 0.2);">
                                    <td style="padding: 12px; font-weight: 600; color: #1a1a1a;">{area}</td>
                                    <td style="padding: 12px; text-align: center; color: #555;">{price1}</td>
                                    <td style="padding: 12px; text-align: center; color: #555;">{price2}</td>
                                    <td style="padding: 12px; text-align: center; color: #555;">{price4}</td>
                                </tr>
                                '''
    
    html = f'''<h3>Choose Your Area</h3>
                    <div style="overflow-x: auto; margin-bottom: 20px;">
                        <table style="width: 100%; border-collapse: collapse; background: linear-gradient(135deg, #fffdf8 0%, #fffaf2 100%); border: 1px solid rgba(214, 173, 96, 0.3); border-radius: 8px; overflow: hidden;">
                            <thead>
                                <tr style="background: linear-gradient(135deg, #d6ad60, #e5bf77); color: #fff;">
                                    <th style="padding: 12px; text-align: left; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">Area</th>
                                    <th style="padding: 12px; text-align: center; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">1 Session</th>
                                    <th style="padding: 12px; text-align: center; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">2 Sessions</th>
                                    <th style="padding: 12px; text-align: center; font-weight: 600; border-bottom: 2px solid rgba(214, 173, 96, 0.5);">4 Sessions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {rows}
                            </tbody>
                        </table>
                    </div>'''
    return html


def generate_frequency(frequency_data):
    """Generate frequency recommendation HTML."""
    rows = ''
    for label, copy in frequency_data:
        rows += f'''<div class="frequency-row">
                                <div class="frequency-bullet"></div>
                                <div>
                                    <p class="frequency-label">{label}</p>
                                    <p class="frequency-copy">{copy}</p>
                                </div>
                            </div>
                            '''
    
    html = f'''<div class="frequency-card">
                        <div class="frequency-header">
                            <div class="frequency-icon"><i class="fas fa-clock"></i></div>
                            <div>
                                <p class="frequency-title">Recommended Frequency</p>
                                <p class="frequency-sub">Optimize your results with proper scheduling.</p>
                            </div>
                        </div>
                        <div class="frequency-rows">
                            {rows}
                        </div>
                    </div>'''
    return html


def generate_form_options(options):
    """Generate form select options HTML."""
    options_html = '<option value="">Select option</option>\n'
    for option in options:
        options_html += f'                                <option value="{option}">{option}</option>\n'
    
    return f'''<div class="form-group">
                            <label for="interested">Interested in *</label>
                            <select id="interested" name="interested" required>
                                {options_html}                            </select>
                        </div>'''


def generate_faqs(faqs):
    """Generate FAQ accordion HTML."""
    html = ''
    for question, answer in faqs:
        html += f'''<div class="accordion-item">
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
    return html


print("Starting body treatment page generation...")
print(f"Treatment directory: {TREATMENT_DIR}")

configs = generate_treatment_config()
print(f"\\nGenerating {len(configs)} treatment pages...")

for filename, config in configs.items():
    print(f"\\nProcessing: {filename}")
    
    # Generate dynamic HTML sections
    benefits_html = generate_benefit_cards(config['benefits'])
    steps_html = generate_steps(config['steps'])
    pricing_html = generate_pricing_table(config['pricing_table'])
    frequency_html = generate_frequency(config['frequency'])
    form_options_html = generate_form_options(config['form_options'])
    faqs_html = generate_faqs(config['faqs'])
    
    # Read the template from hifu-butt-lift.html
    with open(os.path.join(TREATMENT_DIR, 'hifu-butt-lift.html'), 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholders
    html_content = template
    
    # Replace page-specific content
    html_content = html_content.replace('HIFU Butt &amp; Breast Treatments', config['page_title'])
    html_content = html_content.replace('HIFU Butt & Breast Treatments', config['page_title'])
    html_content = html_content.replace('Lift, sculpt, and firm the buttocks', config['tagline'])
    
    # Replace meta tags
    html_content = html_content.replace(
        'HIFU Butt & Breast Treatments at Mili Skin & Beauty - Lift and firm buttocks and breasts without surgery.',
        config['meta_description']
    )
    html_content = html_content.replace(
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
    html_content = html_content.replace(old_about, config['about_content'])
    
    # Find and replace Benefits section (between <div class="benefits-grid"> and </div> after last benefit-card)
    benefits_start = html_content.find('<div class="benefits-grid">')
    if benefits_start != -1:
        # Find the closing </div> for benefits-grid
        benefits_start += len('<div class="benefits-grid">')
        # Count div depth
        depth = 1
        i = benefits_start
        while depth > 0 and i < len(html_content):
            if html_content[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html_content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    benefits_end = i
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            old_benefits = html_content[benefits_start:benefits_end].strip()
            html_content = html_content[:benefits_start] + '\n                        ' + benefits_html + '\n                    ' + html_content[benefits_end:]
    
    # Find and replace Steps section
    steps_start = html_content.find('<div class="experience-grid">')
    if steps_start != -1:
        steps_start += len('<div class="experience-grid">')
        # Find the closing </div> for experience-grid
        depth = 1
        i = steps_start
        while depth > 0 and i < len(html_content):
            if html_content[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html_content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    steps_end = i
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html_content = html_content[:steps_start] + '\n                ' + steps_html + '            ' + html_content[steps_end:]
    
    # Find and replace Pricing table
    pricing_start = html_content.find('<h3>Choose Your Area</h3>')
    if pricing_start != -1:
        # Find end of pricing table div
        pricing_end = html_content.find('</div>', html_content.find('</table>', pricing_start))
        if pricing_end != -1:
            pricing_end += len('</div>')
            html_content = html_content[:pricing_start] + pricing_html + html_content[pricing_end:]
    
    # Find and replace Frequency card
    freq_start = html_content.find('<div class="frequency-card">')
    if freq_start != -1:
        # Find the closing </div> for frequency-card
        depth = 1
        i = freq_start + len('<div class="frequency-card">')
        while depth > 0 and i < len(html_content):
            if html_content[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html_content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    freq_end = i + 6
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html_content = html_content[:freq_start] + frequency_html + html_content[freq_end:]
    
    # Find and replace Form options
    form_start = html_content.find('<div class="form-group">\n                            <label for="interested">Interested in *</label>')
    if form_start != -1:
        form_end = html_content.find('</div>', form_start) + len('</div>')
        html_content = html_content[:form_start] + form_options_html + html_content[form_end:]
    
    # Find and replace FAQs
    faqs_start = html_content.find('<div class="accordion faqs-accordion">')
    if faqs_start != -1:
        faqs_start += len('<div class="accordion faqs-accordion">')
        # Find the closing </div> for accordion
        depth = 1
        i = faqs_start
        while depth > 0 and i < len(html_content):
            if html_content[i:i+5] == '<div ':
                depth += 1
                i += 5
            elif html_content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    faqs_end = i
                    break
                i += 6
            else:
                i += 1
        
        if depth == 0:
            html_content = html_content[:faqs_start] + '\n                ' + faqs_html + '            ' + html_content[faqs_end:]
    
    # Write the file
    file_path = os.path.join(TREATMENT_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Created: {filename}")

print(f"\\n{'='*60}")
print(f"All {len(configs)} body treatment pages have been generated successfully!")
print(f"{'='*60}")
