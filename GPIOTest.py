import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # G
GPIO.setup(21, GPIO.OUT) # R

while True:
    GPIO.output(20, True)
    GPIO.output(21, False)
    time.sleep(1)
    GPIO.output(20, False)
    GPIO.output(21, True)
    time.sleep(1)