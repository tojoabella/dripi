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
        get all localities

        :param bool printall: whether to print all geocodes
        :param float lat: latitude
        :param float lon: longitude

        :return list of string: all localities
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
                        address_name = address['long_name']
                        if address_name not in current_localities:
                            current_localities.append(address_name)
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
            if format is None: 
                list of string (e.g. ['Farrington Highway', 'Queen Liliuokalani Freeway', 'Kamehameha Highway'])
            if format == 'detailed': 
                list of dict (e.g. ['Kamehameha Highway': (place_id)])
                Note: place_id is the place_id for the address that has type: ['routes']
                currently potentially all addresses of type 'routes' for all geocodes of type 'routes' because place_id must be for a geocode with type route
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
                                address_name = address['long_name']
                                if address_name not in current_routes:
                                    current_routes.append(address_name)
            elif format == 'detailed':
                for geocode in geocodes:
                    if 'route' in geocode['types']:
                        for address in geocode['address_components']:
                            if 'route' in address['types']:
                                address_name = address['long_name']
                                place_id = geocode['place_id']
                                tmp_dict = {'name': address_name,
                                            'id': place_id}
                                #address_name: place_id}
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
             'name': road_name,
             'id': place_id
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
                            address_name = address['long_name']
                            break
                    place_id = geocode['place_id']
                    return {'name': address_name,
                            'id': place_id}
                    #return {address_name: place_id}
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
                    address_name = geocode['address_components'][0]['long_name']
            return address_name
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
                    address_name = geocode['address_components'][0]['long_name']
                    return address_name
                elif type == 'street_address':
                    print('street_adress')
                    address_name = geocode['address_components'][1]['long_name']
                    return address_name
                elif type == 'premise':
                    print('premise')
                    address_name = geocode['address_components'][1]['long_name']
                    return address_name
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
                            address_name = address['long_name']
                            place_id = geocode['place_id']
                            tmp_dict = {address_name: place_id}
                            if tmp_dict not in current_routes:
                                current_routes.append(tmp_dict)
            return current_routes
        except:
            print("FAILED GET_ALL_ROADS ATTEMPT")
            print(f"the ({lat}, {lon}) the geocodes are:")
            for i in range(len(geocodes)):
                print(f"{i}: {geocodes[i]}")         

