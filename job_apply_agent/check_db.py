import sqlite3
#python -c "from sqlalchemy import inspect; from app.database.db import engine; print(inspect(engine).get_table_names())"
#['jobs']

#Open DB Browser for SQLite
#Click Open Database
#Select:
#D:\CHATBOT\JOB_APPLY_AGENT\jobs.db
#Go to Browse Data
#Select the jobs table

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

cursor.execute("""
SELECT title, company, location, job_url, description, experience, employment_type, skills, match_score, posted_date, application_status
FROM jobs
""")

for row in cursor.fetchall():
    print(row)

tables = print(cursor.fetchall())

print("Tables:")
print(tables)

conn.close()