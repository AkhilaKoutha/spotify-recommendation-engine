import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://spotify:spotify@postgres:5432/spotify_ai")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class BaseModel(Base):
    __tablename__ = "base_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))