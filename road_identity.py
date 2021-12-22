import os
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))

def reverse_geocode(lat, lon):
    return gmaps.reverse_geocode((lat, lon))
