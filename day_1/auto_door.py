import RPi.GPIO as GPIO
import time


SERVO_PIN = 12

TRGI = 23
ECHO = 24


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(SERVO_PIN, GPIO.OUT)

GPIO.setup(TRGI, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


servo = GPIO.PWM(SERVO_PIN, 50) # 힘 세기
servo.start(0) # 시작 힘
GPIO.output(TRGI, False)


door = 0 # 0: closed, 1: opened
while True:
    print("Start")
    GPIO.output(TRGI, True)
    time.sleep(0.00001)
    GPIO.output(TRGI, False)
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    check_time = stop - start
    distance = check_time*34300/2
    print("Distance : %.1f cm" %distance)
    time.sleep(0.4)


    if distance <50: # 50cm이내 접근하면 문은 열린 상태
        if door == 0: # 문이 닫혀있다면 문을 열음
            print("Open")
            servo.ChangeDutyCycle(2.5)
            door = 1
        else: # 문이 열려있다면 가만히 있음
            print("Opened") 
            time.sleep(5) # passing time 고려    
    else: # 대상이 50cm이상이거나 없다면 문은 닫힌 상태
        if door==1: #문이 열려있다면 문을 닫음
            print("Close")
            servo.ChangeDutyCycle(7.5)
            door=0
    time.sleep(0.4)