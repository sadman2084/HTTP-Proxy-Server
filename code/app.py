
from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    if not url.startswith('http://') and not url.startswith('https://'):
        return "Invalid URL"
    try:
        resp = requests.get(url)
        return resp.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
