from services.modes_microservice.lib.gmaps_api import GMaps


class locationIdentifiers:
    """
    https://googlemaps.github.io/google-maps-services-java/v0.1.3/javadoc/com/google/maps/model/AddressType.html
    """
    def __init__(self):
        pass

    @staticmethod
    def get_all_localities(lat, lon):
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            current_localities = []
            for geocode in geocodes:
                for address in geocode['address_components']:
                    if address['types'][0] == 'locality':
                        potential_address = address['long_name']
                        if potential_address not in current_localities:
                            current_localities.append(potential_address)
            return current_localities
        except:
            print("FAILED GET_ALL_LOCALITIES ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")
    
    @staticmethod
    def get_all_roads(lat, lon):
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            current_routes = []
            for geocode in geocodes:
                type = geocode['types'][0]
                if type == 'route' or type == 'street_address' or type == 'premise':
                    for address in geocode['address_components']:
                        if 'route' in address['types']:
                            potential_address = address['long_name']
                            if potential_address not in current_routes:
                                current_routes.append(potential_address)
            return current_routes
        except:
            print("FAILED GET_ALL_ROADS ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")

    @staticmethod
    def get_city(lat, lon):
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            for geocode in geocodes:
                if 'locality' in geocode['types']:
                    potential_address = geocode['address_components'][0]['long_name']
            return potential_address
        except:
            print("FAILED GET_CITY ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
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
            print("FAILED GET_NEIGHBORHOOD ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
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
            print("FAILED GET_ROAD ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")                

print(locationIdentifiers.get_all_roads(21.364537, -158.076410))