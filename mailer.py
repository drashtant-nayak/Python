# os library if needed
import os
# smptp library for email send functionality
import smtplib
from email.mime.text      import MIMEText
from email.header         import Header

def sendemail(subject,body,recipients):
    # MIME definition
    msg = MIMEText(body, 'plain', 'utf-8')
    # Setting Subject with proper utf format	
    msg['Subject'] = Header(subject, 'utf-8')
    # Setting up from emailer
    msg['From'] = "no-reply@xyz.com"
    # Receivers email address
    msg['To'] = recipients
    # smtp with proper format of port and timeout 
    s = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    s.set_debuglevel(1)
    try:
        s.starttls()
        s.login("gmail_username", "gmail_password")
        s.sendmail(msg['From'], recipients, msg.as_string())
    finally:
        s.quit()

sendemail("Testing","Demo Message")
