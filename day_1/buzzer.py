import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 100)
Frq = [263, 294, 330, 349, 392, 440, 493, 523]  # 도레미파솔라시
a, b, c = 263, 294, 330
# 비행기 노래 Frq1
Frq1 = [c, b, a, b, c, c, c, b, b, b, c, c,
        c, c, b, a, b, c, c, c, b, b, c, b, a]
speed = 0.5

p.start(10)

try:
    while 1:
        for fr in Frq1:
            p.ChangeFrequency(fr)
            time.sleep(speed)

        time.sleep(5)
except KeyboardInterrupt:
    pass
    p.stop()
