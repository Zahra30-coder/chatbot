from app.database.db import SessionLocal
from app.database.models import Job


def save_job(
    title,
    company,
    location,
    job_url,
    description
):
    db = SessionLocal()

    existing = (
        db.query(Job)
        .filter(Job.job_url == job_url)
        .first()
    )

    if existing:
        return False

    job = Job(
        title=title,
        company=company,
        location=location,
        job_url=job_url,
        description=description,
        match_score=0,
        status="NEW"
    )

    db.add(job)
    db.commit()

    return True