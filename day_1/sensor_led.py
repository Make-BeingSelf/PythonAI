import RPi.GPIO as GPIO
import time

sensor=4
LED=8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN) # sensor:4
GPIO.setup(LED, GPIO.OUT) # LED: 8


try:
    while True:

        if GPIO.input(sensor)==1:
            print("Detect!!")
            GPIO.output(8,1)
            time.sleep(0.1)
        else:
            print("No Detect!!")
            GPIO.output(8,0)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup
