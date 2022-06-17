
from time import sleep
import signal
import firebase_admin
from threading import Thread
from gpiozero import LED
from firebase_admin import db
from firebase_admin import credentials

LED = LED(17)

PAHT_CRED = '/home/pi/Desktop/projects/cred.json'
URL_DB = 'https://p-rasp-default-rtdb.firebaseio.com/'
REF_HUERTA = 'huerta'
REF_REGADO = 'regado'
REF_REGAR = 'regar'

class IOT():
    
    def __init__(self):
        cred = credentials.Certificate(PAHT_CRED)
        firebase_admin.initialize_app(cred, {
                             'databaseURL': URL_DB
        })
        self.refhuerta = db.reference(REF_HUERTA)
        
        #self.estructura()
        
        self.refregado = self.refhuerta.child(REF_REGADO)
        self.refregar = self.refregado.child(REF_REGAR)
        
    def estructura(self):
        self.refhuerta.set({
            'regado': {
                'regar' :True
                }
            })
        
    def ledcontrol(self, estado):
        if estado == "true":
            LED.on()
            print('led on')
        elif estado =="false":
            LED.off()
            print('led off')
            
    def database(self):
        E, i = [], 0
        
        last_state = self.refregar.get()
        self.ledcontrol(last_state)
        
        E.append(last_state)
        
        while True:
            actual_state = self.refregar.get()
            E.append(actual_state)
            
            if E[i] != E[-1]:
                self.ledcontrol(actual_state)
                
            del E[0]
            i = i + i
            sleep(0.4)
        
        
    
        
iot = IOT()

estado = Thread(target = iot.database)
estado.daemon = True
estado.start()

signal.pause()