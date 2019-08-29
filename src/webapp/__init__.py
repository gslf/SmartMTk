from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '&r9VG9P@]U=<2!xWEo$Uc-2$~e{P$[@yE(S(hk^Kh7@JV'
login = LoginManager(app)

from webapp import routes
