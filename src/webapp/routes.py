from flask import render_template, Response, jsonify, request, redirect,url_for
from flask_login import login_required, login_user, logout_user, current_user

from webapp import app
from webapp.Camera import Camera
from webapp.ComputerVision import ComputerVision
from webapp.User import User
from SmartMTk import SmartMTk

import time


# SmartMTk object init
smtk = SmartMTk()
cv = ComputerVision()


############################################
# Control page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')




############################################
# Login management
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
                
    username = request.form['username']
    password = request.form['password']

    user = User(username)
    user.load()
                   
    if username is None or password is None or not user.check_password(password):
        return redirect(url_for('index'))
    
    login_user(user, remember=True)
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('dashboard'))




############################################
# Video Stream
@app.route('/video_feed')
def video_feed():
    return Response(cv.frameGen(), mimetype='multipart/x-mixed-replace; boundary=frame')



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


#############################################
# Settings endpoint
@app.route('/status', methods=['GET'])
def status():
    s = {'alarm':cv.alarm.status} 
    return jsonify(s)


@app.route('/motiondetection', methods=['POST'])
def motiondetection_switch():
    cv.motion_detection = not cv.motion_detection 
    
    if not cv.motion_detection:
        cv.alarm.defuse()
    return ('', 204)

@app.route('/defusealarm', methods=['POST'])
def defusealarm():
    cv.alarm.defuse() 
    return ('', 204)





