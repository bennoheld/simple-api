import os
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return '', 200

@app.route('/')
def home():
    return '🚀', 200

if __name__ == '__main__':
    api_host = os.environ.get('API_HOST', '0.0.0.0')
    api_port = os.environ.get('API_PORT', '5003')
    app.run(host=api_host, port=api_port)
    
