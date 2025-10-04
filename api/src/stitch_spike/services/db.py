from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv

# import .env settings
load_dotenv()
POC_DB_PORT = getenv("POC_DB_PORT", "5432")

# Define database connection string
DATABASE_URL = "postgresql://postgres:postgres@db:" + POC_DB_PORT + "/poc"
# Set up SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
