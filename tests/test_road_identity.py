import unittest
import services.modes_microservice.lib.road_identity as road_identity

class TestRoadIdentity(unittest.TestCase):

    def test_1(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.321789, -157.879638
        expected_result = 'North Nimitz Highway'
        actual_result = road_identity.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_2(self):
        '''
        road type: premise
        '''
        lat, lon = 21.364855, -158.075853
        expected_result = 'Pueonani Street'
        actual_result = road_identity.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)
    
    def test_3(self):
        '''
        road type: route
        '''
        lat, lon = 21.357599, -157.931699
        expected_result = 'Queen Liliuokalani Freeway'
        actual_result = road_identity.get_road(lat, lon)
        self.assertEqual(actual_result, expected_result)
