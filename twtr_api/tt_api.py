import tweepy

CONSUMER_KEY='CONSUMER_KEY'
CONSUMER_SECRET='CONSUMER_SECRET'
ACCESS_TOKEN='ACCESS_TOKEN'
ACCESS_TOKEN_SECRET='ACCESS_TOKEN_SECRET'


def twitter_conexao():

    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)