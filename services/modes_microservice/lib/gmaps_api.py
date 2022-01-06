
import os
import googlemaps


class GMaps:
    gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))
    def __init__(self):
        pass
    
    @classmethod
    def reverse_geocode(cls, lat, lon):
        """
        from a lat/lng point to a list of geocodes for that point

        :return list of dictionaries:
            {
                'address_components': list of dictionaries: {
                    'long_name': string
                    'short_name': string
                    'types': list of string
                },
                'formatted_address': string,
                'geometry': dictionary,
                'place_id': string,
                'plus_code': string,
                'global_code': string,
                'types': list of string
            }
        """
        return cls.gmaps.reverse_geocode((lat, lon))

    @classmethod
    def reverse_geocode_place_id(cls, place_id):
        """
        from a place_id to its geocode (single geocode in list)

        :return list of dictionaries:
            {
                'address_components': list of dictionaries: {
                    'long_name': string
                    'short_name': string
                    'types': list of string
                },
                'formatted_address': string,
                'geometry': dictionary,
                'place_id': string,
                'plus_code': string,
                'global_code': string,
                'types': list of string
            }
        """
        return cls.gmaps.reverse_geocode(place_id)
    
    @classmethod
    def geocode(cls, address):
        """
        from an address to a geocode

        :param string address: a route. ie. Queen Liliuokalani Freeway

        :return : a geocode of that address
        """
        return cls.gmaps.geocode(address)

    
    @classmethod
    def snap_to_roads(cls, points):
        """
        :param list of tuples of floats points:
            e.g. [(21.529143, -158.039847), (21.545911, -158.045314)]
        """
        return cls.gmaps.snap_to_roads(points)
    

li = [(21.529143, -158.039847), (21.545911, -158.045314)]
print(GMaps.snap_to_roads(li))