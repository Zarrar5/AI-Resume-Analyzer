from typing import List
from fastapi import FastAPI, File, Form, UploadFile
from utils import analyze_resume

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile=File(...), job_description:List[str]=Form(...)):
    result = analyze_resume(file, job_description)
    return result