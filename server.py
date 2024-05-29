from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    url = 'http://localhost:11434/api/chat'
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=data, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)