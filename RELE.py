import RPi.GPIO  as GPIO
import time

GPIO.setmode(GPIO.BCM)
r1 = 6
r2 = 13
r3 = 19
r4 = 26

GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)
GPIO.setup(r4, GPIO.OUT)

while True:
    GPIO.output(r1, GPIO.HIGH)
    GPIO.output(r2, GPIO.HIGH)
    GPIO.output(r3, GPIO.HIGH)
    GPIO.output(r4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(r1, GPIO.LOW)
    GPIO.output(r2, GPIO.LOW)
    GPIO.output(r3, GPIO.LOW)
    GPIO.output(r4, GPIO.)
    time.sleep(1)