import lcddriver
import time

display = lcddriver.lcd()  # 핀배열, 번호 고정

try:
    while True:
        print("Hello Chung-Ang University")
        display.lcd_display_string("Python Class!", 1)
        display.lcd_display_string("with physical", 2)
        time.sleep(2)
        display.lcd_display_string("Nice meet you!", 1)
        display.lcd_display_string("Good Work~!!", 2)
        time.sleep(2)
        display.lcd_clear()
        time.sleep(2)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
