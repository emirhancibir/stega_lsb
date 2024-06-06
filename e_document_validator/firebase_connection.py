import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/home/emir/edocsverified-firebase-adminsdk-julmv-3b8553156e.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://edocsverified-default-rtdb.firebaseio.com/'
})

ref = db.reference('server/documents')

print(ref.get())

def send_data_to_firebase(data):
    ref = db.reference('documents')
    ref.push().set(data)

def get_data_from_firebase(verification_code):
    ref = db.reference('documents')
    snapshot = ref.order_by_child('verification_code').equal_to(verification_code).get()
    if snapshot:
        for key, val in snapshot.items():
            return val
    return None

