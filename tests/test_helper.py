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
    
    def test_direction_finder_1(self):
        expected_result = None
        actual_result = helper.direction_finder_deg(0, 0, 0, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_2(self):
        expected_result = 0.0
        actual_result = helper.direction_finder_deg(1, 0, 0, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_3(self):
        expected_result = 45
        actual_result = helper.direction_finder_deg(1,1,0,0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_4(self):
        expected_result = 90
        actual_result = helper.direction_finder_deg(0,1,0,0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_5(self):
        expected_result = 135
        actual_result = helper.direction_finder_deg(-1, 1,0,0)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_6(self):
        expected_result = 180
        actual_result = helper.direction_finder_deg(-1, 0,0,0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_7(self):
        expected_result = 225
        actual_result = helper.direction_finder_deg(-1, -1,0,0)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_8(self):
        expected_result = 270
        actual_result = helper.direction_finder_deg(0, -1,0,0)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_9(self):
        expected_result = 315
        actual_result = helper.direction_finder_deg(1, -1,0,0)
        self.assertEqual(actual_result, expected_result)