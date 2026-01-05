from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.track import Track

router = APIRouter(prefix="/tracks", tags=["tracks"])

@router.get("/")
def get_tracks():
    db: Session = SessionLocal()
    try:
        tracks = db.query(Track).all()
        return [
            {
                "id": t.id,
                "name": t.name,
                "artist": t.artist,
                "energy": t.energy,
                "valence": t.valence,
                "danceability": t.danceability,
                "tempo": t.tempo,
            }
            for t in tracks
            ]
 
    finally:
        db.close()  
