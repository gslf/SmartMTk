import cv2
import numpy as np
import imutils
import time

from vars import ALARM_MAIL

from webapp.Camera import Camera
from webapp.AlarmManager import AlarmManager

class ComputerVision(object):
    ''' A class for computer vision and image generation
    '''

    def __init__(self):
        # Camera object
        self.camera = Camera()
        time.sleep(2)

        # Frames
        self.curr_frame = None
        self.prev_frame = None

        # Options
        self.motion_detection = False

        # Alarm Manager
        self.alarm = AlarmManager(ALARM_MAIL)

    def detectMov(self):
        ''' Motion detector, compare last 2 frames and detect difference. 
        When motion is detected launch an alarm
        '''

        if self.curr_frame != None and self.prev_frame != None:
            # Load frames in grayscale
            arr1 = np.fromstring(self.curr_frame, np.uint8)
            frame1 = cv2.imdecode(arr1, cv2.IMREAD_GRAYSCALE)

            arr2 = np.fromstring(self.prev_frame, np.uint8)
            frame2 = cv2.imdecode(arr2, cv2.IMREAD_GRAYSCALE)

            # Calculate difference
            delta = cv2.absdiff(frame1, frame2)
            tresh = cv2.threshold (delta, 25, 255, cv2.THRESH_BINARY)[1]
            tresh = cv2.dilate(tresh, None, iterations=2)
            areas = cv2.findContours(tresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            areas = imutils.grab_contours(areas)

            # Loop on all detected areas
            for area in areas:
                # Trigger an alarm if current area is big enough
                if cv2.contourArea(area) > 20:
                    self.alarm.trigger(self.curr_frame)

    def frameGen(self):
        ''' Frame generator

        Return:
            Frame - jpeg encoded frame
        '''

        # Frame generator loop
        while True:
            # Save previous frame and load current frame
            self.prev_frame = self.curr_frame
            self.curr_frame = self.camera.frame

            # Motion detection
            if self.motion_detection:
                self.detectMov()

            # Return last frame
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + self.camera.frame + b'\r\n')
