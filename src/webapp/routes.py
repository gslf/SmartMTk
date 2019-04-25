from flask import render_template
from webapp import app

from SmartMTk import SmartMTk


# SmartMTk object init
smtk = SmartMTk()

############################################
# Control page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


############################################
# Control endpoint

@app.route('/shortbrake',methods = ['POST'])
def shorBrake():
    smtk.shortBrake()
    return "Forward"

@app.route('/forward',methods = ['POST'])
def forward():
    smtk.forward()
    return "Forward"

@app.route('/backward',methods = ['POST'])
def backward():
    smtk.backward()
    return "Forward"

@app.route('/center',methods = ['POST'])
def center():
    smtk.straight()
    return "Forward"

@app.route('/right',methods = ['POST'])
def right():
    smtk.turnRight()
    return "Forward"

@app.route('/left',methods = ['POST'])
def left():
    smtk.turnLeft()
    return "Forward"





