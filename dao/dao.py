import os
import json

SONG_FOLDER = 'songs/txt/'


def set_log(song_number, verse_number, verses_total):
    # updating
    # se for o ultimo verso...
    if verse_number == verses_total:
        # zero o numero de versos e passa para outra musica
        verse_number = 0
        song_number += 1
    else:
        # caso contrario, apenas passa para outro verso
        verse_number += 1

    dic = {'song': song_number, 'verse': verse_number}
    with open('log/log.txt', 'w') as f:
        f.write(str(dic))


def update():
    with open('log/log.txt', 'r') as f:
        log = eval(f.read())
    song_number, verse_number = log['song'], log['verse']
    song_number = 0 if song_number >= 65 else song_number
    files_list = get_files_list()
    file = files_list[song_number]
    song = file.strip('.txt')

    verses_list = get_verses(file)
    verses_total = len(verses_list[:-1])
    verse = verses_list[verse_number]

    return song_number, song, verse_number, verses_total, verse


def get_files_list():
    files_list = os.listdir(SONG_FOLDER)
    return files_list


def get_verses(song_file):
    with open(SONG_FOLDER + song_file, 'r', encoding='latin-1') as f:
        verses_list = list()
        for line in f:
            verses_list.append(line.strip('\n'))
    return verses_list


def get_spotify_links():
    with open('external/links_spotify.json') as file:
        spotify_links = json.load(file)
    return spotify_links
