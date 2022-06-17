import firebase_admin

from firebase_admin import credentials

from firebase_admin import db


cred = credentials.Certificate('/home/pi/Desktop/projects/cred.json')


# Initialize the app with a service account, granting admin privileges

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://p-rasp-default-rtdb.firebaseio.com/'

})


ref = db.reference('message')

print(ref.get())

print ('Ok !')

