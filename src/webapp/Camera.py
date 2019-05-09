import cv2
import pygame
from time import time

class Camera(object):
    '''An object for manage USB camera'''

    def __init__(self):
        self.frame = None
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise RuntimeError('Could not start camera.')


    def get_frame(self):
        '''Get frame from USB camera
        
        Return:
            frame - Encoded image (.jpg)
        '''

        try:
            _, img = self.camera.read()
            self.frame = cv2.imencode('.jpg', img)[1].tobytes()

        except Exception as e:
            self.camera.release()
            self.camera = cv2.VideoCapture(0)
            print(e)
        
        return self.frame


    def __del__(self):
        self.camera.release()


