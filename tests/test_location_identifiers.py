import unittest
from unittest.case import expectedFailure
from services.modes_microservice.lib.location_identifiers import locationIdentifiers

class TestLocationIdentity(unittest.TestCase):
    def test_city_1(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.300425, -157.829691
        expected_result = 'Honolulu'
        actual_result = locationIdentifiers.get_city(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_city_2(self):
        '''
        geocodes are just waianae
        '''
        lat, lon = 21.446484, -158.170989
        expected_result = 'Waianae'
        actual_result = locationIdentifiers.get_city(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_all_localities_1(self):
        '''
        geocodes have both nanakuli and waianae.
        seems like nanakuli is both in waianae and different area than waianae
        '''
        lat, lon = 21.407290, -158.138380
        expected_result = ['Nānākuli', 'Waianae']
        actual_result = locationIdentifiers.get_all_localities(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_get_all_localities_2(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.352688, -158.079959
        expected_result = ['Kapolei', 'Makakilo']
        actual_result = locationIdentifiers.get_all_localities(lat, lon)
        self.assertEqual(actual_result, expected_result)
    
    def test_all_localities_3(self):
        '''
        geocodes are just waianae
        '''
        lat, lon = 21.446484, -158.170989
        expected_result = ['Waianae']
        actual_result = locationIdentifiers.get_all_localities(lat, lon)
        self.assertEqual(actual_result, expected_result)
    
    def test_neighborhood_1(self):
        lat, lon = 21.340514, -157.885905
        expected_result = 'Moanalua'
        actual_result = locationIdentifiers.get_neighborhood(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_road_1(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.321789, -157.879638
        expected_result = {'North Nimitz Highway': 'ChIJqw2z7mduAHwRxMwx2Bitfmk'}
        actual_result = locationIdentifiers.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_road_2(self):
        '''
        road type: premise
        '''
        lat, lon = 21.364855, -158.075853
        expected_result = {'Pueonani Street': 'ChIJI72m1qNjAHwRkCTjfgwBQm4'}
        actual_result = locationIdentifiers.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)
    
    def test_road_3(self):
        '''
        road type: route
        '''
        lat, lon = 21.357599, -157.931699
        expected_result = {'Queen Liliuokalani Freeway': 'ChIJiddTXWxvAHwRyvkjE7TtuWI'}
        actual_result = locationIdentifiers.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)