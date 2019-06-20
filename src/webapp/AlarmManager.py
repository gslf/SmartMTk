import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Email import Email

from vars import ALARM_MAIL
from vars import ALARM_MAIL_FROM
from vars import ALARM_MAIL_FROM_PWD
from vars import ALARM_SUBJECT
from vars import ALARM_MESSAGE

class AlarmManager(object):
    ''' A class to manage alarms
    '''
    
    def __init__(self, mail):
        # Alarm config
        self.status = False
        self.mail = mail
               
    def defuse(self):
        '''Defuse alarm
        '''
        self.status = False

        
    def trigger(self, image):
        '''This funcion trigger an alarm
        '''

        if not self.status:
            # Set alarm as active
            self.status = True

            # Send alarm email
            m = Email(ALARM_MAIL_FROM ,self.mail, ALARM_MAIL , ALARM_SUBJECT + "\nSmartMTk by :#/ promezio.it", image)
            m.send(ALARM_MAIL_FROM, ALARM_MAIL_FROM_PWD)
