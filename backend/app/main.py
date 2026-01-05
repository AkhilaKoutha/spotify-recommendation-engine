from fastapi import FastAPI

app = FastAPI(title="Spotify Recommendation API", version="1.0.0")

@app.get("/")
def health():
    return {"status": "ok"}