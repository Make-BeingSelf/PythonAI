import picamera
import time

with picamera.PiCamera() as camera:
    # camera setting
    camera.resolution=(640,480)
    camera.start_preview()

    # timer
    time.sleep(1)

    # recording
    camera.start_recording('test01.h264')
    camera.wait_recording(10) # recording time
    camera.stop_recording()
    # picture
    #camera.capture('test01.jpg')

    # camera stop
    camera.stop_preview()