import unittest
import services.modes_microservice.lib.road_lengths as road_lengths


class TestRoadLength(unittest.TestCase):

    def test_1(self):
        '''
        road type: street_adress
        '''
        lat, lon = 21.321789, -157.879638
        expected_result = None #TODO
        actual_result = road_lengths.road_length(lat, lon)
        self.assertEqual(actual_result, expected_result)
