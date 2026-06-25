from app.services.pdf_reader import extract_text
from app.services.matcher import score_job

resume = extract_text(
    "ZahraH ML Resume 25thApril '26.pdf"
)

job_description= """
Python
Machine Learning
LLMs
FastAPI
AI
Backend
SQL
RAG
Agentic AI
Agentic RAG
Azure
Azure ML
DevOps
MLOps
"""

score = score_job(
    resume,
    job_description
)

print(score)