# doge-altar

import time
import RPi.GPIO as GPIO

# use GPIO-PINS on Raspberry
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) as Output
GPIO.setup(11, GPIO.OUT)

# Let the LED blink
while 1:
    # LED off
    GPIO.output(11, GPIO.LOW)
    # eine Sekunde warten
    time.sleep(1)
    # LED on
    GPIO.output(11, GPIO.HIGH)
    # wait a second
    time.sleep(1)
