from services.modes_microservice.lib.gmaps_api import GMaps


class locationIdentifiers:
    """
    https://googlemaps.github.io/google-maps-services-java/v0.1.3/javadoc/com/google/maps/model/AddressType.html
    """
    def __init__(self):
        pass

    @staticmethod
    def get_city(lat, lon):
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            for address in geocodes[0]['address_components']:
                #because gmaps thinks makakilo is a locality
                if 'locality' in address['types']:
                    potential_address = address['long_name']
                    ''' for debugging
                    for geocode in geocodes:
                        print(geocode)
                    '''
                    return potential_address
            for geocode in geocodes:
                if 'locality' in geocode['types'][0]:
                    potential_address = geocode['address_components'][0]['long_name']
                    print(geocode)
                    return potential_address
        except:
            print("FAILED CITY_IDENTITY ATTEMPT")
            print("the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")
    
    @staticmethod
    def get_neighborhood(lat, lon):
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            for geocode in geocodes:
                if 'neighborhood' in geocode['types']:
                    potential_address = geocode['address_components'][0]['long_name']
                    return potential_address
        except:
            print("FAILED NEIGHBORHOOD_IDENTITY ATTEMPT")
            print("the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")
    
    @staticmethod
    def get_road(lat, lon):
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
                

print(locationIdentifiers.get_city(21.448698, -158.169090))