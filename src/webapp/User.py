import json

from flask_login import UserMixin

from webapp import login


@login.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
    '''User managemant
    '''

    def __init__(self,username):
        self.id = username
        self.load()
        
    def load(self):
        with open('storage') as f:  
            content = json.load(f)

            if self.id in  content:
                data=content[self.id]
                self.pwd = data['pwd']
                self.alarm_mail = data['alarm_mail']
                self.alarm_mail_server = data['alarm_mail_server']
                self.alarm_mail_port = data['alarm_mail_port']
                self.alarm_mail_from = data['alarm_mail_from']
                self.alarm_mail_from_pwd = data['alarm_mail_from_pwd']

                return True
            else:
                self.pwd = None
                self.alarm_mail = None
                self.alarm_mail_server = None
                self.alarm_mail_port = None
                self.alarm_mail_from = None
                self.alarm_mail_from_pwd = None
                return False

    def save(self):
        data = {self.id:{
                    'pwd': self.pwd,
                    'alarm_mail': self.alarm_mail,
                    'alarm_mail_server': self.alarm_mail_server,
                    'alarm_mail_port': self.alarm_mail_port,
                    'alarm_mail_from': self.alarm_mail_from,
                    'alarm_mail_from_pwd': self.alarm_mail_from_pwd
                    }}

        with open('storage', 'w') as f:  
            json.dump(data, f)

    def check_password(self, password):
        print(self.pwd)
        if self.pwd == password:
            return True
        else:
            return False
