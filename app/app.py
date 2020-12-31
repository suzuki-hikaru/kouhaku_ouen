from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import tweepy
import config

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_index():
    # 取得した各種キーを代入
    CK = config.CK
    CS = config.CS
    AT = config.AT
    AS = config.AS
    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)
    # tweet 範囲指定
    woeid = {
        "日本": 23424856
    }
    items = []
    for area, wid in woeid.items():
        trends = api.trends_place(wid)[0]
        for i, content in enumerate(trends["trends"]):
            if i == 5:
                break
            rank = i+1
            items.append('トレンド'+str(rank)+'位     '+content['name'])
    return render_template("index.html", items=items)


@app.route("/post_index", methods=['POST'])
def post_index():
    # name = request.form['name']
    return render_template("index.html")

######################################################
