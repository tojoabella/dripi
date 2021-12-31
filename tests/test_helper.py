import unittest
import services.modes_microservice.lib.helper as helper

class TestHelper(unittest.TestCase):
    def test_1(self):
        '''
        N 100
        '''
        direction = 'N'
        distance = 100
        expected_result = (100, 0)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)

    def test_2(self):
        '''
        NE 100
        '''
        direction = 'NE'
        distance = 100
        expected_result = (70.71067811865474, 70.71067811865474)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_3(self):
        '''
        E 100
        '''
        direction = 'E'
        distance = 100
        expected_result = (0, 100)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_4(self):
        '''
        SE
        '''
        direction = 'SE'
        distance = 100
        expected_result = (-70.71067811865474, 70.71067811865474)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_5(self):
        '''
        S
        '''
        direction = 'S'
        distance = 100
        expected_result = (-100, 0)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_6(self):
        '''
        SW
        '''
        direction = 'SW'
        distance = 100
        expected_result = (-70.71067811865474, -70.71067811865474)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_7(self):
        '''
        W
        '''
        direction = 'W'
        distance = 100
        expected_result = (0, -100)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_8(self):
        '''
        NW
        '''
        direction = 'NW'
        distance = 100
        expected_result = (70.71067811865474, -70.71067811865474)
        actual_result = helper.vector_decomposition(distance, direction)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_1(self):
        expected_result = None
        actual_result = helper.direction_finder(0, 0, 0, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_2(self):
        expected_result = 0.0
        actual_result = helper.direction_finder(0, 0, 1, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_3(self):
        expected_result = 45
        actual_result = helper.direction_finder(0, 0, 1, 1)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_4(self):
        expected_result = 90
        actual_result = helper.direction_finder(0, 0, 0, 1)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_5(self):
        expected_result = 135
        actual_result = helper.direction_finder(0, 0, -1, 1)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_6(self):
        expected_result = 180
        actual_result = helper.direction_finder(0, 0, -1, 0)
        self.assertEqual(actual_result, expected_result)
    
    def test_direction_finder_7(self):
        expected_result = 225
        actual_result = helper.direction_finder(0, 0, -1, -1)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_8(self):
        expected_result = 270
        actual_result = helper.direction_finder(0, 0, 0, -1)
        self.assertEqual(actual_result, expected_result)

    def test_direction_finder_9(self):
        expected_result = 315
        actual_result = helper.direction_finder(0, 0, 1, -1)
        self.assertEqual(actual_result, expected_result)
