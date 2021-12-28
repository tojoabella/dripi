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
        road type: street_adress
        '''
        lat, lon = 21.352688, -158.079959
        expected_result = 'Kapolei'
        actual_result = locationIdentifiers.get_city(lat, lon)
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
        expected_result = 'North Nimitz Highway'
        actual_result = locationIdentifiers.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_road_2(self):
        '''
        road type: premise
        '''
        lat, lon = 21.364855, -158.075853
        expected_result = 'Pueonani Street'
        actual_result = locationIdentifiers.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)
    
    def test_road_3(self):
        '''
        road type: route
        '''
        lat, lon = 21.357599, -157.931699
        expected_result = 'Queen Liliuokalani Freeway'
        actual_result = locationIdentifiers.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)