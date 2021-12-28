import unittest
import services.modes_microservice.lib.city_identity as city_identity

class TestRoadIdentity(unittest.TestCase):

    def test_1(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.300425, -157.829691
        expected_result = 'Honolulu'
        actual_result = city_identity.get_city(lat, lon)
        self.assertEqual(actual_result, expected_result)

    def test_2(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.352688, -158.079959
        expected_result = 'Kapolei'
        actual_result = city_identity.get_city(lat, lon)
        self.assertEqual(actual_result, expected_result)