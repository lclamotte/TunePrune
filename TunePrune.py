

import json
import requests
from collections import Counter

def run():
    client_id = "5TRar6_l7ibdD4EQdsGR_nvPBObMWgOkV_SJcPO38tIw3-9KkTGt8D0i5iYUGQ7D"
    client_secret = "hS46e1Y7NYKBeG23y_FIW8SpFX6wt8fkJhrC_Ii9WRaBmZV60A1SvANmrqZj7mSNhNXM3z_mW-CSyReDVm8hwQ"
    client_access_token = "4Wthx9BGZ6-kzb1Ret-lEupMLEfc3dIl9lR-W5Kw3hPeM7_pjAhdvdBONmffVZaR"

    tunePrune = TunePrune(client_id, client_secret, client_access_token)
    artist_name = "Drake"
    artist_id = tunePrune.get_artist_id(artist_name)
    top_songs = tunePrune.get_top_songs(artist_id)
    print ()
    print ("Top songs for " + artist_name + " are: ")
    for song in top_songs:
        print (song.song_title)

class TunePrune():
    def __init__(self, client_id, client_secret, client_access_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_access_token = client_access_token
    
    def get_artist_id(self, artist):
        print ("Getting info for " + artist)
        url = "https://api.genius.com/search?access_token=CLIENT_ACCESS_TOKEN&q=" + artist
        response = self.call_endpoint(url)
        ids = []
        for hit in response["response"]["hits"]:
            if hit["result"]["primary_artist"]["name"].upper() == artist.upper():
                return hit["result"]["primary_artist"]["id"]

    def get_top_songs(self, artist_id):
        url = "https://api.genius.com/artists/" + str(artist_id) + "/songs?access_token=CLIENT_ACCESS_TOKEN&sort=popularity"
        response = self.call_endpoint(url)
        songs = []
        for song_info in response["response"]["songs"]:
            song_id = song_info["id"]
            song_title = song_info["title"]
            song = Song(song_id, song_title)
            songs.append(song)
        return songs

    def call_endpoint(self, url):
        url = url.replace("CLIENT_ACCESS_TOKEN", self.client_access_token)
        raw_response = requests.get(url)
        jsn = json.loads(raw_response.text)
        return jsn

class Song():
    def __init__(self, song_id, song_title):
        self.song_id = song_id
        self.song_title = song_title

if __name__ == "__main__":
    run()
