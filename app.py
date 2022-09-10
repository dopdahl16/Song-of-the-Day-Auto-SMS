import smtplib
import ssl
import os
import random
from email.message import EmailMessage

email_sender = str(os.environ.get('SongoftheDaySenderEmail'))
email_password = str(os.environ.get('SongoftheDayAutoSMSPASSWORD'))
email_receiver = str(os.environ.get('SongoftheDayRecipientEmail'))

body_list = [
    "What's the song of the day today?",
    "Song of the day?",
    "Today's song of the day?",
    "What do be that music of this 24 hour period?",
    "Bestow onto me thine selection of the song of the day",
    "Today. Song."
]
body = random.choice(body_list)

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = body
em.set_content(" ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())