from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URI = "sqlite:///vehicle_data.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args = {"check_same_thread": False}
)

# Create session that will be propogated to different areas of the app
SessionLocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine)