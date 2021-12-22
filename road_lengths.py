import os
from datetime import datetime
import googlemaps

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))
s