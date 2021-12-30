from services.modes_microservice.lib.gmaps_api import GMaps


class locationIdentifiers:
    """
    https://googlemaps.github.io/google-maps-services-java/v0.1.3/javadoc/com/google/maps/model/AddressType.html
    """
    def __init__(self):
        pass

    @staticmethod
    def get_all_localities(lat, lon, printall=False):
        """
        :return list of string current_localities:
        """
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            if printall:
                for i in range(len(geocodes)):
                    print(f"{i}: {geocodes[i]}")

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
    def get_all_roads(lat, lon, format=None, printall=False):
        """
        gets all roads

        :param lat: latitude
        :param lon: longitude
        :param format: None or 'detailed'
        :param bool printall: whether to print all geocodes

        :return list current_routes:
            if format is None: list of string (e.g. ['Farrington Highway', 'Queen Liliuokalani Freeway', 'Kamehameha Highway'])
            if format == 'detailed': list of dict (e.g. ['Kamehameha Highway': (place_id)])
        """
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            current_routes = []
            if format is None:
                for geocode in geocodes:
                    type = geocode['types'][0]
                    if type == 'route' or type == 'street_address' or type == 'premise':
                        for address in geocode['address_components']:
                            if 'route' in address['types']:
                                print(geocode)
                                potential_address = address['long_name']
                                if potential_address not in current_routes:
                                    current_routes.append(potential_address)
            elif format == 'detailed':
                for geocode in geocodes:
                    if 'route' in geocode['types']:
                        for address in geocode['address_components']:
                            if 'route' in address['types']:
                                potential_address = address['long_name']
                                place_id = geocode['place_id']
                                tmp_dict = {potential_address: place_id}
                                if tmp_dict not in current_routes:
                                    current_routes.append(tmp_dict)
            if printall:
                for i in range(len(geocodes)):
                    print(f"{i}: {geocodes[i]}")
            return current_routes
        except:
            print("FAILED GET_ALL_ROADS ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")
    
    @staticmethod
    def get_road(lat, lon, printall=False):
        """
        get the road related to the geocode that has type 'route'. Most likely only one road even if overlapping roads (i.e. 21.396117, -157.984485)

        :return dict: 
            {
                (road_name): (place_id)
            }
        """
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            if printall:
                for i in range(len(geocodes)):
                    print(f"{i}: {geocodes[i]}")

            for geocode in geocodes:
                if 'route' in geocode['types']:
                    for address in geocode['address_components']:
                        if 'route' in address['types']:
                            print(geocode)
                            potential_address = address['long_name']
                            break
                    place_id = geocode['place_id']
                    return {potential_address: place_id}
        except:
            print("FAILED GET_ROAD ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")
    
    @staticmethod
    def get_neighborhood(lat, lon, printall=False):
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            if printall:
                for i in range(len(geocodes)):
                    print(f"{i}: {geocodes[i]}")

            for geocode in geocodes:
                if 'neighborhood' in geocode['types']:
                    potential_address = geocode['address_components'][0]['long_name']
                    return potential_address
        except:
            print("FAILED GET_NEIGHBORHOOD ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")



    """
    DEPRECATED
    """
    @staticmethod
    def get_city(lat, lon):
        """
        DON'T USE
        """
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
    def get_road_v2(lat, lon):
        """
        DON'T USE: the address that corresponds to each road has a different place_id
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
            print("FAILED GET_ROAD ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")       

    @staticmethod
    def get_all_roads_v2(lat, lon):
        """
        :return current_routes: list of dict
            {
                (road_name): (place_id)
            }
        
        DON'T USE
        """
        geocodes = GMaps.reverse_geocode(lat, lon)
        try:
            current_routes = []
            for geocode in geocodes:
                type = geocode['types'][0]
                if type == 'route' or type == 'street_address' or type == 'premise':
                    for address in geocode['address_components']:
                        if 'route' in address['types']:
                            potential_address = address['long_name']
                            place_id = geocode['place_id']
                            tmp_dict = {potential_address: place_id}
                            if tmp_dict not in current_routes:
                                current_routes.append(tmp_dict)
            return current_routes
        except:
            print("FAILED GET_ALL_ROADS ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")         

li = locationIdentifiers.get_all_roads(21.390231, -157.961168)
print(li)
