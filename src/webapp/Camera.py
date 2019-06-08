from time import time
import picamera
import io
import threading

class Camera(object):
    '''An object for manage picamera'''

    def __init__(self):
        self.frame = None

        # Retrieve frames in a background thread
        thread = threading.Thread(target=self.retrieveFrame, args=())
        thread.daemon = True
        thread.start()


    def retrieveFrame(self):
        '''Retrieve frame from picamera
        '''
        
        # Get PiCamera object
        with picamera.PiCamera() as camera:
            # Set camera resolution
            camera.resolution = (320, 240)

            # Loop for frame retrieving
            while True:
                stream = io.BytesIO()
                for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                    # return current frame
                    stream.seek(0)
                    self.frame =  stream.read() 
                     
                    # reset stream for next frame
                    stream.seek(0)
                    stream.truncate()



