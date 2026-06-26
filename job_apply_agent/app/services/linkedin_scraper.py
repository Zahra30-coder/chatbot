from playwright.sync_api import sync_playwright

def scrape_jobs():

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(
            "https://www.linkedin.com/jobs/search/?keywords=AI%20Engineer"
        )

        page.wait_for_timeout(5000)

        print(page.title())

        job_cards = page.locator(".base-card")

        count = job_cards.count()

        print(f"Found {count} job cards")

        for i in range(min(count, 20)):

            card = job_cards.nth(i)

            try:

                title = card.locator(
                    ".base-search-card__title"
                ).inner_text().strip()

                company = card.locator(
                    ".base-search-card__subtitle"
                ).inner_text().strip()

                location = card.locator(
                    ".job-search-card__location"
                ).inner_text().strip()

                job_url = card.locator(
                    "a"
                ).first.get_attribute("href")

                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "job_url": job_url 
                })

            except Exception as e:
                print(f"Skipped card: {e}")

        browser.close()

    return jobs