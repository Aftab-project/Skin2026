/* ============================================
   Treatment Page Shared Components
   Reusable JavaScript for all treatment pages
   ============================================ */

// ==========================================
// STICKY SUBNAV HANDLER
// ==========================================
class StickySubnav {
    constructor() {
        this.subnav = document.querySelector('.sticky-subnav');
        this.links = document.querySelectorAll('.subnav-link');
        this.sections = document.querySelectorAll('[id^="section-"]');
        
        if (!this.subnav) return;
        
        this.init();
    }

    init() {
        // Smooth scroll handling
        this.links.forEach(link => {
            link.addEventListener('click', (e) => this.handleLinkClick(e));
        });

        // Update active link on scroll
        window.addEventListener('scroll', () => this.updateActiveLink());
        document.addEventListener('scroll', () => this.updateActiveLink());
    }

    handleLinkClick(e) {
        e.preventDefault();
        const href = e.target.getAttribute('href');
        
        if (!href) return;
        
        const targetId = href.replace('#', '');
        const target = document.getElementById(targetId);
        
        if (target) {
            const subnav = document.querySelector('.sticky-subnav');
            const offset = subnav ? subnav.offsetHeight + 80 : 80;
            
            const topPos = target.offsetTop - offset;
            window.scrollTo({
                top: topPos,
                behavior: 'smooth'
            });

            // Update active link
            this.setActive(e.target);
        }
    }

    updateActiveLink() {
        const scrollPos = window.scrollY || document.documentElement.scrollTop;
        const subnav = document.querySelector('.sticky-subnav');
        const offset = subnav ? subnav.offsetHeight + 100 : 150;

        let current = null;
        
        this.sections.forEach(section => {
            const sectionTop = section.offsetTop - offset;
            const sectionBottom = sectionTop + section.offsetHeight;
            
            if (scrollPos >= sectionTop && scrollPos < sectionBottom) {
                current = section.id;
            }
        });

        // Handle case where we're at the top
        if (scrollPos < 300) {
            const firstSection = document.querySelector('[id^="section-"]');
            if (firstSection) current = firstSection.id;
        }

        // Update all links
        this.links.forEach(link => {
            const href = link.getAttribute('href');
            if (href && href === '#' + current) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    setActive(link) {
        this.links.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
    }
}

// ==========================================
// ACCORDION HANDLER
// ==========================================
class Accordion {
    constructor(selector) {
        this.accordion = document.querySelector(selector);
        if (!this.accordion) return;
        
        this.items = Array.from(this.accordion.querySelectorAll('.accordion-item'));
        this.isFaqAccordion = this.accordion.classList.contains('faqs-accordion');
        
        // Initialize
        this.init();
    }

    init() {
        // Attach click handlers directly to headers
        this.items.forEach((item, index) => {
            const header = item.querySelector('.accordion-header');
            
            if (header) {
                // Remove any existing listeners (in case of re-init)
                const newHeader = header.cloneNode(true);
                header.parentNode.replaceChild(newHeader, header);
                
                // Add fresh listener
                const freshHeader = item.querySelector('.accordion-header');
                freshHeader.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    this.toggle(item);
                });
            }
        });
    }

    toggle(item) {
        // Make sure item is actually in this accordion
        if (!this.items.includes(item)) return;
        
        if (item.classList.contains('open')) {
            this.close(item);
        } else {
            // For step accordions, close all others
            if (!this.isFaqAccordion) {
                this.items.forEach(i => {
                    if (i !== item && i.classList.contains('open')) {
                        this.close(i);
                    }
                });
            }
            this.open(item);
        }
    }

    open(item) {
        item.classList.add('open');
        const content = item.querySelector('.accordion-content');
        const body = item.querySelector('.accordion-body');
        
        if (content && body) {
            const scrollHeight = body.scrollHeight;
            content.style.maxHeight = (scrollHeight + 48) + 'px'; // 48px for padding
        }
    }

    close(item) {
        item.classList.remove('open');
        const content = item.querySelector('.accordion-content');
        
        if (content) {
            content.style.maxHeight = '0px';
        }
    }
}

// ==========================================
// CAROUSEL HANDLER
// ==========================================
class Carousel {
    constructor(selector) {
        this.carousel = document.querySelector(selector);
        if (!this.carousel) return;
        
        this.slides = this.carousel.querySelectorAll('.carousel-slide');
        this.dots = this.carousel.querySelectorAll('.dot');
        this.prevBtn = this.carousel.querySelector('[data-carousel-prev]');
        this.nextBtn = this.carousel.querySelector('[data-carousel-next]');
        
        this.currentIndex = 0;
        this.autoPlayTimer = null;
        
        if (this.slides.length > 0) {
            this.init();
        }
    }

    init() {
        // Button controls
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => this.prev());
        }
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => this.next());
        }

        // Dot controls
        this.dots.forEach((dot, index) => {
            dot.addEventListener('click', () => this.goTo(index));
        });

        // Touch support
        let touchStartX = 0;
        this.carousel.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
        });

        this.carousel.addEventListener('touchend', (e) => {
            const touchEndX = e.changedTouches[0].clientX;
            if (touchStartX - touchEndX > 50) {
                this.next();
            } else if (touchEndX - touchStartX > 50) {
                this.prev();
            }
        });

        // Auto play (optional - comment out if not needed)
        this.startAutoPlay();
        
        // Stop auto play on hover
        this.carousel.addEventListener('mouseenter', () => this.stopAutoPlay());
        this.carousel.addEventListener('mouseleave', () => this.startAutoPlay());

        // Show first slide
        this.goTo(0);
    }

    goTo(index) {
        if (index < 0) {
            this.currentIndex = this.slides.length - 1;
        } else if (index >= this.slides.length) {
            this.currentIndex = 0;
        } else {
            this.currentIndex = index;
        }

        this.slides.forEach((slide, i) => {
            slide.classList.remove('active');
            if (i === this.currentIndex) {
                slide.classList.add('active');
            }
        });

        this.dots.forEach((dot, i) => {
            dot.classList.remove('active');
            if (i === this.currentIndex) {
                dot.classList.add('active');
            }
        });
    }

    next() {
        this.goTo(this.currentIndex + 1);
    }

    prev() {
        this.goTo(this.currentIndex - 1);
    }

    startAutoPlay() {
        this.autoPlayTimer = setInterval(() => this.next(), 5000);
    }

    stopAutoPlay() {
        if (this.autoPlayTimer) {
            clearInterval(this.autoPlayTimer);
        }
    }
}

// ==========================================
// FORM HANDLER
// ==========================================
class EnquiryForm {
    constructor(selector) {
        this.form = document.querySelector(selector);
        if (!this.form) return;
        
        this.submitBtn = this.form.querySelector('[type="submit"]');
        this.init();
    }

    init() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    handleSubmit(e) {
        e.preventDefault();

        if (!this.validate()) {
            alert('Please fill in all required fields.');
            return;
        }

        // Gather form data
        const formData = new FormData(this.form);
        
        // Send to existing handler (contact.php or similar)
        const action = this.form.getAttribute('action') || 'contact.php';
        
        this.submitBtn.disabled = true;
        this.submitBtn.textContent = 'Sending...';

        fetch(action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.ok ? 'success' : 'error')
        .then(result => {
            if (result === 'success') {
                alert('Thank you! We will contact you shortly.');
                this.form.reset();
            } else {
                alert('There was an error sending your message. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error. Please try again later.');
        })
        .finally(() => {
            this.submitBtn.disabled = false;
            this.submitBtn.textContent = 'Send Enquiry';
        });
    }

    validate() {
        const inputs = this.form.querySelectorAll('[required]');
        let valid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.classList.add('error');
                valid = false;
            } else {
                input.classList.remove('error');
            }
        });

        return valid;
    }
}

// ==========================================
// LAZY LOAD IMAGES
// ==========================================
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for older browsers
        images.forEach(img => {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        });
    }
}

// ==========================================
// DOCUMENT READY INITIALIZATION
// ==========================================
document.addEventListener('DOMContentLoaded', function() {
    // Initialize sticky subnav
    new StickySubnav();

    // Initialize accordions (for steps and FAQs)
    new Accordion('.steps-accordion');
    new Accordion('.faqs-accordion');

    // Initialize carousel
    new Carousel('.results-carousel');

    // Initialize form
    new EnquiryForm('.enquiry-form');

    // Initialize lazy loading
    initLazyLoading();

    // Smooth scroll behavior (fallback for older browsers)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href && href !== '#') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
});

// ==========================================
// SCROLL TO TOP HELPER
// ==========================================
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        const subnav = document.querySelector('.sticky-subnav');
        const offset = subnav ? subnav.offsetHeight + 80 : 80;
        const topPos = section.offsetTop - offset;
        
        window.scrollTo({
            top: topPos,
            behavior: 'smooth'
        });
    }
}

// Export functions for inline use
window.scrollToSection = scrollToSection;
