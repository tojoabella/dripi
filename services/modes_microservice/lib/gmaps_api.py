
import os
import googlemaps


class GMaps:
    gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))
    def __init__(self):
        pass
    
    @classmethod
    def reverse_geocode(cls, lat, lon):
        return cls.gmaps.reverse_geocode((lat, lon))