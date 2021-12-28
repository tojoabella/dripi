from flask import Flask, Response, request
from flask_cors import CORS
import logging

from services.modes_microservice.lib.location_identifiers import locationIdentifiers


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
    return f"""hello and welcome to dripi
    hi"""

@app.route('/get_city', methods=['GET'])
def get_city():
    """
    get city
    """
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    res = locationIdentifiers.get_city(lat, lng)
    if res is None:
        return "None"
    return res

@app.route('/get_neighborhood', methods=['GET'])
def get_neighborhood():
    """
    get neighborhood
    """
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    res = locationIdentifiers.get_neighborhood(lat, lng)
    if res is None:
        return "None"
    return res

@app.route('/get_road', methods=['GET'])
def get_road():
    """
    get road
    """
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    res = locationIdentifiers.get_road(lat, lng)
    if res is None:
        return "None"
    return res

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)
