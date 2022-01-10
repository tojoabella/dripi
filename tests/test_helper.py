import unittest
import math
import services.modes_microservice.lib.helper as helper

class TestHelper(unittest.TestCase):

    def test_radians_to_degrees_1(self):
        rad = 0

        expected_result = 0
        actual_result = helper.radians_to_degrees(rad)
        self.assertEqual(actual_result, expected_result)

    def test_radians_to_degrees_2(self):
        rad = math.pi

        expected_result = 180
        actual_result = helper.radians_to_degrees(rad)
        self.assertEqual(actual_result, expected_result)

    def test_radians_to_degrees_3(self):
        rad = -math.pi

        expected_result = -180
        actual_result = helper.radians_to_degrees(rad)
        self.assertEqual(actual_result, expected_result)
    
    def test_radians_to_degrees_4(self):
        rad = 2*math.pi

        expected_result = 360
        actual_result = helper.radians_to_degrees(rad)
        self.assertEqual(actual_result, expected_result)
    
    def test_radians_to_degrees_5(self):
        rad = 3*math.pi

        expected_result = 540
        actual_result = helper.radians_to_degrees(rad)
        self.assertEqual(actual_result, expected_result)