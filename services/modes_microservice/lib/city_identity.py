from services.modes_microservice.lib.gmaps_api import GMaps

def get_city(lat, lon):
    """
    https://googlemaps.github.io/google-maps-services-java/v0.1.3/javadoc/com/google/maps/model/AddressType.html
    """
    geocodes = GMaps.reverse_geocode(lat, lon)
    try:
        for geocode in geocodes:
            type = geocode['types'][0]
            if type == 'locality':
                potential_address = geocode['address_components'][0]['long_name']
                return potential_address
    except:
        print("FAILED CITY_IDENTITY ATTEMPT")
        print("the geocodes are:")
        for i in range(len(geocodes)):
            print(f"{i}: {geocodes[i]}")
