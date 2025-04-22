# app.py
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        return f"Error serving index.html: {str(e)}", 500

@app.route('/result')
def result():
    try:
        return send_from_directory(app.static_folder, 'result.html')
    except Exception as e:
        return f"Error serving result.html: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
