import time
from random import choice
from datetime import datetime

DELAY = 1.5

EMOJIS = [['🎶'], ['🎵'], ['🎵🎶'], ['🎶🎵'], ['🎵🎵'],
          ['🎶🎶'], ['🎼'], ['🎼🎵'], ['🎸'], ['🎸🎼'],
          ['🎹🎸'], ['🎷'], ['🎷🎷'], ['🎷🎸'], ['🎶🎼']]

CHIFRE = '🐂'


def get_delay():
    return time.sleep(DELAY)


def get_emoji():
    emoji = str(choice(EMOJIS)[0])
    return emoji


def get_now():
    now = datetime.now()
    return '{}/{}/{} {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
