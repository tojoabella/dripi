
import os
import googlemaps


class GMaps:
    gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))
    def __init__(self):
        pass
    
    @classmethod
    def reverse_geocode(cls, lat, lon):
        """
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
