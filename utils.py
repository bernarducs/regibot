import time
from random import choice
from datetime import datetime

DELAY = 60 * 60 * 3


def get_delay():
    return time.sleep(DELAY)


EMOJIS = [['🎶'], ['🎵'], ['🎵🎶'], ['🎶🎵'], ['🎵🎵'],
          ['🎶🎶'], ['🎼'], ['🎼🎵'], ['🎸'], ['🎸🎼'],
          ['🎹🎸'], ['🎷'], ['🎷🎷'], ['🎷🎸'], ['🎶🎼']]


def get_emoji():
    emoji = str(choice(EMOJIS)[0])
    return emoji


def get_now():
    now = datetime.now()
    print('{}/{}/{} {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
