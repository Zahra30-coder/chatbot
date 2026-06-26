from sqlalchemy import Column, Integer, String, Float, Text, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    job_url = Column(String, unique=True)
    description = Column(Text)
    experience = Column(Integer)
    employment_type = Column(String, nullable=True)
    skills = Column(String)
    match_score = Column(Float)
    posted_date = Column(String)
    application_status = Column(String, default="Not Applied")