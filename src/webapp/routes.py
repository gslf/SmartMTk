from flask import render_template, Response
from webapp import app
from webapp.Camera import Camera
from SmartMTk import SmartMTk

import time


# SmartMTk object init
smtk = SmartMTk()

############################################
# Control page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

############################################
# Video Stream
def gen():
    
    # Create a camera object
    camera = Camera()
    time.sleep(2)
    
    # Yeld camera frames
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + camera.frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')



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





