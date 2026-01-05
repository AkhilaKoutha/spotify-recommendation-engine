from app.db.session import Base, engine
from app.models.track import Track

def init_db():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)