import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import tweepy
import datetime
import time

''' Tweepyの設定 '''
CK = "111111111111111111111111111111"
CS = "111111111111111111111111111111"
AT = "111111111111111111111111111111"
AS = "111111111111111111111111111111"
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
