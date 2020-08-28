import RPi.GPIO as GPIO
import time
import lcddriver

display = lcddriver.lcd() # 핀배열, 번호 고정

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 100)
a,b,c=263,294,330
Frq1 = [c,b,a,b,c,c,c,b,b,b,c,c,c,c,b,a,b,c,c,c,b,b,c,b,a]
speed = 0.5


sensor=4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

people=0

try:
    while True:
        p.start(10)
        if GPIO.input(sensor)==1:
            
            people+=1
            time.sleep(1)
            display.lcd_display_string("Welcome!!!", 2)
            print('welcome!')
            for fr in Frq1:
                p.ChangeFrequency(fr)
                time.sleep(speed)
        p.stop()
except KeyboardInterrupt:
    print(people)
    GPIO.cleanup
    p.stop()
