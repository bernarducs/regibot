import json


def spotify_link(song_name):
    with open('data/links_spotify/links_spotify.json', 'r') as file:
        links = json.load(file)
        for name, link in links.items():
            if song_name.lower() == name.lower():
                return link
