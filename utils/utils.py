import time
from random import choice
from datetime import datetime

DELAY = 60 * 60 * 5

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
    now = datetime.utcnow()
    return now.strftime('%Y-%m-%d %H:%M:%S')
