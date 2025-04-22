from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List

app = FastAPI()

@app.post("/process")
async def process_files(files: List[UploadFile] = File(...)):
    if len(files) != 3:
        raise HTTPException(status_code=400, detail="Exactly 3 PDFs required")
    for file in files:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDFs allowed")
    # Placeholder: Simulate processing, return dummy download URL
    return {"download_url": "http://localhost:8000/dummy_output.pdf"}