from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/result')
def result():
    return send_from_directory(app.static_folder, 'result.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Use 5001 if 5000 fails