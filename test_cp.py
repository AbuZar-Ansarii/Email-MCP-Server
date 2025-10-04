import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError


# ⚡ Configure your email credentials here
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "fake.emailt1t2@gmail.com"
SENDER_PASSWORD = "klkezzmoqqnhnhgb" 



def send_email(receiver: str, subject: str, content: str) -> str:
    """Send an email to the given receiver with subject and content."""
    try:
        # Validate receiver email
        validate_email(receiver)

        # Create email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(content, "plain"))

        # Send using SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver, msg.as_string())

        return f"✅ Email sent successfully to {receiver}"
    except EmailNotValidError:
        return "❌ Invalid receiver email address"
    except Exception as e:
        return f"❌ Failed to send email: {e}"

if __name__ == "__main__":
    rec = 'venomdemon718@gmail.com'
    sub = 'email test mcp server'
    cont = 'hii, this email is sending for the testing perpose only'
    
    result = send_email(rec, sub, cont)
    print(result)
