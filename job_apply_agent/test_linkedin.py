from app.services.linkedin_scraper import scrape_jobs

jobs = scrape_jobs()

print("\nRESULTS:\n")

for job in jobs[:10]:
    print(job)