from random import choice

from controllers.lyrics import song_picker, get_verses
from utils.utils import get_now
from twtr_api import tt_api

api = tt_api.twitter_conexao()
log_file = 'log/log_mentions.txt'


def get_new_mentions():
    last_mentions = api.mentions_timeline()
    return {m.id: [m.created_at, m.user.screen_name]
            for m in last_mentions}


def get_mentions_log():
    with open(log_file, 'r') as file_in:
        data = file_in.read().splitlines()
        data = [int(d) for d in data]
    return data


def get_tweets_to_response(log_ids, new_mentions):
    new_mentions_id = new_mentions.keys()
    return set(new_mentions_id).difference(log_ids)


def reply_a_user():
    log = get_mentions_log()
    new_mentions = get_new_mentions()
    tts = list(get_tweets_to_response(log, new_mentions))
    if tts:
        for tt in tts:
            send_a_reply(new_mentions[tt][1], tt)
            print(new_mentions[tt][1], tt)

    new_log = list(new_mentions.keys())
    new_log.extend(tts)
    write_log(new_log)


def pick_a_line():
    verses = get_verses(song_picker())
    line = choice(verses)
    return line


def send_a_reply(user, mention_id):
    line = pick_a_line()
    print(f"@{user} {line}", mention_id, get_now())
    api.update_status(f"@{user} {line}", mention_id)


def write_log(new_log):
    with open(log_file, 'w') as f:
        for log in new_log:
            f.write(f"{log}\n")


if __name__ == "__main__":
    reply_a_user()
