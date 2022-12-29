import os
import requests
import random

from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

playlist_ids = [
    "37i9dQZF1DXbYM3nMM0oPk",
    "37i9dQZF1DX4WYpdgoIcn6",
    "37i9dQZF1DWXRqgorJj26U",
    "37i9dQZF1DX62Nfha2yFhL",
    "37i9dQZF1DX4VvfRBFClxm",
    "37i9dQZF1DX9qNs32fujYe",
    "37i9dQZF1DWYnwbYQ5HnZU",
    "37i9dQZF1DWXbttAJcbphz",
    "37i9dQZF1DX9tPFwDMOaN1",
    "37i9dQZEVXbNG2KDcFcKOF",
    "37i9dQZF1DWXtlo6ENS92N",
    "37i9dQZF1DXaKIA8E7WcJj",
    "37i9dQZF1DX2pSTOxoPbx9",
    "37i9dQZF1DWWjGdmeTyeJ6",
    "37i9dQZF1DX4pAtJteyweQ",
]


def get_spotify_token() -> str:
    """
    Function to retrieve a Spotify access token
    """
    SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
    SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

    payload = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials",
    }

    END_POINT = "https://accounts.spotify.com/api/token"

    response = requests.post(
        END_POINT, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET), data=payload
    )

    return response.json()["access_token"]


def get_random_song() -> dict:
    ACCESS_TOKEN = get_spotify_token()
    random.shuffle(playlist_ids)
    random_playlist_id = random.choice(playlist_ids)

    PLAYIST_URL = f"https://api.spotify.com/v1/playlists/{random_playlist_id}/tracks"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(PLAYIST_URL, headers=headers)

    song_details = {}
    if response.status_code == 200:
        songs = response.json()["items"]
        random.shuffle(songs)
        random_song = random.choice(songs)["track"]
        # print(random_song)
        song_details = {
            "track_id": random_song["id"],
            "title": random_song["name"],
            "artist": [artist["name"] for artist in random_song["artists"]],
            "cover_img": random_song["album"]["images"][0]["url"],
            "preview_url": random_song["preview_url"] or "",
            "spotify_url": random_song["external_urls"]["spotify"],
        }

    return song_details
