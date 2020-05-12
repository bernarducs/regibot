import tweepy
from configparser import ConfigParser

config = ConfigParser()
config.read(r'keys.ini')
keys = config['DEFAULT']

CONSUMER_KEY=keys['CONSUMER_KEY']
CONSUMER_SECRET=keys['CONSUMER_SECRET']
ACCESS_TOKEN=keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=keys['ACCESS_TOKEN_SECRET']


def twitter_conexao():

    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)
