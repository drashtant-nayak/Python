# os library if needed
import os
# smptp library for email send functionality
import smtplib
from email.mime.text      import MIMEText
from email.header         import Header

def sendemail(subject,body):
    # MIME definition
    msg = MIMEText(body, 'plain', 'utf-8')
    # Setting Subject with proper utf format	
    msg['Subject'] = Header(subject, 'utf-8')
    # Setting up from emailer
    msg['From'] = "Dev-INWK admin@devinwk.com"
    # Receivers email address
    recipients = "drashtant391993@gmail.com"
    msg['To'] = recipients
    # smtp with proper format of port and timeout 
    s = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    s.set_debuglevel(1)
    try:
        s.starttls()
        s.login("dynotecxmailer@gmail.com", "DynSol1!")
        s.sendmail(msg['From'], recipients, msg.as_string())
    finally:
        s.quit()

sendemail("Testing","Demo Message")
