from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="../static")
cors = CORS(app)
app.config.from_object('config')

@app.route('/')
def index():
    return send_from_directory('../static', 'index.html')

@app.route('/<path:path>')
def serve(path):
    return send_from_directory('../static', path)

from app.controllers import questions