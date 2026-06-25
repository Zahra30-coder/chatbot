from app.services.job_fetcher import fetch_jobs
from app.services.job_service import save_job


def run_job_finder():

    jobs = fetch_jobs()

    for job in jobs:

        save_job(
            title=job["title"],
            company=job["company"],
            location=job["location"],
            job_url=job["job_url"],
            description=job["description"]
        )

    print(f"{len(jobs)} jobs saved")