from random import choice
from datetime import datetime, timedelta

from controllers.lyrics import song_picker, get_verses
from utils.utils import get_now
from twtr_api import tt_api

api = tt_api.twitter_conexao()
last_mentions = api.mentions_timeline()

now = datetime.utcnow()
last_five_minutes = now - timedelta(minutes=5)


def users_mentions_last_seven_days(mentions):
    for mention in mentions:
        if mention.created_at > last_five_minutes:
            send_a_reply(mention.user.screen_name, mention.id)


def pick_a_line():
    verses = get_verses(song_picker())
    line = choice(verses)
    return line


def send_a_reply(user, mention_id):
    line = pick_a_line()
    print(f"@{user} {line}", mention_id, get_now())
    api.update_status(f"@{user} {line}", mention_id)


users_mentions_last_seven_days(last_mentions)
