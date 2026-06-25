from app.database.db import SessionLocal
from app.database.models import Job

def get_all_jobs():
    db = SessionLocal()
    jobs = db.query(Job).all()
    return jobs