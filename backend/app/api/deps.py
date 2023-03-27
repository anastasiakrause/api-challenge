from typing import Generator

from app.db.session import SessionLocal

# Grab current db Session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()