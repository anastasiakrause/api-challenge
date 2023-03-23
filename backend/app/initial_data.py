import logging
from db.base import Base
from db.init_db import init_db
from db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    init_db(db)

def main() -> None:
    logger.info("creating initial data")
    init()
    logger.info("initial data created")

if __name__ == "__main__":
    main()