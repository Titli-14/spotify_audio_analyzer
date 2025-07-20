import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-private",
    cache_path=".cache"
))

def analyze_track(track_id):
    try:
        features = sp.audio_features([track_id])
        if not features or features[0] is None:
            return {"error": "No features found for the track ID."}

        f = features[0]
        return {
            "danceability": f.get("danceability"),
            "energy": f.get("energy"),
            "tempo": f.get("tempo"),
            "valence": f.get("valence"),
            "speechiness": f.get("speechiness"),
            "acousticness": f.get("acousticness"),
            "instrumentalness": f.get("instrumentalness"),
            "liveness": f.get("liveness"),
            "loudness": f.get("loudness")
        }

    except SpotifyException as e:
        return {"error": f"Spotify API error: {str(e)}"}
    
    except Exception as e:
        return {"error": f"Internal error occurred: {str(e)}"}

def extract_track_id(track_input):
    if "open.spotify.com/track/" in track_input:
        return track_input.split("track/")[1].split("?")[0]
    return track_input.strip()
