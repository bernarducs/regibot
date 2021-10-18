import os
from random import choice
from ast import literal_eval

FILE_PATH = 'log/log.txt'


def read_log():
    with open(FILE_PATH, 'r') as file_in:
        log = literal_eval(file_in.read())
    return log['song'], log['verse_number']


def write_log(song, verse_number, last_verse):
    if last_verse:
        song = song_picker()
        verse_number = 0
    else:
        verse_number += 1

    dic = {'song': song, 'verse_number': verse_number}
    result = str(dic)
    with open(FILE_PATH, 'w') as file_out:
        file_out.write(result)
    return result


def song_and_verse():
    """
    get current song, verse and if is a new song or last verse
    update its status writing a log txt file
    :return: str, str, bool, bool
    """
    first_verse, last_verse = False, False

    song, verse_number = read_log()
    verses = get_verses(song)
    verse = verses[verse_number]

    # check if is it either first or last verse
    if verse_number == 0:
        first_verse = True
    elif verse_number == len(verses) - 1:
        last_verse = True

    write_log(song, verse_number, last_verse)
    return verse, song, first_verse, last_verse


def current_song_and_verse():
    """
    deprecated
    """

    first_verse, last_verse = False, False
    with open('log/log.txt', 'r') as file_in:
        log = literal_eval(file_in.read())
    song, verse_number = log['song'], log['verse_number']
    try:
        verses = get_verses(song)
        verse = verses[verse_number]
        verse_number += 1
        if verse_number == len(verses):
            last_verse = True
        return verse, song, first_verse, last_verse
    except IndexError:
        first_verse = True
        song = song_picker()
        verses = get_verses(song)
        verse_number = 0
        verse = None
        return verse, song, first_verse, last_verse
    finally:
        dic = {'song': song, 'verse_number': verse_number}
        with open('log/log.txt', 'w') as file_out:
            file_out.write(str(dic))


def song_picker():
    files = os.listdir('data/songs/')
    picked = choice(files)[:-4]
    return picked


def get_verses(song):
    with open(f"data/songs/{song}.txt", "r") as f:
        lines = f.read()
    shaped_verses = transform_verses(literal_eval(lines))
    return shaped_verses


def transform_verses(verses):
    parsed = list()

    def func(v):
        return ['\n'.join(v[i:i + 2]) for i in range(0, len(v), 2)]

    for verse in verses:
        n_items = len(verse)
        if n_items % 2 == 0:
            parsed.extend(func(verse))
        else:
            first, last = verse[:-3], verse[-3:]
            parsed.extend(func(first))
            parsed.extend(['\n'.join(last)])

    parsed_clean = list(filter(None, parsed))
    return parsed_clean
