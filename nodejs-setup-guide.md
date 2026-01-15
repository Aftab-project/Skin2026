# Node.js Alternative - Contact Form Handler
# If you prefer Node.js over PHP, use this setup

## Prerequisites
- Node.js 14.x or higher
- npm (Node Package Manager)

## Installation

1. Install dependencies:
```bash
npm install express nodemailer body-parser cors dotenv
```

2. Create a `.env` file in the root directory:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
EMAIL_TO=aftabk200284@gmail.com
PORT=3000
```

3. Save the server code as `server.js`

4. Run the server:
```bash
node server.js
```

## Gmail Setup (if using Gmail)

1. Go to your Google Account settings
2. Enable 2-Factor Authentication
3. Generate an App Password
4. Use the App Password in `.env` file

## Production Deployment

### Option 1: Heroku
```bash
heroku create mili-skin-beauty
git push heroku main
```

### Option 2: DigitalOcean, AWS, or other VPS
- Upload files via FTP/SSH
- Install Node.js on server
- Use PM2 for process management:
```bash
npm install -g pm2
pm2 start server.js
pm2 startup
```

### Option 3: Vercel/Netlify (Serverless)
- Deploy as serverless function
- Configure environment variables in dashboard

## Update index.html

Change the form action in `index.html`:
```html
<!-- From -->
<form id="contactForm" class="contact-form" action="contact.php" method="POST">

<!-- To -->
<form id="contactForm" class="contact-form" action="http://your-server:3000/api/contact" method="POST">
```

## Testing

Use curl or Postman to test:
```bash
curl -X POST http://localhost:3000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "phone": "07123456789",
    "message": "Test message"
  }'
```

## Security Notes

- Never commit `.env` file to Git
- Add `.env` to `.gitignore`
- Use environment variables for all sensitive data
- Implement rate limiting in production
- Use HTTPS in production
