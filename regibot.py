"""
arquivo principal que envia tuítes pela api
"""

import tweepy

from twtr_api import tt_api

from controllers.lyrics import current_song_and_verse
from controllers.spotify import spotify_link
from utils.utils import get_emoji, get_delay, CHIFRE

api = tt_api.twitter_conexao()

while True:

    verse, song, new_song, last_verse = current_song_and_verse()
    if new_song:
        intro_txt = f"Hoje irei tocar {song} \nSe liga aí, bicho! {CHIFRE}"
        print(intro_txt, '\n')
        api.update_status(intro_txt)
        get_delay()

    if verse:
        verse_txt = f"{verse} {get_emoji()}"
        print(verse_txt, '\n')
        try:
            api.update_status(verse_txt)
        except tweepy.error.TweepError as e:
            print(e)
        get_delay()

    if last_verse:
        link = spotify_link(song)
        if link:
            spfy_txt = f"Ouça {song} em {link} \n{CHIFRE} @reginaldorossi"
            print(spfy_txt, '\n')
            api.update_status(spfy_txt)
            get_delay()
