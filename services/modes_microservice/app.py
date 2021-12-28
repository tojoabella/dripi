from flask import Flask, Response, request
from flask_cors import CORS
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    """
    a health check
    """
    return "hello and welcome to dripi"

