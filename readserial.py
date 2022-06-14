import serial
arduino= serial.Serial(port= "/dev/ttyAMA0", baudrate=9600, timeout=.1)

while True:
    if (arduino.in_waiting >0):
         line=arduino.readline()
         print(line.decode('utf-8'))