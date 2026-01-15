/**
 * Node.js Server for Mili Skin & Beauty Contact Form
 * Alternative to PHP backend
 */

const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('.')); // Serve static files

// Rate limiting storage (in-memory, use Redis for production)
const submissionTracker = new Map();

// Clean up old submissions every hour
setInterval(() => {
    const now = Date.now();
    for (const [ip, timestamp] of submissionTracker.entries()) {
        if (now - timestamp > 3600000) { // 1 hour
            submissionTracker.delete(ip);
        }
    }
}, 3600000);

// Email transporter configuration
const transporter = nodemailer.createTransport({
    host: process.env.EMAIL_HOST || 'smtp.gmail.com',
    port: process.env.EMAIL_PORT || 587,
    secure: false,
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
});

// Verify email configuration on startup
transporter.verify((error, success) => {
    if (error) {
        console.error('Email configuration error:', error);
    } else {
        console.log('✅ Email server is ready to send messages');
    }
});

// Input validation helpers
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function sanitizeInput(input) {
    return input.trim().replace(/[<>]/g, '');
}

// Contact form endpoint
app.post('/api/contact', async (req, res) => {
    try {
        // Get client IP for rate limiting
        const clientIP = req.ip || req.connection.remoteAddress;
        
        // Rate limiting check
        const lastSubmission = submissionTracker.get(clientIP);
        const now = Date.now();
        if (lastSubmission && (now - lastSubmission) < 60000) { // 60 seconds
            return res.status(429).json({
                success: false,
                message: 'Please wait a moment before submitting again.'
            });
        }

        // Extract and sanitize form data
        const { name, email, phone, message } = req.body;
        
        const sanitizedName = sanitizeInput(name || '');
        const sanitizedEmail = sanitizeInput(email || '');
        const sanitizedPhone = sanitizeInput(phone || '');
        const sanitizedMessage = sanitizeInput(message || '');

        // Validation
        const errors = [];

        if (!sanitizedName) {
            errors.push('Name is required.');
        } else if (sanitizedName.length < 2) {
            errors.push('Name must be at least 2 characters.');
        }

        if (!sanitizedEmail) {
            errors.push('Email is required.');
        } else if (!validateEmail(sanitizedEmail)) {
            errors.push('Invalid email address.');
        }

        if (!sanitizedMessage) {
            errors.push('Message is required.');
        } else if (sanitizedMessage.length < 10) {
            errors.push('Message must be at least 10 characters.');
        }

        if (errors.length > 0) {
            return res.status(400).json({
                success: false,
                message: errors.join(' ')
            });
        }

        // Create email HTML
        const emailHTML = `
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        line-height: 1.6; 
                        color: #333; 
                        margin: 0;
                        padding: 0;
                    }
                    .container { 
                        max-width: 600px; 
                        margin: 0 auto; 
                        padding: 20px; 
                    }
                    .header { 
                        background: linear-gradient(135deg, #8B6F47, #C9A87C); 
                        color: white; 
                        padding: 30px 20px; 
                        text-align: center;
                        border-radius: 5px 5px 0 0;
                    }
                    .header h2 {
                        margin: 0 0 10px 0;
                        font-size: 24px;
                    }
                    .content { 
                        background: #f9f9f9; 
                        padding: 30px 20px; 
                        border-radius: 0 0 5px 5px;
                    }
                    .field { 
                        margin-bottom: 20px;
                        background: white;
                        padding: 15px;
                        border-radius: 5px;
                        border-left: 4px solid #D4AF37;
                    }
                    .label { 
                        font-weight: bold; 
                        color: #8B6F47;
                        font-size: 12px;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 5px;
                    }
                    .value { 
                        color: #333; 
                        margin-top: 5px;
                        font-size: 14px;
                    }
                    .footer { 
                        text-align: center; 
                        margin-top: 20px; 
                        color: #666; 
                        font-size: 12px;
                        padding: 20px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h2>New Contact Form Submission</h2>
                        <p>Mili Skin & Beauty</p>
                    </div>
                    <div class="content">
                        <div class="field">
                            <div class="label">Name</div>
                            <div class="value">${sanitizedName}</div>
                        </div>
                        <div class="field">
                            <div class="label">Email</div>
                            <div class="value">${sanitizedEmail}</div>
                        </div>
                        ${sanitizedPhone ? `
                        <div class="field">
                            <div class="label">Phone</div>
                            <div class="value">${sanitizedPhone}</div>
                        </div>
                        ` : ''}
                        <div class="field">
                            <div class="label">Message</div>
                            <div class="value">${sanitizedMessage.replace(/\n/g, '<br>')}</div>
                        </div>
                        <div class="field">
                            <div class="label">Submitted</div>
                            <div class="value">${new Date().toLocaleString('en-GB', { 
                                dateStyle: 'full', 
                                timeStyle: 'short' 
                            })}</div>
                        </div>
                    </div>
                    <div class="footer">
                        <p>This email was sent from the Mili Skin & Beauty contact form.</p>
                        <p>📍 13b Edinburgh Cl, London E2 9NY | 📞 07346 001219</p>
                    </div>
                </div>
            </body>
            </html>
        `;

        // Email options
        const mailOptions = {
            from: `"Mili Skin & Beauty" <${process.env.EMAIL_USER}>`,
            to: process.env.EMAIL_TO || 'Militest@gmail.com',
            replyTo: sanitizedEmail,
            subject: `New Contact Form Submission from ${sanitizedName}`,
            html: emailHTML,
            text: `
Name: ${sanitizedName}
Email: ${sanitizedEmail}
Phone: ${sanitizedPhone || 'Not provided'}
Message: ${sanitizedMessage}
Submitted: ${new Date().toLocaleString()}
            `
        };

        // Send email
        await transporter.sendMail(mailOptions);

        // Update rate limiting tracker
        submissionTracker.set(clientIP, now);

        // Success response
        res.json({
            success: true,
            message: 'Thank you for your message! We will get back to you soon.'
        });

        // Log submission
        console.log(`✉️ New submission from: ${sanitizedName} (${sanitizedEmail})`);

    } catch (error) {
        console.error('Contact form error:', error);
        res.status(500).json({
            success: false,
            message: 'An error occurred. Please email us directly at Militest@gmail.com'
        });
    }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({ 
        status: 'ok', 
        timestamp: new Date().toISOString(),
        service: 'Mili Skin & Beauty API'
    });
});

// Serve index.html for root path
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ 
        success: false, 
        message: 'Endpoint not found' 
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 Mili Skin & Beauty server running on port ${PORT}`);
    console.log(`📧 Contact form API: http://localhost:${PORT}/api/contact`);
    console.log(`🏥 Health check: http://localhost:${PORT}/api/health`);
    console.log(`🌐 Website: http://localhost:${PORT}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
    console.log('SIGTERM received, shutting down gracefully...');
    process.exit(0);
});

module.exports = app;
