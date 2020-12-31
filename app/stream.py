import tweepy
# 先ほど取得した各種キーを代入する
CK="AcxvPuLT2be7m6M4TVbGrQTi2"
CS="aYfPmb3wr3lVS8arKVldZ5OrK7PjQK7tvNdHabEcJA66iNxmCS"
AT="1244563330217345024-WTHY1HKu0rrEAsfTwYmeI6a1GawBls"
AS="S2dEXLuI4ESxG1VgjZFBtrgs2QGEW5mx4IPTrRtL5UFCi"
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print('------------------------------')
        print(status.text)
        for hashtag in status.entities['hashtags']:
            print(hashtag['text']),
        print("------------------------------")
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.filter(track=['#NiziU'])
