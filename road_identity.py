import os
import googlemaps

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))

def reverse_geocode(lat, lon):
    return gmaps.reverse_geocode((lat, lon))

def get_street(lat, lon):
    """
    https://googlemaps.github.io/google-maps-services-java/v0.1.3/javadoc/com/google/maps/model/AddressType.html
    """
    geocodes = reverse_geocode(lat, lon)
    try:
        for geocode in geocodes:
            type = geocode['types'][0]
            if type == 'street_address':
                potential_address = geocode['address_components'][1]['long_name']
                return potential_address
            elif type == 'premise':
                potential_address = geocode['address_components'][1]['long_name']
                return potential_address
            elif type == 'route':
                potential_address = geocodes['address_components'][0]['long_name']
                return potential_address
    except:
        print("the geocodes are:")
        for i in range(len(geocodes)):
            print(f"{i}: {geocodes[i]}")
