from app.database.db import SessionLocal
from app.database.models import Job

db = SessionLocal()

job = Job(
    title="AI Engineer",
    company="OpenAI",
    location="Remote",
    job_url="https://example.com/job1",
    description="Test Job",
    match_score=0,
    status="NEW"
)

db.add(job)
db.commit()

print("Job inserted successfully")