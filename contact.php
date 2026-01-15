<?php
/**
 * Mili Skin & Beauty - Contact Form Handler
 * Sends form submissions to email
 */

// Set response header to JSON
header('Content-Type: application/json');

// Initialize response array
$response = array('success' => false, 'message' => '');

// Check if form was submitted via POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    $response['message'] = 'Invalid request method.';
    echo json_encode($response);
    exit;
}

// Security: Basic spam protection
session_start();
$submitTime = time();
if (isset($_SESSION['last_submit']) && ($submitTime - $_SESSION['last_submit']) < 60) {
    $response['message'] = 'Please wait a moment before submitting again.';
    echo json_encode($response);
    exit;
}

// Sanitize and validate input data
$name = isset($_POST['name']) ? trim(strip_tags($_POST['name'])) : '';
$email = isset($_POST['email']) ? trim(strip_tags($_POST['email'])) : '';
$phone = isset($_POST['phone']) ? trim(strip_tags($_POST['phone'])) : '';
$message = isset($_POST['message']) ? trim(strip_tags($_POST['message'])) : '';

// Validation
$errors = array();

if (empty($name)) {
    $errors[] = 'Name is required.';
} elseif (strlen($name) < 2) {
    $errors[] = 'Name must be at least 2 characters.';
}

if (empty($email)) {
    $errors[] = 'Email is required.';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'Invalid email address.';
}

if (empty($message)) {
    $errors[] = 'Message is required.';
} elseif (strlen($message) < 10) {
    $errors[] = 'Message must be at least 10 characters.';
}

// If there are validation errors, return them
if (!empty($errors)) {
    $response['message'] = implode(' ', $errors);
    echo json_encode($response);
    exit;
}

// Email configuration
$to = 'Militest@gmail.com';
$subject = 'New Contact Form Submission - Mili Skin & Beauty';

// Create email body
$emailBody = "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: linear-gradient(135deg, #8B6F47, #C9A87C); color: white; padding: 20px; text-align: center; }
        .content { background: #f5f5f5; padding: 20px; border-radius: 5px; margin-top: 20px; }
        .field { margin-bottom: 15px; }
        .label { font-weight: bold; color: #8B6F47; }
        .value { color: #333; margin-top: 5px; }
        .footer { text-align: center; margin-top: 20px; color: #666; font-size: 12px; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h2>New Contact Form Submission</h2>
            <p>Mili Skin & Beauty</p>
        </div>
        <div class='content'>
            <div class='field'>
                <div class='label'>Name:</div>
                <div class='value'>" . htmlspecialchars($name) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Email:</div>
                <div class='value'>" . htmlspecialchars($email) . "</div>
            </div>";

if (!empty($phone)) {
    $emailBody .= "
            <div class='field'>
                <div class='label'>Phone:</div>
                <div class='value'>" . htmlspecialchars($phone) . "</div>
            </div>";
}

$emailBody .= "
            <div class='field'>
                <div class='label'>Message:</div>
                <div class='value'>" . nl2br(htmlspecialchars($message)) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Submitted:</div>
                <div class='value'>" . date('F j, Y, g:i a') . "</div>
            </div>
        </div>
        <div class='footer'>
            <p>This email was sent from the Mili Skin & Beauty contact form.</p>
        </div>
    </div>
</body>
</html>
";

// Email headers
$headers = array();
$headers[] = 'MIME-Version: 1.0';
$headers[] = 'Content-type: text/html; charset=utf-8';
$headers[] = 'From: Mili Skin & Beauty <noreply@miliskinbeauty.com>';
$headers[] = 'Reply-To: ' . $email;
$headers[] = 'X-Mailer: PHP/' . phpversion();

// Send email
try {
    $mailSent = mail($to, $subject, $emailBody, implode("\r\n", $headers));
    
    if ($mailSent) {
        $response['success'] = true;
        $response['message'] = 'Thank you for your message! We will get back to you soon.';
        
        // Store submission time to prevent spam
        $_SESSION['last_submit'] = $submitTime;
        
        // Optional: Log submission (for analytics)
        $logEntry = date('Y-m-d H:i:s') . " - New submission from: $name ($email)\n";
        @file_put_contents('contact_log.txt', $logEntry, FILE_APPEND);
    } else {
        $response['message'] = 'Failed to send email. Please try again or contact us directly at Militest@gmail.com';
    }
} catch (Exception $e) {
    $response['message'] = 'An error occurred. Please email us directly at Militest@gmail.com';
    error_log('Contact form error: ' . $e->getMessage());
}

// Send JSON response
echo json_encode($response);
exit;
?>
