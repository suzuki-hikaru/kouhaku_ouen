import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import tweepy
import datetime
import time

''' Tweepyの設定 '''
CK = "AcxvPuLT2be7m6M4TVbGrQTi2"
CS = "aYfPmb3wr3lVS8arKVldZ5OrK7PjQK7tvNdHabEcJA66iNxmCS"
AT = "1244563330217345024-WTHY1HKu0rrEAsfTwYmeI6a1GawBls"
AS = "S2dEXLuI4ESxG1VgjZFBtrgs2QGEW5mx4IPTrRtL5UFCi"
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

''' Firebaseの設定 '''
cred = credentials.Certificate('./config.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kouhaku-default-rtdb.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})
ref = db.reference('/another_resource')

key_word = '紅白'


def job():
    # day_time
    dt_now = datetime.datetime.now()
    day_time = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    for tweet in tweepy.Cursor(api.search, q="{} -filter:retweets".format(key_word)).items(1):
        print(day_time)
        t_time = day_time
        print(tweet.text)
        t_text = tweet.text

    def saveDB():
        ref.set({
            'record': {
                'day': t_time,
                'text': t_text
            }
        })

    saveDB()


while(True):
    job()
    time.sleep(15)
