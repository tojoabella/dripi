import unittest
from services.modes_microservice.lib.gmaps_api import GMaps

class TestGMaps(unittest.TestCase):

    def test_snap_to_roads(self):
        li = [(21.529143, -158.039847), (21.545911, -158.045314)]

        expected_result = [{'location': {'latitude': 21.52913092949176, 'longitude': -158.0398908312465}, 'originalIndex': 0, 'placeId': 'ChIJi72emdNdAHwRFCmN1g4esLU'}, 
                            {'location': {'latitude': 21.545920197832345, 'longitude': -158.04528214734293}, 'originalIndex': 1, 'placeId': 'ChIJz8N9dChcAHwRcfV5HGWhU2g'}
                            ]
        actual_result = GMaps.snap_to_roads(li)
        self.assertEqual(actual_result, expected_result)
    
    def test_snap_to_roads_2(self):
        '''
        one way street
        '''
        li = [(40.805297, -73.963433), (40.805861, -73.964760)]
        expected_result = [{'location': {'latitude': 40.8052956071465, 'longitude': -73.96343402498748}, 
                            'originalIndex': 0, 
                            'placeId': 'ChIJhRX3Pzz2wokRMIb20Q8Ervc'}, 
                            {'location': {'latitude': 40.8058066, 'longitude': -73.964646}, 
                            'placeId': 'ChIJhRX3Pzz2wokRMIb20Q8Ervc'}, 
                            {'location': {'latitude': 40.8058066, 'longitude': -73.964646}, 
                            'placeId': 'ChIJzdugDjz2wokR4A-FQcO1vqA'}, 
                            {'location': {'latitude': 40.80585614034125, 'longitude': -73.96476357390948}, 
                            'originalIndex': 1, 
                            'placeId': 'ChIJzdugDjz2wokR4A-FQcO1vqA'}]
        actual_result = GMaps.snap_to_roads(li)
        self.assertEqual(actual_result, expected_result)

        li = [(40.805861, -73.964760), (40.805297, -73.963433)]
        expected_result = [{'location': {'latitude': 40.8058066, 'longitude': -73.964646}, 
                            'originalIndex': 0, 
                            'placeId': 'ChIJhRX3Pzz2wokRMIb20Q8Ervc'}]
        actual_result = GMaps.snap_to_roads(li)
        self.assertEqual(actual_result, expected_result)
    
    def test_nearest_roads(self):
        li = [(21.365566, -158.080033)]
        expected_result = [{'location': {'latitude': 21.36563563983145, 'longitude': -158.0800802076825}, 
                            'originalIndex': 0, 
                            'placeId': 'ChIJK_czJaRjAHwRHMxmchZM38w'}]
        actual_result = GMaps.snap_to_roads(li)
        self.assertEqual(actual_result, expected_result)
    
    def test_reverse_geocode_place_id(self):
        id = 'ChIJK_czJaRjAHwRHMxmchZM38w'
        expected_result = [{'address_components': [{'long_name': 'Makakilo Drive', 'short_name': 'Makakilo Dr', 'types': ['route']}, 
                                                   {'long_name': 'Kapolei', 'short_name': 'Kapolei', 'types': ['locality', 'political']}, 
                                                   {'long_name': 'Honolulu County', 'short_name': 'Honolulu County', 'types': ['administrative_area_level_2', 'political']}, 
                                                   {'long_name': 'Hawaii', 'short_name': 'HI', 'types': ['administrative_area_level_1', 'political']}, 
                                                   {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, 
                                                   {'long_name': '96707', 'short_name': '96707', 'types': ['postal_code']}], 
                                                   'formatted_address': 'Makakilo Dr, Kapolei, HI 96707, USA', 
                                                   'geometry': {'bounds': {'northeast': {'lat': 21.3660743, 'lng': -158.0791587}, 'southwest': {'lat': 21.3655881, 'lng': -158.080161}}, 
                                                   'location': {'lat': 21.36586939645376, 'lng': -158.0796797459298}, 
                                                   'location_type': 'GEOMETRIC_CENTER', 
                                                   'viewport': {'northeast': {'lat': 21.3671801802915, 'lng': -158.0783108697085}, 'southwest': {'lat': 21.3644822197085, 'lng': -158.0810088302915}}}, 
                                                   'place_id': 'ChIJK_czJaRjAHwRHMxmchZM38w', 
                                                   'types': ['route']}]
        actual_result = GMaps.reverse_geocode_place_id(id)
        self.assertEqual(actual_result, expected_result)