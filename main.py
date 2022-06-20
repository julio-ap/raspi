import serial
from time import sleep
import signal
import firebase_admin
from threading import Thread
import RPi.GPIO  as GPIO
import time

from firebase_admin import db
from firebase_admin import credentials

r1 = 6
r2 = 13
r3 = 19
r4 = 26


PAHT_CRED = '/home/pi/Desktop/projects/cred.json'
URL_DB = 'https://p-rasp-default-rtdb.firebaseio.com/'

REF_HUERTA = 'huerta'

REF_AUTO = 'auto'
REF_REGAR1 = 'regar1'
REF_REGAR2 = 'regar2'
REF_REGAR3 = 'regar3'

REF_SEN ='sensores'
REF_H1 ='hum1'
REF_H2='hum2'
REF_H3='hum3'
REF_LUZ = 'luz'
REF_TEMP = 'temp'


                    
                    
class IOT():
    
    def __init__(self):
       
        cred = credentials.Certificate(PAHT_CRED)
        firebase_admin.initialize_app(cred, {
                             'databaseURL': URL_DB
        })
        self.refhuerta = db.reference(REF_HUERTA)
        
        #self.estructura()
        
        self.refregado = self.refhuerta.child(REF_AUTO)
        self.sensores = self.refhuerta.child(REF_SEN)
        
        self.refregar1 = self.refregado.child(REF_REGAR1)
        self.refregar2 = self.refregado.child(REF_REGAR2)
        self.refregar3 = self.refregado.child(REF_REGAR3)
        
        self.hume1 = self.sensores.child(REF_H1)
        self.hume2 = self.sensores.child(REF_H2)
        self.hume3 = self.sensores.child(REF_H3)
        
        self.luz = self.sensores.child(REF_LUZ)
        self.temp = self.sensores.child(REF_TEMP)
        
    def estructura(self):
        self.refhuerta.set({
            'regado': {
                'auto' :False,
                'regar1':False,
                'regar2':False,
                'regar3':False
                },
            'sensores':{
                'hum1':0,
                'hum2':0,
                'hum3':0,
                'luz':0,
                'temp':0
                }
            })
    def serial_ard(self):
        
        while True:
            arduino= serial.Serial(port= "/dev/ttyAMA0", baudrate=9600,timeout=0.05)
            if (arduino.in_waiting >0):
                mensaje=""
                line=arduino.readline()
                mensaje=(line.decode('utf-8').split())
                hum1 = mensaje [0]
                self.hume1.set(hum1)
                hum2 = mensaje [1]
                self.hume2.set(hum2)
                hum3 = mensaje [2]
                self.hume3.set(hum3)
                l= mensaje [3]
                self.luz.set(l)
                t =mensaje[4]
                self.temp.set(t)
                print (mensaje)
            sleep(0.02)
        
    def r_auto(self, estado):
        if estado == "true":
            LED1.on()
            print('led on')
        elif estado =="false":
            LED1.off()
            print('led off')
            


    def reg1(self, estado1):
        if estado1 == "true":
            LED2.on()
            print('led on')
        elif estado1 =="false":
            LED2.off()
            print('led off')
            
            
            
    def reg2(self, estado2):
        if estado2 == "true":
            LED3.on()
            print('led on')
        elif estado2 =="false":
            LED3.off()
            print('led off')



    def reg3(self, estado3):
        if estado3 == "true":
            LED4.on()
            print('led on')
        elif estado3 =="false":
            LED4.off()
            print('led off')
            
            
            
    def database(self):
        E, i = [], 0
        
        last_state = self.refregado.get()
        self.r_auto(last_state)
        E.append(last_state)
        
        while True:
            actual_state = self.refregado.get()
            E.append(actual_state)
            
            if E[i] != E[-1]:
                self.r_auto(actual_state)
                
            del E[0]
            i = i + i
            sleep(0.05)
            
            
            
    def database1(self):
        A, i = [], 0
        
        last_state1 = self.refregar1.get()
        self.reg1(last_state1)
        A.append(last_state1)
        
        while True:
            actual_state1 = self.refregar1.get()
            A.append(actual_state1)
            
            if A[i] != A[-1]:
                self.reg1(actual_state1)
                
            del A[0]
            i = i + i
            sleep(0.05)
            

    def database2(self):
        B, i = [], 0
        
        last_state2 = self.refregar2.get()
        self.reg2(last_state2)
        B.append(last_state2)
        
        while True:
            actual_state2 = self.refregar2.get()
            B.append(actual_state2)
            
            if B[i] != B[-1]:
                self.reg2(actual_state2)
                
            del B[0]
            i = i + i
            sleep(0.05)
            
    def database3(self):
        C, i = [], 0
        
        last_state3 = self.refregar3.get()
        self.reg3(last_state3)
        C.append(last_state3)
        
        while True:
            actual_state3 = self.refregar3.get()
            C.append(actual_state3)
            
            if C[i] != C[-1]:
                self.reg3(actual_state3)
                
            del C[0]
            i = i + i
            sleep(0.05)
            
       
       
iot = IOT()
ard_serial =Thread(target =iot.serial_ard)
ard_serial.daemon = True
ard_serial.start()

estado = Thread(target = iot.database)
estado.daemon = True
estado.start()

estado1 = Thread(target = iot.database1)
estado1.daemon = True
estado1.start()

estado2 = Thread(target = iot.database2)
estado2.daemon = True
estado2.start()

estado3= Thread(target = iot.database3)
estado3.daemon = True
estado3.start()


##signal.pause()



    