import serial
from time import sleep
import signal
import firebase_admin
from threading import Thread
import RPi.GPIO  as GPIO
import time
from firebase_admin import db
from firebase_admin import credentials

GPIO.setmode(GPIO.BCM)
r1 = 6
r2 = 13
r3 = 19
r4 = 26

GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)
GPIO.setup(r4, GPIO.OUT)

PAHT_CRED = '/home/pi/Desktop/projects/cred.json'
URL_DB = 'https://p-rasp-default-rtdb.firebaseio.com/'

REF_HUERTA = 'huerta'

REF_REGADO = 'regado'
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
        
        self.refregado = self.refhuerta.child(REF_REGADO)
        self.sensores = self.refhuerta.child(REF_SEN)
        
        self.auto = self.refregado.child(REF_AUTO)
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
       
    
    
    
    
    ## regado1
    
    
    def regado1(self, estado):
        if estado == "true":
            GPIO.output(r1, GPIO.HIGH)
            GPIO.output(r4, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(r1, GPIO.LOW)
            GPIO.output(r4, GPIO.LOW  
                        
            
    def database1(self):
        E, i = [], 0
        
        last_state = self.refregar1.get()
        self.regado1(last_state)
        E.append(last_state)
        
        while True:
            actual_state = self.refregar1.get()
            E.append(actual_state)
            
            if E[i] != E[-1]:
                self.regado1(actual_state)
                
            del E[0]
            i = i + i
            sleep(0.05)
                        
                        
   ##regado2
                        
    def regado2(self, estado):
        if estado == "true":
            GPIO.output(r1, GPIO.HIGH)
            GPIO.output(r4, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(r1, GPIO.LOW)
            GPIO.output(r4, GPIO.LOW  
                        
            
    def database2(self):
        A, i = [], 0
        
        last_state = self.refregar2.get()
        self.regado2(last_state)
        A.append(last_state)
        
        while True:
            actual_state = self.refregar2.get()
            A.append(actual_state)
            
            if A[i] != A[-1]:
                self.regado2(actual_state)
                
            del A[0]
            i = i + i
            sleep(0.05)
                      
    
    ##REGADO3
                        
    def regado3(self, estado):
        if estado == "true":
            GPIO.output(r1, GPIO.HIGH)
            GPIO.output(r4, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(r1, GPIO.LOW)
            GPIO.output(r4, GPIO.LOW            
        
                        
            
    def database3(self):
        B, i = [], 0
        
        last_state = self.refregar3.get()
        self.regado3(last_state)
        B.append(last_state)
        
        while True:
            actual_state = self.refregar3.get()
            B.append(actual_state)
            
            if B[i] != B[-1]:
                self.regado3(actual_state)
                
            del B[0]
            i = i + i
            sleep(0.05)
                        
            
        
    
        
iot = IOT()

                        '''
au = Thread(target = iot.database)
estado.daemon = True
estado.start()
                        '''
                        
rega1 = Thread(target = iot.database1)
rega1.daemon = True
rega1.start()

rega2 = Thread(target = iot.database2)
rega2.daemon = True
rega2.start()

rega3 = Thread(target = iot.database3)
rega3.daemon = True
rega3.start()
