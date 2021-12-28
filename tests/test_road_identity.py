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
