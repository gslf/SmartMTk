import os
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from mimetypes import guess_type
from email.encoders import encode_base64
from getpass import getpass

from vars import ALARM_MAIL_SERVER
from vars import ALARM_MAIL_PORT


class Email(object):
    ''' A class for email managemant
    '''

    def __init__(self, from_address, to_address, subject, message, image=None):
        # Email data
        self.from_address = from_address
        self.to_address = to_address
        
        # Create the email
        self.email = MIMEMultipart()

        self.email['From'] = from_address
        self.email['To'] = to_address
        self.email['Subject'] = subject

        text = MIMEText(message, 'plain')
        self.email.attach(text)

        # Manage attachments
        if image != None:
            attachment = MIMEBase('image','jpg')
            attachment.set_payload(image)
            encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment', filename='image.jpg')
            
            self.email.attach(attachment)

        self.message = self.email.as_string()

    def send(self, username, password):
        # Server data
        server = ALARM_MAIL_SERVER
        port = ALARM_MAIL_PORT
        
        # Connection
        context = ssl.create_default_context()
        connection = smtplib.SMTP_SSL(server, port, context=context)
        connection.login(username, password)

        # Send the message
        connection.sendmail(self.from_address, self.to_address, self.message)
        
        # Close
        connection.close()
