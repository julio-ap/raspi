import serial
from time import sleep
arduino= serial.Serial(port= "/dev/ttyAMA0", baudrate=9600,timeout=0.05)



while True:
    if (arduino.in_waiting >0):
        mensaje=""
        line=arduino.readline()
        mensaje=(line.decode('utf-8').split())
        '''
        hum1 = mensaje [0]
        hum2 = mensaje [1]
        hum3 = mensaje [2]
        luz= mensaje [3]
        temp =mensaje[4]'''
        print (mensaje)
    ##sleep(0.1)