import requests


def fetch_remoteok_jobs():

    url = "https://remoteok.com/api"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    data = response.json()

    jobs = []

    for item in data[1:]:

        jobs.append({
            "title": item.get("position"),
            "company": item.get("company"),
            "location": item.get("location"),
            "job_url": item.get("url"),
            "description": item.get(
                "description", ""
            )
        })

    return jobs