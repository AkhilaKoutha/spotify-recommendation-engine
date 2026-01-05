from fastapi import FastAPI
from app.db.init_db import init_db
from app.loaders.spotify_loader import load_spotify_data

app = FastAPI(title="Music Recommendation API", version="1.0.0")

@app.on_event("startup")
def startup():
    print("Start up event is runnning")
    init_db()
    load_spotify_data()

@app.get("/")
def health():
    return {"status": "ok"}