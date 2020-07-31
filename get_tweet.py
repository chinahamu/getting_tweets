import TOKEN
import tweepy
import datetime

def gettwitterdata(keyword,dfile,limit):

    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = TOKEN.API_KEY
    Consumer_secret = TOKEN.API_SECRET_KEY
    Access_token = TOKEN.ACCESS_TOKEN
    Access_secret = TOKEN.ACCESS_TOKEN_SECRET

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定 
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    #カーソルを使用してデータ取得
    #for tweet in tweepy.Cursor(api.search, q=q,count=100,tweet_mode='extended').items(10000):

        #つぶやき時間がUTCのため、JSTに変換  ※デバック用のコード
        #jsttime = tweet.created_at + datetime.timedelta(hours=9)
        #print(jsttime)
        #print(tweet)

        #つぶやきテキスト(FULL)を取得
    #    tweets_data.append(tweet.full_text + '\n')

    for tweet in tweepy.Cursor(api.followers_ids, id=q).items(int(limit)):
    	user = api.get_user(tweet)
    	user_info = [user.id_str, user.screen_name, user.name, user.created_at]
    	print(user.screen_name)
    	if(user.protected == False):
	    	for tweet in api.user_timeline(id=user.id_str,include_rts=False):
	    		tweets_data.append(tweet.text+"\n")

    print(tweets_data)

    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)


if __name__ == '__main__':

    #ユーザーIDを入力
    print ('====== 調査するユーザーID   =====')
    keyword = input('>  ')

    #出力ファイル名を入力(相対パス or 絶対パス)
    print ('====== 保存ファイル名 =====')
    dfile = input('>  ')

    #何人分とるか
    print ('====== 何人分とるか =====')
    limit = input('>  ')

    print 

    gettwitterdata(keyword,dfile,limit)
    print('=====END=====')