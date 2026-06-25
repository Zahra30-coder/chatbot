import sqlite3

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
SELECT title, company
FROM jobs
""")

for row in cursor.fetchall():
    print(row)

print(cursor.fetchall())

conn.close()