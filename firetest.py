from firebase import firebase

url = 'https://p-rasp-default-rtdb.firebaseio.com/'
firebase = firebase.FirebaseApplication(url)
result = firebase.put("/Test Val","Value",126)
print(result)
