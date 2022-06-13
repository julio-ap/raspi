import pyrebase

#Configure and Connext to Firebase

firebaseConfig = { apiKey: "AIzaSyDRNRy2kWJEf6ZyQ57Q_TP6N0iloIjBUK8",
                   authDomain: "p-rasp.firebaseapp.com",
                   databaseURL: "https://p-rasp-default-rtdb.firebaseio.com",
                   projectId: "p-rasp",
                   storageBucket: "p-rasp.appspot.com",
                   messagingSenderId: "235208075939",
                   appId: "1:235208075939:web:4223c6f5df5f60521ced16"}

firebase=pyrebase.initialize_app(firebaseConfig)
