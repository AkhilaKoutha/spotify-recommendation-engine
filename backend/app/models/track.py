from sqlalchemy import Column, String, Float
from app.db.session import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)

    energy = Column(Float)
    valence = Column(Float)
    danceability = Column(Float)
    tempo = Column(Float)
