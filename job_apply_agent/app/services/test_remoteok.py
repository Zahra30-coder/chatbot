from app.services.scrapers.remoteok_scraper import (
    fetch_remoteok_jobs
)

jobs = fetch_remoteok_jobs()

print(len(jobs))

print(jobs[:3])