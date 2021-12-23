import os
import googlemaps

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))

def reverse_geocode(lat, lon):
    return gmaps.reverse_geocode((lat, lon))

def get_street(lat, lon):
    geocodes = reverse_geocode(lat, lon)
    potential_address = geocodes[0]['address_components']
    street = potential_address[1]['long_name']
    print(street)
    return street