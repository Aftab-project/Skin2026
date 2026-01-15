# Mili Skin & Beauty Website

A modern, elegant, and fully responsive website for Mili Skin & Beauty - a premium skin care clinic in Bethnal Green, London.

## 🌟 Features

- **Responsive Design**: Fully mobile-friendly and optimized for all devices
- **Modern UI/UX**: Clean, luxurious design with earthy color palette
- **SEO Optimized**: Complete meta tags, structured data, and semantic HTML5
- **Interactive Elements**: Smooth scrolling, hover animations, mobile menu
- **Contact Form**: Full PHP backend for email submissions
- **Service Showcase**: 24 treatments across Facials and HIFU categories
- **Price Transparency**: Clear pricing displayed for all services

## 📁 Project Structure

```
MiliSkin&Beauty/
├── index.html          # Main HTML file
├── styles.css          # Complete stylesheet
├── script.js           # JavaScript functionality
├── contact.php         # PHP email handler
├── images/             # Image assets directory
│   └── README.md       # Image specifications guide
├── Requirement         # Original project requirements
└── README.md          # This file
```

## 🎨 Design Specifications

### Color Palette
- **Primary**: #8B6F47 (Brown)
- **Secondary**: #C9A87C (Beige/Gold)
- **Accent**: #D4AF37 (Gold)
- **Background**: #F5F1E8 (Light beige)
- **Text**: #2C2416 (Dark brown)

### Typography
- **Headings**: Playfair Display (serif)
- **Body**: Lato (sans-serif)

## 🚀 Getting Started

### Prerequisites
- Web server with PHP support (Apache, Nginx, or hosting service)
- PHP 7.0 or higher
- Mail server configured for PHP mail() function

### Installation

1. **Upload Files**
   - Upload all files to your web server
   - Ensure proper file permissions (755 for directories, 644 for files)

2. **Configure Email**
   - Open `contact.php`
   - Verify the email address (currently set to: aftabk200284@gmail.com)
   - Test email functionality

3. **Add Images**
   - Review `/images/README.md` for required images
   - Upload your logo, hero banner, and treatment images
   - Follow naming conventions specified in the images README

4. **Update Google Maps**
   - Open `index.html`
   - Locate the Google Maps iframe in the contact section
   - Update the embed URL with your exact location coordinates

5. **Customize Content**
   - Update opening hours in the footer
   - Adjust business information if needed
   - Add or modify service descriptions

### Local Development

To test locally:

1. **Using PHP Built-in Server**:
   ```bash
   cd path/to/MiliSkin&Beauty
   php -S localhost:8000
   ```
   Visit: http://localhost:8000

2. **Using XAMPP/WAMP/MAMP**:
   - Place folder in htdocs/www directory
   - Start Apache server
   - Visit: http://localhost/MiliSkin&Beauty

## 📧 Contact Form Setup

The contact form uses PHP's `mail()` function. For production:

### Option 1: Hosting Provider's Mail Server
Most hosting providers (Bluehost, SiteGround, etc.) support PHP mail() out of the box.

### Option 2: SMTP Setup (Recommended)
For better deliverability, use PHPMailer with SMTP:

1. Download PHPMailer: https://github.com/PHPMailer/PHPMailer
2. Configure SMTP settings (Gmail, SendGrid, etc.)
3. Update `contact.php` to use PHPMailer

### Option 3: Third-Party Services
- **Formspree**: https://formspree.io
- **EmailJS**: https://www.emailjs.com
- **SendGrid**: https://sendgrid.com

## 📱 Sections Overview

1. **Header & Navigation**
   - Sticky navigation with smooth scroll
   - Mobile-responsive hamburger menu
   - Instagram social link

2. **Hero Section**
   - Full-screen banner with tagline
   - Call-to-action "Book Now" button

3. **About Section**
   - Company description
   - Four key benefits with icons

4. **Services Section**
   - 11 Facial Treatments
   - 13 HIFU Treatments
   - Each with description, price, and benefits

5. **Price List**
   - Clear pricing table layout
   - Organized by category

6. **Contact Section**
   - Contact information cards
   - Working contact form
   - Google Maps integration
   - Phone, email, and Instagram links

7. **Footer**
   - Quick navigation links
   - Business information
   - Social media links
   - Opening hours

## 🔧 Customization

### Changing Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #8B6F47;
    --secondary-color: #C9A87C;
    --accent-color: #D4AF37;
    /* etc. */
}
```

### Adding New Services
1. Copy an existing service card in `index.html`
2. Update service name, price, description, and benefits
3. Add corresponding image to `/images/` directory

### Modifying Layout
- Grid layouts use CSS Grid and Flexbox
- Responsive breakpoints: 992px, 768px, 480px
- Adjust in `styles.css` media queries section

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📊 Performance Optimization

- Images: Use WebP format and lazy loading
- CSS: Already minified and optimized
- JavaScript: Vanilla JS (no heavy frameworks)
- Fonts: Google Fonts with preconnect

## 🔒 Security Features

- Input sanitization in PHP
- XSS protection
- CSRF protection via session
- Rate limiting (60 seconds between submissions)
- Email validation

## 📈 SEO Features

- Semantic HTML5 structure
- Meta descriptions and keywords
- Open Graph tags for social sharing
- Structured data (JSON-LD) for local business
- Alt tags for images
- Proper heading hierarchy

## 🎯 Business Information

- **Business Name**: Mili Skin & Beauty
- **Location**: Bethnal Green, London
- **Phone**: 07346 001219
- **Email**: aftabk200284@gmail.com
- **Instagram**: @mili.skin.beauty

## 📝 To-Do / Future Enhancements

- [ ] Add actual images (logo, hero, treatments)
- [ ] Set up online booking system integration
- [ ] Add customer testimonials section
- [ ] Implement before/after gallery
- [ ] Add blog section for skin care tips
- [ ] Integrate Google Analytics
- [ ] Add multilingual support
- [ ] Implement appointment calendar

## 🐛 Troubleshooting

### Contact Form Not Working
- Check PHP mail() function is enabled on server
- Verify email address is correct in `contact.php`
- Check server error logs
- Test with a simple PHP mail test script

### Images Not Loading
- Verify image filenames match exactly (case-sensitive)
- Check file permissions
- Ensure images are in `/images/` directory
- Check browser console for errors

### Mobile Menu Not Working
- Clear browser cache
- Check JavaScript console for errors
- Verify `script.js` is loading correctly

## 💻 Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Flexbox, Grid, Animations
- **JavaScript**: ES6+ (Vanilla JS)
- **PHP**: Backend form handling
- **Font Awesome**: Icon library
- **Google Fonts**: Typography

## 📄 License

This website is proprietary to Mili Skin & Beauty. All rights reserved.

## 👤 Contact & Support

For website support or modifications:
- **Email**: aftabk200284@gmail.com
- **Instagram**: @mili.skin.beauty

---

**Built with ❤️ for Mili Skin & Beauty**

*Last Updated: December 2025*
