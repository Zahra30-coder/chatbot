from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

#DATABASE_URL = "sqlite:///jobs.db"
BASE_DIR = Path(__file__).resolve().parents[2]   # job_apply_agent folder

DATABASE_URL = f"sqlite:///{BASE_DIR / 'jobs.db'}"

print("Current working directory:", Path.cwd())
print("Database URL:", DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)