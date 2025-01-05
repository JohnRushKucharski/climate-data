'''Tests the countries module.'''

import unittest

from climate_data.countries import get_country_bounding_box

class TestCountries(unittest.TestCase):
    '''Tests the countries module.'''	
    def test_get_country_bounding_box(self):
        '''Tests the get_country_bounding_box function.'''	
        bbox = get_country_bounding_box("Laos")
        self.assertEqual(bbox, [100, 13, 108, 23])
