import streamlit as st
from app.services.job_query import (get_all_jobs)
import pandas as pd

st.title("AI Job Apply Agent")
st.write("Welcome Rockstar Candidate")
st.success("Frontend Connected")    

jobs = get_all_jobs()

data = []

for job in jobs:

    data.append({
        "Title": job.title,
        "Company": job.company,
        "Location": job.location,
        "Status": job.status
    })

st.dataframe(
    pd.DataFrame(data),
    use_container_width=True
)
