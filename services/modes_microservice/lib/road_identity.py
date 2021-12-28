from services.modes_microservice.lib.gmaps_api import GMaps

def get_road(lat, lon):
    """
    https://googlemaps.github.io/google-maps-services-java/v0.1.3/javadoc/com/google/maps/model/AddressType.html
    """
    geocodes = GMaps.reverse_geocode(lat, lon)
    try:
        for geocode in geocodes:
            type = geocode['types'][0]
            if type == 'route':
                print('route')
                potential_address = geocode['address_components'][0]['long_name']
                return potential_address
            elif type == 'street_address':
                print('street_adress')
                potential_address = geocode['address_components'][1]['long_name']
                return potential_address
            elif type == 'premise':
                print('premise')
                potential_address = geocode['address_components'][1]['long_name']
                return potential_address
            elif type == 'plus_code' or type == 'neighborhood' or type == 'postal_code' or type == 'locality' or type == 'administrative_area_level_1' or type == 'administrative_area_level_2' or type == 'country':
                break
    except:
        print("FAILED ROAD_IDENTITY ATTEMPT")
        print("the geocodes are:")
        for i in range(len(geocodes)):
            print(f"{i}: {geocodes[i]}")
