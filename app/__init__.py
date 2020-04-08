from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder="../static")
cors = CORS(app)
app.config.from_object('config')

from app.controllers import questions