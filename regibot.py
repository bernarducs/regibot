"""
arquivo principal que envia tuítes pela api
"""

import tweepy

from twtr_api import tt_api

from controllers.lyrics import song_and_verse
from controllers.spotify import spotify_link
from controllers.albums import album_of_day
from controllers.videos import video_song
from utils.utils import get_emoji, get_delay, get_now, CHIFRE

api = tt_api.twitter_conexao()

while True:
    print(get_now())

    verse, song, new_song, last_verse = song_and_verse()
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
            try:
                api.update_status(spfy_txt)
            except tweepy.error.TweepError as e:
                print(e)
            get_delay()

        video = video_song(song)
        if video:
            media_id = video["media"].media_id
            media_yt_link = video["link"]
            vid_twt = api.update_status(status=f"{song} #reginaldorossi",
                                        media_ids=[media_id])
            api.update_status(status=f"assista o vídeo completo aqui: "
                                     f"in youtube {media_yt_link}",
                              in_reply_to_status_id=vid_twt.id)

    message, album_pic = album_of_day()
    if message:
        print(message, album_pic)
        api.update_with_media(album_pic, message)
        get_delay()
