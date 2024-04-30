import smtplib
#import Emailsendinggame as ex
from email.message import EmailMessage
import ssl

# print(ex.person)

## import  smtlib
# from app2 import password  ie
# this is generated in chrome
email_sender = 'njugunaalekii99@gmail.com'
email_password = ''  # password generated
email_reciever = ""
subject = 'i am writing using python '
body = """
whn you recieve know its alex trying to 
send email with python 
"""
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
