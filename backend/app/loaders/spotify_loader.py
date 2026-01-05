import json 
from pathlib import Path
from app.db.session import SessionLocal
from app.models.track import Track

DATA_PATH = Path(__file__).parent.parent / "data" / "spotify_sample.json"


def load_spotify_data():
    db = SessionLocal()

    with open(DATA_PATH) as f:
        tracks = json.load(f)

        for t in tracks:
            exists = db.get(Track, t["id"])
            if exists:
                continue

            track = Track(
            id=t["id"],
            name=t["name"],
            artist=t["artist"],
            energy=t["audio_features"]["energy"],
            valence=t["audio_features"]["valence"],
            danceability=t["audio_features"]["danceability"],
            tempo=t["audio_features"]["tempo"],
        )
            db.add(track)

    db.commit()
    db.close()