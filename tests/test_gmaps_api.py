import unittest
from services.modes_microservice.lib.location_identifiers import GMaps

class TestGMaps(unittest.TestCase):

    def test_snap_to_roads(self):
        li = [(21.529143, -158.039847), (21.545911, -158.045314)]

        expected_result = [{'location': {'latitude': 21.52913092949176, 'longitude': -158.0398908312465}, 'originalIndex': 0, 'placeId': 'ChIJi72emdNdAHwRFCmN1g4esLU'}, 
                            {'location': {'latitude': 21.545920197832345, 'longitude': -158.04528214734293}, 'originalIndex': 1, 'placeId': 'ChIJz8N9dChcAHwRcfV5HGWhU2g'}
                            ]
        actual_result = GMaps.snap_to_roads(li)
        self.assertEqual(actual_result, expected_result)
    