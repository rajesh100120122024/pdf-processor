from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Template error: {str(e)}", 500

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    if len(files) != 3:
        return 'Please upload exactly 3 PDFs', 400

    fastapi_url = 'http://localhost:8000/process'  # Update this if backend is deployed elsewhere
    files_data = [('files', (f.filename, f, 'application/pdf')) for f in files]

    try:
        response = requests.post(fastapi_url, files=files_data)
        if response.status_code == 200:
            download_url = response.json().get('download_url')
            return render_template('result.html', download_url=download_url)
        return 'Processing failed', 500
    except requests.RequestException as e:
        return f"Error connecting to backend: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
