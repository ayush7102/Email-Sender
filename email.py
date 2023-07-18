import smtplib

# SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email credentials
sender_email = '#email of sender'
password = '#password of the email'

# Recipient and email content
subject = "#Hui Hui"
body = "#python is a game"
msg = f"Subject: {subject}\n\n{body}"
recipients = ['#list of mail recipients']

# Create an SMTP object and establish a secure connection
ob = smtplib.SMTP_SSL(smtp_server, smtp_port)

try:
    # Login to the email account
    ob.login(sender_email, password)
    
    # Send the email
    ob.sendmail(sender_email, recipients, msg)
    print("Mail Sent")
    
except smtplib.SMTPAuthenticationError:
    print("SMTP Authentication Error. Please check your credentials.")
    
finally:
    # Quit the SMTP connection
    ob.quit()
