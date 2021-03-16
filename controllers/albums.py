import os
from random import choice
from datetime import datetime as dt


def get_album_path(album):
    return f"data/images/{album}"


def get_random_album():
    album_files = os.listdir("data/images")
    album = choice(album_files)
    album_name = album[:-4].capitalize()
    album_path = f"data/images/{album}"
    return album_name, album_path


def album_of_day():
    today = dt.today()
    hour = today.hour
    # 0 for monday
    weekday = today.weekday()

    if weekday == 0 and (6 <= hour <= 11):
        message = "Começando bem a semana com esse disco aqui. " \
                  "Alguém tem esse?"
    elif weekday == 4 and (18 <= hour <= 23):
        message = "Vamos sextar ouvindo um disco? " \
                  "Esse já tá na vitrola!"
    else:
        message = None

    _, album_pic = get_random_album()
    return message, album_pic
