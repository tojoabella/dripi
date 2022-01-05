import unittest
import services.modes_microservice.lib.road_lengths as road_lengths
import math
    
class TestRoadLength(unittest.TestCase):
    def test_vector_decomposition_1(self):
        '''
        N 100
        '''
        direction = 0
        distance = 100
        expected_result = (100, 0)
        actual_result = road_lengths.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)

    def test_vector_decomposition_2(self):
        '''
        NE 100
        '''
        direction = math.pi/4
        distance = 100
        expected_result = (71, 71)
        dy, dx = road_lengths.vector_decomposition(distance, direction)
        self.assertEqual((dy, dx), expected_result)
    
    def test_vector_decomposition_3(self):
        '''
        E 100
        '''
        direction = 90
        distance = 100
        expected_result = (0, 100)
        actual_result = road_lengths.vector_decomposition(distance, direction, dir_deg=True)
        self.assertEqual(actual_result, expected_result)
    
    def test_vector_decomposition_4(self):
        '''
        SE
        '''
        direction = 135
        distance = 100
        expected_result = (-71, 71)
        actual_result = road_lengths.vector_decomposition(distance, direction, dir_deg=True)
        self.assertEqual(actual_result, expected_result)
    
    def test_vector_decomposition_5(self):
        '''
        S
        '''
        direction = math.pi
        distance = 100
        expected_result = (-100, 0)
        actual_result = road_lengths.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_vector_decomposition_6(self):
        '''
        SW
        '''
        direction = 5*math.pi/4
        distance = 100
        expected_result = (-71, -71)
        actual_result = road_lengths.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_vector_decomposition_7(self):
        '''
        W
        '''
        direction = 3*math.pi/2
        distance = 100
        expected_result = (0, -100)
        actual_result = road_lengths.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_vector_decomposition_8(self):
        '''
        NW
        '''
        direction = 315
        distance = 100
        expected_result = (71, -71)
        actual_result = road_lengths.vector_decomposition(distance, direction, dir_deg=True)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_1(self):
        expected_result = None
        actual_result = road_lengths.direction_finder_deg(0, 0, 0, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_2(self):
        expected_result = 0.0
        actual_result = road_lengths.direction_finder_deg(0, 0, 1, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_3(self):
        expected_result = 45
        actual_result = road_lengths.direction_finder_deg(0, 0, 1, 1)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_4(self):
        expected_result = 90
        actual_result = road_lengths.direction_finder_deg(0, 0, 0, 1)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_5(self):
        expected_result = 135
        actual_result = road_lengths.direction_finder_deg(0, 0, -1, 1)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_6(self):
        expected_result = 180
        actual_result = road_lengths.direction_finder_deg(0, 0, -1, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_7(self):
        expected_result = 225
        actual_result = road_lengths.direction_finder_deg(0, 0, -1, -1)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_8(self):
        expected_result = 270
        actual_result = road_lengths.direction_finder_deg(0, 0, 0, -1)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_9(self):
        expected_result = 315
        actual_result = road_lengths.direction_finder_deg(0, 0, 1, -1)
        self.assertEqual(actual_result, expected_result)
