# backend/app.py
from fastapi import FastAPI, File, UploadFile, HTTPException
import pytesseract
from pdf2image import convert_from_bytes
from transformers import pipeline
import io

app = FastAPI()

# Initialize Hugging Face sentiment analysis (placeholder for checkbox/comment detection)
classifier = pipeline("sentiment-analysis")

@app.post("/process")
async def process_files(file1: UploadFile = File(...), file2: UploadFile = File(...), file3: UploadFile = File(...)):
    files = [file1, file2, file3]
    for file in files:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDFs allowed")
    
    extracted_texts = []
    for file in files:
        # Read PDF content
        pdf_content = await file.read()
        # Convert PDF to images
        images = convert_from_bytes(pdf_content)
        # Extract text with Tesseract
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        extracted_texts.append(text)
    
    # Analyze text with Hugging Face (placeholder: sentiment as proxy)
    analysis_results = []
    for text in extracted_texts:
        result = classifier(text[:512])  # Truncate to 512 tokens
        analysis_results.append(result[0])
    
    # Placeholder: Simulate processed PDF response
    return {
        "download_url": "http://localhost:8000/dummy_output.pdf",
        "texts": extracted_texts,
        "analysis": analysis_results
    }
