import pyrebase

#Configure and Connext to Firebase

firebaseConfig = { "apiKey": "AIzaSyDRNRy2kWJEf6ZyQ57Q_TP6N0iloIjBUK8",
                   "authDomain": "p-rasp.firebaseapp.com",
                   "databaseURL": "https://p-rasp-default-rtdb.firebaseio.com",
                   "projectId": "p-rasp",
                   "storageBucket": "p-rasp.appspot.com",
                   "messagingSenderId": "235208075939",
                   "appId": "1:235208075939:web:4223c6f5df5f60521ced16"}

firebase=pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

h1=db.child("database/humedad1").get()
h2=db.child("database/humedad2").get()
h3=db.child("database/humedad3").get()
luz=db.child("database/luz").get()
temp=db.child("database/temperatura").get()

print ("humedad 1 :", h1.val())
print ("humedad 2 :", h2.val())
print ("humedad 3 :", h3.val())
print ("luz :", luz.val())
print ("temperatura :", temp.val())