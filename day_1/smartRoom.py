import RPi.GPIO as GPIO
import time

#### GPIO SETTINGS ####
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##################

# LED settings
GPIO.setup(14, GPIO.OUT)

# LED
def led_on():
    GPIO.output(14,1)
    GPIO.cleanup()


def led_off():    
    GPIO.output(14,0)
    GPIO.cleanup()


# Moter settings
# SERVO_PIN = 12
SERVO_PIN = 12
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50) # 힘 세기
servo.start(0) # 시작 힘

servo.ChangeDutyCycle(7.5)
# window
def window_open():
    if window == 0: # 문이 닫혀있다면 문을 열음
        print("Open")
        servo.ChangeDutyCycle(2.5)
        window = 1
        return 1
def window_close():
    if window==1: #문이 열려있다면 문을 닫음
        print("Close")
        servo.ChangeDutyCycle(7.5)
        window = 0
        return 0

# active sensor
GPIO.setup(4, GPIO.IN)
def active_sensor():
    while True:
        if GPIO.input(sensor)==1:
            print("Active")
            time.sleep(1)
            return 1
        else:
            print("Not Active")
            time.sleep(3)
            return 0

## buzz
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 100)
Frq = [263,294,330,349,392,440,493,523] # 도레미파솔라시
a,b,c=263,294,330
Frq1 = [c,b,a,b,c,c,c,b,b,b,c,c,c,c,b,a,b,c,c,c,b,b,c,b,a]
speed = 0.5

p.start(10)

def buzz():
    try:
        while 1:
            for fr in Frq1:
                p.ChangeFrequency(fr)
                time.sleep(speed)

            time.sleep(5)
    except KeyboardInterrupt:
        pass
        p.stop()


#GPIO.output(14,GPIO.LOW)
#led_off()

servo.ChangeDutyCycle(2.5)