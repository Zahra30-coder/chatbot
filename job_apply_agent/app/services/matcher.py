from app.services.gemini_service import model

def score_job(resume_text, job_description):
    prompt = f"""

    Compare the resume with the job

    Resume:
    {resume_text}

    Job:
    {job_description}

    Return ONLY a score from 0 to 100
    """

    response = model.generate_content(
    prompt
    )
    
    return response.text