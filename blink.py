import RPi.GPIO as GPIO
import time

ESPERA = 0.5

LED1 =17
LED2 =22
LED3 =27

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

try:
    while True:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.HIGH)
        GPIO.output(LED3, GPIO.HIGH)
        time.sleep(ESPERA)
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.LOW)
        time.sleep(ESPERA)
except KeyboardInterrupt:
    print ("interrupcion")
finally:
    GPIO.cleanup()