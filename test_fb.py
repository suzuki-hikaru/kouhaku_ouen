import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./config.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kouhaku-default-rtdb.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

ref = db.reference('/another_resource')

## add data to database
users_ref = ref.child('users')

users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
        },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
        }
    })

# insert
users_ref.child('mituba').set({
    'date_of_birth': 'Aug 23, 1994',
    'full_name': 'Mituba Mituba'
    })

## get data
print(ref.get())