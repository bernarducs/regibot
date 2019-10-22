from dao import dao
from utils import get_emoji, get_delay, get_now
import tweepy
from twtr_api import tt_api

api = tt_api.twitter_conexao()


def regibot_run():
    while True:
        song_number, song, verse_number, verses_total, verse = dao.update()
        print('song number: {}, song:{},verse_number: {},'
              'verses_total: {},'
              'verse: {}'.format(song_number, song, verse_number, verses_total, verse))
        spotify_dict = dao.get_spotify_links()  # return dict of external link

        # tweet intro
        if verse_number == 0:
            tweet = "Hoje eu irei cantar '{}'. Se liga aí, bicho!".format(song)
            print(tweet, get_now())
            # api.update_status(tweet)
            get_delay()

        # tweeting  verses
        try:
            tweet = '{} {}'.format(verse, get_emoji())
            print(tweet, get_now())
            # api.update_status(tweet)
        except tweepy.error.TweepError as e:
            print(e)
            if e[0]['code'] == 187:
                dao.set_log(song_number, verse_number, verses_total)  # updating log
        finally:
            get_delay()

        # external link
        if verse_number == verses_total:
            tweet = "Ouça '{}' em: {}".format(song, spotify_dict[song].strip("\""))
            print(tweet, get_now())
            # api.update_status(tweet)
            get_delay()

if __name__ == '__main__':
    regibot_run()
